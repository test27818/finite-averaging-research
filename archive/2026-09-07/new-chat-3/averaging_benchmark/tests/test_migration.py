"""Regression suite: standard library only. python3 -m unittest discover -s tests -v"""
import hashlib
import itertools
import json
from pathlib import Path
import random
import sys
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
import solver
import solver_v2 as V
import construct as C
import mix_engine as E
import prove_no as P
import legacy_bfs as B
from lower import lower_bound

CASES = [([38,-23,-14,16,-11,4,63,80,14,38],10),
         ([-81,-60,-95,-95,-20,-13,-87,-80,42,54],11)]


def fixture_rows():
    # Frozen BEFORE migration: never cross-check a new solver against its own new data.
    return [json.loads(line) for line in (ROOT/'tests/fixtures/original_small.jsonl').read_text().splitlines()]


class MigrationTests(unittest.TestCase):
    def test_original_truths(self):
        n = 0
        for row in fixture_rows():
            if row['min_steps'] is None:
                continue
            n += 1
            r = V.solve(row['a'], deadline_s=3)
            self.assertTrue(r['certified'], row)
            self.assertEqual(r['min_steps'], row['min_steps'], row)
            self.assertTrue(solver.verify_sequence(row['a'], r['sequence'])[0])
            self.assertLessEqual(lower_bound(row['a']), row['min_steps'])
        self.assertEqual(n, 78)

    def test_pre_migration_random_truths(self):
        rows = json.loads((ROOT/'tests/fixtures/pre_migration_260.json').read_text())
        for row in rows:
            r = V.solve(row['a'], deadline_s=5)
            self.assertTrue(r['certified'], row)
            self.assertEqual(r['min_steps'], row['min'], row)
            self.assertTrue(solver.verify_sequence(row['a'], r['sequence'])[0])

    def test_all_shipped_labels_and_constructions(self):
        for sp in ['dev','test','hard','small']:
            for line in (ROOT/'data'/f'{sp}.jsonl').read_text().splitlines():
                row = json.loads(line)
                self.assertEqual('YES' if solver.judge(row['a']) else 'NO', row['label'])
                if row['label'] == 'YES':
                    r = C.construct(row['a'], deadline_s=5)
                    self.assertTrue(r['verified'], row['id'])
                    self.assertTrue(solver.verify_sequence(row['a'], r['steps'])[0])

    def test_case_studies_and_decision_endpoints(self):
        for a, minimum in CASES:
            r = V.solve(a, deadline_s=5)
            self.assertEqual(r['min_steps'], minimum)
            no = P.decision(E.deviations(a), minimum-1, deadline=time.time()+5)
            self.assertTrue(no[0])
            self.assertEqual(no[3], 'proved')
            yes = P.decision(E.deviations(a), minimum, deadline=time.time()+5)
            self.assertFalse(yes[0])
            self.assertEqual(yes[3], 'found')
            self.assertTrue(solver.verify_sequence(a, yes[4])[0])

    def test_expired_deadline_is_not_proof(self):
        a = CASES[1][0]
        r = V.solve(a, deadline_s=0)
        self.assertEqual(r['status'], 'limit')
        self.assertFalse(r['certified'])
        self.assertIsNone(r['min_steps'])
        out = P.decision(E.deviations(a), 11, deadline=time.time()-1)
        self.assertEqual(out[3], 'time')
        self.assertFalse(out[0])

    def test_node_and_memory_caps(self):
        st = E.state_of(CASES[1][0])
        for kwargs in [dict(node_budget=0), dict(node_budget=1), dict(memo_cap=0)]:
            found, moves, nodes, memo, reason = E.decision(st, 11, **kwargs)
            self.assertEqual(reason, 'cap')
            self.assertFalse(found)
            if 'node_budget' in kwargs:
                self.assertLessEqual(nodes, kwargs['node_budget'])
        best = E.construct_moves(st)
        r = E.ida_ladder(st, best, node_budget=1)
        self.assertFalse(r['certified'])
        self.assertLessEqual(r['expanded'], 1)

    def test_depth_cap_and_no_incumbent(self):
        st = E.state_of([0,0,0,1,9])
        best = E.construct_moves(st)
        r = E.ida_ladder(st, best, max_depth=5)
        self.assertFalse(r['certified'])
        ms, notes = P.exact_min([0,0,0,1,9], hi=8, deadline=time.time()+2)
        self.assertIsNone(ms)  # numeric hi is NOT a verified incumbent
        self.assertIn('incomplete', notes)
        self.assertRaises(ValueError, E.decision, st, -1)

    def test_no_optimality_from_numeric_upper(self):
        st = E.state_of([0,0,0,1,9])
        self.assertRaises(ValueError, E.ida_ladder, st, E.construct_moves(st), lower=50)

    def test_strict_construction_step_cap(self):
        st = E.state_of([0,0,0,1])
        self.assertIsNone(E.construct_moves(st, max_steps=2))
        self.assertEqual(len(E.construct_moves(st, max_steps=3)), 3)

    def test_position_api_not_value_api(self):
        for a in [[0,0,0,1,9], [4,2,-5,-1], [11,-4,3,2]]:
            st = E.deviations(a)
            ms, seq, _, status = V.astar(st, deadline=time.time()+3)
            self.assertEqual(status, 'solved')
            self.assertTrue(solver.verify_sequence(a, seq)[0])
            self.assertEqual(ms, len(seq))
            for i,j in seq:
                self.assertTrue(1 <= i <= len(a) and 1 <= j <= len(a))

    def test_independent_fraction_bfs_no_denominator_cutoff(self):
        # Exhaustive small multisets; BFS uses fractions and no projective search code.
        for a in itertools.combinations_with_replacement(range(4), 4):
            ms, seq = B.min_steps_sequence(a, max_depth=6, max_den_exp=None)
            self.assertIsNotNone(ms)
            self.assertEqual(V.solve(a, deadline_s=2)['min_steps'], ms)
            self.assertLessEqual(E.h_pairs(E.state_of(a)), ms)

    def test_labelled_affine_and_permutation_invariance(self):
        rng = random.Random(71)
        base = [0,0,0,1,9]
        for scale in [1,-1,17,-113]:
            a = [10**80+scale*x for x in base]
            rng.shuffle(a)
            r = V.solve(a, deadline_s=3)
            self.assertEqual(r['min_steps'], 9)
            self.assertTrue(solver.verify_sequence(a,r['sequence'])[0])

    def test_large_n_can_be_certified_without_search(self):
        # Corrects the old claim that n>=13 can never be labelled optimal.
        a = list(range(14))
        r = V.solve(a, max_exact_n=12)
        self.assertTrue(r['certified'])
        self.assertEqual(r['min_steps'], 7)
        self.assertEqual(r['states'], 0)

    def test_large_integer_and_zero_steps(self):
        for a in [[],[7],[5,5],[5]*128]:
            r = V.solve(a)
            self.assertEqual(r['min_steps'],0)
            self.assertEqual(r['sequence'],[])
            self.assertTrue(solver.verify_sequence(a,[])[0])
        a = [10**255+7, -10**255+4, 12, 3]
        r = V.solve(a)
        self.assertTrue(solver.verify_sequence(a,r['sequence'])[0])
        self.assertFalse(solver.judge([9000000000000000,9000000000000002,9000000000000005]))

    def test_bad_certificates(self):
        for steps in [[[1,1]],[[1,3]],[[True,2]],[[1.0,2]],[[0,1]],[]]:
            self.assertFalse(solver.verify_sequence([0,2],steps)[0])
        self.assertTrue(solver.verify_sequence([0,2],[[1,2]])[0])

    def test_manifest(self):
        manifest = json.loads((ROOT/'data/manifest.json').read_text())
        for name, row in manifest['files'].items():
            data = (ROOT/'data'/name).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), row['sha256'])
            self.assertEqual(len(data.splitlines()), row['count'])


if __name__ == '__main__':
    unittest.main()
