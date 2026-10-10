# 一般元数与GRH

[总状态](../STATUS.md) · [接手入口](../START_HERE.md)

保留GRH条件，分清单个维数、首个非自动G点和最终阈值。此前会话的暂停安排不自动约束新用户任务。


| ID | 结论 | 状态 |
|---|---|---|
| COMPOSITE-FRONTIER | 一般元数三项主任务与GRH范围 | 部分结果／明确范围 |
| COMPOSITE-DEFINITIONS | M、H、N与自动G维数不能混用 | 解释／综述，非新可达性证明 |

### COMPOSITE-FRONTIER · 一般元数三项主任务与GRH范围

**状态：** 部分结果／明确范围。无条件全部k的2k+1端点；奇素数幂奇数中间维数；GRH下平方族与2、3幂临界点。

**边界：** 不等于一般N(k)=B(k)。p≥5高奇次幂临界、混合素因子临界及整段接续仍未全闭合。

**原文：** [general_k_three_tasks_progress_20260915.md](../../outputs/general_arity/general_k_three_tasks_progress_20260915.md) · [general_k_grh_stage_and_remaining_tasks_20260915.md](../../outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md)

**条件／外部依赖：** 部分临界结果依赖Dirichlet L函数GRH，不能删条件

**还应读：** COMPOSITE-DEFINITIONS

**核验：** `python knowledge/project_knowledge.py verify COMPOSITE-FRONTIER` 只展示已登记命令及边界，不自动启动计算。

### COMPOSITE-DEFINITIONS · M、H、N与自动G维数不能混用

**状态：** 解释／综述，非新可达性证明。M最早成功、H首个非自动G成功、N此后全部成立，是不同量词；六平均九元自动成功，十元是非自动G点。

**边界：** 历史全局表中的开放范围以COMPOSITE-FRONTIER更新；未将候选临界线推广成已证最终阈值。

**原文：** [averaging_global_status_20260912.md](../../outputs/general_arity/averaging_global_status_20260912.md) · [composite_critical_scale_and_conjecture.md](../../outputs/general_arity/composite_critical_scale_and_conjecture.md)

**核验：** `python knowledge/project_knowledge.py verify COMPOSITE-DEFINITIONS` 只展示已登记命令及边界，不自动启动计算。
