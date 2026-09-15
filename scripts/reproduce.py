"""Reproduce selected evidence in a temporary copy, preserving archive bytes."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time

from check_archive import check as check_archive
from build_check_index import render, TARGET as INDEX

ROOT=Path(__file__).resolve().parents[1]
MAIN="2026-09-07/3-3-triple-average-research-note"
BINARY="2026-09-07/new-chat-3/averaging_benchmark"
BENCHMARK="2026-09-10/new-chat/outputs/averaging_algorithm_benchmark"


def tasks_for(suite):
    tasks=[]
    def registry(name, arguments, count):
        tasks.append({
            "name":name,"directory":MAIN,
            "argv":[sys.executable,"-B","work/run_verifications.py",*arguments,"--fail-fast"],
            "markers":[f"SUMMARY PASS={count} FAIL=0 SKIP=0"]})
    if suite in ("prime","review"):
        registry("prime-proof",["--profile","prime-proof"],18)
    if suite in ("ternary","review"):
        ids=["n7-n8-complete","n10-complete"]
        if suite=="ternary":
            ids+=["all-dimensions-double-triple-invariant"]
        registry("ternary-bases" if suite=="review" else "ternary",
                 [arg for ident in ids for arg in ("--id",ident)],len(ids))
    if suite in ("general","review"):
        registry("general-endpoint",["--id","even-arity-all-endpoints"],1)
    if suite in ("dyadic","review"):
        tasks.append({"name":"uniform-dyadic-column","directory":MAIN,
            "argv":[sys.executable,"-B","research/prime_arity_padic/verify_uniform_dyadic_column_lifting.py"],
            "markers":['"status": "PASS"','"complete_mod8_parameter_classes": 4096']})
    if suite in ("binary","review"):
        tasks.append({"name":"binary-python","directory":BINARY,
            "argv":[sys.executable,"-B","-m","unittest","discover","-s","tests","-v"],
            "markers":["Ran 19 tests","\nOK"]})
        tasks.append({"name":"binary-javascript","directory":BINARY,
            "argv":["node","tests/test_web.js"],"markers":["All 6 groups passed."]})
    if suite in ("benchmark","review"):
        tasks.append({"name":"ternary-prime-benchmark","directory":BENCHMARK,
            "argv":[sys.executable,"-B","verify_paths.py","--self-check"],
            "markers":["reference paths and known negative control: PASS",
                       "strict rational and invalid-path guards: PASS"]})
    return tasks


def main():
    if sys.flags.optimize:
        raise SystemExit("Do not run mathematical checks with assertions disabled.")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite",choices=["review","prime","ternary","dyadic","general","binary","benchmark"],default="review")
    parser.add_argument("--output-dir",type=Path,default=ROOT/"verification_runs")
    args=parser.parse_args()
    output=args.output_dir.resolve()
    if output.is_relative_to((ROOT/"archive").resolve()):
        raise SystemExit("Output directory must be outside the frozen archive.")
    output.mkdir(parents=True,exist_ok=True)
    tasks=tasks_for(args.suite)
    logpath=output/(args.suite+".log")
    reportpath=output/(args.suite+".json")
    report={"suite":args.suite,"started_utc":datetime.now(timezone.utc).isoformat(),
            "status":"RUNNING","tasks":[],"scope":"Selected exact evidence and regressions, not formal proof certification or all historical research."}
    began=time.perf_counter()
    report["archive_before"]=check_archive()
    assert INDEX.read_text(encoding="utf-8")==render(),"Regenerate CHECKS.md."
    preflight=[t["argv"][0] for t in tasks if shutil.which(t["argv"][0]) is None]
    if preflight:
        report.update(status="FAIL",missing_executables=sorted(set(preflight)))
        reportpath.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
        print("Missing executables: "+", ".join(sorted(set(preflight))))
        return 1
    environment=os.environ.copy()
    environment.pop("PYTHONOPTIMIZE",None)
    environment["PYTHONDONTWRITEBYTECODE"]="1"
    environment["PYTHONIOENCODING"]="utf-8"
    with logpath.open("w",encoding="utf-8") as logfile:
        def emit(line):
            print(line,flush=True)
            logfile.write(line+"\n")
            logfile.flush()
        emit("Suite: "+args.suite)
        with tempfile.TemporaryDirectory(prefix="finite-averaging-review-") as tmp:
            archive=Path(tmp)/"archive"
            emit("Copying archived research to a temporary workspace.")
            shutil.copytree(ROOT/"archive",archive,ignore=shutil.ignore_patterns("__pycache__","*.pyc"))
            for task in tasks:
                emit("\n["+task["name"]+"]")
                start=time.perf_counter()
                process=subprocess.Popen(task["argv"],cwd=archive/task["directory"],
                    stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=environment,
                    text=True,encoding="utf-8",errors="replace")
                captured=[]
                try:
                    for line in process.stdout:
                        captured.append(line)
                        emit(line.rstrip("\n"))
                    code=process.wait()
                except BaseException:
                    process.terminate()
                    process.wait()
                    raise
                stdout="".join(captured)
                missing=[m for m in task["markers"] if m not in stdout]
                passed=code==0 and not missing
                result={"name":task["name"],"status":"PASS" if passed else "FAIL",
                        "exit_code":code,"missing_markers":missing,
                        "wall_seconds":round(time.perf_counter()-start,3)}
                report["tasks"].append(result)
                emit("RESULT "+json.dumps(result))
                if not passed:
                    break
        report["archive_after"]=check_archive()
        report["status"]="PASS" if len(report["tasks"])==len(tasks) and all(t["status"]=="PASS" for t in report["tasks"]) else "FAIL"
        report["wall_seconds"]=round(time.perf_counter()-began,3)
        emit("\nFINAL "+report["status"])
    reportpath.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print("Report: "+str(reportpath))
    return 0 if report["status"]=="PASS" else 1


if __name__=="__main__":
    raise SystemExit(main())
