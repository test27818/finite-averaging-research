"""Small offline checks of the pinned Danus tokenizer and content-ID semantics.
Does not install Danus, start services, call models, or change mathematical records.
"""
from pathlib import Path
import importlib.util,json,sys

ROOT=Path(__file__).resolve().parent/'harness_sources/danus'

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m
    spec.loader.exec_module(m)
    return m

bm=module('review_danus_bm25',ROOT/'danus/core/bm25.py')
schema=module('review_danus_schema',ROOT/'danus/core/schema.py')
queries=['偶数部分统一了吗','上半带 九偏移','2p+2 3p-1','bounded template escape']
tokens={q:bm.tokenize(q) for q in queries}
assert tokens[queries[0]]==[] and tokens[queries[1]]==[]
scores=bm.bm25_scores(queries[0],[bm.tokenize('偶数部分已经有完整证明'),bm.tokenize('odd band')])
assert scores==[0.0,0.0]
base={'problem_id':'averaging','predecessors':[], 'glossary_introduces':{},
      'statement':'For every n >= 7, the G criterion holds.', 'proof':'Apply the direct theorem.'}
h1=schema.compute_fact_id(**base)
space={**base,'proof':'Apply  the direct theorem.\n'}
rephrase={**base,'statement':'The G criterion holds for all n >= 7.'}
assert schema.compute_fact_id(**space)==h1
assert schema.compute_fact_id(**rephrase)!=h1
out={'commit':json.loads((ROOT/'repository.json').read_text(encoding='utf-8'))['commit'],
     'tokens':tokens,'pure_chinese_scores':scores,'whitespace_deduplication':True,
     'paraphrase_changes_fact_id':True,
     'scope':'Offline function checks only. Verifier accuracy, agent orchestration, platform support, and claimed mathematical case studies were not tested.'}
(ROOT/'focused_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8');print(json.dumps(out,ensure_ascii=False,indent=2))
