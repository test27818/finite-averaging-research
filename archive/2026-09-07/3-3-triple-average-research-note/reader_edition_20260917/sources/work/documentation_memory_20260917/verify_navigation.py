"""Maintenance acceptance checks; does not run mathematical proof verifications."""
from pathlib import Path
import copy,hashlib,io,json,subprocess,sys,tempfile
from contextlib import redirect_stdout

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'knowledge'))
import project_knowledge as k
import frozen_compat as frozen

def frozen_policy_tests():
    """Isolated fixtures: prove the migration is narrow, without touching real proof files."""
    with tempfile.TemporaryDirectory() as directory:
        root=Path(directory);records={};entries=[]
        for name in frozen.NAVIGATION:
            p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b'current navigation')
            backup='work/documentation_memory_20260917/originals/'+name
            b=root/backup;b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(b'original navigation')
            records[name]=frozen.sha(b)
            entries.append({'path':name,'backup':backup,'original_sha256':records[name],
                            'accepted_current_sha256':frozen.sha(p)})
        proof=root/'outputs/proof.md';proof.parent.mkdir(exist_ok=True);proof.write_bytes(b'mathematical source')
        records['outputs/proof.md']=frozen.sha(proof)
        s=root/frozen.SNAPSHOT;s.parent.mkdir(parents=True,exist_ok=True);s.write_text(json.dumps(records),encoding='utf-8')
        policy=root/frozen.MIGRATIONS;policy.parent.mkdir(parents=True,exist_ok=True)
        m={'legacy_snapshot_sha256':frozen.sha(s),'entries':entries}
        policy.write_text(json.dumps(m),encoding='utf-8')
        assert not frozen.audit(root)['errors']
        scenarios=[]
        for label,path in [('proof-modification',proof),('proof-deletion',proof),
                           ('original-backup',root/entries[0]['backup']),
                           ('new-unregistered-navigation',root/entries[0]['path']),('snapshot-rewrite',s)]:
            saved=path.read_bytes()
            if label=='proof-deletion':path.unlink()
            else:path.write_bytes(saved+b' tampered')
            assert frozen.audit(root)['errors'],label
            path.write_bytes(saved);scenarios.append(label)
        extra=copy.deepcopy(m)
        extra['entries'].append({'path':'outputs/proof.md','backup':'anything','original_sha256':'bad','accepted_current_sha256':'bad'})
        policy.write_text(json.dumps(extra),encoding='utf-8')
        assert frozen.audit(root)['errors'];scenarios.append('proof-disguised-as-navigation')
    return scenarios

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    data=k.load();by={c['id']:c for c in data['claims']}
    cases=[('五元 小分母','FIVE-TEMPLATE-ESCAPE'),('两根 列修正','PRIME-TWO-ROOTS'),
           ('七元 尖点','SEVEN-GEOMETRY'),('GRH','COMPOSITE-FRONTIER'),
           ('21504','N91-CONTAINER-CORRECTION'),('全词 逃逸','FIVE-ESCAPE-OPEN'),
           ('局部均值','WINDOW-MEAN'),('仿射 交换子','AFFINE-IDEAL')]
    cases += [('上半带 九偏移','PRIME-CRITICAL-CONTROLLER'),
              ('2p+2 3p-1','PRIME-2P2'),('2p+2 3p-1','PRIME-3PM1'),
              ('偶数部分统一了吗','PRIME-NATURAL-UNIFICATION'),
              ('偶数部分统一了吗','PRIME-EVEN-INTERIOR'),
              ('上半区三段选参是否合并','PRIME-CRITICAL-CONTROLLER'),
              ('小p资源是否统一','PRIME-NATURAL-UNIFICATION')]
    queries=[]
    for query,expected in cases:
        results=[c['id'] for c in k.ranked(query,data['claims'])[:4]]
        assert expected in results,(query,expected,results)
        queries.append({'query':query,'required_card':expected,'top_results':results})
    assert any(u['id']=='PRIME-TWO-ROOTS' for u in by['PRIME-SPLIT-COLUMNS']['updates'])
    pack=k.context_ids(k.ranked('两根 列修正',data['claims'])[:3],data)
    assert 'PRIME-CONSERVATION13' in pack  # successor of a successor, formerly missed
    # Overview and coverage must read the claim object, never an independent summary.
    probe=copy.deepcopy(data);probe['claims'][0]['scope']='SINGLE_SOURCE_SENTINEL'
    assert 'SINGLE_SOURCE_SENTINEL' in k.render(probe)['STATUS.md']
    assert all(set(row)=={'claim'} for row in data['overview'])
    probe=copy.deepcopy(data)
    cc=next(c for c in probe['claims'] if c['id']=='PRIME-2P2')
    cc['coverage']['r2']['startup']='COVERAGE_SINGLE_SOURCE_SENTINEL'
    assert 'COVERAGE_SINGLE_SOURCE_SENTINEL' in k.render(probe)['topics/prime.md']
    for key in ('TRIPLE-ALL','FIVE-TEMPLATE-ESCAPE','PRIME-ODD-PENCIL','TRIPLE-BASES','COMPOSITE-FRONTIER'):
        assert '命令：' in k.evidence(by[key])
    docs=k.document_paths()
    assert all('/originals/' not in p.as_posix() and '/__pycache__/' not in p.as_posix() for p in docs)
    # Deliberately wrong source hash must be detected, with no files mutated.
    probe=copy.deepcopy(data);probe['claims'][0]['source_hashes'][probe['claims'][0]['documents'][0]]='bad'
    sink=io.StringIO()
    with redirect_stdout(sink):assert k.check(probe)==1
    assert '来源已变化' in sink.getvalue()
    probe=copy.deepcopy(data)
    item=next(c for c in probe['claims'] if c.get('evidence_hashes'))
    item['evidence_hashes'][next(iter(item['evidence_hashes']))]='bad'
    sink=io.StringIO()
    with redirect_stdout(sink):assert k.check(probe)==1
    assert '程序／记录版本已变化' in sink.getvalue()
    snapshots=json.loads((ROOT/'work/documentation_memory_20260917/snapshots.json').read_text(encoding='utf-8'))
    for entry in snapshots:
        path=ROOT/'work/documentation_memory_20260917/originals'/entry['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256']
    result={'claims':len(data['claims']),
            'independent_research_notes':len(list((ROOT/'research/prime_arity_padic').glob('*.md')))-1,
            'legacy_verification_entries':len(k.legacy()),'active_markdown_inventory':len(docs),
            'retrieval_scenarios':queries,'source_change_detection':'PASS','evidence_change_detection':'PASS',
            'original_navigation_snapshots_verified':len(snapshots),
            'frozen_policy_negative_tests':frozen_policy_tests(),
            'single_source_propagation':'PASS','two_level_successor_context':'PASS',
            'scope':'Navigation checks only. The repair task separately reran four impacted mathematical verifiers, recorded in the review response.',
            'consistency_check':'pending'}
    out=Path(__file__).with_name('navigation_validation.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    sink=io.StringIO()
    with redirect_stdout(sink):code=k.check(data)
    result['consistency_check']=json.loads(sink.getvalue())
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    assert code==0,sink.getvalue()
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
