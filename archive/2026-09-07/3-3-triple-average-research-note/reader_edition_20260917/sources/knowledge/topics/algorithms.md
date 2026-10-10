# 算法、复杂度与核验

[总状态](../STATUS.md) · [接手入口](../START_HERE.md)

存在性、构造、最短性、计时和搜索失败必须分别报告；一条固定输入路径可以精确重放，但不承载无穷量词。


| ID | 结论 | 状态 |
|---|---|---|
| ALG-LENGTH | 构造长度与最短路径的不同状态 | 部分结果／明确范围 |
| ALG-WEB | 网页求解器与效率比较的证据范围 | 部分结果／明确范围 |

### ALG-LENGTH · 构造长度与最短路径的不同状态

**状态：** 部分结果／明确范围。三平均直接算法有数值界和固定n位长多项式界；原求解器、精确IDA*和最短路径困难分别登记。

**边界：** 可变n统一多项式构造长度未证；最短性NP困难不否定非最优多项式路径可能性。

**原文：** [triple_average_sequence_length_analysis.md](../../outputs/algorithms/triple_average_sequence_length_analysis.md) · [pair_triple_solver_comparison_and_optimality.md](../../outputs/algorithms/pair_triple_solver_comparison_and_optimality.md)

**核验：** `python knowledge/project_knowledge.py verify ALG-LENGTH` 只展示已登记命令及边界，不自动启动计算。

### ALG-WEB · 网页求解器与效率比较的证据范围

**状态：** 部分结果／明确范围。保存Arena源码审阅、同题精确重放、批量计时及二平均HTML比较。

**边界：** 有限随机速度优势不证明最坏复杂度；预算搜索失败不是数学反例。

**原文：** [arena_triple_solver_review.md](../../outputs/algorithms/arena_triple_solver_review.md) · [averaging_algorithm_benchmark.md](../../outputs/algorithms/averaging_algorithm_benchmark.md)

**核验：** `python knowledge/project_knowledge.py verify ALG-WEB` 只展示已登记命令及边界，不自动启动计算。
