"""Register reviewed additions on the existing subcritical claim IDs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'knowledge/catalog.json';data=json.loads(path.read_text(encoding='utf-8'))
by={c['id']:c for c in data['claims']}
doc='research/prime_arity_padic/subcritical_prime_uniform_arithmetic_20260917.md'
script='research/prime_arity_padic/verify_subcritical_prime_uniform_structure.py'
record='research/prime_arity_padic/subcritical_prime_uniform_structure_verification.json'
for key in ('SUBCRITICAL-COMPLETE','SUBCRITICAL-LIMITS'):
    c=by[key]
    if doc not in c['documents']:c['documents'].append(doc)
    c['source_hashes'][doc]=hashlib.sha256((ROOT/doc).read_bytes()).hexdigest()
    if not any(x['argv'][1]==script for x in c['local_checks']):
        c['local_checks'].append({'argv':['python',script],'level':'symbolic-check / finite-sanity',
          'scope':'一般p的补集G公式、两分支有限模类计数、原位置更新及全r固定同余反例的有限精确检查。全参数有理边界分类、维数和反例不可达性由正文证明，未推出一般r≥3位长多项式界。',
          'records':[record]})
    for name in (script,record):c['evidence_hashes'][name]=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
c=by['SUBCRITICAL-COMPLETE']
c['title']='p至2p统一补集判定；p+2强制递归与p进二叉结构'
c['scope']='所有奇素数p的p+2元已有位长多项式判定及最短词；完整p进紧集判据为K_p成员加(p+2)|(u+v)，维数log2/logp。一般p+r有完整整数能量图，补集G=n/gcd(n,Σu)。'
c['boundary']='p+3起有真零和子集分支，一般只证伪多项式算法；K_p成员仍非固定次gcd公式。p=2,n=4另有二进网络，不适用奇p陷阱。'
c['related']=list(dict.fromkeys(c['related']+['SUBCRITICAL-LIMITS','FIVE-FRACTAL','SIX-EXPLICIT']))
c['aliases']+=['p平均p+2元 p到2p p+r r维 K_p log2/logp 全区间 补集G']
c=by['SUBCRITICAL-LIMITS']
c['scope']='对每个奇素数p、每个p+2≤n≤2p和任意固定M，都有逐项modM相同、G均为1的一可解一不可解输入；一个全r公式统一旧端点例子。有限实半代数判据也不足以刻画p+2方向。'
c['boundary']='只排除G加预定有限同余，以及指定实半代数表达；不排除自适应gcd或其他算术编码。没有证明简洁判据不可能。'
c['aliases']+=['全区间 固定模数 p+3 2p G不充分']
# View update only: no duplicated mathematical state.
data['topic_notes']['subcritical']='先读SUBCRITICAL-COMPLETE最新一般p稿：p至2p都有统一整数补集判定，p+2为强制递归且最短可求；p+3以后一般位长多项式界未得。五元静态算术分类与固定D逃逸另列，不要把已解可判定性重开。'
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Updated SUBCRITICAL-COMPLETE and SUBCRITICAL-LIMITS; no duplicate research card created.')
