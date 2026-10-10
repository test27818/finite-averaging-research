# 成果与研究索引

2026-09-15整理。当前任务：素数平均证明的整合和改进。先按主题选择入口；旧研究过程已移入同目录的[历史路线账本](history/research_routes_history_20260915.md)，技术附录已实际移入主题文件夹，链接与核验注册同步更新。

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

## 素数平均：完整最终阈值

最新证明简化：[三个共轭根与浅层提升](prime_arity/structure/transverse_root_lifting_without_long_orbits.md)。九偏移的奇数n已删除高阶方向／尺度轨道，偶数n只剩至多8个二进修正类；p≥83用统一三连参数公式，保留162组物理计数证书与原两项局部补充。

[主入口](prime_arity/README.md) → [总证明与覆盖表](prime_arity/proof.md) → [通用算术引理](prime_arity/arithmetic_toolkit.md) → [几何解释](prime_arity/geometry.md)。

全部奇素数 p 有 N(p)=2p+1，N(2)=4；阈值以上判据为中心化、本原化后的 G 是 p 幂。两条偶数边界、九个低偏移和全部旧 dₚ 尾部缺口均已完成。不要据旧专题中的阶段状态重新开启这些定理。

最新整理把二进补充所用倍率的扩环正式并入[九偏移第6节](prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)。无条件结论仍使用 Morris/Serre，有限参数证书仍是证明的一部分。[本轮阅读、核验与维护记录](prime_arity/verification.md)说明实际核对范围。

## 三平均：独立直接证明和算法

- [双三重值任意维数直接证明](triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md)：n≥11 的初等主证明，接7、8、9、10元基例得 n≥7；不依赖上述一般算术群证明。
- [二平均原文复核](literature/triple_average_binary_source_reassessment_2026-09-11.md)：直接方法的来源、实际读过的原文和误用边界。
- [序列长度研究](algorithms/triple_average_sequence_length_analysis.md)：区分数值能量界、固定 n 的位长界和未证的可变 n 统一界。
- [算法测试集](algorithms/averaging_algorithm_benchmark.md)：已知可达但可能难于提取路径的输入；搜索失败不代表反例。

旧“17到59的种子／非分裂／仿射／Hecke”研究按[历史路线表](history/research_routes_history_20260915.md)查找。其方法障碍可能仍有意义，素数平均可达性定理本身已不再开放。

## 合数元数：成果保留，另有未解范围

当前交接为[三项任务的完成范围和剩余](general_arity/general_k_three_tasks_progress_20260915.md)。本轮不推进这些任务，不改变用户此前允许采用 GRH 的决定。

| 已有结果 | 条件与入口 |
|---|---|
| 所有平方元数 t² 在 t²+t+1 元完整成立 | [GRH阶段定理](general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md)；充分大参数另有无条件结果 |
| 2、3的全部幂达到最早临界点 | GRH 下；见上述最新交接，不能称为全部后续维数的最终阈值 |
| 任意整数 k≥2 的 2k+1 端点 | [偶元数补齐](general_arity/even_arity_all_endpoints_completion.md)，接已证奇元数结果；无条件 |
| 奇素数幂的全部奇数 2k<n<3k | [奇合数区间与块均值转译](general_arity/odd_composite_coprime_middle_band_completion.md)；无条件 |
| 十平均十六元固定六步网络及推广族 | [固定网络](general_arity/ten_average_sixteen_and_dyadic_network_family.md)；无条件 |
| 任意元数的已知宽尾部 | [一般线性阈值](general_arity/arbitrary_arity_linear_threshold.md)，不等于最优阈值 |

定义 M、H、N 及原猜想的历史来源见[全局状态](general_arity/averaging_global_status_20260912.md)和[合数临界猜想](general_arity/composite_critical_scale_and_conjecture.md)。两篇日期较早，以新交接判断其开放范围。

## 证据与历史

[素数核验说明](prime_arity/verification.md) · [机器依赖图](prime_arity/proof_map.json) · [全项目核验注册](../work/verification_manifest.json) · [此前阅读日志](history/research_reading_log_20260915.md) · [原根 README 历史](../HISTORY.md)。

符号：当前 p 是平均元数，n 是位置数。很多旧 triple_average 文件的 p 是位置数，引用公式前必须检查。
