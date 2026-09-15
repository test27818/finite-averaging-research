"""Run the claim-to-script checks declared in verification_manifest.json."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time


WORK_DIR = Path(__file__).resolve().parent
ROOT_DIR = WORK_DIR.parent
MANIFEST_PATH = WORK_DIR / "verification_manifest.json"
REQUIRED_ENTRY_FIELDS = {
    "id",
    "claim",
    "claim_status",
    "evidence_level",
    "documents",
    "scripts",
    "commands",
    "evidence_scope",
    "does_not_establish",
    "runtime_class",
    "dependencies",
    "profiles",
}


class ManifestError(ValueError):
    pass


def load_manifest() -> dict:
    with MANIFEST_PATH.open(encoding="utf-8") as source:
        manifest = json.load(source)

    if manifest.get("schema_version") != 1:
        raise ManifestError("unsupported or missing schema_version")
    profiles = manifest.get("profiles")
    evidence_levels = manifest.get("evidence_levels")
    entries = manifest.get("verifications")
    support_files = manifest.get("referenced_support_files")
    if not isinstance(profiles, dict) or not profiles:
        raise ManifestError("profiles must be a non-empty object")
    if not isinstance(evidence_levels, dict) or not evidence_levels:
        raise ManifestError("evidence_levels must be a non-empty object")
    if not isinstance(entries, list) or not entries:
        raise ManifestError("verifications must be a non-empty array")
    if not isinstance(support_files, list):
        raise ManifestError("referenced_support_files must be an array")

    seen_ids = set()
    for index, entry in enumerate(entries):
        missing = REQUIRED_ENTRY_FIELDS - set(entry)
        if missing:
            raise ManifestError(
                f"verification #{index} is missing: {', '.join(sorted(missing))}"
            )
        verification_id = entry["id"]
        if verification_id in seen_ids:
            raise ManifestError(f"duplicate verification id: {verification_id}")
        seen_ids.add(verification_id)
        if entry["evidence_level"] not in evidence_levels:
            raise ManifestError(
                f"{verification_id}: unknown evidence level "
                f"{entry['evidence_level']}"
            )
        unknown_profiles = set(entry["profiles"]) - set(profiles)
        if unknown_profiles:
            raise ManifestError(
                f"{verification_id}: unknown profiles "
                f"{', '.join(sorted(unknown_profiles))}"
            )
        for relative_path in entry["documents"] + entry["scripts"]:
            if not (ROOT_DIR / relative_path).is_file():
                raise ManifestError(
                    f"{verification_id}: missing file {relative_path}"
                )
        if not entry["commands"]:
            raise ManifestError(f"{verification_id}: commands must not be empty")
        for command in entry["commands"]:
            if not command.get("argv"):
                raise ManifestError(f"{verification_id}: command argv is empty")
            if not isinstance(command.get("expected_markers"), list):
                raise ManifestError(
                    f"{verification_id}: expected_markers must be an array"
                )
    seen_support_paths = set()
    for item in support_files:
        missing = {"path", "documents", "role", "authority"} - set(item)
        if missing:
            raise ManifestError(
                "support-file item is missing: " + ", ".join(sorted(missing))
            )
        if item["path"] in seen_support_paths:
            raise ManifestError(f"duplicate support-file path: {item['path']}")
        seen_support_paths.add(item["path"])
        for relative_path in [item["path"], *item["documents"]]:
            if not (ROOT_DIR / relative_path).is_file():
                raise ManifestError(f"support-file item: missing file {relative_path}")
    return manifest


def print_catalog(manifest: dict) -> None:
    entries = manifest["verifications"]
    print(f"Manifest: {MANIFEST_PATH.relative_to(ROOT_DIR)}")
    print(f"Catalogued checks: {len(entries)}")
    print(
        "Referenced support/discovery files: "
        f"{len(manifest['referenced_support_files'])}"
    )
    print()
    print(f"{'ID':<30} {'STATUS':<30} {'EVIDENCE':<20} PROFILES")
    print("-" * 108)
    for entry in entries:
        profiles = ",".join(entry["profiles"])
        print(
            f"{entry['id']:<30} {entry['claim_status']:<30} "
            f"{entry['evidence_level']:<20} {profiles}"
        )
    print()
    print("Profiles:")
    for profile, description in manifest["profiles"].items():
        count = sum(profile in entry["profiles"] for entry in entries)
        print(f"  {profile:<7} {count:>2} checks  {description}")
    print()
    print("Run a profile with --profile PROFILE or one check with --id ID.")


def display_command(argv: list[str]) -> str:
    return subprocess.list2cmdline(argv)


def run_command(command: dict) -> tuple[str, float, list[str]]:
    declared_argv = command["argv"]
    argv = [sys.executable if declared_argv[0] == "python" else declared_argv[0]]
    argv.extend(declared_argv[1:])
    print(f"  $ {display_command(declared_argv)}", flush=True)

    environment = os.environ.copy()
    environment.pop("PYTHONOPTIMIZE", None)
    environment.setdefault("PYTHONIOENCODING", "utf-8")
    started = time.perf_counter()
    try:
        process = subprocess.Popen(
            argv,
            cwd=ROOT_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=environment,
        )
    except FileNotFoundError as error:
        return "skip", time.perf_counter() - started, [str(error)]

    captured = []
    assert process.stdout is not None
    try:
        for line in process.stdout:
            captured.append(line)
            print(f"    {line}", end="", flush=True)
        return_code = process.wait()
    except KeyboardInterrupt:
        process.terminate()
        process.wait()
        raise

    elapsed = time.perf_counter() - started
    output = "".join(captured)
    missing = [
        marker for marker in command["expected_markers"] if marker not in output
    ]
    errors = []
    if return_code:
        errors.append(f"exit code {return_code}")
    if missing:
        errors.append("missing markers: " + "; ".join(missing))
    return ("fail" if errors else "pass"), elapsed, errors


def run_entry(entry: dict) -> tuple[str, float]:
    print()
    print(f"[{entry['id']}] {entry['claim']}")
    print(
        f"  evidence={entry['evidence_level']}  "
        f"status={entry['claim_status']}  runtime={entry['runtime_class']}"
    )
    started = time.perf_counter()
    overall = "pass"
    for command in entry["commands"]:
        result, elapsed, errors = run_command(command)
        if result == "skip":
            overall = "skip" if overall == "pass" else overall
        elif result == "fail":
            overall = "fail"
        if errors:
            print(f"  {result.upper()}: {'; '.join(errors)}")
        else:
            print(f"  command PASS ({elapsed:.2f}s)")
    elapsed = time.perf_counter() - started
    if overall == "pass":
        suffix = ""
        if entry["evidence_level"] == "exploratory-search":
            suffix = " (expected bounded/open result reproduced)"
        print(f"[{entry['id']}] PASS{suffix} ({elapsed:.2f}s)")
    else:
        print(f"[{entry['id']}] {overall.upper()} ({elapsed:.2f}s)")
    return overall, elapsed


def select_entries(manifest: dict, profile: str | None,
                   verification_ids: list[str] | None) -> list[dict]:
    entries = manifest["verifications"]
    by_id = {entry["id"]: entry for entry in entries}
    if verification_ids:
        unknown = [item for item in verification_ids if item not in by_id]
        if unknown:
            raise ManifestError("unknown verification ids: " + ", ".join(unknown))
        return [by_id[item] for item in verification_ids]
    if profile:
        return [entry for entry in entries if profile in entry["profiles"]]
    return []


def parse_arguments(profile_names: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run reproducible checks from verification_manifest.json."
    )
    selector = parser.add_mutually_exclusive_group()
    selector.add_argument(
        "--list", action="store_true", help="list checks and evidence levels"
    )
    selector.add_argument(
        "--profile", choices=profile_names, help="run a named check profile"
    )
    selector.add_argument(
        "--id",
        dest="verification_ids",
        action="append",
        metavar="ID",
        help="run one check; repeat this option to run several",
    )
    parser.add_argument(
        "--fail-fast", action="store_true", help="stop after the first failure"
    )
    return parser.parse_args()


def main() -> int:
    if sys.flags.optimize:
        print(
            "Refusing to run verification with Python assertions disabled "
            f"(optimization level {sys.flags.optimize}).",
            file=sys.stderr,
        )
        return 2
    try:
        manifest = load_manifest()
        arguments = parse_arguments(list(manifest["profiles"]))
        if arguments.list or (
            arguments.profile is None and not arguments.verification_ids
        ):
            print_catalog(manifest)
            return 0
        selected = select_entries(
            manifest, arguments.profile, arguments.verification_ids
        )
    except (OSError, json.JSONDecodeError, ManifestError) as error:
        print(f"Manifest error: {error}", file=sys.stderr)
        return 2

    print(manifest["pass_semantics"])
    if arguments.profile == "full":
        print(
            "The full profile includes the roughly 5-minute directed n=91 "
            "cusp-29 depth-5 search."
        )

    counts = {"pass": 0, "fail": 0, "skip": 0}
    total_started = time.perf_counter()
    try:
        for entry in selected:
            result, _ = run_entry(entry)
            counts[result] += 1
            if result == "fail" and arguments.fail_fast:
                break
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130

    elapsed = time.perf_counter() - total_started
    print()
    print(
        "SUMMARY "
        f"PASS={counts['pass']} FAIL={counts['fail']} SKIP={counts['skip']} "
        f"TIME={elapsed:.2f}s"
    )
    return 1 if counts["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
