"""Audit no integer out-edge, without claiming rational nonreachability."""
import json
from pathlib import Path
from verify_endpoint_reverse_diagnostic import value_patterns

if __name__ == '__main__':
    report = Path(__file__).with_name('exact_seven_average_n15_bounded_b5.json')
    states = json.loads(report.read_text(encoding='utf-8'))['reports'][0]['unknown_states']
    for values in states:
        assert not any(len(set(move)) > 1 and sum(move) % 7 == 0
                       for move in value_patterns(values))
    print('n15 integer-frozen inputs, rational status handled separately: PASS', len(states))
