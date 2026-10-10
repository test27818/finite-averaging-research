"""One-time UTF-8 writes; avoid Windows PowerShell legacy pipe transcoding."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
texts={
'README.md':'''# 有限步平均研究

**统一接手入口：[knowledge/START_HERE.md](knowledge/START_HERE.md)。** 当前结论、证明链、开放问题、旧路线与核验入口已经集中整理；请从这里进入，不凭某篇旧文的“尚未解决”决定新任务。

| 要做什么 | 入口 |
|---|---|
| 五分钟了解数学状态 | [当前状态](knowledge/STATUS.md) |
| 看完整证明依赖与剩余接口 | [证明链](knowledge/PROOF_ROUTES.md) |
| 查相近思路以前做到哪里 | [路线边界](knowledge/ROUTE_GUARDS.md) · [结论卡登记](knowledge/catalog.json) |
| 找某个结论对应的程序 | [核验说明](knowledge/VERIFICATION.md) |
| 按文件查文献和历史材料 | [文档清单](knowledge/DOCUMENTS.md) · [旧成果目录](outputs/README.md) |

三平均 n≥7、全部奇素数平均 n≥2p+1 的 G 判据已有完整证明。自然统一、路径复杂度、五元静态分类与合数最优阈值是不同研究任务，范围和条件见当前状态。

在根目录检索：

```text
python knowledge/project_knowledge.py context "五元 小分母"
python knowledge/project_knowledge.py context "两根 列修正"
python knowledge/project_knowledge.py verify SEVEN-GEOMETRY
python knowledge/project_knowledge.py check
```

原证明在 `outputs/`，后续独立研究在 `research/`，计算材料在 `work/`。本次保留全部原文、脚本、证书和路径；导航原件存于[整理快照](work/documentation_memory_20260917/snapshots.json)。数学状态以准确的结论卡和原证明为准，散列／PASS 都不是数学认证。

研究者先读 [AGENTS.md](AGENTS.md)。新成果应更新已有结论卡、来源、后续替代和核验范围，不再把 README 写成时间线。完整维护与审查边界见[整理报告](knowledge/ORGANIZATION_AUDIT_20260917.md)。
''',
'research/prime_arity_padic/README.md':'''# 独立研究入口

这里保存原完成证明之后的改进，以及五元、六元、七元的算术研究。技术稿和原位置验证文件均保留；本入口不再追加“最新进展”时间线。

**先读[统一接手页](../../knowledge/START_HERE.md)及[当前状态](../../knowledge/STATUS.md)。** 本目录全部技术文稿已经关联结论卡、后续替代与核验命令。

| 主题 | 当前入口 |
|---|---|
| 素数证明：从三共轭根到列修正、有限对应和共同反射 | [素数主题](../../knowledge/topics/prime.md) |
| 五元完整算法与尚未完成的静态算术分类 | [低维主题](../../knowledge/topics/subcritical.md) |
| 七元范数、尖点与全维数根格解释 | [三平均主题](../../knowledge/topics/triple.md) |
| 外部定理、旧Hecke路线与复制／窗口限制 | [公共接口](../../knowledge/topics/interfaces.md) |
| 结论到程序的对应 | [核验说明](../../knowledge/VERIFICATION.md) |
| 按文件追溯全部历史 | [文件清单](../../knowledge/DOCUMENTS.md) |

本目录的“已证明”默认是文稿已有一般论证，不表示全部新结论均已独立审稿或纳入冻结主证明。原阈值定理已经完整；保留114组根资源、统一奇数下半带等属于具体改进范围，不能与旧基线162组计数混用。

继续研究前：

```text
python knowledge/project_knowledge.py context "对应关键词"
```

原先累计入口已完整保存在[整理快照](../../work/documentation_memory_20260917/originals/research/prime_arity_padic/README.md)中，仅作原始版本恢复。数学稿与证书未搬动。新的阅读顺序与状态统一在 `knowledge/catalog.json` 维护。
''',
'work/README.md':'''# 计算材料与核验入口

这里保留全部原核验器、证书、搜索脚本和历史缓存。文件名 `verify_` 本身不决定数学证据强度；请按结论检索。

```text
python knowledge/project_knowledge.py verify TRIPLE-ALL
python knowledge/project_knowledge.py verify PRIME-ODD-PENCIL
python knowledge/project_knowledge.py verify FIVE-TEMPLATE-ESCAPE
```

这些命令只展示对应脚本、记录与证明边界，不启动计算。新的独立研究脚本在 `research/prime_arity_padic/`，现在同样可以从这个入口找到。

原完成项目的执行器和185项登记保持原样：

```text
python work/run_verifications.py --list
python work/run_verifications.py --id seven-endpoint-structure
python work/run_verifications.py --profile prime-proof
```

`prime-proof` 仍对应原冻结证明版本，不假装已经执行后续所有独立简化。[原注册](verification_manifest.json)记录每项检查的 `evidence_scope` 和 `does_not_establish`；[统一核验说明](../knowledge/VERIFICATION.md)解释两套登记如何衔接。

搜索器的阴性输出不证明不可达，有限样本不承担无穷量词，JSON结果的存在也不等于本轮已重跑。接手先读[当前数学状态](../knowledge/STATUS.md)，不要据旧文的阶段性“未解”重开已完成任务。

旧版长核验日志完整保存在[原导航快照](documentation_memory_20260917/originals/work/README.md)，用于溯源和恢复；具体脚本和证书没有移动。源码与正文的当前关联见[文档清单](../knowledge/DOCUMENTS.md)。
'''}
for path,text in texts.items():(ROOT/path).write_text(text,encoding='utf-8',newline='\n')
p=ROOT/'knowledge/catalog.json';data=json.loads(p.read_text(encoding='utf-8'));by={c['id']:c for c in data['claims']}
repairs={
 'AFFINE-IDEAL':('仿射交换子理想：可逆宏已有后根参数可完整计算',
 '可执行仿射生成元的导群参数理想由交换子与倍率局部化精确生成；无需逐参数搜根。',
 '必须先有真实正向逆；非零理想不等于本原理想，导群也不必是全部平移核。',['仿射 交换子 根理想 affine commutator']),
 'PARAMETRIC-RIGIDITY':('固定参数词的有限射影周期刚性',
 '固定有理函数矩阵词若非恒等满足分圆迹关系，仅有限参数有有限射影阶；无限族须有恒等关系或变化词形。',
 '不排除随参数无界增长的词，也不否定后来的统一正向种子。',['参数周期 刚性 trace cyclotomic finite order']),
 'N91-CONTAINER-CORRECTION':('九十一元21504容器等式已经被反驳',
 '模8和模91的尺度字符耦合，证明特定宏群不等于旧21504容器；必要容器修正为43008。',
 '43008仍只是必要容器，未证明等于实际宏群；九十一元可达性已有独立归约，不能混为未解。',['91 九十一 21504 43008 容器 陪集 cusp'])}
for key,fields in repairs.items():
 for name,value in zip(('title','scope','boundary','aliases'),fields):by[key][name]=value
for key,alias in [('FIVE-TEMPLATE-ESCAPE','五元 小分母'),('FIVE-ESCAPE-OPEN','五元 小分母 全词')]:
 by[key]['aliases']=[s for s in by[key]['aliases'] if '??' not in s]+[alias]
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Rewrote affected navigation text from a UTF-8 file; source mathematical documents untouched.')
