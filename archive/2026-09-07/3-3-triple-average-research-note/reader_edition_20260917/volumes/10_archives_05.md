# 工作材料、历次快照及旧目录完整附卷 · 第5分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [历史进展日志（截至2026-09-15整理前）](#doc-12f1160dea79)
- [有限步平均研究](#doc-7b5914820386)
- [成果与研究索引](#doc-03c850066dd0)
- [B_n 参数无关子问题模板编译器](#doc-436d3ed577dd)
- [多危险素数三幂核的链间耦合与加权和转移](#doc-51326f2bfdc0)
- [任意平均元数的线性阈值：非单位差分也是可执行资源](#doc-1f9362671efe)
- [Arena三平均网页算法审阅与同题对比](#doc-82dc396fa577)
- [原位置 p 平均算法测试集](#doc-5aca8265bf7d)
- [从二平均到任意平均元数：当前全貌与临界猜想](#doc-61d3ffed997d)
- [二平均之后的文献进展：2018--2026 检索与可用工具](#doc-ef0a7164ebda)

---

<a id="doc-12f1160dea79"></a>

## 原文导签：历史进展日志（截至2026-09-15整理前）

来源：`work/document_reorganization_20260915/originals/HISTORY.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/HISTORY.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-12f1160dea79 -->
# 历史进展日志（截至2026-09-15整理前）

> 本文保留原根 README。当前状态请读[项目入口](../sources/work/document_reorganization_20260915/originals/README.md)和[素数证明入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/README.md)；下文过期的“未解／下一步”不作当前结论。

---

# 三平均有限步可达性研究

> **研究入口（2026-09-15）**：先读 [outputs/README.md](../sources/work/document_reorganization_20260915/originals/outputs/README.md)。它汇总已完成结果、已排除路线、当前瓶颈和下一步优先级；本页以下是按日期累积的详细记录。

> **GRH三项任务新进展**：[状态与证明入口](../sources/work/document_reorganization_20260915/originals/outputs/general_k_three_tasks_progress_20260915.md)。GRH下全部2、3的幂达到最早临界点；所有整数元数k的2k+1端点补齐；十平均十六元固定六步网络给M(10)=16；奇素数幂的全部奇数2k<n<3k由旧证明的真实互素条件和块均值转译完成。四项均有完整正文和已通过的精确核验；未宣布一般N(k)=B(k)。

> **用户已选择以GRH为主线假设推进一般k**：[条件性平方族完成及剩余任务](../sources/work/document_reorganization_20260915/originals/outputs/general_k_grh_stage_and_remaining_tasks_20260915.md)正式汇合全部t²平均在t²+t+1元的完整判据，素数偶次幂的M、H达到旧下界。H_t不再作为当前主线缺口；下一阶段为素数奇次幂、混合元数及全区间接续。结论明确保留GRH条件，未证明一般最终N(k)=B(k)。

> **H_t已有文献直接适用**：[文献调查](../sources/work/document_reorganization_20260915/originals/outputs/ht_literature_and_eventual_square_completion_20260915.md)实际读到Pollack2017任意模数真子群的小非剩余定理，证明H_t对所有充分大的t无条件成立；n=t²+t+1素数时另有全范围抽屉原理。精确商秩证书补齐t<1000，GRH下得到全t命题；无条件全t仍未完成。已记录3份实际读取的PDF、其余题录／间接引用及2025显式Burgess的适用限制。核验ID ht-literature-interfaces。

> **采纳平方入口建议**：[建议文稿](../sources/work/document_reorganization_20260915/originals/outputs/general_k_plan_review_and_square_entry_20260915.md)已用旧三单点交换子补齐所有t的(t²,t,1)全输入合法入口；[复核](../sources/work/document_reorganization_20260915/originals/outputs/general_k_review_response_20260915.md)确认，并将下一任务集中到小整数尺度群H_t。现有一步终端全在H_t中；入口和t-1根因子已不再开放。独立核验10条入口、404个原子通过；t<=200的H_t满群只是有限诊断。

> **一般k平均后续计划**：[任务顺序与明确验收](../sources/work/document_reorganization_20260915/originals/outputs/general_k_averaging_proof_plan_20260915.md)安排平方族入口和尺度、素数幂、宽区间接续与混合元数。规划复核同时将平方核心资源加强到所有t的U(R)、L(nR)：取得可逆Delta(2)后重新与Sigma作交换子即可，旧t-1奇因子障碍已解除。一般平方族全输入临界定理仍未完成。

> **证明策略与合数继续推进**：[整体策略及合数临界结构](../sources/work/document_reorganization_20260915/originals/outputs/averaging_proof_strategy_and_composite_frontier_20260915.md)重新按入口、真实逆、根、同余控制、方向与尺度、精确终端梳理素数证明；新增块均值转译，完成任意q的全部n=kq、k>=3。另由[平方元数统一周期](../sources/work/document_reorganization_20260915/originals/outputs/square_arity_uniform_controller_and_nine_thirteen.md)和显式除二夹乘完成九平均十三元，M(9)=H(9)=13；没有将其外推为N(9)=13。核验ID square-arity-controller-nine-thirteen、prime-factor-block-mean-transfer。

> **素数平均最优阈值现已完成**：[大载体与两个等大块](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)用共同的(p,p,p+s)核心解决全部3p+s、1<=s<=9。接已证其余区间及2p反例，得到每个奇素数p的N(p)=2p+1；N(2)=4。p>=307由统一闭式计数证明，较小p用同一接口的522组完整有限参数证书和两项明确局部补充。已复核原位置、真实逆、根理想、全部方向、单位尺度和精确终端；沿用Morris/Serre依赖。[最后复核记录](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_nine_offsets_completion_audit.md)。核验ID nine-offsets-large-symmetric-carrier。

**以下为历史进展日志。** 其中“九偏移未解”“N(p)<=3p+10”“一般素数最优阈值尚未证明”均是当时状态，已由上面的完成证明取代；旧方法的限定性障碍仍保留其原数学意义。

> **三进共同终端与半数素数的新最终上界**：[三进载体证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_triadic_packed_carrier_completion.md)完成3p+3、p=1模3与3p+6、p=2模3；第11节完成3p+9、p=1模3。因此p=1模3有N(p)<=3p+8，全体素数仍为3p+10。核心是U(3R)、横向反射及两次状态相关CRT，未搜索平均词或有限群。未完成参数继续保留在完整目标中。核验ID triadic-packed-carrier-completion、nine-offset-residue-one。

> **三个低余量统一完成**：[载体打包共同控制器](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_low_offsets_common_controller.md)证明所有素数p>=5的3p+2、3p+4、3p+8，并覆盖r偶、3不整除r、p>=2r的一般区间。根理想恰为nR，Gamma(n)后一次模n平移完成，未搜索平均词。一般剩余为s=1,3,5,6,7,9；所有n>=2p+1且gcd(n,6)=1已完成，但N(p)<=3p+10未进一步降低。核验ID even-low-offsets-common-controller。

> **小载体的新完整族**：[3p+1、p=4模9](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_plus_one_residue_four.md)以统一收缩逆、迹零恒等式和完美局部群/可解商分离完成全输入判据。九族共用的原位置反射条件现为(3t+b)(3v+s)=bs modp；它只提供可逆返回接口，尚不证明其他偏移终止。完整目标仍是全部素数、全部n>=2p+1。核验ID three-p-plus-one-residue-four。

> **全部素数统一3p+10，无小p阈值例外**：[容量、单位密度与局部提升](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_all_prime_three_p_plus_ten.md)将同一返回接口用于19、23、29、31的八组上端参数，再以两个仿射族和共同的两轮局部提升完成(13,50)、(13,51)、(17,66)。结合已证素数位置数43、67以及4p尾部，得到所有素数p>=5的N(p)<=3p+10。2、3另有更强定理。p=11的34至42仍属于一般3p+1至3p+9家族，未宣称已解；p=2、3、5、7的上半带原本已完成。核验ID upper-band-small-prime-interface。

> **全部3p-1已完成**：[统一3p-1证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_minus_one_completion.md)对所有素数p>=7给出同一重叠反射和乘3折返证明，p=5的14元由显式夹乘补齐，得到N(5)=11。下半带仍有2p+2，已由下一项补齐；上方仍是3p+1至3p+9这九种偏移族。

> **全部2p+2已完成**：[统一2p+2证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_two_p_plus_two_uniform.md)删除 p+1 至多两个素因子的限制。正确的三步重叠反射给深主同余，两个状态相关返回把载体坐标直接安排成 +-1 模控制层；所有素数的 2p<n<=3p 现在都已完成。上方九种偏移仍开放。核验ID two-p-plus-two-uniform。

> **九个低偏移的统一前沿**：[低偏移结构](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_low_offset_unified_frontier.md)修正旧模板容量和组合充分性表述，新增一次模逆的共同原位置反射公式。一般九族仍未完成，不再把缺少锚点保留与整数初始化的组合候选称为充分归约。

> **4p上方尾部完整关闭，达到3p+常数阈值**：[统一d_p尾部证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_four_p_tail_completion.md)证明每个素数p>=5的全部n>=4p完整判据；结合上端和小p接口，所有素数满足N(p)<=3p+10。仍未证明N(p)<=3p；一般3p+1至3p+9偏移族仍须处理。核验ID four-p-tail-completion。

> **一次重叠统一补齐上端**：[重叠载体返回](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_overlap_completion.md)及后续小p接口证明所有素数p>=13的4p-2、4p-1全输入G=1判据；4p上方尾部也已关闭。3p小余量仍开放。核验ID upper-band-overlap-completion。

> **上半带内部区间统一完成**：[无条件上半带证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_unrestricted_completion.md)证明所有素数p>=13、3p+10<=n<=4p-3的全输入G=1充要判据，删除旧gcd(n,6)=1限制；上端及4p上方已有后续证明。核验ID upper-band-unrestricted-completion。

> **端点与全部奇数下半带现已完整证明**：[三单点交换子与无条件入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unrestricted_endpoint_and_odd_band.md)。三个单点角色的交换子给出模rad(n)的真实正向剪切；失效素数整除r+2，其见证可由r个保留位置承接。由此删除端点六素因子/密度条件及下半带r>=omega(n)条件，接已有核心定理得到任意奇p的全部2p+1端点、任意素数p的全部奇数2p<n<3p全输入G=1判据。所有偶余量入口也已完成，但一般偶数核心与最终阈值仍未全解。核验ID unrestricted-endpoint-entry。

> **核内缺口复查**：[常高度乘法、有限例外与多步下降](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_core_gap_reassessment_20260915.md)。保载体返回可在完整约分后使用整除p+1的奇数数字，给出全部本原分母v<=p+1的合法双载体核统一归零算法；结合明确引用的Furstenberg拓扑定理，固定素数p下的剩余分母只有有限多个，但没有有效界或全例外覆盖。另有无限一步失败锥及两种真实逃逸。一般2p+2全输入、其他偶余量和最终阈值仍未完成；核验ID core-gap-four-lifts。

> **邻点完整终止更新**：[统一文稿第11节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)证明所有奇p>=5且omega(p+1)<=2的n=2p+2全输入G=1判据。最近奇数加一次除二配比修复，使本原正奇整数v每轮严格下降到1，全部操作有原位置实现；没有使用算术群或闭路搜索。五平均12元已解，只剩14元。任意p的整个中间带仍未全解。

> **二进深度工具**：[统一文稿第10节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)把每个偶余量合法核心的v2(az)降到1；r=2、p-1已分别由统一状态相关CRT和重叠反射完成。

> **内部偶余量新完成**：[全部内部偶余量](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_interior_completion.md)利用有限逆提升、局部循环和完整单位尺度输送，证明所有素数p>=7、4<=r<=p-3的偶数核心全输入G=1判据；两个边界r=2、p-1已有后续统一完成。

> **完整阈值更新：N(7)=15。** [七平均20、22元与最优阈值证明](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_sharp_threshold_complete.md)补齐最后两个核内缺口。固定正向标量闭路提供逆，主同余包含后完整检查方向与单位尺度；22元的3872个联合状态全在一个终端轨道。接旧结果和十四元反例得到最优阈值。一般p与五平均14仍开放；以下旧日志中的“七平均未解20、22”已由本项取代。

> **中间带统一证明入口**：[整数格、整族终端与两轮入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)。两条带使用同一个m=1、2加权核心，明确保留非幺模换元的2、3局部信息和有限单位尺度。两轮修复接最新三单点交换子初始化后，下半带入口不再需要任何素因子数或密度条件；一般偶数核内终止仍未证明。后续阅读以统一文稿、新入口证明及状态表为主，下面日期日志用于溯源。

2026-09-14上半带完整定理：[与6互素维数的统一证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_coprime_six_complete.md)完成任意素数p>=13、3p+10<=n<=4p-3且gcd(n,6)=1的全输入G=1判据，不限制n素因子数。额外对合统一反演r，三个一阶方向加强到Gamma(n)，Smith-CRT夹乘给安全整数返回的正向逆，半载体激活3，二三单位小代表与Bezout送到零触发终端。274组参数和822条精确目标输送等核验通过；被2或3整除的维数、两端短区间及4p上方接续仍开放，最终阈值未降低。核验ID upper-band-coprime-six-complete。

2026-09-14上半带迁移：[四返回双向根与深同余控制](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_four_return_congruence.md)把现有两种载体各取相邻参数，统一构造U(rn²R)、L(rn²R)，接深同余引理得到Gamma(r²n⁴,R)。所需容量对p>=13、3p+10<=n<=4p-3全部成立；有限终端覆盖、两端小余量和4p上方接续未证。本项不新增完整维数或降低最终阈值。核验ID upper-band-four-return-congruence。

2026-09-14偶数维数推进：[偶数深同余与七平均十八元](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_middle_congruence_and_eighteen.md)证明任意内部偶余量4<=r<=p-3的深主同余控制，并以短配比替代部分失败的周期入口。七平均18元的完整模5184终端证书和R=Z[1/65]单位提升完成全输入G=1判据，临界未解剩20、22。一般偶数终端覆盖、r=2及r=p-1仍开放，最终阈值未降低。核验ID even-middle-eighteen-congruence。

2026-09-14任意p的中间带统一结果：[全部奇余量核心](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_uniform_odd_middle_cores.md)证明任意素数p>=5、奇数3<=r<p的合法(p,p,r)核心全部可达。两个始终存在的对合统一产生n倍双向二进根，主同余控制再使保载体收缩F1获得正向逆；小代表折返替代“2是原根”的特殊条件。接已有入口，所有2p<n<3p的素数维数及满足周期密度条件的奇合数维数得到完整G=1判据。七平均17、19元新增完成，尚缺18、20、22元。一般最终阈值未降低；完整平均词效率仍未控制。核验ID uniform-odd-middle-cores。

2026-09-14后续区间实际应用：[五平均十三元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/five_average_thirteen_congruence_complete.md)将已有(5,5,3)核的两个对合接入新的有限指数/强同余接口。倍率-12与换块给U(13/4)，再得双向13Z[1/2]根；三个幂零方向覆盖模13的全部主同余层，有限模平移及2的单位代表送到三步终端。由既有全输入入口，十三元G=1充要判据成立。五平均剩余12、14元；N(5)<=15未降低。本页为引用外部群论定理的存在证明，不提供高效任意输入完整平均词。核验ID five-thirteen-congruence。

2026-09-14文献接口补齐：[任意合数端点核心的同余闭合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)引用Morris 2007定理6.1(2)和Serre的SL2(Z[1/2])强同余子群性质，证明二进U(A)、L(nA)恰生成Gamma1(n,A)。再用一个平衡小主元补齐整数Gamma0(n)，接已有正向控制器，得到任意奇元数p的合法2p+1双块核心全部可达。六素因子或Theta(n)<1入口范围因此升级为完整端点判据。任意多素因子入口和后续维数仍开放；证明不提供高效完整平均词求解器。内部有限商与单位分解已独立核验，外部定理不由样本验证。核验ID endpoint-congruence-completion。

2026-09-14局部算术分支已补齐：[全碰撞单位分支的统一补回](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_complete_unit_collision_recovery.md)证明规定载体步骤后至多再作三次安全整数平均即可恢复相邻p重值对，完整核心前缀至多五步。小负逆元由载体预算统一处理；e=1、h>=4由一次重叠和模h^2-2的O(h)配比构造处理。另证明h(h-1)r<p时两个不交非恒等整数组根本不存在，983例以统一五步绕过。3305个计数系统、627个实际临界入口全部通过，此前十个入口已覆盖。这里完成局部补回，未证明多值输出递归闭合或降低阈值。ID complete-local-unit-recovery。

2026-09-14重数与精度的锐边界：[重数弱化的锐障碍与一位精度必要性](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_sharp_repetition_and_precision_barriers.md)证明截断重数和S_p>=2p-1+h保证安全非恒等整数平均，并将安全整数停滞态压缩为一个大背景及至多p+h-1个例外。纯整数冻结的第二大重数至多p-2且可达等号；但(p,p-1)及S_p>=2p-1都被任意大维数的G=1停滞族反驳，其唯一非恒等整数输出G=n。n=5p-4的该族恰需一位额外精度，充分性引用现有大维数定理。另给安全三步分数前缀耗尽一位精度、同一输入却有两步整数造零的对照。132个停滞例、24个锐冻结例、161个保护选择及8组策略对照通过；没有降低阈值。ID sharp-multiplicity-precision。

2026-09-14任意h的新转移：[欧几里得见证转移与最大值下降](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_euclidean_witness_transfer.md)统一处理全部d>h，以及e=h-d>=2且2d eta>=e的临界入口，其中eta=-(s+1)^(-1) mod e。短正余数由一次模逆直接构造，两个真实不交组产生相邻整数重值。d>h输出还可消去全部旧A、B，再建立更低的重值对，使全局最大值严格下降。剩余通用菜单边界为d=h-1或3d<h且负逆元很小；这一版菜单曾留下10个入口，现已由统一补回续篇覆盖。4957个余数系统、2413个计数系统、474条不交组转移及248条实际输出续行通过；递归闭包和阈值仍未解决。ID euclidean-witness-transfer。

2026-09-14单位见证继续推进：[Hilbert基、精确容量与三原子补回](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unit_witness_replenishment.md)完整参数化核心全碰撞分支hs<p，证明偏差(1,s+1,-s)的Hilbert基及两原子补回充要条件；容量不足只在h<sqrt(p/2)、1<=p-hs<2h-2。进一步以三原子公式补齐全部缺额1及(h,d)=(3,2)，从而覆盖所有h=2、3不足分支。另证明任意k、n>3k且k不整除n时，相邻重值对不能作为单步闭合不变量；实际29平均95元核心虽有该障碍，却有四步造零。241187个容量系统、1051条两原子补回、14个扩展或直接分支及49个统一障碍实例通过核验；未证明递归闭包或降低阈值。ID unit-witness-replenishment。

2026-09-14三条改进的后续：[来源关系、动态见证与整数返回阶段](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_provenance_dynamic_and_integer_stages.md)证明指定核心出口后总有第二次安全整数续步或已造零；所有危险素数共用同一个支持，由gcd(3alpha-2,n)确定，保护预算至多一处。实际七步反例否定任意来源后继的整数闭包；固定A、C会排除分数阶段的共同因子约分，并在明确核心族上阻止本原平方能量与临界两两距离下降。奇素数同格整数返回至少五步，且有合法五步正对照。5926条后继续步及相关精确核验通过；未证明递归闭包或降低阈值。ID provenance-dynamic-integer-stages。

2026-09-14不变量改进：[能量唯一性范围与上半带整数出口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_invariant_improvements_and_core_exit.md)明确唯一性仅限共同单调固定正定二次型。证明任意合法整数(2p,p,r)核心都有一次安全非恒等整数平均保留两个不同p重值；碰撞会迫使n整除3j+1，故排除。核心原始同余保护只有3|r时的模3分支，r=1、2时每个原子都保留所有见证。下一步应使用后继关系pM=iA+jB+C，而非把四值后继视为任意状态。10800个类型选组、944条整数出口、180个非二次势核验通过；未证明递归闭包或降低阈值。ID `core-exit-potential-scope`。

2026-09-14已纳入可用的外部想法：[不同实际值数的整数归约](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_distinct_value_integer_reduction.md)证明任意k在n>2k时，D>=d+2k-1保证安全非恒等整数平均，并有限降到D<=d+2k-2。另[回看三平均合数与高斯周期路线](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_revisiting_ternary_factor_gaussian_route.md)核对旧素数归约及ell=1 mod3证明：一般p的高斯范数正向逆可推广，但3p<ell<4p没有ell=1 modp的素数位置数，旧范数一剪切恒等式也不能直接替换p。合数真因子在2p<n<4p时都小于2p，须另外证明小商可解。六条整数入口、六个全系数基的原位置周期及4503项容量核验通过。未降低阈值。ID `distinct-entry-gaussian-transfer`。

2026-09-12新的实质结果：[单值零和最优界与极端冻结态三步逃逸](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_sharp_concentration_and_escape.md)否定旧3p-2猜想，证明所有N>=2p-1的最优两桶界N-floor((p-1)/3)。引用Balandraud定理并核对勘误；达到最坏界的合法整数冻结族在全部素数p>=13（另含p11）都有三次真实平均造p个零的公式，首次造零步数最优。45408个零和自由序列、319015个余数配置及91条原位置路径核验通过。未新增全维数判据或降低N(p)。ID `sharp-monochromatic-escape`。


2026-09-12主余类储备推进：[主余类储备与刚性例外](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_dominant_residue_reservoir.md)把多余轻余数分支压缩为：主余类碰撞先锁定小整数提升；任意例外余数有合法配比；两个配比同时碰撞时提升满足唯一整数仿射关系；总超额达到p时有严格能量下降。367224个碰撞提升、37754个例外配比、13301个容量包装和834条原位置续步通过。多余类全局闭包仍未证明。核验ID `dominant-residue-reservoir`。

2026-09-12整数闭包新证明：[二类型碰撞的整数格结构](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_binary_collision_lattice.md)用平面空三角形的指数1性质，证明临界p预算下二类型全碰撞参数必为整数，并给富余预算的总和界。对(a^(p+alpha),b^p,轻值)且一个低重模p余类、保护数h<=r的上半带状态，得到安全非恒等整数续步；只有一种实际轻值时h<=1，覆盖r=1。另通过G=1直接补齐三个重值在3p+1的一个额外位置分支。2133条单轻值、300条三重值、127条同余多实际值原位置续步通过；一般多余类闭包及N(p)<=3p仍未证明。核验ID `binary-collision-lattice`。

2026-09-12核心终止审计：[距离3p的真实缺口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_remaining_gap.md)给出七平均22元(2^14,(-1)^7,-21)：所有十个非恒等三组不交核心返回均非法或增大本原能量，且无终端后继，但两次重叠整数平均即可造七个零。该逃逸推广到任意素数p>=5的(2^(2p),(-1)^p,-3p)族，首次造零恰需两步。另给所有r>=4的第二载体对合，明确终止步数必须随输入高度无界，以及p761/n3045未被旧4p-2+d不等式覆盖。未完成一般核心终止或降低N(p)。核验ID `upper-band-descent-boundary`。

2026-09-12上半带统一归约：[3p到4p的任意素因子数三值归约](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_three_value_reduction.md)证明每个素数p>=5、每个3p<n<4p的全部合法输入，至多12+3ω(n)次原位置平均进入合法(2p,p,n-3p)二维核心。初等短区间筛选、双块集中见证和三行折叠消除r>=d及素因子数限制。核心G=gcd(y,n)，二次型判别式-8n(n-3p)；所有r>=4还有显式三步全局射影对合。385条归约路径、700条六原子标量周期及本原高度增长恒等式通过。不宣称核心终止、七平均22元已解或最终阈值降低。核验ID `upper-band-three-value-reduction`。

全局总览（2026-09-12）：[从二平均到任意平均元数：证明、自动G、非自动G边缘和临界猜想](../sources/work/document_reorganization_20260915/originals/outputs/averaging_global_status_20260912.md)。统一区分固定维数完整判据、G自动成立的无条件维数、G真正筛选输入的H(q)，以及要求所有后续维数的最终阈值N(q)。当前已证非自动边缘为H(2)=5、H(3)=7、H(4)=7、H(5)=11、H(6)=10、H(7)=15、H(8)=13、H(10)=H(12)=17；九平均13、十四平均22、十五平均21等仍是候选。任意q的大维数定理为n>=4q-1+d_q(n)，精确临界线H(q)=C(q)仍为猜想。



2026-09-12十、十二平均17元完整解决：[十平均与十二平均的非自动G判据](../sources/work/document_reorganization_20260915/originals/outputs/ten_twelve_average_seventeen_complete.md)证明两者均可达当且仅当G=1，因此H(10)=H(12)=17；16元的G自动满足不计入非自动边缘。两步进入(10,6,1)/(12,4,1)核，18陪集Gamma_0(17)分别由十平均的Delta(5)和十二平均的Delta(3)配合二进根覆盖。17个q<=200的旧B自动点也已独立列出。各自60个大整数入口和3条完整路径通过；不宣称N(10)=17或N(12)=17。核验ID `ten-twelve-seventeen-complete`。



2026-09-12入口继续缩小范围：[六素因子入口与覆盖系统边界](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_six_prime_endpoint_entry.md)证明任意至多六个不同素因子的2p+1输入可进入合法双p块。五个任意乘法阶坏类不能覆盖；真正合并时坏类只来自一个非全支持单点，至多d-1个，因此得到六素因子结论。原p217717/n435435的K4直接分组障碍可至多五次真实平均绕开并进入核心，未宣称该巨大level已完成归零。另给任意d下Theta(n)=sum 1/ord_ell(2)-min 1/ord_ell(2)<1的入口充分条件，六个坏类的模24覆盖说明继续外推需要不同见证选择。核验ID six-prime-endpoint-entry。核心群包含与中间带终止仍独立。



2026-09-12两方向新推进：[四素因子端点入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_four_prime_endpoint_entry.md)证明任意至多四种危险素数的2p+1输入都能有限步进入合法双p块。交换在各端点素数下统一产生2^k，每处只禁止一个指数类；3、5的奇偶筛选与剩余密度界保证指数存在。接原核心证书，195、231、255、315、399、435、455、1155八个端点新增全输入判据，p=97不再缺入口。另见[中间带周期密度归约与全部r的对合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_band_period_and_involutions.md)：r>=d且局部交换阶倒数和<1时，所有2p+r输入可降到(p,p,r)，包括中间带所有素数维数；每个r还显式具有合法两步射影对合，四原子成非零标量周期。尚未证明任意level的核心群包含或一般三块核心终止。核验ID four-prime-entry-and-band。



2026-09-12合数端点统一推广：[CRT陪集证书与两素数入口](../sources/work/document_reorganization_20260915/originals/outputs/composite_endpoint_crt_transfer.md)。十五元方法已编译为统一流程，36个列明模数的32112条回路全部通过独立精确核验；28个双素因子模数由一般三步入口得到全输入G=1充要判据，包括十七平均35元、十九平均39元、三十一平均63元、三十七平均75元及含重复素因子的135、147、175、207等。结合旧素数幂定理，全部奇整数3<=p<=109的2p+1端点均已覆盖。p97/n195等8个多素数模数的入口已由四素因子入口定理补齐，36个列明端点均已完成全输入判据。未证明任意合数的全称群包含，有限主元菜单全成功也不外推；最小非自动G边缘对合数平均元数仍须单独研究。ID `composite-endpoint-transfer`。



2026-09-12算法回归交付：[困难输入测试集](../sources/work/document_reorganization_20260915/originals/outputs/averaging_algorithm_benchmark.md)保存584道去重题、19道精选题及2道历史束搜索深度24未出解的大整数题。其中196道七平均十五元冻结态已由新端点定理保证可达；108条参考原位置路径独立精确重放通过。p=19、37扩展题按有无直接证书标注，332道不设可达性真值。附1基索引验解器、新题生成器及旧预算记录；不重新搜索，不把路径未找到记为反例。核验ID averaging-algorithm-benchmark。



2026-09-12七平均十五元完整解决：[两素数入口与二进Gamma_0(15)](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_fifteen_complete.md)证明可达恰在G=1，故按非自动G标准H(7)=15。任意至多两种危险素数的端点输入可用至多三次平均进入合法双p重块；十五元CRT给24个陪集，全部72条回路用62个左上主元、8个右下主元及2次半整数剪切完成正向编译，完全使用已证二进根，不另搜索种子或激活11、17倍率。192个本原模行、72个强制三步入口与7条完整Fraction路径通过；最长样本7746步不代表最短界。平均元数7的候选端点15现已证，8的13也已证，下一个待攻的元数是9、候选13元。七平均更高维数17、18、19、20、22仍未解决，因此不宣称N(7)=15。核验ID `seven-average-fifteen-complete`。



2026-09-12非自动G条件的新完整结果：[六平均十元](../sources/work/document_reorganization_20260915/originals/outputs/six_average_ten_complete.md)证明可达恰在G=1或2，G=5或10由模5障碍排除，故按“G确实筛选输入”的标准H(6)=10。两步进入(6,3,1)核后，新增两步宏R满足R^4=-I/324、(AR)^2=I/36、(RAC)^2=I/216；正向逆与真实交换子给出L(-5/3)，进而实现Gamma_0(5)的全部18条回路。两类合法G各60个大整数入口、196种余数多重集和6条完整原位置路径（最长1931步）通过。后续研究以非自动算术边缘H为主，无条件网络作为辅助工具。六平均当前首个未解维数为11；不宣称最终阈值已确定。ID `six-average-ten-complete`。



2026-09-12历史反向诊断已更正：[整数冻结态与分数逃离](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_counterexample_reverse.md)。高度5的35714个合法状态全部可达；其中7个无整数出边，87个首步值类型均无零触发，但七条完整分数路径均独立重放通过。旧“最低层重叠自动下降”说法已撤回：部分相交实际加深分母，成功路径通过不交分组留下单点。七平均十五元随后已完整证明，困难题现转作算法测试。ID endpoint-reverse-diagnostic。



2026-09-12合数临界线新结构：[局部平方根尺度与精确猜想](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md)。定义S(q)=max p^ceil(v_p(q)/2)。赋值间隙不变量证明q<n<q+S全部有G1反例；边界q+S除非只有q允许的素因子，否则也有反例。因此B(q)=q+S或q+S+1是已证下界，猜想M(q)=N(q)=B(q)，其中M排除n=q后表示最早成功，N要求之后所有维数成功。新固定四步族q=m(m-1),n=m²在m或m-1为素数时与下界吻合，严格给出M(12)=16、M(20)=25、M(30)=36、M(42)=49、M(56)=64等。另由(8,4,1)核、两个精确周期及模13全部42条回路证明M(8)=13。二平均的4与六平均的9属于G自动合法的固定网络点；5与10则是随后第一个非自动G维数，六平均10现已由独立模5控制器证明。核验ID `composite-critical-scale`、`eight-average-thirteen-complete`。



2026-09-12路线重评估：[任意 p 的结构、分段高度与文献](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_strategy_reassessment_20260912.md)。第二轮检索44个结构关键词、148篇去重题录并阅读4份全文后，最有希望的不是寻找新的固定二次能量，而是建立带局部同余、p进内容和块形状节点的 path-complete 离散高度；算术群的相对有界生成可作为已实现根之后的后处理。同步记录了多素数单位分离障碍和一般 r 合并恒等式。当前完整新族仍是 p=2^s-1 的 n=2p+2；全中间带开放。ID strategy-reassessment-20260912。



2026-09-12合数平均的统一突破：[任意元数的线性阈值](../sources/work/document_reorganization_20260915/originals/outputs/arbitrary_arity_linear_threshold.md)把充分大维数定理推广到每个整数q>=3：n>=4q-1+d_q(n)时，完整判据为G的素因子均整除q，且整数零和输入只需一位额外q进精度。非单位差分delta用q/gcd(delta,q)份配比直接平均；偶数元数唯一中点碰撞由顺序结构或相反值终端解决。由此N(4)<=16、N(6)<=24，不再留下无限多未解维数。同时[四平均九元](../sources/work/document_reorganization_20260915/originals/outputs/four_average_nine_complete.md)用显式四步周期、二进根和模9全部36条Schreier回路完全解决，无种子搜索。结合半块转译，候选临界带内尚未证明G充分的仅四平均11、13、15元，六平均11、13、14、16、17、19、20、22、23元。新核验ID `arbitrary-arity-linear-threshold`、`four-average-nine-complete`；不宣称最短解或精确阈值。



同日更新：[四平均七元](../sources/work/document_reorganization_20260915/originals/outputs/four_average_seven_complete.md)通过 (4,2,1) 核和三个真实一步宏完成；实际周期为 C^3=I/8、(CA)^2=I/8，Sigma也由真实三步词实现。改用模7的0、±1、±2、±4代表，24条回路全部采用二进单位主元，无种子或平均词搜索。[六平均九元](../sources/work/document_reorganization_20260915/originals/outputs/six_average_nine_fixed_network.md)独立复核固定四步网络，并证明三步固定全输入网络不可能。入口 `four-average-seven-complete`、`six-average-nine-fixed-network`。两项结论只确定7和9这两个维数；最终阈值仍为 \(7\le N(4)\le16\)、\(9\le N(6)\le24\)，不能由端点成功直接取等号。



2026-09-12新完整中间维数族：[统一能量与 2p+2](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_energy_and_dyadic_neighbour.md)。对每个 p=2^s-1、s>=2（允许奇合数平均元数），全部 n=2p+2 输入恰在本原中心化 G=1 时可达，特别新增七平均十六元。安全分块、CRT 单点等值化、真实两步上平移及除法返回使本原奇数方向高度 |v| 在完整阶段间严格下降，不依赖 2p+1 端点。一般 p 的双单点也能在至多 p+1 步归约到合法 (p,p,2) 二维核。另证明共同单调正定二次型只有平方能量，非整数交换的本原平方高度反而增加。31278 个方向、24 条核路径、48 条原输入 Fraction 路径等核验通过。ID carrier-energy-dyadic-neighbour。



2026-09-12合数平均新结果：[四平均、六平均与统一半块转译](../sources/work/document_reorganization_20260915/originals/outputs/composite_arity_four_six_transfer.md)。对偶数q，原位置重叠块制造q/2的倍数份副本，再把所有允许的奇素因子吸收到副本数c中；剩余二平均商维数M=2或M>=4时，完整G判据成立。这覆盖任意偶数q的全部q倍数维数，并证明四平均全部偶数n>=8（另有n=4）、六平均全部3|n且n>=6。六平均九元有固定四步网络，其三进张量推广补齐纯三幂维数。四平均六元(-1^4,0,4)、六平均八元(-1^6,0,6)均为G=1的严格不可达例，由局部赋值与同余分支证明。533个标准基、35个副本宏、32415个陷阱后继及336条完整路径精确通过。核验ID `composite-four-six-transfer`；未证明四平均全部奇数维数、六平均3不整除的维数或最终阈值。



2026-09-12中间带接口已修订：[相对尺度与单点—块交换](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_middle_band_relative_scale.md)。该交换自动保持全部非 p 同余见证，模 p 匹配只为整数中间值所需；允许分数后必须另证终止。(p,p,1^r) 的均值格商阶为 2p+r，只有实际等值化成 (p,p,r) 才能除去 gcd(p,r)。旧的“同时匹配与动态保护均未解决”表述不再适用于这个交换子类。



2026-09-12临界端点的深层结构：[素数幂端点与临界几何](../sources/work/document_reorganization_20260915/originals/outputs/prime_power_endpoint_and_critical_geometry.md)。对任意奇p，q=2p+1为素数幂时，两张局部射影坐标图的全部Schreier回路均可由已证正向控制器编译，得到射影Gamma_0(q)包含；配合两步合法入口和Bezout输送，完整解决所有素数幂端点，特别是十三平均二十七元与形式上的1093平均2187元。临界能量是判别式-q虚二次阶的范数，产生权一theta级数；但level27、weight1的LMFDB空间全为Eisenstein，模形式解释计数而不直接提供原位置路径。相邻2p+2的真正障碍是局部逆只给共同收缩lambda，外部单点固定后变成diag(lambda,lambda,1)，不再是全局射影单位。独立核验15612条回路、55512个模行、168条编译回路、32个入口及2754个范数恒等式。ID `prime-power-endpoint-completion`。



2026-09-12临界前沿交接：[当前方法的障碍与2p+1结构](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_critical_frontier_handoff.md)。区分一步双重值闭包、固定保护、有限短词表、直接多素数分块和余维一黑箱调用的已证障碍，明确这些是特定方法边界而非总猜想的反例。建议将碰撞总和保留为上界支线，优先研究素数幂端点的真实正向轨道和2p+2双单点的部分控制。新增完整证明：q=2p+1为素数幂时，任意G=1输入都能两步进入合法K_p；p本身为奇素数且q合数时，q必为3的幂。入口不解决核内轨道，未新增完整端点或降低阈值。独立原位置核验ID：prime-power-endpoint-entry。



2026-09-12任意p的统一碰撞结构：[两组相加、总和窗口与高重数分类](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_uniform_collision_structure.md)。在保护后3p+1层，任一低重数余类达到p-2重即可统一闭合：全碰撞只允许D=3p或3p-1，再由私人见证／全局零和排除。分数坐标族有显式除数参数，包含所有p=2 mod3的一族，不需逐p求表。另由Dias da Silva--Hamidoune受限和集定理处理至少sigma(p)=min_k(2k+ceil((p-1)/k))种余数；零和因子分解给两个明确的总余数窗口。二平均最近对也推广为安全连续p块的新生重值引理，但一般保护容量仍在。核对51618个高重数符号模式、779个原位置合法步骤、4824个零和分解、105760个窗口公式及144个受限和集构造。剩余是中等重数余类交互；未降低一般4p级完整阈值。ID `uniform-collision-structure`。



2026-09-12七平均推进到3p+2：[对称碰撞总和证书](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_three_p_plus_two_threshold.md)完整解决七平均23、24、25、26元，接已有>=27，得到15<=N(7)<=23；21元另已解，22元仍开放。一般有效的余数类对称压缩只保留总和，57026个完整模7模式仅有11个相容解，再接最小保护总和矛盾；新增四维数均只需一位额外精度。另见[可交换保护与统一初始化](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_protected_exchange_and_mass.md)：初始化降至n>=3p+d-2，p=23,n=70反例说明不能固定任意极小保护集；交换后产生一整个p=2 mod3的3p+1元五步整数族。任意p的3p级阈值仍未证明，p=11总和数据仅为探索。ID `seven-average-three-p-plus-two`、`minimal-protection-and-exchange`。



2026-09-12五平均达到3p：[最小同余见证与碰撞总和证书](../sources/work/document_reorganization_20260915/originals/outputs/five_average_three_p_threshold.md)。完整解决五平均n=16、17、18；结合已证n=15及全部n>=19，得到11<=N(5)<=15=3p。低总重数不同余双重值的全部碰撞对应903个模5模式的有理线性系统，只有22个相容解，且总和的局部分母可控；最小保护横截集的私人见证与全局零和排除所有合法例外。新增三维数都保持一位额外精度；本证明是完整有限符号证书辅助，不是平均词搜索或有限输入外推。五平均尚未解决12、13、14；任意p的3p级阈值仍开放。新的通用方向是证明碰撞关联方程的总和证书，无需逐个确定所有坐标。ID `five-average-three-p-threshold`。



2026-09-12直接面向3p：[长零和自由序列与双锚点接口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_additive_interface.md)。引用Savchev--Chen长序列结构，重复锚点将其单位缩放锁为1，证明n>=3p+d时低总重数不同余双重值必有安全非恒等整数候选，保留一个旧p重块；较长序列零和自由时用一／两个低重数位置进一步修复碰撞，完整保持双重值。剩余是候选存在但实际和全部碰撞的恢复／造零，尚未证明3p统一上界。新核验器精确计算模p子序列和的实际最小／最大值，避免过早截断安全池；4246个样本未留全碰撞不承担无限结论。与2024年同余拟阵基／群标签基理论的具体对应和适用边界已记录。ID `three-p-two-anchor-interface`。



2026-09-12阈值实际下降：[逆EGZ的4p-2+d定理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_inverse_egz_threshold.md)。对奇素数p>=5，完整判据已在n>=4p-2+d_p(n)成立，故N(p)<=4p+ceil(log_2 p)，特别N(5)<=19、N(7)<=27。三重值的单份／双份中间值修复把该分支降到3p+2；两个不同余重值总重数>=3p-2时有共同预留跨越。保护后2p-2池若无整数p子集，逆EGZ强迫两个p-1余数类，再借一份／两份锚点修复碰撞。全部整数能量闭包保持，一位额外精度仍成立。约7p/2+d路线已有明确容量，但低重数池的统一碰撞恢复尚未证明，不列为新上界。ID `inverse-egz-threshold`。



2026-09-12逆零和工具已转译：[碰撞修复与2p+4七步族](../sources/work/document_reorganization_20260915/originals/outputs/inverse_zero_sum_averaging_progress.md)。2022逆加权零和定理给出O(p)模运算的真实副本选择；两次相反碰撞在不交副本和保留见证下恢复双重值。五平均十四元的(5,5,2,2)核在两个锚点模5不同、低重数两值模5不同或有锚点同余时，已有完整安全整数闭包；余数集中情形确实可能每步失去不变量。另有任意奇数p>=5的2p+4元二参数族，两次平均造零、总计至多七步；其中(6^p,8^p,[p(18-p)]^2,[p(p-25)]^2)对所有奇素数合法且没有非恒等整数一步双重值闭包。没有新增完整维数或降低统一阈值。ID `inverse-zero-sum-transfer`。



2026-09-12外部文献检索：[2018--2026年的二平均后续与可借用工具](../sources/work/document_reorganization_20260915/originals/outputs/averaging_literature_survey_2018_2026.md)。核对原论文2019会议／2020期刊版本、作者2019博士论文、2020 RPRIS、2019 Clique Gossiping、2021--2022块Kaczmarz、2022逆加权零和和EGZ近线性算法，以及2024 splitter和2025--2026相关题录。本轮未找到一般p平均完整判据或最优阈值的已核验外部证明。已读逆零和全文给出一个可由两份副本实现的整数平均候选引理，但安全性与碰撞仍需另证。没有更改正式求解算法或新增完整维数；综述明确标注全文与摘要的证据边界。



2026-09-12维数传播与统一终端：[造零收尾、余维一障碍和加权均值格](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_interpolation_and_lattice_structure.md)。对所有奇素数p及n>=2p+1，一旦真实p平均产生p个零，就能完整归零。下半区间只需已证的2p+1含零尾部，无需端点完整猜想；上半区间用3p、4p和大维数定理按支持数传播。另证n非p幂时整块等化n-1个位置必归零或陷入G=n障碍，因此不能用相邻已解维数黑箱直接内插。块重数除公因子后的总和s给出Z^k/(零和格+常值方向)=Z/s，统一解释端点的Gamma_0(2p+1)和三块的Gamma_0(3)。未证明任意合法输入必能先造零，未新增完整中间维数。ID `prime-arity-zero-trigger-bridge`。



2026-09-12中间维数推进：[三块运输与3p完整定理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_middle_band_structure.md)。对每个奇素数p，n=3p的完整p幂G判据已证；p>=5时写p=3m+epsilon，两张明确非负运输表mJ+epsilon(I+-D)在原3p位置实现U(+-1)，块重标记再给L(3)，同一个四陪集Gamma_0(3)及模3分组修复完成全部输入。无种子或平均词搜索，旧3p一步闭包反例族也全部解决。另证n>=3p+d时两个模p同余重值的安全整数闭包。五平均新增n=15，尚待覆盖12、13、14、16、17、18、19；统一N(p)上界不变。ID `prime-arity-middle-band`。



2026-09-12统一正向控制器：[无需搜索的临界种子证明](../sources/work/document_reorganization_20260915/originals/outputs/uniform_endpoint_positive_controller.md)。对每个奇数平均元数 p>=3，在原 q=2p+1 个位置上的两种两步返回、互补仿射倍率和必碰偶数的整数递推，统一给出可逆倍率2、U(1)、L(q)。欧拉同余随后为全部安全的 j<=p 构造正向逆，得到 R_q=Z[1/l:l<=p且l不整除q] 上的完整上根、q倍下根及对角单位。q为素数时，完整Schreier与入口证明遂解决全部输入，统一(3,7)、(5,11)、(11,23)、(23,47)等，无平均词搜索。q为合数时种子已解决，但合数level轨道与任意输入安全入口仍未闭合，七平均十五元仍不宣称全解。ID `uniform-endpoint-controller`。



2026-09-12七元精确端点结构：[为什么阈值是七](../sources/work/document_reorganization_20260915/originals/outputs/seven_exact_threshold_structure.md)。双三重块与全系统载体的六次交换给出 -1/27 的正向标量周期；三个明确跨块返回满足三条短周期，生成 Z[1/6] 上的上根、7倍下根及对角单位，八陪集与六个 Schreier 回路遂给出完整 Γ₀(7)。这是不依赖旧十八词下降覆盖的另一份七元充分性证明。一般p双块扫掠的判别式为p(p-4)，解释p=3的有限周期与p>=5的双曲分界；精确端点不必通过不断压低大维数常数获得。ID `seven-endpoint-structure`。



2026-09-12上界降至4p级：[三个重值的顺序结构与3p边界](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_four_p_threshold.md)。对奇素数平均元数p，n>=d_p(n)+4p-1 已足够，故 N(p)<=4p+ceil(log_2 p)+1。三个重值用实际极值和单份参与直接处理，只对两个重值预留2p位置，再调用保护后的EGZ。因此五平均全部 n>=20 已解，结合 n=11，尚待覆盖 n=12,...,19。另有任意p>=5的合法3p元族，所有非恒等整数平均都会只剩一个p重值且不造零；这只否定未经补充的双重值一步闭包，不证明3p不可达。ID `prime-arity-four-p-threshold`。



2026-09-12五平均十一元已证：[完整证明](../sources/work/document_reorganization_20260915/originals/outputs/five_average_eleven_complete.md)。五个两步原位置返回和三条短标量周期提供全部正向逆；在 (a,a-b) 坐标中生成 Z[1/30] 上完整上根、11倍下根和对角单位。有符号十二陪集与十个明确 Schreier 回路证明包含 Γ₀(11)，Bezout 输送和四步终端解决全部合法输入。因此五平均 n=11 的充要判据是 G=1，不再只是有限样本结果。全程只用五平均，未调用三平均或子维数求解器。n=12,...,24 尚未由此解决，N(5)=11 仍未证明；不承诺一位额外精度或最短构造。ID `five-average-eleven-complete`。



2026-09-12边界推进：[预留重数与临界结构](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_boundary_progress.md)将素数元平均的充分界改进为 n>=d_p(n)+5p-1，特别 N(p)<=5p+ceil(log_2 p)+1<=6p，且 11<=N(5)<=25。n=2p+1 中含零状态统一至多五步收尾，Y_p=(1^p,2^p,-3p) 恰好四步可解。若2p+1为素数，全输入两步可进入合法K_p；若含六个不同素因子，K4/CRT构造会阻塞每个直接(p,p,1)划分。p>=5的两个自然核返回保留避零实区间，必须加入跨块操作；第一未解实例是五平均十一元的全参数核终止。ID `prime-arity-boundary-progress`。



2026-09-12阈值细化：[素数元平均的线性阈值与 2p 边界](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_linear_threshold.md)。EGZ 保护池、四重值的极端锚点及系数跨越打包，将 n>=2p^3 改进为 n>=d_p(n)+8p-7，特别是 n>=9p-5。对奇素数 p，(-p,0^(p-1),1^p) 在 n=2p 处不可达，故 2p+1<=N(p)<=9p-5。N(2)=4、N(3)=7；p>=5 的 N(p)=2p+1 仍为猜想。n=2p+1 的 (1^p,2^p,-3p) 还明确否定无例外的双 p 重值一步闭包，不能只靠调小常数声称最优界。ID `prime-arity-linear-threshold`。



2026-09-12素数平均元数推广：[素数元平均的充分大维数定理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_averaging_large_dimension.md)。这里 p 是一次平均的位置数，n 是任意总维数。对每个素数 p、n>=2p^3，完整可达判据为本原中心化 G 是 p 幂；整数零和合法输入只需分母 p。证明通过双 p 重值、保护池和一次模逆调节，把不能继续的状态限制为可直接消去的短等差数列，不调用三平均定理或任何子维数。阈值只求充分，不声称最优；合数平均元数尚未由此证明。ID `prime-arity-large-dimension`。



本目录保留全部研究过程，同时提供一层稳定的接手入口。2026-09-11：[双三重值不变量](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_prime_double_triple_invariant.md)给出全部素数 p>=11 的统一原位置证明，结合既有七元证明和合数归约，闭合原判据：对任意 n>=7，中心化、本原化后的非零状态恰在 G 为三幂时可达；全零状态单独显然可达。



新证明先研究 3X，至多两次整数三平均建立“至少两个不同三重值”，再按模3余类与重数选择真实原子，保持模p不全同余，直至 (a^3,(-a)^3,0^(p-6)) 终端。固定整数格上的平方能量给出有限终止，因此 p>=11 的整数零和合法输入只需一位额外三进精度。全称结论由正文证明，程序只做有限独立重放；未证明位长多项式构造长度或七元／任意合数的一位精度界。核验ID `prime-double-triple-invariant`。



本轮的原文阅读、外部文献及研究复盘见[重读二平均与统一证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_binary_source_reassessment_2026-09-11.md)。旧控制器仍保留为历史证书库；下文“最小未解”等表述描述各自的历史阶段，不代表当前状态。



此前结论：[Hecke与模符号路线的最后检验](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_final_hecke_audit.md)。该阶段没有得到任意p证明，暂停直接模形式方案。标准矩阵对任意奇p都有整数幺模共轭，旧指数p换基不是内在level；有根的第二算子与标准生成元没有共同正定Hecke星结构；整个下三角族不能从u非零到u=0；直接线性普通Manin编码被中心负号排除。此前将局部投影称为全局Eisenstein／Steinberg分量、将数字算子称为已实现T_3、将删点置换放入PGL2自然位置表示的说法已撤回。[修订接口页](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_iwahori_hecke_modular_interface.md)保留正确恒等式及历史实验，原稿已存档。ID `final-hecke-manin-audit`；旧核验ID仅证明有限代数恒等式。该阶段最小未解为71，现由上述直接证明覆盖。



此前路线复盘：[停止局部拼接，返回二维除法结构](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_route_reassessment_2026-09-11.md)。它记录载体路线的局部成果与全局困难；其中后来提出的直接Hecke／Manin主线现由上面的最后检验取代。弱的输入相关终端覆盖仍开放，但尚无分支提升定理或全局下降量。仿射交换子理想、参数周期刚性、混合迹零条件归约继续保留各自已经证明的范围。



结构结果：[载体扫掠催化器](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_carrier_sweep_catalyst.md)。r个三重块与一个载体各交换一次，始终得到1/3乘整数幺模矩阵；r=2恰恢复七元Artin中心，r=3则在固定十位置窗口中产生24个正向幺幂，其中12个具有同长度正向逆。四个固定共轭根显式给出E12(36)、E13(96)、E21(720)、E31(2160)，进而包含E3(4320^2 Z)，所以局部群的算术有限指数已经证明。更进一步，根约化与至多三次扫掠的精确有理锥证书证明：任意三个三重块加一个载体都能在这十个原位置内有限步产生叶／载体或叶／叶碰撞，不要求局部G条件，也不依赖p。固定窗口的外部耦合是以局部均值为中心后消失的1-coboundary。其全局拼接边界和路线降级见上面的最新复盘。ID `carrier-sweep-catalyst`、`carrier-catalyst-local-descent`。



最新终端化简：[等载体形式冻结定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_equal_carrier_formal_freezing.md)。在D_r=(u_1^3,...,u_r^3,a^2)中，形式交换群显式包含左上SL_(r-1)(Z)；任意合法素数核先以SL把叶差化成单gcd坐标，做一次真实等载体交换后，新叶差gcd自动整除新基值，再用第二个SL便产生零叶块。有限域中唯一避开零叶超平面的轨道是q|3r+2时的常值直线，素数维数下它恰为非法方向。因此形式轨道终端已闭合。正文同时证明正向局部化锥障碍：任何不依赖未参与叶的正向输出行只能有非负叶系数，故不能直接实现平衡SL剪切。剩余目标必须使用全局边界的状态相关抵消，或直接命中零叶。ID `equal-carrier-formal-freezing`。



最新完整结果：[59元判据与结构总结](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_fifty_nine_arithmetic_complete.md)。一次额外原子库给出正向种子，33节点无环逆证书经仿射消元产生上下三进根，21个Schreier回路实现共轭Gamma_0(59)，独立折叠60陪集并接九元终端。59已加入因子闭包，最小未解维数更新为71。入口 `python work/run_verifications.py --id n59-complete`。此后主线停止逐素数推进，转向统一的非分裂素数种子定理。



17至59证书中可预测与不可预测的部分见[非分裂素数结构综合](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_nonsplit_prime_structure_synthesis.md)。根提取、尖点、Schreier消元与终端已有统一公式；未统一的是原位置返回半群中正向可逆种子的存在。下一阶段优先研究PGL2(F_p)非分裂三阶轨道的p+1到p位置商实现，避免继续逐素数搜索。



备选条件归约：[混合单点迹零返回控制器](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_mixed_singleton_controller.md)。令B为不超过(p-1)/2且不等于3、5的素数乘积，两个显式返回R_0与R_(1/(10B))一旦能在原p个位置实现，其周期、仿射交换子和显式Bezout恒等式便统一产生U(R)、L(pR)；固定因子15补齐3、5，对角吸收随后覆盖全部合法方向并接九元终端。两个目标已有共同严格正三进运输和副本实现。这条特定充分路线内部只差两运输的原位置分解；该条件不等价于一般种子存在，也不排除条件宏、奇异降秩或直接终端命中的其他证明路径。ID `mixed-singleton-conditional-controller`。



原位置分解的精确半群方程、两个返回的相对混合器、现有返回库二因子边界、非分裂平移闭路边界及叶数字控制器边界见[原位置分解前沿](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_original_position_factorization_frontier.md)。这些有限阴性结果用于收缩统一语法，不构成不可达性证明。



最新：[53元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_fifty_three_arithmetic_complete.md)已登记n53-complete并加入已解因子目录。74节点正向逆证书、三进根和20个Schreier回路消元给出共轭Gamma_0(53)，独立折叠54陪集并重放九元终端。最小未解维数更新为59；下文更早的未解起点属于历史状态。全部素数统一证明仍开放。



最新结构：[Reynolds半群、交叉计数与判别式对偶](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_reynolds_hecke_hodge.md)。原子生成代数对全部n>=5已是整个End(V)，因此线性化不能区分五元失败；固定1／3重数的整数运输表则精确参数化普遍可执行层，自动关于加权伴随封闭，并有有限Hecke角解释。能量Hodge对偶在危险p处交换Iwahori边两侧，把合法方向送进非法余类，解释自然伴随取逆的障碍。已给出无隐藏宏适用条件的运输半群终端猜想，未新增已解维数。ID `reynolds-hodge-structure`、`contingency-layer-semigroup`。



当前素数路线总览：[证明路径与剩余猜想](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_prime_proof_roadmap.md)。按已解无限族、统一标准核入口、正向种子、同余生成与终端分层，分别列出强资源猜想、有限Schreier目标及更弱的合法单轨道目标，避免把充分条件当成必要条件。该页主体写于47元完成后；后续53、59已经补齐，当前最小未解为71。



最新完整结果：[47元判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_forty_seven_arithmetic_complete.md)。一个固定宽度一尖点词与两个伸缩校正给出E12(Z[1/6])及E21(47Z[1/6])；18个完整Schreier生成元逐个正向消元，实现共轭Gamma_0(47)，独立折叠为48陪集。统一桥与Bezout输送完成全部47元输入。47已进入因子闭包，最小未解维数现在为53。入口 `python work/run_verifications.py --id n47-complete`。



最新一般定理：[局部化Iwahori生成与通用尖点公式](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_localized_iwahori_generation.md)。对任意素数p，若正向群提供Z[1/(p-1)!]上的上根、p倍下根及相应对角单位，则统一标准代表和三因子消元证明包含Gamma_0(p)。另有任意奇次三进返回产生宽度一尖点的恒等式。剩余统一任务是这些资源的原维数物理实现，非再次逐素数猜同余群。



此前：[正向根群饱和与统一素数策略](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_positive_root_saturation.md)。一般迹根引理将逆元构造化为一个线性有理方程；固定三层证书已让旧167个B47宏全部获得正向逆，连同新增对合共170个。原Q(sqrt89)共轭目标已有57次模板的正向实现；整数换基后正向群包含E12(47Z[1/6])、E21(47Z[1/6])两整族。该阶段未完成的同余包含已由上面的n47-complete补齐。独立入口 `python work/run_verifications.py --id b47-root-activation`，不运行发现搜索。



该页同时给出统一素数猜想的准确形式：正向群包含共轭Gamma_0(p)即足够，由同一个Bezout公式收尾。全部p=1 mod3素数与合数归约已经统一；剩余难点是p=2 mod3的普遍正向生成，不是逐素数重做终端分类。



此前47元进展：[额外原子平均、正向对合与平移根群](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_b47_extra_atom_and_adjoint.md)。一次额外预备三平均产生三个新对合，并使标准A0等六个旧宏获得正向逆；固定词进一步生成全部U(47t)、t属于Z[1/6]，为后来n47-complete提供种子。入口 `python work/run_verifications.py --id b47-extra-atom-involutions`。



同页给出倒序平均的能量伴随接口：旧167库只有15个反向模板通过全参数适用域，均未新增宏。一般同型对合的两两乘积还落在同一分裂环面，不能仅靠该族对合推断模群有限指数。



最新统一工具：[全局谱平衡与周期判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_projective_spectral_balance.md)。Newton多边形与Kronecker定理将任意秩有理宏的有限射影阶，等价为半单性、实谱等模及一组特征系数整数性；Ad表示给出给定矩阵的多项式时间分圆验证算法。它不解决宏词的存在性，最小未解仍为47。



[47元当前库周期边界](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_b47_cycle_frontier.md)精确排除167模板中长度至多4的有限周期，以及全部j>=0的A0^jBC。四因子部分用整数模筛选，737665600组合仅3896个需要完整整数复核。该排除不延伸到更长词或其他宏库。



最新一般结构：[等值载体与二进重分组](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_paired_carrier_reset.md)。全部n=3r+2、奇数r>=5的合法状态可进入二重等值载体核；一个4r-3步的原维数宏给出W=2V、V属于GL_r(Z[1/3])，坐标和差分理想都恰乘2。单独载体交换的标量周期被奇偶不变量排除，新宏的全局周期仍未证明。入口 `python work/run_verifications.py --id paired-carrier-two-adic-reset`，最小未解维数仍是47。



最新：[四十一元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_forty_one_arithmetic_complete.md)。21个通用宏、10个正向三因子对合和10个整数词给出完整42陪集的共轭Gamma_0(41)，唯一合法尖点归零。41已加入因子闭包，最小未解维数现在为47。入口为 `python work/run_verifications.py --id n41-complete`。



[有限模调度的高度边界](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_modular_height_barrier.md)给出一个统一精确族：全部指定非三剩余类和G保持不变、实能量下降，但本原整数高度按3^(2h)增长。它不否定已证的模调度桥，说明终止还需完整操作词的实／三进联合控制。



统一接口：[有限模正向控制与二例外归约](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_two_carrier_modular_bridge.md)。对全部n>=17且n=5 mod6，包括合数，直接用混合好划分、双载体有限模调度及合法n-2元调用进入(u^(n-2),a,b)核；不需安全能量下降或因子归纳。形式逆只在有限模数上正向化，不能据此声称核必终止。入口为 `python work/run_verifications.py --id two-carrier-modular-bridge`。



再用一步真实三平均可安全进入标准B_n，故这个n族的多危险素数标准核接口也已闭合。其一般原则是：全域可执行且行列式为三进单位的正向宏，与形式群在所有非三有限商上轨道相同；精确归零仍需另证。



此前：[二十九元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_twenty_nine_arithmetic_complete.md)。18个通用宏、9个三因子正向周期和7个整数词给出共轭Gamma_0(29)的完整30陪集证书，唯一合法尖点可归零。29已进入因子闭包。入口为 `python work/run_verifications.py --id n29-complete`，不运行浮点发现搜索。



无限族：[全部p=1 mod3素数的完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_split_prime_gaussian_controller.md)。原p个位置上的高斯周期层提供全局正向标量循环；一个范数一分圆单位保证单位剪切，再由整数仿射格正规形完整归零。所有这类素数及其因子闭包已解决，包含31、37、43、61、97等。结合29、41元证书，剩余统一问题归约到p=2 mod3、从47开始的素数。核验入口 `python work/run_verifications.py --id split-prime-gaussian-controller`。



此前原维数进展：[平坦核形式群的统一算术性](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_flat_star_arithmeticity.md)。所有p>=13的素数核可进入同一个一／二载体框架；显式幺幂与高秩初等同余群定理证明其形式群整数部分有限指数。模2和模p的第一层联合像及终端代表也已统一。该一般框架的整体正向实现仍开放；29元后来由独立三因子周期证书解决。



[置换剩余像与局部耦合](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_permutation_shadow_entanglement.md)证明：九十一元旧21504容器严格大于特定宏群，新的必要容器指数为43008。对应紧模曲线有无分歧二重覆盖和Jacobian二阶线丛解释。旧容器及其有限搜索标签完整保留。



最新结构定理：[数字算子的完整同余群](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_digit_congruence_group.md)。平衡剪切与置换恰生成全部整数保和／保常值群；加入数字算子后，群恰为模n倍率属于3的循环子群的同余群，并有显式分裂扩张和全部有理射影轨道分类。所有合法方向只有一个轨道，但正向实现仍使用三份复制。入口为 `python work/run_verifications.py --id balanced-digit-congruence-group`。



此前结果：[一次三份复制稳定化](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_one_tripling_stabilization.md)。所有 $N\ge9$ 且 $3\mid N$ 的维数已无条件解决，包括含当前未解素数47的141元；任意合法有理输入只需复制三份即可归零。证明把离散梯度／Hilbert 90、真实副本剪切与整数仿射格轨道分类接起来。原维数复制消去仍开放。入口为 `python work/run_verifications.py --id one-tripling-stabilization`。



其他AI结构图景的最新复核见[局部到整体与数域边界](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_structural_picture_audit.md)：保留原稿，纠正合法域不能单独决定高次level、数域扩张不改变固定输入可达性、内容理想不能替代R加法模等问题。



该复核第11节记录29元原1195模板的周期边界：没有二因子有限周期，且所有指数j>=0的A^jB均被排除。新完整证书使用三个不同因子，因而不与旧边界冲突。



一般结果：[任意维数严格归约到素数](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_all_dimensions_to_primes.md)。全部合数的接口已闭合，原猜想等价于仅证明全部素数p>=7。当前结合分裂素数族与29、41元基例，已解所有n>=7且素因子属于2、5、11、17、23、29、41或p=1 mod3的维数，并另有全部三整除维数。入口为 `python work/run_verifications.py --id even-prime-power-halving --id all-dimensions-prime-reduction`。



最新一般突破：[奇数合数的乘法闭包](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_odd_composite_factor_closure.md)与[25元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_twenty_five_arithmetic_complete.md)结合后，全部奇数n>=7已严格归约到全部p>=7素数。当前已解P={7,11,13,17,19,23}的任意乘积和素数幂，再乘任意三幂、五幂都已解决，包括25、35、49、77、91、121、125等无限族。入口为 `python work/run_verifications.py --id n25-complete --id odd-composite-factor-closure`。



此前该证明先覆盖8整除维数；最新的低二进重数桥已将v2=1、2也接入因子归约，所以现在允许任意二幂因子。



此前[二例外因子桥](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_prime_first_factor_reduction.md)的最优准备步数结论仍保留，构造已推广到d+2例外核心。剩余统一任务是素数核的正向可达性。



现代框架的主线复核与可执行定义见 [Modern Frame 严格化契约](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_modern_framework_review_and_contract.md)；奇素数维数的策略限制见 [子问题调用下界](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_subproblem_prime_obstruction.md)。



项目背后的统一结构猜测见[局部算术轨道图景](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_structural_picture_conjecture.md)：它区分已证的同余子群样本、因子归约的组合接口，以及尚待证明的正向算术轨道与终端覆盖。



此前基例：[二十三元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_twenty_three_arithmetic_complete.md)。三个固定原子宏生成共轭 Gamma_0(23) 的指数24充分子群。入口为 `python work/run_verifications.py --id n23-complete`；原固定词证书保持可复现。



同轮完成：[十九元及其三进塔](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_nineteen_arithmetic_complete.md)，通过通用十五元调用生成指数20充分子群。其内部子问题路径允许依赖参数，与二十三元的固定原子词证书不同。



[素数维数与同余子群的准确关系](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_prime_congruence_structure.md)给出一般p进稳定子定理和真实循环的尺度约束，不能据已解例子断言所有素数都自动生成足够大的群。整系数宏编译器在搜索前加入重数与支撑格缓存，并与旧版95个十七元矩阵逐项对照。



此前完成：[十七元及其三进塔](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_seventeen_arithmetic_complete.md)。固定原子逆词给出共轭 Gamma_0(17) 的指数18充分子群，独立入口为 `python work/run_verifications.py --id n17-complete`。



发现方法见[参数无关子问题模判据与范数环面](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_universal_subproblem_lattice.md)：任意参数维数的模板合法性可用局部化整数模包含判定。该页保留旧库与局部调度阶段，当前完成状态以上面的十七元定理为准。



此前的一般族：[全部二三光滑维数的完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_two_three_smooth_complete.md)，涵盖所有 n=2^a·3^b≥7。独立入口为 `python work/run_verifications.py --id two-three-smooth-complete`。



此前完成：[十四元及其三进塔](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_fourteen_complete.md)。[图论核心定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_blocker_graph_core.md) 同时将一般安全终端的重复值下界提高为 n-d-2。核验入口为 `python work/run_verifications.py --id blocker-graph-safe-core --id n14-complete`。



此前完成：[十五元及其三进塔的完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_fifteen_via_subblocks_complete.md)，通过模8调度调用十二元和十元子问题。[偶维 B 核减半桥](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_even_kernel_halving_bridge.md) 仅提供核内接口，十四元高维部分由最新证明补齐。入口为 `python work/run_verifications.py --id n15-via-subblocks-complete`。



此前完成：[十二元及其三进塔的完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_twelve_arithmetic_complete.md)。真实正向宏含共轭于 Gamma_0(8) 的指数 12 子群，唯一合法尖点可终止。独立核验入口为 `python work/run_verifications.py --id n12-complete`。



进一步完成：[十八元及其三进塔](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_eighteen_via_twelve_complete.md)，通过可解十二元子块和重数配对归零。B21 搜索已改用[整数状态引擎](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_b21_integer_search_optimization.md)，同样八进程约 11 秒完成。



## 从哪里开始



1. 先读[统一素数证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_prime_double_triple_invariant.md)及[本轮复盘](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_binary_source_reassessment_2026-09-11.md)，再按需要查阅 [`outputs/triple_average_research_handoff_2026-09-09.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_research_handoff_2026-09-09.md)中的历史结构。

2. 再读 [`outputs/triple_average_research_corrections.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_research_corrections.md)，避免继续使用已经撤回或修正的旧结论。

3. 用 [`outputs/triple_average_verification_guide.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_verification_guide.md) 查找每项结论对应的文档、脚本、命令、预期输出和证据边界。

4. 机器可读映射位于 [`work/verification_manifest.json`](../sources/work/document_reorganization_20260915/originals/work/verification_manifest.json)，统一入口为 [`work/run_verifications.py`](work/run_verifications.py)。



计算资源使用、性能剖析和九十一元 `24/24` 有限深度覆盖见 [`outputs/triple_average_computation_performance_audit.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_computation_performance_audit.md)；外部减暴力建议的逐项核对见 [`outputs/triple_average_search_optimization_review_2026-09-09.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_search_optimization_review_2026-09-09.md)。



标准核接口、自守/adelic 路线与 n=12 首个二维核实验见 [`outputs/triple_average_kernel_interface_and_automorphic_route.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_kernel_interface_and_automorphic_route.md) 和 [`outputs/triple_average_b12_kernel_experiment.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_b12_kernel_experiment.md)。



统一的现代结构语言见 [`outputs/triple_average_unified_modern_framework.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_unified_modern_framework.md)：将状态视为有向重写纤维，把三平均视为 A2 投影，并用带适用域的有向范畴组织跨核操作。只有具有正向逆词的部分才构成群胚。主文件已重写，原稿完整存档在 outputs/history/。



最新的可执行统一接口见 [`outputs/triple_average_template_compiler_and_torus.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_template_compiler_and_torus.md)：用 Smith 格判据编译参数无关子问题调用，并用虚二次范数环面组织 B17 的行列式 3 宏。



任意 \(q\)-平均的根格必要条件、原子秩与宏秩区分、\(S\)-算术控制器猜想见 [`outputs/triple_average_q_average_arithmetic_geometry.md`](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_q_average_arithmetic_geometry.md)。



从本目录运行：



```text

python work/run_verifications.py --list

python work/run_verifications.py --profile smoke

python work/run_verifications.py --profile core

```



`full` 档包含九十一元深度四、cusp 29 深度五及 B12/B15/B18/B21 的有限实验，会运行数分钟。新增标准接口、宏族和 theta 格对应见 [三进扩张修复](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_carry_repair_and_arithmetic_interface.md)；审核修订见 [audit 修订记录](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_audit_resolution_2026-09-09.md)。单项核验可用 `python work/run_verifications.py --id <ID>`。



## 目录约定



- `outputs/`：证明、综合、勘误、交接和验证指南。最新交接稿与勘误优先于早期探索稿。

- `work/`：验证证书、有限实验、搜索程序、辅助模块和历史缓存。其内部说明见 [`work/README.md`](../sources/work/document_reorganization_20260915/originals/work/README.md)。



现有文件保持原位，以免破坏旧文档中的路径和历史可追溯性。文件名前缀只能表示作者当时的用途；一个 `verify_*` 文件是否构成证明证书，必须以验证清单中的 `evidence_level` 和 `evidence_scope` 为准。


����߽磺�����ഢ���ƽ��У�v=0��1��ֱ�ӽ�������alpha=p-2ʱ�������޵���������壻��˶�����հ�������ȱ�ڡ�


2026-09-12形状势的文献接口：[零和组合文献接口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_shape_potential_literature_interface.md)已阅读Grynkiewicz 2006计数定理、2007逆EGZ及2011 Graham结构。它们支持“失败池低支撑/高重桶”方向，但仍需原位置保护与整数返回宏；不宣称已解决全局终止。

旧 single-value-zero-sum-conjecture 已被 p=13、0^32 1^4 2^4 否定；现有核验改检查反例、最优界 N-floor((p-1)/3) 和三步极端族，不再使用打印占位命令。

EGZ截断分类已更正：对任意 N>=2p-1，无混合p项零和时，至多两个重桶；双重桶覆盖全池，单重桶外的至多p-1个例外必须零和自由。

撤回不必要的 N<4p 上限；正确分类对任意 N>=2p-1 成立。

<!-- END SOURCE doc-12f1160dea79 -->

---

<a id="doc-7b5914820386"></a>

## 原文导签：有限步平均研究

来源：`work/document_reorganization_20260915/originals/README.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-7b5914820386 -->
# 有限步平均研究

更新：2026-09-15。当前工作是**整理和改进素数平均证明**；合数研究保留原进展，本轮暂停推进。

对奇素数 p，最优最终阈值已证明为 N(p)=2p+1；二平均 N(2)=4。n 在阈值以上时，非全等有理输入经原位置 p 平均可达全等，当且仅当中心化、本原化后的差分 gcd 是 p 的幂。只有 p 不整除 n 时才能简写成 G=1。

## 从这里开始

| 需要 | 入口 |
|---|---|
| 新 AI 接手／理解当前定理 | [素数证明入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/README.md) |
| 完整证明链与各维数覆盖 | [总证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/proof.md) |
| 统一代数工具与真正的几何结构 | [通用引理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/arithmetic_toolkit.md) · [模曲线与标记格](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/geometry.md) |
| 阅读记录、证明证据、独立审核 | [本轮核验说明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/verification.md) |
| 合数的现有成果与 GRH 条件 | [合数交接](../sources/work/document_reorganization_20260915/originals/outputs/general_k_three_tasks_progress_20260915.md) |
| 三平均直接证明、算法和其他主题 | [成果索引](../sources/work/document_reorganization_20260915/originals/outputs/README.md) |
| 查询曾试过什么 | [历史路线账本](../sources/work/document_reorganization_20260915/originals/outputs/research_routes_history_20260915.md) · [原根进展日志](../sources/work/document_reorganization_20260915/originals/HISTORY.md) |

素数证明无条件，但引用已审核的 Morris/Serre 定理，且九偏移部分含完整有限参数证书。尚未证明可变 p、n 下的统一多项式操作长度，也未解决一般合数元数的最优最终阈值。旧历史文稿的“未解”不覆盖当前已完成结论。

## 核验入口

在项目根目录执行：

```text
python work/run_verifications.py --profile prime-proof
```

这是素数主线的选定核验集，包含最终独立证书检查；PASS 的证明范围以[注册清单](../sources/work/document_reorganization_20260915/originals/work/verification_manifest.json)为准，不能代替正文的一般量词或外部定理。其他脚本见 [work 索引](../sources/work/document_reorganization_20260915/originals/work/README.md)。

## 文档维护

当前定理和阅读顺序集中维护，技术附录保留原位置不改名；历史过程归档，不再向两个 README 逐条追加进展。新结果必须区分“完整定理／有限证书／公式核验／探索”，并更新相关依赖与证据边界。

<!-- END SOURCE doc-7b5914820386 -->

---

<a id="doc-03c850066dd0"></a>

## 原文导签：成果与研究索引

来源：`work/document_reorganization_20260915/originals/outputs/README.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-03c850066dd0 -->
# 成果与研究索引

2026-09-15整理。当前任务：素数平均证明的整合和改进。先按主题选择入口；旧研究过程已移入同目录的[历史路线账本](../sources/work/document_reorganization_20260915/originals/outputs/research_routes_history_20260915.md)，原技术附录路径保持不变。

## 素数平均：完整最终阈值

[主入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/README.md) → [总证明与覆盖表](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/proof.md) → [通用算术引理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/arithmetic_toolkit.md) → [几何解释](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/geometry.md)。

全部奇素数 p 有 N(p)=2p+1，N(2)=4；阈值以上判据为中心化、本原化后的 G 是 p 幂。两条偶数边界、九个低偏移和全部旧 dₚ 尾部缺口均已完成。不要据旧专题中的阶段状态重新开启这些定理。

最新整理把二进补充所用倍率的扩环正式并入[九偏移第6节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)。无条件结论仍使用 Morris/Serre，有限参数证书仍是证明的一部分。[本轮阅读、核验与维护记录](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/verification.md)说明实际核对范围。

## 三平均：独立直接证明和算法

- [双三重值任意维数直接证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_all_dimensions_double_triple_invariant.md)：n≥11 的初等主证明，接7、8、9、10元基例得 n≥7；不依赖上述一般算术群证明。
- [二平均原文复核](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_binary_source_reassessment_2026-09-11.md)：直接方法的来源、实际读过的原文和误用边界。
- [序列长度研究](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_sequence_length_analysis.md)：区分数值能量界、固定 n 的位长界和未证的可变 n 统一界。
- [算法测试集](../sources/work/document_reorganization_20260915/originals/outputs/averaging_algorithm_benchmark.md)：已知可达但可能难于提取路径的输入；搜索失败不代表反例。

旧“17到59的种子／非分裂／仿射／Hecke”研究按[历史路线表](../sources/work/document_reorganization_20260915/originals/outputs/research_routes_history_20260915.md)查找。其方法障碍可能仍有意义，素数平均可达性定理本身已不再开放。

## 合数元数：成果保留，另有未解范围

当前交接为[三项任务的完成范围和剩余](../sources/work/document_reorganization_20260915/originals/outputs/general_k_three_tasks_progress_20260915.md)。本轮不推进这些任务，不改变用户此前允许采用 GRH 的决定。

| 已有结果 | 条件与入口 |
|---|---|
| 所有平方元数 t² 在 t²+t+1 元完整成立 | [GRH阶段定理](../sources/work/document_reorganization_20260915/originals/outputs/general_k_grh_stage_and_remaining_tasks_20260915.md)；充分大参数另有无条件结果 |
| 2、3的全部幂达到最早临界点 | GRH 下；见上述最新交接，不能称为全部后续维数的最终阈值 |
| 任意整数 k≥2 的 2k+1 端点 | [偶元数补齐](../sources/work/document_reorganization_20260915/originals/outputs/even_arity_all_endpoints_completion.md)，接已证奇元数结果；无条件 |
| 奇素数幂的全部奇数 2k<n<3k | [奇合数区间与块均值转译](../sources/work/document_reorganization_20260915/originals/outputs/odd_composite_coprime_middle_band_completion.md)；无条件 |
| 十平均十六元固定六步网络及推广族 | [固定网络](../sources/work/document_reorganization_20260915/originals/outputs/ten_average_sixteen_and_dyadic_network_family.md)；无条件 |
| 任意元数的已知宽尾部 | [一般线性阈值](../sources/work/document_reorganization_20260915/originals/outputs/arbitrary_arity_linear_threshold.md)，不等于最优阈值 |

定义 M、H、N 及原猜想的历史来源见[全局状态](../sources/work/document_reorganization_20260915/originals/outputs/averaging_global_status_20260912.md)和[合数临界猜想](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md)。两篇日期较早，以新交接判断其开放范围。

## 证据与历史

[素数核验说明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/verification.md) · [机器依赖图](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/proof_map.json) · [全项目核验注册](../sources/work/document_reorganization_20260915/originals/work/verification_manifest.json) · [此前阅读日志](../sources/work/document_reorganization_20260915/originals/outputs/research_reading_log_20260915.md) · [原根 README 历史](../sources/work/document_reorganization_20260915/originals/HISTORY.md)。

符号：当前 p 是平均元数，n 是位置数。很多旧 triple_average 文件的 p 是位置数，引用公式前必须检查。

<!-- END SOURCE doc-03c850066dd0 -->

---

<a id="doc-436d3ed577dd"></a>

## 原文导签：B_n 参数无关子问题模板编译器

来源：`work/document_reorganization_20260915/originals/outputs/ai3_bn_template_compiler.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/ai3_bn_template_compiler.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-436d3ed577dd -->
# B_n 参数无关子问题模板编译器

本文把“一个子问题能否对所有参数调用”写成可计算的 Smith/Fitting 条件，并把它和返回后的局部合法性分开处理。结果给出两个适用于任意 (n) 的真实模板族，以及以三幂维数为子问题的无穷多条严格规模递减调用边。

这里不重复十七元的具体宏，也不声称这些返回宏已经给出任意 (B_n) 的终止控制器。

令

\[
R=\mathbb Z[1/3],\qquad
\mathcal B_n(u,v)=(u^{n-4},v^3,w),\quad
w=-(n-4)u-3v.
\]

对整数 (N\ne0)，记

\[
N_{\ne3}=N/3^{v_3(N)}.
\]

## 1. 可编译模板的状态数据

一个参数无关调用模板包含：

1. 一个实际三平均前置词，把 (\mathcal B_n(u,v)) 送到若干坐标
   \[
   x_i=u+c_i d,\qquad d=(v-u)/m,
   \]
   其中 (m) 是三幂；
2. 一个大小为 (s) 的子块 (C)，其系数为 (c_1,\ldots,c_s\)；
3. 一个已证明完整判据的 (s) 元子程序；
4. 一个实际三平均后置词，把子块归并值与残余位置重新编译为
   \(\mathcal B_n(u',v')\)；
5. 输出矩阵 (M\in M_2(R))，使
   \[
   \binom {u'}{v'}=M\binom uv.
   \]

前置和后置词必须有独立的位置重数账本。下面的格判据只负责第 2 步的“可调用性”，不能凭形式矩阵取代真实词。

## 2. 秩一 Smith/Fitting 判据

令 (a=c_1)，并定义

\[
g=\gcd_i(c_i-a),\qquad T=\sum_{i=1}^s c_i.
\]

系数差模是秩一 (R)-模

\[
L=gdR.
\]

子块均值减去锚点值为

\[
\mu-(u+ad)=\frac{T-sa}{s}d.
\]

故得到如下精确的编译判据。

> **秩一模板定理。** 子块均值对全部参数 (u,v) 都属于原子块的仿射 (R)-格，当且仅当
> \[
> \boxed{(sg)_{\ne3}\mid T-sa.}
> \tag{2.1}
> \]

证明只需将上式除以 (gd)：所需系数属于 (R)，当且仅当

\[
\frac{T-sa}{sg}\in R.
\]

这正是 (2.1)。在一般二维参数模板中，同一个条件由差系数矩阵的 Smith 标准形给出；这里的唯一非零 Smith 不变量就是 (g)。

从 Fitting 理想的角度，局部障碍由有限商

\[
(L+R(\mu-x_1))/L
\]

在每个 (p\ne3) 的长度决定；其支撑恰是

\[
\frac{(sg)_{\ne3}}
{\gcd((sg)_{\ne3},T-sa)}.
\]

它为 1 当且仅当 (2.1) 成立。

若 (d=0)，子块本来全等。若 (d\ne0)，条件 (2.1) 等价于子块中心化本原化后的差分 gcd 只含 3。故当大小 (s) 已有完整 (G)-判据时，(2.1) 使该子程序可对**所有** (u,v) 调用。

## 3. 返回合法性的独立行列式条件

所有下文模板的输出矩阵有行和 1，可写成

\[
M=
\begin{pmatrix}
1-\lambda&\lambda\\
1-\beta&\beta
\end{pmatrix}.
\]

于是

\[
u'-v'=\det(M)(u-v),\qquad \det(M)=\beta-\lambda.
\tag{3.1}
\]

若 (M\) 的条目在 (R)，且其行列式在每个 (p\mid n, p\ne3) 处为单位，即若写成既约分数

\[
\det(M)=A/3^h
\]

后满足

\[
\boxed{\gcd(A,n_{\ne3})=1,}
\tag{3.2}
\]

那么合法 (B_n) 参数必被送到合法 (B_n) 参数。因为对每个这样的 (p)，式 (3.1) 不会使原来的非零 (u-v\pmod p) 消失。

条件 (2.1) 和 (3.2) 逻辑独立。前者只保证子问题对所有参数可调用；后者才保证该调用编译成的返回宏可以继续作用在合法 (B_n) 参数上。

## 4. 模板 T1：调用大小 n-4 的子问题

设

\[
r=n-4,qquad m=3^h\ge3,qquad r\ge m+1.
\]

先对 ((u^{m-1},v)) 执行一个大小 (m) 的真实三进网络，得到

\[
a=u+d,\qquad d=(v-u)/m.
\]

选择 (r) 元子块

\[
C_1=(a^{m-1},u^{r-m-1},v^2).
\tag{4.1}
\]

它的系数模式是

\[
(1^{m-1},0^{r-m-1},m^2),
\]

故 (g=1,T=3m-1)。判据 (2.1) 变为

\[
\boxed{r_{\ne3}\mid3m-1.}
\tag{4.2}
\]

在 (4.2) 下，若 (r) 元问题已经解决，归并 (C_1) 后尚余一个 (a)、两个 (u) 和 (w)。真实平均 ((a,u,u)) 后得到新的 (B_n)。输出为

\[
\begin{aligned}
u'&=u+\frac{3m-1}{mr}(v-u),\\
v'&=u+\frac1{3m}(v-u),
\end{aligned}
\tag{4.3}
\]

因而

\[
M_1=
\begin{pmatrix}
1-\frac{3m-1}{mr}&\frac{3m-1}{mr}\\
1-\frac1{3m}&\frac1{3m}
\end{pmatrix},
\qquad
\det(M_1)=\frac{n-1-9m}{3m(n-4)}.
\tag{4.4}
\]

分母只含 3 的部分之外来自 (n-4)，但 (4.2) 已保证在其非三素数处约掉；最终是否保持 (B_n) 合法性仍由 (3.2) 对既约形式检测。

位置账本如下：前置网络使用 (m) 个位置；子块使用 (m-1) 个新 (a)、(r-m-1) 个 (u)、两个 (v)；后置三平均使用留下的一个 (a) 和两个 (u)。最终正好保留 (r) 个子块均值、三个新 (v') 和原单点 (w)。

## 5. 模板 T2：调用大小 n-2 的子问题

仍令 (r=n-4)，并设 (m=3^h\ge3)、(r\ge m-2)。先对

\[
(u^{m-2},v^2)
\]

执行真实大小 (m) 三进网络，得到

\[
a=u+2d,\qquad d=(v-u)/m.
\]

选择 (s=n-2=r+2) 元子块

\[
C_2=(a^{m-1},u^{r-m+2},v).
\tag{5.1}
\]

其系数模式为

\[
(2^{m-1},0^{r-m+2},m),
\]

仍有 (g=1,T=3m-2)，故通用调用条件为

\[
\boxed{(n-2)_{\ne3}\mid3m-2.}
\tag{5.2}
\]

归并后，只留下一个 (a)、原单点 (w) 和 (n-2) 个均值。平均 ((a,\mu,\mu))，便重建 (B_n)。输出矩阵是

\[
M_2=
\begin{pmatrix}
1-\frac{3m-2}{m(n-2)}&\frac{3m-2}{m(n-2)}\\
1-\frac{2(n-4+3m)}{3m(n-2)}&
\frac{2(n-4+3m)}{3m(n-2)}
\end{pmatrix},
\tag{5.3}
\]

且

\[
\det(M_2)=\frac{2n-2-3m}{3m(n-2)}.
\tag{5.4}
\]

同样，必须对这个既约行列式应用 (3.2)，才可将它登记为保持合法域的返回宏。

## 6. 以三幂子问题为终端库的无穷递归边

已知所有 (3^e) 元问题都已解决。把它们作为子问题库，可得到两族完全符号化的调用边。

取 (m=3)。

**T1 族。** 令

\[
n=3^e+4,\qquad e\ge2.
\]

子问题大小为 (n-4=3^e)，所以 (4.2) 自动成立。由 (4.4)

\[
\det(M_1)=\frac{3^{e-1}-8}{3^{e+1}}.
\]

并且

\[
\gcd(3^e+4,3^{e-1}-8)=\gcd(3^e+4,28).
\]

因此 T1 是保持合法域的全参数返回宏，当且仅当

\[
e\not\equiv1\pmod6.
\tag{6.1}
\]

**T2 族。** 令

\[
n=3^e+2,\qquad e\ge2.
\]

子问题大小 (n-2=3^e)，故 (5.2) 自动成立。由 (5.4)

\[
\det(M_2)=\frac{2\cdot3^e-7}{3^{e+2}},
\]

并且

\[
\gcd(3^e+2,2\cdot3^e-7)=\gcd(3^e+2,11).
\]

因此 T2 是保持合法域的全参数返回宏，当且仅当

\[
e\not\equiv2\pmod5.
\tag{6.2}
\]

这两条结论都给出无穷多个 (B_n) 到一个严格更小、且已解决的 (3^e) 子问题的调用边，规模分别下降 4 和 2。

更一般地，固定任意三幂 (m)，将 T1、T2 分别作用于 (n=3^e+4)、(n=3^e+2) 时，子问题 Smith 条件自动成立。行列式的非三障碍完全落在固定常数上：

\[
\gcd(3^e+4,9m+1),
\qquad
\gcd(3^e+2,3m+2).
\tag{6.3}
\]

故每个固定 (m) 的可用指数集合都是可有效计算的周期同余集合。若该有限周期表存在一个安全余类，就立刻给出无穷模板族；(m=3) 的安全余类已由 (6.1)、(6.2) 明确给出。

## 7. 递归边的边界

这里“规模下降”只指调用的子问题从 (n) 降到 (n-4) 或 (n-2)。调用完成后，整体状态被编译回同一个大小的 (B_n)，并没有把整个 (n) 元问题缩到子问题大小。

因此，模板编译器生成的是带已解子程序的合法**自返回边**：

\[
B_n\xrightarrow{\text{调用已解 }s<n}B_n.
\]

要从这些边推出 (B_n) 完整定理，还须证明这些返回矩阵的半群对每个合法参数最终碰到终端，或把它们接到一个真正的尺寸缩减桥上。T1、T2 的行列式即使在实绝对值小于 1，也通常只把 (u-v) 乘以一个非零有理数，不能在有限步自动变为零。

也不能只检查 (2.1)。例如 (n=11,m=3) 的 T2 调用九元子问题满足 Smith 条件，但

\[
\det(M_2)=11/81.
\]

它在模 11 退化，会把某些合法 (B_{11}) 参数的模 11 差异消掉，所以不是保持合法域的返回宏。这是“子问题全参数合法”不足以推出“全局模板可重复”的明确反例。

## 8. 精确核验

[`work/verify_ai3_bn_template_recursion.py`](../work/verify_ai3_bn_template_recursion.py) 用 `Fraction` 检查：

- 48 个实际前置三进网络、抽象已证子程序调用和后置三平均的位置账本；
- 2,131 组秩一 Smith/Fitting 数据及仿射格整除条件；
- 91 个行列式局部单位判据，其中 27 个故意保留的非单位边界；
- T1/T2 三幂子问题无穷族的 128 个指数前缀，以及 (B_{11}) 反例。

输出：

```text
template real-network and 2x2 matrix checks: PASS 48
Smith/Fitting child-lattice checks: PASS 2131
away-from-3 determinant checks: PASS 91 nonunit cases 27
infinite-family and determinant-boundary checks: PASS 128
```

一般量词由第 2--6 节的符号推导给出。脚本属于 `symbolic-check` 与 `finite-sanity`，不证明返回半群的终止，也没有改动统一验证清单。

<!-- END SOURCE doc-436d3ed577dd -->

---

<a id="doc-51326f2bfdc0"></a>

## 原文导签：多危险素数三幂核的链间耦合与加权和转移

来源：`work/document_reorganization_20260915/originals/outputs/ai3_multprime_chain_report.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/ai3_multprime_chain_report.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-51326f2bfdc0 -->
# 多危险素数三幂核的链间耦合与加权和转移

本文只研究三幂分块核中的真实宏、局部非三素数见证和链间加权和转移，不处理十四元，也不声称已经得到任意核的终止算法。

设

\[
K_{\mathbf r}=\{(u_1^{r_1},\ldots,u_t^{r_t}):
 r_i=3^{k_i},\ \sum_i r_i u_i=0\},
\]

其中每个块 (i) 表示 (r_i) 个相同位置，值为 (u_i\in\mathbb Z[1/3])。对 (p\ne3)，定义块值的局部见证为

\[
W_p(u)=\{u_i\bmod p:1\le i\le t\}.
\]

称 (p)-见证存在，当且仅当 (W_p(u)) 至少含两个余类。由于 (r_i) 是三幂，所有 (r_i) 在模 (p) 下可逆。若展开状态的差分 gcd 为三的幂，则每个 (p\mid n, p\ne3) 都必须有这样的见证。

## 1. 等权三块合并

设三个块 (i,j,k) 的权重均为 (r)，值分别为 (a,b,c)。对每个偏移量 (0\le h<r)，选取这三个块在偏移量 (h) 的三个真实位置，执行一次三平均。共执行 (r) 次真实操作，得到一个权重 (3r) 的新块，值为

\[
m=\frac{a+b+c}{3}.
\]

位置账本是：三个输入块的 (3r) 个位置全部被使用；每次操作使用三个位置并产生三个 (m) 位置；输出是一个 (3r) 重的 (m) 块。加权和严格保持：

\[
r(a+b+c)=3r m.
\]

对固定 (p\ne3)，合并后的块值集合为

\[
\{m\}\cup\{u_\ell:\ell\notin\{i,j,k\}\}.
\]

因此有精确的安全判据：

> **等权合并见证判据。** 合并三块对 (p) 保持见证，当且仅当上述输出集合在模 (p) 下不全相同。

等价地，合并会破坏 (p)-见证，当且仅当所有未选块值都同余于某个 (d)，且

\[
a+b+c\equiv3d\pmod p.
\]

这个条件必须对每个危险素数分别检查，不能把不同素数的条件简单相乘。

存在真实且合法的破坏见证例子。取 (n=7)、七个权重都为 1，状态

\[
(1,1,5,0,0,0,-7).
\]

它总和为零，差分 gcd 为 1，且模 7 非全同余。合并前三个位置后得到

\[
\left((7/3)^3,0,0,0,-7\right).
\]

清除三进分母后，差分 gcd 变成 7。因此等权进位不是无条件的安全操作；必须使用上面的逐素数判据，或使用已经登记的危险支持集排除条件。

## 2. 任意不同三幂权重块的真实交换

取两个块，设大块权重为 (R)，小块权重为 (q)，并令

\[
R=sq,\qquad s=3^h>1.
\]

大块值为 (u)，小块值为 (v)。把小块的 (q) 个位置逐个作为种子；对每个种子，从大块取出 (s-1) 个位置，用标准三进扩张树把种子扩张成 (s) 个位置。每个种子使用

\[
\frac{s-1}{2}
\]

次真实平均，共使用

\[
q\frac{s-1}{2}=\frac{R-q}{2}
\]

次真实操作。大块还剩 (q) 个旧 (u) 位置。于是位置级输出账本为

\[
\begin{array}{c|c|c}
\text{输出块}&\text{位置数}&\text{输出值}\\ \hline
\text{原大块位置}&R& m=((s-1)u+v)/s\\
\text{原小块位置}&q&u
\end{array}
\]

即真实宏

\[
(u^R,v^q)\longmapsto(m^R,u^q),
\qquad m=\frac{s-1}{s}u+\frac1s v.
\tag{2.1}
\]

加权和恒等式为

\[
Rm+qu
 =q((s-1)u+v)+qu
 =Ru+qv.
\]

因此该宏可以用于不同链的块之间，而不要求任一条链单独加权和为零。

## 3. 对所有危险素数同时保持见证

交换宏 (2.1) 对每个 (p\ne3) 都保持非全同余见证，而且不需要分别为每个素数挑选交换边。

设交换后所有块值都同余于 (d\pmod p)。输出小块值是旧 (u)，故 (u\equiv d)。输出大块值满足

\[
s m=(s-1)u+v.
\]

由于 (s) 在模 (p) 下可逆，(m\equiv d\) 与 (u\equiv d) 联立得到 (v\equiv d)。其余未改变的块也都同余于 (d)，所以交换前所有块值已经同余。这证明了逆否命题：

> **跨链交换见证引理。** 若交换前对某个 (p\ne3) 存在至少两个块值不同，则交换后仍存在至少两个块值不同。该结论对所有 (p\mid n, p\ne3) 同时成立。

这里不要求 (p\nmid R) 或 (p\nmid q)，只要求 (p\ne3)，因为交换比例 (s) 是三幂。由此，交换宏比等权合并更适合作为多危险素数环境中的“安全耦合”操作。

## 4. 单位置载体交换

设有一个单独位置 (w)，以及一个权重 (r=3^h>1) 的块值 (u)。把单独位置作为种子，从 (r)-块中取出 (r-1) 个位置进行三进扩张树，使用

\[
\frac{r-1}{2}
\]

次真实平均，留下一个旧 (u) 位置。输出为

\[
(w^1,u^r)\longmapsto
\left(u^1,\left(\frac{w+(r-1)u}{r}\right)^r\right).
\tag{4.1}
\]

令 (d=u-w)，则新单位置仍为旧 (u)，新大块值为 (u-d/r)。因此

\[
d'=-\frac d r.
\tag{4.2}
\]

若还有其他块值 (u_i)，以新的单位置为参考，

\[
d_i'=u_i-u=d_i-d.
\tag{4.3}
\]

这正是三幂核中的局部多维减法公式。

载体交换也逐个保持所有 (p\ne3) 见证：如果输出全同余于 (c)，保留下来的单位置给出 (u\equiv c)，新大块值给出 (w+(r-1)u\equiv rc)，从而 (w\equiv c)。未改变块也必须同余，故输入本来已经全同余。

## 5. 链间加权和转移

把块索引划分为若干条链 (C_1,\ldots,C_m)，不要求每条链自身加权和为零。定义

\[
S_a=\sum_{i\in C_a}r_i u_i,
\qquad \sum_a S_a=0.
\]

若大块 (i\in C_a) 与小块 (j\in C_b) 进行交换，令

\[
\Delta=q(v-u),\qquad q=r_j.
\]

则

\[
S_a'=S_a+\Delta,
\qquad
S_b'=S_b-\Delta,
\tag{5.1}
\]

其他链和不变。也就是说，跨链交换把一份精确质量 (Delta) 从一条链转移到另一条链；总和恒为零。该转移量由实际选中的两个块值和小块权重决定，而不是任意可调参数。

如果恰好有

\[
\Delta=-S_a,
\tag{5.2}
\]

则链 (C_a) 被一次交换精确归零，非零链数量严格下降。这是一个可检验的链间终端判据。

更一般地，对链和平方势

\[
\Phi=\sum_a S_a^2,
\]

单次 (a,b) 交换满足精确恒等式

\[
\Phi'-\Phi=2\Delta(S_a-S_b)+2\Delta^2.
\tag{5.3}
\]

因此当

\[
\Delta\bigl(S_a-S_b+\Delta\bigr)<0
\tag{5.4}
\]

时，链和平方严格下降。条件 (5.4) 是一个真实可执行的局部下降判据。

## 6. 终止性的准确边界

式 (5.3) 尚不能给出一般终止定理。原因有两个：

1. 可用转移量只在集合
   \[
   \{r_j(u_j-u_i):i,j\text{ 属于不同链}\}
   \]
   中取值，不能任意选择。即使 (Phi>0)，也可能没有满足 (5.4) 的跨链边。
2. 交换包含除以 (s=3^h) 的步骤。若当前值分母只含 (3^K)，一次交换可能把分母高度提高到 (K+h)。因此把 (Phi) 乘以一个固定三幂后取整数，并不能形成已知的良序下降量。

可以使用如下条件势函数，但只能得到条件定理：

\[
\Psi=(z,\Phi),
\qquad
z=\#\{a:S_a\ne0\},
\]

先在满足 (5.2) 的交换中严格降低 (z)，否则在满足 (5.4) 且分母高度不增加的步骤中降低 (Phi)。要把它升级为全称终止定理，还必须证明：只要 (z>0)，总能找到一个保持局部见证的跨链交换，使 (z) 或该有界高度版本的 (Phi) 严格下降。目前没有这样的选择引理。

等权三块合并确实降低块数，但其局部见证可能被完全消除；跨链交换保持所有见证，却不一定降低块数或链和势。因此两类宏需要配合一个“安全合并或可下降交换”二择一引理，这正是多危险素数一般核的主要缺口。

## 7. 严格结论与未解决部分

本文得到以下可直接复用的命题：

1. 任意两个不同三幂权重块之间都有真实交换宏，操作数为 ((R-q)/2)；
2. 该宏精确转移链和 (q(v-u))；
3. 该宏对所有 (p\ne3) 同时保持非全同余见证；
4. 单位置载体交换给出 (d_j'=-d_j/r_j)、(d_i'=d_i-d_j)，并同样保持所有局部见证；
5. 等权三块合并的安全性有精确逐素数判据，但没有无条件安全性；
6. 链和平方势的变化式 (5.3) 给出可检查的条件下降。

尚未证明：

- 任意多链状态都存在满足 (5.2) 或 (5.4) 的交换；
- 允许等权安全合并和跨链交换后，块数必然有限步降到零和三幂终端；
- 动态三进分母高度可以和链和势联合形成良序；
- 多个危险素数的见证重置可以在合并失败时由统一的交换图控制。

因此本文是一个链间耦合接口和条件下降定理，不是一般 (K_{\mathbf r}) 的充分性证明。

## 8. 精确核验

脚本 [`work/verify_ai3_multprime_chain.py`](../sources/work/document_reorganization_20260915/originals/work/verify_ai3_multprime_chain.py) 只使用整数和 `Fraction`，包含：

- 19 个真实交换和单位置载体的位置账本；
- 43,784 个随机多危险素数局部见证保持检查；
- 823,536 个模 7 残基的等权合并判据穷举；
- 一个 (G=1) 但合并后出现 (p=7) 公因子的具体反例；
- 1,000 个链和转移及平方势恒等式检查。

运行输出：

```text
real exchange/carrier ledgers: PASS 19
simultaneous p!=3 witness preservation: PASS 43784
equal-carry safety criterion and p=7 counterexample: PASS 823536
chain-sum transfer identities and potential: PASS 1000
```

证据等级为 `symbolic-check` 加 `finite-sanity`。脚本不证明任意核的终止，也没有修改统一 manifest。

<!-- END SOURCE doc-51326f2bfdc0 -->

---

<a id="doc-1f9362671efe"></a>

## 原文导签：任意平均元数的线性阈值：非单位差分也是可执行资源

来源：`work/document_reorganization_20260915/originals/outputs/arbitrary_arity_linear_threshold.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/arbitrary_arity_linear_threshold.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-1f9362671efe -->
# 任意平均元数的线性阈值：非单位差分也是可执行资源

日期：2026-09-12。这里 \(q\) 是每次平均的位置数，不要求为素数或素数幂。本文在原位置给出统一证明；二平均副本归约不是本定理的前提。

## 1. 结果及当前边界

令
\[
P_q(n)=\{\ell:\ell\mid n,\ \ell\text{ 为素数},\ \ell\nmid q\},
\qquad d_q(n)=|P_q(n)|.
\]
非全等有理输入按项目约定中心化、清分母并本原化为整数零和 \(X\)，记 \(G=\gcd_{i<j}|X_i-X_j|\)。

**定理。** 对任意整数 \(q\ge3\)，只要
\[
\boxed{n\ge4q-1+d_q(n),}
\tag{1}
\]
便有
\[
\boxed{\text{有限步 \(q\) 平均可达}\iff \operatorname{rad}G\mid q.}
\tag{2}
\]
全等输入由空词解决。若输入本身为整数零和状态且合法，存在所有中间坐标均属于 \((1/q)\mathbb Z\) 的路径。路径只使用原来的 \(n\) 个位置。

因此，对每个平均元数都存在最终充分阈值，并有
\[
\boxed{N(q)\le4q+\lceil\log_2q\rceil+1\le5q\quad(q\ge3).}
\tag{3}
\]
二平均由已有定理给出 \(N(2)=4\)。

具体地，(1) 保证
\[
N(4)\le16,\qquad N(6)\le24.
\tag{4}
\]
结合[半块转译](../sources/work/document_reorganization_20260915/originals/outputs/composite_arity_four_six_transfer.md)的低维反例，以及[四平均七元](../sources/work/document_reorganization_20260915/originals/outputs/four_average_seven_complete.md)和[九元](../sources/work/document_reorganization_20260915/originals/outputs/four_average_nine_complete.md)的完整证明，得到
\[
7\le N(4)\le16,\qquad 9\le N(6)\le24.
\]
两种平均元数在各自候选临界线以上仍待补的是：

- 四平均：\(11,13,15\)；
- 六平均：\(11,13,14,16,17,19,20,22,23\)；十元已由[独立模5控制器](../sources/work/document_reorganization_20260915/originals/outputs/six_average_ten_complete.md)完成。

这不声称已分类四平均六元、六平均八元的全部可达状态；这些维数已有反例排除无条件的 \(G\) 充分性，但完整逐输入判据仍是独立问题。

## 2. 与旧证明相比，真正增加了什么

项目此前[素数元数的4p证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_four_p_threshold.md)在两处使用了“非零模 \(p\) 差分可逆”：选择均值可控的整数操作，以及处理三个重值。本轮给这两处补上完整的合数分支：

1. 差分不是单位时，按其与 \(q\) 的最大公因子配比，两种值本身就能组成非恒等整数平均。
2. 偶数元数下，两种配比可能给出同一中点。这是唯一的新碰撞类型；若不能直接避开第三个重值，则两个相邻差分为单位，旧顺序论证重新适用。

其余组合保护、初始化、系数打包和能量终止不需要平均元数为素数。EGZ 的一般整数版本也可由素数版本逐因子提升，下面给出证明。

所以素数性不是充分大维数结论的本质限制。有限环中的非单位并不只是缺少逆元：在平均问题里，它提供了有较小参与份数的精确混合比例。

## 3. 算术安全性与两个重值

在本轮构造中，不在每一步重新本原化。称整数零和状态 \(E\) **合法**，若它对每个 \(\ell\in P_q(n)\) 模 \(\ell\) 不全相同。对本原输入，这正好是 (2) 的右侧。

必要性沿用共同非零余类障碍：\(\ell\nmid q\) 时，平均保持模 \(\ell\) 的共同值；本原输入若 \(\ell\mid G\)，此共同值非零，不能达到零。

令
\[
H(E)=\{a:f_E(a)\ge q\}.
\]
构造保持
\[
E\in\mathbb Z^n,\quad \sum E_i=0,\quad E\text{ 合法},\quad |H(E)|\ge2.
\tag{5}
\]

安全性的三个工具如下，它们只使用 \(\ell\nmid q\)：

- 若一个被选实际值在未选位置仍有副本，则在“输出全部模 \(\ell\) 相同”的假设下，该实际值必等于共同余类。
- 若被选组只含 \(a,b\) 及一份第三值 \(x\)，而 \(a,b\) 都保留未选副本，输出全同余会再迫使 \(x\) 同余，故这种整数操作安全。
- 因 \(n>2q\)，每个危险素数至多有一个占据至少 \(n-q\) 位置的主余类，其非空例外集大小在2到 \(q\) 之间。从任意候选池中为每个尚可能被完整选中的例外集留出一个位置，至多损失 \(d_q(n)\) 个位置，就能保证其后所有 \(q\) 子集都安全。

例外集不能只有一个位置，因为零和与 \(\ell\mid n\) 会迫使该唯一例外也属于主类。

从 \(qX\) 出发，初值全部被 \(q\) 整除。旧初始化的证明仅需 \(n\ge d_q(n)+3q\)：已有两种重值时不操作；唯一重值足够多时平均其 \(q-1\) 份与一个不同值；否则在尚未改变的初值池中用安全操作制造新重值，必要时从 \(q+1\) 个候选中删一项来避开旧均值。没有重值时先做一次，再应用后一分支。总计至多两次。

这里初态没有重值时，第一次新均值最多出现 \(2q-1\) 次；它之外的全部位置未被改变，仍被 \(q\) 整除。保护后有 \(q+1\) 个位置时，若删去任意一项的均值都等于同一旧值，比较各和会强迫所有候选相同，与每值不足 \(q\) 份矛盾。

(1) 蕴含所需初始化容量。具体逐位置实现复用已经审定的初始化程序，但危险素数表改为“素数不整除 \(q\)”，不能继续用“素数不等于 \(q\)”。

## 4. 非单位差分混合引理

设两个不同的 \(q\) 重值为 \(a,b\)，并令
\[
g=\gcd(a-b,q)>1,\qquad k=q/g.
\]
则真实操作
\[
\boxed{(a^k,b^{q-k})}
\tag{6}
\]
的均值为
\[
b+\frac{a-b}{g}\in\mathbb Z.
\tag{7}
\]
它非恒等；\(1\le k\le q/2\)，两种值都留有未选副本，所以同时对所有危险素数安全。

若 \(f(b)\ge2q-1\)，操作后 \(b\) 仍有至少 \(q\) 份，且新均值不同于 \(b\)。因此直接保持 (5)。

反向交换两种配比得到
\[
c_1=b+(a-b)/g,\qquad c_2=a+(b-a)/g,
\]
满足
\[
c_1-c_2=(2/g-1)(a-b).
\tag{8}
\]
它们相等当且仅当 \(g=2\)，此时均为中点 \((a+b)/2\)。这是全部偶数碰撞例外。

## 5. 大背景值引理不再需要素数性

设 (5) 成立，\(n>2q\)，某个重值 \(b\) 有至少 \(2q-1\) 份，另一个重值为 \(a\)。若差分非单位，第4节直接继续。

以下设 \(\delta=a-b\) 为模 \(q\) 单位。对每个第三值 \(x\)，取唯一 \(0\le i<q\) 满足
\[
i\delta+x-b=0\pmod q.
\]
平均
\[
(a^i,b^{q-1-i},x).
\tag{9}
\]
操作是安全非恒等整数平均，\(b\) 仍有至少 \(q\) 份。如果新均值不等于 \(b\)，就保持 (5)。

因此，无继续操作时，每个第三值都必须是
\[
x=b-j\delta,\qquad 1\le j<q.
\tag{10}
\]
仅有 \(a,b\) 两值也不可能：合法性及 \(\gcd(\delta,q)=1\) 给出 \(\gcd(\delta,n)=1\)，零和则使 \(a\) 的重数被 \(n\) 整除，矛盾。

若 \(a\) 也有至少 \(2q-1\) 份，(9) 保留两个旧重值。若某个 \(x=b-j\delta\) 有至少 \(2q-1\) 份，分两支：

- \(\gcd(x-b,q)=1\)：用 \(x,b\) 调节一份 \(a\)，保留两个旧重值；
- \(\gcd(x-b,q)>1\)：用第4节的混合，保留背景 \(b\) 并制造不同新重值。

这补齐了旧证明隐含的“每个 \(j\) 都可逆”。因而没有继续操作时，可写成
\[
((b+\delta)^A,b^B,(b-\delta)^{c_1},\ldots,(b-(q-1)\delta)^{c_{q-1}}),
\tag{11}
\]
其中 \(q\le A\le2q-2,\ B\ge2q-1,\ c_j\le2q-2\)。完整等差结构与合法性给出 \(\gcd(\delta,n)=1\)。

令 \(S=\sum j c_j\)。若 \(S\ge q\) 且有 \(j\ge2\)，将负系数按降序排列，取总和首次达到 \(q\) 的前缀 \(j_1,\ldots,j_s\)，记 \(T=\sum j_i\)。有
\[
2\le s\le q-1,\quad T+s\le2q.
\]
后一个不等式来自 \(T\le q-1+j_s\)、\((s-1)j_s\le q-1\) 以及
\((s-1)(q+1-s)-(q-1)=(s-2)(q-s)\ge0\)。

取 \(t=T-q,\ z=q-s-t\)，平均
\[
(b-j_1\delta,\ldots,b-j_s\delta,(b+\delta)^t,b^z).
\tag{12}
\]
得到均值 \(b-\delta\)。位置数恰为 \(q\)，\(t\le q-2\)，背景至少留下 \(q\) 份。未选的 \(a,b\) 在每个危险素数下不同余，故此操作安全并保持 (5)。

若 \(S<q\)，零和给 \(n\mid A-S\)，但 \(0<A-S<n\)，矛盾。唯一剩余情形是只出现 \(j=1\)，并由零和得到
\[
\boxed{(\delta^A,(-\delta)^A,0^B).}
\tag{13}
\]
反复平均 \((\delta,-\delta,0^{q-2})\) 完成归零。整个背景引理对任意 \(q\ge3\) 成立。

## 6. 三个及以上重值：完整处理中点碰撞

### 至少四个重值

若任何两个重值的差分非单位，用 (6)，另外至少两个旧重值完整保留。

否则任取四个递增重值 \(a_1<a_2<a_3<b\)。用 \(a_1,a_2\) 的单位差分调节一份 \(a_3\)，即 (9) 型操作。新均值严格小于未参与的 \(b\)，且所有选中类型都保留副本，所以安全并保持 (5)。

### 恰好三个重值

排列为 \(a<b<c\)。若一对非单位差分的两种配比中至少有一个均值不等于第三个值，该操作就解决问题。

若有非单位差分但所有这些操作都撞上第三个值，(8) 迫使：
\[
q\text{ 偶},\quad a+c=2b,\quad
\gcd(c-a,q)=2,\quad
\gcd(b-a,q)=\gcd(c-b,q)=1.
\tag{14}
\]
理由：中点只能是三个值的中间值，所以任何非单位对都只能是两端；相邻差分若也非单位，其混合均值严格位于相邻两值之间，不会等于第三个值。

否则，三个差分全是单位。两种情况下相邻差分都为单位，于是：

- 存在低重数值 \(x<c\)：用 \(a,b\) 调节 \(x\)，新均值小于 \(c\)；
- 存在低重数值 \(x>c\)：用 \(b,c\) 调节 \(x\)，新均值大于 \(a\)；
- 没有低重数值且 \(a\) 多于 \(q\) 份：取一份 \(a\)，用 \(b,c\) 调节，新均值大于仍保留 \(q\) 份的 \(a\)；
- 对 \(c\) 多于 \(q\) 份同理。

最后只剩没有低重数值且 \(f(a)=f(c)=q\)。在 (14) 的中点情形，零和直接给 \(b=0,a=-c\)，已经是 (13) 的终端。在三个差分全为单位的情形，\(f(b)=n-2q\ge2q-1\)，调用第5节背景引理。

这样补齐的是全称的碰撞分类，不是有限 \(q\) 样本观察。

## 7. 恰好两个重值及一般 EGZ

设重值为 \(a,b\)。若有一个重数至少 \(2q-1\)，用第5节；否则各自最多 \(2q-2\) 份。

各预留 \(q\) 份。余下池至少有 \(d_q(n)+2q-1\) 个位置，每个实际值不足 \(q\) 份。再保护至多 \(d_q(n)\) 个位置，用 EGZ 选出 \(q\) 个和被 \(q\) 整除的位置。该操作安全、非恒等，并保留两个旧重值。

**EGZ 的一般整数版本为何可用：** 素数版本已有 Chevalley–Warning 证明。若 \(q=uv\)，在 \(2uv-1\) 个整数中，反复应用 \(u\) 的版本取出 \(2v-1\) 个不交 \(u\) 元组，各组和被 \(u\) 整除。最后一次取组前恰好还至少有 \(2u-1\) 项。把各组和除以 \(u\)，应用 \(v\) 的版本选择 \(v\) 组，其并集恰有 \(uv\) 项且和被 \(uv\) 整除。对素因子个数归纳即得任意整数 \(q\)。

程序沿用基数／余数动态规划找这一个子集，容量为 \(O(q^2)\) 个布尔状态；不是枚举平均词。

## 8. 终止、精度与阈值

每个非终端分支都有保持 (5) 的安全非恒等整数操作。其能量降幅为
\[
\sum_{i\in S}E_i^2-q\left(\frac{\sum_{i\in S}E_i}{q}\right)^2
=\sum_{i\in S}(E_i-\bar E_S)^2\ge2.
\]
因此从 \(qX\) 出发有限步进入已给真实收尾的终端。对原输入执行同一索引词，中间值全部在 \((1/q)\mathbb Z\)，并有粗步数界
\[
T\le\frac{q^2}{2}\sum_iX_i^2.
\tag{15}
\]
这是数值高度界，不是可变 \(n\) 的输入位长多项式路径长度证明。给定满足 (1) 的维数，判定只需计算 \(G\) 并检查其素因子是否被 \(q\) 支持，因而是多项式时间；可用反复除 \(\gcd(G,q)\) 检查支持，不需要分解巨大 \(G\)。

为证明 (3)，令 \(h=\lceil\log_2q\rceil,\ n_0=4q+h+1\)。有 \(h\le q-1\)，故 \(n_0\le5q<8\cdot2^h\)，从而 \(\lfloor\log_2 n_0\rfloor\le h+2\)。于是
\[
n_0-\lfloor\log_2 n_0\rfloor\ge4q-1.
\]
整数函数 \(n-\lfloor\log_2n\rfloor\) 单调不减，而 \(d_q(n)\le\lfloor\log_2n\rfloor\)，故所有 \(n\ge n_0\) 满足 (1)。

四平均：16、17、18逐项满足 (1)；\(n\ge19\) 时 \(n-\lfloor\log_2n\rfloor\ge15\)。六平均：24没有危险素数；\(n\ge25\) 时危险素数都至少为5，故 \(d_6(n)\le\lfloor\log_5n\rfloor\)，且 \(n-\lfloor\log_5n\rfloor\ge23\)。这证明 (4)。

## 9. 四个零／六个零的统一终端接口

**推论。** 对 \(q=4\) 或 \(q=6\)，任意 \(n\ge q\) 元零和状态一旦产生 \(q\) 个零，就可全部归零。一般输入中的“零”应理解为减去总体均值后的零，即已经等于目标均值的位置。

若 \(n\le2q\)，非零位置至多有q个；将全部非零位置加适量零位置凑成一个q元组，一步即可归零。下面处理较大的n。

四平均：若 \(n\) 偶，已有半块定理；若 \(n\) 奇，留下一个零不动，在剩下偶数 \(n-1\ge8\) 个位置调用该定理。子状态零和且仍有零坐标，因此本原化后 \(G=1\)。

六平均：留下 \(n\bmod3\) 个零不动，在剩下的三倍数位置调用六平均完整定理。至少有一个零保留在该子状态中，故仍为 \(G=1\)。子维数至少9。

零向量本身当然单独结束。该推论不证明每个合法状态都能先制造 \(q\) 个零；它把剩余小维数问题的终端目标统一了。

## 10. 核验对应与局限

入口：

~~~text
python work/run_verifications.py --id arbitrary-arity-linear-threshold
~~~

对应脚本 [verify_arbitrary_arity_linear_threshold.py](../sources/work/document_reorganization_20260915/originals/work/verify_arbitrary_arity_linear_threshold.py)，记录 [arbitrary_arity_linear_witnesses.json](../work/arbitrary_arity_linear_witnesses.json)。

本次精确核验：

~~~text
all-arity nonunit and midpoint classification: PASS 987 172
all-arity uniform threshold capacities: PASS 3040
composite EGZ residue multisets: PASS 4488
all-arity large-integer closure and initialization: PASS 2804 39
composite zero-trigger original-position paths: PASS 24
all-arity original-position full paths: PASS 70 94
arbitrary-arity linear threshold: PASS
~~~

987个非单位比例恒等式、172个有限中点例外、3040个容量样本、四／六平均的4488个完整余数多重集、2804个大整数局部分支及39个初始化实例核对公式。70个独立随机筛选输入的完整路径覆盖四、六、八、九、十、十二、十五平均，最长94步；未以逆向打乱生成这些输入。

原始路径以 Fraction 重放，只接收原始输入与位置索引。对整数零和本原输入，还独立核对分母整除 \(q\)；合数分母可以是 \(q\) 的真因子，不能沿用旧程序“分母只能为1或 \(q\)”的素数断言。

另存24条第9节造零收尾的完整原位置路径，特意覆盖尚未证明全部输入可达的低维情形；这些路径只证明该零坐标子族。通用算法的15种分支全部被有限样本触及，其中两个大背景等差分支用专门实例直接核验。

本轮没有改变旧素数求解器的适用域。新程序明确传入 \(P_q(n)\)，只复用不依赖素数性的初始化、位置账本、EGZ 动态规划和系数打包函数。一般量词由本文证明承担，有限核验只审查实现。

<!-- END SOURCE doc-1f9362671efe -->

---

<a id="doc-82dc396fa577"></a>

## 原文导签：Arena三平均网页算法审阅与同题对比

来源：`work/document_reorganization_20260915/originals/outputs/arena_triple_solver_review.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/arena_triple_solver_review.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-82dc396fa577 -->
# Arena三平均网页算法审阅与同题对比

日期：2026-09-12。审阅对象：[用户提供的网页](https://01a09196-93af-786c-810a-960e700588f5.arena.site/)。

结论：在小整数、零和组合较多的输入上，网页是一个实用的短解启发式，连续运行时确有提速。但相对项目已有的“短宏+结构构造”组合，步数多数相同；其大整数稳定性明显不足，不能作为完整求解算法替代现有构造。最值得采用的是零和子集宏与快速选步，再接严格构造兜底。

## 1. 实际审阅与复现范围

通过无界面的Microsoft Edge实际打开网页，读取内部 iframe 的算法源码，保存[页面快照](../work/arena_triple_solver_review/frame1.html)和[提取的计算部分](../work/arena_triple_solver_review/arena_solver.js)。算法文件没有修改，仅统一换行；[来源与SHA256](../work/arena_triple_solver_review/provenance.json)记录版本。

将已检查的纯计算函数放入Node隔离上下文，排除页面渲染、网络加载和统计脚本，用原网页单题默认参数运行：

~~~text
width=400, depth=70, maxNodes=60000, timeMs=9000, moveCap=60
~~~

另设外部16秒终止保护，以免原网页的预算检查失效。正式48个对比输入均由网页自身返回，没有触发外部终止。各题串行运行，随后再串行复测旧Python算法，避免同时争抢CPU。

复用原有三个数据集：

- 24个独立均匀取自[-20,20]、同时满足二平均和三平均条件的输入，n为11、12、16、20；
- 18个8、16、32位幅度输入，n为11或20；
- 6个64、128位幅度输入，n为11、20、50，由旧大整数数据集各组选取第0个样本。

额外测试整体缩放、已知判定类别和固定宏。所有网页报告成功的索引序列，均由另外的Python Fraction验证器从原始数值重放至精确均值。

没有把随机搜索未命中认定为不可达；样本比较不外推到所有输入。

## 2. 网页的真正算法

它采用以下顺序：

1. 找精确零和三元组，立即消去。
2. 用中间相遇方法寻找4至9元的零和子集，配合已有零位置执行固定宏。
3. 尝试一个准备操作，使下一步能直接消元。
4. 如果仍未归零，运行有宽度、深度和预算限制的束搜索。
5. 解长不超过60时，尝试逐个删除操作；只有从原输入重新验证成功才接受删除。

### 固定宏是最有效的一部分

| 非零子集大小 | 所需额外零位置 | 固定宏步数 |
|---:|---:|---:|
| 4 | 3 | 5 |
| 5 | 2 | 5 |
| 6 | 1 | 5 |
| 7 | 2 | 6 |
| 8 | 1 | 6 |
| 9 | 0 | 6 |

这些宏确实正确。审阅中对每类零和子空间的全部基向量，另外用Fraction重放，共33个基测试通过，因此不是“看起来接近零”的假解。

寻找零和子集时仅使用最多24个非零位置，中间相遇每半至多12项，所以典型规模是每半至多4096个子集。对小值域输入，这能快速一次消去很多位置；它比只降低平方能量更贴近“早日达到精确零”的目标。

项目此前已经采用零和三元组、补零三幂块和四非零项收尾，因此很多小输入会产生同样长度的解。网页的额外4至6元宏和不同子集选取次序，偶尔能进一步缩短。

## 3. 24个小整数同题：确实快，步数改进较小

两边都解出24/24题。与旧的短宏组合算法比较：

- 22题步数相同；
- 1题从19步降到13步；
- 1题从9步变成10步；
- 平均步数从8.46降到8.25。

分维数看：

| n | 旧纯不变量构造的平均步数 | 旧短宏组合 | 网页 |
|---:|---:|---:|---:|
| 11 | 16.17 | 7.00 | 7.00 |
| 12 | 16.33 | 6.50 | 6.50 |
| 16 | 22.33 | 10.50 | 9.50 |
| 20 | 23.67 | 9.83 | 10.00 |

所以如果对比的是更早的纯能量下降，网页的改进很大；如果对比的是已经加入短宏的版本，整体步数改进约2.5%。

### 计时要计入浏览器预热差异

用每题新建JS上下文时，网页平均2.25ms，旧Python短宏组合平均1.95ms。

但用户通常在同一个网页连续求解，因此另做一次固定上下文、先执行3次不计时预热的24题对比，网页平均降到
\[
\boxed{0.85\ \text{ms/题}}
\]
而旧Python约1.95ms。这个场景下网页约快2.3倍，用户的提速体感有依据。

这些是本机实测，不是语言无关的算法复杂度结论。Node/V8的JIT、BigInt实现、Python对象开销都参与了差异；页面绘制、加载、动画与启动开销没有计入算法时间。不能把0.85ms理解为用户点击到页面全部绘制完的耗时。

## 4. 位数提高后的成功率与耗时

后面三组对比的旧基线是“最大安全能量降幅”完整构造，未额外搜索更短解。两种策略目标不同：网页花预算尝试更短路径，旧构造先保证给出可验证的解。

| 输入组 | 题数 | 网页成功 | 旧构造成功 | 网页平均耗时 | 旧构造平均耗时 |
|---|---:|---:|---:|---:|---:|
| 小整数同题 | 24 | 24 | 24 | 0.85ms，预热后 | 1.95ms |
| 8位幅度 | 6 | 6 | 6 | 193ms | 2.04ms |
| 16位幅度 | 6 | 3 | 6 | 4.75秒 | 3.41ms |
| 32位幅度 | 6 | 0 | 6 | 9.30秒 | 6.91ms |
| 64/128位幅度 | 6 | 0 | 6 | 10.48秒 | 86.98ms |

8位组中有5题几毫秒完成，但1题进入约1.14秒的束搜索，所以平均值突然上升。不能只用“8位”假设每题难度相近。

网页成功的8位组平均11.5步，旧构造27.17步。16位组只对网页成功的同3题比较，网页平均14步，旧构造35.33步；没有用成功子集的步数均值冒充全组表现。

一个具体同题：

~~~text
[-191, 162, 107, -16, 42, 58, 38, -148, 41, 123, -29]
~~~

网页7步，最大降幅构造22步，网页在此确实更短。

但旧64位十一元样本能用133步在约9.5ms内构造完成，网页默认预算约8秒返回“未找到”。64/128位尚远未到Number溢出范围，不能把这些失败全归因于溢出；主要问题是小值域精确零和组合减少，束搜索的候选和排名没有充分利用严格的模3及重数结构。

全部48个比较题里，网页解出33题，旧方法解出48题。因此网页目前不适合作为通用求解器唯一后端。

## 5. “全程精确算术”需要更准确地表述

网页的数值更新与最终验证确实使用约分BigInt分数，已经给出的成功解没有发现浮点伪零问题。

但决定搜哪些操作时使用
~~~javascript
Number(numerator) / Number(denominator)
~~~
并据此做近邻定位、排序、容差预筛和评分。因此准确说法应是：

> 状态与验解精确；候选筛选和搜索评分使用浮点启发式。

两个影响已被实际触发：

### 同一题整体放大，会改变解甚至导致漏解

用旧数据集的一道十一元题，保持结构不变，仅乘正数：

| 整体倍率 | 网页结果 |
|---|---|
| 1 | 9步成功 |
| \(10^{30}\) | 10步成功 |
| \(10^{310}\) | 未找到；没有生成任何搜索候选 |

我把原9步索引原封不动作用到两种放大后的输入，都用Fraction精确验证成功。因此不是数学可达性变化，是数值表示和启发式变化。

巨大倍率下Number出现Infinity/NaN，近邻筛选不再正常。网页手动输入并未限制位数，所以这个输入在其接受范围内。简单的连续整数示例在同样倍率下仍可能被固定宏直接解决，故不是“大整数一律失败”，而是需要搜索时容易暴露问题。

### 评分的优先级不随尺度保持

代码使用
~~~javascript
nonzeroCount * 1e12 + distinctCount * 1e6 + sumAbs
~~~
以及带 \(10^{15}\) 常数的异号优先分数。数值变大后，幅度项会压过原本想优先考虑的非零位置数或异号配对，导致排序目标改变。

这可以通过字典序评分或对幅度归一化解决，无需牺牲精确验解。

## 6. 搜索预算和产品行为的限制

预算只在一个外层节点处理结束且
~~~javascript
(nodes & 511) === 0
~~~
时检查。一个外层节点能一次增加多个节点，可能直接跨过512的倍数，因此检查频率不可靠。

实际将预算设为1ms、节点上限10时，函数仍运行约211ms，并生成6112个候选。默认9秒预算的一个大整数样本也运行到14.86秒。主求解的贪心和中间相遇阶段没有统一截止时间。

此外：

- 没有Web Worker，主要计算在页面线程进行；async只在偶尔到达的检查点让出执行。
- 束搜索只保留少量启发式候选，不完整枚举所有三元组；G合法并不保证在预算内能找到路径。
- 搜索状态只按精确有理多重集去重，没有整体本原尺度商，可能重复探索相同射影结构。
- 束搜索阶段没有重新充分调用固定短宏收尾，已有的宏优势主要局限于前置贪心阶段。
- 单题导出包含完整操作；批量结果只保存步数和耗时，未保存各题操作序列，所以批量导出无法独立重放。若按用户原求解器要求，这一项还需补齐。

它明确将预算失败显示为“已判定可行，但未找到”，这一点是正确的。不能把网页显示的成功率当作G判据的成立比例。

随机生成确实是各位置独立抽样再用判据筛选，没有逆向打乱泄露答案。不过使用Math.random与Number取整，只适合普通安全整数值域；不宜声称任意大整数值域都均匀精确采样。

## 7. 最值得整合的改进

建议保留现有算法为快速候选层，顺序如下：

1. 精确零和三元组与中间相遇零和子集，调用已核验短宏；
2. 遇到难题立即保留一个由项目完整构造算法给出的解；
3. 用剩余预算运行束搜索，只有找到更短且验证通过的序列才替换；
4. 在束节点接近终端时尝试短宏收尾，不必再逐原子搜索全部尾段。

同时做四个实现修正：

- 在中心化整数代表上处理精确三元和；用哈希表查第三项，避免Number预筛遗漏。
- 评分采用字典序：非零数、结构特征、归一化能量等，避免固定大常数被输入幅度击穿。
- 用“距离下次检查已新增多少节点”或固定循环计数检测预算，并覆盖所有前置阶段；放入Worker以保持页面可操作。
- 若采用本原化或符号商，只用于搜索与排名，并保存原位置账本；最终仍从原始输入精确重放。

这些改进不会证明最短解，但可以结合网页的小值域速度与项目构造的大整数稳定性。本轮只审阅、对比和保存证据，没有修改线上网页或将试验性启发式替换项目正式求解器。

## 8. 文件与快速核验

全部审阅文件放在 [arena_triple_solver_review](../sources/work/document_reorganization_20260915/originals/work/arena_triple_solver_review) 中，和历史数学证明分开：

- [来源与版本](../work/arena_triple_solver_review/provenance.json)
- [48题比较及4个额外缩放示例](../work/arena_triple_solver_review/comparison_single.json)
- [同机复测旧算法](../work/arena_triple_solver_review/baseline_current.json)
- [同一JS上下文预热结果](../work/arena_triple_solver_review/warm_small.json)
- [数值尺度和预算诊断](../work/arena_triple_solver_review/structure_checks.json)
- [机器可读汇总](../work/arena_triple_solver_review/summary.json)
- [快速独立核验](../work/arena_triple_solver_review/verify_saved_review.py)

~~~text
python work/run_verifications.py --id arena-triple-solver-review
~~~

快速核验只校验源码哈希、重放已保存成功序列、核对33个宏基和整体缩放反例，不再次运行长束搜索或访问网络。

~~~text
Arena captured algorithm provenance: PASS
Arena saved independent solution replays: PASS 37 24 33
Arena same-input success and step comparison: PASS 48 33 48 22 1 1
Arena scaled-input heuristic counterexample: PASS
Arena triple solver review artifacts: PASS
~~~

37包括主比较中的33个成功和4个连续整数缩放示例；另24个预热同题均被重放。所有速度数据只是这一版本、这一机器和这些输入的观测，不是复杂度或全输入性能证明。

<!-- END SOURCE doc-82dc396fa577 -->

---

<a id="doc-5aca8265bf7d"></a>

## 原文导签：原位置 p 平均算法测试集

来源：`work/document_reorganization_20260915/originals/outputs/averaging_algorithm_benchmark.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/averaging_algorithm_benchmark.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-5aca8265bf7d -->
# 原位置 p 平均算法测试集

日期：2026-09-12。用户已通知七平均十五元由其他 AI 完成证明；本次只整理构造算法的困难输入，不继续把搜索失败作为反例候选。

主包位置：
[测试集说明](C:/Users/19226/Documents/Codex/2026-09-10/new-chat/outputs/averaging_algorithm_benchmark/README.md)。

交付包含 584 道去重题，其中：

- 196 道七平均十五元、无非恒等整数出边的已知可达主测试题；
- 384 道 p=19,n=39 或 p=37,n=75 的结构扩展题，其中 52 道附已验证路径，332 道不设可达性真值；
- 1 道二十三平均七十元的保护位置回归题，附五步路径；
- 2 道容易正例和 1 道已证不可达的 2p 阴性对照。

共有 108 条独立 Fraction 重放通过的完整原位置路径。精选集 19 题；挑战集为 2 道旧束搜索宽度96、深度24未出路径的大整数七平均题。现在这两题的可达性由新的十五元定理保证，仍可测试具体路径的构造效率。

保留原始 576 次抽样的分布、所有预算、停止原因、重复别名、题面指纹和逐位置路径。值全部存为十进制字符串，索引统一为1基。验解器只用 Python 标准库，检查原始输入上的准确平均与最终全等，拒绝重复位置、越界索引、浮点坐标和未完成路径。

该测试集没有把旧搜索失败算成不可达，也不把已知路径长度算成最短长度；p=19,37 的未附路径扩展题不会错误继承十五元定理。

生成器可按相同零和自由结构生成新种子和更高位长的题面。建议先运行精选集，再运行七平均主集和新种子；参考答案文件由评测端保管。

项目核验入口：python work/run_verifications.py --id averaging-algorithm-benchmark。

<!-- END SOURCE doc-5aca8265bf7d -->

---

<a id="doc-61d3ffed997d"></a>

## 原文导签：从二平均到任意平均元数：当前全貌与临界猜想

来源：`work/document_reorganization_20260915/originals/outputs/averaging_global_status_20260912.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/averaging_global_status_20260912.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-61d3ffed997d -->
# 从二平均到任意平均元数：当前全貌与临界猜想

**最新合数主线：** [四项新结果](../sources/work/document_reorganization_20260915/originals/outputs/general_k_three_tasks_progress_20260915.md)包含GRH下全部2、3幂的最早临界点、任意元数2k+1端点、奇素数幂的全部奇数中间维数，以及M(10)=16的固定六步网络。下文相应旧“未证”状态保留为历史；一般合数最终阈值仍未解决。

**2026-09-15最新总结果：** [九偏移共同完成](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)接此前下半带及3p+10以上的证明，给出全部奇素数p的N(p)=2p+1；N(2)=4。判据始终为rad(G)|p，不能在p|n时一律写G=1。素数部分已无未覆盖维数；一般合数元数的最优阈值仍开放。下文是2026-09-12及早期追加的历史快照，其中五平均14元、素数元平均一般阈值“未解”等表述均已过期，最新状态以[当前索引](../sources/work/document_reorganization_20260915/originals/outputs/README.md)为准。

2026-09-15完整更新：[三单点交换子与无条件入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unrestricted_endpoint_and_odd_band.md)删除下半带全部素因子数和密度入口条件。任意奇p>=3的2p+1端点、任意素数p>=5的全部奇数2p<n<3p均已全输入完成；全部偶余量也已进入合法核心，但一般核内终止和最终阈值仍未解决。统一坐标及后续两轮修复见[统一文稿](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)。

2026-09-15偶数后续：[内部偶余量完整证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_interior_completion.md)已完成所有4<=r<=p-3的偶数核心方向、尺度和终端输送。偶数下半带剩余一般边界为r=2和r=p-1；最终阈值仍未降低。

2026-09-14的[合数端点同余闭合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)先完成任意合法核心；2026-09-15新入口使原六素因子或Theta限制全部删除。一般后续偶数维数仍须处理；本页各小元数最终阈值并未因此降低。

2026-09-14上半带完整族：[与6互素的上半带定理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_coprime_six_complete.md)证明所有素数p>=13、3p+10<=n<=4p-3且gcd(n,6)=1的全输入G=1充要判据，不限制n的素因子个数。一般最终阈值与未覆盖的2、3局部情形、两端短区间仍开放。

日期：2026-09-12。记 \(q\) 为每次平均的元数，\(n\) 为总位置数。对有理输入减去总体均值、清分母并本原化为
\[
X\in\mathbb Z^n,\quad \sum_iX_i=0,\quad \gcd_iX_i=1,\qquad
G(X)=\gcd_{i<j}|X_i-X_j|.
\]

## 1. 统一必要条件与量词

对任意 \(q,n\)，可达必然满足
\[
\boxed{\operatorname{rad}(G)\mid q,\qquad G\mid n.}
\]
第一条来自禁止素数的共同非零余类不变量；第二条来自零和与本原性。

定义 \(\mathcal P(q,n)\) 为“对所有有理输入，可达当且仅当 \(\operatorname{rad}(G)\mid q\)”。定义
\[
N(q)=\min\{N:\mathcal P(q,n)\text{ 对所有 }n\ge N\},
\]
\[
H(q)=\min\{n>q:\operatorname{rad}(n)\nmid q,\ \mathcal P(q,n)\}.
\]
\(H\) 是 \(G\) 真正筛选输入的非自动边缘；\(N\) 是最终阈值。自动维数满足 \(\operatorname{rad}(n)\mid q\)，此时G条件本身不筛选输入。

另有普遍小维数定理：\(n=q+1\) 时，可达当且仅当某个初始坐标已经等于总体均值。它不是一般G判据。

## 2. 已证的素数和小元数结果

### \(q=2\)

\[
n=3\Longleftrightarrow\text{三数成等差},\qquad
n\ge4:\quad \mathcal P(2,n).
\]
因此 \(N(2)=4\)。四元是自动G维数，非自动边缘 \(H(2)=5\) 已证。

### \(q=3\)

\[
\boxed{\mathcal P(3,n)\quad(n\ge7)}
\]
即 \(G\) 为三幂当且仅当可达；\(N(3)=H(3)=7\)。

### \(q=4\)

已证
\[
\mathcal P(4,7),\qquad \mathcal P(4,9),
\]
以及全部偶数 \(n\ge8\) 的完整判据。六元有 \(G=1\) 不可达例
\[
(-1,-1,-1,-1,0,4).
\]
所以 \(H(4)=7\)，但整体仍只有
\[
7\le N(4)\le16,
\]
\(n=11,13,15\) 未解决。

### \(q=5\)

已证 \(n=11,12,13\) 及全部 \(n\ge15\) 的完整判据。十二元由[统一文稿第11节的直接整数下降](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)补齐，十三元由[主同余群证明](../sources/work/document_reorganization_20260915/originals/outputs/five_average_thirteen_congruence_complete.md)承担。故
\[
H(5)=11,\qquad N(5)\in\{11,15\}.
\]
只有\(n=14\)仍未解决。若它满足完整判据，则N(5)=11；若存在合法反例，则N(5)=15。

### \(q=6\)

八元有 \(G=1\) 不可达例
\[
(-1^6,0,6).
\]
九元有固定四步网络，但G自动成立，只是辅助结果。十元已证
\[
\boxed{\mathcal P(6,10):\quad G\in\{1,2\}\Longleftrightarrow\text{可达}.}
\]
因为十元 \(G\mid10\)，这正是 \(G=2^a3^b\) 的简化；所以 \(H(6)=10\)。此外全部 \(3\mid n,\ n\ge6\) 及全部 \(n\ge24\) 已证。当前
\[
9\le N(6)\le24,
\]
未解决的非自动维数为 \(11,13,14,16,17,19,20,22,23\)。

### \(q=7\)

全部n>=15现已证明
\[
\boxed{\mathcal P(7,n)\quad(n\ge15),\qquad N(7)=H(7)=15.}
\]
最新[最优阈值证明](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_sharp_threshold_complete.md)用原位置标量闭路、深主同余和完整方向—尺度有限证书补齐20、22元；接已证15—19、21及全部n>=23。十四元有已证G=1不可达族，故阈值15最优。一般p的最优阈值与五平均12、14仍开放。

### \(q=8\)

九至十二元有临界赋值反例；十三元已证
\[
\boxed{\mathcal P(8,13):\quad G=1\Longleftrightarrow\text{可达}},
\]
故 \(H(8)=13\)。最终 \(N(8)\) 未定。

### \(q=9,10,12\)

九平均十三元已由[平方元数统一控制器](../sources/work/document_reorganization_20260915/originals/outputs/square_arity_uniform_controller_and_nine_thirteen.md)完整证明M(9)=H(9)=13。十平均十七元、十二平均十七元两项也已证：
\[
\boxed{H(10)=H(12)=17,\qquad \mathcal P(10,17),\ \mathcal P(12,17).}
\]
N(9)仍未确定。十、十二平均十六元的G条件自动成立，不能代替十七元结论；十二平均十六元有固定四步网络，十平均十六元现也有固定六步网络，故M(10)=M(12)=16。

## 3. 任意平均元数的大维数定理

对任意整数 \(q\ge3\)，令
\[
d_q(n)=\#\{\ell:\ell\mid n,\ \ell\nmid q\}.
\]
已证明
\[
\boxed{n\ge4q-1+d_q(n)\Longrightarrow\mathcal P(q,n).}
\]
因此每个固定 \(q\) 都有最终阈值，且
\[
\boxed{N(q)\le4q+\lceil\log_2q\rceil+1\le5q.}
\]
证明不需要q为素数：非单位差分用 \(q/\gcd(\delta,q)\) 与其余份数的两值配比直接构造整数平均；中点碰撞、一般EGZ、保护池和整数能量下降随后完成闭包。

这是一条统一充分上界，不是最优临界线。

## 4. 原 \(B(q)\) 与精确临界线猜想

定义
\[
S(q)=\max_{p^a\parallel q}p^{\lceil a/2\rceil},
\]
并令
\[
B(q)=q+S(q)+
\begin{cases}
0,&\operatorname{rad}(q+S(q))\mid q,\\
1,&\operatorname{rad}(q+S(q))\nmid q.
\end{cases}
\]
赋值间隙不变量已证明：\(q<n<q+S(q)\) 存在 \(G=1\) 反例；边界 \(q+S(q)\) 在不自动的情形也存在反例。因此 \(M(q),N(q)\ge B(q)\)，其中 \(M\) 是排除平凡 \(n=q\) 后的最早完整G维数。

按当前“只关心G真正筛选输入”的标准，精确候选应为
\[
\boxed{C(q)=\min\{n\ge B(q):\operatorname{rad}(n)\nmid q\}.}
\]
已有下界给出 \(H(q)\ge C(q)\)。最自然的两条猜想是
\[
\boxed{H(q)=C(q)}
\]
以及更强的
\[
\boxed{M(q)=B(q),\qquad N(q)=M(q).}
\]
前者是非自动算术猜想；后者还要求自动点和后续维数没有空档。

代表性数值：
\[
\begin{array}{c|cccccccccccc}
q&2&3&4&5&6&7&8&9&10&12&14&15\\
\hline
B(q)&4&7&7&11&9&15&13&13&16&16&22&21\\
C(q)&5&7&7&11&10&15&13&13&17&17&22&21\\
\text{H状态}&已证&已证&已证&已证&已证&已证&已证&已证&已证&已证&未证&未证
\end{array}
\]

其中 \(q=10,12\) 的 \(B=16\) 是自动G点，必须跳到17；这正是“加一后仍可能自动”的情形。

## 5. \(B(q)\) 中自动G点的完整列表（\(q\le200\)）

\[
\begin{array}{c|c@{\qquad}c|c@{\qquad}c|c}
q&B(q)&q&B(q)&q&B(q)\\ \hline
2&4&6&9&10&16\\
12&16&20&25&30&36\\
42&49&54&64&56&64\\
75&81&90&96&110&121\\
120&125&132&144&138&162\\
156&169&182&196&&
\end{array}
\]
自动的精确定义始终是 \(\operatorname{rad}(B(q))\mid q\)；表格只是 \(q\le200\) 的枚举。

## 6. 奇端点 \(n=2q+1\) 的合数推广

端点的两部分必须分开：

- 若 \(2q+1\) 至多含两个不同素因子，已有统一三步入口；结合完整CRT陪集证书可证明全输入 \(G=1\) 判据。
- 统一CRT流程已核验36个指定合数level的32112条回路，其中28个两素因子level得到全输入结论，8个三、四素因子level的核心证书先行完成，后来四素因子入口定理已补齐，因此这36个列明端点均已完成全输入判据。
- 结合素数幂端点定理，在有限范围内所有奇 \(3\le q\le109\) 的 \(2q+1\) 端点均已解决。

一般合数level仍未有全称群包含定理；三个以上危险素因子的任意输入入口也曾是独立缺口。有限证书不能外推到任意level。

## 7. 自动网络与G等价的区别

自动G维数不应与非自动算术边缘混为一谈。例如：

- 二平均四元、六平均九元、以及 \(q=m(m-1), n=m^2\) 的固定四步网络族，都是无条件网络；
- 这些点说明存在一个固定全输入平均词，不说明相邻非自动维数；
- \(q=6,n=9\) 是无条件成功，真正的G筛选点是 \(n=10\)；
- \(q=10,12,n=16\) 的G自动，真正已证筛选点是 \(n=17\)。

## 8. 当前可复核入口

主要证明证书：

~~~text
python work/run_verifications.py --id six-average-ten-complete
python work/run_verifications.py --id seven-average-fifteen-complete
python work/run_verifications.py --id ten-twelve-seventeen-complete
python work/run_verifications.py --id four-average-seven-complete
python work/run_verifications.py --id eight-average-thirteen-complete
python work/run_verifications.py --id composite-endpoint-transfer
python work/run_verifications.py --id arbitrary-arity-linear-threshold
~~~

对应文档分别覆盖 \(H(6)=10\)、\(H(7)=15\)、\(H(10)=H(12)=17\)、\(H(4)=7\)、\(H(8)=13\)、合数端点有限推广以及任意q的大维数充分定理。各程序都区分定理证书、有限核验与探索性搜索，不把超时或有界搜索失败当成不可达证明。

<!-- END SOURCE doc-61d3ffed997d -->

---

<a id="doc-ef0a7164ebda"></a>

## 原文导签：二平均之后的文献进展：2018--2026 检索与可用工具

来源：`work/document_reorganization_20260915/originals/outputs/averaging_literature_survey_2018_2026.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/averaging_literature_survey_2018_2026.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ef0a7164ebda -->
# 二平均之后的文献进展：2018--2026 检索与可用工具

后续战略检索见[任意 p 路线重评估](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_strategy_reassessment_20260912.md)：44个结构查询得到148篇去重题录，并下载阅读 S-整数 SL2 有界生成、语言约束 Lyapunov、多面体 path-complete 和 Chevalley 有界生成四份全文。新增的 2026 SL2 预印本报告至多7个初等因子；这些结果仍不自动带来原位置运输。

检索日期：2026-09-12。

同日后续：[逆零和定理的实际转译](../sources/work/document_reorganization_20260915/originals/outputs/inverse_zero_sum_averaging_progress.md)已给出O(p)模运算的带副本选择、相反碰撞恢复、五平均十四元配对核的部分完整分类，以及所有奇数p>=5的2p+4元七步二参数族。安全性和碰撞不再只停留在这篇综述的候选说明中，但一般阈值仍未改善。

## 1. 本轮结论

有值得借用的后续进展，但本轮没有找到已经证明以下结论的公开文献：

- 固定原位置、每次把恰好三个或一般 p 个值同时替换为算术平均时，对任意有理输入的完整可达判据；
- 一般奇素数平均元数的最优阈值 N(p)=2p+1；
- 由端点维数直接内插整个中间区间的定理。

这是本轮检索的结果，不是“这些文献不存在”的证明，更不能单凭它认定项目结果具有发表意义上的首次性。

最值得优先借用的三类材料是：

1. **2022 年逆加权零和定理**：把“没有可用选择”转成强制的重复余数结构，最贴近当前重数与容量问题。
2. **2019 年正式发表的 Clique Gossiping**：提供真正的多点平均框架与有限步全初值网络判据，但必须区分其量词与本项目。
3. **2021--2022 年块 Kaczmarz 与 gossip 的统一分析**：可用于合法块的能量下降和速度分析，不能直接代替精确有限终止。

另找到 2022 年确定性 O(n log n) 的 EGZ 构造预印本，是改进现有实现的明确候选，但没有改善 2n-1 的一般长度门槛。

## 2. 检索范围和证据等级

实际检查了以下路线：

- 原论文的 arXiv、会议和期刊版本，分别查正向引用；
- 原作者的后续题录、2019 年博士论文，以及作者主页；
- clique gossip、finite-time consensus、block gossip、Kaczmarz；
- mixing graphs、mix-reachability、随机矩阵与幂等／可达性关键词；
- EGZ、逆零和、加权零和、构造算法；
- 2024--2026 年相关题录和主要相关论文的后续引用。

使用 Crossref、OpenAlex、Semantic Scholar 的公开接口，并回到 Dagstuhl、大学论文库、作者主页、Springer 和 Integers 期刊核对。
保存了数十份成功或返回明确错误状态的检索／页面响应记录；另下载并提取三份新增全文：2019 年博士论文、2022 年逆零和论文、2024 年 splitter networks 论文。

访问限制：本机直接连接 arXiv 多次失败，Semantic Scholar 后续请求受到限流，Google 无法连接，Bing 对稀有术语退化为无关结果，部分出版商只开放摘要。
因此下面明确区分“已读全文相关章节”和“只核对摘要、题录”。未读到全文的材料不作为已审定可直接调用的证明。

还遇到两种数据库问题：同一论文的预印本、会议和期刊记录分散；Miguel Gonzalez 的作者记录混入了同名化学作者。
直接引用图也有漏项：2024 年 splitter 论文的正文确实引用原论文，但并未出现在本次 OpenAlex 原论文引用列表中。
因此不把数据库的引用数当成研究进展的完整计数。

## 3. 原论文并非只有“2018 年版”

Miguel Coviello Gonzalez、Marek Chrobak：
**Towards a Theory of Mixing Graphs: A Characterization of Perfect Mixability**。

- 2018 年 arXiv 预印本：[arXiv:1806.08875](https://arxiv.org/abs/1806.08875)。用户提供的 v4 源码已在项目中阅读。
- 2019 年 CIAC 会议扩展摘要：[DOI 10.1007/978-3-030-17402-6_16](https://doi.org/10.1007/978-3-030-17402-6_16)。
- 2020 年正式期刊版：Theoretical Computer Science **845**, 98--121；[DOI 10.1016/j.tcs.2020.09.007](https://doi.org/10.1016/j.tcs.2020.09.007)。Crossref 给出 2020 年 12 月卷期，OpenAlex 给出 2020-09-10 的日期。

这三个记录属于同一研究成果的版本链，不能把 2020 年期刊版算成三平均推广。

原文末节提出的主要后续问题是一般 MixReachability、单滴目标的最小浪费，以及给定线性映射是否由 mixing graph 实现。
这些问题比“最终全部相等”的 perfect mixability 更宽；原文没有给出一般 p 平均定理。

## 4. 直接后续：作者论文与 2024 年网络工作

### 4.1 2019 年博士论文：补充材料比会议稿丰富

Miguel Coviello Gonzalez，**Towards a Theory of Droplet-Mixing Graphs in Microfluidics**，UC Riverside，2019 年 9 月。

[大学正式条目](https://escholarship.org/uc/item/4wb2g5z2)；
[公开全文](https://escholarship.org/content/qt4wb2g5z2/qt4wb2g5z2.pdf)。

本轮阅读了模型、贡献概述、perfect mixing 及第四章相关范围说明。
除二平均定理外，论文包含固定深度困难性、一般输入输出的 dominance 必要条件和某些特殊目标的可判定性。
它明确区别：在允许任意体积混合的 fluid 模型中，dominance 也是充分条件；固定液滴模型中则不是。

**与项目的关系：** 这与我们已经遇到的“连续运输／majorization 可行不等于原位置平均词可实现”是同一种边界。
博士论文并没有把该边界解决，也明确将研究限定在 1:1 混合模型。

### 4.2 2020 年 RPRIS：真实续作，但目标不同

Coviello Gonzalez、Chrobak，**A Waste-Efficient Algorithm for Single-Droplet Sample Preparation on Microfluidic Chips**。

2019 年预印本 [arXiv:1908.09618](https://arxiv.org/abs/1908.09618)，2020 年 ACM Journal of Experimental Algorithmics 正式版：
[DOI 10.1145/3408297](https://doi.org/10.1145/3408297)。

其 RPRIS 算法为单个目标液滴构造混合图，改善最坏情形的浪费上界和实验表现。
本轮核对了摘要、正式题录，并读到博士论文中相应问题的介绍。

**限制：** 它允许按目标制备并处理剩余液滴；不是固定 n 个值全部归零的系统，也没有证明一般 k 元平均的阈值。

### 4.3 2024 年 splitter networks：流与稳态方面的实质进展

Basile Couëtoux、Bastien Gastaldi、Guyslain Naves，
**The Steady-States of Splitter Networks**，FUN 2024。

[正式出版页和开放全文](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FUN.2024.9)。本轮已读相关全文。

主要结果：计算 splitter 网络稳态的多项式时间方法；通过带相等约束的循环流及辅助 Markov 链处理流量；构造平衡网络，并证明 Omega(n log n) 的节点下界。
它明确引用 2020 年 perfect mixability 论文。

**关键区别：** 该模型允许有向循环，研究稳态流量。正文明确指出，为任意数量的输出实现平衡，有向循环可能是必要的。
所以不能把稳态存在定理直接解释成固定个数液滴经有限次平均完成。

**可借用处：** 相等约束流、残余网络和障碍证书的组织方式，可用于研究某些具体运输方案。
它不提供一般“运输矩阵到有限正向平均词”的分解定理。

## 5. 与 p 平均最直接相邻的文献：Clique Gossiping

**2026-09-12合数平均复核更新：** 下述机构摘要的整除表述不能直接当作本项目的定理。[六平均九元的固定四步原位置网络](../sources/work/document_reorganization_20260915/originals/outputs/composite_arity_four_six_transfer.md)已对全部标准基精确重放，得到J9/9，但6不整除9。尚未取得全文，无法确定完整假设或摘要表述的差异；本项目后续结论不调用“m|n必要”。以下保留原始摘要阅读记录，不将它视为已经核验的适用判据。

Yang Liu、Bo Li、Brian D. O. Anderson、Guodong Shi，
**Clique Gossiping**，IEEE/ACM Transactions on Networking，2019。

[DOI 10.1109/TNET.2019.2952082](https://doi.org/10.1109/TNET.2019.2952082)；
[作者机构正式记录](https://hdl.handle.net/1885/307516)；
[预印本 arXiv:1706.02540](https://arxiv.org/abs/1706.02540)。

注意其预印本早于 2018 年，2019 年是正式发表时间，不宜说全部思想都在原论文之后才出现。
本轮核对了作者机构摘要、期刊题录和后续引用；机构 PDF 受限，未读到全文证明。

该文研究沿 clique 序列进行多节点线性交互，其中 clique averaging 正是把一个组的节点一起取平均。
摘要明确报告：使用相同大小 m 的 clique，存在全初值有限步共识网络的充要条件是 m|n，且 m、n 有完全相同的素因子集合。
它还研究最快的有限步构造，以及无环广义线图下的谱次序不变性。

### 为什么这不反驳我们的 p 平均研究

对 p 为素数，上述全初值网络条件给出 n 必须是 p 幂。
这种目标是寻找一个线性操作词 W，使

\[
\exists W\quad\forall x\in\mathbb R^n,
\qquad W x=\frac{\sum_i x_i}{n}\mathbf1.
\]

我们的目标则允许

\[
\forall\text{ 合法 }x\in\mathbb Q^n\quad\exists W_x.
\]

两者不能交换量词。
事实上，一个固定 p 平均词的矩阵元素都在 Z[1/p]；如果它对所有实输入精确平均，其矩阵必须是 J/n，于是 1/n 必须属于 Z[1/p]，立即要求 n 为 p 幂。

**可借用处：** 多点平均的统一矩阵框架、张量式有限网络、原子顺序的交换与谱简化。
**不能借用成：** “不是 p 幂时所有合法有理输入都不可达”，或一般 2p+1 阈值定理。

## 6. 2021--2022 年：块平均作为 Kaczmarz 投影

### 6.1 统一框架与加速

Nicolas Loizou、Peter Richtarik，
**Revisiting Randomized Gossip Algorithms: General Framework, Convergence Rates and Novel Block and Accelerated Protocols**，IEEE Transactions on Information Theory，2021。

[DOI 10.1109/TIT.2021.3113285](https://doi.org/10.1109/TIT.2021.3113285)；
[2019 年预印本](https://arxiv.org/abs/1905.08645)。

将平均共识转成特定线性系统，把迭代线性求解器解释为分布式 gossip，涵盖成对、路径和块平均，并发展加速与对偶方法。
本轮核对摘要和正式题录，未取得全文。

### 6.2 从不交铺分推广到覆盖

Jamie Haddock、Benjamin Jarman、Chen Yap，
**Paving the Way for Consensus: Convergence of Block Gossip Algorithms**，
IEEE Transactions on Information Theory **68(11)**, 7515--7527，2022。

[DOI 10.1109/TIT.2022.3202733](https://doi.org/10.1109/TIT.2022.3202733)；
[预印本 arXiv:2110.14609](https://arxiv.org/abs/2110.14609)；
[作者出版目录](https://jamiehaddock.com/publications/)。

把 clique、path、同步成对 gossip 与 block randomized Kaczmarz 联系起来。
分析允许比 paving 更一般的 block coverings，并涵盖秩亏系统，改善收敛界。
本轮核对摘要、作者研究页面、正式卷期及后续引用；未取得全文。

**对项目的实际意义：** 可以将当前允许的安全平均组看作一族投影，研究这族投影是否仍覆盖所有需要消去的方向，以及是否具有统一能量下降比例。

**不能省略的一步：** 几何速度或期望收敛不是有限步精确归零。
若 p 进分母可以无限增长，能量趋于零时仍可能永远不为零。
要把这样的估计转成有限终止，必须另有固定离散格、精度界，或精确终端机制。
论文中的加速权重、额外状态或松弛操作也必须逐项检查是否仍是允许的 p 平均。

## 7. 最贴近当前阈值缺口的新材料：逆加权零和

### 7.1 已读全文的 2022 年定理

Sukumar Das Adhikari、Shruti Hegde、Md Ibrahim Molla、Subha Sarkar，
**Inverse Problems Related to Some Weighted Zero-sum Constants for Cyclic Groups**，
Integers **22 (2022), A7**，2022-01-07 发表。

[期刊公开全文](https://math.colgate.edu/~integers/w7/w7.pdf)；
[期刊卷目录](https://math.colgate.edu/~integers/vol22.html)。本轮已读定理 1 及其证明。

对 A={1,...,r}、1<r<n，文中定理 1 给出：长度 ceil(n/r)-1 的 Z/nZ 序列没有非空 A-加权零和子序列，当且仅当它是同一个单位的重复。
文中还处理平方单位权重的某些素数幂与平方自由模数；这些分支不是当前最直接需要的部分。

这类结果比只知道“足够长时必有选择”更有用：它精确描述失败时的形状。

### 7.2 可以直接转译成真实副本选择的推论

令 p>=5 为奇素数，k=(p-1)/2。假设有 k 对带标签副本，值分别为 x_1,...,x_k，另有一个 p 重锚点 a。
若 x_i-a 的模 p 余数不是同一个非零余数的重复，则上面的定理取 r=2 给出

\[
c_i\in\{0,1,2\},\qquad
1\le s=\sum_i c_i\le p-1,
\qquad
\sum_i c_i(x_i-a)=0\pmod p.
\]

取 c_i 份真实 x_i，再用 p-s 份 a 补足 p 个位置，就得到一次整数 p 平均。
每个系数至多 2，正好由两份实际副本提供；总位置数也严格受到控制。

这可用于 n=3p-1 等维数中“剩余位置恰形成多对副本”的配置。
它没有凭空允许加权平均。

仍须另证：保留所有非 p 同余见证，避免新均值碰撞到唯一完整保留的重值，以及不能立即继续时的终止机制。
所以这是可用的局部引理来源，尚不是中间区间的完整证明。

### 7.3 其他相关的新材料

Md Ibrahim Molla，**Some inverse problems in zero-sum theory**，
Proceedings - Mathematical Sciences **132**, article 63，2022。

[DOI 10.1007/s12044-022-00712-4](https://doi.org/10.1007/s12044-022-00712-4)。
本轮读到出版商摘要和引用列表，全文受限。
它继续研究若干加权零和常数的极值序列分类；不能在未检查具体权重集与位置容量前直接调用。

## 8. 2022 年 EGZ 的确定性近线性构造

Seok-Hwan Choi、Hanpil Kang、Dongjae Lim，
**Simple deterministic O(n log n) algorithm finding a solution of Erdős-Ginzburg-Ziv theorem**，2022-08-16 预印本。

[arXiv:2208.07728](https://arxiv.org/abs/2208.07728)。

作者给出从任意 2n-1 个整数中构造 n 个和被 n 整除的元素的确定性 O(n log n) 算法。
本轮核对了预印本题录和摘要，未取得全文，也未确认后续正式期刊版本。

**可用价值：** 项目已证明的保护池步骤仍可先排除少量禁选位置，再调用更快的 EGZ 构造。
这比继续使用通用固定基数模 p 动态规划更值得作为实现优化候选。

**严格限制：** 它不把一般长度门槛从 2n-1 降低。
输入任意大整数的读取、取模及位运算成本还需按原文计算模型核对，不能直接把摘要的 O(n log n) 写成无条件的位复杂度界。
本轮没有把尚未阅读全文的算法替换进正式证明核验器。

## 9. 2024--2026 的命中中，哪些不能当作突破

- **Constructing Stochastic Matrices for Weighted Averaging in Gossip Networks**，Erkan Bayram、Mohamed-Ali Belabbas，IFAC-PapersOnLine，2025；[DOI 10.1016/j.ifacol.2025.07.049](https://doi.org/10.1016/j.ifacol.2025.07.049)。摘要明确研究无限乘积及有限极限集，并允许设计随机矩阵，不是固定 p 个位置全等化的有限词分解。
- **Privacy-Preserving Distributed Average Consensus in Finite Time using Random Gossip**，2022；[DOI 10.23919/ECC55457.2022.9838457](https://doi.org/10.23919/ECC55457.2022.9838457)。虽然题名含 finite time，摘要明确说 approximate average consensus，因此不是精确归零定理。
- **Block Matrix and Tensor Randomized Kaczmarz Methods for Linear Feasibility Problems**，2025；[DOI 10.1007/s44007-025-00163-z](https://doi.org/10.1007/s44007-025-00163-z)。摘要结论是期望意义的线性收敛。
- **Finite-field consensus networks with multi-communication channels and time-delays**，2026 年题录；[DOI 10.1016/j.ffa.2026.102814](https://doi.org/10.1016/j.ffa.2026.102814)。本轮只取得题录，不把有限域共识外推成有理数精确平均结论。

大量含 mixing、gossip 的检索命中实际研究图神经网络、信息传播、概率分布的 joint mixability 或连续流体。
这些不属于原平均操作模型，未列入可用定理。

另一个 OpenAlex 命中为 Zakharov 的 **Convex geometry and the Erdős-Ginzburg-Ziv problem**，预印本 [arXiv:2002.09892](https://arxiv.org/abs/2002.09892)。其高维 EGZ 摘要有研究价值，但本轮数据库给出的期刊 DOI 无法解析，未把该期刊信息采纳为已核验事实；也未将高维渐近界当成一维 2p-1 门槛的改进。

## 10. 对当前项目的建议

优先读取和转译逆零和论文，将“参与次数”明确解释为真实副本数，并加入总长度、禁选位置和均值碰撞约束。
这最有机会直接处理不同余双重值与非等重数三值配置。

其次利用 block Kaczmarz 的覆盖分析研究已经合法的宏族是否有统一下降速度，同时保留精度或整数格条件。
它适合帮助完善多步下降证明，不能仅凭谱隙宣布精确终止。

实现优化方面，应在获得并审阅 2022 年 EGZ 算法全文后，独立实现和交叉核对，再决定替换现有动态规划。

本轮没有找到一个可以直接接上、立刻解决所有 p 或整个中间区间的模形式／Hecke 定理。
现有后续文献里，最贴近项目当前缺口的是带容量的零和结构和投影块覆盖，而不是再给形式群换一个描述。

本页是外部文献检索与接口分析，不是新的全维数可达性证明。

<!-- END SOURCE doc-ef0a7164ebda -->
