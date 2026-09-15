"""Deterministically document the frozen binary solver's zero-budget behavior."""
from itertools import count
import json
from pathlib import Path
import sys
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/"archive/2026-09-07/new-chat-3/averaging_benchmark/src"))
import solver_v2
from solver import verify_sequence


def check():
    x=[-81,-60,-95,-95,-20,-13,-87,-80,42,54]
    with patch("time.time",return_value=1000.0):
        frozen=solver_v2.solve(x,deadline_s=0)
    ticks=count(1000.0,0.001)
    with patch("time.time",side_effect=lambda:next(ticks)):
        advancing=solver_v2.solve(x,deadline_s=0)
    assert frozen["status"]=="solved" and frozen["certified"] is False and frozen["min_steps"] is None
    assert verify_sequence(x,frozen["sequence"])[0]
    assert advancing["status"]=="limit" and advancing["certified"] is False and advancing["min_steps"] is None
    return {
        "diagnostic_status":"PASS",
        "known_issue_reproduced":True,
        "frozen_tick":{"status":frozen["status"],"certified":frozen["certified"],
                       "min_steps":frozen["min_steps"],"exact_path_verified":True},
        "advancing_clock":{"status":advancing["status"],"certified":advancing["certified"],
                           "min_steps":advancing["min_steps"]},
        "scope":"Reproduces the recorded zero-budget status inconsistency; does not mark the archived regression suite as passing.",
    }


if __name__=="__main__":
    print(json.dumps(check(),indent=2))
