"""Guard maintained Markdown against the GitHub math failures found on 2026-09-16.

This is a source-format check, not a substitute for GitHub/browser rendering.
Historical archived research is deliberately excluded.
"""
from pathlib import Path
import re
import json

ROOT=Path(__file__).resolve().parents[1]
TICK=chr(96)


def maintained_documents():
    return [ROOT/"README.md",ROOT/"README.en.md",
            *sorted((ROOT/"docs").glob("*.md")),
            *sorted((ROOT/"topics").rglob("*.md"))]


def inspect(path):
    text=path.read_text(encoding="utf-8")
    formulas=[]
    fence=None
    display=[]
    for number,line in enumerate(text.splitlines(),1):
        marker=re.match(r"^\s*("+TICK+r"{3,}|~{3,})(.*)",line)
        if fence:
            if marker and marker[1][0]==fence[0][0] and len(marker[1])>=len(fence[0]):
                if fence[2]=="math":
                    formulas.append((fence[1],"\n".join(display)))
                fence=None;display=[]
            elif fence[2]=="math":
                display.append(line)
            continue
        if marker:
            fence=(marker[1],number,marker[2].strip())
            continue
        assert "$$" not in line,(path,number,"Use a fenced math block")
        pattern=r"\$"+TICK+r"([^"+TICK+r"]+)"+TICK+r"\$"
        inline=list(re.finditer(pattern,line))
        formulas.extend((number,m[1]) for m in inline)
        rest=re.sub(pattern,"",line)
        assert "$" not in rest,(path,number,"Use protected inline math delimiters")
    assert fence is None,(path,"Unclosed code fence")
    for number,formula in formulas:
        assert r"\operatorname" not in formula,(path,number,"Macro rejected by GitHub")
        assert "<" not in formula and ">" not in formula,(path,number,"Use lt/gt commands")
        balance=0
        for m in re.finditer(r"(?<!\\)[{}]",formula):
            balance+=1 if m[0]=="{" else -1
            assert balance>=0,(path,number,"Unmatched brace")
        assert balance==0,(path,number,"Unmatched brace")
    return {"path":path.relative_to(ROOT).as_posix(),"math_formulas":len(formulas)}


def check():
    documents=[inspect(p) for p in maintained_documents()]
    return {"status":"PASS","documents":documents,
            "total_formulas":sum(d["math_formulas"] for d in documents),
            "scope":"Source guard only; confirm actual GitHub rendering separately."}


if __name__=="__main__":
    print(json.dumps(check(),indent=2))
