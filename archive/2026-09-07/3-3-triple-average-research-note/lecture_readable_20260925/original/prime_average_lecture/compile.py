"""Compile the self-contained lecture sources; no mathematical checks are run."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
engine = shutil.which('xelatex')
if not engine:
    local_engine = Path(r'C:\CTEX\MiKTeX\miktex\bin\xelatex.exe')
    if local_engine.exists():
        engine = str(local_engine)
if not engine:
    sys.exit('XeLaTeX is required. Install MiKTeX or TeX Live and add xelatex to PATH.')

with tempfile.TemporaryDirectory(prefix='prime-average-lecture-') as temporary:
    build = Path(temporary)
    for run in range(3):
        result = subprocess.run(
            [engine, '-interaction=nonstopmode', '-halt-on-error',
             f'-output-directory={build}', 'prime_average_lecture.tex'],
            cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        if result.returncode:
            log = HERE / 'compilation_error.log'
            log.write_bytes(result.stdout)
            sys.exit(f'Compilation failed. See {log}')
    shutil.copyfile(build/'prime_average_lecture.pdf', HERE/'prime_average_lecture.pdf')
    print(f'Created {HERE / "prime_average_lecture.pdf"}')
