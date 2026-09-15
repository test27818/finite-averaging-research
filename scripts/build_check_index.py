"""Generate the bilingual claim-to-check catalog from the frozen registry."""
import argparse
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT/"archive/2026-09-07/3-3-triple-average-research-note"
TARGET = ROOT/"catalog/CHECKS.md"


def link(path, label=None):
    assert (MAIN/path).is_file(), path
    target = "../"+(MAIN/path).relative_to(ROOT).as_posix()
    return "["+(label or path)+"]("+quote(target,safe="/")+")"


def render():
    manifest = json.loads((MAIN/"work/verification_manifest.json").read_text(encoding="utf-8"))
    entries = manifest["verifications"]
    lines = [
        "# 命题—脚本—证据索引 / Claim-to-check index", "",
        "[中文首页](../README.md) · [English](../README.en.md) · [核验指南 / Verification](../docs/VERIFICATION.md)", "",
        "由冻结的verification_manifest.json自动生成，包含"+str(len(entries))+"项注册检查。不是按名称猜测数学范围，也不是重新审定所有命题。", "",
        "Generated from the frozen registry. Each entry preserves its claim status, evidence scope, exclusions, dependencies and executable commands.", "",
        "注意：部分条目的status保留该局部结果建立时的历史措辞（如boundaries-open），不代表这些边界在整个项目中仍未解决。全局当前状态见[证明指南](../docs/PROOF_GUIDE.md)。", "",
        "Some status strings preserve the historical scope of that local result, such as boundaries-open. They are not the current global frontier; consult the proof guide for completed coverage.", "",
        "证据类别 / Evidence levels:", "",
    ]
    for k,v in manifest["evidence_levels"].items():
        lines += ["- **"+k+"**: "+v]
    lines += ["", "## 按ID定位 / Find a check", "", "| ID | 状态 / Status | 证据 / Evidence |", "|---|---|---|"]
    for e in entries:
        lines.append("| ["+e["id"]+"](#"+e["id"]+") | "+e["claim_status"].replace("|","/")+" | "+e["evidence_level"]+" |")
    lines += ["", "## 独立新增引理 / Independent addition", "",
        "2026-09-16二进列提升未写入冻结注册，另见[证明](../archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/structural_reassessment_and_uniform_dyadic_orbits.md)、[核验器](../archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/verify_uniform_dyadic_column_lifting.py)及[结果](../archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/uniform_dyadic_column_lifting_verification.json)。",
        "", "The independent dyadic lemma has its own proof, verifier and evidence; it is not silently substituted into the archived registry.", ""]
    for e in entries:
        lines += ["## "+e["id"], "", "**Claim / 命题：** "+e["claim"], "",
            "**Status:** "+e["claim_status"]+" · **Evidence:** "+e["evidence_level"]+
            " · **Runtime class:** "+e["runtime_class"], "",
            "**Documents / 正文：** "+ " · ".join(link(p) for p in e["documents"]), "",
            "**Scripts / 脚本：** "+" · ".join(link(p) for p in e["scripts"]), "",
            "**Evidence scope / 核验范围：** "+e["evidence_scope"], "",
            "**Does not establish / 不建立：** "+e["does_not_establish"], "",
            "**Dependencies / 依赖：**", ""]
        lines += ["- "+d for d in e["dependencies"]]
        lines += ["", "**Run / 运行：** from the main research directory / 在主研究目录中：", "",
                  "~~~sh","python -B work/run_verifications.py --id "+e["id"],"~~~","",
                  "Expected output markers / 预期标记：",""]
        for c in e["commands"]:
            lines += ["~~~text"]+c["expected_markers"]+["~~~",""]
    return "\n".join(lines).rstrip()+"\n"


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",action="store_true")
    args=parser.parse_args()
    expected=render()
    if args.check:
        assert TARGET.read_text(encoding="utf-8")==expected,"CHECKS.md differs from its source registry"
        print("Claim-to-check catalog: PASS 185")
    else:
        TARGET.write_text(expected,encoding="utf-8")
        print("Wrote catalog/CHECKS.md")


if __name__=="__main__":
    main()
