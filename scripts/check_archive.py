"""Check source bytes and new navigation; no rewriting of research evidence."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
from check_math_markup import check as check_math_markup

ROOT = Path(__file__).resolve().parents[1]


def check():
    manifest = json.loads((ROOT/"catalog/FILES.json").read_text(encoding="utf-8"))
    bad = []
    for item in manifest["files"]:
        path = ROOT/item["path"]
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            bad.append(item["path"])
    if bad:
        raise AssertionError({"missing_or_changed": bad})
    documents = (list(ROOT.glob("*.md")) + list((ROOT/"topics").rglob("*.md"))
                 + list((ROOT/"docs").rglob("*.md")) + list((ROOT/"catalog").glob("*.md")))
    checked_links = 0
    for path in documents:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0].strip("<>"))
            if not (path.parent/target).exists():
                raise AssertionError({"document":str(path.relative_to(ROOT)), "missing_link":target})
            checked_links += 1
    return {
        "status":"PASS", "source_files":len(manifest["files"]),
        "source_bytes":sum(item["bytes"] for item in manifest["files"]),
        "navigation_links":checked_links,
        "maintained_math_formulas":check_math_markup()["total_formulas"],
    }


if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, indent=2))
