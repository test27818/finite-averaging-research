"""Preserve the legacy snapshot while recognizing explicitly migrated navigation.

No mathematical source can be exempted here. Current navigation and original backups
are both pinned. A new edit needs an explicit migration update, never a baseline rewrite.
"""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[1]
SNAPSHOT='research/prime_arity_padic/existing_documents_snapshot.json'
MIGRATIONS='knowledge/navigation_migrations.json'
NAVIGATION=frozenset(('README.md','outputs/README.md','outputs/prime_arity/README.md',
                     'outputs/triple_average/README.md','outputs/general_arity/README.md','work/README.md'))

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def audit(root=ROOT):
    root=Path(root).resolve()
    try:
        migration=json.loads((root/MIGRATIONS).read_text(encoding='utf-8'))
        records=json.loads((root/SNAPSHOT).read_text(encoding='utf-8'))
    except (OSError,ValueError) as error:
        return {'legacy_total':None,'strictly_unchanged':0,'reviewed_navigation_migrations':0,
                'errors':['Missing or invalid frozen policy/snapshot: '+str(error)]}
    errors=[]
    if sha(root/SNAPSHOT)!=migration['legacy_snapshot_sha256']:
        errors.append('Legacy snapshot changed; migration cannot replace its hashes.')
    entries=migration['entries'];by={row['path']:row for row in entries}
    if len(by)!=len(entries) or set(by)!=NAVIGATION:
        errors.append('Navigation migration must name exactly the six reviewed README paths.')
    strict=migrated=0
    for name,old_digest in records.items():
        path=root/name
        row=by.get(name)
        if row is None:
            if not path.is_file() or sha(path)!=old_digest:
                errors.append('Frozen material changed or missing: '+name)
            else:strict+=1
            continue
        backup_name='work/documentation_memory_20260917/originals/'+name
        if row['original_sha256']!=old_digest or row['backup']!=backup_name:
            errors.append('Migration no longer matches original snapshot: '+name)
            continue
        backup=root/backup_name
        if not backup.is_file() or sha(backup)!=old_digest:
            errors.append('Original navigation backup changed or missing: '+name)
        if not path.is_file() or sha(path)!=row['accepted_current_sha256']:
            errors.append('Unregistered navigation version: '+name)
        migrated+=1
    if not set(by)<=set(records):errors.append('Migration path outside legacy snapshot.')
    return {'legacy_total':len(records),'strictly_unchanged':strict,
            'reviewed_navigation_migrations':migrated,'errors':errors,
            'semantics':'All non-navigation files must match the original snapshot; reviewed READMEs require both the original backup and accepted current version.'}

def require_frozen(root=ROOT):
    result=audit(root)
    assert not result['errors'],result['errors']
    # Historical callers expect the checked entry count, not a new report schema.
    return result['legacy_total']

if __name__=='__main__':
    result=audit();print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(bool(result['errors']))
