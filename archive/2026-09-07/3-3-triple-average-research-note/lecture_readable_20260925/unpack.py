from pathlib import Path
from hashlib import sha256
import json
import zipfile

HERE = Path(__file__).resolve().parent
SOURCE = Path('C:/Users/19226/Documents/Codex/2026-09-24/c-users-19226-documents-codex-2026/outputs/prime_average_lecture_complete.zip')
DEST = HERE / 'original'
DEST.mkdir(exist_ok=True)
with zipfile.ZipFile(SOURCE) as archive:
    for item in archive.infolist():
        target = (DEST / item.filename).resolve()
        if not target.is_relative_to(DEST.resolve()):
            raise ValueError(item.filename)
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(item))
(HERE/'source.json').write_text(json.dumps({'archive':str(SOURCE),
    'sha256':sha256(SOURCE.read_bytes()).hexdigest()},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Extracted original lecture without modifying the supplied archive.')
