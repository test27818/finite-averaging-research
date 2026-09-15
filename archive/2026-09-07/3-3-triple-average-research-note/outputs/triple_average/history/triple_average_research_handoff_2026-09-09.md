# 三平均研究最新总览与交接说明（2026-09-09）

持续更新至2026-09-10。并行研究的主线接口与已确认结论见[团队交接](triple_average_team_handoff_2026-09-10.md)。

**最新统一条件归约：** [混合单点迹零返回](triple_average_mixed_singleton_controller.md)证明，对每个p=2 mod3，只要两个显式缩放返回能在原p位置实现，周期、上下根、Schreier输送和终端即全部闭合。两个目标已有严格正三进副本运输；原位置半群分解是这条充分路线的唯一缺口，而非原猜想的必要形式。进一步的精确方程、返回商及高效短语法边界见[原位置分解前沿](triple_average_original_position_factorization_frontier.md)。

**最新纯代数模型与判别式边界：** [Reynolds／Hecke／Hodge结构](triple_average_reynolds_hecke_hodge.md)证明所有n>=5的原子生成有理代数等于End(V)，所以不能据完整代数推正向可达。1／3块重数的运输表给出全部普遍可执行层及伴随闭包；单三重块模型无损编码全部原子词，多个三块加双载体模型更小但只作为充分子系统。三元组交数s导致秩n-3-max(0,2-s)。B_p能量Hodge对偶因判别式p的一次赋值，将全部合法方向送到非法线，局部形如[[0,eta],[-p,0]]，正规化Iwahori但交换树边两端。ID reynolds-hodge-structure、contingency-layer-semigroup；最小未解仍53。

当前素数路线的集中入口是[证明路径与剩余猜想](triple_average_prime_proof_roadmap.md)。该页将已证入口、条件性同余生成、已证终端与尚缺的正向种子／算术资源逐层分开，并指出全部Rp资源属于偏强的充分目标，只实现必要Schreier回路或合法轨道也可完成原问题。

**47元历史节点，后续最小未解已更新为71：** [完整证明](../arithmetic_cases/triple_average_forty_seven_arithmetic_complete.md)把新宽度一尖点词接到两个校正伸缩，得到C基下的E12(R)、E21(47R)，R=Z[1/6]。全部18个Schreier生成元的下左条目为0/47/94/141，单位提升和高斯消元逐个正向实现；48陪集与独立标签确认共轭Gamma_0(47)，唯一合法轨道可归零。47已加入solved_size因子闭包，冻结certificate_size不变；53、59随后也已完成。ID n47-complete。

**一般同余生成接口进一步闭合：** [局部化Iwahori生成](triple_average_localized_iwahori_generation.md)用I、ST^j的统一陪集代表，证明Rp=Z[1/(p-1)!]上的正向上根、p倍下根与对角单位足以生成Gamma_0(p)。另证明对所有p和奇数k，特定R_p(3^-k)返回与标准A_p及pZ[1/3]平移产生同一个宽度一尖点。原维数普遍实现这些资源仍开放；47已实例化全部接口。ID localized-iwahori-generation。

**此前47元全库正向逆与统一素数目标：** [正向根群饱和](triple_average_positive_root_saturation.md)证明一般二维迹根激活引理；由九个种子出发，46、113、2三层激活全部167旧模板，连同新增三宏共170个。固定JSON与独立重放无需重新搜索。Q(sqrt89)共轭有57模板正向词；整数换基后包含E12(47Z[1/6])、E21(47Z[1/6])。该阶段未完成的同余与合法轨道部分现由n47-complete补齐。ID b47-root-activation。

该页第6至8节回答素数策略：合数归约、全部p=1 mod3、高维进入与Bezout终端已统一；剩余是p=2 mod3的正向算术生成。明确充分猜想为C Gamma_0(p) C^(-1)包含于真实可逆正向群。此前共轭的限定搜索阴性记录仍保留，已被不同词形的正向实现越过。

**47元新增正向对合及整条局部化根群：** [固定接口](triple_average_b47_extra_atom_and_adjoint.md)在旧两步预备后只加一个原子三平均，得到J、K、L三个全参数对合，实际平方为25/2187、25/2187、8/243。L与旧宏形成三个三因子周期，使标准A0等六宏都可正向取逆。时间词LBAbLa给出U(47)，A0共轭除以-3，词bL的斜率倍率为-2，因此正向群包含全部U(47Z[1/6])。尚无有限指数或完整终端覆盖，47仍开放。ID b47-extra-atom-involutions。

同页提炼(n-1)t+beta=3的对合模板方程；这个单参数对合族的两两乘积共用两条有理特征线，位于同一分裂环面，不能单靠它们生成模群有限指数。已证局部化平移可用于精确整性插值；本轮插值未闭合，停止不表示指数无限。新增extra字段不改变旧模板默认集合或既有短周期排除。

**伴随与共轭数域接口审计：** 倒序子集投影加源核投影形式上给出G^-1 A^T G；只有全部倒序子调用合法才是正向宏，只有A^TGA=lambda G才是射影逆。旧B47的167个形式伴随恒等式全部核对，15个倒序域普遍合法且都已在旧库。Q(sqrt89)目标共轭在额外3/9调用的20426/111393个限定中间态中未找到，不排除其他词形。ID adjoint-return-domain-audit。

**任意秩周期验证已统一：** [全局谱平衡判据](triple_average_projective_spectral_balance.md)将有理A的有限射影阶等价为半单、全部复根等模、c_k^d/det(A)^k全部为整数。有限处由Newton单斜率证明，充分性由Kronecker单位根定理。Ad_A的分圆多项式检测给出给定矩阵的多项式时间精确算法，候选阶只需phi(m)<=d^2、m<=2d^4。它不证明可用宏词存在。ID projective-spectral-balance。

同页第8节补齐可交换数域乘法库的周期存在性接口：对S单位关系格取模有理尺度的饱和商，得到整数矩阵C；非零非负e满足Ce=0等价于正向标量周期，全严格正e等价于全部生成元有正向射影逆。实二次域还需一个单位指数行，不能只消去有限素理想赋值。给定关系矩阵后是有理线性规划；一般S单位基计算未实现、未宣称多项式。高斯范数周期是全正关系的显式实例。

**47元短周期范围已精确封闭：** [库边界](triple_average_b47_cycle_frontier.md)对当前167模板排除全部长度1至4周期及任意j>=0的A0^jBC。4657463三因子、27160不同二因子；四因子737665600组合经整数模筛选仅3896幸存，精确复核全拒绝。浮点发现扫描另保留，不能与该证书混同。ID b47-short-cycle-boundary（full）。其中一个9/27/43调用宏是Q(sqrt89)的范数-2乘法，3处谱平衡却在2处分裂成不同赋值；它说明只看三进处不够。47及任意n仍未解。

**等值载体核与统一二进重分组：** [完整证明](triple_average_paired_carrier_reset.md)用有限模桥安排安全的一步等载体入口，得到(u_i^3,a^2)核。其自然参数格Gram判别为2n*3^(r-2)，纯载体交换保持叶奇偶、故不可能有非空全局标量周期。固定12位置层K4/3通过两遍广播将叶模2矩阵变为J，再一次载体交换，在4r-3步得到W=2V，V为R可逆、det V=-3^(-(3r-2))。两个完整R理想均恰乘2，G保持。

新宏不自动周期：六个秩的迹整性均排除当前单宏有限射影阶，r5/7的全部5160个输出置换也被精确排除；一般标量词若只用W的置换共轭与额外载体交换，两类宏次数均须被r整除。虚拟射影点还存在总和障碍，不能凭两个载体相等就删掉。ID paired-carrier-two-adic-reset；最小未解仍为47。

**四十一元已完整解决，最小未解变为47：** [固定证书](../arithmetic_cases/triple_average_forty_one_arithmetic_complete.md)使用21个通用宏、10个三因子对合周期及10个整数词，独立验证42陪集、共轭Gamma_0(41)、属3及唯一合法尖点。子调用仅3/9/18/27/37/38/39；37使用已证分裂素数定理。完整输入输送由Bezout公式和安全核心完成，41已加入因子闭包。ID n41-complete。

**有限模控制尚不足以给出高度下降：** [统一高度边界](triple_average_modular_height_barrier.md)在(1^(n-2),0,-(n-2))上反复局部载体交换，给出所有有限h的闭式。模任意指定M的正向恒等词保持G=1及本原剩余类，实能量严格下降，但本原高度精确为([4(n-2)^2+4n-11]3^(2h)+3)/4。ID modular-primitive-height-barrier，重放2304个实际操作。该结果不否定新模桥，只说明统一终止还需净实／三进控制。

**一般n=5 mod6的正向二例外归约已证：** [完整证明](triple_average_two_carrier_modular_bridge.md)对每个n>=17（不要求素数）先作r个三元块加两个单位置的同时好划分，再用局部主同余群分别控制模n和模m，m为r=(n-2)/3的非三部分。模n常值稳定子保持全局合法性，保护模n的两个局部SL_r块在模m生成全部SL_(r+1)。有限模逆以统一ord_nm(-1/3)次幂正向实现，最后合法调用已解n-2元子块，输出G=1的(u^(n-2),a,b)核。此桥不依赖安全能量下降或因子归纳。

新桥不解决终止：素数二例外核在n-2非三幂时，单靠这个大子块调用没有安全的非平凡推进。必须区别子问题合法与全局安全；(5^15,1,-76)的15元子调用合法却产生全局G=17陷阱。ID two-carrier-modular-bridge，包含5条共567步的实际正向模调度样本。当前最小未解维数为47。

二例外参数x=u、y=a-b给出2E=n(n-2)x^2+y^2、G=gcd(y,n)；平均a与两个u后一步进入合法B_n，y_B=(nu+2y)/3。因此所有n=5 mod6、n>=17的多素数标准核接口已闭合。第6.1节另给出一般非三profinite原则：无条件R可逆正向宏的有限商像等于形式群像，可以启用任何有限同余适用域，但不能据此声称精确终端可达。

**二十九元已完整解决，最小未解变为41：** [完整证明](../arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)固定18个通用模板、9个三因子正向标量周期和7个整数生成词。精确折叠与独立模29标签给出完整30陪集、共轭Gamma_0(29)、唯一合法尖点及六步终端。全部调用大小仅3/9/25/27；最终证书使用冻结旧库的1194模板，不依赖本轮新增维数或扩展首步。ID n29-complete。29已加入任意幂和因子的闭包。

非分裂射影三阶轨道可在原p位置上组织成三块与二载体，但平移层可能奇异且不交换；p29的奇异位移为8/12/17/21。这解释了高斯范数循环不能直接迁移。ID nonsplit-projective-layer-boundary保留精确有限边界；41元随后由三因子对合和整数子群证书完成。

**全部p=1 mod3素数已统一解决：** [高斯周期正向控制器](triple_average_split_prime_gaussian_controller.md)直接在原p个位置上，以三阶乘法轨道及平移重分组构造高斯周期层。全部共轭的乘积为全局正标量；两个Eisenstein格周期恒等式给出根到根、根到单位坐标的稀疏映射。关键单位theta*conjugate(theta)-1的范数为1，由此对任意素数排除剪切系数的共同分子因子，正向实现所有整数平衡剪切和全部整数仿射行群。两次仿射正规形及一次高斯层消去差分gcd，最后九元网络归零。p=7/13用已证基例，其余p>=19由同一证明覆盖。

结合29、41元后续证书，任意n进一步归约到p=2 mod3、p>=47的素数。已解因子现在允许任意p=1 mod3，以及2、3、5、11、17、23、29、41；所有N>=9的三整除维数仍无条件解决。原子词长度未证明多项式。高斯证明不依赖Tits形式算术性，也未将扩张域作用当作原位置操作。核验ID split-prime-gaussian-controller；solved_size已更新，certificate_size未动。

**原维数形式群的算术性已统一：** [完整证明](triple_average_flat_star_arithmeticity.md)从载体交换构造秩一幺幂、参数4的平衡剪切及行差剪切；结合Tits／Bass--Milnor--Serre初等同余群定理，r>=4的一载体群包含Gamma_r((192(3r+1))^2)，两载体群也含有限指数整数特殊线性子群。因此全部p>=13的原维数平坦核，形式群算术性不再逐素数开放。模2像为交错块置换群，模p像为常值向量稳定子，Goursat引理给出第一层直接乘积；每个合法第一层轨道有含零三重块的代表。尚未证明整体正向逆或更高层全部终端覆盖。ID flat-star-formal-arithmeticity。

**九十一元旧群等式已被否定：** [置换level与尺度耦合](triple_average_permutation_shadow_entanglement.md)发现模91倍率与模8标量共用二阶字符。显式矩阵(547,728;74256,98827)属于旧21504容器却不属于宏群。新必要容器指数43008，有192尖点、48合法尖点、属3473；它到旧属1737紧模曲线是无分歧二重覆盖。未证明宏群等于新容器。旧计算标签保留，91元整体的因子证明不受影响。ID cyclotomic-level-entanglement。

**副本宏的完整算术群已识别：** [数字同余群定理](triple_average_digit_congruence_group.md)证明，n>=5时平衡剪切加置换等于整个整数保和／保常值群，限制到A_(n-1)为B*eta=eta模n的稳定子。若2<=q<=n-2且gcd(q,n)=1，再加入数字算子，恰得到B*eta=q^j*eta模n的同余群；它是阶ord_n(q)的分裂循环扩张。有理射影轨道由d|n及单位c模d对<-1,q>分类，合法d=1只有一个轨道。这是一般整数初等生成证明，不是有限模像推断；正向实现仍在q份副本上。核验ID balanced-digit-congruence-group。

原维数29的当前1195模板另经审计：714610个二因子乘积无有限周期；对任意j>=0，A^jB无有限周期，指数由五个精确二次迹方程一次处理，未作无限深度搜索。见[复核第11节](triple_average_structural_picture_audit.md)，ID b29-current-cycle-boundary。不要继续只增加A重复次数；更长混合词、条件宏及平坦高秩核仍未被排除。

**一次三份复制已足够：** [完整证明](triple_average_one_tripling_stabilization.md)给出数字算子KD=DF与Hilbert90周期，进而在三份副本上正向实现任意平衡剪切。至少五个整数坐标的轨道由总和、差分gcd和共同余类完全分类。结合同时好划分，所有N>=9且3整除N的维数均无条件解决，非三素因子任意；87元无需29元假设，123元同样无需41元假设。一般原维数充分性与复制消去仍开放。

**结构图景新增数域章节的复核：** [独立审计](triple_average_structural_picture_audit.md)保留原稿并给出反例：固定输入的数域扩张不改变可达性，内容理想支撑及所提类群条件并非必要，O_K理想相等也会漏掉R加法模障碍。可用的辅助数域是宏矩阵的分圆Hilbert90及范数环面，不应与改变输入值域混同。核验ID为one-tripling-stabilization。

同一证明的第10节已推广到q平均：n>=max(5,q+2)、gcd(n,q)=1时，q份复制上的完整判据为G=1，核心是两个循环区间之差。原维数新接口见审计第9、10节：任意B_p一步进入三重块加一／二载体；同一组六项Artin关系给出七元局部中心收缩及五步正向逆。局部中心不与其他载体交换对易，拼接仍开放。对n>=9，一旦形成三个零即可用最近的三整除子块统一收尾。

**任意维数已严格归约到素数：** [总归约定理](../proofs/triple_average_all_dimensions_to_primes.md)补齐v2=1、2。2p^e、4p^e的四例外核心用至多两次预备平均加十二元子问题减半；70、110、130的五行边界用一个可变深度梳状分裂修复，其余维数由统一容量强归纳处理。因此原猜想等价于全部素数p>=7的判据，合数接口不再是独立缺口。

因子归约允许任意二、三、五幂及已解奇素数的任意乘积；20、22、26、28等均已补齐。结合分裂素数族和29、41元，所有n>=7且素因子属于2、5、11、17、23、29、41或p=1 mod3均已解决，最小未解维数为47。仍未证明统一素数定理。

**奇数合数的统一乘法闭包已证：** [完整证明](triple_average_odd_composite_factor_closure.md)将进位桥推广到r个例外，并用两个可选系数h=1、2满足行容量。结合n-d-2核心，已解素数集合P>=7的任意乘积和素数幂均可解；35元边界与[25元30陪集证书](../arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)均已补齐，因此可再乘任意三幂和五幂。当前P={7,11,13,17,19,23}；25、35、49、55、65、77、91、121、125、143等无限族已解。

全部奇数现已严格归约到全部p>=7素数：25元不再是条件，二例外入口也不再需要额外假设。25元证书只调用已解21元子问题，具有独立模25标签与唯一合法cusp。91元整体判据已经由7、13因子接口完成；后续耦合字符已证明旧(81,9,1)宏群不等于21504容器，是否等于新43008容器仍开放。

**此前的八整除阶段：** 同一因子容量证明先完成a>=3的二幂因子；新总归约已取消这个限制，因此二进指数也可任意。40、56、88、200等继续是已解族中的例子。

**其他AI报告重新复核：** [局部到整体综合](triple_average_other_ai_local_global_review.md)重新读取AI-3运输与模板、AI-4高秩、AI-5复制报告，给出一个一般结构定理：任意连通的不等权块交换图，在加权零和空间的Zariski闭包为整个GL。证明使用秩一投影与Lie括号，非有限模像外推；算术有限指数和终端覆盖仍未证明。

同页加强交换为完整仿射格保护，并给出非零均值Burau的准确正向逆接口、跨链耦合的秩二公式，以及重新分组副本后一层平均与K/3双随机商的等价。可逆商的秩障碍排除无条件逐层消去。原AI文件保留，新发现与修正由主线综合页登记；当前已解维数不变。

**素数优先的归约推进：** [因子接口与三进进位定理](triple_average_prime_first_factor_reduction.md)把素数算术与合数归约单列。对任意a>=7、b>=3，合法(u^(ab-2),v,w)可在至多ceil(log_3(a的非三部分))次原子操作后分成合法a元行及合法b元均值商。对(1^(ab-2),0,2-ab)且b含非三素因子，这个准备步数精确最优。X49直接七乘七划分失败，但两步进位即修复。

两份与三份复制的加法闭包结合十／十五元定理，可处理任意至少两份合法五元状态，因此因子5不需要假设错误的五元充分性。早期二例外桥已推广到d+2核心，25元和低二进重数接口也均已补齐。剩余统一任务是素数核。

modern frame 已按用户要求[重写](triple_average_unified_modern_framework.md)，[完整原稿](../../history/triple_average_unified_modern_framework_before_2026-09-10_revision.md)已存档且哈希核对一致。修改理由见[主线严格化说明](triple_average_modern_framework_review_and_contract.md)：全体真实宏使用带适用域的有向范畴，只有正向可逆子类形成群胚；终端反向可达集需额外的覆盖与终止证书。

**二十三元已完整解决：** [完整证明](../arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md)用15、17、24步固定原子宏和指数24子群收尾。该模曲线属为2，仍由一个合法cusp完成。它现在作为总归约的素数基例；最小未解维数是29。

**同轮十九元完成：** [完整证明](../arithmetic_cases/triple_average_nineteen_arithmetic_complete.md)通过七个通用十五元调用宏和指数20子群闭合19*3^k。内部调用允许依赖参数；二十三元最终宏已经全部原子化。不要把两种证书的长度混同。

**素数结构与搜索前筛选：** [稳定子和尺度周期定理](triple_average_prime_congruence_structure.md)说明，保持素数p合法方向的群，其整数部分受共轭 Gamma_0(p) 约束；但真实正向群达到这一上界并非自动成立。23处不能复制负三进单位循环，实际成功的尺度是4/27与2/3^7，因此不能丢掉物理比例或忽略2处。整系数编译器缓存重数选择与支撑格，95个十七元矩阵与旧版逐项一致，222个十九元、60个二十三元模板均通过独立 Fraction 重放。

**此前十七元完成：** [完整证明](../arithmetic_cases/triple_average_seventeen_arithmetic_complete.md)构造固定原子逆词，给出共轭 Gamma_0(17) 的指数18充分子群、六步终端和一般进入桥。十九元用的是通用十五元调用，内部路径可能依赖参数，不能把两种证书长度混同。

**一般方法进展：** [参数无关子问题调用与范数环面](triple_average_universal_subproblem_lattice.md)的任意参数维数模包含判据驱动了这次发现。十七元进一步给出统一充分目标：对 n>=9，若真实正向 B_n 群包含 C Gamma_0(N) C^-1，N为n的非三部分、C=[[1,0],[1,1]]，则整个 B_n 核由同一 Bezout 公式收尾。该包含对任意n尚未证明，多危险素数的一般进入桥也仍开放。

历史阶段的五宏有17／19步原子证书和35步调度。那个特定无条件宏半群不含 B 的固定逆词；新增 Q、T、U 宏已打破其模3不变集。48类十四元预备调度的净下降没有被证明，其中一支实际处处增高；完整十七元证明由新的群轨道方法完成，不依赖这个旧调度成为下降算法。

对应的首个[十七元带条件调用实验](triple_average_b17_guarded_subproblem_experiment.md)已生成10个真实返回模板，逐项核验局部整除域与输出合法性。高度24、至多12次调用中542/683个方向可下降或进入已知终端，141个未覆盖，未得到十七元定理。深度指子问题调用而非原子操作。

旧库的缺口已加强为一个有证明的无限不变域：[旧库第5节](triple_average_b17_guarded_subproblem_experiment.md)。历史[奇背景跨核桥](triple_average_b17_cross_stratum_escape.md)给出受限逃逸及一个净下降见证；最新的通用 B 宏调度已去掉该桥的奇偶、模7和模13限制。[同余方法边界](triple_average_congruence_method_scope.md)则说明有限有理轨道原则的准确条件，并给出有限模像很大但指数无限的反例。

**二三光滑维数已统一：** [完整证明](../proofs/triple_average_two_three_smooth_complete.md) 给出对所有 \(8\mid n,\ n\ge16\) 的 B 核安全减半模板，结合八、十二、十八元定理完成全部 \(2^a3^b\ge7\)。该结果包含16、32、64等无限多个二幂及其三进塔。

**结构核接口加强：** [所有偶维 B 核减半](triple_average_all_even_B_kernel_halving.md) 已覆盖任意偶数 \(n\ge14\)。若 \(n/2\) 维可解，则合法 B_n 可解；尚不提供多危险素数一般输入的高维进入桥。

**奇素数维数的策略限制：** [子问题调用的缺失素数障碍](triple_average_subproblem_prime_obstruction.md) 证明：若调用大小都不含某个 \(p\mid n\)，统一有界次数的调用不能覆盖全部合法 B_n 有理方向。因此十七元不能仅靠有限深度的严格更小子问题调用表完成，必须保留可重复的局部归约循环或群轨道机制。这是算法结构下界，不是不可达结论。

**B17 范数环面接口：** [普遍子问题格判据](triple_average_universal_subproblem_lattice.md)中的 B 在 \(\mathbb Q(\sqrt{-2})\) 中是范数3乘法。现在其共轭素元已由61步正向词实现；两个 theta 格分支均有真实操作。核的全覆盖另由级17同余子群完成，两种算术对象的作用不应混同。

本文是在保留全部旧笔记基础上的最新权威索引。阅读时以本文、[研究勘误](triple_average_research_corrections.md) 和各个“完整判据/定理”文档为准；早期探索稿保留发现过程，其中被后续结果替代的开放问题或猜测不应继续引用为当前结论。

**一般结构与十四元完成：** [危险支持集图论核心](triple_average_blocker_graph_core.md) 将安全终端的重复值下界提高为 \(n-d-2\)。借此，[十四元完整判据](../arithmetic_cases/triple_average_fourteen_complete.md) 把最后缺口缩为两个不交危险二元组，并用512个模8／模7模式的至多两步预备操作接入十二元定理与 B14 减半桥，完成 \(14\cdot3^k\) 全部维数。

**十二元完成：** [十二元完整判据](../arithmetic_cases/triple_average_twelve_arithmetic_complete.md) 的四个真实宏含正向逆元，生成一个共轭于 \(\Gamma_0(8)\) 的指数 12 子群，其唯一合法尖点可终止。它解决了 \(12\cdot3^k\) 整条维数族，并被后续十四、十五、十八元归约调用。

**进一步推广：** [十八元及其三进塔](../arithmetic_cases/triple_average_eighteen_via_twelve_complete.md) 已通过调用合法十二元子问题、形成偶重数、分成两份三幂零和块证明。新增 \(18\cdot3^j\) 全部维数，无须单独建立 B18 算术群。B21 深度五已改用整数状态商，同样八进程从约 98 秒降至约 11 秒，见 [性能复核](triple_average_b21_integer_search_optimization.md)。

**十五元完成：** [十五元完整归约](../arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md) 利用模8八循环，先调用十二元子问题，再调用十元子问题归零。新增 \(15\cdot3^k\) 全部维数；不依赖新的十五元大算术群。[偶维 B 核减半桥](triple_average_even_kernel_halving_bridge.md) 本身只解决结构核，十四元一般输入的进入步骤由最新完整证明另行提供。

## 1. 当前总问题

将输入中心化、清分母并本原化，得到

\[
X=(x_1,\ldots,x_n)\in\mathbb Z^n,
\qquad \sum_i x_i=0,\qquad\gcd_i x_i=1,
\]

并定义

\[
G(X)=\gcd_{i<j}|x_i-x_j|.
\]

对任意 $n$，可达都蕴含 $G(X)\mid n$ 且 $G(X)$ 是三的幂。主猜想仍是

\[
\boxed{n\ge7:\quad X\text{ 可达}\iff G(X)=3^a.}
\tag{1.1}
\]

式 (1.1) 尚未证明。若它成立，判定算法只需规范化、求 gcd 和反复除以 $3$，所以直接是输入总位长的多项式时间算法；平均路径是否有多项式长度是另一个更强的问题。

## 2. 已经完整解决的维数

目前已证明：

最新完整族可以统一写成
\[
n=2^a3^b5^c7^{e_7}11^{e_{11}}13^{e_{13}}17^{e_{17}}19^{e_{19}}23^{e_{23}}\ge7,
\]
所有指数任意非负。以下较早的族都包含于这一结论中。

\[
n=3^k;\qquad
n=2^a3^b\ge7;\qquad
n=m3^k\quad(m\in\{7,10,11,13,14,15,17,19,23\},\ k\ge0).
\tag{2.1}
\]

最新再加入整个乘法族
\[
n=3^a5^b\prod_{p\in\{7,11,13,17,19,23\}}p^{e_p}\ge7,
\qquad a,b,e_p\ge0.
\tag{2.2}
\]
这包括35、49、77、91等，不是逐个维数的有限样本结论。

还有全部
\[
n=2^a3^b5^c\prod_{p\in\{7,11,13,17,19,23\}}p^{e_p},
\qquad a\ge3,\quad b,c,e_p\ge0.
\tag{2.3}
\]

这些维数中，$G$ 为三幂是充要条件。五元和六元有 $G=1$ 的反例；结合后续分裂素数族与29、41元证书，最小尚未闭合的 $n\ge7$ 是 $47$。

各基维数证明见：

* (25)：[二十五元完整判据](../arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)；

* 奇数合数乘法闭包及35元：[多例外因子归约](triple_average_odd_composite_factor_closure.md)；

* (23)：[二十三元完整判据](../arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md)；

* (19)：[十九元完整判据](../arithmetic_cases/triple_average_nineteen_arithmetic_complete.md)；

* (17)：[十七元完整判据](../arithmetic_cases/triple_average_seventeen_arithmetic_complete.md)；

* 二三光滑维数：[统一减半与归纳](../proofs/triple_average_two_three_smooth_complete.md)；

* (7,8)：[七元与八元完整判据](../proofs/triple_average_seven_eight_complete.md)；
* (10)：[十元完整判据](../proofs/triple_average_ten_complete.md)；
* (11)：[十一元完整判据](../arithmetic_cases/triple_average_eleven_complete.md)；
* (12)：[十二元完整判据](../arithmetic_cases/triple_average_twelve_arithmetic_complete.md)；
* (18)：[十八元完整归约](../arithmetic_cases/triple_average_eighteen_via_twelve_complete.md)；
* (15)：[十五元完整归约](../arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md)；
* (14)：[十四元完整判据](../arithmetic_cases/triple_average_fourteen_complete.md)；
* (13)：[十三元完整判据](../arithmetic_cases/triple_average_thirteen_arithmetic_complete.md)。

三进塔传播和同时好划分见 [一般维数综合](triple_average_general_n_synthesis.md)。

## 3. 任意维数已经完成的两个归约

第一，[复制稳定化定理](triple_average_stabilization_theorem.md) 证明：

\[
G(X)=3^a
\iff
\text{每个坐标复制某个共同三幂次数后可达}.
\]

它等价于存在 $\mathbb Z[1/3]$ 上的正双随机矩阵 $P$ 满足 $PX=0$。原猜想因而等价于 $n\ge7$ 时的“三份复制消去”。稳定化已经消除了所有复制后仍存在的算术障碍，但没有取消原维数中的额外副本。

第二，[三幂分块压缩定理](triple_average_power_partition_reduction.md) 证明任意合法 \(n\) 元输入可在 \(O(n\log n)\) 次真实三平均后进入

\[
(u_1^{r_1},\ldots,u_t^{r_t}),\qquad
r_i=3^{k_i},\quad t=O(\log n),\quad\sum_i r_i=n,
\tag{3.1}
\]

并保持 $G$ 为三幂。多危险素数的高维组合压缩因此已经统一；未解部分集中在对数秩三幂权重核。

## 4. 最新突破：Burau 幂链群

若式 (3.1) 的权重形成几何链

\[
R s^{t-1},R s^{t-2},\ldots,R,\qquad s=3^k,
\]

相邻块之间的真实扩张宏给出参数 $1/s$ 的 Burau 表示。它们满足 Artin 辫子关系；Coxeter 乘积 $C$ 在加权零和空间上满足

\[
C^t=s^{-t}I.
\]

由此每个相邻宏的射影逆元都能写成正向宏词。换言之，任意秩几何链上的正向平均宏半群自动成为射影群。

完整定理与证明见 [Burau 幂链定理](triple_average_burau_power_chain.md)。它统一了十三元 $(9,3,1)$ 核中的三阶分圆关系，并给出 $(27,9,3,1)$ 核上参数空间维数为三的可逆 Burau 返回群；尚未给出其完整下降控制器。

这个结果没有直接证明一般核可达。关键边界是：几何链必须对自身加权零和，嵌入更大核后的非零链平均会阻止正词成为整个状态上的射影逆元。一般问题现在具体化为“链之间转移加权和”以及“Burau 像是否足够算术”两件事。

## 5. 九十一元支线的最新复核

**当前总状态：91元已经由奇数合数因子定理完整解决。** 以下保留旧(81,9,1)独立局部容器的支线；后续耦合字符已证明该21504容器严格过大，新43008容器见本页顶部链接。

核

\[
(u^{81},v^9,-81u-9v)
\]

仍有统一的三个真实宏，但旧的群论候选需要两处修正。

第一，本原化允许差值乘子属于

\[
\langle-1,3\rangle\subset(\mathbb Z/91\mathbb Z)^\times,
\]

而不是只用 $\langle-1,9\rangle$。只记录模 $91$ 行标签与模 $2$ 奇偶时得到指数 $1344$ 的粗容器。

第二，真实整数返回宏还带有模 $8$ 条件。当时的独立局部容器使用六元素局部像

\[
L_8=\langle C_9,3I\rangle,
\]

指数为

\[
21504.
\]

这个历史容器有 $96$ 个尖点，其中 $24$ 个满足 $G=1$，恰为六个模 $91$ 差值类各分四个二进尖点。现在已经证明真实整数宏群严格包含于它，不能把这组尖点当成实际宏群的完整轨道分类。

旧缺失类代表也曾写错：对 $(u,v)=(1,-3)$，单独坐标是 $-54$，不是 $-72$。正确两步路径为

\[
(1^{81},(-3)^9,-54)
\to(1^{81},(-3)^7,(-20)^3)
\to(1^{79},(-3)^7,(-20)^2,(-6)^3).
\]

其中 $1^{21},(-3)^5,-6$ 是 $27$ 元零和块；归零后剩余 $64$ 个非零位置与 $17$ 个新零组成 $81$ 元零和块。因此六个模 $91$ 差值类都存在终端。深度四的离核搜索覆盖旧容器中 $23/24$ 个合法尖点；随后对尖点 $29$ 的深度五搜索又得到一条五步证书，完成旧容器的 $24/24$ 有限深度覆盖。它不自动覆盖新容器的48个合法尖点；该支线不再承担91元整体判据的证明。

## 6. 现阶段最接近一般证明的结构

目前可以把全局路线画成

\[
\text{任意合法输入}
\longrightarrow
\text{对数秩三幂核}
\longrightarrow
\text{几何链 Burau 群与链间耦合}
\longrightarrow
\text{零和三幂终端块}.
\]

第一箭头已经证明。第二层中的单条几何链已经群化。真正未解的是：

1. 把任意三幂权重多重集组织成少量链，并在链之间可控地移动加权和；
2. 证明所得高秩返回群是足够大的算术群，而不是薄群；
3. 证明每个满足全部非三局部条件的有理轨道都与某个零和三幂子块相交；
4. 或者从复制稳定化一侧，直接证明这些核上的三份复制可以消去。

十三元的参数格维数为二，相应 PGL2 的群秩为一。Burau 定理提示研究更高参数维数的算术群与终端超平面；奇异降维宏另属分层间有向对应，不能全部视为群作用。

## 7. 哪些文档应如何阅读

已证明定理、总纲与勘误：

* [研究总纲](triple_average_master_summary.md)
* [研究勘误](triple_average_research_corrections.md)
* [复制稳定化](triple_average_stabilization_theorem.md)
* [三幂分块压缩](triple_average_power_partition_reduction.md)
* [Burau 幂链](triple_average_burau_power_chain.md)
* [可填充三幂块](triple_average_zero_padding_theorem.md)
* [单危险素数降维](triple_average_isolated_prime_reduction.md)
* [多危险素数核心](triple_average_multi_prime_core.md)
* [加强图论核心](triple_average_blocker_graph_core.md)：将上一项的 \(n-3d-1\) 提高为 \(n-d-2\)，且明确一步 B 核桥并非自动安全。
* [二三光滑维数](../proofs/triple_average_two_three_smooth_complete.md)：通过十二元子问题统一消去额外二因子。
* 上述九个已解决起始维数的完整证明（12、15、18 含三因子，分别是一条新传播塔的起点）。

严格接口、条件定理和开放猜想：

* [标准核接口与自守路线](triple_average_kernel_interface_and_automorphic_route.md)
* [q-平均根格与 \(S\)-算术控制器](../../general_arity/triple_average_q_average_arithmetic_geometry.md)
* [三进扩张修复宏与算术接口](triple_average_carry_repair_and_arithmetic_interface.md)：含一般宏族与下界证明，完整控制器仍开放。
* [B12 六步下降与导子塔](triple_average_b12_six_step_and_conductor_tower.md)：保留十二元闭合之前的局部范数路线，以及严格 theta 子格公式。
* [十二元四宏的参数延拓](triple_average_twelve_macro_family_extension.md)：三个真实宏可延拓，但已用的二阶和抛物关系只在十二元成立。
* [偶维 B 核减半桥](triple_average_even_kernel_halving_bridge.md)：对 \(n=2\pmod4,\ n\ge14\) 给出调用八元子块的减半接口。

有限实验与审核记录：

* [B12 二维核有限实验](triple_average_b12_kernel_experiment.md)
* [四维数核比较](triple_average_single_prime_kernel_comparison.md)
* [外部 audit 修订记录](triple_average_audit_resolution_2026-09-09.md)

结构解释文档仍然有用，但应连同勘误阅读：

* [根格与一般维数综合](triple_average_general_n_synthesis.md)
* [算术几何视角](triple_average_arithmetic_geometry_view.md)
* [测度、托里克与重写视角](triple_average_barycentric_toric_view.md)
* [覆盖设计障碍](triple_average_covering_design_obstruction.md)
* [见证重置](triple_average_witness_reset_lemma.md)

早期探索记录包括 `ternary_averaging_*`、`binary_vs_ternary_averaging_followup.md`、`triple_average_global_breakthrough.md`、`triple_average_arbitrary_n_outlook.md` 与 `triple_average_thirteen_macro_frontier.md`。它们保存搜索过程和局部引理，但其中“待解决维数”、旧公式、算法边界或实验外推可能已经被后续文档替代。

## 8. 核验入口

完整的“结论—文档—脚本—命令—输出—证据边界”映射见 [计算核验指南](../../algorithms/triple_average_verification_guide.md)。机器可读清单为 `work/verification_manifest.json`，统一入口为：

```text
python work/run_verifications.py --list
python work/run_verifications.py --profile smoke
python work/run_verifications.py --profile core
```

其中最关键的精确核验为：

```text
work/verify_thirteen_arithmetic_group.py
work/verify_twelve_arithmetic_group.py
work/verify_stabilized_averaging.py
work/verify_power_partition_compression.py
work/verify_burau_power_chain.py
work/cyclotomic_congruence.py
work/analyze_n91_terminal_cusps.py
```

Burau 核验对 $3\le t\le8$、$s=3,9$ 的十二组参数全部通过。九十一元脚本区分“真实宏群”“已知同余容器”和“终端覆盖”，不再把粗模 $91\times2$ 标签误当作完整群。

九十一元深度四的 $23/24$ 用

```text
python work/analyze_n91_terminal_cusps.py --depth 4
```

重现；脚本默认深度为 $2$，覆盖 $14/24$，深度 $3$ 覆盖 $20/24$。优化后的深度 $4$ 默认使用全部逻辑处理器，本机实测约 $14.2$ 秒（前一版整数 DP 约 $118$ 秒），找到尖点 $30,32,35$ 的新证书。随后对唯一开放的尖点 $29$ 使用

```text
python work/analyze_n91_terminal_cusps.py --cusp 29 --depth 5 --jobs 8 --split-depth 2
```

在本机用时约 $273$ 秒，得到五步终端证书，因此已知同余容器内的 $24/24$ 个合法尖点均有有限深度见证。程序中的 `OPEN` 是有限深度内未找到见证，不是不可达证明；$24/24$ 仍不等于真实返回宏群等式，也不替代任意输入进入二维核的桥。性能剖析与优化依据见 [计算性能审计](../../algorithms/triple_average_computation_performance_audit.md)。

## 9. 当前结论

现在还不能宣布任意 $n\ge7$ 已解决，但它已经严格等价于全部素数p>=7的判据。d+2核心、奇数因子桥、低二进减半及有限边界修复共同闭合了所有合数归约。结合分裂素数统一证明和29、41元证书，最小未解维数为47。下一步可在最小反例素数p的假设下使用全部更小维数已解子问题，集中研究非分裂正向控制；复制消去仍为等价路线。有限模调度本身没有控制本原高度，必须另证整个词的净下降或全局周期。
