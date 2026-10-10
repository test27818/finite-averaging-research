"""One-time addendum recording the scope of the most easily overread local checks."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'knowledge/catalog.json';data=json.loads(p.read_text(encoding='utf-8'))
scopes={
'FIVE-TEMPLATE-ESCAPE':('symbolic-check + exploratory-search',
 '精确检查混合块能量矩阵、模p特征多项式、模板展开及周期递推；可选深度18只解524286个有限词的范数返回根。固定模板一般逃逸由ESS格陪集归约与正文射线排除承担；不证明任意变模板全词逃逸。'),
'FIVE-BOUNDED-RUNS':('theorem-certificate + symbolic-check',
 '有理网格加严格尾误差认证D=1至多三段的全部字长；一般固定段数有限性来自正文紧致化。另重放六平均九元固定网络，不能升级为任意段数分类。'),
'FIVE-HECKE':('symbolic-check / finite-sanity',
 '检查258个间隙截断、长度至6的127个格变基、有限层单位射影周期和1000个Pell赋值实例。一般显式界与同层等价由正文证明，Aka–Shapira不是由有限计数验证。'),
'FIVE-SPARSITY':('symbolic-check / finite-sanity',
 '检查正词谱模3恒等式、二次递推、Pell/Fibonacci表达、纯分支范数及整数区间界的精确前提。ESS/SML一般有限性不由有限词数据承担。'),
'FIVE-UNITS-GROUP':('symbolic-check / finite-sanity',
 '检查单位指数、局部群生成恒等式和有限D=1指数诊断；Baker–Brumer仅按已读来源引用，k范围实验不证明D=1全分类。'),
'FIVE-FRACTAL':('symbolic-check / finite-sanity',
 '核对模3各层类数、实际递归及有理点分型的有限实例；全部有理边界分类和Hausdorff维数由正文的一般论证承担。'),
'SUBCRITICAL-COMPLETE':('symbolic-check / finite-sanity',
 '把强制递归与独立整数能量DAG对照，检查补集公式、实际操作和长词族；完整停机／最短性及位长界来自书面证明。'),
'SEVEN-GEOMETRY':('symbolic-check / finite-sanity',
 '3072个本原核心G/范数/尖点检查、1200层theta及本原计数、17条一般矩阵编译路径、75个局部化列归约及三进覆盖实例；一般宏群等式与theta模性仍需正文和外部来源。'),
'GEOMETRY-ALL-N':('symbolic-check / finite-sanity',
 '860个根格配对、258个模素数秩、200个A₂投影、边界反例与9个维数的旧构造独立重放。全维数充分性引用既有直接证明，不是本轮样本新证。'),
'PRIME-SPLIT-COLUMNS':('symbolic-check / finite-sanity',
 '在旧162组资源上核对不读取direction/binary_unit的列输送、实际混合与终端；通用列算法由正文证明。不会验证全参数初始root_pairs的存在。'),
'PRIME-FIVE-RETURNS':('theorem-certificate + symbolic-check',
 '核对一般五返回计数、原位置重放、48组替代及剩余114组根资源清单；通式的无限参数容量界由正文证明。不等于重新审核整篇素数主定理。'),
'PRIME-FINITE-TERMINAL':('symbolic-check / finite-sanity',
 '核对有限对应内容分支、群化和终端输送实例；一般轨道等式见正文。必须预先有真实深核，且行列式与模数互素。'),
'PRIME-ODD-PENCIL':('symbolic-check / finite-sanity',
 '检查共同反射的容量、矩阵、平方标量、根公式和实际位置返回；所有奇p、奇r的量词由正文公式证明。Morris/Serre依赖及已有终端前提保留。'),
'PRIME-GEOMETRY':('symbolic-check / finite-sanity',
 '核对有限二维计数纤维、内容/伴随公式和有限对应分支；整数凸包根格的一般结论由正文证明，不宣布所有退化纤维有安全出口。'),
'PRIME-FIBER':('symbolic-check / finite-sanity',
 '核对同行列式输出移动、给定范围直接根与有限精度本原内容；不证明任意小p/全部r有足够初始资源或终端覆盖。')}
for c in data['claims']:
 if c['id'] in scopes:
  level,scope=scopes[c['id']]
  for item in c['local_checks']:item['level']=level;item['scope']=scope
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Refined evidence scopes for',len(scopes),'high-risk claims.')
