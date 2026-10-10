# 工作材料、历次快照及旧目录完整附卷 · 第2分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [文档清单](#doc-222bf2d06b26)
- [大型数学证明项目的现成经验与适合本项目的 harness](#doc-aab16f33b700)
- [项目记忆与证明导航整理报告](#doc-232fe86005a9)
- [证明链与真正开放的接口](#doc-7eb52d82bcd2)
- [开始新路线前，先排除这些重复与偷换](#doc-758033e3448d)
- [研究轮次记录模板](#doc-5182695697d4)
- [接手入口：先定位问题，再阅读证明](#doc-3b227852f0e8)
- [当前状态与问题分流](#doc-9ac70881754c)
- [核验：从结论定位脚本，不从文件名前缀猜结论](#doc-46173a558d11)
- [算法、复杂度与核验](#doc-d5fb440f3df7)
- [一般元数与GRH](#doc-f9fd4177f2c5)
- [公共工具与路线边界](#doc-365cc5f17b32)

---

<a id="doc-222bf2d06b26"></a>

## 原文导签：文档清单

来源：`knowledge/DOCUMENTS.md` · [逐字节原样副本](../sources/knowledge/DOCUMENTS.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-222bf2d06b26 -->
# 文档清单

文件发现索引，不替代结论卡。历史文件中仍可能有有效引理；未人工标注不等于没有价值。快照、缓存和下载PDF不混入默认检索。

用 `python knowledge/project_knowledge.py context "关键词"` 同时检索结论与正文，默认不检索整理备份。

## outputs

| 文件 | 角色 | 结论卡／旧核验ID |
|---|---|---|
| [Arena三平均网页算法审阅与同题对比](../sources/outputs/algorithms/arena_triple_solver_review.md) | 已建立结论卡 | ALG-WEB |
| [原位置 p 平均算法测试集](../sources/outputs/algorithms/averaging_algorithm_benchmark.md) | 已建立结论卡 | ALG-WEB |
| [二平均求解器复核、三平均优化与最短性](../sources/outputs/algorithms/pair_triple_solver_comparison_and_optimality.md) | 已建立结论卡 | ALG-LENGTH |
| [算法、复杂度与测试集](../sources/outputs/algorithms/README.md) | 目录入口（状态见结论卡） | — |
| [三平均计算的性能审计与搜索优化](../sources/outputs/algorithms/triple_average_computation_performance_audit.md) | 仅旧核验登记；阅读前核对最新状态 | n91-search-optimization, n91-cusp29-depth5 |
| [三平均搜索优化建议复核（2026-09-09）](../sources/outputs/algorithms/triple_average_search_optimization_review_2026-09-09.md) | 仅旧核验登记；阅读前核对最新状态 | n91-search-optimization |
| [双三重值算法的操作序列长度](../sources/outputs/algorithms/triple_average_sequence_length_analysis.md) | 已建立结论卡 | ALG-LENGTH |
| [三平均研究的计算核验指南](../sources/outputs/algorithms/triple_average_verification_guide.md) | 文件已发现；未人工判定全部结论 | — |
| [任意平均元数的线性阈值：非单位差分也是可执行资源](../sources/outputs/general_arity/arbitrary_arity_linear_threshold.md) | 仅旧核验登记；阅读前核对最新状态 | arbitrary-arity-linear-threshold |
| [从二平均到任意平均元数：当前全貌与临界猜想](../sources/outputs/general_arity/averaging_global_status_20260912.md) | 已建立结论卡 | COMPOSITE-DEFINITIONS |
| [从素数完整证明到合数临界问题：策略、可迁移定理与真实困难](../sources/outputs/general_arity/averaging_proof_strategy_and_composite_frontier_20260915.md) | 仅旧核验登记；阅读前核对最新状态 | square-arity-controller-nine-thirteen, prime-factor-block-mean-transfer |
| [合数平均：四平均、六平均与原位置副本转译](../sources/outputs/general_arity/composite_arity_four_six_transfer.md) | 仅旧核验登记；阅读前核对最新状态 | six-average-nine-fixed-network, composite-four-six-transfer |
| [合数平均的临界尺度：最早成立、最终阈值与无条件网络](../sources/outputs/general_arity/composite_critical_scale_and_conjecture.md) | 已建立结论卡 | COMPOSITE-DEFINITIONS |
| [从十五元推广到合数端点：统一CRT证书与两素数完整入口](../sources/outputs/general_arity/composite_endpoint_crt_transfer.md) | 仅旧核验登记；阅读前核对最新状态 | composite-endpoint-transfer |
| [全部偶数元数的2k+1端点：旧种子与统一取逆](../sources/outputs/general_arity/even_arity_all_endpoints_completion.md) | 仅旧核验登记；阅读前核对最新状态 | even-arity-all-endpoints |
| [四平均九元完整判据：一个四步周期与模9控制器](../sources/outputs/general_arity/examples/four_average_nine_complete.md) | 仅旧核验登记；阅读前核对最新状态 | four-average-nine-complete |
| [四平均七元完整判据：\((4,2,1)\) 核与模7控制器](../sources/outputs/general_arity/examples/four_average_seven_complete.md) | 仅旧核验登记；阅读前核对最新状态 | four-average-seven-complete |
| [合数元数实例](../sources/outputs/general_arity/examples/README.md) | 目录入口（状态见结论卡） | — |
| [六平均九元：所有输入固定四步完成](../sources/outputs/general_arity/examples/six_average_nine_fixed_network.md) | 仅旧核验登记；阅读前核对最新状态 | six-average-nine-fixed-network |
| [六平均十元完整G判据：第一个非自动的算术成功维数](../sources/outputs/general_arity/examples/six_average_ten_complete.md) | 仅旧核验登记；阅读前核对最新状态 | six-average-ten-complete |
| [一般k平均的证明计划：先完成核心，再接成全部维数](../sources/outputs/general_arity/general_k_averaging_proof_plan_20260915.md) | 仅旧核验登记；阅读前核对最新状态 | square-core-entry-review |
| [接受GRH后的完整平方族定理与剩余证明任务](../sources/outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md) | 已建立结论卡 | COMPOSITE-FRONTIER |
| [一般k平均规划评议：平方族入口可直接补齐，尺度任务可以数论化](../sources/outputs/general_arity/general_k_plan_review_and_square_entry_20260915.md) | 仅旧核验登记；阅读前核对最新状态 | square-core-entry-review |
| [对一般k规划建议的复核与采纳](../sources/outputs/general_arity/general_k_review_response_20260915.md) | 仅旧核验登记；阅读前核对最新状态 | square-core-entry-review |
| [GRH主线三项任务：本轮完成范围与当前剩余](../sources/outputs/general_arity/general_k_three_tasks_progress_20260915.md) | 已建立结论卡 | COMPOSITE-FRONTIER |
| [H_t文献调查：已有小生成元理论、无条件充分大结论与全范围边界](../sources/outputs/general_arity/ht_literature_and_eventual_square_completion_20260915.md) | 来源／调查 | ht-literature-interfaces |
| [逆零和定理的原位置转译：碰撞修复与 2p+4 元七步族](../sources/outputs/general_arity/inverse_zero_sum_averaging_progress.md) | 仅旧核验登记；阅读前核对最新状态 | inverse-zero-sum-transfer |
| [较大素数高奇次幂：两种统一三步正向反射](../sources/outputs/general_arity/large_prime_high_odd_power_three_step_reflections.md) | 仅旧核验登记；阅读前核对最新状态 | large-prime-high-odd-power-reflections |
| [奇合数元数的奇余量区间：按真实互素条件迁移旧证明](../sources/outputs/general_arity/odd_composite_coprime_middle_band_completion.md) | 仅旧核验登记；阅读前核对最新状态 | odd-composite-coprime-middle-band |
| [一般元数与合数研究](../sources/outputs/general_arity/README.md) | 目录入口（状态见结论卡） | — |
| [平方元数的统一正向控制器与九平均十三元](../sources/outputs/general_arity/square_arity_uniform_controller_and_nine_thirteen.md) | 仅旧核验登记；阅读前核对最新状态 | square-arity-controller-nine-thirteen |
| [十平均十六元与一族确定性三块网络](../sources/outputs/general_arity/ten_average_sixteen_and_dyadic_network_family.md) | 仅旧核验登记；阅读前核对最新状态 | ten-sixteen-dyadic-network-family |
| [十平均与十二平均17元完整G判据，以及原B公式中的自动维数](../sources/outputs/general_arity/ten_twelve_average_seventeen_complete.md) | 仅旧核验登记；阅读前核对最新状态 | ten-twelve-seventeen-complete |
| [q-平均的根格、\(S\)-算术与控制器猜想](../sources/outputs/general_arity/triple_average_q_average_arithmetic_geometry.md) | 文件已发现；未人工判定全部结论 | — |
| [统一四／六阶控制器完成2、3奇次幂临界点](../sources/outputs/general_arity/two_three_odd_power_critical_grh_completion.md) | 仅旧核验登记；阅读前核对最新状态 | two-three-odd-power-critical |
| [项目历史索引与阅读日志](../sources/outputs/history/README.md) | 目录入口（状态见结论卡） | — |
| [合数研究阅读记录](../sources/outputs/history/research_reading_log_20260915.md) | 历史目录；可能仍含有效工具 | — |
| [历史路线账本（2026-09-15归档）](../sources/outputs/history/research_routes_history_20260915.md) | 历史目录；可能仍含有效工具 | — |
| [三平均的 Iwahori--Hecke 与模形式接口](../sources/outputs/history/triple_average_hecke_interface_before_final_audit.md) | 历史目录；可能仍含有效工具 | — |
| [三平均的统一现代框架：有向托里克纤维上的 S-算术操作群胚](../sources/outputs/history/triple_average_unified_modern_framework_before_2026-09-10_revision.md) | 历史目录；可能仍含有效工具 | — |
| [二平均之后的文献进展：2018--2026 检索与可用工具](../sources/outputs/literature/averaging_literature_survey_2018_2026.md) | 来源／调查 | strategy-reassessment-20260912 |
| [二平均为何有完整判据，以及三平均卡在何处](../sources/outputs/literature/binary_vs_ternary_averaging_followup.md) | 来源／调查 | — |
| [文献调查与原证明复核](../sources/outputs/literature/README.md) | 目录入口（状态见结论卡） | — |
| [重读二平均原证、文献检索与三平均的统一证明](../sources/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md) | 来源／调查 | prime-double-triple-invariant |
| [真实返回、同余纤维与有限终端：通用引理](../sources/outputs/prime_arity/arithmetic_toolkit.md) | 已建立结论卡 | PRIME-TOTAL |
| [2p 至 3p 区间与外部定理的专项审核](../sources/outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md) | 审查记录 | EXTERNAL-ARITH |
| [2026-09-15 新进展独立审核](../sources/outputs/prime_arity/audits/prime_arity_new_results_audit_20260915.md) | 审查记录 | — |
| [九偏移完成证明的最后复核](../sources/outputs/prime_arity/audits/prime_arity_nine_offsets_completion_audit.md) | 审查记录 | nine-offsets-large-symmetric-carrier |
| [全部奇素数最优阈值的独立增量审核](../sources/outputs/prime_arity/audits/prime_arity_optimal_threshold_independent_audit_20260915.md) | 审查记录 | prime-final-independent-audit, nine-offsets-large-symmetric-carrier |
| [研究复查结论：哪些仍卡住，哪一个接口已接通](../sources/outputs/prime_arity/audits/prime_arity_research_audit_20260914.md) | 审查记录 | — |
| [全部素数 3p+10 最终上界的增量审核](../sources/outputs/prime_arity/audits/prime_arity_three_p_plus_ten_audit_20260915.md) | 审查记录 | — |
| [专项与独立审核](../sources/outputs/prime_arity/audits/README.md) | 目录入口（状态见结论卡） | — |
| [五平均十一元的完整判据：两步返回、正向周期与 Γ₀(11)](../sources/outputs/prime_arity/examples/five_average_eleven_complete.md) | 仅旧核验登记；阅读前核对最新状态 | five-average-eleven-complete |
| [五平均 (n=10) 的不可解比例实验](../sources/outputs/prime_arity/examples/five_average_n10_unsolvable_ratio.md) | 文件已发现；未人工判定全部结论 | — |
| [五平均十一元临界实验](../sources/outputs/prime_arity/examples/five_average_n11_random_experiment.md) | 仅旧核验登记；阅读前核对最新状态 | five-average-n11-random-experiment |
| [五平均十三元：已有对合接同余子群定理](../sources/outputs/prime_arity/examples/five_average_thirteen_congruence_complete.md) | 仅旧核验登记；阅读前核对最新状态 | five-thirteen-congruence |
| [五平均达到 3p：最小同余见证与碰撞总和证书](../sources/outputs/prime_arity/examples/five_average_three_p_threshold.md) | 仅旧核验登记；阅读前核对最新状态 | five-average-three-p-threshold |
| [(p=13) 临界对照：(n=26) 与 (n=27)](../sources/outputs/prime_arity/examples/p13_boundary_n26_n27_comparison.md) | 文件已发现；未人工判定全部结论 | — |
| [小素数实例与历史证据](../sources/outputs/prime_arity/examples/README.md) | 目录入口（状态见结论卡） | — |
| [七平均十五元完整G判据：两素数入口与二进 \(\Gamma_0(15)\) 覆盖](../sources/outputs/prime_arity/examples/seven_average_fifteen_complete.md) | 仅旧核验登记；阅读前核对最新状态 | composite-endpoint-transfer, seven-average-fifteen-complete |
| [七平均 (n=14) 与 (n=15) 对照实验](../sources/outputs/prime_arity/examples/seven_average_n14_vs_n15_comparison.md) | 文件已发现；未人工判定全部结论 | — |
| [七平均 (n=15) 数值证据](../sources/outputs/prime_arity/examples/seven_average_n15_numerical_evidence.md) | 文件已发现；未人工判定全部结论 | — |
| [七平均的最优最终阈值：二十元、二十二元与 N(7)=15](../sources/outputs/prime_arity/examples/seven_average_sharp_threshold_complete.md) | 仅旧核验登记；阅读前核对最新状态 | seven-average-sharp-completion |
| [七平均达到 3p+2：对称碰撞总和的完整证书](../sources/outputs/prime_arity/examples/seven_average_three_p_plus_two_threshold.md) | 仅旧核验登记；阅读前核对最新状态 | seven-average-three-p-plus-two |
| [为什么三平均的精确阈值是七：资源边界、有限周期与合法单轨道](../sources/outputs/prime_arity/examples/seven_exact_threshold_structure.md) | 已建立结论卡 | SEVEN-STRUCTURE |
| [同余群的几何解释：标记格、模曲线与权一 theta](../sources/outputs/prime_arity/geometry.md) | 文件已发现；未人工判定全部结论 | — |
| [中间带的统一降维条件与全部 r 的显式正向对合](../sources/outputs/prime_arity/history/prime_arity_band_period_and_involutions.md) | 历史目录；可能仍含有效工具 | four-prime-entry-and-band |
| [素数元平均的边界推进：预留重数、临界收尾与分组障碍](../sources/outputs/prime_arity/history/prime_arity_boundary_progress.md) | 历史目录；可能仍含有效工具 | prime-arity-boundary-progress |
| [偶数核心缺口复查：常高度乘法、有限例外与多步下降](../sources/outputs/prime_arity/history/prime_arity_core_gap_reassessment_20260915.md) | 历史目录；可能仍含有效工具 | core-gap-four-lifts |
| [p 平均临界前沿报告：方法障碍、2p+1 的结构与后续研究](../sources/outputs/prime_arity/history/prime_arity_critical_frontier_handoff.md) | 历史目录；可能仍含有效工具 | prime-power-endpoint-completion, prime-power-endpoint-entry |
| [按不同实际值数的安全整数归约](../sources/outputs/prime_arity/history/prime_arity_distinct_value_integer_reduction.md) | 历史目录；可能仍含有效工具 | distinct-entry-gaussian-transfer |
| [主余类储备：把多余类碰撞压缩到刚性例外](../sources/outputs/prime_arity/history/prime_arity_dominant_residue_reservoir.md) | 历史目录；可能仍含有效工具 | dominant-residue-reservoir |
| [反向构造端点反例：整数陷阱、最小反例与分母层](../sources/outputs/prime_arity/history/prime_arity_endpoint_counterexample_reverse.md) | 历史目录；可能仍含有效工具 | endpoint-reverse-diagnostic |
| [欧几里得见证转移：任意 h 的新阶段与最大值下降](../sources/outputs/prime_arity/history/prime_arity_euclidean_witness_transfer.md) | 历史目录；可能仍含有效工具 | euclidean-witness-transfer |
| [同一载体打包控制器完成三个低余量：3p+2、3p+4、3p+8](../sources/outputs/prime_arity/history/prime_arity_even_low_offsets_common_controller.md) | 历史目录；可能仍含有效工具 | even-low-offsets-common-controller |
| [偶数中间维数：深同余控制、二进终端与七平均十八元](../sources/outputs/prime_arity/history/prime_arity_even_middle_congruence_and_eighteen.md) | 历史目录；可能仍含有效工具 | even-interior-completion, even-middle-eighteen-congruence |
| [从 5p 到 4p：三个重值的顺序结构与 3p 边界](../sources/outputs/prime_arity/history/prime_arity_four_p_threshold.md) | 历史目录；可能仍含有效工具 | prime-arity-four-p-threshold |
| [四素因子端点入口：幂指数避让与见证合并](../sources/outputs/prime_arity/history/prime_arity_four_prime_endpoint_entry.md) | 历史目录；可能仍含有效工具 | six-prime-endpoint-entry, four-prime-entry-and-band |
| [九个低余量的真实边界与新的统一接口](../sources/outputs/prime_arity/history/prime_arity_low_offset_unified_frontier.md) | 历史目录；可能仍含有效工具 | triadic-packed-carrier-completion, three-p-plus-one-residue-four, low-offset-reflection-interface |
| [从固定保护到可交换见证：统一初始化、五步族与总和推广](../sources/outputs/prime_arity/history/prime_arity_protected_exchange_and_mass.md) | 历史目录；可能仍含有效工具 | minimal-protection-and-exchange |
| [回看三平均的合数归约与分裂素数路线](../sources/outputs/prime_arity/history/prime_arity_revisiting_ternary_factor_gaussian_route.md) | 历史目录；可能仍含有效工具 | distinct-entry-gaussian-transfer |
| [单值零和的最优集中界与极端冻结态的三步逃逸](../sources/outputs/prime_arity/history/prime_arity_sharp_concentration_and_escape.md) | 历史目录；可能仍含有效工具 | sharp-monochromatic-escape, single-value-zero-sum-conjecture |
| [六素因子入口与剩余范围：五个坏指数类不能覆盖](../sources/outputs/prime_arity/history/prime_arity_six_prime_endpoint_entry.md) | 历史目录；可能仍含有效工具 | six-prime-endpoint-entry |
| [任意 p 平均路线重评估：最有希望的接口与文献边界](../sources/outputs/prime_arity/history/prime_arity_strategy_reassessment_20260912.md) | 历史目录；可能仍含有效工具 | strategy-reassessment-20260912 |
| [直接面向 3p：长零和自由序列、双锚点与同余基的实际和](../sources/outputs/prime_arity/history/prime_arity_three_p_additive_interface.md) | 历史目录；可能仍含有效工具 | three-p-two-anchor-interface |
| [小载体的正向逆与可解商分离：3p+1 的一个统一完成族](../sources/outputs/prime_arity/history/prime_arity_three_p_plus_one_residue_four.md) | 历史目录；可能仍含有效工具 | three-p-plus-one-residue-four |
| [距离 N(p)≤3p 的真实缺口：核心陷阱、两步逃逸与第二个对合](../sources/outputs/prime_arity/history/prime_arity_three_p_remaining_gap.md) | 历史目录；可能仍含有效工具 | upper-band-descent-boundary |
| [三进低余量：共同 CRT 终端与一次局部筛选](../sources/outputs/prime_arity/history/prime_arity_triadic_packed_carrier_completion.md) | 历史目录；可能仍含有效工具 | triadic-packed-carrier-completion, nine-offset-residue-one |
| [单位见证的补回阶段：Hilbert 基、精确容量与相邻重值障碍](../sources/outputs/prime_arity/history/prime_arity_unit_witness_replenishment.md) | 历史目录；可能仍含有效工具 | unit-witness-replenishment |
| [素数路线历史与方法障碍](../sources/outputs/prime_arity/history/README.md) | 目录入口（状态见结论卡） | — |
| [素数平均最优最终阈值：总证明与技术依赖](../sources/outputs/prime_arity/proof.md) | 已建立结论卡 | PRIME-TOTAL |
| [合数端点核心的统一闭合：有限指数、同余子群与二进根](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md) | 已建立结论卡 | EXTERNAL-ARITH |
| [全部内部偶余量的完整证明：有限逆提升、局部循环与尺度](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md) | 已建立结论卡 | PRIME-EVEN-INTERIOR |
| [2p 与 4p 之间：三块运输解掉 3p，并缩小双重值障碍](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md) | 已建立结论卡 | PRIME-3P |
| [全部 3p-1 的统一完成与五平均最优阈值](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md) | 已建立结论卡 | PRIME-3PM1 |
| [全部 2p+2：可逆缩放、三步反射与两次 CRT 返回](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md) | 已建立结论卡 | PRIME-2P2 |
| [任意素数的奇余量中间核：两个对合、主同余控制与小代表](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_uniform_odd_middle_cores.md) | 仅旧核验登记；阅读前核对最新状态 | unrestricted-endpoint-entry, uniform-odd-middle-cores |
| [无条件端点与全部奇数中间维数：三单点交换子补齐入口](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md) | 仅旧核验登记；阅读前核对最新状态 | three-p-minus-one-completion, even-interior-completion, unrestricted-endpoint-entry |
| [2p到3p：全输入入口与完成证明](../sources/outputs/prime_arity/proofs/lower_band/README.md) | 目录入口（状态见结论卡） | — |
| [素数主证明技术附录](../sources/outputs/prime_arity/proofs/README.md) | 目录入口（状态见结论卡） | — |
| [素数元平均的充分大维数定理](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_averaging_large_dimension.md) | 仅旧核验登记；阅读前核对最新状态 | prime-arity-large-dimension |
| [统一补齐 4p 上方的 d_p 尾部：N(p)<=3p+10](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_four_p_tail_completion.md) | 仅旧核验登记；阅读前核对最新状态 | upper-band-small-prime-interface, four-p-tail-completion |
| [逆 EGZ 真正降低阈值：4p-2+d，以及向 7p/2 推进的具体接口](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_inverse_egz_threshold.md) | 仅旧核验登记；阅读前核对最新状态 | four-p-tail-completion, inverse-egz-threshold |
| [素数元平均的线性阈值与 2p 边界](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_linear_threshold.md) | 仅旧核验登记；阅读前核对最新状态 | prime-arity-linear-threshold |
| [尾部上界与最优性下界](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/README.md) | 目录入口（状态见结论卡） | — |
| [容量、单位密度与局部提升：全部素数的 3p+10 阈值](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_all_prime_three_p_plus_ten.md) | 仅旧核验登记；阅读前核对最新状态 | three-p-minus-one-completion, upper-band-small-prime-interface |
| [九个低偏移的共同完成：改用大载体与两个等大块](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md) | 仅旧核验登记；阅读前核对最新状态 | transverse-root-shallow-lifting, carrier-interval-reduction, prime-final-independent-audit, nine-offsets-large-symmetric-carrier |
| [上半带与 6 互素维数的完整证明](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_coprime_six_complete.md) | 仅旧核验登记；阅读前核对最新状态 | upper-band-unrestricted-completion, upper-band-coprime-six-complete |
| [上半带四返回：统一双向根与深主同余控制](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_four_return_congruence.md) | 仅旧核验登记；阅读前核对最新状态 | upper-band-unrestricted-completion, upper-band-four-return-congruence |
| [一次重叠替换载体：统一补齐靠近 4p 的两条边界](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_overlap_completion.md) | 仅旧核验登记；阅读前核对最新状态 | upper-band-small-prime-interface, four-p-tail-completion, upper-band-overlap-completion |
| [3p 到 4p：任意素因子数的原位置三值归约](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_three_value_reduction.md) | 仅旧核验登记；阅读前核对最新状态 | even-low-offsets-common-controller, upper-band-overlap-completion, upper-band-unrestricted-completion, upper-band-three-value-reduction |
| [上半带内部区间的无条件完整证明](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_unrestricted_completion.md) | 仅旧核验登记；阅读前核对最新状态 | nine-offset-residue-one, even-low-offsets-common-controller, four-p-tail-completion, upper-band-overlap-completion, upper-band-unrestricted-completion |
| [3p以上：核心、反射与完成证明](../sources/outputs/prime_arity/proofs/upper_band/README.md) | 目录入口（状态见结论卡） | — |
| [素数平均：当前证明入口](../sources/outputs/prime_arity/README.md) | 目录入口（状态见结论卡） | — |
| [反射容量的一维整数区间与最小缺失单位：削减九偏移证书](../sources/outputs/prime_arity/structure/carrier_interval_and_unit_descent.md) | 仅旧核验登记；阅读前核对最新状态 | carrier-interval-reduction |
| [从整格拼接到正运输：哪些结构使同余群和真实逆自然出现](../sources/outputs/prime_arity/structure/integral_gluing_and_positive_transport.md) | 文件已发现；未人工判定全部结论 | — |
| [原子首位乘积与Kneser边界：2p+1的组合突变](../sources/outputs/prime_arity/structure/padic_leading_symbols_and_kneser_boundary.md) | 仅旧核验登记；阅读前核对最新状态 | padic-quadratic-group |
| [p进翻译：原子退化、加一动力学与典范分支的适用边界](../sources/outputs/prime_arity/structure/padic_places_and_canonical_branches.md) | 文件已发现；未人工判定全部结论 | — |
| [二次代数群统一局部返回：形式对数、低素数缺陷与有限轨道](../sources/outputs/prime_arity/structure/padic_quadratic_group_and_orbit_defect.md) | 仅旧核验登记；阅读前核对最新状态 | padic-quadratic-group |
| [二类型碰撞的整数格证明：同余单类闭包与 3p+1 的三重值分支](../sources/outputs/prime_arity/structure/prime_arity_binary_collision_lattice.md) | 仅旧核验登记；阅读前核对最新状态 | binary-collision-lattice |
| [全碰撞单位分支的统一补回：载体、重叠与整数配比](../sources/outputs/prime_arity/structure/prime_arity_complete_unit_collision_recovery.md) | 仅旧核验登记；阅读前核对最新状态 | complete-local-unit-recovery |
| [素数元平均在临界维数附近的多种结构](../sources/outputs/prime_arity/structure/prime_arity_critical_structures.md) | 文件已发现；未人工判定全部结论 | — |
| [从统一能量到整数方向下降：2p+2 的一族完整证明](../sources/outputs/prime_arity/structure/prime_arity_energy_and_dyadic_neighbour.md) | 仅旧核验登记；阅读前核对最新状态 | carrier-energy-dyadic-neighbour |
| [能量唯一性之后：可改进的不变量与上半带整数出口](../sources/outputs/prime_arity/structure/prime_arity_invariant_improvements_and_core_exit.md) | 仅旧核验登记；阅读前核对最新状态 | core-exit-potential-scope |
| [2p+1 与 3p 之间的相对尺度接口](../sources/outputs/prime_arity/structure/prime_arity_middle_band_relative_scale.md) | 已建立结论卡 | WINDOW-MEAN |
| [来源关系、动态见证与整数返回阶段：三条改进的证明及边界](../sources/outputs/prime_arity/structure/prime_arity_provenance_dynamic_and_integer_stages.md) | 仅旧核验登记；阅读前核对最新状态 | provenance-dynamic-integer-stages |
| [允许块形状变化的整数检查点势](../sources/outputs/prime_arity/structure/prime_arity_shape_changing_integer_potential.md) | 仅旧核验登记；阅读前核对最新状态 | shape-changing-integer-potential |
| [形状变化势：已核对的零和文献与实际适用范围](../sources/outputs/prime_arity/structure/prime_arity_shape_potential_literature_interface.md) | 来源／调查 | — |
| [重数弱化的锐障碍与一位额外精度的必要性](../sources/outputs/prime_arity/structure/prime_arity_sharp_repetition_and_precision_barriers.md) | 仅旧核验登记；阅读前核对最新状态 | sharp-multiplicity-precision |
| [单值零和：旧猜想撤回与正确结构](../sources/outputs/prime_arity/structure/prime_arity_single_value_zero_sum_conjecture.md) | 仅旧核验登记；阅读前核对最新状态 | single-value-zero-sum-conjecture |
| [任意素数的碰撞结构：两组相加、总和窗口与高重数分类](../sources/outputs/prime_arity/structure/prime_arity_uniform_collision_structure.md) | 仅旧核验登记；阅读前核对最新状态 | uniform-collision-structure |
| [素数证明的结构与简化](../sources/outputs/prime_arity/structure/README.md) | 目录入口（状态见结论卡） | — |
| [三个共轭根替代高阶轨道：浅同余层与固定二进修正](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md) | 仅旧核验登记；阅读前核对最新状态 | transverse-root-shallow-lifting |
| [已解维数怎样组合：统一造零收尾与同余群背后的均值格](../sources/outputs/prime_arity/tools/prime_arity_interpolation_and_lattice_structure.md) | 仅旧核验登记；阅读前核对最新状态 | prime-arity-zero-trigger-bridge |
| [中间带的统一整数格、终端族与原位置入口](../sources/outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md) | 仅旧核验登记；阅读前核对最新状态 | two-p-plus-two-uniform, unrestricted-endpoint-entry, two-prime-neighbour-complete, even-core-dyadic-depth, uniform-two-block-entry |
| [临界双块的局部几何、素数幂完整证明与 theta 联系](../sources/outputs/prime_arity/tools/prime_power_endpoint_and_critical_geometry.md) | 仅旧核验登记；阅读前核对最新状态 | prime-power-endpoint-completion |
| [已使用的核心与均值格工具](../sources/outputs/prime_arity/tools/README.md) | 目录入口（状态见结论卡） | — |
| [临界双块系统的统一正向控制器：不再搜索种子周期](../sources/outputs/prime_arity/tools/uniform_endpoint_positive_controller.md) | 仅旧核验登记；阅读前核对最新状态 | uniform-endpoint-controller |
| [本次整理的阅读、修改与核验范围](../sources/outputs/prime_arity/verification.md) | 已建立结论卡 | PRIME-TOTAL |
| [成果与研究索引](../sources/outputs/README.md) | 目录入口（状态见结论卡） | — |
| [三平均旧算术实例](../sources/outputs/triple_average/arithmetic_cases/README.md) | 目录入口（状态见结论卡） | — |
| [十八元及其三进塔：调用十二元定理的配对归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_eighteen_via_twelve_complete.md) | 仅旧核验登记；阅读前核对最新状态 | two-three-smooth-complete, n18-via-twelve-complete |
| [三平均的十一元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_eleven_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n11-complete |
| [十五元完整判据：模八轮转与可解子块](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n15-via-subblocks-complete |
| [59元完整判据与跨维数结构](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifty_nine_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n59-complete |
| [53元完整判据：三进根与完整主元同余](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifty_three_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n53-complete |
| [四十一元完整判据：三因子对合与级41同余证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_one_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n41-complete |
| [四十七元完整判据：尖点平移与局部化根群消元](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_seven_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n47-complete |
| [十四元完整判据：图论核心与512类余数桥](../sources/outputs/triple_average/arithmetic_cases/triple_average_fourteen_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n14-complete |
| [十九元完整判据：通用十五元调用与级19同余子群](../sources/outputs/triple_average/arithmetic_cases/triple_average_nineteen_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n19-complete, bn-integer-template-compiler |
| [十七元完整判据：正向逆元、级17同余子群与唯一合法尖点](../sources/outputs/triple_average/arithmetic_cases/triple_average_seventeen_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n17-complete, b17-old-integral-return-audit |
| [十三元完整判据：可逆宏、同余子群与有限尖点法](../sources/outputs/triple_average/arithmetic_cases/triple_average_thirteen_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n13-complete, cyclotomic-macros |
| [十二元完整判据：正向宏与指数 12 的模群子群](../sources/outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | two-three-smooth-complete, n15-via-subblocks-complete, n18-via-twelve-complete, n12-complete |
| [二十五元完整判据：级25子群与奇数归约的最后小基例](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n25-complete |
| [二十九元完整判据：三因子正向周期与级29同余群](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n29-complete, nonsplit-projective-layer-boundary |
| [二十三元完整判据：含2因子的正向周期与级23同余子群](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md) | 仅旧核验登记；阅读前核对最新状态 | n23-complete, bn-integer-template-compiler |
| [B_n 参数无关子问题模板编译器](../sources/outputs/triple_average/history/ai3_bn_template_compiler.md) | 历史目录；可能仍含有效工具 | ai3-template-report-audit |
| [多危险素数三幂核的链间耦合与加权和转移](../sources/outputs/triple_average/history/ai3_multprime_chain_report.md) | 历史目录；可能仍含有效工具 | — |
| [三平均研究历史](../sources/outputs/triple_average/history/README.md) | 目录入口（状态见结论卡） | — |
| [三平均的继续研究：正确级联、反向分拆编码与对数界的核心障碍](../sources/outputs/triple_average/history/ternary_averaging_continued_research.md) | 历史目录；可能仍含有效工具 | — |
| [三平均的进一步结构：五元精确递归、三进连分数与判定边界](../sources/outputs/triple_average/history/ternary_averaging_deeper_results.md) | 历史目录；可能仍含有效工具 | cascade-bound, n5-bounded-search |
| [三平均的进一步推进：二字母逆树、严格高度枚举与对数界的剩余核心](../sources/outputs/triple_average/history/ternary_averaging_further_progress.md) | 历史目录；可能仍含有效工具 | — |
| [三平均问题的新结构：三进支持集、提升机制与五元特殊性](../sources/outputs/triple_average/history/ternary_averaging_new_insights.md) | 历史目录；可能仍含有效工具 | — |
| [仿射交换子理想：从可逆宏预测整个根参数族](../sources/outputs/triple_average/history/triple_average_affine_commutator_ideal.md) | 历史目录；可能仍含有效工具 | AFFINE-IDEAL |
| [所有偶维 B 核的统一减半定理](../sources/outputs/triple_average/history/triple_average_all_even_B_kernel_halving.md) | 历史目录；可能仍含有效工具 | all-even-B-kernel-halving |
| [三平均任意维数的全局视角：有限基维数究竟说明了什么](../sources/outputs/triple_average/history/triple_average_arbitrary_n_outlook.md) | 历史目录；可能仍含有效工具 | — |
| [三平均的算术几何结构：射影投影、二次型与 adelic 高度](../sources/outputs/triple_average/history/triple_average_arithmetic_geometry_view.md) | 历史目录；可能仍含有效工具 | general-lifting, arithmetic-geometry-structure |
| [外部 audit 的修订与证据登记](../sources/outputs/triple_average/history/triple_average_audit_resolution_2026-09-09.md) | 历史目录；可能仍含有效工具 | standard-kernel-interface, search-contracts |
| [\(\mathcal B_{12}\) 二维核有限实验](../sources/outputs/triple_average/history/triple_average_b12_kernel_experiment.md) | 历史目录；可能仍含有效工具 | b12-complete-bounded-domain |
| [B12 六步局部下降与二次序导子塔](../sources/outputs/triple_average/history/triple_average_b12_six_step_and_conductor_tower.md) | 历史目录；可能仍含有效工具 | b12-six-step-local-branches, b12-return-frontier-certificates |
| [绕开 B17 调用库封闭域的跨核桥](../sources/outputs/triple_average/history/triple_average_b17_cross_stratum_escape.md) | 历史目录；可能仍含有效工具 | b17-cross-stratum-escape |
| [B17 的带条件子问题返回实验](../sources/outputs/triple_average/history/triple_average_b17_guarded_subproblem_experiment.md) | 历史目录；可能仍含有效工具 | b17-guarded-library-trap, b17-guarded-subproblem-experiment |
| [B21 深度五性能复核与整数状态商](../sources/outputs/triple_average/history/triple_average_b21_integer_search_optimization.md) | 历史目录；可能仍含有效工具 | — |
| [47元当前模板库的精确周期边界](../sources/outputs/triple_average/history/triple_average_b47_cycle_frontier.md) | 历史目录；可能仍含有效工具 | b47-short-cycle-boundary |
| [47元新正向对合与三进平移群：模板内部的一步扩展](../sources/outputs/triple_average/history/triple_average_b47_extra_atom_and_adjoint.md) | 历史目录；可能仍含有效工具 | b47-extra-atom-involutions, adjoint-return-domain-audit |
| [三平均的本质结构：重写系统、托里克关系与有限时间共识](../sources/outputs/triple_average/history/triple_average_barycentric_toric_view.md) | 历史目录；可能仍含有效工具 | — |
| [危险支持集的图论核心：从 n-3d-1 提高到 n-d-2](../sources/outputs/triple_average/history/triple_average_blocker_graph_core.md) | 历史目录；可能仍含有效工具 | n14-complete, blocker-graph-safe-core |
| [三幂几何链上的 Burau 群：任意秩可逆宏定理](../sources/outputs/triple_average/history/triple_average_burau_power_chain.md) | 历史目录；可能仍含有效工具 | burau-power-chain, cyclotomic-macros |
| [(t=4,s=3) Burau 高秩算术性审计](../sources/outputs/triple_average/history/triple_average_burau_rank4_arithmetic_audit.md) | 历史目录；可能仍含有效工具 | — |
| [载体扫掠催化器：从七元 Artin 中心到十元局部 SL3](../sources/outputs/triple_average/history/triple_average_carrier_sweep_catalyst.md) | 历史目录；可能仍含有效工具 | carrier-sweep-catalyst, carrier-catalyst-local-descent, carrier-collision-global-interface |
| [三进扩张修复宏与严格算术接口](../sources/outputs/triple_average/history/triple_average_carry_repair_and_arithmetic_interface.md) | 历史目录；可能仍含有效工具 | bn-arithmetic-structure, bn-symbolic-returns-depth5 |
| [同余子群是否是通用方法：有限轨道原则与严格边界](../sources/outputs/triple_average/history/triple_average_congruence_method_scope.md) | 历史目录；可能仍含有效工具 | prime-congruence-structure, finite-orbit-method-boundary |
| [多危险素数的覆盖设计：为何局部安全下降不能直接统一](../sources/outputs/triple_average/history/triple_average_covering_design_obstruction.md) | 历史目录；可能仍含有效工具 | — |
| [对角资源压缩：根群加一个剩余单位种子](../sources/outputs/triple_average/history/triple_average_diagonal_resource_reduction.md) | 历史目录；可能仍含有效工具 | — |
| [数字算子的完整同余群：平衡生成、循环扩张与有理轨道分类](../sources/outputs/triple_average/history/triple_average_digit_congruence_group.md) | 历史目录；可能仍含有效工具 | balanced-digit-congruence-group |
| [等载体形式冻结定理：SL--交换--SL 三段正规形](../sources/outputs/triple_average/history/triple_average_equal_carrier_formal_freezing.md) | 历史目录；可能仍含有效工具 | equal-carrier-formal-freezing |
| [偶维 B 核的八元归并减半桥](../sources/outputs/triple_average/history/triple_average_even_kernel_halving_bridge.md) | 历史目录；可能仍含有效工具 | all-even-B-kernel-halving, n14-complete, even-kernel-halving |
| [偶次返回：参数交换与宽度四根](../sources/outputs/triple_average/history/triple_average_even_return_root_interface.md) | 历史目录；可能仍含有效工具 | — |
| [精确返回的支撑刚性：载体必须最后混合](../sources/outputs/triple_average/history/triple_average_exact_return_support_rigidity.md) | 历史目录；可能仍含有效工具 | — |
| [Hecke 与模符号路线的最后检验](../sources/outputs/triple_average/history/triple_average_final_hecke_audit.md) | 历史目录；可能仍含有效工具 | OLD-HECKE-AUDIT |
| [原维数平坦核的统一算术性：显式幺幂与高秩初等群](../sources/outputs/triple_average/history/triple_average_flat_star_arithmeticity.md) | 历史目录；可能仍含有效工具 | flat-star-formal-arithmeticity |
| [三平均的任意维数框架：根格、二维核与三进维数提升](../sources/outputs/triple_average/history/triple_average_general_n_synthesis.md) | 历史目录；可能仍含有效工具 | general-lifting, isolated-prime-core |
| [三平均的整体复审：六元有限判定与七八元完整判据](../sources/outputs/triple_average/history/triple_average_global_breakthrough.md) | 历史目录；可能仍含有效工具 | — |
| [三进无关部分只有一个素数时的统一降维](../sources/outputs/triple_average/history/triple_average_isolated_prime_reduction.md) | 历史目录；可能仍含有效工具 | isolated-prime-core |
| [Hecke 代数恒等式与尚未建立的模形式接口](../sources/outputs/triple_average/history/triple_average_iwahori_hecke_modular_interface.md) | 历史目录；可能仍含有效工具 | final-hecke-manin-audit, iwahori-hecke-modular-interface, nonsplit-hecke-chart-boundary, atomic-hecke-wall-boundary, b71-symbolic-directed-terminal-cover |
| [标准核接口与自守路线的统一说明](../sources/outputs/triple_average/history/triple_average_kernel_interface_and_automorphic_route.md) | 历史目录；可能仍含有效工具 | — |
| [从局部化根群到素数同余群：统一生成定理](../sources/outputs/triple_average/history/triple_average_localized_iwahori_generation.md) | 历史目录；可能仍含有效工具 | localized-iwahori-generation |
| [三平均有限步可达性：研究总纲与当前路线](../sources/outputs/triple_average/history/triple_average_master_summary.md) | 历史目录；可能仍含有效工具 | — |
| [混合单点迹零返回：全非分裂素数的单一条件归约](../sources/outputs/triple_average/history/triple_average_mixed_singleton_controller.md) | 历史目录；可能仍含有效工具 | OLD-TRACE-RETURN |
| [Modern Frame 的可用部分与严格化契约](../sources/outputs/triple_average/history/triple_average_modern_framework_review_and_contract.md) | 历史目录；可能仍含有效工具 | b17-guarded-subproblem-experiment |
| [有限模正向化与高度的严格边界](../sources/outputs/triple_average/history/triple_average_modular_height_barrier.md) | 历史目录；可能仍含有效工具 | modular-primitive-height-barrier |
| [多个危险素数仍给出线性高重数核心](../sources/outputs/triple_average/history/triple_average_multi_prime_core.md) | 历史目录；可能仍含有效工具 | multi-prime-core |
| [固定词一致性障碍：统一证明必须依赖状态或降维](../sources/outputs/triple_average/history/triple_average_no_oblivious_consensus.md) | 历史目录；可能仍含有效工具 | — |
| [非分裂Reynolds层的完整置换影子：交错群](../sources/outputs/triple_average/history/triple_average_nonsplit_alternating_shadow.md) | 历史目录；可能仍含有效工具 | — |
| [非分裂素数的可预测结构：17至59证书后的综合](../sources/outputs/triple_average/history/triple_average_nonsplit_prime_structure_synthesis.md) | 历史目录；可能仍含有效工具 | — |
| [非分裂三阶轨道与双载体：原位置实现](../sources/outputs/triple_average/history/triple_average_nonsplit_punctured_orbits.md) | 历史目录；可能仍含有效工具 | — |
| [合数的统一因子归约：奇数乘法闭包与八整除族](../sources/outputs/triple_average/history/triple_average_odd_composite_factor_closure.md) | 历史目录；可能仍含有效工具 | odd-composite-factor-closure |
| [奇次返回的容量族与53元目标](../sources/outputs/triple_average/history/triple_average_odd_return_capacity_family.md) | 历史目录；可能仍含有效工具 | — |
| [一次三份复制稳定化：离散梯度、Hilbert 90 与平衡初等变换](../sources/outputs/triple_average/history/triple_average_one_tripling_stabilization.md) | 历史目录；可能仍含有效工具 | one-tripling-stabilization |
| [统一混合返回的原位置分解前沿](../sources/outputs/triple_average/history/triple_average_original_position_factorization_frontier.md) | 历史目录；可能仍含有效工具 | — |
| [其他 AI 报告复核：可用的局部到整体接口](../sources/outputs/triple_average/history/triple_average_other_ai_local_global_review.md) | 历史目录；可能仍含有效工具 | other-ai-local-global-synthesis, ai3-template-report-audit, ai5-synchronized-replica-audit |
| [等值载体核与二进重分组：一个统一的保秩正向宏](../sources/outputs/triple_average/history/triple_average_paired_carrier_reset.md) | 历史目录；可能仍含有效工具 | paired-carrier-two-adic-reset |
| [参数周期刚性：为什么逐素数短周期不能成为统一证明](../sources/outputs/triple_average/history/triple_average_parametric_cycle_rigidity.md) | 历史目录；可能仍含有效工具 | PARAMETRIC-RIGIDITY |
| [置换剩余像与局部耦合：九十一元旧容器的严格修正](../sources/outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md) | 历史目录；可能仍含有效工具 | N91-CONTAINER-CORRECTION |
| [正向根群饱和：47元全库逆元与统一素数策略](../sources/outputs/triple_average/history/triple_average_positive_root_saturation.md) | 历史目录；可能仍含有效工具 | b47-root-activation |
| [(n-4) 为三幂时的统一返回宏](../sources/outputs/triple_average/history/triple_average_power_block_macro.md) | 历史目录；可能仍含有效工具 | power-block-macro |
| [任意维数的三幂分块压缩：把一般输入降到对数秩标准核](../sources/outputs/triple_average/history/triple_average_power_partition_reduction.md) | 历史目录；可能仍含有效工具 | power-partition-compression |
| [素数维数为什么出现同余子群：稳定子定理与尺度周期](../sources/outputs/triple_average/history/triple_average_prime_congruence_structure.md) | 历史目录；可能仍含有效工具 | prime-congruence-structure |
| [先解素数再归约合数：可行主线、严格接口与三进进位桥](../sources/outputs/triple_average/history/triple_average_prime_first_factor_reduction.md) | 历史目录；可能仍含有效工具 | prime-factor-carry-bridge |
| [素数情况的完整证明路线与剩余猜想](../sources/outputs/triple_average/history/triple_average_prime_proof_roadmap.md) | 历史目录；可能仍含有效工具 | — |
| [全局标量周期的谱判据：Newton 多边形、Kronecker 与分圆验证](../sources/outputs/triple_average/history/triple_average_projective_spectral_balance.md) | 历史目录；可能仍含有效工具 | projective-spectral-balance |
| [三份复制消去：同步路径、算术商与严格边界](../sources/outputs/triple_average/history/triple_average_replica_elimination_research.md) | 历史目录；可能仍含有效工具 | ai5-synchronized-replica-audit |
| [研究复核：目标平均值、动力学方向与算法边界](../sources/outputs/triple_average/history/triple_average_research_corrections.md) | 历史目录；可能仍含有效工具 | stabilization-theorem, n91-congruence-container, n91-corrected-witness, n91-cusp-depth4 |
| [三平均研究最新总览与交接说明（2026-09-09）](../sources/outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md) | 历史目录；可能仍含有效工具 | n91-congruence-container, n91-corrected-witness, n91-cusp-depth4, n91-cusp29-depth5 |
| [更内在的代数对象：Reynolds 半群、交叉计数与判别式对偶](../sources/outputs/triple_average/history/triple_average_reynolds_hecke_hodge.md) | 历史目录；可能仍含有效工具 | reynolds-hodge-structure, contingency-layer-semigroup |
| [非分裂素数路线复盘：停止局部拼接，返回二维除法结构](../sources/outputs/triple_average/history/triple_average_route_reassessment_2026-09-11.md) | 历史目录；可能仍含有效工具 | — |
| [B12、B15、B18、B21 的统一有限比较](../sources/outputs/triple_average/history/triple_average_single_prime_kernel_comparison.md) | 历史目录；可能仍含有效工具 | bn-comparison-depth4, b15-two-depth5, b21-depth5 |
| [所有 p=1 mod3 素数的完整判据：高斯周期正向控制器](../sources/outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md) | 历史目录；可能仍含有效工具 | split-prime-gaussian-controller |
| [任意维数的新统一结果：复制稳定化、双随机矩阵与消去猜想](../sources/outputs/triple_average/history/triple_average_stabilization_theorem.md) | 历史目录；可能仍含有效工具 | STABILIZATION |
| [结构图景复核：可用的局部到整体机制及数域边界](../sources/outputs/triple_average/history/triple_average_structural_picture_audit.md) | 历史目录；可能仍含有效工具 | b29-current-cycle-boundary, one-tripling-stabilization |
| [三平均问题的局部算术轨道图景：结构性猜测与证明路线](../sources/outputs/triple_average/history/triple_average_structural_picture_conjecture.md) | 历史目录；可能仍含有效工具 | — |
| [子问题调用的缺失素数障碍与奇素数维数](../sources/outputs/triple_average/history/triple_average_subproblem_prime_obstruction.md) | 历史目录；可能仍含有效工具 | subproblem-prime-obstruction |
| [主线与三个并行研究方向的交接](../sources/outputs/triple_average/history/triple_average_team_handoff_2026-09-10.md) | 历史目录；可能仍含有效工具 | — |
| [参数无关宏编译器与范数环面：从 B17 走向任意 n](../sources/outputs/triple_average/history/triple_average_template_compiler_and_torus.md) | 历史目录；可能仍含有效工具 | — |
| [十三元二维核：已得到的真实宏与剩余的三进高度问题](../sources/outputs/triple_average/history/triple_average_thirteen_macro_frontier.md) | 历史目录；可能仍含有效工具 | — |
| [三进运输稳定化：双随机返回与复制消去的精确接口](../sources/outputs/triple_average/history/triple_average_triadic_transport_stabilization.md) | 历史目录；可能仍含有效工具 | — |
| [十二元四宏的参数延拓及其关系边界](../sources/outputs/triple_average/history/triple_average_twelve_macro_family_extension.md) | 历史目录；可能仍含有效工具 | — |
| [有限模控制的正向实现：所有 n=5 mod6 的二例外归约](../sources/outputs/triple_average/history/triple_average_two_carrier_modular_bridge.md) | 历史目录；可能仍含有效工具 | two-carrier-modular-bridge |
| [两个统一迹零返回：根10与有限局部终端](../sources/outputs/triple_average/history/triple_average_two_trace_zero_returns.md) | 历史目录；可能仍含有效工具 | OLD-TRACE-RETURN |
| [三平均的统一框架：带局部条件的有向操作与算术轨道](../sources/outputs/triple_average/history/triple_average_unified_modern_framework.md) | 历史目录；可能仍含有效工具 | — |
| [参数无关子问题调用：局部化整数模判据与十七元新宏](../sources/outputs/triple_average/history/triple_average_universal_subproblem_lattice.md) | 历史目录；可能仍含有效工具 | b17-universal-subproblem-lattice |
| [统一迹零返回目标：从孤立周期到参数恒等式](../sources/outputs/triple_average/history/triple_average_universal_trace_zero_target.md) | 历史目录；可能仍含有效工具 | OLD-TRACE-RETURN |
| [危险素数的见证重置：局部约分为何必须纳入一般算法](../sources/outputs/triple_average/history/triple_average_witness_reset_lemma.md) | 历史目录；可能仍含有效工具 | multi-prime-core |
| [可填充三幂块的统一收尾](../sources/outputs/triple_average/history/triple_average_zero_padding_theorem.md) | 历史目录；可能仍含有效工具 | zero-padding |
| [三平均直接证明与小基例](../sources/outputs/triple_average/proofs/README.md) | 目录入口（状态见结论卡） | — |
| [双三重值不变量的任意维数直接证明](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md) | 已建立结论卡 | TRIPLE-ALL |
| [任意维数严格归约到素数：低二进重数的最后接口](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_to_primes.md) | 仅旧核验登记；阅读前核对最新状态 | all-dimensions-prime-reduction, even-prime-power-halving |
| [素数维数的双三重值不变量：一位额外三进精度证明](../sources/outputs/triple_average/proofs/triple_average_prime_double_triple_invariant.md) | 仅旧核验登记；阅读前核对最新状态 | prime-double-triple-invariant |
| [三平均的新突破：七元与八元的完整判据](../sources/outputs/triple_average/proofs/triple_average_seven_eight_complete.md) | 已建立结论卡 | TRIPLE-BASES |
| [三平均的十元完整判据](../sources/outputs/triple_average/proofs/triple_average_ten_complete.md) | 已建立结论卡 | TRIPLE-BASES |
| [全部二三光滑维数的完整判据](../sources/outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md) | 仅旧核验登记；阅读前核对最新状态 | two-three-smooth-complete |
| [三平均：直接证明与原算术路线](../sources/outputs/triple_average/README.md) | 目录入口（状态见结论卡） | — |

## research

| 文件 | 角色 | 结论卡／旧核验ID |
|---|---|---|
| [从固定群到格对应：本原直线的阿代尔描述与两端点共同CRT](../sources/research/prime_arity_padic/adelic_primitive_lines_and_common_endpoint_preparation.md) | 已建立结论卡 | PRIME-ADELIC |
| [Burau辫子群路线复盘：哪些仍可用，哪些不适合当前临界带](../sources/research/prime_arity_padic/burau_route_reassessment.md) | 已建立结论卡 | BURAU-REASSESS |
| [用载体的 p 进格位移审查统一机制](../sources/research/prime_arity_padic/carrier_balance_and_uniform_mechanism.md) | 已建立结论卡 | PRIME-CARRIER-OBSTRUCTION |
| [载体更新的统一四步式：配平与横向耦合必须同时存在](../sources/research/prime_arity_padic/carrier_refresh_normal_form.md) | 已建立结论卡 | PRIME-BALANCE |
| [九偏移证书的结构分解：奇偏移与全偶载体](../sources/research/prime_arity_padic/certificate_anatomy_and_odd_offsets.md) | 已建立结论卡 | PRIME-CERTIFICATE-ANATOMY |
| [临界带的共同形状与整数关系：从局部配方到可比较的结构](../sources/research/prime_arity_padic/common_shape_integer_relations_and_mainstream_structure.md) | 已建立结论卡 | PRIME-COMMON-SHAPE |
| [五条返回的统一根供应：守恒交换的容量定理与114组剩余](../sources/research/prime_arity_padic/conservation_capacity_and_five_return_supply.md) | 已建立结论卡 | PRIME-FIVE-RETURNS |
| [守恒交换直接产生n根：替代辅助13的群论修补](../sources/research/prime_arity_padic/conservation_exchange_removes_auxiliary13.md) | 已建立结论卡 | PRIME-CONSERVATION13 |
| [一个跨过3p的完整共同证明：同一反射、根与终端接口](../sources/research/prime_arity_padic/critical_band_common_controller.md) | 已建立结论卡 | PRIME-CRITICAL-CONTROLLER |
| [同行列式纤维与有限格对应：直接根、跨格准备和终止接口](../sources/research/prime_arity_padic/determinant_fibers_and_finite_lattice_correspondences.md) | 已建立结论卡 | PRIME-FIBER |
| [2p+1端点：G的判别式交环、虚二次能量与全部可逆射影轨道](../sources/research/prime_arity_padic/endpoint_discriminant_orders_and_G_orbits_20260917.md) | 已建立结论卡 | PRIME-ENDPOINT-GEOMETRY |
| [深核只建一次：有限对应自动群化与不扩环的共同终端](../sources/research/prime_arity_padic/finite_orbit_completion_without_ring_extension.md) | 已建立结论卡 | PRIME-FINITE-TERMINAL |
| [三平均五元：当前成果、统一理解与真正剩余问题](../sources/research/prime_arity_padic/five_averaging_progress_summary_20260917.md) | 已建立结论卡 | FIVE-SUMMARY, FIVE-ESCAPE-OPEN |
| [五元的新分界：有界切换的有效有限性，以及代数对应为何不自动扩张](../sources/research/prime_arity_padic/five_bounded_switches_and_correspondence_degree_20260917.md) | 已建立结论卡 | FIVE-BOUNDED-RUNS |
| [统一逃离小分母：固定任意重复模板已证明，任意正词仍有缺口](../sources/research/prime_arity_padic/five_bounded_templates_uniform_escape_20260917.md) | 已建立结论卡 | FIVE-TEMPLATE-ESCAPE, FIVE-ESCAPE-OPEN |
| [全五元的统一算术形式，以及单一范数路线的严格障碍](../sources/research/prime_arity_padic/five_complete_arithmetic_normal_form_20260916.md) | 已建立结论卡 | FIVE-NORMAL-FORM |
| [五元结构的继续推进：普通三进数字的有限状态障碍与单变量代数对应](../sources/research/prime_arity_padic/five_digit_obstruction_and_rational_correspondence_20260916.md) | 已建立结论卡 | FIVE-DIGITS |
| [五元的显式间隙界与共同Hecke二次型：类信息已统一，未知量在标记位置](../sources/research/prime_arity_padic/five_explicit_gap_common_hecke_form_20260917.md) | 已建立结论卡 | FIVE-HECKE |
| [固定D问题的实质推进：有效稀疏界、周期返回有限与D=1的精确Pell目标](../sources/research/prime_arity_padic/five_fixed_D_effective_sparsity_and_periodic_return_20260917.md) | 已建立结论卡 | FIVE-SPARSITY |
| [五元的新局部—整体结构：固定理想上的单位指数分形与三进大群闭包](../sources/research/prime_arity_padic/five_fixed_ideal_unit_exponents_and_padic_group_20260917.md) | 已建立结论卡 | FIVE-UNITS-GROUP |
| [五元原整数的三进读位：有限进位的严格边界与二进约分的望远镜公式](../sources/research/prime_arity_padic/five_integer_digits_and_carry_20260917.md) | 已建立结论卡 | FIVE-DIGITS |
| [五元的共同算术几何：Q(√5)范数一环面与扭曲平移](../sources/research/prime_arity_padic/five_norm_one_torus_and_twisted_translation_20260917.md) | 已建立结论卡 | FIVE-TORUS |
| [五元完整可解性的算术几何：三进自相似集的有理点定理](../sources/research/prime_arity_padic/five_padic_fractal_rational_points_20260916.md) | 已建立结论卡 | FIVE-FRACTAL |
| [五元的一个显式范数判据：判别式−11与5·3幂子族](../sources/research/prime_arity_padic/five_quadratic_norm_explicit_slice_20260916.md) | 已建立结论卡 | FIVE-NORM-SLICE |
| [五元二次范数推广：根标签耦合、统一椭圆宏剥离与−59／−971判据](../sources/research/prime_arity_padic/five_quadratic_norm_towers_and_minus59_20260917.md) | 已建立结论卡 | FIVE-NORM-SLICE |
| [五元、六元能否有直观判据：欧几里得式判定与固定同余的严格限制](../sources/research/prime_arity_padic/five_six_intuitive_criteria_and_modular_limits_20260916.md) | 已建立结论卡 | SUBCRITICAL-LIMITS |
| [环面结构怎样约束五元可解性：精确分母、相邻互素与同理想局部反例](../sources/research/prime_arity_padic/five_torus_denominators_and_local_separation_20260917.md) | 已建立结论卡 | FIVE-DENOMINATORS |
| [五元环面研究的外部定理记录](../sources/research/prime_arity_padic/five_torus_literature_20260917/README.md) | 目录入口（状态见结论卡） | — |
| [有界切换之后的文献调查：Lucas赋值、混合逼近与Hecke周期](../sources/research/prime_arity_padic/five_torus_literature_20260917/switch_hecke_review_20260917.md) | 来源／调查 | — |
| [五元问题的定向外部调查与适用性审查](../sources/research/prime_arity_padic/five_torus_literature_20260917/targeted_review_20260917.md) | 来源／调查 | — |
| [全词逃逸方向：外部定理的实际贡献与适用边界](../sources/research/prime_arity_padic/five_torus_literature_20260917/uniform_escape_review_20260917.md) | 来源／调查 | — |
| [n≥4p的证明怎样继续简化：见证预算与双重值恢复](../sources/research/prime_arity_padic/four_p_tail_optimization.md) | 已建立结论卡 | PRIME-TAIL-BACKUP |
| [G的深层含义：有限障碍群、正运输与2p+1后的目标可达性](../sources/research/prime_arity_padic/G_as_obstruction_group_and_stable_threshold_20260916.md) | 已建立结论卡 | G-OBSTRUCTION |
| [从参数表到二维格几何：有界纤维的根、内容对偶与整体闭合方向](../sources/research/prime_arity_padic/global_structure_and_bounded_fiber_geometry_20260916.md) | 已建立结论卡 | PRIME-GEOMETRY |
| [整体结构调查的文献访问记录](../sources/research/prime_arity_padic/global_structure_investigation_20260916/source_index.md) | 来源／调查 | — |
| [本次整数移动文献核对](../sources/research/prime_arity_padic/literature_integer_moves/README.md) | 目录入口（状态见结论卡） | — |
| [从已经成功的局部证明提取整体主线：全系统尺度配平](../sources/research/prime_arity_padic/local_proofs_to_global_balance.md) | 已建立结论卡 | PRIME-BALANCE |
| [移动见证再合并：全部元数、全部超临界维数的同一入口](../sources/research/prime_arity_padic/move_witnesses_then_merge.md) | 已建立结论卡 | PRIME-MOVE-MERGE |
| [一对边界反射统一整个奇数下半区：端点不再另作启动](../sources/research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md) | 已建立结论卡 | PRIME-ODD-PENCIL |
| [保持来源、交换输出：从可逆返回直接得到真实剪切](../sources/research/prime_arity_padic/output_exchange_produces_roots.md) | 已建立结论卡 | PRIME-OUTPUT-ROOT |
| [独立研究入口](../sources/research/prime_arity_padic/README.md) | 目录入口（状态见结论卡） | — |
| [立方根缺口的来源与消除：重新接入旧载体和端点机制](../sources/research/prime_arity_padic/retained_carrier_bridge_and_endpoint_lessons.md) | 已建立结论卡 | PRIME-RETAINED-BRIDGE |
| [三平均七元：G、分歧范数单位与可执行尖点轨道的同一个判据](../sources/research/prime_arity_padic/seven_averaging_cusps_norm_and_eisenstein_20260917.md) | 已建立结论卡 | SEVEN-GEOMETRY |
| [七元算术几何：实际阅读、外部接口与自足证明](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/README.md) | 目录入口（状态见结论卡） | — |
| [三平均六元的显式G=3判据：三重块全解、四重块只查一项赋值](../sources/research/prime_arity_padic/six_triple_block_explicit_G3_20260916.md) | 已建立结论卡 | SIX-EXPLICIT |
| [小参数怎样自然闭合：格指数、退化纤维和真正尚缺的定理](../sources/research/prime_arity_padic/small_parameters_lattice_defects_and_closure_target.md) | 已建立结论卡 | PRIME-NATURAL-UNIFICATION |
| [两块的分裂环面：取消全部独立方向证书与二进迹条件](../sources/research/prime_arity_padic/split_torus_completes_all_directions.md) | 已建立结论卡 | PRIME-SPLIT-COLUMNS |
| [用平方零厚化把p进逐位修正压成一次标量同余](../sources/research/prime_arity_padic/square_zero_hensel_compiler.md) | 已建立结论卡 | PRIME-SQUARE-ZERO |
| [整体证明的结构复盘：用一个二进列提升定理替代两张轨道表](../sources/research/prime_arity_padic/structural_reassessment_and_uniform_dyadic_orbits.md) | 已建立结论卡 | PRIME-DYADIC |
| [p+1至2p：补集动力学、整数下降与p+2的完整递归](../sources/research/prime_arity_padic/subcritical_complement_dynamics_20260916.md) | 已建立结论卡 | SUBCRITICAL-COMPLETE |
| [奇素数p平均的p至2p位置：统一判定、完整p+2几何与全区间反例](../sources/research/prime_arity_padic/subcritical_prime_uniform_arithmetic_20260917.md) | 已建立结论卡 | SUBCRITICAL-COMPLETE, SUBCRITICAL-LIMITS |
| [让终端吸收尺度：九偏移无需额外二进单位补充](../sources/research/prime_arity_padic/terminal_fan_replaces_dyadic_units.md) | 已建立结论卡 | PRIME-TERMINAL-FAN |
| [三平均全部n≥7的统一几何：根格障碍、正向投影与零目标饱和](../sources/research/prime_arity_padic/triple_all_n_root_lattice_and_target_saturation_20260917.md) | 已建立结论卡 | GEOMETRY-ALL-N |
| [只提升当前列：两个根、终端族与可自动生成的方向](../sources/research/prime_arity_padic/two_root_column_completion.md) | 已建立结论卡 | PRIME-TWO-ROOTS |
| [分散证明怎样统一：本轮框架审计与实际取得的分支合并](../sources/research/prime_arity_padic/unified_stable_range_saturation_candidate_20260916.md) | 已建立结论卡 | PRIME-NATURAL-UNIFICATION |
| [全部偶数载体的一致取逆：四步更新、两步混合、一次平方](../sources/research/prime_arity_padic/uniform_even_carrier_inverse.md) | 已建立结论卡 | PRIME-EVEN-INVERSE |
| [所说的“统一公式”具体是什么](../sources/research/prime_arity_padic/uniform_reflection_formula.md) | 已建立结论卡 | PRIME-CERTIFICATE-ANATOMY |

<!-- END SOURCE doc-222bf2d06b26 -->

---

<a id="doc-aab16f33b700"></a>

## 原文导签：大型数学证明项目的现成经验与适合本项目的 harness

来源：`knowledge/MATH_PROJECT_HARNESSES.md` · [逐字节原样副本](../sources/knowledge/MATH_PROJECT_HARNESSES.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-aab16f33b700 -->
# 大型数学证明项目的现成经验与适合本项目的 harness

调查日期2026-09-17。实际读取官方项目文档和下面列出的部分实现；没有安装、运行或独立安全审计这些项目。本页是工具选择调查，不是新的平均问题数学结论。

**用户补充后的重要修正：** [Danus](https://github.com/frenzymath/Danus)直接针对非形式化数学的长期多代理研究、事实图记忆与审核准入，比下述多数单项工具更贴近当前协调需求。初轮漏检，不能将此前工具清单当作完整调查。已对其固定提交做针对性源码阅读和两个离线函数检查，详见第8节；未部署代理群或验证其论文案例。

## 1. 最贴近当前阶段：ANTEDB

[Analytic Number Theory Exponent Database](https://github.com/teorth/expdb) 系统记录解析数论中的定理、猜想和可推导关系，同时提供人类可读的Blueprint与可执行Python。它的 `Hypothesis` 对象包含数学数据、证明／引用与依赖；可以递归列出推导来源。贡献指南明确说明：只有一小部分已经Lean形式化，没有Lean代码的部分也可使用Blueprint结构。

这与本项目的“自然语言证明＋精确Python＋外部定理＋未解决接口”相当接近。实际读了README、CONTRIBUTING及 `blueprint/src/python/hypotheses.py` 前155行，确认上述用途，不把Python对象称为形式化证明内核。

适合借鉴：统一符号和前提；将一个可复用结论表示为对象而非一篇孤立文章；已发表输入、猜想和派生结果分开；查询返回依赖链；把尚未接入主证明的内容明确标记为未整合。

目前结论卡可逐步向这种“有类型的命题＋有前提的推导规则”发展，但不要让登记程序自行推断两个自然语言命题等价。比如“已有深核”必须是规则的输入，不能在导航中被省略。

## 2. 大证明蓝图：Lean Blueprint / plasTeX dependency graphs

[Lean Blueprint](https://github.com/PatrickMassot/leanblueprint) 把LaTeX里的定理、定义、证明及 `\uses` 依赖变成可导航的图，并用 `\lean` 链接Lean声明。`\leanok` 是作者标记；`checkdecls` 检查引用的Lean声明是否存在，不能把该检查等同于全部声明不含sorry或依赖已审。

其底层 [plastexdepgraph](https://github.com/PatrickMassot/plastexdepgraph) 本身不要求Lean，能用于普通LaTeX证明的依赖图。Lean Blueprint的默认创建流程则预期已有Lake工程，偏向GitHub及Pages。这意味着不需要为“先看清证明全貌”立刻全项目形式化或发布。

[Tao的PFR Blueprint实践说明](https://terrytao.wordpress.com/2023/11/18/formalizing-the-proof-of-pfr-in-lean4-using-blueprint-a-short-tour/)展示了按节点追踪定义、陈述、证明及前置依赖的做法。[FLT项目](https://github.com/ImperialCollegeLondon/FLT)也把Blueprint作为数学路线入口；README明确称其为进行中的多人形式化项目，不应说已完成全部FLT形式化。

适合借鉴：未来把主证明整理成一份带稳定标签的连续LaTeX正文；区分“陈述已准确”“纸面证明已有”“已独立审查”“已形式化”四个字段。当前 `depends_on` 仍是导航前提，不可直接改名为机器认证的逻辑依赖图。

## 3. 长期数学知识库：Stacks Project

[Stacks的tag制度](https://stacks.math.columbia.edu/tags)为定理、定义和其他数学对象提供永久标识，条目移动或编号变化不改变tag。[About](https://stacks.math.columbia.edu/about)强调在线超链接、可追溯依赖和维护者接纳修改的机制。

适合借鉴：结论ID保持稳定；“相关”“依赖”“加强”“反例”“修正”是不同关系；移动文件不改变结论身份。Stacks主要是数学编辑与引用体系，不是自动证明工具，不能指望tags自行判定重复或正确性。

## 4. 搜索与验证分开：Equational Theories Project

[Equational Theories](https://github.com/teorth/equational_theories)同时整理蕴含、反蕴含、计算搜索和仪表盘。该项目的README明确把Lean已验证断言与尚未Lean验证的人类／机器断言分开，提供从Lean提取已证蕴含的脚本，再生成进度与查询图。

适合借鉴：搜索器给候选，独立核验器检查证书，已验证数据再驱动仪表盘；不从搜索日志直接生成“定理已证”状态。这个模式适合本项目的有限反射表和实际原位置词证书。

限制：它的主要任务是规格清晰的等式蕴含，不是接入任意Markdown长证明的通用解决器。我们的“已给书面证明”不应照搬其“Lean verified”的术语。

## 5. 真正的AI证明执行 harness：Pantograph / LeanDojo-v2

[Pantograph](https://github.com/lenianiva/Pantograph)是Lean 4的机器对机器接口。官方README展示启动目标、运行tactic、查询符号环境、返回JSON状态；可据Lean反馈控制AI证明搜索。

[LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2)提供Lean库追踪、定理与依赖数据、检索、训练及Pantograph上的证明执行。原[LeanDojo仓库](https://github.com/lean-dojo/LeanDojo)当前README明确提示旧库已弃用、新项目用v2；不建议按旧说明直接搭环境。

适合未来的一个小型试点：形式化平均原子、均值守恒、平方能量下降、G必要性，或七元精确宏恒等式。这样AI产出的Lean片段可以被内核检查。逐步扩展时还要检查声明类型是否忠实于原命题、是否含sorry／额外公理。

不适合立即用来替换全部现有研究：需把问题、数据结构与所引定理转换成Lean；Morris／Serre、ESS等接口的形式化可能很重。LeanDojo-v2的训练栈还包含GPU与大型依赖，本轮没有安装，也没有必要只为文档检索引入。

## 6. 对本项目的选择

**当前采用ANTEDB的命题对象与来源思路、Blueprint的依赖和进度分层、Stacks的稳定ID。保留现有轻量登记，修补实际兼容与检索。** 不再另建一套知识管理框架。

本轮已经落实的具体修补：

- 冻结数学材料与明确允许演进的导航分开，保留原散列和原版备份；新检查实际调用旧冻结兼容审查。
- 素数主题顶部按参数范围列启动、收尾与残留证据；视图只引用结论卡内的事实。
- `overview`只保留结论ID，生成器不再硬写某个证书计数；增加真实中文问题路由及回归测试。
- “全参数原位置资源供应”作为主目标；纤维比较、改变来源与状态相关准备并列，退化出口只是候选策略。

再往前最有价值的两步，不需要马上执行全面迁移：第一，将主定理所必需的结论卡细化成准确陈述和证明依赖，逐条人工审核；第二，选一个小接口做Lean试点。只有前提稳定后，证明执行harness才会给出可靠反馈，而不是把翻译错误固化下来。

此次调查没有找到一个经实际验证、可直接替代自然语言大项目全部协调与数学审核的现成万能harness。以上分别解决组织、依赖、证书和形式证明执行的不同层，不能相互冒充。

用户补充Danus后，这个推荐应细化：ANTEDB／Blueprint仍值得借鉴知识结构；Danus则成为实际研究编排的优先试点候选。没有任何一个LLM审核框架因此变成数学正确性的形式保证。

## 7. 来源与实际读取范围

原始网页／README、URL和SHA256保存在[本地来源目录索引](../sources/work/documentation_memory_20260917/harness_sources/source_index.json)。取得的是访问时版本；散列用于精确保存阅读对象，不声称对应某个已锁定Git提交。

| 来源 | 实际读取 |
|---|---|
| leanblueprint | README的启动、编辑宏、checkdecls和项目实例 |
| plastexdepgraph | README选项与最小LaTeX示例 |
| PFR实践文章 | 正文中依赖图、状态颜色及节点展开说明 |
| FLT | README的项目状态、Blueprint入口；未审数学源码 |
| expdb | README、CONTRIBUTING、Hypothesis类的字段和依赖遍历实现 |
| Stacks | About与Tags explained；未审其网站实现 |
| Equational Theories | README的状态语义、数据提取与仪表盘脚本职责 |
| Pantograph | README的JSON REPL、goal/tactic及环境要求；未执行 |
| LeanDojo / v2 | README的弃用提示、架构与环境要求；未安装、训练或跑证明 |

## 8. Danus：最贴近调度痛点，但需要适配我们的证据体系

来源：[frenzymath/Danus](https://github.com/frenzymath/Danus)，本次读取默认`codex`分支固定提交
`6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c`。作者同时保留使用Claude Code主编排的`main`分支；本文只评估所读取的版本，不混用分支。Apache-2.0，pyproject标记0.1.0／Alpha、POSIX Linux。

### 8.1 它直接针对哪些问题

- 本地工作记忆、全局发现／失败路线记忆、经过审核的事实图分层；研究计划不自动成为证明前提。
- 工作代理一次提交一个准确命题与证明；独立新启动的审核代理返回接受／修补意见。
- MCP入口区分编排者、工作者和审核者的可见工具；`fact_submit`返回`correct`后才写入事实图。
- 事实的内容ID绑定陈述、证明、术语及前置ID；撤销事实时递归撤销登记的后继，避免已知错误继续被当作基础。
- 由事实图抽取最终定理的依赖闭包，产生报告／论文，再有整篇文字审核。

这比我们当前的导航登记多出了实际研究循环、审核准入和撤销传播。若目标是减少用户亲自分配注意力、提醒历史成果，Danus明显比单独增加索引更直接。

### 8.2 源码核对出的五个适配点

**1. “verified”是LLM接受，不是形式证明。** 官方`docs/security-and-trust.md`明确说明审核者不是Lean/Coq。`gateway/server.py`以返回的`verdict == "correct"`作为准入，不在代码中重新推导报告中无critical_errors／gaps。新启动能减少对探索过程的依赖，但不保证作者与审核者没有相同数学盲点。本项目仍应保留“文稿证明、独立AI复核、有限证书、形式核验”等不同证据等级，不能把全部输入都升级为同一种数学事实。

**2. 默认审核者不运行计算证书。** `agents/contracts/verifier.md`的Resource safety明确禁止运行Python、符号代数、求解器或证明助手，要求不能重建成完整书面论证的计算依赖记为缺口。这是外部软件角色约定，不是本会话的新指令。对本项目需另接现有独立核验器：提供脚本／输入证书／结果散列和核验范围，再由审核者检查一般归约。不能让LLM文本裁决替代原185项核验和后续补充登记。

**3. 当前纯中文检索会漏失。** `danus/core/bm25.py`的分词正则是`[A-Za-z0-9_]+`；`FactGraph.search`与记忆检索使用它。本地加载该纯函数检查：`偶数部分统一了吗`与`上半带 九偏移`分词都是空列表、BM25分数全0。我们已有中文词表、公式归一化和真实问题回归用例，迁移时必须接入或补齐。该结论仅针对固定提交，未推测所有分支或未来版本。

**4. 内容去重不是数学语义去重。** `compute_fact_id`归一化空白，但包含statement、proof等内容。离线检查同文空白改变ID不变、同义英文陈述改写ID不同。适合同时保留两层身份：本项目稳定的结论ID用于“这是同一研究问题／数学主张”；Danus内容ID用于“这是哪一版陈述和证明”。不能单靠哈希消除换名后的重复研究。其原始`predecessors`也需要从我们的导航关系人工细化成真正证明前提，不能直接把`related`或阶段替代边当逻辑依赖。

**5. 运行边界与旧材料导入需设计。** 项目默认工作／审核代理经shell启动，官方说明绕过沙箱；MCP角色表不等于操作系统隔离。当前运行脚本以Linux/Bash与symlink为主，Windows本机应先在隔离的WSL／副本里试点。外部引用`external_refs`不计入内容哈希，而我们的证明依赖精确外部定理版本与计算文件，因此应额外绑定这些来源／证书的版本。不要把63张导航卡批量灌成其“已验证事实”，也不要把冻结目录交给自动代理自由改写。

### 8.3 建议的最小试点（尚未启动）

先以已有且可复现的一条七元链作导入／审核测试：G必要性、实际返回周期、整数Γ₀(7)轨道及原位置终端。将对应证据与少量旧错误接口一起提供，检查它能否：找回现有结果、拒绝“局部窗口逆就是全局逆”、拒绝“有限模像就是全群”、区分G1存在性和最短词。

验收重点是**是否减少重复和错误准入**，不是产生多少facts。通过后再将范围有限的开放资源命题交给研究循环，并设置明确预算和停止条件。新数据先留在独立试点目录；合并回本项目继续走明确版本和人工／独立复核流程。

这一方案不要求先把项目全部Lean化，也不要求废弃现有登记。若将来需要形式核验，可选局部命题再接Pantograph等；搜索到的`Danus_with_lean_verification`等分叉本轮未审，不因名字就认为原版已有形式验证。

### 8.4 阅读、检查与未验证范围

读取README、ARCHITECTURE、security-and-trust、DATA_MODEL相关字段，及schema、factgraph的写入／搜索／撤销、BM25、gateway准入和角色表、verify服务与launcher、审核合同、pyproject。下载其他合同仅作定位，未声称逐条审计其全部提示词。

仅执行两个无网络、无模型调用的离线函数检查：中文分词／BM25、内容ID。没有安装Danus、没有运行服务或代理群、没有核验README中的研究案例或其“已解决YTD”宣称，不把作者案例报告当作本轮认证。

固定提交与来源清单见[仓库记录](../sources/work/documentation_memory_20260917/harness_sources/danus/repository.json)、[源码来源散列](../sources/work/documentation_memory_20260917/harness_sources/danus/code_sources.json)；[检查脚本](../sources/work/documentation_memory_20260917/inspect_danus.py)与[实际结果](../sources/work/documentation_memory_20260917/harness_sources/danus/focused_checks.json)可复现上述两个具体限制。

<!-- END SOURCE doc-aab16f33b700 -->

---

<a id="doc-232fe86005a9"></a>

## 原文导签：项目记忆与证明导航整理报告

来源：`knowledge/ORGANIZATION_AUDIT_20260917.md` · [逐字节原样副本](../sources/knowledge/ORGANIZATION_AUDIT_20260917.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-232fe86005a9 -->
# 项目记忆与证明导航整理报告

2026-09-17。用户指出分散文稿让研究者重复已有工作、难以掌握证明全貌。本轮进行文档与证据关联整理，没有开展新的平均定理研究，也未重新认证全部数学证明。

## 1. 实际问题

| 发现 | 对研究的影响 | 本次处理 |
|---|---|---|
| 根入口停在2026-09-15的三共轭根阶段 | 后续AI把已绕开的方向／尺度任务继续当缺口 | 根入口改指统一状态；原基线明确注明版本 |
| 独立研究目录有45篇技术／总结稿及1篇累计README，均不在原核验注册中 | 最新成果和原证明断开，核验者容易漏读整条支线 | 全部45篇接入结论卡和程序映射 |
| work/README与独立README不断追加“最新” | 同页多套历史状态互相覆盖，阅读成本随每轮增加 | 精简为稳定导航，原件完整保存 |
| 同一目标有多套不同强度的表述 | 可达性已解仍重搜种子；五元算法已解仍被说成判定开放 | 按量词分卡，写范围与不证明内容 |
| 162／114证书数、21504／43008容器等更新分散 | 历史容器和改进版本易混同 | 记录具体替代关系与反驳范围，不能整篇笼统作废 |
| 有脚本但没有统一的新结论到脚本入口 | 核验只能凭名称猜，PASS容易被高估 | 同一命令查询原185项与本地研究检查 |

初始盘点：outputs有252篇Markdown；research有53篇Markdown；work保留407份有效Python脚本及大量旧证据／备份。数量本身不是错误，缺失的是跨文件的当前结论关系。

## 2. 新的维护结构

- `knowledge/catalog.json`：59张人工整理的稳定ID结论卡；范围、状态、边界、前提／相关结果、后续替代、旧核验ID和本地检查是同一维护源。
- `knowledge/STATUS.md`、`topics/`、`DOCUMENTS.md`：由登记表生成，不能手工各自维护另一套数学状态。
- `PROOF_ROUTES.md`：三平均、素数、五元、合数与算法的证明骨架，明确已完成的定理与仍开放的接口。
- `ROUTE_GUARDS.md`：把历史绕圈点及重新推进所需增量集中列出。
- `AGENTS.md`：让后来AI在研究前必须检索和回读，研究后更新已有结论卡及证据。
- `project_knowledge.py`：检索、阅读包、结论展示、核验命令查询、生成和一致性检查。只用Python标准库，不自动执行数学程序。

“原证明已完成”与“本地文稿已有证明、未独立重审”分开显示。来源被登记不意味着被本次独立认证。多个结论可以引用同一稿件，一篇稿件也可以同时含已证部分和开放问题；卡的精确范围比整篇文件名优先。

## 3. 原材料保留情况

没有移动、删除或改写原数学证明、计算脚本、证书及原185项核验清单。调整了七个导航入口：根README、outputs根及三个主题入口、work入口、独立研究入口。原件与散列保存在[快照记录](../sources/work/documentation_memory_20260917/snapshots.json)。

原完成证明及其162组核验继续按原执行器运行；独立研究不会被悄悄塞入原profile。新的补充登记提供跨版本导航，但没有将“114组剩余根资源”伪装成已重新审核的完整主证明。

## 4. 验证方式与边界

运行 `python knowledge/project_knowledge.py check`，检查：

- 结论ID、文件／脚本／记录存在，导航前提无循环，关联与旧核验ID可解析；
- 独立研究顶层45篇技术／总结稿全部有卡；
- 登记来源、程序、结果与文献记录的散列变化会提示重新核对；
- 生成页保持一致，新知识库内部链接有效；
- 默认正文搜索不包含文档整理备份、旧快照和缓存。

另外以真实交接问题测试检索：“五元小分母”“两根列修正”“七元尖点”“GRH”“21504”。测试要求能找到当前卡及必要的后续／纠正，而非仅返回旧关键词。

具体自动结果见[导航核验记录](../sources/work/documentation_memory_20260917/navigation_validation.json)。这些检查只验证导航与维护机制，不审查定理真假，也不声称原工作区所有历史链接均已修复。

## 5. 后续如何避免再次失效

新研究开始前应产出一个小阅读包：现有最近结论、准确前提、已知反例、当前缺口。结尾至少更新一张已有卡；仅当有独立的新技术内容才新增稿件。变更登记的来源时，检查器会要求核对对应卡，而不是让过时摘要静默继续流传。

仍有边界：文档清单覆盖全部outputs/research Markdown，但59张卡不是对约300篇文稿逐命题的正式知识图谱。原185项核验与历史路线账本继续补足定位；未细分的旧稿明确标记“仅旧核验／文件发现”，不能自动判为无效或已审。后续应在使用某篇旧稿时逐步补精确卡，不再重造一份总体总结。

机制已经建立并实际接入入口，维护责任由后续研究者承担；无需用户继续充当外置记忆来逐项提醒。

## 6. 后续兼容复核与修补（同日）

另一位AI准确发现：初次整理虽通过新导航检查，却破坏旧 `check_frozen_files()` 对六份README的字节冻结。因此前文“已检查”只覆盖当时的新导航机制，不能解读为原数学核验全部可正常执行。这是维护兼容遗漏。

修补保留原256项快照与全部历史散列，在 `navigation_migrations.json` 逐项记录六份导航的原备份、原散列和接纳的当前散列；其余250项继续严格冻结。统一检查现在也调用这个审查。隔离临时目录的负例测试确认：证明改动、证明删除、备份篡改、未登记导航版本、重写原快照和伪装证明为导航，都会失败。

实际重新运行并通过四项受到影响的核验：平方零编译器（32项一般编译、486项旧资源编译、540项公式）；共同控制器（结果见原JSON）；有限对应收尾（3762次列输送）；奇数反射（138373组计数／容量、4433组矩阵恒等式、1332次实际平均）。这些复跑验证修补后的接口，没有重新证明外部群论定理。对应四张卡已逐项复核后刷新程序／结果版本。

后续新增四张已有边界证明卡：2p+2、内部偶余量、3p−1和3p；当前为63张卡。素数主题顶部生成12行覆盖视图，区分全部小素数基线、p≥83共同接口和不同选参来源。覆盖事实存在所属结论卡，视图只存引用。`overview`也改为只引用结论ID，生成器不再硬写证书计数。

中文检索新增受控词表、符号归一化和真实问题路由，阅读包展开所选结果及两层后续／前提，不再只看前三项的直接关联。维护测试含15个查询断言（包括用户给出的三个失败例）、单源变更传播、后续的后续可见性，以及上述冻结负例。

主目标改为“全参数原位置资源供应”；纤维比较、改变来源和状态相关准备并列，退化出口不是预设的唯一必经路线。本次未搬动数学文件、未另建知识框架。

工具调查实际读取官方资料，见[数学项目harness](../sources/knowledge/MATH_PROJECT_HARNESSES.md)。推荐借鉴ANTEDB的命题／依赖数据、Blueprint的证明蓝图与Stacks稳定ID；Pantograph和LeanDojo-v2用于未来小范围Lean试点，未在本轮安装。

<!-- END SOURCE doc-232fe86005a9 -->

---

<a id="doc-7eb52d82bcd2"></a>

## 原文导签：证明链与真正开放的接口

来源：`knowledge/PROOF_ROUTES.md` · [逐字节原样副本](../sources/knowledge/PROOF_ROUTES.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-7eb52d82bcd2 -->
# 证明链与真正开放的接口

本页给阅读骨架，精确范围和证据查 [STATUS.md](../sources/knowledge/STATUS.md) 及对应结论卡。这里不是所有正文的自包含替代，也不是自动生成的形式化依赖证明。

## 三平均

已经证明所有 n≥7：G为3幂当且仅当有限三平均可达。最短的主阅读链是：

1. **必要性与公共算术对象：** `G-OBSTRUCTION`。根格配对／仿射R格的障碍模；G非3部分不能沿操作消掉。
2. **全部 n≥11 的充分性：** `TRIPLE-ALL`。研究3X，至多两步建立两个不同三重值；同时保护危险素数见证；选取真实整数平均；离散能量严格下降；进入显式终端。
3. **有限边界：** `TRIPLE-BASES`、`SEVEN-STRUCTURE`。七元正向逆与尖点控制，八元Euclid，九元固定三幂网络，十元精确宏覆盖。
4. **几何理解：** `GEOMETRY-ALL-N`、`SEVEN-GEOMETRY`。前者统一根格和局部退化，后者给真实可执行的模曲线例子；两者均不能替代第2、3步的操作存在性。

已绕开的旧必经关卡：逐个素数位置数搜种子、一般合数归约、所有输入压到同一个二维核、指定迹零矩阵的原位置分解。它们的独立工具仍可用，不能再说三平均全维数证明尚依赖这些未完成目标。

真正开放：可变n的统一多项式构造长度；更简洁的统一原位置资源定理；阈值以下的静态分类。一般最短问题与此分开。

## 素数平均

完整基线由 [原总证明](../sources/outputs/prime_arity/proof.md) 及 [原依赖图](../sources/outputs/prime_arity/proof_map.json) 给出。原注册中的 162 组是该版本的证书。

```mermaid
flowchart LR
  A[合法输入与安全入口] --> B[带重数账本的核心]
  B --> C[实际标量周期与根资源]
  C --> D[深同余工具]
  D --> E[有限列与尺度输送]
  E --> F[零和终端及收尾]
```

独立改进不是再证明各处可达，而是替换这条链的部分环节。按接口读，避免把旧计数当最新状态：

| 接口 | 先读 | 已替代什么 | 仍需要什么 |
|---|---|---|---|
| 全输入入口／共同形状 | PRIME-MOVE-MERGE、PRIME-COMMON-SHAPE | 统一双块入口和跨3p形状 | 核内资源供应 |
| 初始正向逆 | PRIME-EVEN-INVERSE、PRIME-ODD-PENCIL | 全偶载体周期；全部奇数下半带含端点的共同反射 | 一般偶数／上半带完整资源 |
| 容量内的根 | PRIME-FIBER、PRIME-GEOMETRY | 同行列式作用格、二维整数凸包的本原根 | 退化／小库存的一般存在性 |
| 九偏移资源记录 | PRIME-CONSERVATION13、PRIME-FIVE-RETURNS | 辅助13；48组根记录由通式替代 | 此路线保留114组根资源，不能自动改写基线审计 |
| 已有资源后的终端 | PRIME-SPLIT-COLUMNS、PRIME-FINITE-TERMINAL | direction、binary_unit、反复扩环等更强要求 | 初始根与深核必须先成立 |

推进自然统一之前必读 `PRIME-NATURAL-UNIFICATION`。**“已有深核后可做”不能倒过来成为深核启动的证明。** 只需存在成功选择；不要求任意合法选择都终止。

## 五元

完整逐输入问题与算术研究要分别追踪。

```mermaid
flowchart LR
  A[SUBCRITICAL-COMPLETE: 强制递归与最短词] --> B[FIVE-NORMAL-FORM: 完整正词描述]
  B --> C[FIVE-FRACTAL: 三进紧集有理点]
  C --> D[FIVE-TORUS: 扭曲环面]
  D --> E[FIVE-UNITS-GROUP: 固定理想单位指数]
  E --> F[FIVE-ESCAPE-OPEN: 固定D全词逃逸]
  E --> G[FIVE-SPARSITY: 稀疏与周期]
  G --> H[FIVE-TEMPLATE-ESCAPE: 固定模板逃逸]
  H -. 任意变模板仍缺 .-> F
```

这个图是研究关联，不声称每一条边都是不可替换的证明前提。更细的脚本与原文从结论卡定位。

- 已解决：任意有理五元能否可达、失败能否判停、最少步数。
- 已证明的结构：部分静态范数族、完整正词／连分数／三进描述、环面及理想坐标、多块固定模板逃逸。
- 尚未解决：D=1只三个单位指数；固定D任意词只有有限成功点；像G一样的一次性完整算术判据。

固定模板可以有无界切换，但“模板固定”的量词不能删。零密度、Baker–Brumer超越性、Aka–Shapira整周期等分布都不自动填这个缺口。

## 合数与算法

合数先读 `COMPOSITE-FRONTIER`，再读 `COMPOSITE-DEFINITIONS`。GRH、单个临界维数、自动G、首个非自动G维数及最终阈值必须逐项保留。不要从全部2k+1端点已解推断全部n≥2k+1已解。

算法先读 `ALG-LENGTH`。存在性、路径长度上界、生成一条路径、该路径最短、有限计时比较，是五种不同结论。五元的专门最短算法不与一般最短路径困难性冲突。

## 快速获得阅读包

```text
python knowledge/project_knowledge.py context "固定模板 小分母"
python knowledge/project_knowledge.py context "容量 深核 退化"
python knowledge/project_knowledge.py context "七元 尖点"
python knowledge/project_knowledge.py verify PRIME-ODD-PENCIL
```

开始研究时在记录中注明选中哪条链、哪个接口、要增加哪一个量词。单纯新增矩阵记号、提高有限搜索范围、重写为几何术语，不自动构成该接口的新结果。

<!-- END SOURCE doc-7eb52d82bcd2 -->

---

<a id="doc-758033e3448d"></a>

## 原文导签：开始新路线前，先排除这些重复与偷换

来源：`knowledge/ROUTE_GUARDS.md` · [逐字节原样副本](../sources/knowledge/ROUTE_GUARDS.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-758033e3448d -->
# 开始新路线前，先排除这些重复与偷换

本页集中常见误判，详细成果由结论卡和原文承担。不是禁止研究这些方向，而是明确再做时必须新增什么。

| 拟做／拟声称 | 项目已经知道 | 重新推进需新增 | 结论卡 |
|---|---|---|---|
| 继续逐个素数证明三平均 n≥7 | 全维数已由n≥11双三重直接证明加基例完成 | 简化证明、算法界或更强结构，不能叫填原可达性缺口 | TRIPLE-ALL |
| 证明所有奇素数平均N(p)=2p+1 | 原总证明已经完整 | 减少分段、物理资源的一般存在性或词提取 | PRIME-TOTAL |
| 从三共轭根继续补高阶方向表 | 两根列修正＋分裂乘法＋有限对应已删除多项更强前提 | 初始根资源／退化出口，不重建已绕开的字段 | PRIME-TWO-ROOTS、PRIME-SPLIT-COLUMNS、PRIME-FINITE-TERMINAL |
| 原证书162组已变成114组，所以整篇最新证明完成重审 | 114是独立路线的剩余根资源记录；冻结基线仍162组 | 完整替代依赖图、接口与独立审核 | PRIME-FIVE-RETURNS |
| 无界整数关系格有本原步长，所以容量内有操作 | 有限库存可能只容纳零移动 | 有界纤维的整数点／凸包或安全退出存在性 | PRIME-FIBER、PRIME-GEOMETRY |
| 两个返回不交换，所以一定有根 | 已有反例；可只生成对角／反对角群 | 真实根及其理想、横向资源的明确构造 | PRIME-OUTPUT-ROOT |
| 借深核准备出口，再由出口建立深核 | 存在循环依赖 | 深核之前的独立可执行资源 | PRIME-FINITE-TERMINAL |
| 把一般r送到r=1、2或p | 位置数与r固定，不是免费变维数 | 原位置转换、补集与总和账本 | PRIME-NATURAL-UNIFICATION |
| 等角、伴随或运输矩阵恒等式提供真实返回 | 像不变、原位置分解和复制消去并不自动成立 | 所需子空间上的准确恒等式＋位置实现 | OLD-TRACE-RETURN、STABILIZATION |
| Hecke分支之和、群闭包、大模像给一个成功正词 | 旧Ihara–Hecke路线已审计此缺口 | 指定作用的真实分支提升／正向实现 | OLD-HECKE-AUDIT |
| 九十一元真实宏群是否等于21504容器还待证明 | 这个等式已被尺度字符耦合反驳；43008为新的必要容器 | 若研究群本身，须处理修正后的容器；可达性早已有别的证明 | N91-CONTAINER-CORRECTION |
| 重搜每个参数的仿射根或固定短周期 | 交换子理想可统一计算，固定参数词的周期刚性已有一般定理 | 新的真实逆、恒等周期或随参数变化的可执行模板 | AFFINE-IDEAL、PARAMETRIC-RIGIDITY |
| 七元的Γ₀(7)直接嵌入所有n | 局部窗口围绕自身均值缩放 | 全局均值及相对尺度兼容 | WINDOW-MEAN |
| 范数／类数一即可决定一般可平均性 | 七元特殊；n=11能量22仍G=1可解；六元亦有类数一陷阱 | 根基位置与真实控制接口 | GEOMETRY-ALL-N |
| 五元仍需搜索所有输入判断可解 | 强制递归完整、可停机、可求最短词 | 真正静态算术简化或新的结构定理 | SUBCRITICAL-COMPLETE |
| 分形／零密度／超越性证明无简单判据 | 只排除精确定义的有限同余／编码模型 | 针对拟定表达能力的严格不可表示证明 | SUBCRITICAL-LIMITS、FIVE-DIGITS |
| 固定S单位相邻边有限，因此固定D返回有限 | 可离开S再返回；条件不同 | 全轨道交点控制 | FIVE-TORUS、FIVE-ESCAPE-OPEN |
| 固定模板逃逸已经证明全词逃逸 | 模板本身可随长度改变 | 对增长模板复杂度一致的论证，或反例 | FIVE-TEMPLATE-ESCAPE |
| 2k+1端点已解，所以一般合数最终阈值已解 | 后面的全部区间并未自动覆盖 | 单独的传播／区间接续证明 | COMPOSITE-FRONTIER |
| 随机求解失败是反例／网页快是复杂度证明 | 搜索有预算、实例分布与机器因素 | 不可达不变量／完整算法界或同题受控测试 | ALG-LENGTH、ALG-WEB |

更多历史路线编号E1—E8、H1—H7、I1—I10保留在[旧路线账本](../sources/outputs/history/research_routes_history_20260915.md)。其“未完成”字段常描述旧阶段；先查当前结论卡的后续更新，不把整张历史表当现在的任务列表。

<!-- END SOURCE doc-758033e3448d -->

---

<a id="doc-5182695697d4"></a>

## 原文导签：研究轮次记录模板

来源：`knowledge/SESSION_TEMPLATE.md` · [逐字节原样副本](../sources/knowledge/SESSION_TEMPLATE.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-5182695697d4 -->
# 研究轮次记录模板

日期／任务／对应结论卡 ID：

## 开始前的去重检查

- 检索词与实际读过的来源、章节：
- 已有结论及前提：
- 曾被排除的相近路线及排除范围：
- 本轮希望增加的精确命题（不是换名或重写）：

## 实际结果

- 一般证明／条件定理／有限证书／恒等式检查／探索：
- 新增与旧结论的关系：加强、特例、独立证明、修正或仅解释：
- 外部定理的版本、实际读取范围和代入条件：
- 对应脚本、证书、运行命令与证据边界：

## 交接

- 当前仍未证明的精确命题：
- 下一步必须新增的内容与可复用入口：
- 已更新的结论卡 ID 与替代关系：
- `project_knowledge.py check` 结果：

仅状态改变时更新结论卡，无须复制本模板生成另一份总体总结。需要记录独立的新实验／证明过程时再保存轮次文件。

<!-- END SOURCE doc-5182695697d4 -->

---

<a id="doc-3b227852f0e8"></a>

## 原文导签：接手入口：先定位问题，再阅读证明

来源：`knowledge/START_HERE.md` · [逐字节原样副本](../sources/knowledge/START_HERE.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-3b227852f0e8 -->
# 接手入口：先定位问题，再阅读证明

这里解决“同一项目反复发现旧结果”的问题。原论文式证明和研究经过保留原位置；当前结论、真正缺口、替代关系和核验入口集中登记在 [catalog.json](../sources/knowledge/catalog.json)，专题页和状态页由它生成。

先读 [当前状态](../sources/knowledge/STATUS.md)，再选一个主题：

| 任务 | 入口 |
|---|---|
| 三平均全部 n≥7 的完整证明与几何解释 | [三平均与统一几何](../sources/knowledge/topics/triple.md) |
| 全部素数元数的阈值，以及减少分段／证书的研究 | [素数定理与自然统一](../sources/knowledge/topics/prime.md) |
| 五元、六元及 p<n≤2p | [阈值以下与五元算术](../sources/knowledge/topics/subcritical.md) |
| 合数元数、M/H/N、GRH 条件 | [一般元数](../sources/knowledge/topics/composite.md) |
| 计算复杂度、最短路径、求解器 | [算法与核验](../sources/knowledge/topics/algorithms.md) |
| 外部定理、已排除的偷换、历史路线 | [公共工具与路线边界](../sources/knowledge/topics/interfaces.md) |

理解证明全貌读 [证明链与开放接口](../sources/knowledge/PROOF_ROUTES.md)。开始一个新想法前读 [避免重复研究的路线表](../sources/knowledge/ROUTE_GUARDS.md)。严格核验读 [核验使用说明](../sources/knowledge/VERIFICATION.md)。全部 Markdown 的文件级定位在 [文档清单](../sources/knowledge/DOCUMENTS.md)，它只作发现，不自动判定正文真假。

素数研究先看[参数范围 × 启动 × 收尾 × 残留证据](../sources/knowledge/topics/prime.md#当前参数覆盖启动与收尾分开看)。大型数学项目的现成工具与本项目适配建议见[Blueprint、ANTEDB及证明执行harness调查](../sources/knowledge/MATH_PROJECT_HARNESSES.md)。

## 一个接手动作

在项目根目录执行：

```text
python knowledge/project_knowledge.py context "五元 小分母"
python knowledge/project_knowledge.py context "两根 列修正"
python knowledge/project_knowledge.py context "偶数部分统一了吗"
python knowledge/project_knowledge.py context "上半区三段选参是否合并"
python knowledge/project_knowledge.py search "Hecke"
python knowledge/project_knowledge.py show FIVE-TEMPLATE-ESCAPE
```

`context` 返回相关结论卡、已登记的前提、后续替代、历史核验及正文命中。它是阅读包，不是自动数学判断。进入原文以后仍须核对符号、假设和量词。

## 几条容易混淆的状态

- 三平均 n≥7 和全部奇素数平均 n≥2p+1 的可达性已有完整证明。继续研究自然统一，不意味着原定理尚缺证明。
- 五元逐输入判定及最短操作已解决；尚缺的是用户要求的一次性算术分类。固定 D 的全词逃逸仍是猜想，多块固定模板已给证明。
- 七元与 Γ₀(7) 的对应有真实正向宏支撑；一般 Hecke 分支之和、群闭包或运输存在不具备这个自动接口。
- 原素数基线证书与独立研究的剩余根资源清单属于不同版本／作用范围；当前计数直接查 PRIME-TOTAL、PRIME-FIVE-RETURNS 及覆盖表。不能仅修改一个计数便宣称整篇新证明已重审。

## 维护责任

结论状态、依赖和脚本的维护属于研究工作本身。新研究者应遵守 [AGENTS.md](../sources/AGENTS.md)，使用 [轮次模板](../sources/knowledge/SESSION_TEMPLATE.md)。用户不再负责逐次提醒“这件事以前已做过”。

本次整理属于导航、交接和证据关联审查，未重新认证全部数学证明。新研究的状态按“文稿已给证明／尚未独立审核”明确记录。

<!-- END SOURCE doc-3b227852f0e8 -->

---

<a id="doc-9ac70881754c"></a>

## 原文导签：当前状态与问题分流

来源：`knowledge/STATUS.md` · [逐字节原样副本](../sources/knowledge/STATUS.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-9ac70881754c -->
# 当前状态与问题分流

> 由 catalog.json 生成。导航整理不等于独立审稿。修改结论卡后执行 build。

当前研究任务以用户会话为准；下表记录数学状态，不把某条支线自动设为当前任务。

| 结论／任务 | 当前范围 | 还缺什么 |
|---|---|---|
| TRIPLE-ALL · 三平均 n≥7 的完整G判据 | 非全等输入中心化、本原化后，可达全等 ⇔ G为3幂。n≥11同一双三重直接证明，接7—10基例。 | 判定已解决；不等于最短路径或可变n统一多项式构造长度已解决。 |
| PRIME-TOTAL · 所有奇素数平均的最优最终阈值 | 所有奇素数p：N(p)=2p+1，阈值以上G为p幂充要；N(2)=4。原主证明覆盖表完整。 | 已完成存在性不等于新统一无证书证明或通用高效群词提取。162组是冻结基线，后续独立简化不自动重写它。 |
| PRIME-NATURAL-UNIFICATION · 自然统一的主目标：全参数原位置资源供应 | 原阈值已证。目标是统一2p<n<4p的初始物理资源供应；纤维比较、改变来源、状态相关准备是并列候选策略。奇数下半带已有共同反射。 | 退化出口不是唯一必经关卡；先有独立真实资源才可使用深核。共同收尾、共同形状与同一选参公式是不同强度。 |
| FIVE-SUMMARY · 五元：算法已解、静态分类仍未解 | 逐输入判定与最短路径完成；椭圆型真实宏的范数剥离已统一，新增−59／−971子族及跨素数根标签耦合。全五元静态判据及固定D全词逃逸仍未解。 | 本总结不是所有新证明的独立审核。有限实验、零密度、分形维数和超越性均不能证明静态简单判据不可能。 |
| FIVE-ESCAPE-OPEN · 固定D全词逃逸与D=1完整分类 | 猜想min_|W|=L D(We)→∞；更小猜想D=1只允许单位指数k=0,±1。 | 模板定理、零密度、群闭包、有限指数范围实验都不能替代任意词证明。没有证明简单判据不可能。 |
| SIX-EXPLICIT · 六元三重核心G=3与唯一后继 | 三重核心G=3且无四重值可解；四重值有模9条件；一般G=1失败出口后剩唯一后继。 | 一般G=1尚未压成一次性公式；不是所有六元G合法都可解。 |
| SEVEN-GEOMETRY · 七元G、分歧范数、尖点与Eisenstein的完整对接 | 指定宏群恰为PGL₂(Z[1/6])模7上三角子群；G=1等价合法尖点及Q(√−7)分歧单位，theta与本原能量层有显式计数。 | 七元可达性是已有结果；theta计数和类数一不能替代真实正向宏。非全局窗口不能直接推广。 |
| COMPOSITE-FRONTIER · 一般元数三项主任务与GRH范围 | 无条件全部k的2k+1端点；奇素数幂奇数中间维数；GRH下平方族与2、3幂临界点。 | 不等于一般N(k)=B(k)。p≥5高奇次幂临界、混合素因子临界及整段接续仍未全闭合。 |
| ALG-LENGTH · 构造长度与最短路径的不同状态 | 三平均直接算法有数值界和固定n位长多项式界；原求解器、精确IDA*和最短路径困难分别登记。 | 可变n统一多项式构造长度未证；最短性NP困难不否定非最优多项式路径可能性。 |

## 证明全貌

[三平均完整链](../sources/knowledge/PROOF_ROUTES.md#三平均) · [素数基线与独立改进](../sources/knowledge/PROOF_ROUTES.md#素数平均) · [五元开放问题](../sources/knowledge/PROOF_ROUTES.md#五元) · [路线边界](../sources/knowledge/ROUTE_GUARDS.md)

## 独立改进的范围（直接引用结论卡）

- PRIME-FIVE-RETURNS：一般容量公式与守恒n根供应两组横向系数；对原九偏移资源表替代48组，列出114组剩余。 **限制：** 114是本独立改进对物理根资源的剩余，不是重写冻结主证明后的完整独立审计计数；s>p/2该模板有障碍。
- PRIME-FINITE-TERMINAL：已有真实深核，行列式与控制模数互素时，有限正向对应轨道等于明确有限群轨道；终端无需反复扩环。 **限制：** 不供应初始根与深核；共享坏因子的行列式不自动覆盖。
- PRIME-ODD-PENCIL：所有奇素数p≥3、全部奇数1≤r<p，用同一两组三步反射及两步反射取得根、深核与终端。包含r=1，无83界。 **限制：** 偶数余量、3p及上半带没有因此统一；Morris/Serre等原依赖仍保留。

本次机器目录覆盖 309 篇 outputs/research Markdown，人工登记 64 张结论卡；原核验清单有 185 项。未登记正文不会被自动当作过时或无效。

<!-- END SOURCE doc-9ac70881754c -->

---

<a id="doc-46173a558d11"></a>

## 原文导签：核验：从结论定位脚本，不从文件名前缀猜结论

来源：`knowledge/VERIFICATION.md` · [逐字节原样副本](../sources/knowledge/VERIFICATION.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-46173a558d11 -->
# 核验：从结论定位脚本，不从文件名前缀猜结论

有两套互补登记：原完成项目的 [185项核验清单](../sources/work/verification_manifest.json)，以及 [catalog.json](../sources/knowledge/catalog.json) 中独立研究的 `local_checks`。两者由同一查询入口联接，原清单和证书内容不因本次整理而改写。

```text
python knowledge/project_knowledge.py verify TRIPLE-ALL
python knowledge/project_knowledge.py verify FIVE-TEMPLATE-ESCAPE
python knowledge/project_knowledge.py verify PRIME-FINITE-TERMINAL
```

查询会列出命令、数据记录、证据等级与不覆盖范围；**不自动运行**。先读范围，再执行所需命令。不需要为了接手一条小支线重跑全项目长搜索。

## 原完成项目

```text
python work/run_verifications.py --list
python work/run_verifications.py --id all-dimensions-double-triple-invariant
python work/run_verifications.py --id seven-endpoint-structure
python work/run_verifications.py --profile prime-proof
```

旧运行器的输出标记只证实相应检查成功。`theorem-certificate` 只承担正文明确归约后的有限子问题；`symbolic-check` 和 `finite-sanity` 不能证明无穷量词。`exploratory-search` 失败不能当不存在证明。

## 后续独立研究

结论卡直接关联文稿、实际核验器和JSON记录。无独立脚本的综述／书面推导明确标记，不伪装成漏登的PASS。一个脚本可能核对多个结论，也可能读旧证书，须检查卡中范围和原文。

例如固定模板逃逸的正式证明依赖ESS及谱引理；脚本只检查公式与有限样本。`--return-depth 18` 的524286个词诊断与一般定理分开，不构成“只搜索到18便证明逃逸”。

## 文档与知识登记检查

```text
python knowledge/project_knowledge.py check
```

检查ID唯一性、文件与脚本存在性、关联ID、导航前提循环、来源散列变化、独立研究是否遗漏、生成页是否过期和新知识库链接。**它不会审查证明是否正确。**

现在还实际调用旧冻结兼容审查。原[256项冻结快照](../sources/research/prime_arity_padic/existing_documents_snapshot.json)及其散列保留；[导航迁移登记](../sources/knowledge/navigation_migrations.json)只允许六份明确README演进，逐项要求旧备份与原散列相符、当前版本与迁移登记相符。其余250项必须原样。不能把证明文件加入例外名单，也不能覆盖原散列消除失败。

旧调用者的 `check_frozen_files()` 仍返回核查条目总数；部分历史输出字段名含 `unchanged`，现在应按上述兼容政策解释为“冻结材料与已登记导航迁移均通过”，不代表六份当前README字节未变。新统一检查会分别报告两类数量。

有意修改来源后，先读相应结论卡并更新范围／边界，再执行：

```text
python knowledge/project_knowledge.py accept-sources FIVE-TEMPLATE-ESCAPE
python knowledge/project_knowledge.py build
python knowledge/project_knowledge.py check
```

`accept-sources` 只是记录维护者已处理的版本，不会认证新数学结果。不要为了消除警告批量确认未阅读的变更。

## 新结果的最低登记要求

固定ID、精确量词、条件（尤其GRH）、证明状态、已知边界、相关前置结果、替代的具体范围、原文路径。涉及程序结论时再加命令、输入／证书文件、结果文件、实际核验承担什么。外部定理加来源版本与实际读过的章节。

有限检查可以复用，不必给纯导航更改重跑数学程序。本次整理的自动核查与检索试验记录在 [整理报告](../sources/knowledge/ORGANIZATION_AUDIT_20260917.md)。

<!-- END SOURCE doc-46173a558d11 -->

---

<a id="doc-d5fb440f3df7"></a>

## 原文导签：算法、复杂度与核验

来源：`knowledge/topics/algorithms.md` · [逐字节原样副本](../sources/knowledge/topics/algorithms.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-d5fb440f3df7 -->
# 算法、复杂度与核验

[总状态](../sources/knowledge/STATUS.md) · [接手入口](../sources/knowledge/START_HERE.md)

存在性、构造、最短性、计时和搜索失败必须分别报告；一条固定输入路径可以精确重放，但不承载无穷量词。


| ID | 结论 | 状态 |
|---|---|---|
| ALG-LENGTH | 构造长度与最短路径的不同状态 | 部分结果／明确范围 |
| ALG-WEB | 网页求解器与效率比较的证据范围 | 部分结果／明确范围 |

### ALG-LENGTH · 构造长度与最短路径的不同状态

**状态：** 部分结果／明确范围。三平均直接算法有数值界和固定n位长多项式界；原求解器、精确IDA*和最短路径困难分别登记。

**边界：** 可变n统一多项式构造长度未证；最短性NP困难不否定非最优多项式路径可能性。

**原文：** [triple_average_sequence_length_analysis.md](../sources/outputs/algorithms/triple_average_sequence_length_analysis.md) · [pair_triple_solver_comparison_and_optimality.md](../sources/outputs/algorithms/pair_triple_solver_comparison_and_optimality.md)

**核验：** `python knowledge/project_knowledge.py verify ALG-LENGTH` 只展示已登记命令及边界，不自动启动计算。

### ALG-WEB · 网页求解器与效率比较的证据范围

**状态：** 部分结果／明确范围。保存Arena源码审阅、同题精确重放、批量计时及二平均HTML比较。

**边界：** 有限随机速度优势不证明最坏复杂度；预算搜索失败不是数学反例。

**原文：** [arena_triple_solver_review.md](../sources/outputs/algorithms/arena_triple_solver_review.md) · [averaging_algorithm_benchmark.md](../sources/outputs/algorithms/averaging_algorithm_benchmark.md)

**核验：** `python knowledge/project_knowledge.py verify ALG-WEB` 只展示已登记命令及边界，不自动启动计算。

<!-- END SOURCE doc-d5fb440f3df7 -->

---

<a id="doc-f9fd4177f2c5"></a>

## 原文导签：一般元数与GRH

来源：`knowledge/topics/composite.md` · [逐字节原样副本](../sources/knowledge/topics/composite.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-f9fd4177f2c5 -->
# 一般元数与GRH

[总状态](../sources/knowledge/STATUS.md) · [接手入口](../sources/knowledge/START_HERE.md)

保留GRH条件，分清单个维数、首个非自动G点和最终阈值。此前会话的暂停安排不自动约束新用户任务。


| ID | 结论 | 状态 |
|---|---|---|
| COMPOSITE-FRONTIER | 一般元数三项主任务与GRH范围 | 部分结果／明确范围 |
| COMPOSITE-DEFINITIONS | M、H、N与自动G维数不能混用 | 解释／综述，非新可达性证明 |

### COMPOSITE-FRONTIER · 一般元数三项主任务与GRH范围

**状态：** 部分结果／明确范围。无条件全部k的2k+1端点；奇素数幂奇数中间维数；GRH下平方族与2、3幂临界点。

**边界：** 不等于一般N(k)=B(k)。p≥5高奇次幂临界、混合素因子临界及整段接续仍未全闭合。

**原文：** [general_k_three_tasks_progress_20260915.md](../sources/outputs/general_arity/general_k_three_tasks_progress_20260915.md) · [general_k_grh_stage_and_remaining_tasks_20260915.md](../sources/outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md)

**条件／外部依赖：** 部分临界结果依赖Dirichlet L函数GRH，不能删条件

**还应读：** COMPOSITE-DEFINITIONS

**核验：** `python knowledge/project_knowledge.py verify COMPOSITE-FRONTIER` 只展示已登记命令及边界，不自动启动计算。

### COMPOSITE-DEFINITIONS · M、H、N与自动G维数不能混用

**状态：** 解释／综述，非新可达性证明。M最早成功、H首个非自动G成功、N此后全部成立，是不同量词；六平均九元自动成功，十元是非自动G点。

**边界：** 历史全局表中的开放范围以COMPOSITE-FRONTIER更新；未将候选临界线推广成已证最终阈值。

**原文：** [averaging_global_status_20260912.md](../sources/outputs/general_arity/averaging_global_status_20260912.md) · [composite_critical_scale_and_conjecture.md](../sources/outputs/general_arity/composite_critical_scale_and_conjecture.md)

**核验：** `python knowledge/project_knowledge.py verify COMPOSITE-DEFINITIONS` 只展示已登记命令及边界，不自动启动计算。

<!-- END SOURCE doc-f9fd4177f2c5 -->

---

<a id="doc-365cc5f17b32"></a>

## 原文导签：公共工具与路线边界

来源：`knowledge/topics/interfaces.md` · [逐字节原样副本](../sources/knowledge/topics/interfaces.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-365cc5f17b32 -->
# 公共工具与路线边界

[总状态](../sources/knowledge/STATUS.md) · [接手入口](../sources/knowledge/START_HERE.md)

跨主题先读这些共同工具和反例边界。历史文中方法的限制可以仍有效，原可达性目标却可能已经由其他路线完成。


| ID | 结论 | 状态 |
|---|---|---|
| G-OBSTRUCTION | G的障碍模、Smith余核与目标饱和 | 本地文稿已给证明，未独立重审 |
| STABILIZATION | 正双随机运输与3幂复制稳定化 | 原证明已完成 |
| EXTERNAL-ARITH | Morris／Serre外部定理的审核与边界 | 原证明已完成 |
| OLD-HECKE-AUDIT | 旧Ihara–Hecke／Manin接入的修正 | 修正／撤回过强表述 |
| WINDOW-MEAN | 局部窗口的均值与相对尺度障碍 | 原证明已完成 |
| OLD-TRACE-RETURN | 统一／双／混合迹零返回的历史接口 | 部分结果／明确范围 |
| BURAU-REASSESS | Burau路线的现有资源与临界带容量边界 | 解释／综述，非新可达性证明 |
| AFFINE-IDEAL | 仿射交换子理想：可逆宏已有后根参数可完整计算 | 原证明已完成 |
| PARAMETRIC-RIGIDITY | 固定参数词的有限射影周期刚性 | 原证明已完成 |
| N91-CONTAINER-CORRECTION | 九十一元21504容器等式已经被反驳 | 修正／撤回过强表述 |

### G-OBSTRUCTION · G的障碍模、Smith余核与目标饱和

**状态：** 本地文稿已给证明，未独立重审。O_p(X)=坐标R理想/差分R理想；其阶为G非p部分，沿操作有逆向满射。复制稳定条件对所有n成立。

**边界：** G不是保持不变的动态量；新障碍可以产生。目标可达性不能扩大成任意运输矩阵分解。

**原文：** [G_as_obstruction_group_and_stable_threshold_20260916.md](../sources/research/prime_arity_padic/G_as_obstruction_group_and_stable_threshold_20260916.md)

**还应读：** STABILIZATION, GEOMETRY-ALL-N

**核验：** `python knowledge/project_knowledge.py verify G-OBSTRUCTION` 只展示已登记命令及边界，不自动启动计算。

### STABILIZATION · 正双随机运输与3幂复制稳定化

**状态：** 原证明已完成。任意n：G为3幂 ⇔ 存在严格正三进双随机P消去X ⇔ 某个3幂复制后真实可达。

**边界：** 原位置分解不随运输存在自动成立；五、六元有复制后成功而原态失败。n≥7复制消去可由已证总定理推出，不是独立新证明。

**原文：** [triple_average_stabilization_theorem.md](../sources/outputs/triple_average/history/triple_average_stabilization_theorem.md)

**核验：** `python knowledge/project_knowledge.py verify STABILIZATION` 只展示已登记命令及边界，不自动启动计算。

### EXTERNAL-ARITH · Morris／Serre外部定理的审核与边界

**状态：** 原证明已完成。原素数证明所需有限指数、强同余性质及无限单位前提的明确引用接口。

**边界：** 已读来源与未取得原文须按审查文稿保留；有限模像满不推出全群包含。

**原文：** [prime_arity_lower_band_external_theorems_audit_20260915.md](../sources/outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md) · [prime_arity_endpoint_congruence_completion.md](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md)

**核验：** `python knowledge/project_knowledge.py verify EXTERNAL-ARITH` 只展示已登记命令及边界，不自动启动计算。

### OLD-HECKE-AUDIT · 旧Ihara–Hecke／Manin接入的修正

**状态：** 修正／撤回过强表述。保存原Hecke关系、星结构、中心符号及物理分支提升的审计；旧直接闭合推断不可作为定理使用。

**边界：** 不否定全部自守方法；七元实群、五元Aka–Shapira接口必须按各自已证前提使用。

**原文：** [triple_average_final_hecke_audit.md](../sources/outputs/triple_average/history/triple_average_final_hecke_audit.md)

**还应读：** SEVEN-GEOMETRY, FIVE-HECKE

**核验：** `python knowledge/project_knowledge.py verify OLD-HECKE-AUDIT` 只展示已登记命令及边界，不自动启动计算。

### WINDOW-MEAN · 局部窗口的均值与相对尺度障碍

**状态：** 原证明已完成。子块差分缩放只围绕子块自身均值，外部位置不跟随；不能当作整系统射影逆。

**边界：** 重写仿射矩阵或换称标记格不会自动提供窗口拼接定理。

**原文：** [prime_arity_middle_band_relative_scale.md](../sources/outputs/prime_arity/structure/prime_arity_middle_band_relative_scale.md)

**还应读：** GEOMETRY-ALL-N

**核验：** `python knowledge/project_knowledge.py verify WINDOW-MEAN` 只展示已登记命令及边界，不自动启动计算。

### OLD-TRACE-RETURN · 统一／双／混合迹零返回的历史接口

**状态：** 部分结果／明确范围。参数化周期和部分根公式成立；指定返回的原位置分解是更强目标，旧单返回充分性曾过强。

**边界：** 原可达性已由别的路线完成；运输／复制证书不是这些指定矩阵的原位置分解。

**原文：** [triple_average_universal_trace_zero_target.md](../sources/outputs/triple_average/history/triple_average_universal_trace_zero_target.md) · [triple_average_two_trace_zero_returns.md](../sources/outputs/triple_average/history/triple_average_two_trace_zero_returns.md) · [triple_average_mixed_singleton_controller.md](../sources/outputs/triple_average/history/triple_average_mixed_singleton_controller.md)

**还应读：** STABILIZATION, OLD-HECKE-AUDIT, AFFINE-IDEAL, PARAMETRIC-RIGIDITY

**核验：** `python knowledge/project_knowledge.py verify OLD-TRACE-RETURN` 只展示已登记命令及边界，不自动启动计算。

### BURAU-REASSESS · Burau路线的现有资源与临界带容量边界

**状态：** 解释／综述，非新可达性证明。正向中心、几何链及非零均值修正有效；三幂链最短容量与2p—4p临界带不匹配。

**边界：** Zariski稠密不等于算术指数／终端覆盖；不能因三平均就假设B₃。

**原文：** [burau_route_reassessment.md](../sources/research/prime_arity_padic/burau_route_reassessment.md)

**核验：** `python knowledge/project_knowledge.py verify BURAU-REASSESS` 只展示已登记命令及边界，不自动启动计算。

### AFFINE-IDEAL · 仿射交换子理想：可逆宏已有后根参数可完整计算

**状态：** 原证明已完成。可执行仿射生成元的导群参数理想由交换子与倍率局部化精确生成；无需逐参数搜根。

**边界：** 必须先有真实正向逆；非零理想不等于本原理想，导群也不必是全部平移核。

**原文：** [triple_average_affine_commutator_ideal.md](../sources/outputs/triple_average/history/triple_average_affine_commutator_ideal.md)

**还应读：** OLD-TRACE-RETURN

**核验：** `python knowledge/project_knowledge.py verify AFFINE-IDEAL` 只展示已登记命令及边界，不自动启动计算。

### PARAMETRIC-RIGIDITY · 固定参数词的有限射影周期刚性

**状态：** 原证明已完成。固定有理函数矩阵词若非恒等满足分圆迹关系，仅有限参数有有限射影阶；无限族须有恒等关系或变化词形。

**边界：** 不排除随参数无界增长的词，也不否定后来的统一正向种子。

**原文：** [triple_average_parametric_cycle_rigidity.md](../sources/outputs/triple_average/history/triple_average_parametric_cycle_rigidity.md)

**还应读：** OLD-TRACE-RETURN

**核验：** `python knowledge/project_knowledge.py verify PARAMETRIC-RIGIDITY` 只展示已登记命令及边界，不自动启动计算。

### N91-CONTAINER-CORRECTION · 九十一元21504容器等式已经被反驳

**状态：** 修正／撤回过强表述。模8和模91的尺度字符耦合，证明特定宏群不等于旧21504容器；必要容器修正为43008。

**边界：** 43008仍只是必要容器，未证明等于实际宏群；九十一元可达性已有独立归约，不能混为未解。

**原文：** [triple_average_permutation_shadow_entanglement.md](../sources/outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md)

**还应读：** OLD-HECKE-AUDIT

**核验：** `python knowledge/project_knowledge.py verify N91-CONTAINER-CORRECTION` 只展示已登记命令及边界，不自动启动计算。

<!-- END SOURCE doc-365cc5f17b32 -->
