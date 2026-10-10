"""Compile the standalone lecture. No mathematical verifiers are run."""
from pathlib import Path
import json,shutil,subprocess,sys,tempfile

HERE=Path(__file__).resolve().parent
engine=shutil.which('xelatex')
if not engine:
    fallback=Path('C:/CTEX/MiKTeX/miktex/bin/xelatex.exe')
    if fallback.exists():engine=str(fallback)
if not engine:raise SystemExit('XeLaTeX is required (MiKTeX or TeX Live).')
main='general_k_average_lecture'
with tempfile.TemporaryDirectory(prefix='general-k-lecture-') as folder:
    build=Path(folder)
    for run in range(3):
        result=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error',
                '-no-shell-escape',f'-output-directory={build}',main+'.tex'],cwd=HERE,
                stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if result.returncode:
            (HERE/'compilation_error.log').write_bytes(result.stdout)
            raise SystemExit('Compilation failed; see compilation_error.log')
    shutil.copyfile(build/(main+'.pdf'),HERE/(main+'.pdf'))
    shutil.copyfile(build/(main+'.log'),HERE/'compilation.log')
    shutil.copyfile(build/(main+'.toc'),HERE/'contents.toc')
    shutil.copyfile(build/(main+'.aux'),HERE/'labels.aux')
print('PDF compiled in three passes.')
