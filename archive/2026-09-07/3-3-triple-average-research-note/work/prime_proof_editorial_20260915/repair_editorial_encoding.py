"""Repair only the new editorial text; preserve archived original bytes."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
record = json.loads((HERE / 'archive_record.json').read_text(encoding='utf-8'))
headers = {
    'HISTORY.md': '# 历史进展日志（截至2026-09-15整理前）\n\n> 本文保留原根 README。当前状态请读[项目入口](README.md)和[素数证明入口](outputs/prime_arity/README.md)；下文过期的“未解／下一步”不作当前结论。\n\n---\n\n',
    'outputs/history/research_routes_history_20260915.md': '# 历史路线账本（2026-09-15归档）\n\n> 本文保留旧索引和 E／H／I 路线表。当前证明以[素数入口](prime_arity/README.md)为准；旧范围记录用于理解方法边界，不表示当前定理仍有缺口。\n\n---\n\n',
}
for item in record['archives']:
    path = ROOT / item['archive']
    original = path.read_bytes()[-item['original_bytes']:]
    path.write_bytes(headers[item['archive']].encode('utf-8') + original)

banner = '> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](prime_arity/README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。'
for name in record['source_banners']:
    path = ROOT / 'outputs' / name
    lines = path.read_text(encoding='utf-8').splitlines()
    index = next(i for i, line in enumerate(lines[:6]) if line.startswith('> **'))
    lines[index] = banner
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

log = ROOT / 'outputs/history/research_reading_log_20260915.md'
text = log.read_text(encoding='utf-8')
marker = '\n\n## ?????????2026-09-15?'
if marker in text:
    text = text.split(marker, 1)[0]
    text += '''

## 素数证明整理补记（2026-09-15）

本轮回到素数主线，未推进合数GRH任务。直接阅读三份最终／专项审核、九偏移与多个区间附录的相关章节，整理为独立[素数入口](prime_arity/README.md)。具体篇名、章节和间接引用边界见[本轮阅读核验表](prime_arity/verification.md)。实际下载并阅读 Milne v1.31 的模曲线、Hecke对应、level结构及权二微分相关段落；Stein和MIT仅导航，Serre及Kani仍保留原有访问等级。

数学修改：将99组二进补充所需的倍率扩环并入九偏移§6；集中证明本原列模可用单位的精确同余轨道分类及共同终端提升定理。这是对已有纤维接口的统一整理，并非新发现此前未有的原则。没有宣布消去有限证书或新的多项式词长。两个旧README同目录归档，24篇关键附录加当前状态提示；本轮重跑范围和运行输出见上述核验表。
'''
    log.write_text(text, encoding='utf-8')

geometry = ROOT / 'outputs/prime_arity/geometry.md'
text = geometry.read_text(encoding='utf-8').replace('等ogeny（同源）', '同源（isogeny）')
geometry.write_text(text, encoding='utf-8')

(ROOT / 'README.md').write_text('''# 有限步平均研究

更新：2026-09-15。当前工作是**整理和改进素数平均证明**；合数研究保留原进展，本轮暂停推进。

对奇素数 p，最优最终阈值已证明为 N(p)=2p+1；二平均 N(2)=4。n 在阈值以上时，非全等有理输入经原位置 p 平均可达全等，当且仅当中心化、本原化后的差分 gcd 是 p 的幂。只有 p 不整除 n 时才能简写成 G=1。

## 从这里开始

| 需要 | 入口 |
|---|---|
| 新 AI 接手／理解当前定理 | [素数证明入口](outputs/prime_arity/README.md) |
| 完整证明链与各维数覆盖 | [总证明](outputs/prime_arity/proof.md) |
| 统一代数工具与真正的几何结构 | [通用引理](outputs/prime_arity/arithmetic_toolkit.md) · [模曲线与标记格](outputs/prime_arity/geometry.md) |
| 阅读记录、证明证据、独立审核 | [本轮核验说明](outputs/prime_arity/verification.md) |
| 合数的现有成果与 GRH 条件 | [合数交接](outputs/general_arity/general_k_three_tasks_progress_20260915.md) |
| 三平均直接证明、算法和其他主题 | [成果索引](outputs/README.md) |
| 查询曾试过什么 | [历史路线账本](outputs/history/research_routes_history_20260915.md) · [原根进展日志](HISTORY.md) |

素数证明无条件，但引用已审核的 Morris/Serre 定理，且九偏移部分含完整有限参数证书。尚未证明可变 p、n 下的统一多项式操作长度，也未解决一般合数元数的最优最终阈值。旧历史文稿的“未解”不覆盖当前已完成结论。

## 核验入口

在项目根目录执行：

```text
python work/run_verifications.py --profile prime-proof
```

这是素数主线的选定核验集，包含最终独立证书检查；PASS 的证明范围以[注册清单](work/verification_manifest.json)为准，不能代替正文的一般量词或外部定理。其他脚本见 [work 索引](work/README.md)。

## 文档维护

当前定理和阅读顺序集中维护，技术附录保留原位置不改名；历史过程归档，不再向两个 README 逐条追加进展。新结果必须区分“完整定理／有限证书／公式核验／探索”，并更新相关依赖与证据边界。
''', encoding='utf-8')

(ROOT / 'outputs/README.md').write_text('''# 成果与研究索引

2026-09-15整理。当前任务：素数平均证明的整合和改进。先按主题选择入口；旧研究过程已移入同目录的[历史路线账本](research_routes_history_20260915.md)，原技术附录路径保持不变。

## 素数平均：完整最终阈值

[主入口](prime_arity/README.md) → [总证明与覆盖表](prime_arity/proof.md) → [通用算术引理](prime_arity/arithmetic_toolkit.md) → [几何解释](prime_arity/geometry.md)。

全部奇素数 p 有 N(p)=2p+1，N(2)=4；阈值以上判据为中心化、本原化后的 G 是 p 幂。两条偶数边界、九个低偏移和全部旧 dₚ 尾部缺口均已完成。不要据旧专题中的阶段状态重新开启这些定理。

最新整理把二进补充所用倍率的扩环正式并入[九偏移第6节](prime_arity_nine_offsets_large_symmetric_carrier_completion.md)。无条件结论仍使用 Morris/Serre，有限参数证书仍是证明的一部分。[本轮阅读、核验与维护记录](prime_arity/verification.md)说明实际核对范围。

## 三平均：独立直接证明和算法

- [双三重值任意维数直接证明](triple_average_all_dimensions_double_triple_invariant.md)：n≥11 的初等主证明，接7、8、9、10元基例得 n≥7；不依赖上述一般算术群证明。
- [二平均原文复核](triple_average_binary_source_reassessment_2026-09-11.md)：直接方法的来源、实际读过的原文和误用边界。
- [序列长度研究](triple_average_sequence_length_analysis.md)：区分数值能量界、固定 n 的位长界和未证的可变 n 统一界。
- [算法测试集](averaging_algorithm_benchmark.md)：已知可达但可能难于提取路径的输入；搜索失败不代表反例。

旧“17到59的种子／非分裂／仿射／Hecke”研究按[历史路线表](research_routes_history_20260915.md)查找。其方法障碍可能仍有意义，素数平均可达性定理本身已不再开放。

## 合数元数：成果保留，另有未解范围

当前交接为[三项任务的完成范围和剩余](general_k_three_tasks_progress_20260915.md)。本轮不推进这些任务，不改变用户此前允许采用 GRH 的决定。

| 已有结果 | 条件与入口 |
|---|---|
| 所有平方元数 t² 在 t²+t+1 元完整成立 | [GRH阶段定理](general_k_grh_stage_and_remaining_tasks_20260915.md)；充分大参数另有无条件结果 |
| 2、3的全部幂达到最早临界点 | GRH 下；见上述最新交接，不能称为全部后续维数的最终阈值 |
| 任意整数 k≥2 的 2k+1 端点 | [偶元数补齐](even_arity_all_endpoints_completion.md)，接已证奇元数结果；无条件 |
| 奇素数幂的全部奇数 2k<n<3k | [奇合数区间与块均值转译](odd_composite_coprime_middle_band_completion.md)；无条件 |
| 十平均十六元固定六步网络及推广族 | [固定网络](ten_average_sixteen_and_dyadic_network_family.md)；无条件 |
| 任意元数的已知宽尾部 | [一般线性阈值](arbitrary_arity_linear_threshold.md)，不等于最优阈值 |

定义 M、H、N 及原猜想的历史来源见[全局状态](averaging_global_status_20260912.md)和[合数临界猜想](composite_critical_scale_and_conjecture.md)。两篇日期较早，以新交接判断其开放范围。

## 证据与历史

[素数核验说明](prime_arity/verification.md) · [机器依赖图](prime_arity/proof_map.json) · [全项目核验注册](../work/verification_manifest.json) · [此前阅读日志](research_reading_log_20260915.md) · [原根 README 历史](../HISTORY.md)。

符号：当前 p 是平均元数，n 是位置数。很多旧 triple_average 文件的 p 是位置数，引用公式前必须检查。
''', encoding='utf-8')
print('Editorial UTF-8 restored; original archive payloads preserved.')
