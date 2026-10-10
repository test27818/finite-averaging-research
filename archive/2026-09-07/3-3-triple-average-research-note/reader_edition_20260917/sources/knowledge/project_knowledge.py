"""Local research navigation. Standard library only; never executes mathematical checks.

catalog.json owns curated state; the legacy verification manifest remains read-only.
Generated pages are reproducible. A hash change means review needed, not theorem false.
"""
from pathlib import Path
import argparse,hashlib,json,re,sys,unicodedata
from functools import lru_cache
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
CAT=HERE/'catalog.json'
MANIFEST=ROOT/'work/verification_manifest.json'
TOPICS={'triple':'三平均全维数与几何','prime':'素数定理与自然统一',
        'subcritical':'阈值以下与五元算术','composite':'一般元数与GRH',
        'algorithms':'算法、复杂度与核验','interfaces':'公共工具与路线边界'}
LABELS={'proved-source':'原证明已完成','proved-local':'本地文稿已给证明，未独立重审',
        'partial':'部分结果／明确范围','open':'开放问题','synthesis':'解释／综述，非新可达性证明',
        'historical':'历史方案／已被更宽接口覆盖','corrected':'修正／撤回过强表述'}

def read(path):return path.read_text(encoding='utf-8-sig')
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load():return json.loads(read(CAT))
def legacy():return json.loads(read(MANIFEST))['verifications']
def evidence_paths(c):
    paths=list(c.get('source_records',[]))
    for item in c.get('local_checks',[]):
        paths.append(item['argv'][1]);paths+=item.get('records',[])
    return list(dict.fromkeys(paths))
def link(path,label=None,prefix='../'):
    return f'[{label or Path(path).name}]({prefix}{path})'
@lru_cache(maxsize=4)
def query_config(version):
    data=load()
    return data.get('query_vocabulary',[]),data.get('query_synonyms',{}),data.get('query_routes',[])
def normalize_query(q):
    q=unicodedata.normalize('NFKC',q).casefold().replace('−','-').replace('–','-')
    _,synonyms,_=query_config(CAT.stat().st_mtime_ns)
    for source,target in synonyms.items():q=q.replace(source.casefold(),target.casefold())
    return q
@lru_cache(maxsize=128)
def tokens(q):
    q=normalize_query(q);vocabulary,_,_=query_config(CAT.stat().st_mtime_ns)
    found=[]
    for part in re.split(r'\s+',q.strip()):
        if not part:continue
        if re.search(r'[\u4e00-\u9fff]',part):
            matches=[word.casefold() for word in vocabulary if word.casefold() in part]
            if matches:found+=matches
            else:found.append(part)
            found+=re.findall(r'[a-z0-9]+(?:[+\-][a-z0-9]+)*',part)
        else:found.append(part)
    return list(dict.fromkeys(found))
def score(query,text):
    low=unicodedata.normalize('NFKC',text).casefold().replace('−','-').replace('–','-');terms=tokens(query)
    return sum(1+min(low.count(t),4) for t in terms if t in low)+(20 if terms and all(t in low for t in terms) else 0)
def ranked(query,entries):
    rows=[];q=normalize_query(query);route_bonus={}
    _,_,routes=query_config(CAT.stat().st_mtime_ns)
    for route in routes:
        if all(normalize_query(t) in q for t in route['all']):
            for i,key in enumerate(route['cards']):route_bonus[key]=max(route_bonus.get(key,0),500-20*i)
    for e in entries:
        implicit='五元 三平均 5元' if e['id'].startswith('FIVE-') else ''
        searchable=json.dumps(e,ensure_ascii=False)+' '+implicit
        rank=score(query,searchable)
        if rank:
            # Prefer actual claim names and curated aliases over incidental mentions.
            rank+=3*score(query,e.get('title','')+' '+implicit+' '+' '.join(e.get('aliases',[])))
        rows.append((rank+route_bonus.get(e['id'],0),e))
    return [e for s,e in sorted(rows,key=lambda x:(-x[0],x[1]['id'])) if s]

def document_paths():
    paths=[]
    for folder in ('outputs','research'):
        paths.extend(p for p in (ROOT/folder).rglob('*.md') if '__pycache__' not in p.parts)
    return sorted(paths)

def inventory(data):
    cards=data['claims'];bydoc={}
    for c in cards:
        for doc in c['documents']:bydoc.setdefault(doc,[]).append(c['id'])
    legacydocs={}
    for v in legacy():
        for doc in v.get('documents',[]):legacydocs.setdefault(doc,[]).append(v['id'])
    result=[]
    for p in document_paths():
        path=p.relative_to(ROOT).as_posix();s=read(p)
        heading=next((l.lstrip('# ').strip() for l in s.splitlines() if l.startswith('#')) ,p.stem)
        if p.name=='README.md':role='目录入口（状态见结论卡）'
        elif '/history/' in path:role='历史目录；可能仍含有效工具'
        elif '/audits/' in path:role='审查记录'
        elif 'literature' in path or 'investigation' in path:role='来源／调查'
        elif path in bydoc:role='已建立结论卡'
        elif path in legacydocs:role='仅旧核验登记；阅读前核对最新状态'
        else:role='文件已发现；未人工判定全部结论'
        result.append({'path':path,'title':heading,'role':role,'cards':bydoc.get(path,[]),
                       'legacy_verifications':legacydocs.get(path,[]),'sha256':digest(p)})
    return result

def card_text(c,data,topic=False):
    pref='../../' if topic else '../'
    out=[f"### {c['id']} · {c['title']}",'',f"**状态：** {LABELS[c['status']]}。{c['scope']}",'',
         '**边界：** '+c['boundary'],'',
         '**原文：** '+' · '.join(link(p,prefix=pref) for p in c['documents']),'']
    if c.get('assumptions'):out+=['**条件／外部依赖：** '+'；'.join(c['assumptions']),'']
    if c.get('source_records'):out+=['**证据／文献记录：** '+' · '.join(link(p,prefix=pref) for p in c['source_records']),'']
    if c.get('depends_on'):out+=['**导航前提：** '+', '.join(c['depends_on'])+'（不是自动抽取的完整证明DAG）','']
    if c.get('related'):out+=['**还应读：** '+', '.join(c['related']),'']
    if c.get('updates'):out+=['**与旧结果的关系：** '+'；'.join(x['id']+'：'+x['scope'] for x in c['updates']),'']
    newer=[(x['id'],u['scope']) for x in data['claims'] for u in x.get('updates',[]) if u['id']==c['id']]
    if newer:out+=['**后续更新：** '+'；'.join(k+'：'+s for k,s in newer),'']
    out+=['**核验：** `python knowledge/project_knowledge.py verify '+c['id']+'` 只展示已登记命令及边界，不自动启动计算。','']
    if c.get('next_step'):out+=['**继续须新增：** '+c['next_step'],'']
    return '\n'.join(out)

def coverage_text(data,topic):
    refs=data.get('coverage_views',{}).get(topic,[])
    if not refs:return ''
    by={c['id']:c for c in data['claims']}
    out=['## 当前参数覆盖：启动与收尾分开看','',
         '记 n=2p+r。以下同时展示完整基线和明确范围的改进；重叠行是替代关系，不能据一行的共同收尾推断启动也统一。','',
         '| 参数范围 | 初始构造 | 收尾 | 残留证据／统一边界 | 来源卡 |',
         '|---|---|---|---|---|']
    for ref in refs:
        c=by[ref['claim']];row=c['coverage'][ref['row']]
        source=row['source'].split('#')[0]
        out.append('| '+' | '.join(row[k] for k in ('parameters','startup','terminal','residual'))+
                   ' | '+link(source,c['id'],prefix='../../')+' |')
    return '\n'.join(out)+'\n'

def context_ids(matches,data,depth=2):
    by={c['id']:c for c in data['claims']};seen=set();ordered=[]
    queue=[(c['id'],0) for c in matches]
    while queue:
        key,level=queue.pop(0)
        if key in seen:continue
        seen.add(key);ordered.append(key)
        if level>=depth:continue
        c=by[key]
        # Later replacements first: prevents reading only the obsolete stopping point.
        newer=[x['id'] for x in data['claims'] if any(u['id']==key for u in x.get('updates',[]))]
        queue += [(k,level+1) for k in newer+c.get('related',[])+c.get('depends_on',[])]
    return ordered

def render(data):
    claims=data['claims'];by={c['id']:c for c in claims};inv=inventory(data);pages={}
    status=['# 当前状态与问题分流','',
            '> 由 catalog.json 生成。导航整理不等于独立审稿。修改结论卡后执行 build。','',
            '当前研究任务以用户会话为准；下表记录数学状态，不把某条支线自动设为当前任务。','',
            '| 结论／任务 | 当前范围 | 还缺什么 |','|---|---|---|']
    for row in data['overview']:
        c=by[row['claim']]
        status.append('| '+c['id']+' · '+c['title']+' | '+c['scope']+' | '+c['boundary']+' |')
    status+=['','## 证明全貌','',
             '[三平均完整链](PROOF_ROUTES.md#三平均) · [素数基线与独立改进](PROOF_ROUTES.md#素数平均) · [五元开放问题](PROOF_ROUTES.md#五元) · [路线边界](ROUTE_GUARDS.md)','',
             '## 独立改进的范围（直接引用结论卡）','']
    for key in data.get('status_highlights',[]):
        c=by[key];status+=['- '+key+'：'+c['scope']+' **限制：** '+c['boundary']]
    status+=['',
             f'本次机器目录覆盖 {len(inv)} 篇 outputs/research Markdown，人工登记 {len(claims)} 张结论卡；原核验清单有 {len(legacy())} 项。未登记正文不会被自动当作过时或无效。','']
    pages['STATUS.md']='\n'.join(status)
    for key,title in TOPICS.items():
        selected=[c for c in claims if c['topic']==key]
        lines=['# '+title,'','[总状态](../STATUS.md) · [接手入口](../START_HERE.md)','',data['topic_notes'][key],'',
               coverage_text(data,key),'| ID | 结论 | 状态 |','|---|---|---|']
        for c in selected:lines.append(f"| {c['id']} | {c['title']} | {LABELS[c['status']]} |")
        lines+=['']+[card_text(c,data,True) for c in selected]
        pages['topics/'+key+'.md']='\n'.join(lines)
    lines=['# 文档清单','',
           '文件发现索引，不替代结论卡。历史文件中仍可能有有效引理；未人工标注不等于没有价值。快照、缓存和下载PDF不混入默认检索。','',
           '用 `python knowledge/project_knowledge.py context "关键词"` 同时检索结论与正文，默认不检索整理备份。','']
    for folder in ('outputs','research'):
        lines+=['## '+folder,'','| 文件 | 角色 | 结论卡／旧核验ID |','|---|---|---|']
        for d in inv:
            if not d['path'].startswith(folder+'/'):continue
            names=', '.join(d['cards']) or ', '.join(d['legacy_verifications']) or '—'
            lines.append('| '+link(d['path'],d['title'].replace('|','／'))+' | '+d['role']+' | '+names+' |')
        lines+=['']
    pages['DOCUMENTS.md']='\n'.join(lines)
    pages['document_inventory.json']=json.dumps(inv,ensure_ascii=False,indent=2)+'\n'
    return pages

def evidence(c):
    out=[];old={x['id']:x for x in legacy()}
    for vid in c.get('verification_ids',[]):
        v=old[vid]
        out+=['旧核验 '+vid+' ['+v.get('evidence_level','unspecified')+']',v.get('evidence_scope','')]
        for cmd in v.get('commands',[]):out.append('命令：'+' '.join(cmd['argv']))
        out.append('不证明：'+v.get('does_not_establish','以原注册为准'))
    for e in c.get('local_checks',[]):
        out+=['本地核验 ['+e['level']+']',e['scope'],'命令：'+' '.join(e['argv'])]
        if e.get('records'):out.append('记录：'+', '.join(e['records']))
        out.append('本次导航整理未因此重跑或独立认证该数学证明。')
    if not out:out=['本卡无独立核验命令；属于书面证明、综述或开放任务。请按原文阅读，不把空项当作已验证。']
    return '\n'.join(out)

def search(query,data,limit=8):
    rows=ranked(query,data['claims'])[:limit]
    print('结论卡（人工状态）：')
    for c in rows:print(c['id'],LABELS[c['status']],c['title'],'\n ',c['scope'])
    print('\n旧核验（可能含已被替代的历史阶段）：')
    for v in ranked(query,legacy())[:min(limit,4)]:print(v['id'],v.get('claim',''),'\n ',','.join(v.get('documents',[])))
    found=[]
    for p in document_paths():
        content=read(p);s=score(query,p.as_posix()+' '+content)
        if s:
            hits=[(score(query,l),i,l) for i,l in enumerate(content.splitlines(),1) if any(t in l.casefold() for t in tokens(query))]
            best=max(hits,key=lambda v:v[0]) if hits else None
            line=(best[1],best[2]) if best else None
            # Long historical logs should not obscure the current authored source.
            if '/history/' in p.as_posix():s-=8
            if p.name=='README.md':s-=3
            found.append((s,p,line))
    print('\n正文定位（匹配不是当前结论）：')
    for s,p,line in sorted(found,key=lambda v:(-v[0],str(v[1])))[:limit]:
        i,l=line or (1,'');print(f'{p.relative_to(ROOT).as_posix()}:{i} {l[:200]}')
    return rows

def check(data):
    errors=[];cards=data['claims'];ids=[c['id'] for c in cards];oldids={v['id'] for v in legacy()}
    if re.search(r'\?{4,}|\ufffd',json.dumps(data,ensure_ascii=False)):
        errors.append('登记表出现可疑编码替换字符')
    if len(ids)!=len(set(ids)):errors.append('重复结论ID')
    for row in data['overview']:
        if set(row)!={'claim'} or row.get('claim') not in ids:errors.append('overview必须仅引用现有结论ID')
    for key in data.get('status_highlights',[]):
        if key not in ids:errors.append('未知状态摘要ID '+key)
    by={c['id']:c for c in cards}
    for topic,refs in data.get('coverage_views',{}).items():
        for ref in refs:
            if set(ref)!={'claim','row'} or ref['claim'] not in by or ref['row'] not in by[ref['claim']].get('coverage',{}):
                errors.append('覆盖视图必须引用结论卡上的覆盖行');continue
            row=by[ref['claim']]['coverage'][ref['row']]
            if not (ROOT/row['source'].split('#')[0]).is_file():errors.append('覆盖来源不存在 '+row['source'])
    for route in data.get('query_routes',[]):
        if any(key not in ids for key in route['cards']):errors.append('检索路由有未知ID')
    registered=set()
    for c in cards:
        for field in ('id','title','topic','status','scope','boundary','documents','source_hashes'):
            if field not in c:errors.append(c.get('id','?')+' 缺少 '+field)
        if c['status'] not in LABELS or c['topic'] not in TOPICS:errors.append(c['id']+' 状态/主题无效')
        for target in c.get('depends_on',[])+c.get('related',[])+[u['id'] for u in c.get('updates',[])]:
            if target not in ids:errors.append(c['id']+' 未知关联 '+target)
        paths=c['documents']+c.get('source_records',[])
        for e in c.get('local_checks',[]):
            paths+=e.get('records',[])
            if len(e['argv'])<2 or e['argv'][0]!='python':errors.append(c['id']+' 非标准本地命令')
            else:paths.append(e['argv'][1])
        for p in paths:
            if not (ROOT/p).is_file():errors.append(c['id']+' 引用不存在 '+p)
        for p in c['documents']:
            registered.add(p)
            if (ROOT/p).is_file() and c['source_hashes'].get(p)!=digest(ROOT/p):
                errors.append(c['id']+' 来源已变化，须核对结论卡 '+p)
        for p in evidence_paths(c):
            if (ROOT/p).is_file() and c.get('evidence_hashes',{}).get(p)!=digest(ROOT/p):
                errors.append(c['id']+' 程序／记录版本已变化，须核对证据范围 '+p)
        for v in c.get('verification_ids',[]):
            if v not in oldids:errors.append(c['id']+' 旧核验ID不存在 '+v)
    research={p.relative_to(ROOT).as_posix() for p in (ROOT/'research/prime_arity_padic').glob('*.md') if p.name!='README.md'}
    for p in sorted(research-registered):errors.append('独立研究未登记 '+p)
    # Prerequisites are deliberately curated; relations may cross-reference, dependencies must be acyclic.
    graph={c['id']:c.get('depends_on',[]) for c in cards};active=set();done=set()
    def visit(k):
        if k in active:errors.append('导航前提循环 '+k);return
        if k in done or k not in graph:return
        active.add(k)
        for j in graph[k]:visit(j)
        active.remove(k);done.add(k)
    for k in graph:visit(k)
    from frozen_compat import audit
    frozen=audit(ROOT)
    errors += ['冻结兼容：'+e for e in frozen['errors']]
    for path,content in render(data).items():
        p=HERE/path
        if not p.exists() or read(p)!=content:errors.append('生成页过期 '+path+'；执行 build')
    entrypoints=[ROOT/x for x in ('README.md','AGENTS.md','work/README.md','outputs/README.md',
                                 'outputs/prime_arity/README.md','outputs/triple_average/README.md',
                                 'outputs/general_arity/README.md','research/prime_arity_padic/README.md')]
    for p in list(HERE.rglob('*.md'))+entrypoints:
        if 'archive' in p.parts:continue
        if re.search(r'\?{4,}|\ufffd',read(p)):errors.append('可疑编码 '+str(p.relative_to(ROOT)))
        for target in re.findall(r'\]\(([^)]+)\)',read(p)):
            if target.startswith(('http:','https:','#','app:')):continue
            target=unquote(target.strip('<>').split('#')[0])
            if target and not (p.parent/target).exists():errors.append('断链 '+str(p.relative_to(ROOT))+' -> '+target)
    print(json.dumps({'claims':len(cards),'research_documents_registered':len(research&registered),
                      'legacy_verifications':len(oldids),'frozen_materials':frozen,'errors':errors},ensure_ascii=False,indent=2))
    return 1 if errors else 0

def main():
    sys.stdout.reconfigure(encoding='utf-8',errors='replace')
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='cmd',required=True)
    for name in ('search','context'):
        x=sub.add_parser(name);x.add_argument('query');x.add_argument('--limit',type=int,default=6)
    for name in ('show','verify'):
        x=sub.add_parser(name);x.add_argument('id')
    sub.add_parser('build');sub.add_parser('check')
    x=sub.add_parser('accept-sources');x.add_argument('ids',nargs='+')
    args=p.parse_args();data=load();byid={c['id']:c for c in data['claims']}
    if args.cmd=='build':
        for name,content in render(data).items():
            path=HERE/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8',newline='\n')
        print('Generated status, topic pages and document inventory. No mathematics or verification scripts executed.')
    elif args.cmd=='check':return check(data)
    elif args.cmd=='accept-sources':
        for key in args.ids:
            if key not in byid:p.error('未知ID '+key)
        for key in args.ids:
            c=byid[key];c['source_hashes']={d:digest(ROOT/d) for d in c['documents']}
            c['evidence_hashes']={d:digest(ROOT/d) for d in evidence_paths(c)}
        CAT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print('Refreshed declared source hashes for '+', '.join(args.ids)+'. This does not certify mathematical correctness.')
    elif args.cmd in ('show','verify'):
        if args.id not in byid:p.error('未知ID '+args.id)
        c=byid[args.id];print(evidence(c) if args.cmd=='verify' else card_text(c,data)+'\n'+evidence(c))
    else:
        matches=search(args.query,data,args.limit)
        if args.cmd=='context':
            if any(c['topic']=='prime' for c in matches):print('\n'+coverage_text(data,'prime'))
            for k in context_ids(matches,data):print('\n'+card_text(byid[k],data))
            print('\n开始研究前：读上述原文，写出已有结论、精确缺口、预期新增内容；有限检索没有命中不表示文献不存在。')
    return 0

if __name__=='__main__':raise SystemExit(main())
