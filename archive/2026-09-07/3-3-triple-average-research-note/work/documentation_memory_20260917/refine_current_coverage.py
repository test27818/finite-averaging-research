"""One-time curated amendment from the reviewed coverage documents; not a proof search."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'knowledge/catalog.json';data=json.loads(p.read_text(encoding='utf-8'));by={c['id']:c for c in data['claims']}

def add(key,title,scope,boundary,doc,vid,aliases):
    c={'id':key,'title':title,'topic':'prime','status':'proved-source','scope':scope,'boundary':boundary,
       'documents':[doc],'source_hashes':{doc:hashlib.sha256((ROOT/doc).read_bytes()).hexdigest()},
       'depends_on':['EXTERNAL-ARITH'],'related':['PRIME-NATURAL-UNIFICATION','PRIME-RETAINED-BRIDGE'],
       'updates':[],'verification_ids':[vid] if vid else [],'local_checks':[],
       'assumptions':['原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词'],
       'next_step':'','aliases':aliases,'source_records':[],'evidence_hashes':{}}
    if key not in by:data['claims'].append(c);by[key]=c

add('PRIME-2P2','偶数下边界 n=2p+2：状态相关的两次CRT返回',
    '全部素数p≥5、n=2p+2的完整G=1判据；无需omega(p+1)限制。',
    '原文的“上方九偏移仍未解”是历史状态；本边界已完整，但不等于内部偶数启动已经同构。',
    'outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md','two-p-plus-two-uniform',
    ['2p+2 r=2 双载体 偶数下半带 边界 CRT'])
add('PRIME-EVEN-INTERIOR','偶数下半带内部 4≤r≤p−3 的完整证明',
    '全部p≥7、偶数4≤r≤p−3，n=2p+r全输入G=1充要。',
    '不承担r=2及r=p−1；这两条边界有独立完整卡。旧二进表可由PRIME-DYADIC替代，不等于启动全部统一。',
    'outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md','even-interior-completion',
    ['偶数 内部 下半带 4≤r≤p-3 相邻对合'])
add('PRIME-3PM1','偶数上边界 n=3p−1：重叠反射完整证明',
    '全部素数p≥5、n=3p−1的完整G=1判据；p≥7通式，p=5有显式夹乘。',
    '两条偶数边界均已完成；本卡并未宣称与r=2及内部是同一资源公式。',
    'outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md','three-p-minus-one-completion',
    ['3p-1 r=p-1 偶数下半带 上边界 重叠反射'])
add('PRIME-3P','n=3p：三个等大块运输',
    'n=3p的完整判据允许G为p幂；等大三块具有独立的真实运输／终端机制。',
    '此处不可简写G=1；本原重数改变，未由r≠p的共同控制器替代。',
    'outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md','prime-arity-middle-band',
    ['3p r=p 等块 三块 运输'])

c=by['PRIME-NATURAL-UNIFICATION']
c['title']='自然统一的主目标：全参数原位置资源供应'
c['scope']='原阈值已证。目标是统一2p<n<4p的初始物理资源供应；纤维比较、改变来源、状态相关准备是并列候选策略。奇数下半带已有共同反射。'
c['boundary']='退化出口不是唯一必经关卡；先有独立真实资源才可使用深核。共同收尾、共同形状与同一选参公式是不同强度。'
c['next_step']='证明全参数库存内足够的真实作用：可比较计数纤维、改变来源或按状态准备；须接可控终端，不要求所有出口序列终止。'
c['aliases']+=['偶数部分统一了吗 上半带统一到哪里 下半带 资源供应 分段 启动 收尾 小素数 83']
c['related']+=['PRIME-2P2','PRIME-EVEN-INTERIOR','PRIME-3PM1','PRIME-3P','PRIME-CRITICAL-CONTROLLER']
by['PRIME-CRITICAL-CONTROLLER']['aliases']+=['上半带 九偏移 三段选参 3p<n<4p 共同收尾 p≥83']
by['PRIME-RETAINED-BRIDGE']['aliases']+=['偶数下半带 p≥83 启动构造 内部 r=p-1']
by['PRIME-FIVE-RETURNS']['aliases']+=['小素数 九偏移 p<83 剩余证据']

# Scope facts live on their claim, once. The view is only a list of references.
def cover(key,name,parameter,start,finish,residual,source):
    by[key].setdefault('coverage',{})[name]={'parameters':parameter,'startup':start,'terminal':finish,
        'residual':residual,'source':source}
cover('PRIME-ODD-PENCIL','odd-lower','奇p≥3；奇数1≤r<p；n=2p+r',
      '同一边界反射铅笔，包含r=1；启动无83界',
      '已证根／深核＋有限对应共同终端',
      '此整族不再逐小p启动；原Morris/Serre依赖保留',by['PRIME-ODD-PENCIL']['documents'][0])
cover('PRIME-2P2','r2','p≥5；r=2；n=2p+2',
      '可逆缩放＋三步重叠反射；对当前列选两次CRT数字返回',
      '指定载体坐标后接精确同余纤维',
      '全小素数有效，无omega(p+1)限制；仍与内部不同启动',by['PRIME-2P2']['documents'][0])
cover('PRIME-EVEN-INTERIOR','even-interior','p≥7；偶数4≤r≤p−3',
      '原相邻载体对合与实际逆／根资源',
      '原深核与终端；二进表可用PRIME-DYADIC统一替代',
      '全参数已证；尚非与r=2、p−1共用一个资源公式',by['PRIME-EVEN-INTERIOR']['documents'][0])
cover('PRIME-3PM1','rpm1','p≥5；r=p−1；n=3p−1',
      '重叠反射族；p=5接明确夹乘，p≥7通式',
      '方向、单位与主同余纤维',
      '完整解析证明；没有因此消除边界与内部启动差别',by['PRIME-3PM1']['documents'][0])
cover('PRIME-RETAINED-BRIDGE','large-lower','p≥83；3≤r<p（覆盖上述偶数内部及r=p−1）',
      'r<r₀用旧载体桥；r≥r₀用共同新载体公式',
      '同一根／单位／移动终端；已有深核后可用有限对应',
      '共同收尾已合并，启动仍分旧／新载体；r=2不包含',by['PRIME-RETAINED-BRIDGE']['documents'][0])
cover('PRIME-3P','rp','n=3p',
      '三个等大块，控制level为3',
      '真实正运输与零触发',
      '独立机制；判据为G的p幂，不能写G=1',by['PRIME-3P']['documents'][0])
upper=by['PRIME-CRITICAL-CONTROLLER']['documents'][0]
cover('PRIME-CRITICAL-CONTROLLER','upper-near','p≥83；r=p+s，1≤s≤9',
      '§3.3旧三连参数计数，使用前两个输出',
      '统一反射、根与终端接口',
      '此范围不用小参数表；三段选参尚未合成单一公式',upper+'#3.3')
cover('PRIME-CRITICAL-CONTROLLER','upper-middle','p≥83；r=p+s，10≤s≤⌊p/2⌋',
      '§3.2平衡来源＋相邻输出',
      '与紧邻3p及上端相同',
      '已合并控制与收尾，来源计数仍不同',upper+'#3.2')
cover('PRIME-CRITICAL-CONTROLLER','upper-far','p≥83；3p/2<r<2p',
      '§3.1按剩余载体选择q=2来源',
      '与另外两段相同',
      '上半带全覆盖；并非三段启动选参已完全合并',upper+'#3.1')
cover('PRIME-FIVE-RETURNS','small-offsets','11≤p<83；n=3p+s，1≤s≤9',
      '冻结基线162组；独立五返回通式替代其中48组',
      'direction/binary_unit及特殊辅助已由后续接口替代',
      '独立路线仍列114组根资源；不等于已改写并重审基线',by['PRIME-FIVE-RETURNS']['documents'][0])
cover('PRIME-TOTAL','other-small','5≤p<83其他上半带；p=3单独',
      '原完整区间证明；p=5、7用锐界；p=3用三平均直接链',
      '按原覆盖表的各已证终端',
      '可达性全证；新共同p≥83公式未全参数替代这些分支',by['PRIME-TOTAL']['documents'][0]+'#4')
cover('PRIME-TAIL-BACKUP','tail','n≥4p',
      '已有整数见证下降；容量不足时接既有算术核心',
      '原尾部全参数完成',
      '备用改进，不再视为当前可达性缺口',by['PRIME-TAIL-BACKUP']['documents'][0])
data['coverage_views']={'prime':[
 {'claim':k,'row':r} for k,r in [('PRIME-ODD-PENCIL','odd-lower'),('PRIME-2P2','r2'),
 ('PRIME-EVEN-INTERIOR','even-interior'),('PRIME-3PM1','rpm1'),('PRIME-RETAINED-BRIDGE','large-lower'),
 ('PRIME-3P','rp'),('PRIME-CRITICAL-CONTROLLER','upper-near'),('PRIME-CRITICAL-CONTROLLER','upper-middle'),
 ('PRIME-CRITICAL-CONTROLLER','upper-far'),('PRIME-FIVE-RETURNS','small-offsets'),
 ('PRIME-TOTAL','other-small'),('PRIME-TAIL-BACKUP','tail')]]}
data['overview']=[{'claim':k} for k in ['TRIPLE-ALL','PRIME-TOTAL','PRIME-NATURAL-UNIFICATION',
 'FIVE-SUMMARY','FIVE-ESCAPE-OPEN','SIX-EXPLICIT','SEVEN-GEOMETRY','COMPOSITE-FRONTIER','ALG-LENGTH']]
data['status_highlights']=['PRIME-FIVE-RETURNS','PRIME-FINITE-TERMINAL','PRIME-ODD-PENCIL']
data['query_vocabulary']=['上半带','下半带','上半区','下半区','九偏移','共同控制器','偶数','奇数',
 '统一','启动','资源','收尾','全参数','选参','小素数','小参数','边界','分段','五元','小分母','两根','列修正','尖点']
data['query_synonyms']={'上半区':'上半带','下半区':'下半带','偶余量':'偶数','奇余量':'奇数','小p':'小素数'}
data['query_routes']=[
 {'all':['上半带','九偏移'],'cards':['PRIME-CRITICAL-CONTROLLER','PRIME-FIVE-RETURNS','PRIME-NATURAL-UNIFICATION']},
 {'all':['上半带','选参'],'cards':['PRIME-CRITICAL-CONTROLLER','PRIME-NATURAL-UNIFICATION']},
 {'all':['偶数','统一'],'cards':['PRIME-NATURAL-UNIFICATION','PRIME-2P2','PRIME-EVEN-INTERIOR','PRIME-3PM1','PRIME-RETAINED-BRIDGE']},
 {'all':['2p+2'],'cards':['PRIME-2P2']},
 {'all':['3p-1'],'cards':['PRIME-3PM1']},
 {'all':['小素数','资源'],'cards':['PRIME-NATURAL-UNIFICATION','PRIME-FIVE-RETURNS','PRIME-ODD-PENCIL']},
 {'all':['共同收尾'],'cards':['PRIME-FINITE-TERMINAL','PRIME-CRITICAL-CONTROLLER','PRIME-RETAINED-BRIDGE']}]
data['topic_notes']['prime']='原可达性定理已经完成。先看参数覆盖表，区分共同形状、共同收尾、统一启动和已独立审核；表内大参数替代行可与基线行重叠，不是新的互斥证明划分。全参数资源供应可走纤维比较、改变来源或状态相关准备，退化出口不是唯一关卡。'
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Coverage facts on claims; views contain references only. Cards:',len(data['claims']))
