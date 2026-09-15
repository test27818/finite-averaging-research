"""Create a portable zip and verify every archived byte against its checksum."""
from hashlib import sha256
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path('C:/Users/19226/Documents/Codex/2026-09-10/new-chat/outputs/averaging_algorithm_benchmark')

if __name__ == '__main__':
    files = sorted(p for p in ROOT.iterdir()
                   if p.is_file() and p.suffix in ('.md', '.json', '.py'))
    hashes = {p.name: sha256(p.read_bytes()).hexdigest() for p in files}
    checksum = ROOT/'SHA256SUMS.txt'
    checksum.write_text(''.join(hashes[p.name]+'  '+p.name+'\n' for p in files), encoding='ascii')
    destination = ROOT.parent/'averaging_algorithm_benchmark.zip'
    with ZipFile(destination, 'w', ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files+[checksum]:
            archive.write(path, ROOT.name+'/'+path.name)
    with ZipFile(destination) as archive:
        assert archive.testzip() is None
        for name, digest in hashes.items():
            assert sha256(archive.read(ROOT.name+'/'+name)).hexdigest() == digest
    print('benchmark archive integrity: PASS', len(files)+1, 'files,', destination.stat().st_size, 'bytes')
