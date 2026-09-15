import json
from pathlib import Path
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from import_web import convert
from upgrade_data import upgrade
from solver import verify_sequence


class IntegrationTests(unittest.TestCase):
    def test_browser_import_uses_fixed_order_and_ignores_optimal_claim(self):
        ground=[dict(id='a',a=[0,2]),dict(id='b',a=[0,2])]
        forged=dict(input=['0','2'],operations=[[1,2]],optimal=True,steps=0)
        records=convert(forged,ground)
        self.assertEqual([r['id'] for r in records],['a','b'])
        for row in records:
            self.assertEqual(set(row),{'id','steps'})
            self.assertTrue(verify_sequence([0,2],row['steps'])[0])
        with self.assertRaises(ValueError):
            convert(dict(input=['2','0'],operations=[[1,2]]),ground)
        with self.assertRaises(ValueError):
            convert(dict(input=['0','2'],operations=[]),ground)

    def test_upgrade_zero_budget_preserves_old_minimum_and_witness(self):
        rows=[json.loads(l) for l in (ROOT/'tests/fixtures/original_small.jsonl').read_text().splitlines()]
        row=max((r for r in rows if r.get('min_steps') is not None), key=lambda r:r['min_steps'])
        with tempfile.TemporaryDirectory() as tmp:
            src,dst=Path(tmp)/'in.jsonl',Path(tmp)/'out.jsonl'
            src.write_text(json.dumps(row)+'\n')
            upgrade(src,dst,0,0)
            new=json.loads(dst.read_text())
            self.assertTrue(new['certified'])
            self.assertEqual(new['min_steps'],row['min_steps'])
            self.assertEqual(new['sequence'],row['sequence'])
            self.assertEqual(new['lb'],new['ub'])
            self.assertTrue(verify_sequence(row['a'],new['sequence'])[0])

    def test_upgrade_rejects_inconsistent_old_truth(self):
        with tempfile.TemporaryDirectory() as tmp:
            src,dst=Path(tmp)/'in.jsonl',Path(tmp)/'out.jsonl'
            row=dict(id='bad',a=[0,2],label='YES',min_steps=0,sequence=[])
            src.write_text(json.dumps(row)+'\n')
            with self.assertRaises(ValueError):
                upgrade(src,dst,1,1000)
            self.assertFalse(dst.exists())
