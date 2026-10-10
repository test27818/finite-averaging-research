"""Run the standalone benchmark audit; does not rerun any search experiment."""
from pathlib import Path
import subprocess
import sys

PACKAGE = Path('C:/Users/19226/Documents/Codex/2026-09-10/new-chat/outputs/averaging_algorithm_benchmark')

if __name__ == '__main__':
    subprocess.run([sys.executable, str(PACKAGE/'verify_paths.py'), '--self-check'],
                   cwd=PACKAGE, check=True)
    print('averaging algorithm benchmark package: PASS')
