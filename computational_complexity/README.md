# p 平均的计算复杂性

2026-10-11—12 的计算复杂性研究专题。来自用户与 AI 研究会话的本地证明、精确核验与探索；尚未独立同行审稿。p 表示每次平均的位置数，n 表示总位置数，B 表示输入二进制总位长。

**近期新增 54 个原文件：12 篇研究稿、24 个 Python 程序、18 个 JSON 核验或来源记录。另收录 1 个既有运行依赖。** [全部文件清单](INVENTORY.md) · [哈希与来源](manifest.json) · [相关结论卡](knowledge/claims_snapshot.json) · [本次发布核验](publication_check.json)

## 当前结论与未解范围

- **可变 p 的统一问题：** 严格亚临界 p+2≤n≤2p−1 的不限步数可达性，已有本地 NP-hard 归约证明；整体 NP 上界与强 NP-hard 未证明。
- **固定 p、n=p+2：** 已有 P 判定。固定余量 r=n−p 的亚临界问题已有多项式长度证书，因此属于 NP。
- **固定五平均八元：** 已有完整有限判定器、多项式归约和多个 P 子程序；完整问题尚未证明属于 P，也尚未证明 NP-hard。
- 指数多状态／出口、长成功周期和有限 NO 反例分别排除某些枚举或模板方法；均不直接证明固定五平均八元非 P。
- 指定策略的验证与自由选择成功策略的存在性须区分；资源超限不是 NO。

## 12 篇新增研究稿

| 结论卡与研究稿 | 新增内容 |
|---|---|
| [SUBCRITICAL-BIT-COMPLEXITY · 亚临界位复杂度：固定余量短证书与指数状态族](research/prime_arity_padic/subcritical_bit_complexity_frontier_20261011.md) | 固定余量的多项式长度证书与 NP 上界；显式指数状态族；六元三平均的 P 判定。 |
| [SUBCRITICAL-NP-HARD · 可变素数元数的亚临界不限步数可达性 NP 困难](research/prime_arity_padic/subcritical_uniform_reachability_np_hard_20261011.md) | p 随输入变化时，严格亚临界全区间的不限步数判定 NP-hard；不含固定五平均八元。 |
| [SUBCRITICAL-DUAL-NORMALS · 固定p对偶法向量与单例外多项式解析](research/prime_arity_padic/fixed_p_dual_normal_decoding_20261011.md) | 关系格与对偶法向量轨道相交；给定单项法向量的 P 成员解析。 |
| [SUBCRITICAL-BLOCK-NORM · 三值核心正定范数层的P判定与强制多例外压缩](research/prime_arity_padic/fixed_p_three_value_norm_descent_20261011.md) | 三值范数层的 P 判定与强制操作段压缩。 |
| [SUBCRITICAL-CLUSTER-ESCAPE · 局部块首位逃逸与完整p+3压缩判定器](research/prime_arity_padic/fixed_p_cluster_escape_and_compressed_solver_20261011.md) | 首位逃逸过滤和完整有限 p+3 求解器；尚无多项式最坏时间保证。 |
| [SUBCRITICAL-LOCAL-PRECISION · 五与七平均的局部精度合成及实数范围判否](research/prime_arity_padic/fixed_p_local_precision_and_real_obstruction_20261011.md) | p=5、7 的局部精度合成与实数范围障碍；局部可合成不代表全局可达。 |
| [FIVE-EIGHT-CLUSTER-REDUCTION · 五平均八元到七位置同余块的多项式等价归约](research/prime_arity_padic/five_eight_polynomial_cluster_reduction_20261011.md) | 五平均八元与七位置同余块子问题的多项式等价。 |
| [FIVE-EIGHT-FIRST-ESCAPE · 五平均八元首次外部交互的完整P子程序](research/prime_arity_padic/five_eight_first_external_interaction_20261011.md) | 首次外部交互存在性的完整 P 子程序；补入深度 14 的完整有限 NO 证书。 |
| [FIVE-EIGHT-EXIT-LANGUAGE · 五平均八元最早出口的指数规模与单项词解析](research/prime_arity_padic/five_eight_earliest_exit_language_20261011.md) | 最早出口仍可指数多个；纯单项局部词有 P 成员解析。 |
| [FIVE-EIGHT-LOCAL-PRODUCTS · 五平均八元任意局部前缀的返回乘积表示](research/prime_arity_padic/five_eight_complete_local_products_20261011.md) | 任意局部词的有符号返回乘积表示、模 4 过滤及一段二幂成本的 P 判据。 |
| [SUBCRITICAL-RANK-CLOCK · p加三核心的秩稳定性与像平面解析](research/prime_arity_padic/p_plus_three_rank_clock_and_plane_decoding_20261011.md) | 秩二稳定、p 进时钟与给定像平面的 P 解析；同核历史可有不同结局。 |
| [SUBCRITICAL-PERIODIC-POLICY · p加三有理返回分类与给定周期策略的P判定](research/prime_arity_padic/p_plus_three_rational_returns_and_periodic_policy_20261011.md) | 任意给定周期策略的 P 判定，包括纯单项；成功周期长度有 Ω(B) 下界。 |

10 月 12 日的主要补充集中在最后一稿：补齐纯单项周期，使给定周期判定覆盖所有非空 proper 周期；同时证明固定有限周期库与 O(log B) 周期穷举无法覆盖全部 YES 输入。此下界仍与按输入生成长策略的 P 算法相容。

## 原有证明前提

本目录保持原研究相对路径。更早的数学前提继续保留在仓库原归档中：

- [ALG-LENGTH · triple_average_sequence_length_analysis.md](../archive/2026-09-07/3-3-triple-average-research-note/outputs/algorithms/triple_average_sequence_length_analysis.md)
- [ALG-LENGTH · pair_triple_solver_comparison_and_optimality.md](../archive/2026-09-07/3-3-triple-average-research-note/outputs/algorithms/pair_triple_solver_comparison_and_optimality.md)
- [SIX-EXPLICIT · six_triple_block_explicit_G3_20260916.md](../archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/six_triple_block_explicit_G3_20260916.md)
- [SUBCRITICAL-COMPLETE · subcritical_complement_dynamics_20260916.md](../archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/subcritical_complement_dynamics_20260916.md)
- [SUBCRITICAL-COMPLETE · subcritical_prime_uniform_arithmetic_20260917.md](../archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/subcritical_prime_uniform_arithmetic_20260917.md)

结论卡快照保留原范围、未证明事项、前提及核验规模；所有 `proved-local` 均表示本地已给证明，不等于外部审稿或证明助手认证。

## 运行与复核

本专题程序只使用 Python 标准库，无需新增第三方包。先在仓库根目录执行：

```sh
cd computational_complexity
python -B -X utf8 check_snapshot.py
```

数学核验程序与对应实现放在同一目录；在本专题根目录按原稿命令运行，例如：

```sh
python -B -X utf8 research/prime_arity_padic/verify_p_plus_three_periodic_policy.py
python -B -X utf8 research/prime_arity_padic/verify_short_period_coverage.py
python -B -X utf8 research/prime_arity_padic/verify_subcritical_uniform_np_hard.py
```

其余核验入口见清单中的 `verify_*.py`。这些程序会重写同名 JSON；可在单独工作副本执行，再查看差异。耗时与规模不同，深度 14 的完整 NO 核验涉及 103252 个状态。

本次发布执行文件哈希、JSON/Python 可读性、全部 Python 导入依赖检查，并复跑周期策略与短周期覆盖两组核验。其余数学核验 JSON 沿用 10 月 11—12 日研究时的记录；本次上传不宣称重新审核全部证明。

## 来源与整理口径

54 个近期文件均逐字节复制自 `2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic`，且在前次公开归档中均不存在。未复制个人配置、账号资料或无关工作区。

旧依赖 `verify_subcritical_complement_dynamics.py` 单独标为既有文件；新增索引与结论卡快照属于发布整理，不冒充新增数学定理。更完整的项目来源见 [PROVENANCE.md](../PROVENANCE.md)。
