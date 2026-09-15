# 历史路线账本（2026-09-15归档）

> 本文保留旧索引和 E／H／I 路线表。当前证明以[素数入口](prime_arity/README.md)为准；旧范围记录用于理解方法边界，不表示当前定理仍有缺口。

---

# 三平均与任意元数：当前状态和路线台账

更新：2026-09-15。**素数元平均的最优最终阈值已完成：每个奇素数 p 都有 N(p)=2p+1；N(2)=4。**

**三项主任务继续推进：** [本轮完成与剩余](general_k_three_tasks_progress_20260915.md)汇总四项完整结果：GRH下全部2、3的幂达到最早临界点；任意k的2k+1端点全部完成；十平均十六元有统一六步网络，M(10)=16；任意奇素数幂k的全部奇数2k<n<3k已完成。p>=5高奇次幂、一般混合临界点及其余维数接续仍开放；三项完成前不再研究去掉GRH。

**当前按用户选择在GRH下推进一般k。** [已完成范围与剩余三项任务](general_k_grh_stage_and_remaining_tasks_20260915.md)：全部t>=2的t²平均在t²+t+1元有完整G=1判据；对t=p^a，得到M(p^(2a))=H(p^(2a))=p^(2a)+p^a+1。H_t在当前条件性主线已关闭。一般素数奇次幂、混合元数临界点及临界后的全区间接续仍需证明，未宣布N(k)=B(k)。以下无条件H_t讨论保留为独立后续。

**H_t文献已给实质推进：** [小生成元调查与平方族充分大完成](ht_literature_and_eventual_square_completion_20260915.md)从Pollack2017定理1.1／2.7严格推出所有充分大的t均有H_t满群；素数模数n=t²+t+1由抽屉原理对全部参数完成。新有限阿贝尔商证书覆盖2<=t<1000，结合已发表Bach界的明确引用还得到GRH下全t成立。无条件全t尚缺数值界或剩余复合模数的统一证明；这些结果只完成相应平方族维数，不证明最终N(t²)。

**一般k平均执行计划：** [证明任务与验收条件](general_k_averaging_proof_plan_20260915.md)已采纳[建议文稿](general_k_plan_review_and_square_entry_20260915.md)：所有t的平方核心完整根和全输入入口均已具备，当前优先证明小整数生成的尺度群H_t满群。[复核记录](general_k_review_response_20260915.md)确认入口和一步终端限制，并补上一般k双块的精确G公式。H_t全称命题、全平方族临界结论及最终阈值仍未证明。

**策略梳理及合数新进展：** [素数证明主线与合数前沿](averaging_proof_strategy_and_composite_frontier_20260915.md)解释八个证明环节、已有S(q)临界猜想及其真正困难，并新增素数因子“块均值模拟”定理，覆盖全部q平均的n=kq、k>=3。[平方元数统一控制器](square_arity_uniform_controller_and_nine_thirteen.md)从四平均七元的宏直接推出参数周期，完整解决九平均十三元，得到M(9)=H(9)=13；未证明N(9)=13或全部合数最优阈值。

对全部 n>=2p+1，非全等有理输入经有限次原位置 p 平均可达全等，当且仅当中心化、清分母、本原化后的差分 gcd 为 p 幂。p 不整除 n 时才可简写为 G=1。n=2p 的一般反例保证奇素数阈值最优。

## 1. 当前证明的阅读顺序

本次合数调查实际读过的文档、章节及补读时间见[阅读记录](research_reading_log_20260915.md)。后续调查须主动列出直接阅读、间接引用和未核验内容。

1. [九偏移的共同完成](prime_arity_nine_offsets_large_symmetric_carrier_completion.md)：最新关键步骤。将 (2p,p,s) 改成 (p,p,p+s)，统一解决全部3p+s、1<=s<=9。大p有闭式计数；小p由同一接口的522组完整有限参数证书和两项局部补充接续。
2. [最后复核记录](prime_arity_nine_offsets_completion_audit.md)：原位置、逆、局部化、换基、辅助13、二进单位、精确终端，以及本次草稿纠错的准确边界。
3. [全部2p+2及下半带汇合](prime_arity_two_p_plus_two_uniform.md)、[全部3p-1](prime_arity_three_p_minus_one_completion.md)：与无条件入口、奇余量及内部偶余量合并，完成全部2p<n<=3p。
4. [所有素数的3p+10以上](prime_arity_all_prime_three_p_plus_ten.md)、[全部4p以上尾部](prime_arity_four_p_tail_completion.md)：旧d_p条件遗留的上方间隙已覆盖。
5. [2p反例](prime_arity_linear_threshold.md)：提供最优阈值的下界。[外部定理审核](prime_arity_lower_band_external_theorems_audit_20260915.md)给Morris/Serre的准确引用及访问边界。

上述是存在性证明，仍不提供对可变p、n的多项式平均词长、最短路径或实用的一般群词提取。一般合数平均元数的最优阈值仍未完成。

## 2. 当前结论与计算证据

| 对象 | 当前完整结论 | 证据与阅读入口 |
|---|---|---|
| 奇素数p | N(p)=2p+1，所有后续维数均有p幂G充要判据 | [新完成证明](prime_arity_nine_offsets_large_symmetric_carrier_completion.md)及其列明的既有区间 |
| 二平均 | N(2)=4；首个非自动G边缘H(2)=5 | [定义与二平均](averaging_global_status_20260912.md) |
| 三平均 | N(3)=7，另有不依赖一般算术群路线的直接证明 | [任意维数直接证明](triple_average_all_dimensions_double_triple_invariant.md) |
| 九平均 | 十三元完整G=1判据，M(9)=H(9)=13；最终N(9)仍未确定 | [平方元数周期与九平均证明](square_arity_uniform_controller_and_nine_thirteen.md) |
| 2、3的全部幂，GRH下 | 每个元数的最早临界维数已达到；最终N尚未统一确定 | [奇次幂与共同ms²控制器](two_three_odd_power_critical_grh_completion.md) |
| 任意整数k>=2 | 全部2k+1元端点的G=1判据 | [偶元数补齐](even_arity_all_endpoints_completion.md) |
| 奇素数幂k | 全部奇数2k<n<3k的完整判据，包括gcd(k,n)>1 | [奇合数区间与因子转译](odd_composite_coprime_middle_band_completion.md) |
| 十平均 | 十六元固定六步网络，M(10)=16；H(10)=17；N仍未定 | [三块固定网络](ten_average_sixteen_and_dyadic_network_family.md) |
| 全部平方元数，GRH下 | 每个k=t²在n=t²+t+1完整成立；素数偶次幂达到M和H的下界 | [条件性定理及量词](general_k_grh_stage_and_remaining_tasks_20260915.md) |
| 任意q的倍数维数 | 所有n=kq、k>=3具有完整“G的素因子均整除q”判据；另有更一般素数因子转译 | [策略文稿第5、6节](averaging_proof_strategy_and_composite_frontier_20260915.md) |
| 任意整数元数q>=3 | 既有n>=4q-1+d_q(n)时，rad(G)|q为充要条件；一般最优阈值仍开放 | [任意元数上界](arbitrary_arity_linear_threshold.md) |
| 困难输入与算法评测 | 旧有限路径、冻结态及算法测试集仍有用；不可把搜索失败写成不可达 | [算法测试集](averaging_algorithm_benchmark.md) |

新核验ID：`nine-offsets-large-symmetric-carrier`。

- [完整小参数证书](../work/large_symmetric_carrier_small_certificate.json)覆盖全部522组参数，核对2206条根反射计数及相应入口、方向、单位接口。
- [独立核验器](../work/check_large_symmetric_carrier_certificate.py)不导入候选生成器；一般无限量词由正文证明承担。
- [清单](../work/verification_manifest.json)记录证据等级、外部依赖及不涵盖的算法问题。

**文档优先级：** 本页第1、2节是当前结论；下面第3至5节保留各方法当时做到的范围，用于防止重复研究。历史表内“仍缺”“尚未完成”不再表示素数p的可达性定理仍有缺口；其中限定的直接算法、固定宏或更强结构问题可能独立开放。

**符号注意：** 当前p表示平均元数，n表示位置数。许多旧triple_average_*文件的p表示三平均的位置数，两类问题不可混用。

## 3. 端点及跨维数：哪些已经研究过

编号用于检索和后续更新。“所需增量”指在已有成果和障碍之外，尚需新增的数学内容。

| 编号 / 路线 | 已有成果与失败的准确范围 | 再推进所需增量 | 必读 |
|---|---|---|---|
| E1 正向种子、根、核心轨道 | 统一资源已证；同日新证明用有限指数及强同余性质补齐任意合数核心，绕过短主元菜单 | 核心存在性任务已完成；可另研究可计算分解和长度界，不再重搜种子 | [同余闭合](prime_arity_endpoint_congruence_completion.md)、[旧CRT证书](composite_endpoint_crt_transfer.md) |
| E2 直接划分与CRT入口 | 三单点交换子与模意义正向逆已补齐任意多素数入口；K4和单角色覆盖障碍被绕开 | 入口存在性已完成；可优化交换周期和实际词长 | [无条件入口](prime_arity_unrestricted_endpoint_and_odd_band.md)、[旧六素因子](prime_arity_six_prime_endpoint_entry.md) |
| E3 反向找反例 | 整数冻结已分类为大背景加零和自由例外；若干族已有分数逃逸，七平均十五元已全解 | 真反例须排除分数路径；或在仍开放范围证明新逃逸族 | [反向诊断及纠正](prime_arity_endpoint_counterexample_reverse.md) |
| E4 嵌入更大系统 | 已研究局部均值与相对尺度；射影逆嵌入后只收缩子块，外部不跟随 | 能处理外部总和及相对尺度的真实可重复构造 | [相对尺度](prime_arity_middle_band_relative_scale.md)、[局部几何第7节](prime_power_endpoint_and_critical_geometry.md) |
| E5 块—单点交换、改能量 | 交换自动保持非p同余；非整数交换本原平方高度不降；共同单调固定正定二次型唯一性已证 | 状态相关返回或离散高度；只换固定二次权重不够 | [精确增量与唯一性](prime_arity_energy_and_dyadic_neighbour.md) |
| E6 等值化、受限Euclid | 全部下半带入口完成，全部奇数维数全输入已解；双载体小分母有统一算法 | 一般偶数核内终止仍开放 | [无条件入口](prime_arity_unrestricted_endpoint_and_odd_band.md)、[双载体复查](prime_arity_core_gap_reassessment_20260915.md) |
| E6d 双单点完整Euclid | p+1仅含2和至多一个奇素数时，最近奇数加一次除二修复给原位置严格下降；n=2p+2全输入完成 | 多个奇素因子可能相继阻断安全数字；p29仅排除该一轮下降规则，不是不可达反例 | [完整证明，第11节](prime_arity_unified_weighted_core_theorem.md) |
| E6b 偶余量深同余与深度下降 | 内部偶余量有深主同余；全部偶数r含2、p-1现可用状态相关返回将v2(az)降到1，跨越旧对合不变量 | 深度一中的全部方向、奇素数和共同尺度的终端覆盖 | [一般深度下降](prime_arity_unified_weighted_core_theorem.md)、[旧同余控制](prime_arity_even_middle_congruence_and_eighteen.md) |
| E6c 单对合边界的多宏取逆 | 七平均20、22的短标量闭路提供非迹零宏的正向逆；22元保留两个单位尺度类后联合轨道全覆盖，N(7)=15 | 一般p的相应闭路或其他可执行取逆机制；五平均12、14仍开放 | [七平均完整闭合](seven_average_sharp_threshold_complete.md) |
| E7 相邻维数内插 | 一般内插原则为假；有不可直接调用的2p+1子块族及余维一障碍 | 核对局部仿射格、全局目标和原位置模拟的传播定理 | [维数传播](prime_arity_interpolation_and_lattice_structure.md) |
| E8 固定短词覆盖 | 固定长度原子词表不能覆盖全部临界合法方向 | 输入相关长度，加递归/除法规则及终止证明 | [前沿第4.5节](prime_arity_critical_frontier_handoff.md) |

**2026-09-14对话的去重说明：** 将外部总和写为S、把端点返回写成带S的仿射式，是E4的坐标表达，不构成新路线。更换单点、围绕局部均值分析收缩属于E4至E6已经尝试的内容。新增进展必须提供上述文档未有的可执行控制或终止论证。

## 4. 三平均历史算术路线

旧文的“最小未解71”“只差种子”是2026-09-11直接证明之前的状态。原三平均问题已通过另一条证明完成；指定宏的更强实现问题可以独立开放。

| 编号 / 路线 | 可保留内容 | 已知边界及入口 |
|---|---|---|
| H1 17至59、非分裂轨道 | 根提取、Schreier、终端；删点Reynolds层及字符公式 | 双载体全空间两层等角障碍有一般证明；其他短词未命中限于有限语法。[结构综合](triple_average_nonsplit_prime_structure_synthesis.md)、[轨道](triple_average_nonsplit_punctured_orbits.md) |
| H2 仿射交换子 | 导群参数是倍率局部化环上的显式理想，可统一计算本原性 | 需要实际可逆仿射元；非零根不等于本原根或全轨道覆盖。[交换子理想](triple_average_affine_commutator_ideal.md) |
| H3 参数周期刚性 | 固定有理函数词的非恒等周期条件只命中有限多个参数 | 不排除符号恒等周期或随参数增长的词长。[周期刚性](triple_average_parametric_cycle_rigidity.md) |
| H4 统一/双/混合迹零 | 混合双返回条件定理已补齐根理想与终端；先前单返回的过强充分性已纠正 | 指定返回原位置分解未证；正运输或副本实现不是原位置实现。[单目标](triple_average_universal_trace_zero_target.md)、[双返回](triple_average_two_trace_zero_returns.md)、[混合返回](triple_average_mixed_singleton_controller.md) |
| H5 伴随、复制消去、数字层 | 全原子倒序可执行；适用域和二维强返回已有审计 | 压缩Gram相等不推出像不变；叶差收缩不带动局部均值。须检查W*WE=lambda E及账本。[原位置分解前沿](triple_average_original_position_factorization_frontier.md) |
| H6 Hecke/Manin/模形式 | 有限Hecke关系、算术格及theta联系有准确内容 | 指定星结构、中心负号、单cusp商、分支之和存在障碍。暂停的是旧直接接入方案。[最终审计](triple_average_final_hecke_audit.md)、[theta联系](prime_power_endpoint_and_critical_geometry.md) |
| H7 合数归约与高斯周期 | 三平均旧合数归约有效；一般p能推广部分范数周期 | 临界小商未必可解，旧剪切恒等式不能直接替换p。[重新评估](prime_arity_revisiting_ternary_factor_gaussian_route.md) |

重新借用H6需要明确的数学空间、作用、映射及真实分支提升，不能只改称“覆盖”“饱和”或“gallery”。H2、H3仍是可用代数工具，不应一并归入“群论失败”。

## 5. 上半带与近期不变量改进

| 编号 / 路线 | 目前做到哪里 | 尚未解决或已排除的内容 | 入口 |
|---|---|---|---|
| I1 固定核心返回降能 | 全输入核心入口已证；七平均22元十个不交核心返回已审计 | 该输入没有这种合法降能返回，却有两步重叠造零；只排除该菜单 | [核心陷阱](prime_arity_three_p_remaining_gap.md) |
| I1b 四返回算术控制 | 两种载体各取相邻参数，显式得到U(rn²R)、L(rn²R)及Gamma(r²n⁴,R)；p>=13的3p+10至4p-3容量统一成立；I1d已补齐完整终止 | 3p+1无本菜单四返回，两端低容量仍须新工具 | [四返回迁移](prime_arity_upper_band_four_return_congruence.md) |
| I1c 主同余升级与二三单位下降 | 旧与6互素完整族及Smith-CRT逆继续有效；gcd(n,6)限制现由I1d删除 | 旧n/11小代表不是一般局部类型所必需 | [旧完整族证明](prime_arity_upper_band_coprime_six_complete.md) |
| I1d 深层取逆与全局单位像 | 整个3p+10至4p-3全输入完成；去除r辅助素数，真实返回数字生成全部单位像，2、3及其他素数同时完成方向与尺度 | 3p小余量；4p下方两条边界由I1e在p>=37完成，上方由I1f完成 | [无条件上半带](prime_arity_upper_band_unrestricted_completion.md) |
| I1e 一次重叠替换载体 | p>=37的4p-2、4p-1全输入完成；新矩阵对m统一，根无r因子，辅助p由局部SL2消去，单位平移无m+1因子 | 容量仍约要求r>p/m；上方低余量现由I1f的大载体处理，不再重搜上端B载体种子 | [重叠返回与完整证明](prime_arity_upper_band_overlap_completion.md) |
| I1f 双份新载体与尾部密度 | n=4p+s的旧遗漏强制d>=s+3，保证p>=16s+21和单位计数；全输入进入(2p,p,p+s)，五步对合根gcd仅gcd(n,5)，完整关闭全部尾部 | 不解决一般3p小余量，不给多项式词长；不应再把761/3045列为未解接续 | [尾部及3p+10阈值](prime_arity_four_p_tail_completion.md) |
| I1g 容量与仿射行列式接口 | 八组较小p以单位密度替代大p小代表；三个单A边界用两种重叠族及两轮局部提升完成。N(p)<=3p+10现对所有素数成立 | p=11的34至42仍属于一般低余量；有限参数核验不等于有限高度输入验证 | [全部素数统一阈值](prime_arity_all_prime_three_p_plus_ten.md) |
| I1h (3p-1) 重叠反射 | 所有p>=7统一得到双向2n根、全部单位尺度和精确终端；p=5以夹乘处理，N(5)=11 | 2p+2已由I1i完成；上方低余量仍须继续 | [统一3p-1证明](prime_arity_three_p_minus_one_completion.md) |
| I1i (2p+2) 状态相关CRT终端 | 正确三步重叠反射给 Gamma(h²,Z[1/p])；一次 Mp 和一次 Mq 直接安排 v=+-1 mod h²，所有素因子统一处理 | 上方九个低余量的初始返回资源仍不足 | [统一2p+2证明](prime_arity_two_p_plus_two_uniform.md) |
| I1j 小载体逆与可解商分离 | p=1模3有固定四原子收缩逆；p=4模9的3p+1全输入完成。完美局部群分离统一删除辅助素数 | 其他p的同余分支及s=2至9尚未完成；模双曲线只给可逆返回，不自动给根 | [新完整族](prime_arity_three_p_plus_one_residue_four.md)、[统一反射接口](prime_arity_low_offset_unified_frontier.md) |
| I1k 载体打包与三点轨道 | s=mb、m<=3提供标准收缩的真实逆；m=1、2与反向仿射接成nR根，完整解决偏移2、4、8和更一般偶余量区间 | n含2或3时不能直接反演危险素数；剩余s=1,3,5,6,7,9 | [共同控制器](prime_arity_even_low_offsets_common_controller.md) |
| I1l 三进相位与条件数字返回 | U(3R)及一个横向反射给明确深层，至多一次模3相位调整、两个CRT返回送到精确终端，完成偏移3/6的指定p类；短筛选另完成偏移9的p=1模3 | 高三进相反类仍缺无条件起步与闭合；第12节只有条件原位置消去，不是全解 | [三进共同证明](prime_arity_triadic_packed_carrier_completion.md) |
| I2 来源关系 | 指定出口后第二次安全整数续步已证；r>=2保留额外四值关系 | r=1来源式退化为当前零和式；任意安全后继都可继续为假 | [来源与动态阶段](prime_arity_provenance_dynamic_and_integer_stages.md) |
| I3 动态保护 | 指定后继危险支持完全重合，至多保护一处，由gcd(3alpha-2,n)确定 | 不是任意多值状态都如此；固定某个极小保护集可能错过有效操作 | [动态阶段](prime_arity_provenance_dynamic_and_integer_stages.md)、[保护交换](prime_arity_protected_exchange_and_mass.md) |
| I4 单位见证补回 | Hilbert基、容量、Euclid转移、重叠覆盖全部规定单位碰撞入口；旧十个缺口含p983已补齐 | 多值输出未证递归重入；重值对下移不自动降低全局最大值 | [完整补回](prime_arity_complete_unit_collision_recovery.md)、[转移](prime_arity_euclidean_witness_transfer.md)、[容量](prime_arity_unit_witness_replenishment.md) |
| I5 弱重数不变量 | S_p>=2p-1+h给一步安全条件；规定维数下停滞态有单背景结构 | (p,p-1)、单独S_p>=2p-1有任意大维数停滞族；相邻双重值不能普适单步保持 | [锐边界](prime_arity_sharp_repetition_and_precision_barriers.md)、[单位对障碍](prime_arity_unit_witness_replenishment.md) |
| I6 非二次势、约分 | 整数阶段能量/两两距离下降；部分分支最大值下降；模q全零后有合法约分实例 | 固定原A,C的分数阶段排除公因子约分，并阻止指定高度下降；未排除一切非二次势 | [势的范围](prime_arity_invariant_improvements_and_core_exit.md)、[约分障碍](prime_arity_provenance_dynamic_and_integer_stages.md) |
| I7 整数返回、精度 | 奇素数首次离格到返回同格至少五步；一类输入恰需一位额外精度 | 安全、实能量下降、当前一位精度不足以维持下一步同格；坏前缀会冻结 | [精度边界](prime_arity_sharp_repetition_and_precision_barriers.md) |
| I8 五步参数消去 | 精确记录显示多值来源可消去并恢复固定形状；p3有参数收缩对照 | p>=5指定规则可使归一化参数增长。尚无正式证明文档及清单登记，不能按脚本标题认定一般非终止定理 | [记录](../work/parameter_erasure_recurrence_records.json)、[程序](../work/verify_parameter_erasure_recurrence.py) |
| I9 逆零和与组合选择 | 尖锐两桶界、极端冻结族逃逸、高重/分散余类及部分碰撞分支 | 中等重数多余类交互未闭合；模零筛选后的选组一般不是拟阵基 | [集中与逃逸](prime_arity_sharp_concentration_and_escape.md)、[加法接口](prime_arity_three_p_additive_interface.md) |
| I10 不同实际值归约 | D>=d+2k-1时有安全整数操作，有限降至D<=d+2k-2 | 是前处理；较大n仍可只有三种值而冻结 | [不同值数](prime_arity_distinct_value_integer_reduction.md) |

I8记录范围：209个五原子消去实例、140个来源方向检查、六个素数各20轮递推、8个三平均收缩实例，以及p983补回输出接入。这些检验规定构造，不证明任意合法后继递归归零。本次没有重新运行或扩大实验。

## 6. 后续研究先说明新增了什么

素数元平均的阈值任务已由大载体共同证明完成。下表是可继续研究的直接算法和结构问题，不再是证明N(p)=2p+1所必需的缺口。

| 任务 | 可复用起点 | 应证明的新增内容 |
|---|---|---|
| 停滞态分数逃逸 | E3、I5、I7、I9 | 完整参数族的安全出口及有限返回/零触发；不重复已有极端族 |
| 迁移见证与合法约分 | I3、I6 | 实际操作同时控制非p合法性、公因子、分母，而非仅写净高度条件 |
| 多值后继递归选择 | I2、I4、I8 | 出口仍可处理，每个非终端有允许选择及离散下降；正反例均登记 |
| 端点/中间带控制 | E1核心已闭合，E2入口及E4至E6仍部分开放 | 处理更多素因子入口，或外部质量的原位置构造；再次写出仿射矩阵不够 |

后续优先级为：整理完整论文及其依赖链；优化实际词提取和长度界；研究任意合数平均元数的最优阈值。I8及平方能量支线的限定性障碍仍保留，但不应再次将它们列为素数元平均存在性证明的前置任务。

## 7. 检索、证据与维护

文献入口：[2018至2026综述](averaging_literature_survey_2018_2026.md)、[策略与全文边界](prime_arity_strategy_reassessment_20260912.md)、[零和文献核对](prime_arity_shape_potential_literature_interface.md)。逆EGZ、零和自由序列、受限和集、群标记组合选择、受限切换与多Lyapunov函数、S整数环初等生成均已有查阅；查阅过不等于已建立本题接口。

新尝试前按数学特征检索，不仅搜索拟起的新标题：

    rg -n "相对尺度|局部均值|单点.*交换|等值化" outputs
    rg -n "冻结|停滞|精度|约分|本原.*高度" outputs
    rg -n "非分裂|交换子|迹零|周期刚性|Hecke|Manin" outputs

新增记录注明：适用元数/维数、原位置操作、对应哪条路线、增加了什么、仍缺什么。反例须说明只针对整数路径、某个宏菜单还是固定不变量；有限阴性诊断记录语法与范围。固定维数成功、合法入口、核内轨道、全部后续维数是四种不同结论。

核验等级以清单为准：theorem-certificate闭合明确的有限证书子问题；symbolic-check核对精确公式；finite-sanity是有限实例；exploratory-search是有限搜索。任何等级都不能超出正文量词。新增计算结论应补专题证明与清单，纯导航维护无需重跑整个研究库。

主研究目录是本文件的上级目录。2026-09-10/new-chat/outputs及聊天根目录存在历史副本，不能凭同名认定同步。本次不移动旧文件；之后更新主目录正文和本索引，避免增加同名内容副本。

## 8. 已过期状态速查

- “九偏移尚未统一／N(p)<=3p+10”：已由大载体共同证明取代，奇素数N(p)=2p+1。
- “下半带偶数或2p+2、3p-1仍开放”：均已全输入完成。
- “4p以上还有d_p缺口”：已由尾部证明完整接续。

- “三平均最小未解71 / 必须补统一种子”：已由任意维数直接证明取代；指定宏问题单独保留。
- “七平均十五元未解”：已由两素数入口和Gamma_0(15)完整覆盖解决。
- “p97 / n195缺入口”：已由四素因子入口补齐；早期28全输入/8核心只是当时证据分工。
- “单位补回还缺十个入口，含p983”：已全覆盖；多值递归仍未闭合。
- “非p保护总要留d处”：只是通用预算；特定交换自动安全，指定核心后继至多一处。
- “统一迹零返回就足以完成根与轨道”：早期表述过强，以混合双返回的条件定理为准。
- “解完3p<n<4p便自动有N(p)<=3p”：还须检查4p以上旧上界遗漏维数，如p761、n3045。
- “任意合数端点核心仍缺群包含”：2026-09-14同余闭合证明已补齐，依赖Morris 2007定理6.1(2)与Serre强同余子群性质；全输入入口仍另计。
- “五平均十三元只完成入口”：同日后续已接两个旧对合与主同余控制，完整G=1判据成立；十二、十四元仍未证。
- “一般奇数r只知道一个对合”：3<=r<p时始终有两个指定对合，现已接成完整核心定理；七平均17、19元完成，剩18、20、22元。
