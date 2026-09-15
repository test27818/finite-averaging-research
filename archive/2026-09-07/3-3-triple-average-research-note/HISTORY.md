# 历史进展日志（截至2026-09-15整理前）

> 本文保留原根 README。当前状态请读[项目入口](README.md)和[素数证明入口](outputs/prime_arity/README.md)；下文过期的“未解／下一步”不作当前结论。

---

# 三平均有限步可达性研究

> **研究入口（2026-09-15）**：先读 [outputs/README.md](outputs/README.md)。它汇总已完成结果、已排除路线、当前瓶颈和下一步优先级；本页以下是按日期累积的详细记录。

> **GRH三项任务新进展**：[状态与证明入口](outputs/general_arity/general_k_three_tasks_progress_20260915.md)。GRH下全部2、3的幂达到最早临界点；所有整数元数k的2k+1端点补齐；十平均十六元固定六步网络给M(10)=16；奇素数幂的全部奇数2k<n<3k由旧证明的真实互素条件和块均值转译完成。四项均有完整正文和已通过的精确核验；未宣布一般N(k)=B(k)。

> **用户已选择以GRH为主线假设推进一般k**：[条件性平方族完成及剩余任务](outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md)正式汇合全部t²平均在t²+t+1元的完整判据，素数偶次幂的M、H达到旧下界。H_t不再作为当前主线缺口；下一阶段为素数奇次幂、混合元数及全区间接续。结论明确保留GRH条件，未证明一般最终N(k)=B(k)。

> **H_t已有文献直接适用**：[文献调查](outputs/general_arity/ht_literature_and_eventual_square_completion_20260915.md)实际读到Pollack2017任意模数真子群的小非剩余定理，证明H_t对所有充分大的t无条件成立；n=t²+t+1素数时另有全范围抽屉原理。精确商秩证书补齐t<1000，GRH下得到全t命题；无条件全t仍未完成。已记录3份实际读取的PDF、其余题录／间接引用及2025显式Burgess的适用限制。核验ID ht-literature-interfaces。

> **采纳平方入口建议**：[建议文稿](outputs/general_arity/general_k_plan_review_and_square_entry_20260915.md)已用旧三单点交换子补齐所有t的(t²,t,1)全输入合法入口；[复核](outputs/general_arity/general_k_review_response_20260915.md)确认，并将下一任务集中到小整数尺度群H_t。现有一步终端全在H_t中；入口和t-1根因子已不再开放。独立核验10条入口、404个原子通过；t<=200的H_t满群只是有限诊断。

> **一般k平均后续计划**：[任务顺序与明确验收](outputs/general_arity/general_k_averaging_proof_plan_20260915.md)安排平方族入口和尺度、素数幂、宽区间接续与混合元数。规划复核同时将平方核心资源加强到所有t的U(R)、L(nR)：取得可逆Delta(2)后重新与Sigma作交换子即可，旧t-1奇因子障碍已解除。一般平方族全输入临界定理仍未完成。

> **证明策略与合数继续推进**：[整体策略及合数临界结构](outputs/general_arity/averaging_proof_strategy_and_composite_frontier_20260915.md)重新按入口、真实逆、根、同余控制、方向与尺度、精确终端梳理素数证明；新增块均值转译，完成任意q的全部n=kq、k>=3。另由[平方元数统一周期](outputs/general_arity/square_arity_uniform_controller_and_nine_thirteen.md)和显式除二夹乘完成九平均十三元，M(9)=H(9)=13；没有将其外推为N(9)=13。核验ID square-arity-controller-nine-thirteen、prime-factor-block-mean-transfer。

> **素数平均最优阈值现已完成**：[大载体与两个等大块](outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)用共同的(p,p,p+s)核心解决全部3p+s、1<=s<=9。接已证其余区间及2p反例，得到每个奇素数p的N(p)=2p+1；N(2)=4。p>=307由统一闭式计数证明，较小p用同一接口的522组完整有限参数证书和两项明确局部补充。已复核原位置、真实逆、根理想、全部方向、单位尺度和精确终端；沿用Morris/Serre依赖。[最后复核记录](outputs/prime_arity/audits/prime_arity_nine_offsets_completion_audit.md)。核验ID nine-offsets-large-symmetric-carrier。

**以下为历史进展日志。** 其中“九偏移未解”“N(p)<=3p+10”“一般素数最优阈值尚未证明”均是当时状态，已由上面的完成证明取代；旧方法的限定性障碍仍保留其原数学意义。

> **三进共同终端与半数素数的新最终上界**：[三进载体证明](outputs/prime_arity/history/prime_arity_triadic_packed_carrier_completion.md)完成3p+3、p=1模3与3p+6、p=2模3；第11节完成3p+9、p=1模3。因此p=1模3有N(p)<=3p+8，全体素数仍为3p+10。核心是U(3R)、横向反射及两次状态相关CRT，未搜索平均词或有限群。未完成参数继续保留在完整目标中。核验ID triadic-packed-carrier-completion、nine-offset-residue-one。

> **三个低余量统一完成**：[载体打包共同控制器](outputs/prime_arity/history/prime_arity_even_low_offsets_common_controller.md)证明所有素数p>=5的3p+2、3p+4、3p+8，并覆盖r偶、3不整除r、p>=2r的一般区间。根理想恰为nR，Gamma(n)后一次模n平移完成，未搜索平均词。一般剩余为s=1,3,5,6,7,9；所有n>=2p+1且gcd(n,6)=1已完成，但N(p)<=3p+10未进一步降低。核验ID even-low-offsets-common-controller。

> **小载体的新完整族**：[3p+1、p=4模9](outputs/prime_arity/history/prime_arity_three_p_plus_one_residue_four.md)以统一收缩逆、迹零恒等式和完美局部群/可解商分离完成全输入判据。九族共用的原位置反射条件现为(3t+b)(3v+s)=bs modp；它只提供可逆返回接口，尚不证明其他偏移终止。完整目标仍是全部素数、全部n>=2p+1。核验ID three-p-plus-one-residue-four。

> **全部素数统一3p+10，无小p阈值例外**：[容量、单位密度与局部提升](outputs/prime_arity/proofs/upper_band/prime_arity_all_prime_three_p_plus_ten.md)将同一返回接口用于19、23、29、31的八组上端参数，再以两个仿射族和共同的两轮局部提升完成(13,50)、(13,51)、(17,66)。结合已证素数位置数43、67以及4p尾部，得到所有素数p>=5的N(p)<=3p+10。2、3另有更强定理。p=11的34至42仍属于一般3p+1至3p+9家族，未宣称已解；p=2、3、5、7的上半带原本已完成。核验ID upper-band-small-prime-interface。

> **全部3p-1已完成**：[统一3p-1证明](outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md)对所有素数p>=7给出同一重叠反射和乘3折返证明，p=5的14元由显式夹乘补齐，得到N(5)=11。下半带仍有2p+2，已由下一项补齐；上方仍是3p+1至3p+9这九种偏移族。

> **全部2p+2已完成**：[统一2p+2证明](outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md)删除 p+1 至多两个素因子的限制。正确的三步重叠反射给深主同余，两个状态相关返回把载体坐标直接安排成 +-1 模控制层；所有素数的 2p<n<=3p 现在都已完成。上方九种偏移仍开放。核验ID two-p-plus-two-uniform。

> **九个低偏移的统一前沿**：[低偏移结构](outputs/prime_arity/history/prime_arity_low_offset_unified_frontier.md)修正旧模板容量和组合充分性表述，新增一次模逆的共同原位置反射公式。一般九族仍未完成，不再把缺少锚点保留与整数初始化的组合候选称为充分归约。

> **4p上方尾部完整关闭，达到3p+常数阈值**：[统一d_p尾部证明](outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_four_p_tail_completion.md)证明每个素数p>=5的全部n>=4p完整判据；结合上端和小p接口，所有素数满足N(p)<=3p+10。仍未证明N(p)<=3p；一般3p+1至3p+9偏移族仍须处理。核验ID four-p-tail-completion。

> **一次重叠统一补齐上端**：[重叠载体返回](outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_overlap_completion.md)及后续小p接口证明所有素数p>=13的4p-2、4p-1全输入G=1判据；4p上方尾部也已关闭。3p小余量仍开放。核验ID upper-band-overlap-completion。

> **上半带内部区间统一完成**：[无条件上半带证明](outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_unrestricted_completion.md)证明所有素数p>=13、3p+10<=n<=4p-3的全输入G=1充要判据，删除旧gcd(n,6)=1限制；上端及4p上方已有后续证明。核验ID upper-band-unrestricted-completion。

> **端点与全部奇数下半带现已完整证明**：[三单点交换子与无条件入口](outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)。三个单点角色的交换子给出模rad(n)的真实正向剪切；失效素数整除r+2，其见证可由r个保留位置承接。由此删除端点六素因子/密度条件及下半带r>=omega(n)条件，接已有核心定理得到任意奇p的全部2p+1端点、任意素数p的全部奇数2p<n<3p全输入G=1判据。所有偶余量入口也已完成，但一般偶数核心与最终阈值仍未全解。核验ID unrestricted-endpoint-entry。

> **核内缺口复查**：[常高度乘法、有限例外与多步下降](outputs/prime_arity/history/prime_arity_core_gap_reassessment_20260915.md)。保载体返回可在完整约分后使用整除p+1的奇数数字，给出全部本原分母v<=p+1的合法双载体核统一归零算法；结合明确引用的Furstenberg拓扑定理，固定素数p下的剩余分母只有有限多个，但没有有效界或全例外覆盖。另有无限一步失败锥及两种真实逃逸。一般2p+2全输入、其他偶余量和最终阈值仍未完成；核验ID core-gap-four-lifts。

> **邻点完整终止更新**：[统一文稿第11节](outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)证明所有奇p>=5且omega(p+1)<=2的n=2p+2全输入G=1判据。最近奇数加一次除二配比修复，使本原正奇整数v每轮严格下降到1，全部操作有原位置实现；没有使用算术群或闭路搜索。五平均12元已解，只剩14元。任意p的整个中间带仍未全解。

> **二进深度工具**：[统一文稿第10节](outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)把每个偶余量合法核心的v2(az)降到1；r=2、p-1已分别由统一状态相关CRT和重叠反射完成。

> **内部偶余量新完成**：[全部内部偶余量](outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md)利用有限逆提升、局部循环和完整单位尺度输送，证明所有素数p>=7、4<=r<=p-3的偶数核心全输入G=1判据；两个边界r=2、p-1已有后续统一完成。

> **完整阈值更新：N(7)=15。** [七平均20、22元与最优阈值证明](outputs/prime_arity/examples/seven_average_sharp_threshold_complete.md)补齐最后两个核内缺口。固定正向标量闭路提供逆，主同余包含后完整检查方向与单位尺度；22元的3872个联合状态全在一个终端轨道。接旧结果和十四元反例得到最优阈值。一般p与五平均14仍开放；以下旧日志中的“七平均未解20、22”已由本项取代。

> **中间带统一证明入口**：[整数格、整族终端与两轮入口](outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)。两条带使用同一个m=1、2加权核心，明确保留非幺模换元的2、3局部信息和有限单位尺度。两轮修复接最新三单点交换子初始化后，下半带入口不再需要任何素因子数或密度条件；一般偶数核内终止仍未证明。后续阅读以统一文稿、新入口证明及状态表为主，下面日期日志用于溯源。

2026-09-14上半带完整定理：[与6互素维数的统一证明](outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_coprime_six_complete.md)完成任意素数p>=13、3p+10<=n<=4p-3且gcd(n,6)=1的全输入G=1判据，不限制n素因子数。额外对合统一反演r，三个一阶方向加强到Gamma(n)，Smith-CRT夹乘给安全整数返回的正向逆，半载体激活3，二三单位小代表与Bezout送到零触发终端。274组参数和822条精确目标输送等核验通过；被2或3整除的维数、两端短区间及4p上方接续仍开放，最终阈值未降低。核验ID upper-band-coprime-six-complete。

2026-09-14上半带迁移：[四返回双向根与深同余控制](outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_four_return_congruence.md)把现有两种载体各取相邻参数，统一构造U(rn²R)、L(rn²R)，接深同余引理得到Gamma(r²n⁴,R)。所需容量对p>=13、3p+10<=n<=4p-3全部成立；有限终端覆盖、两端小余量和4p上方接续未证。本项不新增完整维数或降低最终阈值。核验ID upper-band-four-return-congruence。

2026-09-14偶数维数推进：[偶数深同余与七平均十八元](outputs/prime_arity/history/prime_arity_even_middle_congruence_and_eighteen.md)证明任意内部偶余量4<=r<=p-3的深主同余控制，并以短配比替代部分失败的周期入口。七平均18元的完整模5184终端证书和R=Z[1/65]单位提升完成全输入G=1判据，临界未解剩20、22。一般偶数终端覆盖、r=2及r=p-1仍开放，最终阈值未降低。核验ID even-middle-eighteen-congruence。

2026-09-14任意p的中间带统一结果：[全部奇余量核心](outputs/prime_arity/proofs/lower_band/prime_arity_uniform_odd_middle_cores.md)证明任意素数p>=5、奇数3<=r<p的合法(p,p,r)核心全部可达。两个始终存在的对合统一产生n倍双向二进根，主同余控制再使保载体收缩F1获得正向逆；小代表折返替代“2是原根”的特殊条件。接已有入口，所有2p<n<3p的素数维数及满足周期密度条件的奇合数维数得到完整G=1判据。七平均17、19元新增完成，尚缺18、20、22元。一般最终阈值未降低；完整平均词效率仍未控制。核验ID uniform-odd-middle-cores。

2026-09-14后续区间实际应用：[五平均十三元完整判据](outputs/prime_arity/examples/five_average_thirteen_congruence_complete.md)将已有(5,5,3)核的两个对合接入新的有限指数/强同余接口。倍率-12与换块给U(13/4)，再得双向13Z[1/2]根；三个幂零方向覆盖模13的全部主同余层，有限模平移及2的单位代表送到三步终端。由既有全输入入口，十三元G=1充要判据成立。五平均剩余12、14元；N(5)<=15未降低。本页为引用外部群论定理的存在证明，不提供高效任意输入完整平均词。核验ID five-thirteen-congruence。

2026-09-14文献接口补齐：[任意合数端点核心的同余闭合](outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md)引用Morris 2007定理6.1(2)和Serre的SL2(Z[1/2])强同余子群性质，证明二进U(A)、L(nA)恰生成Gamma1(n,A)。再用一个平衡小主元补齐整数Gamma0(n)，接已有正向控制器，得到任意奇元数p的合法2p+1双块核心全部可达。六素因子或Theta(n)<1入口范围因此升级为完整端点判据。任意多素因子入口和后续维数仍开放；证明不提供高效完整平均词求解器。内部有限商与单位分解已独立核验，外部定理不由样本验证。核验ID endpoint-congruence-completion。

2026-09-14局部算术分支已补齐：[全碰撞单位分支的统一补回](outputs/prime_arity/structure/prime_arity_complete_unit_collision_recovery.md)证明规定载体步骤后至多再作三次安全整数平均即可恢复相邻p重值对，完整核心前缀至多五步。小负逆元由载体预算统一处理；e=1、h>=4由一次重叠和模h^2-2的O(h)配比构造处理。另证明h(h-1)r<p时两个不交非恒等整数组根本不存在，983例以统一五步绕过。3305个计数系统、627个实际临界入口全部通过，此前十个入口已覆盖。这里完成局部补回，未证明多值输出递归闭合或降低阈值。ID complete-local-unit-recovery。

2026-09-14重数与精度的锐边界：[重数弱化的锐障碍与一位精度必要性](outputs/prime_arity/structure/prime_arity_sharp_repetition_and_precision_barriers.md)证明截断重数和S_p>=2p-1+h保证安全非恒等整数平均，并将安全整数停滞态压缩为一个大背景及至多p+h-1个例外。纯整数冻结的第二大重数至多p-2且可达等号；但(p,p-1)及S_p>=2p-1都被任意大维数的G=1停滞族反驳，其唯一非恒等整数输出G=n。n=5p-4的该族恰需一位额外精度，充分性引用现有大维数定理。另给安全三步分数前缀耗尽一位精度、同一输入却有两步整数造零的对照。132个停滞例、24个锐冻结例、161个保护选择及8组策略对照通过；没有降低阈值。ID sharp-multiplicity-precision。

2026-09-14任意h的新转移：[欧几里得见证转移与最大值下降](outputs/prime_arity/history/prime_arity_euclidean_witness_transfer.md)统一处理全部d>h，以及e=h-d>=2且2d eta>=e的临界入口，其中eta=-(s+1)^(-1) mod e。短正余数由一次模逆直接构造，两个真实不交组产生相邻整数重值。d>h输出还可消去全部旧A、B，再建立更低的重值对，使全局最大值严格下降。剩余通用菜单边界为d=h-1或3d<h且负逆元很小；这一版菜单曾留下10个入口，现已由统一补回续篇覆盖。4957个余数系统、2413个计数系统、474条不交组转移及248条实际输出续行通过；递归闭包和阈值仍未解决。ID euclidean-witness-transfer。

2026-09-14单位见证继续推进：[Hilbert基、精确容量与三原子补回](outputs/prime_arity/history/prime_arity_unit_witness_replenishment.md)完整参数化核心全碰撞分支hs<p，证明偏差(1,s+1,-s)的Hilbert基及两原子补回充要条件；容量不足只在h<sqrt(p/2)、1<=p-hs<2h-2。进一步以三原子公式补齐全部缺额1及(h,d)=(3,2)，从而覆盖所有h=2、3不足分支。另证明任意k、n>3k且k不整除n时，相邻重值对不能作为单步闭合不变量；实际29平均95元核心虽有该障碍，却有四步造零。241187个容量系统、1051条两原子补回、14个扩展或直接分支及49个统一障碍实例通过核验；未证明递归闭包或降低阈值。ID unit-witness-replenishment。

2026-09-14三条改进的后续：[来源关系、动态见证与整数返回阶段](outputs/prime_arity/structure/prime_arity_provenance_dynamic_and_integer_stages.md)证明指定核心出口后总有第二次安全整数续步或已造零；所有危险素数共用同一个支持，由gcd(3alpha-2,n)确定，保护预算至多一处。实际七步反例否定任意来源后继的整数闭包；固定A、C会排除分数阶段的共同因子约分，并在明确核心族上阻止本原平方能量与临界两两距离下降。奇素数同格整数返回至少五步，且有合法五步正对照。5926条后继续步及相关精确核验通过；未证明递归闭包或降低阈值。ID provenance-dynamic-integer-stages。

2026-09-14不变量改进：[能量唯一性范围与上半带整数出口](outputs/prime_arity/structure/prime_arity_invariant_improvements_and_core_exit.md)明确唯一性仅限共同单调固定正定二次型。证明任意合法整数(2p,p,r)核心都有一次安全非恒等整数平均保留两个不同p重值；碰撞会迫使n整除3j+1，故排除。核心原始同余保护只有3|r时的模3分支，r=1、2时每个原子都保留所有见证。下一步应使用后继关系pM=iA+jB+C，而非把四值后继视为任意状态。10800个类型选组、944条整数出口、180个非二次势核验通过；未证明递归闭包或降低阈值。ID `core-exit-potential-scope`。

2026-09-14已纳入可用的外部想法：[不同实际值数的整数归约](outputs/prime_arity/history/prime_arity_distinct_value_integer_reduction.md)证明任意k在n>2k时，D>=d+2k-1保证安全非恒等整数平均，并有限降到D<=d+2k-2。另[回看三平均合数与高斯周期路线](outputs/prime_arity/history/prime_arity_revisiting_ternary_factor_gaussian_route.md)核对旧素数归约及ell=1 mod3证明：一般p的高斯范数正向逆可推广，但3p<ell<4p没有ell=1 modp的素数位置数，旧范数一剪切恒等式也不能直接替换p。合数真因子在2p<n<4p时都小于2p，须另外证明小商可解。六条整数入口、六个全系数基的原位置周期及4503项容量核验通过。未降低阈值。ID `distinct-entry-gaussian-transfer`。

2026-09-12新的实质结果：[单值零和最优界与极端冻结态三步逃逸](outputs/prime_arity/history/prime_arity_sharp_concentration_and_escape.md)否定旧3p-2猜想，证明所有N>=2p-1的最优两桶界N-floor((p-1)/3)。引用Balandraud定理并核对勘误；达到最坏界的合法整数冻结族在全部素数p>=13（另含p11）都有三次真实平均造p个零的公式，首次造零步数最优。45408个零和自由序列、319015个余数配置及91条原位置路径核验通过。未新增全维数判据或降低N(p)。ID `sharp-monochromatic-escape`。


2026-09-12主余类储备推进：[主余类储备与刚性例外](outputs/prime_arity/history/prime_arity_dominant_residue_reservoir.md)把多余轻余数分支压缩为：主余类碰撞先锁定小整数提升；任意例外余数有合法配比；两个配比同时碰撞时提升满足唯一整数仿射关系；总超额达到p时有严格能量下降。367224个碰撞提升、37754个例外配比、13301个容量包装和834条原位置续步通过。多余类全局闭包仍未证明。核验ID `dominant-residue-reservoir`。

2026-09-12整数闭包新证明：[二类型碰撞的整数格结构](outputs/prime_arity/structure/prime_arity_binary_collision_lattice.md)用平面空三角形的指数1性质，证明临界p预算下二类型全碰撞参数必为整数，并给富余预算的总和界。对(a^(p+alpha),b^p,轻值)且一个低重模p余类、保护数h<=r的上半带状态，得到安全非恒等整数续步；只有一种实际轻值时h<=1，覆盖r=1。另通过G=1直接补齐三个重值在3p+1的一个额外位置分支。2133条单轻值、300条三重值、127条同余多实际值原位置续步通过；一般多余类闭包及N(p)<=3p仍未证明。核验ID `binary-collision-lattice`。

2026-09-12核心终止审计：[距离3p的真实缺口](outputs/prime_arity/history/prime_arity_three_p_remaining_gap.md)给出七平均22元(2^14,(-1)^7,-21)：所有十个非恒等三组不交核心返回均非法或增大本原能量，且无终端后继，但两次重叠整数平均即可造七个零。该逃逸推广到任意素数p>=5的(2^(2p),(-1)^p,-3p)族，首次造零恰需两步。另给所有r>=4的第二载体对合，明确终止步数必须随输入高度无界，以及p761/n3045未被旧4p-2+d不等式覆盖。未完成一般核心终止或降低N(p)。核验ID `upper-band-descent-boundary`。

2026-09-12上半带统一归约：[3p到4p的任意素因子数三值归约](outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_three_value_reduction.md)证明每个素数p>=5、每个3p<n<4p的全部合法输入，至多12+3ω(n)次原位置平均进入合法(2p,p,n-3p)二维核心。初等短区间筛选、双块集中见证和三行折叠消除r>=d及素因子数限制。核心G=gcd(y,n)，二次型判别式-8n(n-3p)；所有r>=4还有显式三步全局射影对合。385条归约路径、700条六原子标量周期及本原高度增长恒等式通过。不宣称核心终止、七平均22元已解或最终阈值降低。核验ID `upper-band-three-value-reduction`。

全局总览（2026-09-12）：[从二平均到任意平均元数：证明、自动G、非自动G边缘和临界猜想](outputs/general_arity/averaging_global_status_20260912.md)。统一区分固定维数完整判据、G自动成立的无条件维数、G真正筛选输入的H(q)，以及要求所有后续维数的最终阈值N(q)。当前已证非自动边缘为H(2)=5、H(3)=7、H(4)=7、H(5)=11、H(6)=10、H(7)=15、H(8)=13、H(10)=H(12)=17；九平均13、十四平均22、十五平均21等仍是候选。任意q的大维数定理为n>=4q-1+d_q(n)，精确临界线H(q)=C(q)仍为猜想。



2026-09-12十、十二平均17元完整解决：[十平均与十二平均的非自动G判据](outputs/general_arity/ten_twelve_average_seventeen_complete.md)证明两者均可达当且仅当G=1，因此H(10)=H(12)=17；16元的G自动满足不计入非自动边缘。两步进入(10,6,1)/(12,4,1)核，18陪集Gamma_0(17)分别由十平均的Delta(5)和十二平均的Delta(3)配合二进根覆盖。17个q<=200的旧B自动点也已独立列出。各自60个大整数入口和3条完整路径通过；不宣称N(10)=17或N(12)=17。核验ID `ten-twelve-seventeen-complete`。



2026-09-12入口继续缩小范围：[六素因子入口与覆盖系统边界](outputs/prime_arity/history/prime_arity_six_prime_endpoint_entry.md)证明任意至多六个不同素因子的2p+1输入可进入合法双p块。五个任意乘法阶坏类不能覆盖；真正合并时坏类只来自一个非全支持单点，至多d-1个，因此得到六素因子结论。原p217717/n435435的K4直接分组障碍可至多五次真实平均绕开并进入核心，未宣称该巨大level已完成归零。另给任意d下Theta(n)=sum 1/ord_ell(2)-min 1/ord_ell(2)<1的入口充分条件，六个坏类的模24覆盖说明继续外推需要不同见证选择。核验ID six-prime-endpoint-entry。核心群包含与中间带终止仍独立。



2026-09-12两方向新推进：[四素因子端点入口](outputs/prime_arity/history/prime_arity_four_prime_endpoint_entry.md)证明任意至多四种危险素数的2p+1输入都能有限步进入合法双p块。交换在各端点素数下统一产生2^k，每处只禁止一个指数类；3、5的奇偶筛选与剩余密度界保证指数存在。接原核心证书，195、231、255、315、399、435、455、1155八个端点新增全输入判据，p=97不再缺入口。另见[中间带周期密度归约与全部r的对合](outputs/prime_arity/history/prime_arity_band_period_and_involutions.md)：r>=d且局部交换阶倒数和<1时，所有2p+r输入可降到(p,p,r)，包括中间带所有素数维数；每个r还显式具有合法两步射影对合，四原子成非零标量周期。尚未证明任意level的核心群包含或一般三块核心终止。核验ID four-prime-entry-and-band。



2026-09-12合数端点统一推广：[CRT陪集证书与两素数入口](outputs/general_arity/composite_endpoint_crt_transfer.md)。十五元方法已编译为统一流程，36个列明模数的32112条回路全部通过独立精确核验；28个双素因子模数由一般三步入口得到全输入G=1充要判据，包括十七平均35元、十九平均39元、三十一平均63元、三十七平均75元及含重复素因子的135、147、175、207等。结合旧素数幂定理，全部奇整数3<=p<=109的2p+1端点均已覆盖。p97/n195等8个多素数模数的入口已由四素因子入口定理补齐，36个列明端点均已完成全输入判据。未证明任意合数的全称群包含，有限主元菜单全成功也不外推；最小非自动G边缘对合数平均元数仍须单独研究。ID `composite-endpoint-transfer`。



2026-09-12算法回归交付：[困难输入测试集](outputs/algorithms/averaging_algorithm_benchmark.md)保存584道去重题、19道精选题及2道历史束搜索深度24未出解的大整数题。其中196道七平均十五元冻结态已由新端点定理保证可达；108条参考原位置路径独立精确重放通过。p=19、37扩展题按有无直接证书标注，332道不设可达性真值。附1基索引验解器、新题生成器及旧预算记录；不重新搜索，不把路径未找到记为反例。核验ID averaging-algorithm-benchmark。



2026-09-12七平均十五元完整解决：[两素数入口与二进Gamma_0(15)](outputs/prime_arity/examples/seven_average_fifteen_complete.md)证明可达恰在G=1，故按非自动G标准H(7)=15。任意至多两种危险素数的端点输入可用至多三次平均进入合法双p重块；十五元CRT给24个陪集，全部72条回路用62个左上主元、8个右下主元及2次半整数剪切完成正向编译，完全使用已证二进根，不另搜索种子或激活11、17倍率。192个本原模行、72个强制三步入口与7条完整Fraction路径通过；最长样本7746步不代表最短界。平均元数7的候选端点15现已证，8的13也已证，下一个待攻的元数是9、候选13元。七平均更高维数17、18、19、20、22仍未解决，因此不宣称N(7)=15。核验ID `seven-average-fifteen-complete`。



2026-09-12非自动G条件的新完整结果：[六平均十元](outputs/general_arity/examples/six_average_ten_complete.md)证明可达恰在G=1或2，G=5或10由模5障碍排除，故按“G确实筛选输入”的标准H(6)=10。两步进入(6,3,1)核后，新增两步宏R满足R^4=-I/324、(AR)^2=I/36、(RAC)^2=I/216；正向逆与真实交换子给出L(-5/3)，进而实现Gamma_0(5)的全部18条回路。两类合法G各60个大整数入口、196种余数多重集和6条完整原位置路径（最长1931步）通过。后续研究以非自动算术边缘H为主，无条件网络作为辅助工具。六平均当前首个未解维数为11；不宣称最终阈值已确定。ID `six-average-ten-complete`。



2026-09-12历史反向诊断已更正：[整数冻结态与分数逃离](outputs/prime_arity/history/prime_arity_endpoint_counterexample_reverse.md)。高度5的35714个合法状态全部可达；其中7个无整数出边，87个首步值类型均无零触发，但七条完整分数路径均独立重放通过。旧“最低层重叠自动下降”说法已撤回：部分相交实际加深分母，成功路径通过不交分组留下单点。七平均十五元随后已完整证明，困难题现转作算法测试。ID endpoint-reverse-diagnostic。



2026-09-12合数临界线新结构：[局部平方根尺度与精确猜想](outputs/general_arity/composite_critical_scale_and_conjecture.md)。定义S(q)=max p^ceil(v_p(q)/2)。赋值间隙不变量证明q<n<q+S全部有G1反例；边界q+S除非只有q允许的素因子，否则也有反例。因此B(q)=q+S或q+S+1是已证下界，猜想M(q)=N(q)=B(q)，其中M排除n=q后表示最早成功，N要求之后所有维数成功。新固定四步族q=m(m-1),n=m²在m或m-1为素数时与下界吻合，严格给出M(12)=16、M(20)=25、M(30)=36、M(42)=49、M(56)=64等。另由(8,4,1)核、两个精确周期及模13全部42条回路证明M(8)=13。二平均的4与六平均的9属于G自动合法的固定网络点；5与10则是随后第一个非自动G维数，六平均10现已由独立模5控制器证明。核验ID `composite-critical-scale`、`eight-average-thirteen-complete`。



2026-09-12路线重评估：[任意 p 的结构、分段高度与文献](outputs/prime_arity/history/prime_arity_strategy_reassessment_20260912.md)。第二轮检索44个结构关键词、148篇去重题录并阅读4份全文后，最有希望的不是寻找新的固定二次能量，而是建立带局部同余、p进内容和块形状节点的 path-complete 离散高度；算术群的相对有界生成可作为已实现根之后的后处理。同步记录了多素数单位分离障碍和一般 r 合并恒等式。当前完整新族仍是 p=2^s-1 的 n=2p+2；全中间带开放。ID strategy-reassessment-20260912。



2026-09-12合数平均的统一突破：[任意元数的线性阈值](outputs/general_arity/arbitrary_arity_linear_threshold.md)把充分大维数定理推广到每个整数q>=3：n>=4q-1+d_q(n)时，完整判据为G的素因子均整除q，且整数零和输入只需一位额外q进精度。非单位差分delta用q/gcd(delta,q)份配比直接平均；偶数元数唯一中点碰撞由顺序结构或相反值终端解决。由此N(4)<=16、N(6)<=24，不再留下无限多未解维数。同时[四平均九元](outputs/general_arity/examples/four_average_nine_complete.md)用显式四步周期、二进根和模9全部36条Schreier回路完全解决，无种子搜索。结合半块转译，候选临界带内尚未证明G充分的仅四平均11、13、15元，六平均11、13、14、16、17、19、20、22、23元。新核验ID `arbitrary-arity-linear-threshold`、`four-average-nine-complete`；不宣称最短解或精确阈值。



同日更新：[四平均七元](outputs/general_arity/examples/four_average_seven_complete.md)通过 (4,2,1) 核和三个真实一步宏完成；实际周期为 C^3=I/8、(CA)^2=I/8，Sigma也由真实三步词实现。改用模7的0、±1、±2、±4代表，24条回路全部采用二进单位主元，无种子或平均词搜索。[六平均九元](outputs/general_arity/examples/six_average_nine_fixed_network.md)独立复核固定四步网络，并证明三步固定全输入网络不可能。入口 `four-average-seven-complete`、`six-average-nine-fixed-network`。两项结论只确定7和9这两个维数；最终阈值仍为 \(7\le N(4)\le16\)、\(9\le N(6)\le24\)，不能由端点成功直接取等号。



2026-09-12新完整中间维数族：[统一能量与 2p+2](outputs/prime_arity/structure/prime_arity_energy_and_dyadic_neighbour.md)。对每个 p=2^s-1、s>=2（允许奇合数平均元数），全部 n=2p+2 输入恰在本原中心化 G=1 时可达，特别新增七平均十六元。安全分块、CRT 单点等值化、真实两步上平移及除法返回使本原奇数方向高度 |v| 在完整阶段间严格下降，不依赖 2p+1 端点。一般 p 的双单点也能在至多 p+1 步归约到合法 (p,p,2) 二维核。另证明共同单调正定二次型只有平方能量，非整数交换的本原平方高度反而增加。31278 个方向、24 条核路径、48 条原输入 Fraction 路径等核验通过。ID carrier-energy-dyadic-neighbour。



2026-09-12合数平均新结果：[四平均、六平均与统一半块转译](outputs/general_arity/composite_arity_four_six_transfer.md)。对偶数q，原位置重叠块制造q/2的倍数份副本，再把所有允许的奇素因子吸收到副本数c中；剩余二平均商维数M=2或M>=4时，完整G判据成立。这覆盖任意偶数q的全部q倍数维数，并证明四平均全部偶数n>=8（另有n=4）、六平均全部3|n且n>=6。六平均九元有固定四步网络，其三进张量推广补齐纯三幂维数。四平均六元(-1^4,0,4)、六平均八元(-1^6,0,6)均为G=1的严格不可达例，由局部赋值与同余分支证明。533个标准基、35个副本宏、32415个陷阱后继及336条完整路径精确通过。核验ID `composite-four-six-transfer`；未证明四平均全部奇数维数、六平均3不整除的维数或最终阈值。



2026-09-12中间带接口已修订：[相对尺度与单点—块交换](outputs/prime_arity/structure/prime_arity_middle_band_relative_scale.md)。该交换自动保持全部非 p 同余见证，模 p 匹配只为整数中间值所需；允许分数后必须另证终止。(p,p,1^r) 的均值格商阶为 2p+r，只有实际等值化成 (p,p,r) 才能除去 gcd(p,r)。旧的“同时匹配与动态保护均未解决”表述不再适用于这个交换子类。



2026-09-12临界端点的深层结构：[素数幂端点与临界几何](outputs/prime_arity/tools/prime_power_endpoint_and_critical_geometry.md)。对任意奇p，q=2p+1为素数幂时，两张局部射影坐标图的全部Schreier回路均可由已证正向控制器编译，得到射影Gamma_0(q)包含；配合两步合法入口和Bezout输送，完整解决所有素数幂端点，特别是十三平均二十七元与形式上的1093平均2187元。临界能量是判别式-q虚二次阶的范数，产生权一theta级数；但level27、weight1的LMFDB空间全为Eisenstein，模形式解释计数而不直接提供原位置路径。相邻2p+2的真正障碍是局部逆只给共同收缩lambda，外部单点固定后变成diag(lambda,lambda,1)，不再是全局射影单位。独立核验15612条回路、55512个模行、168条编译回路、32个入口及2754个范数恒等式。ID `prime-power-endpoint-completion`。



2026-09-12临界前沿交接：[当前方法的障碍与2p+1结构](outputs/prime_arity/history/prime_arity_critical_frontier_handoff.md)。区分一步双重值闭包、固定保护、有限短词表、直接多素数分块和余维一黑箱调用的已证障碍，明确这些是特定方法边界而非总猜想的反例。建议将碰撞总和保留为上界支线，优先研究素数幂端点的真实正向轨道和2p+2双单点的部分控制。新增完整证明：q=2p+1为素数幂时，任意G=1输入都能两步进入合法K_p；p本身为奇素数且q合数时，q必为3的幂。入口不解决核内轨道，未新增完整端点或降低阈值。独立原位置核验ID：prime-power-endpoint-entry。



2026-09-12任意p的统一碰撞结构：[两组相加、总和窗口与高重数分类](outputs/prime_arity/structure/prime_arity_uniform_collision_structure.md)。在保护后3p+1层，任一低重数余类达到p-2重即可统一闭合：全碰撞只允许D=3p或3p-1，再由私人见证／全局零和排除。分数坐标族有显式除数参数，包含所有p=2 mod3的一族，不需逐p求表。另由Dias da Silva--Hamidoune受限和集定理处理至少sigma(p)=min_k(2k+ceil((p-1)/k))种余数；零和因子分解给两个明确的总余数窗口。二平均最近对也推广为安全连续p块的新生重值引理，但一般保护容量仍在。核对51618个高重数符号模式、779个原位置合法步骤、4824个零和分解、105760个窗口公式及144个受限和集构造。剩余是中等重数余类交互；未降低一般4p级完整阈值。ID `uniform-collision-structure`。



2026-09-12七平均推进到3p+2：[对称碰撞总和证书](outputs/prime_arity/examples/seven_average_three_p_plus_two_threshold.md)完整解决七平均23、24、25、26元，接已有>=27，得到15<=N(7)<=23；21元另已解，22元仍开放。一般有效的余数类对称压缩只保留总和，57026个完整模7模式仅有11个相容解，再接最小保护总和矛盾；新增四维数均只需一位额外精度。另见[可交换保护与统一初始化](outputs/prime_arity/history/prime_arity_protected_exchange_and_mass.md)：初始化降至n>=3p+d-2，p=23,n=70反例说明不能固定任意极小保护集；交换后产生一整个p=2 mod3的3p+1元五步整数族。任意p的3p级阈值仍未证明，p=11总和数据仅为探索。ID `seven-average-three-p-plus-two`、`minimal-protection-and-exchange`。



2026-09-12五平均达到3p：[最小同余见证与碰撞总和证书](outputs/prime_arity/examples/five_average_three_p_threshold.md)。完整解决五平均n=16、17、18；结合已证n=15及全部n>=19，得到11<=N(5)<=15=3p。低总重数不同余双重值的全部碰撞对应903个模5模式的有理线性系统，只有22个相容解，且总和的局部分母可控；最小保护横截集的私人见证与全局零和排除所有合法例外。新增三维数都保持一位额外精度；本证明是完整有限符号证书辅助，不是平均词搜索或有限输入外推。五平均尚未解决12、13、14；任意p的3p级阈值仍开放。新的通用方向是证明碰撞关联方程的总和证书，无需逐个确定所有坐标。ID `five-average-three-p-threshold`。



2026-09-12直接面向3p：[长零和自由序列与双锚点接口](outputs/prime_arity/history/prime_arity_three_p_additive_interface.md)。引用Savchev--Chen长序列结构，重复锚点将其单位缩放锁为1，证明n>=3p+d时低总重数不同余双重值必有安全非恒等整数候选，保留一个旧p重块；较长序列零和自由时用一／两个低重数位置进一步修复碰撞，完整保持双重值。剩余是候选存在但实际和全部碰撞的恢复／造零，尚未证明3p统一上界。新核验器精确计算模p子序列和的实际最小／最大值，避免过早截断安全池；4246个样本未留全碰撞不承担无限结论。与2024年同余拟阵基／群标签基理论的具体对应和适用边界已记录。ID `three-p-two-anchor-interface`。



2026-09-12阈值实际下降：[逆EGZ的4p-2+d定理](outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_inverse_egz_threshold.md)。对奇素数p>=5，完整判据已在n>=4p-2+d_p(n)成立，故N(p)<=4p+ceil(log_2 p)，特别N(5)<=19、N(7)<=27。三重值的单份／双份中间值修复把该分支降到3p+2；两个不同余重值总重数>=3p-2时有共同预留跨越。保护后2p-2池若无整数p子集，逆EGZ强迫两个p-1余数类，再借一份／两份锚点修复碰撞。全部整数能量闭包保持，一位额外精度仍成立。约7p/2+d路线已有明确容量，但低重数池的统一碰撞恢复尚未证明，不列为新上界。ID `inverse-egz-threshold`。



2026-09-12逆零和工具已转译：[碰撞修复与2p+4七步族](outputs/general_arity/inverse_zero_sum_averaging_progress.md)。2022逆加权零和定理给出O(p)模运算的真实副本选择；两次相反碰撞在不交副本和保留见证下恢复双重值。五平均十四元的(5,5,2,2)核在两个锚点模5不同、低重数两值模5不同或有锚点同余时，已有完整安全整数闭包；余数集中情形确实可能每步失去不变量。另有任意奇数p>=5的2p+4元二参数族，两次平均造零、总计至多七步；其中(6^p,8^p,[p(18-p)]^2,[p(p-25)]^2)对所有奇素数合法且没有非恒等整数一步双重值闭包。没有新增完整维数或降低统一阈值。ID `inverse-zero-sum-transfer`。



2026-09-12外部文献检索：[2018--2026年的二平均后续与可借用工具](outputs/literature/averaging_literature_survey_2018_2026.md)。核对原论文2019会议／2020期刊版本、作者2019博士论文、2020 RPRIS、2019 Clique Gossiping、2021--2022块Kaczmarz、2022逆加权零和和EGZ近线性算法，以及2024 splitter和2025--2026相关题录。本轮未找到一般p平均完整判据或最优阈值的已核验外部证明。已读逆零和全文给出一个可由两份副本实现的整数平均候选引理，但安全性与碰撞仍需另证。没有更改正式求解算法或新增完整维数；综述明确标注全文与摘要的证据边界。



2026-09-12维数传播与统一终端：[造零收尾、余维一障碍和加权均值格](outputs/prime_arity/tools/prime_arity_interpolation_and_lattice_structure.md)。对所有奇素数p及n>=2p+1，一旦真实p平均产生p个零，就能完整归零。下半区间只需已证的2p+1含零尾部，无需端点完整猜想；上半区间用3p、4p和大维数定理按支持数传播。另证n非p幂时整块等化n-1个位置必归零或陷入G=n障碍，因此不能用相邻已解维数黑箱直接内插。块重数除公因子后的总和s给出Z^k/(零和格+常值方向)=Z/s，统一解释端点的Gamma_0(2p+1)和三块的Gamma_0(3)。未证明任意合法输入必能先造零，未新增完整中间维数。ID `prime-arity-zero-trigger-bridge`。



2026-09-12中间维数推进：[三块运输与3p完整定理](outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md)。对每个奇素数p，n=3p的完整p幂G判据已证；p>=5时写p=3m+epsilon，两张明确非负运输表mJ+epsilon(I+-D)在原3p位置实现U(+-1)，块重标记再给L(3)，同一个四陪集Gamma_0(3)及模3分组修复完成全部输入。无种子或平均词搜索，旧3p一步闭包反例族也全部解决。另证n>=3p+d时两个模p同余重值的安全整数闭包。五平均新增n=15，尚待覆盖12、13、14、16、17、18、19；统一N(p)上界不变。ID `prime-arity-middle-band`。



2026-09-12统一正向控制器：[无需搜索的临界种子证明](outputs/prime_arity/tools/uniform_endpoint_positive_controller.md)。对每个奇数平均元数 p>=3，在原 q=2p+1 个位置上的两种两步返回、互补仿射倍率和必碰偶数的整数递推，统一给出可逆倍率2、U(1)、L(q)。欧拉同余随后为全部安全的 j<=p 构造正向逆，得到 R_q=Z[1/l:l<=p且l不整除q] 上的完整上根、q倍下根及对角单位。q为素数时，完整Schreier与入口证明遂解决全部输入，统一(3,7)、(5,11)、(11,23)、(23,47)等，无平均词搜索。q为合数时种子已解决，但合数level轨道与任意输入安全入口仍未闭合，七平均十五元仍不宣称全解。ID `uniform-endpoint-controller`。



2026-09-12七元精确端点结构：[为什么阈值是七](outputs/prime_arity/examples/seven_exact_threshold_structure.md)。双三重块与全系统载体的六次交换给出 -1/27 的正向标量周期；三个明确跨块返回满足三条短周期，生成 Z[1/6] 上的上根、7倍下根及对角单位，八陪集与六个 Schreier 回路遂给出完整 Γ₀(7)。这是不依赖旧十八词下降覆盖的另一份七元充分性证明。一般p双块扫掠的判别式为p(p-4)，解释p=3的有限周期与p>=5的双曲分界；精确端点不必通过不断压低大维数常数获得。ID `seven-endpoint-structure`。



2026-09-12上界降至4p级：[三个重值的顺序结构与3p边界](outputs/prime_arity/history/prime_arity_four_p_threshold.md)。对奇素数平均元数p，n>=d_p(n)+4p-1 已足够，故 N(p)<=4p+ceil(log_2 p)+1。三个重值用实际极值和单份参与直接处理，只对两个重值预留2p位置，再调用保护后的EGZ。因此五平均全部 n>=20 已解，结合 n=11，尚待覆盖 n=12,...,19。另有任意p>=5的合法3p元族，所有非恒等整数平均都会只剩一个p重值且不造零；这只否定未经补充的双重值一步闭包，不证明3p不可达。ID `prime-arity-four-p-threshold`。



2026-09-12五平均十一元已证：[完整证明](outputs/prime_arity/examples/five_average_eleven_complete.md)。五个两步原位置返回和三条短标量周期提供全部正向逆；在 (a,a-b) 坐标中生成 Z[1/30] 上完整上根、11倍下根和对角单位。有符号十二陪集与十个明确 Schreier 回路证明包含 Γ₀(11)，Bezout 输送和四步终端解决全部合法输入。因此五平均 n=11 的充要判据是 G=1，不再只是有限样本结果。全程只用五平均，未调用三平均或子维数求解器。n=12,...,24 尚未由此解决，N(5)=11 仍未证明；不承诺一位额外精度或最短构造。ID `five-average-eleven-complete`。



2026-09-12边界推进：[预留重数与临界结构](outputs/prime_arity/history/prime_arity_boundary_progress.md)将素数元平均的充分界改进为 n>=d_p(n)+5p-1，特别 N(p)<=5p+ceil(log_2 p)+1<=6p，且 11<=N(5)<=25。n=2p+1 中含零状态统一至多五步收尾，Y_p=(1^p,2^p,-3p) 恰好四步可解。若2p+1为素数，全输入两步可进入合法K_p；若含六个不同素因子，K4/CRT构造会阻塞每个直接(p,p,1)划分。p>=5的两个自然核返回保留避零实区间，必须加入跨块操作；第一未解实例是五平均十一元的全参数核终止。ID `prime-arity-boundary-progress`。



2026-09-12阈值细化：[素数元平均的线性阈值与 2p 边界](outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_linear_threshold.md)。EGZ 保护池、四重值的极端锚点及系数跨越打包，将 n>=2p^3 改进为 n>=d_p(n)+8p-7，特别是 n>=9p-5。对奇素数 p，(-p,0^(p-1),1^p) 在 n=2p 处不可达，故 2p+1<=N(p)<=9p-5。N(2)=4、N(3)=7；p>=5 的 N(p)=2p+1 仍为猜想。n=2p+1 的 (1^p,2^p,-3p) 还明确否定无例外的双 p 重值一步闭包，不能只靠调小常数声称最优界。ID `prime-arity-linear-threshold`。



2026-09-12素数平均元数推广：[素数元平均的充分大维数定理](outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_averaging_large_dimension.md)。这里 p 是一次平均的位置数，n 是任意总维数。对每个素数 p、n>=2p^3，完整可达判据为本原中心化 G 是 p 幂；整数零和合法输入只需分母 p。证明通过双 p 重值、保护池和一次模逆调节，把不能继续的状态限制为可直接消去的短等差数列，不调用三平均定理或任何子维数。阈值只求充分，不声称最优；合数平均元数尚未由此证明。ID `prime-arity-large-dimension`。



本目录保留全部研究过程，同时提供一层稳定的接手入口。2026-09-11：[双三重值不变量](outputs/triple_average/proofs/triple_average_prime_double_triple_invariant.md)给出全部素数 p>=11 的统一原位置证明，结合既有七元证明和合数归约，闭合原判据：对任意 n>=7，中心化、本原化后的非零状态恰在 G 为三幂时可达；全零状态单独显然可达。



新证明先研究 3X，至多两次整数三平均建立“至少两个不同三重值”，再按模3余类与重数选择真实原子，保持模p不全同余，直至 (a^3,(-a)^3,0^(p-6)) 终端。固定整数格上的平方能量给出有限终止，因此 p>=11 的整数零和合法输入只需一位额外三进精度。全称结论由正文证明，程序只做有限独立重放；未证明位长多项式构造长度或七元／任意合数的一位精度界。核验ID `prime-double-triple-invariant`。



本轮的原文阅读、外部文献及研究复盘见[重读二平均与统一证明](outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)。旧控制器仍保留为历史证书库；下文“最小未解”等表述描述各自的历史阶段，不代表当前状态。



此前结论：[Hecke与模符号路线的最后检验](outputs/triple_average/history/triple_average_final_hecke_audit.md)。该阶段没有得到任意p证明，暂停直接模形式方案。标准矩阵对任意奇p都有整数幺模共轭，旧指数p换基不是内在level；有根的第二算子与标准生成元没有共同正定Hecke星结构；整个下三角族不能从u非零到u=0；直接线性普通Manin编码被中心负号排除。此前将局部投影称为全局Eisenstein／Steinberg分量、将数字算子称为已实现T_3、将删点置换放入PGL2自然位置表示的说法已撤回。[修订接口页](outputs/triple_average/history/triple_average_iwahori_hecke_modular_interface.md)保留正确恒等式及历史实验，原稿已存档。ID `final-hecke-manin-audit`；旧核验ID仅证明有限代数恒等式。该阶段最小未解为71，现由上述直接证明覆盖。



此前路线复盘：[停止局部拼接，返回二维除法结构](outputs/triple_average/history/triple_average_route_reassessment_2026-09-11.md)。它记录载体路线的局部成果与全局困难；其中后来提出的直接Hecke／Manin主线现由上面的最后检验取代。弱的输入相关终端覆盖仍开放，但尚无分支提升定理或全局下降量。仿射交换子理想、参数周期刚性、混合迹零条件归约继续保留各自已经证明的范围。



结构结果：[载体扫掠催化器](outputs/triple_average/history/triple_average_carrier_sweep_catalyst.md)。r个三重块与一个载体各交换一次，始终得到1/3乘整数幺模矩阵；r=2恰恢复七元Artin中心，r=3则在固定十位置窗口中产生24个正向幺幂，其中12个具有同长度正向逆。四个固定共轭根显式给出E12(36)、E13(96)、E21(720)、E31(2160)，进而包含E3(4320^2 Z)，所以局部群的算术有限指数已经证明。更进一步，根约化与至多三次扫掠的精确有理锥证书证明：任意三个三重块加一个载体都能在这十个原位置内有限步产生叶／载体或叶／叶碰撞，不要求局部G条件，也不依赖p。固定窗口的外部耦合是以局部均值为中心后消失的1-coboundary。其全局拼接边界和路线降级见上面的最新复盘。ID `carrier-sweep-catalyst`、`carrier-catalyst-local-descent`。



最新终端化简：[等载体形式冻结定理](outputs/triple_average/history/triple_average_equal_carrier_formal_freezing.md)。在D_r=(u_1^3,...,u_r^3,a^2)中，形式交换群显式包含左上SL_(r-1)(Z)；任意合法素数核先以SL把叶差化成单gcd坐标，做一次真实等载体交换后，新叶差gcd自动整除新基值，再用第二个SL便产生零叶块。有限域中唯一避开零叶超平面的轨道是q|3r+2时的常值直线，素数维数下它恰为非法方向。因此形式轨道终端已闭合。正文同时证明正向局部化锥障碍：任何不依赖未参与叶的正向输出行只能有非负叶系数，故不能直接实现平衡SL剪切。剩余目标必须使用全局边界的状态相关抵消，或直接命中零叶。ID `equal-carrier-formal-freezing`。



最新完整结果：[59元判据与结构总结](outputs/triple_average/arithmetic_cases/triple_average_fifty_nine_arithmetic_complete.md)。一次额外原子库给出正向种子，33节点无环逆证书经仿射消元产生上下三进根，21个Schreier回路实现共轭Gamma_0(59)，独立折叠60陪集并接九元终端。59已加入因子闭包，最小未解维数更新为71。入口 `python work/run_verifications.py --id n59-complete`。此后主线停止逐素数推进，转向统一的非分裂素数种子定理。



17至59证书中可预测与不可预测的部分见[非分裂素数结构综合](outputs/triple_average/history/triple_average_nonsplit_prime_structure_synthesis.md)。根提取、尖点、Schreier消元与终端已有统一公式；未统一的是原位置返回半群中正向可逆种子的存在。下一阶段优先研究PGL2(F_p)非分裂三阶轨道的p+1到p位置商实现，避免继续逐素数搜索。



备选条件归约：[混合单点迹零返回控制器](outputs/triple_average/history/triple_average_mixed_singleton_controller.md)。令B为不超过(p-1)/2且不等于3、5的素数乘积，两个显式返回R_0与R_(1/(10B))一旦能在原p个位置实现，其周期、仿射交换子和显式Bezout恒等式便统一产生U(R)、L(pR)；固定因子15补齐3、5，对角吸收随后覆盖全部合法方向并接九元终端。两个目标已有共同严格正三进运输和副本实现。这条特定充分路线内部只差两运输的原位置分解；该条件不等价于一般种子存在，也不排除条件宏、奇异降秩或直接终端命中的其他证明路径。ID `mixed-singleton-conditional-controller`。



原位置分解的精确半群方程、两个返回的相对混合器、现有返回库二因子边界、非分裂平移闭路边界及叶数字控制器边界见[原位置分解前沿](outputs/triple_average/history/triple_average_original_position_factorization_frontier.md)。这些有限阴性结果用于收缩统一语法，不构成不可达性证明。



最新：[53元完整判据](outputs/triple_average/arithmetic_cases/triple_average_fifty_three_arithmetic_complete.md)已登记n53-complete并加入已解因子目录。74节点正向逆证书、三进根和20个Schreier回路消元给出共轭Gamma_0(53)，独立折叠54陪集并重放九元终端。最小未解维数更新为59；下文更早的未解起点属于历史状态。全部素数统一证明仍开放。



最新结构：[Reynolds半群、交叉计数与判别式对偶](outputs/triple_average/history/triple_average_reynolds_hecke_hodge.md)。原子生成代数对全部n>=5已是整个End(V)，因此线性化不能区分五元失败；固定1／3重数的整数运输表则精确参数化普遍可执行层，自动关于加权伴随封闭，并有有限Hecke角解释。能量Hodge对偶在危险p处交换Iwahori边两侧，把合法方向送进非法余类，解释自然伴随取逆的障碍。已给出无隐藏宏适用条件的运输半群终端猜想，未新增已解维数。ID `reynolds-hodge-structure`、`contingency-layer-semigroup`。



当前素数路线总览：[证明路径与剩余猜想](outputs/triple_average/history/triple_average_prime_proof_roadmap.md)。按已解无限族、统一标准核入口、正向种子、同余生成与终端分层，分别列出强资源猜想、有限Schreier目标及更弱的合法单轨道目标，避免把充分条件当成必要条件。该页主体写于47元完成后；后续53、59已经补齐，当前最小未解为71。



最新完整结果：[47元判据](outputs/triple_average/arithmetic_cases/triple_average_forty_seven_arithmetic_complete.md)。一个固定宽度一尖点词与两个伸缩校正给出E12(Z[1/6])及E21(47Z[1/6])；18个完整Schreier生成元逐个正向消元，实现共轭Gamma_0(47)，独立折叠为48陪集。统一桥与Bezout输送完成全部47元输入。47已进入因子闭包，最小未解维数现在为53。入口 `python work/run_verifications.py --id n47-complete`。



最新一般定理：[局部化Iwahori生成与通用尖点公式](outputs/triple_average/history/triple_average_localized_iwahori_generation.md)。对任意素数p，若正向群提供Z[1/(p-1)!]上的上根、p倍下根及相应对角单位，则统一标准代表和三因子消元证明包含Gamma_0(p)。另有任意奇次三进返回产生宽度一尖点的恒等式。剩余统一任务是这些资源的原维数物理实现，非再次逐素数猜同余群。



此前：[正向根群饱和与统一素数策略](outputs/triple_average/history/triple_average_positive_root_saturation.md)。一般迹根引理将逆元构造化为一个线性有理方程；固定三层证书已让旧167个B47宏全部获得正向逆，连同新增对合共170个。原Q(sqrt89)共轭目标已有57次模板的正向实现；整数换基后正向群包含E12(47Z[1/6])、E21(47Z[1/6])两整族。该阶段未完成的同余包含已由上面的n47-complete补齐。独立入口 `python work/run_verifications.py --id b47-root-activation`，不运行发现搜索。



该页同时给出统一素数猜想的准确形式：正向群包含共轭Gamma_0(p)即足够，由同一个Bezout公式收尾。全部p=1 mod3素数与合数归约已经统一；剩余难点是p=2 mod3的普遍正向生成，不是逐素数重做终端分类。



此前47元进展：[额外原子平均、正向对合与平移根群](outputs/triple_average/history/triple_average_b47_extra_atom_and_adjoint.md)。一次额外预备三平均产生三个新对合，并使标准A0等六个旧宏获得正向逆；固定词进一步生成全部U(47t)、t属于Z[1/6]，为后来n47-complete提供种子。入口 `python work/run_verifications.py --id b47-extra-atom-involutions`。



同页给出倒序平均的能量伴随接口：旧167库只有15个反向模板通过全参数适用域，均未新增宏。一般同型对合的两两乘积还落在同一分裂环面，不能仅靠该族对合推断模群有限指数。



最新统一工具：[全局谱平衡与周期判据](outputs/triple_average/history/triple_average_projective_spectral_balance.md)。Newton多边形与Kronecker定理将任意秩有理宏的有限射影阶，等价为半单性、实谱等模及一组特征系数整数性；Ad表示给出给定矩阵的多项式时间分圆验证算法。它不解决宏词的存在性，最小未解仍为47。



[47元当前库周期边界](outputs/triple_average/history/triple_average_b47_cycle_frontier.md)精确排除167模板中长度至多4的有限周期，以及全部j>=0的A0^jBC。四因子部分用整数模筛选，737665600组合仅3896个需要完整整数复核。该排除不延伸到更长词或其他宏库。



最新一般结构：[等值载体与二进重分组](outputs/triple_average/history/triple_average_paired_carrier_reset.md)。全部n=3r+2、奇数r>=5的合法状态可进入二重等值载体核；一个4r-3步的原维数宏给出W=2V、V属于GL_r(Z[1/3])，坐标和差分理想都恰乘2。单独载体交换的标量周期被奇偶不变量排除，新宏的全局周期仍未证明。入口 `python work/run_verifications.py --id paired-carrier-two-adic-reset`，最小未解维数仍是47。



最新：[四十一元完整判据](outputs/triple_average/arithmetic_cases/triple_average_forty_one_arithmetic_complete.md)。21个通用宏、10个正向三因子对合和10个整数词给出完整42陪集的共轭Gamma_0(41)，唯一合法尖点归零。41已加入因子闭包，最小未解维数现在为47。入口为 `python work/run_verifications.py --id n41-complete`。



[有限模调度的高度边界](outputs/triple_average/history/triple_average_modular_height_barrier.md)给出一个统一精确族：全部指定非三剩余类和G保持不变、实能量下降，但本原整数高度按3^(2h)增长。它不否定已证的模调度桥，说明终止还需完整操作词的实／三进联合控制。



统一接口：[有限模正向控制与二例外归约](outputs/triple_average/history/triple_average_two_carrier_modular_bridge.md)。对全部n>=17且n=5 mod6，包括合数，直接用混合好划分、双载体有限模调度及合法n-2元调用进入(u^(n-2),a,b)核；不需安全能量下降或因子归纳。形式逆只在有限模数上正向化，不能据此声称核必终止。入口为 `python work/run_verifications.py --id two-carrier-modular-bridge`。



再用一步真实三平均可安全进入标准B_n，故这个n族的多危险素数标准核接口也已闭合。其一般原则是：全域可执行且行列式为三进单位的正向宏，与形式群在所有非三有限商上轨道相同；精确归零仍需另证。



此前：[二十九元完整判据](outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)。18个通用宏、9个三因子正向周期和7个整数词给出共轭Gamma_0(29)的完整30陪集证书，唯一合法尖点可归零。29已进入因子闭包。入口为 `python work/run_verifications.py --id n29-complete`，不运行浮点发现搜索。



无限族：[全部p=1 mod3素数的完整判据](outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md)。原p个位置上的高斯周期层提供全局正向标量循环；一个范数一分圆单位保证单位剪切，再由整数仿射格正规形完整归零。所有这类素数及其因子闭包已解决，包含31、37、43、61、97等。结合29、41元证书，剩余统一问题归约到p=2 mod3、从47开始的素数。核验入口 `python work/run_verifications.py --id split-prime-gaussian-controller`。



此前原维数进展：[平坦核形式群的统一算术性](outputs/triple_average/history/triple_average_flat_star_arithmeticity.md)。所有p>=13的素数核可进入同一个一／二载体框架；显式幺幂与高秩初等同余群定理证明其形式群整数部分有限指数。模2和模p的第一层联合像及终端代表也已统一。该一般框架的整体正向实现仍开放；29元后来由独立三因子周期证书解决。



[置换剩余像与局部耦合](outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md)证明：九十一元旧21504容器严格大于特定宏群，新的必要容器指数为43008。对应紧模曲线有无分歧二重覆盖和Jacobian二阶线丛解释。旧容器及其有限搜索标签完整保留。



最新结构定理：[数字算子的完整同余群](outputs/triple_average/history/triple_average_digit_congruence_group.md)。平衡剪切与置换恰生成全部整数保和／保常值群；加入数字算子后，群恰为模n倍率属于3的循环子群的同余群，并有显式分裂扩张和全部有理射影轨道分类。所有合法方向只有一个轨道，但正向实现仍使用三份复制。入口为 `python work/run_verifications.py --id balanced-digit-congruence-group`。



此前结果：[一次三份复制稳定化](outputs/triple_average/history/triple_average_one_tripling_stabilization.md)。所有 $N\ge9$ 且 $3\mid N$ 的维数已无条件解决，包括含当前未解素数47的141元；任意合法有理输入只需复制三份即可归零。证明把离散梯度／Hilbert 90、真实副本剪切与整数仿射格轨道分类接起来。原维数复制消去仍开放。入口为 `python work/run_verifications.py --id one-tripling-stabilization`。



其他AI结构图景的最新复核见[局部到整体与数域边界](outputs/triple_average/history/triple_average_structural_picture_audit.md)：保留原稿，纠正合法域不能单独决定高次level、数域扩张不改变固定输入可达性、内容理想不能替代R加法模等问题。



该复核第11节记录29元原1195模板的周期边界：没有二因子有限周期，且所有指数j>=0的A^jB均被排除。新完整证书使用三个不同因子，因而不与旧边界冲突。



一般结果：[任意维数严格归约到素数](outputs/triple_average/proofs/triple_average_all_dimensions_to_primes.md)。全部合数的接口已闭合，原猜想等价于仅证明全部素数p>=7。当前结合分裂素数族与29、41元基例，已解所有n>=7且素因子属于2、5、11、17、23、29、41或p=1 mod3的维数，并另有全部三整除维数。入口为 `python work/run_verifications.py --id even-prime-power-halving --id all-dimensions-prime-reduction`。



最新一般突破：[奇数合数的乘法闭包](outputs/triple_average/history/triple_average_odd_composite_factor_closure.md)与[25元完整判据](outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)结合后，全部奇数n>=7已严格归约到全部p>=7素数。当前已解P={7,11,13,17,19,23}的任意乘积和素数幂，再乘任意三幂、五幂都已解决，包括25、35、49、77、91、121、125等无限族。入口为 `python work/run_verifications.py --id n25-complete --id odd-composite-factor-closure`。



此前该证明先覆盖8整除维数；最新的低二进重数桥已将v2=1、2也接入因子归约，所以现在允许任意二幂因子。



此前[二例外因子桥](outputs/triple_average/history/triple_average_prime_first_factor_reduction.md)的最优准备步数结论仍保留，构造已推广到d+2例外核心。剩余统一任务是素数核的正向可达性。



现代框架的主线复核与可执行定义见 [Modern Frame 严格化契约](outputs/triple_average/history/triple_average_modern_framework_review_and_contract.md)；奇素数维数的策略限制见 [子问题调用下界](outputs/triple_average/history/triple_average_subproblem_prime_obstruction.md)。



项目背后的统一结构猜测见[局部算术轨道图景](outputs/triple_average/history/triple_average_structural_picture_conjecture.md)：它区分已证的同余子群样本、因子归约的组合接口，以及尚待证明的正向算术轨道与终端覆盖。



此前基例：[二十三元完整判据](outputs/triple_average/arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md)。三个固定原子宏生成共轭 Gamma_0(23) 的指数24充分子群。入口为 `python work/run_verifications.py --id n23-complete`；原固定词证书保持可复现。



同轮完成：[十九元及其三进塔](outputs/triple_average/arithmetic_cases/triple_average_nineteen_arithmetic_complete.md)，通过通用十五元调用生成指数20充分子群。其内部子问题路径允许依赖参数，与二十三元的固定原子词证书不同。



[素数维数与同余子群的准确关系](outputs/triple_average/history/triple_average_prime_congruence_structure.md)给出一般p进稳定子定理和真实循环的尺度约束，不能据已解例子断言所有素数都自动生成足够大的群。整系数宏编译器在搜索前加入重数与支撑格缓存，并与旧版95个十七元矩阵逐项对照。



此前完成：[十七元及其三进塔](outputs/triple_average/arithmetic_cases/triple_average_seventeen_arithmetic_complete.md)。固定原子逆词给出共轭 Gamma_0(17) 的指数18充分子群，独立入口为 `python work/run_verifications.py --id n17-complete`。



发现方法见[参数无关子问题模判据与范数环面](outputs/triple_average/history/triple_average_universal_subproblem_lattice.md)：任意参数维数的模板合法性可用局部化整数模包含判定。该页保留旧库与局部调度阶段，当前完成状态以上面的十七元定理为准。



此前的一般族：[全部二三光滑维数的完整判据](outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md)，涵盖所有 n=2^a·3^b≥7。独立入口为 `python work/run_verifications.py --id two-three-smooth-complete`。



此前完成：[十四元及其三进塔](outputs/triple_average/arithmetic_cases/triple_average_fourteen_complete.md)。[图论核心定理](outputs/triple_average/history/triple_average_blocker_graph_core.md) 同时将一般安全终端的重复值下界提高为 n-d-2。核验入口为 `python work/run_verifications.py --id blocker-graph-safe-core --id n14-complete`。



此前完成：[十五元及其三进塔的完整判据](outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md)，通过模8调度调用十二元和十元子问题。[偶维 B 核减半桥](outputs/triple_average/history/triple_average_even_kernel_halving_bridge.md) 仅提供核内接口，十四元高维部分由最新证明补齐。入口为 `python work/run_verifications.py --id n15-via-subblocks-complete`。



此前完成：[十二元及其三进塔的完整判据](outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md)。真实正向宏含共轭于 Gamma_0(8) 的指数 12 子群，唯一合法尖点可终止。独立核验入口为 `python work/run_verifications.py --id n12-complete`。



进一步完成：[十八元及其三进塔](outputs/triple_average/arithmetic_cases/triple_average_eighteen_via_twelve_complete.md)，通过可解十二元子块和重数配对归零。B21 搜索已改用[整数状态引擎](outputs/triple_average/history/triple_average_b21_integer_search_optimization.md)，同样八进程约 11 秒完成。



## 从哪里开始



1. 先读[统一素数证明](outputs/triple_average/proofs/triple_average_prime_double_triple_invariant.md)及[本轮复盘](outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)，再按需要查阅 [`outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md`](outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md)中的历史结构。

2. 再读 [`outputs/triple_average/history/triple_average_research_corrections.md`](outputs/triple_average/history/triple_average_research_corrections.md)，避免继续使用已经撤回或修正的旧结论。

3. 用 [`outputs/algorithms/triple_average_verification_guide.md`](outputs/algorithms/triple_average_verification_guide.md) 查找每项结论对应的文档、脚本、命令、预期输出和证据边界。

4. 机器可读映射位于 [`work/verification_manifest.json`](work/verification_manifest.json)，统一入口为 [`work/run_verifications.py`](work/run_verifications.py)。



计算资源使用、性能剖析和九十一元 `24/24` 有限深度覆盖见 [`outputs/algorithms/triple_average_computation_performance_audit.md`](outputs/algorithms/triple_average_computation_performance_audit.md)；外部减暴力建议的逐项核对见 [`outputs/algorithms/triple_average_search_optimization_review_2026-09-09.md`](outputs/algorithms/triple_average_search_optimization_review_2026-09-09.md)。



标准核接口、自守/adelic 路线与 n=12 首个二维核实验见 [`outputs/triple_average/history/triple_average_kernel_interface_and_automorphic_route.md`](outputs/triple_average/history/triple_average_kernel_interface_and_automorphic_route.md) 和 [`outputs/triple_average/history/triple_average_b12_kernel_experiment.md`](outputs/triple_average/history/triple_average_b12_kernel_experiment.md)。



统一的现代结构语言见 [`outputs/triple_average/history/triple_average_unified_modern_framework.md`](outputs/triple_average/history/triple_average_unified_modern_framework.md)：将状态视为有向重写纤维，把三平均视为 A2 投影，并用带适用域的有向范畴组织跨核操作。只有具有正向逆词的部分才构成群胚。主文件已重写，原稿完整存档在 outputs/history/。



最新的可执行统一接口见 [`outputs/triple_average/history/triple_average_template_compiler_and_torus.md`](outputs/triple_average/history/triple_average_template_compiler_and_torus.md)：用 Smith 格判据编译参数无关子问题调用，并用虚二次范数环面组织 B17 的行列式 3 宏。



任意 \(q\)-平均的根格必要条件、原子秩与宏秩区分、\(S\)-算术控制器猜想见 [`outputs/general_arity/triple_average_q_average_arithmetic_geometry.md`](outputs/general_arity/triple_average_q_average_arithmetic_geometry.md)。



从本目录运行：



```text

python work/run_verifications.py --list

python work/run_verifications.py --profile smoke

python work/run_verifications.py --profile core

```



`full` 档包含九十一元深度四、cusp 29 深度五及 B12/B15/B18/B21 的有限实验，会运行数分钟。新增标准接口、宏族和 theta 格对应见 [三进扩张修复](outputs/triple_average/history/triple_average_carry_repair_and_arithmetic_interface.md)；审核修订见 [audit 修订记录](outputs/triple_average/history/triple_average_audit_resolution_2026-09-09.md)。单项核验可用 `python work/run_verifications.py --id <ID>`。



## 目录约定



- `outputs/`：证明、综合、勘误、交接和验证指南。最新交接稿与勘误优先于早期探索稿。

- `work/`：验证证书、有限实验、搜索程序、辅助模块和历史缓存。其内部说明见 [`work/README.md`](work/README.md)。



现有文件保持原位，以免破坏旧文档中的路径和历史可追溯性。文件名前缀只能表示作者当时的用途；一个 `verify_*` 文件是否构成证明证书，必须以验证清单中的 `evidence_level` 和 `evidence_scope` 为准。


����߽磺�����ഢ���ƽ��У�v=0��1��ֱ�ӽ�������alpha=p-2ʱ�������޵���������壻��˶�����հ�������ȱ�ڡ�


2026-09-12形状势的文献接口：[零和组合文献接口](outputs/prime_arity/structure/prime_arity_shape_potential_literature_interface.md)已阅读Grynkiewicz 2006计数定理、2007逆EGZ及2011 Graham结构。它们支持“失败池低支撑/高重桶”方向，但仍需原位置保护与整数返回宏；不宣称已解决全局终止。

旧 single-value-zero-sum-conjecture 已被 p=13、0^32 1^4 2^4 否定；现有核验改检查反例、最优界 N-floor((p-1)/3) 和三步极端族，不再使用打印占位命令。

EGZ截断分类已更正：对任意 N>=2p-1，无混合p项零和时，至多两个重桶；双重桶覆盖全池，单重桶外的至多p-1个例外必须零和自由。

撤回不必要的 N<4p 上限；正确分类对任意 N>=2p-1 成立。
