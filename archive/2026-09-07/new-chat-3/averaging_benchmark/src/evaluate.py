#!/usr/bin/env python3
"""Evaluation harness for the averaging-to-equalize benchmark.

Reads ground-truth JSONL files and a predictions JSONL file, then prints a
human-readable Markdown report and (optionally) writes a JSON summary.

Prediction schema (one JSON object per line):
  judge     : {"id": "...", "answer": "YES" | "NO" | true | false}
  min_steps : {"id": "...", "answer": <int>}
  construct : {"id": "...", "steps": [[i, j], ...]}

Usage:
    python3 src/evaluate.py --ground data/ --preds results/preds.jsonl \
        [--split test] [--task judge|min_steps|construct] [--out results/report.md]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from solver import verify_sequence  # noqa: E402


def load_ground(ground_dir, split=None):
    rows = []
    if split:
        path = os.path.join(ground_dir, f"{split}.jsonl")
        rows = [json.loads(l) for l in open(path)]
    else:
        for fn in sorted(os.listdir(ground_dir)):
            if fn.endswith(".jsonl") and fn != "manifest.json":
                rows += [json.loads(l) for l in open(os.path.join(ground_dir, fn))]
    return rows


def load_preds(path):
    return {json.loads(l)["id"]: json.loads(l) for l in open(path)}


def norm_label(x):
    if isinstance(x, bool):
        return "YES" if x else "NO"
    return str(x).strip().upper()


def score_judge(rows, preds):
    stats = {"n": 0, "correct": 0}
    tier = defaultdict(lambda: [0, 0])
    trait = defaultdict(lambda: [0, 0])
    tp = tn = fp = fn = 0
    for r in rows:
        if r["id"] not in preds:
            continue
        p = norm_label(preds[r["id"]].get("answer"))
        if p not in ("YES", "NO"):
            continue
        stats["n"] += 1
        ok = p == r["label"]
        stats["correct"] += ok
        tier[r["tier"]][0] += ok
        tier[r["tier"]][1] += 1
        for t in r["traits"]:
            trait[t][0] += ok
            trait[t][1] += 1
        if r["label"] == "YES":
            if p == "YES":
                tp += 1
            else:
                fn += 1
        else:
            if p == "NO":
                tn += 1
            else:
                fp += 1
    out = {}
    out["accuracy"] = stats["correct"] / stats["n"] if stats["n"] else 0.0
    out["n"] = stats["n"]
    out["per_tier"] = {k: {"acc": (v[0] / v[1] if v[1] else None), "n": v[1]}
                       for k, v in sorted(tier.items())}
    out["per_trait"] = {k: {"acc": (v[0] / v[1] if v[1] else None), "n": v[1]}
                        for k, v in sorted(trait.items())}
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    out["precision_YES"] = prec
    out["recall_YES"] = rec
    out["f1_YES"] = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    tnr = tn / (tn + fp) if (tn + fp) else 0.0
    tpr = rec
    out["balanced_acc"] = (tpr + tnr) / 2
    out["confusion"] = {"TP": tp, "TN": tn, "FP": fp, "FN": fn}
    return out


def score_min_steps(rows, preds):
    n = 0
    exact = 0
    mae = 0.0
    ratio_sum = 0.0
    for r in rows:
        if r.get("min_steps") is None or r["id"] not in preds:
            continue
        p = preds[r["id"]].get("answer")
        if not isinstance(p, int):
            continue
        n += 1
        if p == r["min_steps"]:
            exact += 1
            ratio_sum += 1.0
        else:
            mae += abs(p - r["min_steps"])
            ratio_sum += (p / r["min_steps"]) if r["min_steps"] else float("inf")
    out = {
        "n": n,
        "exact_match": exact / n if n else 0.0,
        "mae": mae / n if n else None,
        "mean_step_ratio": ratio_sum / n if n else None,
    }
    return out


def score_construct(rows, preds):
    n = 0
    ok = 0
    steps_sum = 0
    ratio_sum = 0.0
    ratio_n = 0
    for r in rows:
        if r.get("sequence") is None or r["id"] not in preds:
            continue
        steps = preds[r["id"]].get("steps")
        if not isinstance(steps, list):
            continue
        n += 1
        good, _, _ = verify_sequence(r["a"], steps)
        ok += good
        steps_sum += len(steps)
        if good and r.get("min_steps"):
            ratio_sum += len(steps) / r["min_steps"]
            ratio_n += 1
    out = {
        "n": n,
        "success_rate": ok / n if n else 0.0,
        "mean_steps": steps_sum / n if n else None,
        "mean_steps_ratio_vs_min": (ratio_sum / ratio_n) if ratio_n else None,
    }
    return out


def render(judge_res, ms_res, cons_res, split_label):
    lines = []
    lines.append(f"# Benchmark report — {split_label}\n")
    if judge_res and judge_res["n"]:
        j = judge_res
        lines.append("## Task 1 · Judge (mixability YES/NO)\n")
        lines.append(f"- instances scored: {j['n']}")
        lines.append(f"- **accuracy: {j['accuracy']:.4f}**")
        lines.append(f"- balanced accuracy: {j['balanced_acc']:.4f}")
        lines.append(f"- precision(YES)={j['precision_YES']:.3f}  recall(YES)={j['recall_YES']:.3f}  F1={j['f1_YES']:.3f}")
        lines.append(f"- confusion TP={j['confusion']['TP']} TN={j['confusion']['TN']} FP={j['confusion']['FP']} FN={j['confusion']['FN']}\n")
        lines.append("### per tier\n")
        lines.append("| tier | acc | n |")
        lines.append("|---|---|---|")
        for k, v in j["per_tier"].items():
            lines.append(f"| {k} | {round(v['acc'], 4) if v['acc'] is not None else 'n/a'} | {v['n']} |")
        lines.append("")
        lines.append("### per trait\n")
        lines.append("| trait | acc | n |")
        lines.append("|---|---|---|")
        for k, v in j["per_trait"].items():
            lines.append(f"| {k} | {round(v['acc'], 4) if v['acc'] is not None else 'n/a'} | {v['n']} |")
        lines.append("")
    if ms_res and ms_res["n"]:
        m = ms_res
        lines.append("## Task 3 · Min steps\n")
        lines.append(f"- instances scored: {m['n']}")
        lines.append(f"- **exact-match: {m['exact_match']:.4f}**")
        lines.append(f"- MAE: {m['mae']:.3f}   mean step ratio (pred/true): {m['mean_step_ratio']:.3f}\n")
    if cons_res and cons_res["n"]:
        c = cons_res
        lines.append("## Task 2 · Construct (verified sequence)\n")
        lines.append(f"- instances scored: {c['n']}")
        lines.append(f"- **success rate: {c['success_rate']:.4f}**")
        lines.append(f"- mean steps: {c['mean_steps']:.2f}   mean steps ratio vs min: {c['mean_steps_ratio_vs_min'] if c['mean_steps_ratio_vs_min'] is not None else 'n/a'}\n")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ground", default="data")
    ap.add_argument("--preds", required=True)
    ap.add_argument("--split", default=None)
    ap.add_argument("--task", default=None, choices=["judge", "min_steps", "construct"])
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    rows = load_ground(args.ground, args.split)
    preds = load_preds(args.preds)

    judge_res = score_judge(rows, preds) if args.task in (None, "judge") else {}
    ms_res = score_min_steps(rows, preds) if args.task in (None, "min_steps") else {}
    cons_res = score_construct(rows, preds) if args.task in (None, "construct") else {}

    split_label = args.split or "all splits"
    md = render(judge_res, ms_res, cons_res, split_label)
    print(md)

    if args.out:
        with open(args.out, "w") as f:
            f.write(md + "\n")
        summary = {"judge": judge_res, "min_steps": ms_res, "construct": cons_res}
        with open(args.out.replace(".md", ".json"), "w") as f:
            json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
