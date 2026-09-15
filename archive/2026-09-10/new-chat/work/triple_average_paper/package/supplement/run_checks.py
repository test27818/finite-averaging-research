"""Run the paper's exact certificates and finite implementation audits."""

from pathlib import Path
import os
import subprocess
import sys

if not __debug__:
    raise RuntimeError('Run without -O and without PYTHONOPTIMIZE.')

CHECKS = (
    ('verify_seven_descent_cover.py', 'exact certificate: PASS'),
    ('verify_eight_euclidean_descent.py', 'B8 Euclidean macro certificate: PASS'),
    ('verify_ten_descent_cover.py', 'B10 exact local-real descent certificate: PASS'),
    ('verify_ten_complete.py', 'ten-point complete theorem certificate: PASS'),
    ('verify_all_dimensions_double_triple_invariant.py', 'all-dimension double-triple invariant: PASS'),
    ('verify_general_invariant.py', 'direct all-n invariant: PASS'),
    ('verify_paper_data.py', 'paper finite data and internal references: PASS'),
    ('verify_small_dimensions.py', '3/4/5-point claims: PASS'),
)


def main():
    root = Path(__file__).resolve().parent
    log = []
    environment = os.environ.copy()
    environment['PYTHONUTF8'] = '1'
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    for name, marker in CHECKS:
        result = subprocess.run([sys.executable, str(root / name)], cwd=root,
                                env=environment, capture_output=True, text=True, encoding='utf-8')
        section = f'[{name}]\n{result.stdout}{result.stderr}'
        log.append(section)
        print(section, flush=True)
        if result.returncode or marker not in result.stdout:
            (root / 'verification_results.txt').write_text('\n'.join(log), encoding='utf-8')
            raise SystemExit(f'FAIL: {name}')
    message = f'ALL PAPER CHECKS PASS: {len(CHECKS)}'
    print(message, flush=True)
    log.append(message)
    (root / 'verification_results.txt').write_text('\n'.join(log), encoding='utf-8')


if __name__ == '__main__':
    main()
