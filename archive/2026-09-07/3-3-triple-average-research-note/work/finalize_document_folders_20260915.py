"""Write human navigation after the reviewed document migration."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'outputs'
descriptions={
'prime_arity/proofs':('素数主证明技术附录','按下半带、上半带、尾部与下界分组。各篇是总证明的技术来源；历史状态以素数总入口为准。'),
'prime_arity/proofs/lower_band':('2p到3p：全输入入口与完成证明','依次读无条件入口、端点／奇余量／内部偶余量、两条边界，最后读3p。'),
'prime_arity/proofs/upper_band':('3p以上：核心、反射与完成证明','九偏移主文仍保留旧522组版本以便追查；当前精简版先读结构目录的反射区间与单位下降。'),
'prime_arity/proofs/tail_and_lower_bound':('尾部上界与最优性下界','线性阈值第8节给2p反例；逆EGZ及尾部文稿闭合所有较大维数。'),
'prime_arity/tools':('已使用的核心与均值格工具','这里是历史技术来源；集中后的通用算术引理位于素数目录根部。'),
'prime_arity/structure':('素数证明的结构与简化','先读carrier_interval_and_unit_descent：当前已将九偏移有限反射证书缩至180组。其他文稿保留各自适用范围。'),
'prime_arity/audits':('专项与独立审核','审核支持的是各自注明版本；当前区间简化有独立计数和公式核验，不能称为已由旧审核覆盖全部新推导。'),
'prime_arity/examples':('小素数实例与历史证据','完整定理、数值实验和不可达边界都在文件标题及正文标注；不能因同处此目录就视为相同证据等级。'),
'prime_arity/history':('素数路线历史与方法障碍','旧未解列表不是当前待办。当前最优最终阈值已完成；这里保留失败机制和较窄构造的边界。'),
'triple_average':('三平均：直接证明与原算术路线','proofs为当前直接证明及基例；arithmetic_cases保留旧逐维数算术成果；history为探索、纠错和未完成的更强结构。'),
'triple_average/proofs':('三平均直接证明与小基例','先读all_dimensions_double_triple_invariant；它覆盖n≥11，另接7、8、9、10元基例。'),
'triple_average/arithmetic_cases':('三平均旧算术实例','这些完整实例保留其独立价值；一般三平均证明已不再依赖逐素数种子。'),
'triple_average/history':('三平均研究历史','含非分裂轨道、仿射交换子、周期刚性、迹零返回、Hecke等；按文件标题查阅，范围以正文和后续审核为准。'),
'general_arity':('一般元数与合数研究','当前交接为general_k_three_tasks_progress_20260915。保留GRH条件与开放范围；本轮只整理，不推进这些定理。'),
'general_arity/examples':('合数元数实例','各文件分别标注固定网络、完整判据和使用条件。'),
'algorithms':('算法、复杂度与测试集','区分可达性存在、构造长度、最短路径及有限搜索。'),
'literature':('文献调查与原证明复核','阅读层级、获取来源和适用范围由正文记录。'),
'history':('项目历史索引与阅读日志','路线账本帮助避免重复探索；当前状态请回到成果主入口。'),
}
for rel,(title,description) in descriptions.items():
    folder=OUT/rel;folder.mkdir(parents=True,exist_ok=True)
    back=Path(__import__('os').path.relpath(OUT/'README.md',folder)).as_posix()
    lines=[f'# {title}','',description,'',f'[回到成果索引]({back})','']
    if rel=='general_arity':
        lines+=['[当前合数交接](general_k_three_tasks_progress_20260915.md)','']
    for child in sorted(folder.iterdir()):
        if child.is_dir():lines.append(f'- [{child.name}/]({child.name}/README.md)')
        elif child.suffix=='.md' and child.name!='README.md':
            heading=child.read_text(encoding='utf-8').splitlines()[0].lstrip('# ')
            lines.append(f'- [{heading}]({child.name})')
    (folder/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

p=OUT/'README.md'
text=p.read_text(encoding='utf-8')
text=text.replace('原技术附录路径保持不变。','技术附录已实际移入主题文件夹，链接与核验注册同步更新。')
tree='''
## 文件夹地图

```text
outputs/
├─ prime_arity/          素数定理入口、总证明、通用引理
│  ├─ proofs/           lower_band / upper_band / tail_and_lower_bound
│  ├─ tools/            入口、核心与均值格原始工具
│  ├─ structure/        当前证明简化与结构研究
│  ├─ audits/           专项及独立审核
│  ├─ examples/         小素数实例
│  └─ history/          素数研究历史
├─ triple_average/      proofs / arithmetic_cases / history
├─ general_arity/       一般元数、合数与条件性结果
├─ algorithms/          序列、复杂度和测试集
├─ literature/          文献调查
└─ history/             路线账本与阅读日志
```

[素数](prime_arity/README.md) · [三平均](triple_average/README.md) · [一般元数](general_arity/README.md) · [算法](algorithms/README.md) · [文献](literature/README.md) · [历史](history/README.md)。

迁移了220篇文档，旧路径对应新路径可查[完整迁移表](../work/document_reorganization_20260915/path_map.json)。技术脚本和证书仍在work，避免破坏模块导入。没有在outputs根目录留下220个跳转占位文件。
'''
text=text.replace('\n## 素数平均：',tree+'\n## 素数平均：',1)
p.write_text(text,encoding='utf-8')

p=OUT/'prime_arity/README.md';text=p.read_text(encoding='utf-8')
text=text.replace('上级目录保留技术附录和研究历史。','本目录下的proofs、tools、structure、audits、examples和history分别保存技术证明、工具、结构、审核、实例与历史。')
text=text.replace('九个低偏移的证明含522组完整有限参数证书。','九个低偏移现只需180组有限反射证书；p≥97由统一整数区间公式承担，入口及基础单位生成已改为书面证明。原522组版本保留作历史对照。')
text=text.replace('## 2. 按目的阅读','## 当前简化\n\n[反射容量区间与最小单位下降](structure/carrier_interval_and_unit_descent.md)将旧p≥307公式改进到p≥97，减少342组必需证书；仍保留180组及原两项特殊补充。\n\n[证明附录](proofs/README.md) · [结构研究](structure/README.md) · [审核](audits/README.md) · [实例](examples/README.md) · [历史](history/README.md)。\n\n## 2. 按目的阅读')
p.write_text(text,encoding='utf-8')

p=OUT/'prime_arity/proof.md';text=p.read_text(encoding='utf-8')
text=text.replace('p≥307 闭式容量；11≤p<307 的522组完整证书；p=5、7 用各自锐界','[区间构造](structure/carrier_interval_and_unit_descent.md)：p≥97 闭式容量；11≤p<97 的180组反射证书；p=5、7 用各自锐界')
text=text.replace('目前没有证明一套闭式返回计数覆盖全部 p、n，也没有消去522组证书；','目前[区间构造](structure/carrier_interval_and_unit_descent.md)已把九偏移所需反射证书从522组减到180组，入口和基础单位生成不再靠有限证书。尚未证明一套闭式返回计数覆盖全部 p、n，也没有消去剩余180组；')
p.write_text(text,encoding='utf-8')

p=OUT/'prime_arity/geometry.md';text=p.read_text(encoding='utf-8')
text=text.replace('此次未完成新的全参数容量公式。','后续[整数区间构造](structure/carrier_interval_and_unit_descent.md)已把统一容量分界从307降到97，但尚未覆盖其下全部边界。')
p.write_text(text,encoding='utf-8')

p=OUT/'prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md'
text=p.read_text(encoding='utf-8')
first,rest=text.split('\n',1)
note='''

> **当前简化版：**[反射容量区间与单位下降](../../structure/carrier_interval_and_unit_descent.md)已将统一公式范围改进为p≥97，原522组证书现在只需11≤p<97的180组；入口与模n基础单位生成均已有直接书面证明。以下保留p≥307／522组的原审核版本作技术来源，当前最短证明使用上述替代章节。两项特殊补充和原位置扩环仍保留。
'''
p.write_text(first+note+rest,encoding='utf-8')

p=ROOT/'README.md';text=p.read_text(encoding='utf-8')
text=text.replace('且九偏移部分含完整有限参数证书。','且九偏移部分保留180组有限反射证书（已从522组缩减）。')
text=text.replace('技术附录保留原位置不改名；','技术附录已按主题移入文件夹，旧文件名保持不变；')
text=text.replace('## 从这里开始','[文件夹地图](outputs/README.md)展示主题目录；[最新简化](outputs/prime_arity/structure/carrier_interval_and_unit_descent.md)给出p≥97的统一反射区间和不枚举模群的单位下降。\n\n## 从这里开始')
p.write_text(text,encoding='utf-8')
print('Wrote18 folder indexes and updated current proof navigation.')

if __name__=='__main__':pass
