# 历史推导、失败路线与审计 · 第9分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [主线与三个并行研究方向的交接](#doc-2502363be5e5)
- [参数无关宏编译器与范数环面：从 B17 走向任意 n](#doc-8f04e14412f7)
- [十三元二维核：已得到的真实宏与剩余的三进高度问题](#doc-65008db4ce35)
- [三进运输稳定化：双随机返回与复制消去的精确接口](#doc-7df3f977b1d7)
- [十二元四宏的参数延拓及其关系边界](#doc-ddf371bd56cf)
- [有限模控制的正向实现：所有 n=5 mod6 的二例外归约](#doc-aea582e02f93)
- [三平均的统一框架：带局部条件的有向操作与算术轨道](#doc-c83fe1b45f9c)
- [参数无关子问题调用：局部化整数模判据与十七元新宏](#doc-a20253f0d3b0)
- [危险素数的见证重置：局部约分为何必须纳入一般算法](#doc-35981543be1f)
- [可填充三幂块的统一收尾](#doc-22abc15be049)
- [有界切换之后的文献调查：Lucas赋值、混合逼近与Hecke周期](#doc-07cd1b56f163)
- [五元问题的定向外部调查与适用性审查](#doc-a0991a965356)
- [全词逃逸方向：外部定理的实际贡献与适用边界](#doc-14572e4b2cbe)
- [整体结构调查的文献访问记录](#doc-16059490fecd)

---

<a id="doc-2502363be5e5"></a>

## 原文导签：主线与三个并行研究方向的交接

来源：`outputs/triple_average/history/triple_average_team_handoff_2026-09-10.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_team_handoff_2026-09-10.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-2502363be5e5 -->
# 主线与三个并行研究方向的交接

2026-09-11最新交接：[双三重值不变量](../sources/outputs/triple_average/proofs/triple_average_prime_double_triple_invariant.md)直接证明全部素数 p>=11 的合法整数零和状态可在原位置、一位额外三进精度内归零。结合既有七元与合数归约，n>=7 的 G 判据闭合。此前“最小未解71”和“必须补正向种子”的说法已成为历史状态；指定返回和复制消去仍是独立加强问题。下一步集中审查新证明及构造长度，见[二平均原文与文献复盘](../sources/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)。新核验ID `prime-double-triple-invariant`。

更新时间：2026-09-10。主线程继续负责全局证据登记，不覆盖三个独立研究方向的报告。AI-3、AI-4、AI-5 的历史记录和共享文件均保留；当前是否运行须以实际协作工具和进程状态为准，不能由本文推断。

2026-09-11新增主方向：[载体扫掠催化器](../sources/outputs/triple_average/history/triple_average_carrier_sweep_catalyst.md)证明一般三重叶扫掠为1/3乘整数幺模矩阵；三叶十位置窗口产生12个具有同长度正向逆的根。四个固定共轭根显式包含E3(4320^2 Z)，所以整数有限指数已闭合。进一步的80锥、812叶精确下降证书把模20碰撞提升为任意有理十位置窗口的有限碰撞定理；碰撞再经一／两步进入等载体并保持完整仿射模。重叠窗口仍有明确障碍：局部中心收缩使相邻窗口本原高度按3^(8k)-1增长，所以局部Q不能直接拼成全局良序。下一条路线必须同步窗口尺度或冻结零和块。

最新统一条件定理：[混合单点迹零返回](../sources/outputs/triple_average/history/triple_average_mixed_singleton_controller.md)给出一条覆盖全部p=2 mod3素数的充分路线。取最小平方自由素数支撑B后，周期、仿射交换子、两个下根和显式Bezout已经给出完整U(R)、L(pR)，对角吸收完成合法轨道与终端；三幂副本运输也已构造。该路线的唯一缺口是原p位置分解，两个指定返回却不是原猜想的必要条件。精确半群方程和已排除的短语法见[原位置分解前沿](../sources/outputs/triple_average/history/triple_average_original_position_factorization_frontier.md)。

## 主线新增的可用结果

最新结构：[Reynolds／Hecke／Hodge模型](../sources/outputs/triple_average/history/triple_average_reynolds_hecke_hodge.md)。全部n>=5原子生成代数都是End(V)，不区分可达性；固定1／3重数的运输表完整参数化可执行层并自动伴随封闭，单三重块模型无损编码全部原子词，多个三重块双载体模型给出较小的充分猜想。能量规范四分之一转在危险p处交换Iwahori树边，将合法方向送进非法线，因此不能由伴随封闭直接推出正向逆。最小未解仍53，新增两个独立核验ID。

历史节点：[47元已解](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_seven_arithmetic_complete.md)。固定宽度一尖点词、两个校正伸缩及18个Schreier回路的正向高斯分解，给出共轭Gamma_0(47)的48陪集证书。统一高维桥和Bezout输送完成任意合法47元输入，47加入因子闭包；此后53、59也已完成，当前最小未解为71。ID n47-complete。

最新一般接口：[局部化Iwahori生成](../sources/outputs/triple_average/history/triple_average_localized_iwahori_generation.md)证明任意p的显式根／单位资源足以生成Gamma_0(p)，并给出任意奇次三进返回产生宽度一尖点的一般公式。剩余任务是普遍正向实现资源，不能把局部化环中的分母直接当成允许的平均元数。

此前47元：[正向根群饱和](../sources/outputs/triple_average/history/triple_average_positive_root_saturation.md)已完成旧167宏的全部正向逆，固定170节点证书分三层46/113/2。原二次共轭目标有57模板正向实现，两个完整47Z[1/6]相对根群为最新同余证明提供输入。

此前47元：[extra-stage正向对合与47Z[1/6]根群](triple_average_b47_extra_atom_and_adjoint.md)。三个新对合、标准A0等六旧宏的正向逆、固定U(+-47)和二／三进共轭均已核验。倒序伴随域另审计167模板，仅15通过且未新增矩阵。

最新：[任意秩全局谱判据](../sources/outputs/triple_average/history/triple_average_projective_spectral_balance.md)提供给定宏矩阵的精确分圆周期验证；[B47固定库边界](../sources/outputs/triple_average/history/triple_average_b47_cycle_frontier.md)排除长度至多4及所有A0^jBC周期。四因子排除用整数模筛选，不依赖浮点。当前未解起点仍是47，应换词形或宏族而非重复同一范围的短搜索。

最新一般接口：[等值载体二进重分组](../sources/outputs/triple_average/history/triple_average_paired_carrier_reset.md)，4r-3次原平均实现W=2V、V为R可逆并保持本原G。它克服纯载体交换的叶奇偶保持，但不证明全局周期或终止。ID paired-carrier-two-adic-reset；未解维数仍从47开始。

最新：[41元完整证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_one_arithmetic_complete.md)已经通过，最小未解维数为47。新发现工具按行列式平方类作两端拼接，只保存两字母状态，再补一层整数共轭；正式核验固定21宏、10周期、10整数词及42陪集。另有[有限模调度的高度反例族](../sources/outputs/triple_average/history/triple_average_modular_height_barrier.md)，说明原始实能量下降不控制本原高度。

一般接口：[n=5 mod6正向二例外桥](../sources/outputs/triple_average/history/triple_average_two_carrier_modular_bridge.md)，包含合数。混合块保护、有限模主同余控制和n-2子调用将全输入送入合法二例外核；没有证明其统一终止。核验ID two-carrier-modular-bridge。当前最小未解为47。

最新：[29元已完整解决](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)，正式入口n29-complete。冻结旧库18模板、九个三因子正向周期和七个整数词给出完整30陪集。29已加入因子闭包，最小未解维数为41。非分裂射影层的直接范数迁移失败边界另行核验，不影响29元新证明。

最新：[全部p=1 mod3素数已解](../sources/outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md)。高斯周期层在原位置数上提供全局正向逆，范数一分圆单位给出本原剪切，整数仿射行群完成统一归零。一般n现在只剩p=2 mod3的素数入口，最小29。对应ID split-prime-gaussian-controller，旧证书库保留。

最新：[平坦核形式算术性](../sources/outputs/triple_average/history/triple_average_flat_star_arithmeticity.md)统一全部p>=13的一／二载体形式群有限指数，原维数整体正向逆仍未解决。[九十一元字符耦合](../sources/outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md)则否定旧21504群等式，给出43008必要容器及无分歧模曲线二重覆盖。原独立报告、旧缓存和旧容器编号均保留。

**总归约已完成：** [任意维数到素数](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_to_primes.md)补齐2p^e／4p^e的统一十二元减半及70／110／130可变梳状边界。全部n>=7严格归约到p>=7素数；合数接口不再独立开放。所有23光滑维数n>=7已解，最小未解维数为29。入口为 even-prime-power-halving 与 all-dimensions-prime-reduction。

**奇数合数统一归约已证：** [多例外进位定理](../sources/outputs/triple_average/history/triple_average_odd_composite_factor_closure.md)直接处理现有d+2核心；[25元30陪集证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)和35元边界均已补齐。已解p>=7素数的任意乘积、任意素数幂，再乘任意三幂和五幂，都已完成。全部奇数严格归约到全部p>=7素数。入口为 n25-complete 和 odd-composite-factor-closure。91元已由7*13接口完成；旧21504容器等式后来已被否定。

**此前八整除族：** 新总归约已推广到所有二进指数，整体40元等继续是已解实例；旧(27,9,3,1) Burau群的整数有限指数没有因此自动证明。

**重新审阅AI-3/4/5后的接口：** [完整复核](../sources/outputs/triple_average/history/triple_average_other_ai_local_global_review.md)证明任意连通不等权交换图的Zariski闭包为GL_(t-1)，并将交换安全性提升为完整仿射格不变；非零均值链的Burau逆实现准确为中心收缩乘以形式逆，多个链可同步，跨链不交换缺陷秩至多2。副本重新分组的一层操作恰对应全部K/3整数双随机商，但可逆商阻止全空间统一原子下降。主线验证入口 other-ai-local-global-synthesis；不声称算术有限指数或一般终止。

**历史二例外接口：** [原进位桥](../sources/outputs/triple_average/history/triple_average_prime_first_factor_reduction.md)的最优准备步数结论保留；后来多例外构造已处理d+2核心，25元及低二进接口也已闭合，无须额外二例外入口假设。

**最新已解素数：** [二十三元](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md)具有固定原子宏、正向标量循环及24陪集充分子群。入口为 n23-complete。当前最小未解维数是29。

**同轮完成：** [十九元及其三进塔](../sources/outputs/triple_average/arithmetic_cases/triple_average_nineteen_arithmetic_complete.md)通过通用十五元调用和20陪集充分子群收尾，入口为 n19-complete。其内部子问题路径可依赖参数，与二十三元固定原子词不同。

**一般结构：** [素数稳定子与实际尺度周期](../sources/outputs/triple_average/history/triple_average_prime_congruence_structure.md)解释同余level的必然来源，并排除23处实际尺度为负三进单位的通用循环。它不证明每个素数的真实宏都达到算术稳定子。搜索先经过整系数状态、重数与支撑格缓存优化，十七元95矩阵保持一致。

**此前完成：** [十七元及其三进塔](../sources/outputs/triple_average/arithmetic_cases/triple_average_seventeen_arithmetic_complete.md)具有固定原子逆词和18陪集证书。十九元的十五元内部路径允许依赖参数，不应沿用十七元的固定原子长度说法。

此前阶段：[普遍子问题模判据与 B17 范数环面](../sources/outputs/triple_average/history/triple_average_universal_subproblem_lattice.md)。任意参数维数的通用子块条件等价于局部化整数模包含。B 的整数代表为 [[7,2],[-33,-9]]，经 (x,y)=(u,4u+v) 后是乘以 -1-sqrt(-2)，范数乘3；其模5为完整六循环。该页保留局部调度阶段；现在共轭素元正向实现和 B17 全部终止已经由新增宏完成。

旧五宏有17／19步固定原子证书；其模3逆词障碍只针对当时的库，不能套用到新增 Q、T、U。旧十四元预备调度仍未控制总高度增长，完整证明走新的群轨道路线。一般研究应利用参数化宏编译和充分同余子群目标，继续处理多危险素数桥及复制消去。

1. [图论核心定理](../sources/outputs/triple_average/history/triple_average_blocker_graph_core.md)：对 n 至少7的本原合法整数状态，若不存在补集保留各非三见证的非恒等整数三平均，则有至少 n-d-2 重的实际值，d 是危险素数个数。这是一般证明，不是有限搜索。d=1、2各有达到等号的例子。
2. [十四元完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_fourteen_complete.md)：危险集相交时一步进入合法 B14；不交时只剩两个二元组，512类模8／模7证书至多两步后可调用十二元定理并进入 B14。再用八元子问题和七元减半收尾。n14及其三进塔已解。
3. [二三光滑统一减半定理](../sources/outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md) 已闭合全部 \(2^a3^b\ge7\)。其他已解决起始维数包括7、8、10、11、12、13、14、15、17、18、19、23，以及所有三幂；均可向上乘以三幂传播。B21早已是七元塔的已知例子。

核验入口：

补充接口：[所有偶维 B 核减半](../sources/outputs/triple_average/history/triple_average_all_even_B_kernel_halving.md) 已覆盖任意偶数 \(n\ge14\)：至多一次预备三平均加合法八元／十二元调用，即形成两份合法 \(n/2\) 元状态。所有非三见证在压缩后保留；多危险素数的一般输入仍须独立进入 B 核。新的独立入口为 all-even-B-kernel-halving。

    python work/run_verifications.py --id blocker-graph-safe-core --id n14-complete

有限图检查和余数证书检查的证据范围分开。十四元整个证明还依赖独立的七、八、十二元完整定理，不能把子问题的均值赋值当成一次原子平均。

新增一般限制：[缺失素数定理](../sources/outputs/triple_average/history/triple_average_subproblem_prime_obstruction.md)。若所有子块调用大小与某个 \(p\mid n\) 互素，则每个调用词在 B 核上都是非零线性映射，只能消灭至多一条射影方向。无限多个合法方向不可能由统一有界次数覆盖。对素数维数17，任何严格更小的子问题都符合这个障碍；应优先构造可迭代局部控制，而非继续加深一个希望一次覆盖全部参数的模板库。此结论不排除位长多项式算法。

## 给 AI-3

一般安全进位充分条件已在 [扩张修复与算术接口](../sources/outputs/triple_average/history/triple_average_carry_repair_and_arithmetic_interface.md) 中证明：t至少7、h个同权块满足 h(h-1)>6d 时可保留全部非三见证合并。新 n-d-2 核心使用危险支持集的二元子边及普通图连通分量，可能适合强化多素数核的势函数。不要据 n-4 重数直接推一步 B 核桥；危险支持集不交的反例是真实存在的。

主线复核意见（报告修改权仍归 AI-3）：

- “一条链归零则非零链数严格下降”需要接收链原本非零等附加条件。例如链和 (1,0,-1) 经转移变为 (0,1,-1)，非零链数不变。势变化公式本身仍正确。
- 示例 (1,1,5,0,0,0,-7) 合并后清分母为 (7,7,7,0,0,0,-21)，坐标内容也是7，本原 G仍为1。它只证明未本原化的模7见证消失，不证明本原合法性被破坏。若需后者，可用主线已证的 (-2,-1,-1,1,1,1,1) 合并前三值得到 G=7 的例子。
- 当前报告的条件终止论证在这两点修订前，不作为主线一般终止性结论使用；跨链交换和加权和公式可独立引用。

- 模板报告的T1在r=m+1、T2在r=m-2边界缺少系数0，不能硬设Smith gcd为1；例如T1的(n,m)=(8,3)有g=2。脚本已按实际支撑重算并正确拒绝该边界，因此正文简化式与程序证据须区分。有限输出中的“admissible”还需另查子问题大小是否已解。

## 给 AI-4

十二元已有确切正向可执行子群，共轭于 Gamma_0(8)，指数12、四尖点、唯一合法尖点，见十二元完整证明。九十一元21504标签为历史必要容器，现已证明严格大于实际整数宏群；新的耦合必要容器指数43008。高秩 Burau 的正向逆元要求整条链自身加权零和，嵌入非零平均子链时须保留常值方向。

本线程已读取四块报告，但尚未独立重跑其有限模像计算。报告中“射影三维空间”应明确为三维向量空间的射影平面 \(\mathbb P^2\)；“Burau 控制器”若只核验群关系，应称可逆返回宏族，不能暗含所有方向都有下降和终端。t=5、6的同类审计仍须分别给出实际证据。

最新复核已用三个生成元直接重算模2、5、7的射影轨道表，不再为轨道问题遍历完整有限群。一般Zariski闭包现由秩一Lie证明解决；其余算术有限指数、正向终端和高秩局部标签仍开放。原深度8整返回库及其全部有限群阶未在本轮重跑，不能视为新增核验。

## 给 AI-5

十二、十五、十八元完整定理推出：四、五、六元的任意合法状态复制三份后都可达；原维数仍有不可达状态，所以这不是复制消去。对 n至少7的复制消去仍为全局开放方向。新版仿射格子问题判据位于十五元证明：G_C=s/gcd(s,T)，目标均值属于 a+dZ[1/3] 当且仅当局部 G 为三幂，只有已解决的子问题大小才能据此调用。

已看到复制消去报告中的同步路径与矩阵商区分。三个共轭矩阵相加并除以三是算术平均；三个共轭路径串联产生的是矩阵乘积。两者不能互换。该表述已在代理报告中修正，配套脚本已用精确 Fraction 运行通过。

## 统一视角

modern frame 的逐项主线复核见[严格化契约](../sources/outputs/triple_average/history/triple_average_modern_framework_review_and_contract.md)。主文件已按用户要求重写，完整旧稿存档在 history/。其中给出条件箭头的复合域、终端反向可达集、无限字母表的限制，并说明缺失素数定理为何要求某些局部控制图有可迭代循环；不以统一命名代替未证选择引理。

主线已将它用于[B17 条件调用](../sources/outputs/triple_average/history/triple_average_b17_guarded_subproblem_experiment.md)：10个自动生成且附有输入整除域的返回模板，来自已解十三、十四、十五元子问题。该旧库后被证明有无限局部陷阱；[历史跨核桥](../sources/outputs/triple_average/history/triple_average_b17_cross_stratum_escape.md)和通用模判据先后绕开它，最终新增的正向群证书完成十七元全局终止。

三个代理的结果现在统一到[现代框架](../sources/outputs/triple_average/history/triple_average_unified_modern_framework.md)：AI-3 给出不同权重核之间的真实运输态射；AI-4 给出固定几何链的高秩 Burau 自同构及其有理旗标边界；AI-5 说明复制消去是一个有向重写范畴的商函子问题。三者共同留下的目标是分层操作群胚上的有限型有向吸引域，而不是继续为每个维数单独猜测返回群。

主线对该框架的定义补充：全体真实宏包含不可逆、奇异、降维箭头，应首先构成有向范畴；只有被证明具有正向逆元的子类才是群胚。“只除三进单位”还不自动等于 \(\mathbb P^{t-2}(\mathbb Q)\)：必须先选 away-from-3 本原代表，或改为对所有非零有理数取商。原子操作与宏的可达性标签、以及静态 theta 与动态正向 Hecke 的区别，仍以已定义的标准接口为准；不能从统一命名本身获得新的终止定理。

## 所有权与证据

AI-3、AI-4、AI-5的独立文件保持各自修改权。主线程只在报告与脚本具备稳定声明、明确范围并完成复核后登记 manifest。共享文件出现不等于任务完成，也不等于其所有声明已经被主线程采纳。

<!-- END SOURCE doc-2502363be5e5 -->

---

<a id="doc-8f04e14412f7"></a>

## 原文导签：参数无关宏编译器与范数环面：从 B17 走向任意 n

来源：`outputs/triple_average/history/triple_average_template_compiler_and_torus.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_template_compiler_and_torus.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-8f04e14412f7 -->
# 参数无关宏编译器与范数环面：从 B17 走向任意 n

这份笔记把最新的两个结果合并成一个可推广的研究接口：

1. 用 Smith 标准形在参数代入前判断一个已解子问题是否对所有参数合法；
2. 把由此得到的二维返回宏放进一个 (S)-算术环面或更一般的代数群中。

它不声称已经证明任意 (n)。它给出的是一个能逐项生成、检查和复合的统一宏系统。

## 1. 宏模式而不是数值状态

设一个标准核有 (d) 个参数 (z)，其实际位置值写成线性形式

\[
f_i(z)=a_i z,qquad a_i\in R^d,qquad R=\mathbb Z[1/3].
\]

取一个大小为 (s) 的子块，系数向量为 (a_{i_1},\ldots,a_{i_s})。选锚点 (a_{i_1})，定义

\[
L=\sum_j R(a_{i_j}-a_{i_1})\subseteq R^d,
\qquad
\delta=\frac1s\sum_j a_{i_j}-a_{i_1}.
\]

如果子问题大小 (s) 已有完整三平均判据，那么这个子块对所有参数都可以调用，当且仅当

\[
\boxed{\delta\in L.}
\tag{1.1}
\]

原因是目标均值必须属于子块的仿射 (R)-格；对所有参数成立等价于系数级的格包含。由于 (R) 是 PID，(1.1) 可以由 Smith 或 Hermite 标准形在有限步内决定。这个判据自动保留共同因子和非三素数，不依赖抽样参数。

因此一个宏模式的正确数据不是“某个参数成功”，而是：

\[
(	ext{位置重数},	ext{系数矩阵},	ext{Smith 不变量},	ext{输出矩阵},	ext{适用域}).
\]

## 2. 复合域是宏系统的核心

若一个宏 (e) 将权重核 (mathbf r) 映射到 (mathbf s)，系数映射为 (M_e)，其适用域为 (D_e)，随后宏 (f) 的适用域为 (D_f)，则复合并非只有矩阵乘法：

\[
M_{fe}=M_fM_e,
\qquad
D_{fe}=D_e\cap M_e^{-1}(D_f).
\tag{2.1}
\]

每一步还必须保留真实位置账本。这样得到的是一个带域的有向范畴；只有已证明存在正向逆词的等维箭头才可以取为群胚中的可逆部分。

这给出一个宏编译器的抽象算法：

1. 枚举有限的重数模式；
2. 用 Smith 数据筛掉不具备参数无关合法性的子块；
3. 计算输出线性矩阵；
4. 用局部模条件筛掉输出不合法的矩阵；
5. 记录复合域，而不是只保存矩阵；
6. 对终端调用附加完整位置收尾证书。

这个算法可以自动发现 B17 中的五个非平凡通用宏。它把原来的数值搜索改成系数模和有限重数模式的搜索。

## 3. B17 的范数环面

B17 标准核为

\[
\mathcal B_{17}(u,v)=(u^{13},v^3,-13u-3v).
\]

最新通用宏之一的整数射影矩阵为

\[
\widehat B=
\begin{pmatrix}7&2\\-33&-9\end{pmatrix},
\qquad
\det\widehat B=3,
\qquad
\operatorname{tr}\widehat B=-2.
\tag{3.1}
\]

令

\[
x=u,qquad y=4u+v.
\]

则

\[
(x,y)\longmapsto(-x+2y,-x-y),
\]

这是 (mathbb Z[\sqrt{-2}]) 中乘以

\[
\alpha=-1-\sqrt{-2}
\]

的线性作用。对应范数为

\[
q(u,v)=u^2+2(4u+v)^2,
\qquad
q(\widehat Bz)=3q(z).
\tag{3.2}
\]

这里的 3 分解为

\[
3=\alpha\bar\alpha.
\]

这给出一个严格的 (S=\{3,\infty\}) 算术对象：

- 在无穷处，(mathbb Q(\sqrt{-2})) 变成复数，范数环面是紧圆方向；
- 在 3 处，3 分裂，(alpha) 与 (ar\alpha) 是两个局部素元方向；
- 在 5 处，5 惰性，(mathcal O_K/5) 的范数一环面有 6 个元素，(widehat B) 的作用正好产生六循环。

因此 B17 的模 5 调度不是偶然的有限表，而是非分裂环面在有限域上的传递作用。

这类解释能提供局部轨道、范数和 theta 恒等式；它不能自动给出 (ar\alpha) 方向的正向平均宏，也不能自动给出范数下降。正向实现仍是原问题自己的动态约束。

## 4. 一个可推广的条件模板

对任意二维核，若存在参数无关真实宏 (M) 满足：

\[
\det M=\ell^e,qquad
\chi_M(T)=T^2-tT+\ell^e,qquad
t^2-4\ell^e<0,
\]

则 (M) 在一个虚二次域的范数环面上给出一个有理同源。若进一步存在：

1. 一个正向宏实现共轭素元或其有限指数替代；
2. 一个有限的非三局部调度器；
3. 一个在本原约分后严格下降的 (S)-算术高度；

那么可以把“有限模调度 + 范数下降”组织成一个循环控制器。

这是条件定理，不是 B17 或任意 (n) 的完成。它明确指出外部数论真正能提供的接口：环面、局部轨道、理想分解和 theta 数据；还缺少的部分是正向三平均词和全域下降选择引理。

## 5. 面向任意 n 的统一状态机

把每个宏模式压缩成状态

\[
\Sigma=(\mathbf r,\Lambda,\Omega,M,Q,h),
\]

其中：

- (mathbf r) 是三幂权重；
- (Lambda) 是参数系数生成的 (R)-格；
- (Omega) 是非三局部合法域；
- (M) 是真实宏的有理矩阵；
- (Q) 是实二次型或范数；
- (h) 是本原化和参数格尺度。

宏复合给出带域的有向边

\[
\Sigma\xrightarrow{(M,D)}\Sigma'.
\]

固定几何链时，边的可逆子图是 Burau 群；调用已解子问题时，边跨越不同权重分层；危险素数桥和复制同步则是额外的奇异边。

于是任意 (n) 的目标可以写成一个参数化控制器命题：

> 对每个 (n)，由 Smith 格编译器生成的带域宏图，是否存在一个可计算的良序标签，使所有合法状态沿循环或跨分层边最终进入完整零和三幂终端？

这个命题比“真实宏群是算术群”更弱，也更贴近原始操作；它允许不同核使用不同的群、环面或子问题接口。

## 6. 最新结果改变了什么

B17 的新宏说明，缺失素数定理排除的是“统一有界的有限调用树”，不是“参数相关的可迭代控制器”。旧 B17 库的封闭域可以由九元、十三元、十四元跨分层桥逃逸；参数无关的 Smith 模式又把原先的局部 guard 进一步消掉。

因此当前更合理的总路线是：

\[
\text{系数格编译}
\to
\text{局部环面调度}
\to
\text{正向宏循环}
\to
\text{本原高度下降}
\to
\text{终端子问题}.
\]

这仍没有覆盖所有 (n)，但已经把“依赖输入的无限长度”纳入统一框架，不再要求一个被缺失素数定理排除的固定深度模板库。

## 7. 当前可检验的下一步

1. 对 B17 通用宏库搜索 (ar\alpha) 的正向实现，并检查其是否只需有限个额外 Smith 模式；
2. 对一般 (n) 自动枚举 (m=3^k) 与已解子问题大小 (s)，用 Smith 判据生成候选返回宏；
3. 对每个候选宏计算范数环面、局部惰性/分裂类型及本原化分支；
4. 在带域宏图上寻找循环，使每个循环的 (S)-高度净下降；
5. 把高维三幂压缩的多链运输接到同一个编译器，而不是单独猜链间宏。

现有 B17 精确核验已覆盖 1008 个通用宏接口、684 个局部调度案例、1440 个范数分支和 600 个 theta 系数。它们证明了编译器和 B17 局部结构的正确性，不等于 B17 或任意 (n) 已完成。


<!-- END SOURCE doc-8f04e14412f7 -->

---

<a id="doc-65008db4ce35"></a>

## 原文导签：十三元二维核：已得到的真实宏与剩余的三进高度问题

来源：`outputs/triple_average/history/triple_average_thirteen_macro_frontier.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_thirteen_macro_frontier.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-65008db4ce35 -->
# 十三元二维核：已得到的真实宏与剩余的三进高度问题

> **状态更新：** 十三元已经由有限指数同余子群与尖点分类完整解决；本文保留此前探索过程。其三阶关系现已统一为任意秩 Burau 幂链定理。当前证明见 [十三元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_thirteen_arithmetic_complete.md)，一般推广见 [Burau 幂链定理](../sources/outputs/triple_average/history/triple_average_burau_power_chain.md)。

十三元是当前最自然的下一基维数。高维部分已有六重核心和五步桥；这里记录二维核上已经确认的真实宏，以及为什么“实二次型下降”还没有直接给出完整证明。

## 1. 核与坐标

\[
\mathcal B_{13}(u,v)=(u^9,v^3,-9u-3v).
\]

取

\[
x=u,\qquad y=9u+4v.
\]

则

\[
4E=117x^2+3y^2,
\qquad y\equiv x\pmod4,
\qquad G=1\Longleftrightarrow13\nmid y
\]

（对本原参数）。

## 2. 两个基本真实宏

记 (w=-9u-3v)。

### 宏 A：压缩单独位置

选取 ((w,v,v))，得到

\[
(u,v)\longmapsto
A(u,v)=\left(u,-3u-\frac v3\right).
\]

这一步在 $v\ne w$ 时是非恒等操作。$v=w$ 等价于 $y=0$；在非零本原参数下此时 $G=13$，属于非法方向。$u=0$ 才给出可由九元零和块收尾的终端方向。

在 ((x,y)) 坐标中

\[
A:(x,y)\longmapsto(x,-y/3).
\]

### 宏 R：三进扩张并交换重数

连续三次选取当前的 ((v,u,u))，把三重 (v) 扩张为九重

\[
a=\frac{2u+v}{3},
\]

最终返回

\[
R(u,v)=\left(\frac{2u+v}{3},u\right).
\]

在 ((x,y)) 坐标中，清除分母后的射影矩阵可取

\[
R\sim
\begin{pmatrix}-1&1\\39&9\end{pmatrix}.
\]

两种宏都保持 (13\nmid y) 的合法性：A 只把 (y) 乘以 (-1/3)，R 的新大块与旧差 (v-u) 只相差一个三进单位。

## 3. 一个四步返回宏及其强实收缩

先做 A，再做 R，得到四步真实宏

\[
M=R\circ A,
\qquad
M(u,v)=\left(-\frac u3-\frac v9,u\right).
\]

对核二次型

\[
Q(u,v)=90u^2+54uv+12v^2=E(\mathcal B_{13}(u,v))
\]

有精确恒等式

\[
Q(M(u,v))
=\frac13Q(u,v)-\frac{26}{9}(3u+v)^2.
\]

所以 (M) 在所有非零实方向上都把原始二次型至少压到三分之一；等号只在 (3u+v=0) 的方向上取到。这个宏不是形式搜索得到的矩阵，而是由四次真实三平均组成。

## 4. 为什么这还不是十三元完整证明

参数 (u,v) 的整数本原格在 (M) 作用下通常会产生九分母。若直接乘以 (9) 清分母，整数代表由

\[
(-3u-v,9u)
\]

给出；其共同因子是否含有 (3)，以及参数格在 (2) 处的尺度，会改变真正的整数高度。于是实收缩 (Q(Mz)<Q(z)) 不能单独推出本原整数高度下降。

必须同时按下列局部数据分块：

* (v_3(3u+v)) 的截断值；
* 清除分母后 ((-3u-v,9u)) 的共同三因子；
* 参数格条件 (y\equiv x\pmod4) 的二进尺度；
* 合法条件 (13\nmid y)。

这正是一个最小的 adelic 控制器问题。四步宏给出了无穷处的强收缩，但它可能把 (3)-进高度推高；宏 A 可以调节 (v_3(y))，宏 R 负责重新混合 (x,y)。

## 5. 一个可验证的下一命题

> **十三元局部覆盖命题。** 由 A、R、M 以及有限个进一步的短返回宏，按有限的 (3)-进截断类型和二进参数格类型分块后，每个合法非终端方向都有一个严格下降的本原高度。

若此命题成立，十三元 (G=1) 充分性就随六重桥定理成立，并通过三进等块提升得到 (13\cdot3^k) 的完整判据。

当前脚本 `work/check_n13_macro_cover.py` 检查了 A、R、M 及若干四步返回宏的实二次型下降区间；`work/n13_matrix_height.py` 则显示了清除分母和参数格尺度必须显式纳入，不能把实收缩直接当作整数高度下降。

<!-- END SOURCE doc-65008db4ce35 -->

---

<a id="doc-7df3f977b1d7"></a>

## 原文导签：三进运输稳定化：双随机返回与复制消去的精确接口

来源：`outputs/triple_average/history/triple_average_triadic_transport_stabilization.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_triadic_transport_stabilization.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-7df3f977b1d7 -->
# 三进运输稳定化：双随机返回与复制消去的精确接口

日期：2026-09-10。这里证明复制空间中的真实运输，不证明从副本路径下降回原维数。

## 1. 三进双随机矩阵的副本实现

设D是n乘n双随机矩阵，D_ij非负且属于Z[1/3]。取Q=3^k清除全部分母，则A=QD为非负整数矩阵，每行列和均为Q。
把A视为左右各n个顶点的Q正则二分多重图。Hall定理给出一个完美匹配；逐次删除匹配，得到

\[
A=P_1+\cdots+P_Q
\]

其中P_l为置换矩阵。

给输入x的每个坐标Q份副本。第l层副本按P_l重新标号，不需平均操作。
对每个输出坐标i，收集Q个相应输入位置，用k层三进张量网络全部平均。
各坐标组不交，输出恰为(Dx)的Q份副本。因此

\[
\boxed{x^{[Q]}\longrightarrow(Dx)^{[Q]}}
\]

有真实有限三平均路径。操作数为n k 3^{k-1}；匹配分解只负责位置调度。
这是一向实现，不声称D逆也非负或可执行。

## 2. 精确返回容量条件给出三进运输

令m=n-4，0<=t<=1且1<=mt<=3。目标为精确R_n(t)。
[支撑刚性](../sources/outputs/triple_average/history/triple_average_exact_return_support_rigidity.md)给出的三种源类型到三种目标类型的总权如下：

- 每个x行从m个u列取总权1-t，从三个v列取t；
- 每个y行从u列取(mt-1)/3，从v列取(3-mt)/3，从w列取1/3；
- 最后u行从u列取1。

若t属于Z[1/3]，取Q=3^k使上述全部行边际乘Q为整数。
对每一对源/目标类型，在完整二分图上分配非负整数流：行需求为对应目标行边际，源列容量均为Q。
总需求分别为mQ、3Q、Q，与各源类型的总容量相等，所以简单逐行贪心运输即可完成；完整二分图不存在额外割障碍。
除以Q得到条目属于Z[1/3]的非负双随机D，并且Dx正是目标返回状态。

结合第1节，容量条件现在对**三幂复制后的精确返回**充分且必要：

\[
0\le t\le1,quad1\le mt\le3,quad t\in Z[1/3]
\Longrightarrow
B_n(u,v)^{[Q]}\to R_n(t)(u,v)^{[Q]}
\]

对某个共同Q成立，且同一位置调度对全部参数u,v有效。

## 3. 为什么这仍未解决原维数

第1节使用Q份真实副本。不能因为输入和输出参数相同，就删去Q-1份位置。
原维数精确返回要求把D本身分解成三平均矩阵的乘积；稳定化只把D写成置换的算术平均并在副本方向实现这个和。
“算子凸和”与“原空间算子乘积”是不同资源。

这准确定位复制消去猜想：如果能对上述运输类证明副本实现可下降到原位置，就自动得到所有满足容量条件的返回族。
由于允许全部正整数k时区间3^k<=m<=3^{k+1}覆盖m>=3，奇偶返回的容量空隙随之消失。
再配合一般返回根公式，统一种子路线会大幅简化。

反过来，固定词一致性障碍说明不能希望一个状态无关的原n维词实现任意D或J/n。
需要利用B_n二维输入像、返回目标的特殊三类型结构，或允许执行词依赖输入。

## 4. 与非分裂Reynolds结构的联系

Reynolds共轭平均也是一个三进双随机算子凸和。副本空间可以把这类凸组合物理化，而原空间只能复合Reynolds投影。
所以交错群影子和凸标量解释了复制路线为什么容易获得全局各向同性；固定词分母障碍解释为什么它不会自动下降。

统一研究可缩成一个更弱问题：是否能只对三类型返回运输矩阵，证明三幂副本实现可消去？
这弱于任意状态的复制消去，且目标D具有载体列支撑3、一个保留u行和固定类型边际，可能有专门的原位置分解。
目前尚无这样的下降定理。

## 5. 核验

work/verify_triadic_transport_stabilization.py对多组m,t构造整数类型运输，检查双随机列和、目标系数及重复完美匹配分解。
一般匹配存在性由正则二分图Hall定理承担，容量充分性由完整类型运输网络证明，不由样本外推。

<!-- END SOURCE doc-7df3f977b1d7 -->

---

<a id="doc-ddf371bd56cf"></a>

## 原文导签：十二元四宏的参数延拓及其关系边界

来源：`outputs/triple_average/history/triple_average_twelve_macro_family_extension.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_twelve_macro_family_extension.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ddf371bd56cf -->
# 十二元四宏的参数延拓及其关系边界

本笔记回答十二元模群证明是否可以直接推广到 \(n=3^k+3\)。结论是：真实宏与局部合法性可以延拓；用于产生正向逆元的两个关键关系仅在 \(n=12\) 成立。因此不能把十二元有限群证书按参数替换来证明新维数。

## 1. 参数宏族

令 \(r=3^k,\ k\ge2,\ n=r+3,\ m=r-1\)，考虑
\[
\mathcal B_n(u,v)=(u^m,v^3,-mu-3v).
\]
通用 A 为 \((u,-(mu+v)/3)\)。另外有三个真实返回宏，其**实际**线性矩阵为：
\[
B_r=\frac1{9r}\begin{pmatrix}-18&-9\\5r-4&2r-2\end{pmatrix},
\]
\[
C_r=\begin{pmatrix}(r-6)/(3r)&0\\(4r-6)/(9r)&1/3\end{pmatrix},
\qquad
D_r=\begin{pmatrix}(r-6)/(3r)&0\\-(r-1)(r-6)/(9r)&-1/3\end{pmatrix}.
\tag{1}
\]
B 需要 \((r+3)/2\) 次原子操作，C、D 各需 \((r+5)/2\) 次。

**B 的构造。** 先执行 A，将新三重值分别用两个 u 的扩张树扩到 r 重，得到
\[
b=-(2u+v)/r,\qquad (b^r,u^2,v).
\]
再依次平均 \((u,v,b)\)、\((u,c,c)\)，其中 c 是前者的均值。留下 \(b^{r-1}\)、新三重值和单独的 c，得到 (1)。

**C、D 的构造。** 先按十二元宏的共同前六步执行：记
\[
a=\frac{w+2u}{3},\quad b=\frac{2a+v}{3},\quad c=\frac{v+2u}{3},
\quad e=\frac{b+c+u}{3}=\frac{21-2r}{27}u.
\]
最后一个三元组执行三次，得到
\[
(e^9,u^{r-8},v,a).
\]
对九个 e 再扩张 \(k-2\) 层，总共消耗 \(r-9\) 个 u，得到
\[
(f^r,u,v,a),\qquad f=\frac{r-6}{3r}u.
\]
分别平均 \((v,f,u)\)、\((a,f,u)\)，便得到 C、D。
所有中间重数均非负，且最终是原 B 核的重数形状；符号参数数值重合不影响逐位置可执行性。

行列式为
\[
\det B_r=\frac1{9r},\qquad
\det C_r=\frac{r-6}{9r},\qquad
\det D_r=-\frac{r-6}{9r}.
\tag{2}
\]

## 2. 保持合法，但可逆环会改变

对每个 \(p\mid n,\ p\ne3\)，有 \(r=-3\pmod p\)，从而
\(r-6=-9\pmod p\)。所以 (2) 中三个行列式均为 p 进单位。
各矩阵在模 p 下都固定共同值方向 (1,1)，因此它们在二维参数的差值商上也是单位映射，保持 \(p\nmid(u-v)\) 和本原性。三个宏均保持原状态的非三局部合法性。

但 \(r-6\) 可含新素因子，例如 r=27 时含 7。C、D 的形式逆会引入相应分母，不能再把它们自动放进固定的 \(GL_2(\mathbb Z[1/3])\)。这些新素数不必整除 n，因此“原问题的障碍素数”和“形式返回群的可逆环素数”必须分开。

## 3. 十二元的正向逆元关系为何特殊

在实际矩阵尺度下，
\[
\operatorname{tr}(C_rB_r)=\frac{2(r-7)(r-9)}{27r^2},\qquad
\det(C_rB_r)=\frac{r-6}{81r^2}.
\tag{3}
\]
对于三幂 r，迹为零当且仅当 r=9，即 n=12。这时 \(C_rB_r\) 的射影阶为二，正是十二元证明中把 B、C 逆元写成正向词的关系。

事实上其他 \(k\ge3\) 也不能从更高有限阶得到同样补救。定义
\[
J(r)=\frac{\operatorname{tr}(C_rB_r)^2}{\det(C_rB_r)}
=\frac{4(r-7)^2(r-9)^2}{9r^2(r-6)}.
\]
r=27 时 \(J=6400/1701\)，不属于有理二阶矩阵有限射影阶所允许的
\(\{0,1,2,3,4\}\)。r 至少81时 \(J>4\)，特征值为实且比值非单位根。
后一个不等式可用 \(r-7,r-9\ge8r/9\) 直接验证。

同理 A、D 均下三角，乘积的对角项为
\((r-6)/(3r)\)、1/9，只有 r=9 时相等，从而给出十二元的抛物平移。
因此十二元的两组关系并非一般参数恒等式；本文不声称新宏在其他参数下没有别的正向逆元。

## 4. 证据与下一步

work/verify_bn_arithmetic_structure.py 对 k=2..6 独立符号重放 B、C、D，检查实际矩阵、账本、操作数和 (3)。一般 k 的结论来自上面的扩张树归纳。

十八元已经能用十二元定理作为局部子程序，通过重数配对解决，见[十八元完整归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_eighteen_via_twelve_complete.md)。这提示优先研究已解子块之间的组合接口；无需强求每个 B 核都独立生成同一种模群。

B15 的六步、B18 的七步整数符号探索分别找到 6、7 个返回矩阵（通用 A 的迭代），结果保存在 work/b15_return_depth6.json 和 work/b18_return_depth7.json。其旧剪枝漏考虑均值与已有值碰撞，这两个缓存不宣称完备，只保留可重放的正向证书。B18 通过独立结构归约解决，宏发现表的完整性不是其证明前提。

<!-- END SOURCE doc-ddf371bd56cf -->

---

<a id="doc-aea582e02f93"></a>

## 原文导签：有限模控制的正向实现：所有 n=5 mod6 的二例外归约

来源：`outputs/triple_average/history/triple_average_two_carrier_modular_bridge.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_two_carrier_modular_bridge.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`two-carrier-modular-bridge`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-aea582e02f93 -->
# 有限模控制的正向实现：所有 n=5 mod6 的二例外归约

日期：2026-09-10。本文将原维数形式算术群转化成一个真实正向的**降维接口**。它不要求先把形式群的每个逆元实现为全局射影逆，也不证明降维后总能终止。

后续终止性边界：[精确高度族](../sources/outputs/triple_average/history/triple_average_modular_height_barrier.md)证明有限模恒等调度即使保持G=1并严格降低实能量，也可能让本原高度指数增长。本页的有限模降维仍成立，不能据此自动推得整体终止。

## 1. 一般定理

**二例外归约定理。** 设 \(n\ge17,\ n\equiv5\pmod6\)。每个本原零和、G=1的合法n元整数状态，均可由有限次真实三平均送到零，或一个仍合法的二例外状态
\[
\mathcal C_n(u,a,b)=(u^{n-2},a,b),\qquad(n-2)u+a+b=0.
\tag{1}
\]

这个定理对合数n同样成立。前端不需要安全整数能量下降，也不需要将n分解成已解素数；后端只调用已经无条件解决的n-2元子问题，因为n-2>=15且被3整除。

特别地，剩余p=2 mod3素数的全部高维输入，可以统一归约到(1)。这是一个更大重复块的二维核，不是一般充分性已经完成。

本文调用[平坦载体形式算术性](../sources/outputs/triple_average/history/triple_average_flat_star_arithmeticity.md)的整数主同余子群包含结论。实际正向实现只在一个有限模数上使用逆元，最后再执行一次合法子问题；没有把有限模逆误当作有理矩阵的精确逆。

## 2. 不等大小的同时好划分

写 \(n=3r+2\)，其中r为奇数且r>=5。希望划分成r个三元块及两个单位置块。

**混合块划分引理。** 设块数t>=5，指定每块大小，在所有待保护素数q处块大小均为单位。若原坐标在每个q下不全相同，且待保护素数数目小于t-1，则存在指定大小的划分，使所有块均值在每个q下都不全相同。

从任意划分开始，逐个修复素数。若均值模新q已全同，交换两个块中的q不同元素，就会打破全同。对旧素数，只有当一对块以外的均值全为c，且这对块的加权偏差和为零时，交换才可能破坏旧见证。

每个旧素数至多禁用一对块。若两对不交，t>=5提供共同外部块，其共同均值相同，继而每个端点都在另一对的补集中。若两对相交，非共同端点先被迫等于c，加权和关系和权重单位性再迫使共同端点也等于c。这两种情况都与旧均值非全同矛盾。

删除少于t-1条边后，完整块图仍连通。若每条允许边都找不到跨块不同余元素，则沿图传播可知全部输入都相同，矛盾。所以可以逐素数修复。

应用到大小3,...,3,1,1，t=r+2。n的素因子均非2、3，且不同素因子数小于r+1：由 \(2^{r+1}>3r+2\) 即可。将这些三元块各平均一次，得到
\[
(u_1^3,\ldots,u_r^3,w,z),\qquad z=-3\sum_i u_i-w.
\tag{2}
\]
原来每个q|n的非全同见证仍存在，所以清三进分母并本原化后G仍为1。全零时已结束。否则可将参数 \((u_1,\ldots,u_r,w)\) 规范化为本原整数向量；规范化只用于描述共同尺度，不是额外允许的操作。

## 3. 两个有限模数

令
\[
r=3^s m,\quad3\nmid m,\qquad a=n-1=3r+1.
\]
m、n均为奇数，且
\[
\gcd(m,n)=\gcd(m,192a)=\gcd(n,192a)=1.
\tag{3}
\]
我们将在模n上保留合法全局见证，同时在模m上准备合法的n-2元叶块调用。

只交换w与某个三重叶块的局部形式群，其局部总位置数为a。由已有主同余包含定理，它在局部r维零和参数上包含
\[
\Gamma_r(L),\qquad L=(192a)^2.
\tag{4}
\]
对z载体亦然。把这类局部整数矩阵嵌入全局非零局部均值的情形，会出现分母a，但L含a的因子，故(4)的矩阵仍整系数提升。若局部矩阵更属于 \(\Gamma_r(Ln)\)，全局提升还模n为单位矩阵。

由(3)及SL_r整数初等矩阵的中国剩余提升，\(\Gamma_r(L)\) 在模n上的像为全部局部SL_r，\(\Gamma_r(Ln)\) 在模m上的像也为全部局部SL_r。后一类在全局模n完全不动。

所以两处的独立控制来自明确的整数主同余子群，并不需要假设任意两个局部像天然独立。

## 4. 在模n上获得完整常值稳定子

使用以第二个载体为局部常值的有理坐标
\[
u=x+t\mathbf1_r,\qquad w=-a t,\qquad z=-3\mathbf1_r^Tx+t.
\tag{5}
\]
这里只除以a；由于(3)，这在模n与模m上都是可逆坐标变化，不需要除以r。

只交换z的局部群固定t，在 \(t=0\) 空间中给出全部SL_r，因而其像包含 \(\operatorname{diag}(A,1)\)。只交换w的局部群作用在 \(z=0\)、即 \(t=3\mathbf1_r^Tx\) 的空间，并固定局部常值方向
\[
h=(-n\mathbf1_r,1).
\]
模n时h就是末坐标方向。两局部SL_r块相除，给出所有末行根群；例如一个固定线性行ell，差 \(\ell A-\ell\) 随初等A生成任意行，再由SL_r共轭补齐所有坐标。

因此模n的形式群包含
\[
P_n=\left\{\begin{pmatrix}A&0\\c&1\end{pmatrix}:
A\in SL_r(\mathbb Z/n),\ c\in(\mathbb Z/n)^r\right\}.
\tag{6}
\]
它固定全局常值线上的指定向量。所有载体交换本来就固定该向量，所以(6)也是行列式一部分的准确上界。

合法G=1保证输入在每个q|n下都不属于常值线。在(5)中，这等价于x在模n是本原向量。SL_r在有限主理想环的本原向量上可迁，末行平移再任意调整t。因此P_n可以把输入送到以下指定的合法剩余模式：
\[
u_1=1,\quad u_2=-1,\quad u_i=0\ (i>2),
\qquad w=1,\quad z=-1\pmod n.
\tag{7}
\]

## 5. 在保护模n的同时控制全部模m参数

现在只使用来自 \(\Gamma_r(Ln)\) 的局部词。它们模n为单位，但在模m上提供两个完整局部SL_r块。

在(5)坐标中，第一个块为 \(\operatorname{diag}(SL_r,1)\)。记v=e_i-e_j，选择k避开i,j。另一个局部块包含
\[
I+v(e_k^T+n e_t^T).
\tag{8}
\]
因为v位于z=0空间，源行消灭h，且源行在v上为零。这是一个局部SL_r中的幺幂。乘上第一个块中的 \(I-v e_k^T\)，便得到右上纯平移 \(I+n v e_t^T\)。n模m为单位，所以其SL_r共轭生成全部右上根群。

对左下根群，取i,k,l互异、f=e_k^T-e_l^T。另一个局部块包含
\[
I+\left(e_i-\frac3a\mathbf1_r,\frac3a\right)f.
\tag{9}
\]
同样，它的中心在z=0，源行消灭h，故为合法局部幺幂。消去已在第一个SL_r块中的左上部分，得到
\[
I+\frac3a e_t f.
\]
3和a在模m均为单位，因此生成全部左下根群。结合原左上SL_r，得到整个
\[
SL_{r+1}(\mathbb Z/m).
\tag{10}
\]
特别地，m可能整除r，但证明从未除以r；这是两个载体拼接时需要保留的关键接口。

当前参数向量在模m本原，因为起始参数本原，而载体交换在 \(\mathbb Z[1/3]\) 上可逆。因此可以在不改变(7)的条件下，将它送到
\[
u_1=1,\quad u_2=-1,\quad u_i=0\ (i>2),
\qquad w=z=0\pmod m.
\tag{11}
\]
m=1时该要求为空，不需这一步。

## 6. 有限模逆真正变成正向词

上述输送先在形式群中构造。现在令 \(M=nm\)，它为与3互素的奇数。每个载体交换T都满足
\[
(T-I)(T+I/3)=0,
\qquad T=I+(c-1)P,\quad c=-1/3,\quad P^2=P.
\]
投影P只需除以4，所以在模M仍有定义。令
\[
h=\operatorname{ord}_{(\mathbb Z/M)^\times}(-1/3).
\]
那么
\[
T^h\equiv I\pmod M,\qquad T^{-1}\equiv T^{h-1}\pmod M.
\tag{12}
\]
将每个形式逆替换为h-1个正向载体交换，所得真实词与原词在模nm上作用完全一致。因此(7)、(11)都由正向实际平均实现。每次替换的长度小于nm<n^2，但这里没有为原形式输送词的长度给出多项式上界。

注意 (12) 只在有限模数中成立。真实有理矩阵一般不相等，中间值也可能有更高三进分母；这不影响后续整除条件及合法性。

### 6.1 一般的正向有限模启用原则

上述步骤是一个不依赖载体特例的原则。设一组宏在同一参数核上对所有参数都真实可执行，矩阵 \(T_i\in GL_d(\mathbb Z[1/3])\)。令S为正向半群、Gamma为加入形式逆的群。对任意与3互素的整数M，
\[
\operatorname{im}(S\to GL_d(\mathbb Z/M))
=\operatorname{im}(\Gamma\to GL_d(\mathbb Z/M)).
\tag{12a}
\]
因为每个T_i在有限群中具有有限阶，逆元均可替换为正整数幂。于是对任意输入和任何由模M条件给出的适用域D，有
\[
\Gamma X\cap D\ne\varnothing
\quad\Longleftrightarrow\quad SX\cap D\ne\varnothing.
\tag{12b}
\]

换成拓扑语言，S和Gamma在非三有限整点积
\(\prod_{q\ne3}GL_d(\mathbb Z_q)\) 中的闭包相同。有限多个精度的局部适用域是这个拓扑中的开闭集合，所以进入这类域不增加正向性障碍。

条件“宏对全部参数可执行”不可省略；带守卫的宏可能在重复幂的中间阶段离开适用域。这里的载体交换满足全域条件。

精确终端方程如某坐标等于零，不是一个有限模开集。因此(12b)并不将形式群的精确终端输送自动变成正向输送。本证明的做法是先进入一个可执行子问题的有限模适用域，再利用已证子程序完成真实降秩；这正是形式算术群接入原动力学的可用接口。

## 7. 调用n-2元子问题并返回二例外核

完成正向调度后，令S为全部r个叶值之和。由(11)，S属于 \(m\mathbb Z[1/3]\)，所以
\[
\mu=\frac{S}{r}=\frac{S/m}{3^s}\in\mathbb Z[1/3].
\]
在每个q|m下，叶值包括余数1、-1和0，因而叶差仍有单位。中心化并清三进分母后，叶块这个n-2元子问题的本原差分gcd没有任何q|m因子；又其G整除n-2，所以G必为三幂。

由[全部三整除维数定理](../sources/outputs/triple_average/history/triple_average_one_tripling_stabilization.md)，这n-2个位置可以有限三平均等化为mu。两个载体不参与，故输出为
\[
(\mu^{n-2},w,z).
\]
由(7)，有 \(\mu=0,w=1,z=-1\pmod n\)。每个q|n都保留不同余见证，故输出仍G=1。二例外归约定理得证。

## 8. 新核并不自动终止

对素数p和非零合法三值核
\[
\mathcal C_p(u,a,b)=(u^{p-2},a,b),
\]
令m为p-2的非三部分。如果m>1，单独反复调用p-2元子问题无法作保持合法性的非平凡推进。

- 若省略a、b，调用只作用于全相等背景，是恒等操作。
- 若省略一个例外及一个背景，子块只有一个例外。其中心化本原G恰为p-2，与具体不同值无关，故m>1时不合法。
- 若省略两个背景，形式等化后只剩两个实际值。非零零和p元两值状态的本原G为p，故输出不合法；保持全局合法性的调用只能发生于u=0的终端情形。

必须区分子问题可执行与全局安全：例如p=17的 \((5^{15},1,-76)\) 全局G=1，选取 \((5^{13},1,-76)\) 的15元子问题也合法；但等化后得到 \(((-2/3)^{15},5,5)\)，其本原G=17。这个操作可执行，却把全局状态送进不可达陷阱。必要条件并不在任意正向操作下自动保持。

p-2为三幂时第二条不适用，不能将边界外推到29、83等情形。

因此，后续控制器需要打散背景、增加原子平均预备词或使用其他大小子块。二例外核更自然地隔离了真正剩下的二维问题，但没有取消它。

## 9. 二次型与标准B核接口

对 \(\mathcal C_n(u,a,b)\)，写 \(x=u,\ y=a-b=2a+(n-2)u\)。精确有
\[
2E=n(n-2)x^2+y^2,\qquad y\equiv x\pmod2.
\tag{13}
\]
若 \(\gcd(u,a)=1\)，本原合法性简化为
\[
G(\mathcal C_n)=\gcd(a-u,n)=\gcd(y,n).
\tag{14}
\]
所以全部非三局部见证都集中在两个例外值之差y。n不必为素数；n=5 mod6时它自动与2、3互素。

选一个例外a及两个背景u作三平均，令 \(v=(a+2u)/3\)，立即得到
\[
\mathcal B_n(u,v)=(u^{n-4},v^3,b).
\]
由于 \(u-v=(u-a)/3\)，所有q|n的合法性同时保留。这是真实的一步标准核桥，且在B核的对角参数 \(y_B=(n-4)u+4v\) 中满足
\[
y_B=\frac{nu+2y}{3}.
\tag{15}
\]

**标准核接口推论。** 对每个n>=17、n=5 mod6，任意合法n元输入均可正向送入合法B_n；无需假设只有一个危险素数。若该维数B_n已有统一终止控制器，则全部输入的充分性立即成立。

这把高维有限模调度与已有二维算术框架严格接起来，但没有证明新的B_n控制器。

## 10. 对统一路线的意义

这个结果把三项此前分开的进展连接起来：

1. 混合块交换保护所有非三见证，直接生成原维数平坦核。
2. 高秩形式算术性仅用于有限模输送；有限模逆可以全部正向化，所以不需要先解决有理矩阵的整体正向逆问题。
3. 全部三整除维数的判据提供合法大子块调用，将高秩状态真实压到二例外核。

由此，形式群算术性已经产生一个实质性的正向结论。尚缺的是二例外核的统一终止控制；41元后来由独立同余证书解决，当前最小未解维数为47。

## 11. 核验与复杂度范围

脚本：[verify_two_carrier_modular_bridge.py](../sources/work/verify_two_carrier_modular_bridge.py)，统一ID `two-carrier-modular-bridge`。

- 165个混合三块／单位置划分，含多素数455元与11次强制修复。
- 9组不除以r的有限环Levi拼接恒等式。
- 34个局部主同余矩阵的整系数全局提升与模n保护检查。
- p17、模5上的15624个非零参数全部处于正向轨道，用小有限域检查群作用实现。
- 20个统一有限模逆指数检查。
- 5条固定原位置的正向模调度，共567个原子平均，包含29元的实际27元子网络；起始4步扰动另计。
- 480个同时满足模n／模m目标的输入，独立检查n-2子问题G及二例外输出G。
- 320个素数二例外状态检查后续大子块调用的边界。
- 460个二例外核的对角二次型、G公式及进入标准B核的一步全局安全性。

一般有限环生成、同时好划分及正向化由正文证明；程序没有对大模数运行状态BFS，也没有将480个目标模式误称为480条完整调度词。5条实际调度样本通过对已知目标作短扰动后正向逆回到同余类构造，核验的是有限模逆的物理实现，不代替全部输入的群论证明。当前结论保证有限步存在与可枚举构造，不声称这个桥的整体计算复杂度为多项式。

<!-- END SOURCE doc-aea582e02f93 -->

---

<a id="doc-c83fe1b45f9c"></a>

## 原文导签：三平均的统一框架：带局部条件的有向操作与算术轨道

来源：`outputs/triple_average/history/triple_average_unified_modern_framework.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_unified_modern_framework.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-c83fe1b45f9c -->
# 三平均的统一框架：带局部条件的有向操作与算术轨道

修订日期：2026-09-10。按用户要求重写原 modern frame，保留其中有用的统一视角，并修正群胚、射影商、有限字母表及终端的定义。[完整原稿](../sources/outputs/history/triple_average_unified_modern_framework_before_2026-09-10_revision.md)保持可查。

本文是定义、证明原则和研究接口，不是任意 n 已可达的声明。当前结论与核验入口以[最新交接总览](../sources/outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md)和[验证指南](../sources/outputs/algorithms/triple_average_verification_guide.md)为准。

最新结构补充：[Reynolds半群、交叉计数与判别式对偶](../sources/outputs/triple_average/history/triple_average_reynolds_hecke_hodge.md)给出无需宏适用域猜测的有限层半群：1／3重数运输表恰对应原位置重分组层，转置给出可执行加权伴随，单三重块版本无损编码全部原子词。完整生成代数在所有n>=5均为End(V)，Hodge取逆则在p处分歧格上交换合法域两侧。47已由独立完整证书解决，最小未解53；下文保留框架历次推进的历史描述。

## 1. 总对象与当前结论

令 \(R=\mathbb Z[1/3]\)。输入减去全局平均值、统一清分母并本原化后，可写成零和整数状态。重复值必须保留位置重数，目标是使全部位置成为零。

当前一般问题仍为
\[
n\ge7:\quad G(X)=3^a\ \Longrightarrow\ X\text{ 有限步可达零}.
\]

47元已有[新正向对合与局部化根群](../sources/outputs/triple_average/history/triple_average_b47_extra_atom_and_adjoint.md)：额外一次原子预备改变了宏库，使标准A0及其他宏获得正向逆，并生成全部47Z[1/6]平移。它尚未给出有限指数及完整轨道覆盖。能量伴随来自倒序投影，但必须同时满足反向适用域及共形条件才能用作逆；同型对合的分裂环面边界也须保留。

周期侧有一个可统一使用的[谱平衡判据](../sources/outputs/triple_average/history/triple_average_projective_spectral_balance.md)：半单性、复特征值等模和全部有限处等赋值，等价于有限射影阶。有限处可直接检验特征系数的射影整数不变量；Ad分圆算法能精确判定给定矩阵。正向词是否能达到这种平衡仍是独立存在性问题。B47当前167模板的[长度四及A0^jBC排除](../sources/outputs/triple_average/history/triple_average_b47_cycle_frontier.md)已精确验证，未排除更长或跨核路径。

最新[等值载体核](../sources/outputs/triple_average/history/triple_average_paired_carrier_reset.md)把二进问题落实为格的行列式：单独二重载体交换具有额外因子2，且其叶奇偶不变量排除全局周期。重分组三份叶块则在4r-3步产生W=2V、V属于GL_r(R)，使两个R理想都统一乘2。这给出原维数保秩宏，但还需独立证明全局正向逆或终端覆盖。

41元现已由[三因子对合证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_one_arithmetic_complete.md)完成，最小未解维数为47。21个宏的全局正向逆与42陪集的完整子群共同保证终端输送；周期候选可统一写成三矩阵乘积的多齐次迹方程，但一般n的可执行模板与该方程的相交仍待证明。

[有限模调度高度边界](../sources/outputs/triple_average/history/triple_average_modular_height_barrier.md)进一步明确：有限商正向化即使保持全部指定剩余类、且每步实能量下降，也可能使本原高度指数增长。统一终止不能只依靠有限模适用域和原始实能量，还须控制3进代价或构造精确全局周期。

形式群现已通过[有限模控制](../sources/outputs/triple_average/history/triple_average_two_carrier_modular_bridge.md)产生一般正向结论：所有n>=17、n=5 mod6的合法输入，无需先作安全能量下降，即可经混合好划分和两个载体调度进入合法二例外核。形式逆仅在模nm上替换为正向幂，随后调用已解n-2子块；这与有理矩阵全局逆的实现是不同接口。二例外核的统一终止仍未证明。

29元已有[完整正向同余群证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)：九个三因子标量周期使18模板全部可正向取逆，七个整数词生成30陪集的共轭Gamma_0(29)，唯一合法尖点可收尾。它说明二因子周期排除不妨碍稍长的全局周期；41元由后续独立证书完成。

最新[分裂素数统一定理](../sources/outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md)已解决全部p=1 mod3：以H三阶轨道的高斯周期层获得原维数全局正向逆，范数一单位保证本原剪切，整数仿射行群给出统一终端算法。这首次将数域范数、实际正向词及任意素数族的终端覆盖完整接合。剩余统一素数问题是p=2 mod3、从29开始；因子闭包随之扩展。

原维数平坦核的[形式算术性](../sources/outputs/triple_average/history/triple_average_flat_star_arithmeticity.md)现已对全部p>=13统一：真实载体交换加入形式逆后，其整数特殊线性部分有限指数；模2与模p的第一层合法轨道均有终端代表。全体正向宏仍是半群，形式群的算术性不能替代整体正向实现。

局部数据也必须记录联合字符。[置换剩余像与尺度耦合](../sources/outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md)证明九十一元旧21504容器严格过大，新43008必要容器由两个局部群在二阶字符上的纤维积给出。相应紧模曲线之间的无分歧二重覆盖提供了严格的Jacobian二阶线丛解释。

最新[总归约定理](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_to_primes.md)证明：任意n>=7的判据等价于全部素数p>=7的判据。已解素数集合P={7,11,13,17,19,23}可任意相乘，并乘任意二、三、五幂。因此所有23光滑维数n>=7已解决，最小未解维数为29。统一素数定理仍未证明。

新增[一次三份复制定理](../sources/outputs/triple_average/history/triple_average_one_tripling_stabilization.md)无条件解决全部N>=9且3整除N，不限制非三素因子。数字算子在零和空间共轭于有限置换，Hilbert90周期使逆元正向可实现；与局部换位组成平衡剪切，整数仿射格轨道分类再给出全覆盖。这是副本层的统一算术控制器，尚不能在原维数消去。结构图景的数域推广边界见[独立审计](../sources/outputs/triple_average/history/triple_average_structural_picture_audit.md)。

该副本控制器的群结构现已[完整识别](../sources/outputs/triple_average/history/triple_average_digit_congruence_group.md)：平衡群等于全部整数保和／保常值矩阵；数字群等于模n的指定循环倍率稳定子。有限指数、分裂扩张与有理直线轨道都由一般证明给出，不再是该副本库中的猜想。原维数的不同权重库尚未继承这项算术性。

最新[奇数合数乘法闭包](../sources/outputs/triple_average/history/triple_average_odd_composite_factor_closure.md)结合[25元完整证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)，解决全部3^a*5^b*product(p^e_p)>=7，a、b、e_p任意非负、p属于{7,11,13,17,19,23}。它由多例外进位与安全核心的强归纳证明，不需要每个合数另建算术群。全部奇数已严格归约到全部p>=7素数，25元不再是额外条件。

同一证明还解决被8整除、非二三素因子属于5及上述素数集合的全部维数，5的指数任意。若素数方向统一，则所有8整除维数也统一。这里主要使用仿射格见证分配，不要求由Zariski稠密直接推出算术有限指数。

一个合适的统一对象由三层组成：

1. 带质量和总和守恒的有向重写状态；
2. 带局部适用域和真实位置账本的线性操作；
3. 其中确有正向逆元的可逆子群，以及带完整收尾证明的终端集合。

全体操作是有向范畴；可逆部分才可能形成群胚。不能先把所有箭头形式可逆化，再将新增逆操作用于原问题。

## 2. 原子操作与根格

状态可表示为有限支持的计数函数
\[
m=\sum_{t\in R}m_te_t,\qquad m_t\in\mathbb N.
\]
质量 \(N(m)=\sum m_t\) 与总和 \(S(m)=\sum tm_t\) 固定。一次原子操作为
\[
e_a+e_b+e_c\longrightarrow3e_{(a+b+c)/3}.
\tag{1}
\]
每次必须有足够的实际副本。

在线性坐标中，零和空间为 \(V_n\)，整数格为 \(A_{n-1}\)。三平均是消去选中位置内 \(A_2\) 差分平面的正交投影。若用根列矩阵 B 表示该平面，则
\[
P=I-B(B^TB)^{-1}B^T,\qquad
(B^TB)^{-1}=\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
因此原子矩阵只有三进分母；非恒等原子操作严格降低实际平方能量，但清分母与本原化后的整数高度未必下降。

被消去的局部 A2 平面不等于所有返回宏的参数空间。后者由所选重数分层决定，t个块通常有t-1个零和参数；三平均本身并不强制任意n都落在 PGL2。二维控制器出现后，才能进一步识别它的实际算术群或范数环面。

固定词 W 的归零输入是 \(\ker W\cap V_n\)，固定长度内是有限个线性子空间的并。不能仅由此推断任意长度可达集的代数闭性，也不能据有限词枚举证明其无限并等于全部合法点。

## 3. 托里克语言与它的限制

式(1)对应二项式 \(z_az_bz_c-z_q^3\)。它属于质量--一阶矩映射
\[
\mathbb N^{(R)}\to\mathbb N\times R
\]
的关系格。因此“纤维”“关系格”“有向移动”是严格可用的语言。

但字母表 R 是无限的。有限集合若含不同的最小值 a 与次小值 b，对全部三元平均封闭就还须包含 \((2a+b)/3\)，这是矛盾。每条具体路径用有限个值，不等于全部路径有统一有限字母表。

所以有限变量托里克理想的 Noether 性、有限 Markov 基、Gröbner 终止性不能自动搬来。若要使用这些工具，必须另给一个保留可执行性、覆盖全部目标状态的有限模型或参数化有限生成定理。仅证明无向纤维连通还不能控制平均方向。

## 4. 参数分层与尺度

正整数权重向量 \(\mathbf r=(r_1,\ldots,r_t)\) 的总和为 n。定义
\[
V_{\mathbf r}=\{u\in\mathbb Q^t:\sum_i r_i u_i=0\},
\qquad
\iota_{\mathbf r}(u)=(u_1^{r_1},\ldots,u_t^{r_t}).
\]
当 n固定，权重向量描述位置分组；实际值碰撞时可把同值块合并，但必须保持副本数。

三幂压缩把一般合法输入送到 \(r_i=3^{k_i}\)、\(t=O(\log n)\) 的核。之后的有效操作可以进入非三幂权重分层，例如 B12 的(8,3,1)，不能把初始核类别误认为所有后续对象都必须保留的形状。

参数向量维数为 \(t-1\)，射影维数为 \(t-2\)。射影化可采用：

- 对全部非零有理数整体缩放取商；
- 或先选 away-from-3 本原代表，再对 \(\pm3^k\) 取商。

直接在任意有理向量上只除三进单位，不等于有理射影空间。全零状态须单独添入；物理路径的尺度由账本记录，不能把本原约分算成平均操作。

## 5. 带条件箭头的严格契约

一个核间箭头 e 包含：

- 源、目标展开映射及有理线性映射 \(M_e\)；
- 适用域 \(D_e\)，明确局部整除、合法性及重数条件；
- 对每个 \(x\in D_e\)，真实有限三平均词 \(W_{e,x}\) 的实现证明：
\[
W_{e,x}\iota_{\mathbf r}(x)=\iota_{\mathbf s}(M_ex);
\]
- 如调用已解子问题，列出它的中心化本原 G 条件；
- 如需复杂度结论，给出宏展开长度、查找成本、中间位长及递归规模界。

原子宏的词可以固定；已解子问题的内部词可能依赖 x，但其最终均值算子仍是明确的 \(M_e\)。这个区别让算术群法和子问题调用法可以共用接口。

先执行 e，再执行 f：
\[
M_{fe}=M_fM_e,\qquad D_{fe}=D_e\cap M_e^{-1}(D_f).
\tag{2}
\]
只乘矩阵而不检查复合域，会引入不真实的可达路径。所有非奇异、奇异和变维操作可以共存于有向范畴；只有具有正向逆实现的指定子库才作为群胚或自同构群使用。

子问题的局部判据有一个准确仿射格版本：若整数子块大小为 s，取值差 gcd为d，锚点为a，并令 \(T=\sum(x_i-a)/d\)，则非全等时
\[
G_C=\frac{s}{\gcd(s,T)}.
\]
在已经解决的大小s上，这等价于目标均值属于 \(a+dR\)。它不自动证明未解s的充分性。详见[十五元证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md)。

还有一个任意参数维数的**模板预编译判据**：若子块值为线性式 a_i z，令 L 为所有 a_i-a_1 生成的 R 行模，则对全部有理参数都满足仿射格条件，当且仅当均值行减 a_1 属于 L。此条件可用局部化整数 Smith 标准形判定；已解s上由此得到全域真实箭头。它会发现被简单模p guard 漏掉的共同因子消去，详见[普遍子问题模判据](../sources/outputs/triple_average/history/triple_average_universal_subproblem_lattice.md)。

## 6. 局部算术与有限 S

本原零和状态的 G 整除 n。若某个 \(p\ne3\) 整除 G，则所有坐标模p同余为非零值；原子平均将永远保留它，不能归零。

这里必须区分“原始模p见证”与“本原 G”。如果所有值整体出现p因子，本原化后局部见证可能恢复。丢掉原始见证不总等于失去可达性。

对固定有限矩阵库，可以把所有系数分母、非零行列式和输入格的相关素因子组成有限S。条目在R中不保证逆仍在R中；需另查行列式是否为 \(\pm3^k\)。不能对尚未证明有限生成的全部返回宏，直接断言存在同一个有限S。

实与p进射影空间的乘积是局部数据的环境；实际输入还必须来自同一个有理点并满足参数格条件。对二维B核，已有离散能量高度为
\[
\mathcal H_n([a:b])=
\left(\frac4{\gcd(4,b-(n-4)a)}\right)^2
\bigl(n(n-4)a^2+3b^2\bigr),
\]
其中(a,b)是标准整数本原代表。未规范化的有限处乘积不能直接代替它。

## 7. 同余子群法的通用部分

最本质的原则是**正向可实现子群、有限有理轨道、终端代表**。

若固定d维参数核的真实正向宏含一个 \(SL_d(\mathbb Z)\) 的有限指数子群H（可先作固定有理基变换），并且生成元与逆在整个合法域均可实现，则合法有理方向只有有限多个H轨道。原因是 \(SL_d(\mathbb Z)\) 在本原整数列向量上传递。为每个合法轨道给出终端代表，便得到全核充分性。

d=2时这些轨道是经典cusp。d大于2时可以直接用射影向量轨道；完整旗标在算术紧化中很重要，但不是每个状态天然携带的数据。

十二元使用共轭 \(\Gamma_0(8)\) 的指数12子群；十三元使用指数56子群。所需包含方向为 \(H\subseteq\Gamma_{\rm positive}\)，不需要H等于全部真实群。九十一元的同余容器是相反方向的外界，因此24个容器代表都可终止仍不足以解决真实轨道。

十七、十九、二十三元已分别实现共轭 Gamma_0(17)、Gamma_0(19)、Gamma_0(23)。[一般素数稳定子定理](../sources/outputs/triple_average/history/triple_average_prime_congruence_structure.md)说明其整数部分正是合法集合允许的自然上界：在坐标u/(v-u)下，合法域为Z_(p)，其p进稳定子是Iwahori子群。对所有素数是否都能实现足够大的正向子群，仍须另证。

对固定原子词或全参数通用模板，实际标量循环还必须满足lambda=1 modulo n的非三部分。因此实际尺度为正负3^(-k)时，k与符号受3的局部乘法阶约束。搜索必须保留物理尺度；这不能在任意缩放的射影代表上直接判断。

二十三元通过4/27与2/3^7的实际标量循环完成正向逆元，明确展示了指定返回群可能需要2、3两个局部处。它的模曲线属为2，但唯一合法cusp仍可收尾；这里使用边界轨道，不要求求出模曲线内部的全部有理点。候选按共同第一行分组，还能直接找出仿射变换及初等平移。

“同余”便于描述和核验，有限指数本身不要求同余。大有限模像不证明有限指数：由上下参数3的两个初等矩阵生成的子群，在每个 \(p\ne3\) 下均满射到 \(SL_2(\mathbb F_p)\)，但在模群中指数无限。严格证明和高秩初等子群工具见[同余方法的范围](../sources/outputs/triple_average/history/triple_average_congruence_method_scope.md)。

## 8. 终端与反向可达集

终端集合 \(\mathcal T\) 必须附有**全部位置**的收尾证明，例如：

- 全零状态；
- 完整的零和三幂分块；
- 足量零填充后的三幂零和支持；
- 覆盖剩余全部位置且满足局部判据的已解子问题。

一个零坐标、一个零和子块或一个仅有大重数的核，均不自动是终端。

对指定操作库定义
\[
\mathcal A_0=\mathcal T,\qquad
\mathcal A_{j+1}=\mathcal A_j\cup
\bigcup_e\{x\in D_e:M_ex\in\mathcal A_j\},\qquad
\mathcal A_*=\bigcup_j\mathcal A_j.
\tag{3}
\]
这是该库的终端反向可达集。所有成员都有有限证书，但定义本身不提供完备的有限时间成员判定。

若库含全部原子操作，“所有合法点都在 \(\mathcal A_*\)”只是原猜想的改写。要取得新结果，必须提供明确覆盖与良序下降、充分大的正向算术子群与终端轨道，或严格减少子问题规模的归纳接口。

## 9. 控制图需要循环，也需要跨分层边

[缺失素数定理](../sources/outputs/triple_average/history/triple_average_subproblem_prime_obstruction.md)证明：若某个 \(p\mid n,\ p\ne3\) 不整除任何调用大小，每个固定调用词至多消灭一个B核射影方向。因此统一有界调用次数不能覆盖无限多个合法方向。对素数维数17，所有严格更小子问题都落在这个障碍内。

这要求控制图允许输入相关次数的循环，而不是无环的常数深度调用树；不排除位长多项式算法。

但“允许循环”也还不够。[B17旧库](../sources/outputs/triple_average/history/triple_average_b17_guarded_subproblem_experiment.md)有一个无限封闭局部域，唯一可用边为A，且本原高度严格增加。[历史跨核桥](../sources/outputs/triple_average/history/triple_average_b17_cross_stratum_escape.md)首先解决其中的奇背景子族。最新[普遍子块模判据](../sources/outputs/triple_average/history/triple_average_universal_subproblem_lattice.md)进一步产生五个全域返回宏：其中一个模5为六循环，与A结合，使所有合法 B17 至多三次返回后可调用原十五元分支。原不变域已绕开，仍须检查净下降；“总有下一次合法调用”还不是终止性。

## 10. Theta、Hecke 与正向实现

正定格的theta级数满足标准模性定理；这一静态结论无需事先确认整个宏群。但它不证明平均路径存在。

B17现在有一个尤其直接的实例：真实通用宏的整数矩阵 [[7,2],[-33,-9]] 经 (x,y)=(u,4u+v) 后是乘以 -1-sqrt(-2)。其范数型 x^2+2y^2 乘3，模5是非分裂范数环面上的传递六循环，像格 X=Y mod3 的 theta 等于 theta(z^3)。这将真实操作与判别式-8的权1 Eisenstein 级数直接相连。新增正向逆词又实现了共轭素元，因而这个特定范数格的两个三进分支都有真实操作；这仍不自动赋予其他格或其他维数的全部 Hecke 分支正向实现。

早期五宏库的模3不变集确实排除了库内固定共轭逆词。继续编译更多中间分层后，新增 Q、T、U 打破该限制，给出 B 的61步正向射影逆元及 A 的55步逆元。六个正向整数词生成共轭 Gamma_0(17) 的指数18子群，从而完成十七元；不必再要求旧48类预备调度具有净下降。

当前已有真实宏的指数9子格筛选公式，以及迭代拉回的导子塔：B12中某个宏的k次拉回型判别式为 \(-8\cdot3^{4k}\)。这说明即使起始型类数为1，宏也可能带入无界导子层级。单个正向可实现子格分支，不能自动换成完整Hecke求和中的任意分支。

可以追求的严格工具接口是：证明指定真实宏与某个格对应或自守算子兼容，并同时保留局部本原层、尺度、适用域及位置账本。强逼近主要处理局部闭包与约化，且需要相应代数群假设；不能单独用它消除“薄群还是有限指数”的问题。

## 11. 三个并行方向的定位

**链间运输。** 不等三幂块的真实交换及
\[
\Delta=q(v-u),\qquad
\Phi'-\Phi=2\Delta(S_a-S_b)+2\Delta^2
\]
是可用的箭头数据。仍需证明总有能推进终止的选择。把一条链归零未必减少非零链数；若接收链原来为零，可能仅转移非零质量。相关复核意见保留在[团队交接](../sources/outputs/triple_average/history/triple_average_team_handoff_2026-09-10.md)。

**高秩Burau。** 整条几何链自身加权零和时，指定相邻宏的正向逆元关系已证明。一般嵌入子链的非零平均必须单独跟踪。模p有限像和向量轨道是算术候选的证据，不是有理群包含或高秩终端覆盖的证明。

重新综合链间交换与高秩报告后，已有[任意连通交换图的完整Zariski闭包定理](../sources/outputs/triple_average/history/triple_average_other_ai_local_global_review.md)：秩一交换投影的Lie代数是全部gl，因此任意秩几何链的代数闭包不再是未定项。它不解决算术有限指数。非零均值时准确的正向逆接口为(均值投影+三进收缩*偏差投影)乘以形式逆；多个链可同步偏差尺度，而跨链交换与此同步中心的交换子秩至多2。

**复制消去。** 干净同步轨道宏可以投影成原维数真实平均；一般重叠轨道未证明可这样改写。三个共轭路径串联产生矩阵乘积，循环对称化产生凸平均，两者不能互换。稳定化只保证某个输入相关的 \(3^k\) 倍复制可达；n至少7时逐层消去复制仍是开放主线。

允许输出副本重新分组后，一层不交三平均等价于K/3，其中K非负整数且行列和为3。这个更大同步类包含可逆的(2I+循环置换)/3，故不能在整个原零和空间统一实现为非空三平均词；后者必降秩。未来复制下降必须给出状态依赖、低秩限制或面向终端的额外接口。

## 12. 可检验的统一猜想

在一个明确的、参数化可生成的操作库中，要求：

1. 任意合法输入能进入指定标准核；
2. 每个非终端合法参数有一个适用箭头，或者有一个可执行的算术轨道归约；
3. 箭头复合域覆盖全部目标类型；
4. 下降路线给出明确良序量或严格递减子问题规模；群轨道路线给出充分子群、有限轨道覆盖和正向实现；
5. 所有终端都有全局真实收尾；
6. 若声称多项式路径算法，还须控制选择成本、位长、宏展开长度和循环次数。

这才是可检验的“有限型有向控制器”猜想。一般运输的选择引理、充分算术子群的构造以及复制消去不能因为被装入一个元组就当成已经解决。

十七元给出一个任意 n>=9 的充分算术目标：令 N为n的非三部分、C=[[1,0],[1,1]]，若真实 B_n 群包含 C Gamma_0(N) C^-1，则同一 Bezout 公式送全部合法方向至(0,1)，由九元零填充收尾。这个包含不是必要条件，更小的充分子群和多个终端仍可使用；任意n的包含本身尚未证明。

下一步是将模包含编译和正向群关系推广到一般参数化核，同时推进多危险素数的进入接口。多链、高秩与复制路线仍须分别给出可直接检查的公式、域和证书。可复核性以[严格化契约](../sources/outputs/triple_average/history/triple_average_modern_framework_review_and_contract.md)、[同余方法范围](../sources/outputs/triple_average/history/triple_average_congruence_method_scope.md)和各定理文档为准。

因子接口已从[二例外三进进位](../sources/outputs/triple_average/history/triple_average_prime_first_factor_reduction.md)推广到r个例外：只要b>=r+1、行容量足够，每个例外分裂后选出ha_0权重，分别形成合法行，余量汇入一个保留全部局部见证的行。准备操作数至多(r-1)ceil(log_3a_0)。奇数因子的容量可统一满足，35元边界另用余量行中的差异解决，因此现有d+2核心已足够。未解决的是任意偶数的相应接口，而非所有多例外情况。

因此“先解素数再归约合数”应指两个独立定理的组合，而非直接在不同位置数的宏群之间使用交集。原子尺度的素数幂level、行调用的仿射格条件和商状态的全部非三见证必须同时保留。

这两个模块中的合数归约现已完成：低二进重数通过一次／两次预备平均加十二元子问题配成两份；70、110、130边界通过改变一个分裂系数修复无常值行的商见证。当前尚需完成的是统一素数算术模块。可以令p为最小反例素数，此时所有7<=m<p的合法子问题均已可调用；这比逐个素数仅使用固定小库更强。

参数无关调用的编译器和范数环面接口已单独整理于[宏编译器与范数环面](../sources/outputs/triple_average/history/triple_average_template_compiler_and_torus.md)。

<!-- END SOURCE doc-c83fe1b45f9c -->

---

<a id="doc-a20253f0d3b0"></a>

## 原文导签：参数无关子问题调用：局部化整数模判据与十七元新宏

来源：`outputs/triple_average/history/triple_average_universal_subproblem_lattice.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_universal_subproblem_lattice.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`b17-universal-subproblem-lattice`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-a20253f0d3b0 -->
# 参数无关子问题调用：局部化整数模判据与十七元新宏

更新：2026-09-10。

**后续完成状态：** 本文保留参数模判据、旧宏库及局部调度阶段。进一步扩展模板后，已得到 A、B 的正向逆元与级17的完整充分子群，见[十七元完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_seventeen_arithmetic_complete.md)。旧库逆词障碍仍正确，但不适用于新增的 Q、T、U 宏；十七元及其三进塔现在已解决。

## 1. 新增结论

此前的 B17 短返回库有一个无限封闭同余域。进一步按重数编译跨分块调用，发现可以完全消去某些子问题的输入同余条件。关键不是增加局部枚举范围，而是先检查**线性式生成的整数模**。

本文给出任意参数维数的充要条件，用来判定一个指定子块是否对所有参数都满足仿射格条件。在已解决的子块大小上，它直接给出真实可执行的通用宏。十七元由此获得五个新返回宏，现已全部展开为17或19次固定原子操作，无须调用十三／十五元定理。其中一个的整数矩阵行列式为3，并自然对应虚二次域 Q(sqrt(-2)) 中范数为3的乘法。结合 A，任意合法 B17 在至多三次返回后都能开启原库的十五元调用；该后续一般子块调用仍使用十五元定理。

这尚未完成 B17 的全方向控制或任意 n 的可达判定。一般定理判定的是一个指定调用模板的普遍合法性，不是整个平均问题。

## 2. 普遍仿射格判据

令 R=Z[1/3]，子块有 s 个值，写作齐次线性式
\[
f_i(z)=a_i z,\qquad a_i\in R^d,\quad z\in\mathbb Q^d.
\]
选 a_1 为锚点，设
\[
\bar a=\frac1s\sum_{i=1}^s a_i,\qquad
\delta=\bar a-a_1,\qquad
L=\sum_i R(a_i-a_1)\subset R^d.
\tag{1}
\]

**定理。** 下列条件等价：

1. delta 属于 L；
2. 对每个有理参数 z，均值属于该子块的仿射 R 格，即
\[
\delta z\in\sum_i R\bigl((a_i-a_1)z\bigr).
\tag{2}
\]

证明：正向由模表达式代入 z 立即得到。反向使用 R 为 PID。对 L 的行生成矩阵作 Smith 标准形，经可逆列变换后有
\[
L=Rd_1e_1\oplus\cdots\oplus Rd_ke_k.
\]
delta 原本在 L 的有理张成空间中，因为它是生成差分的 1/s 倍和。若 delta 不属于 L，则某个坐标 delta_j 不属于 d_jR。选择列变换对应的第 j 个对偶参数，(2) 就失败。这个参数可取在 R^d 中。因此甚至只检查全部 R 参数，也与(1)等价。

在 s 已有完整三平均判据时，(2)等价于每个子块输入的中心化本原 G 为三幂或子块全等。因此(1)给出**所有参数上的正向调用**。s 未解时，只能推出其必要仿射格条件，不能推出可达。

这是一个有效且多项式可判定的模板属性：清除三幂分母，计算整数 Smith/Hermite 标准形，并忽略商模的三次初级部分。它允许在参数搜索前剔除不合法模板或发现完全不需要局部 guard 的模板。

## 3. 与算术几何的严格联系

把 L 看作 Spec R 上平凡向量丛 R^d 的相干子模。障碍是商模中 delta 的类
\[
[\delta]\in(L+R\delta)/L.
\]
L+R delta 本来就是有理向量空间内的有限生成 R 模，即使 delta 有非三分母也成立。可以把 L 和 delta 共同缩放到整数格中比较；属于 L 时类为零。Smith 不变量描述障碍的素数支撑和幂次，行列式子式给出相应 Fitting 理想。

因此“模板对任意参数是否合法”可在参数值代入之前用有限的整系数模数据决定。它比只观察模 p 的一般位置更强：当所有差分在某个 p 处同时消失时，仍然正确跟踪其共同因子，不会把本原化后的合法状态误判掉。

这属于整数模与算术底空间上的线性代数，不要求先有自守群。theta 与 S-算术工具可以在筛出的真实返回宏上继续使用。

## 4. 十七元的通用十三元调用

从
\[
B_{17}(u,v)=(u^{13},v^3,w),\qquad w=-13u-3v
\]
出发，先平均九元子块 (u^8,v)。令
\[
d=(v-u)/9,\qquad a=u+d=(8u+v)/9.
\]
剩余状态为 (a^9,u^5,v^2,w)。选择十三元子块
\[
C=(a^8,u^3,v^2).
\]
它是固定整系数模式
\[
u+d\,(1^8,0^3,9^2),
\]
其系数平均为2，差分 gcd为1。因此均值
\[
x=u+2d=(7u+2v)/9
\tag{3}
\]
属于同一个仿射 R 格，对**所有** u,v 都可以调用十三元定理。d=0时子块本来全等。d不为0时，中心化本原模式为 (-1^8,-2^3,7^2)，其 G=1。

调用后状态为 (x^13,a,u^2,w)。余下四个位置任取一个作单点、平均另外三个，得到三个通用返回：
\[
R(u,v)=\left(\frac{7u+2v}{9},\frac{26u+v}{27}\right),
\tag{4}
\]
\[
B(u,v)=\left(\frac{7u+2v}{9},-\frac{11u+3v}{3}\right),
\tag{5}
\]
\[
C(u,v)=\left(\frac{7u+2v}{9},-\frac{100u+26v}{27}\right).
\tag{6}
\]
保留的单点依次为 w、a、u。每次仍恰好有17个实际位置；十三元调用不被计成一次原子操作。

这是一个固定仿射模式，而且有如下显式10步归并。对中心化系数状态 (-2^3,-1^8,7^2)，依次平均
\[
(7,7,-2),\quad(4,-2,-2),\quad
(4,-1,0)\text{ 两次},\quad(-1,0,1)\text{ 六次}.
\tag{6a}
\]
前两步后为 (4^2,-1^8,0^3)，再两步为 (-1^6,0,1^6)，最后六步全部归零。所有数值均为整数，每步都有所需的实际重数。任意平移缩放下，同一个位置词仍成立。

因此 R、B、C 各有一个**6+10+1=17步固定原子证书**。十三元完整定理帮助发现模式，但这些宏的最终实现已经不依赖它。

## 5. 虚二次域中的三进分裂素元

(5)的整数射影代表是
\[
\widehat B=\begin{pmatrix}7&2\\-33&-9\end{pmatrix},
\qquad \operatorname{tr}\widehat B=-2,\quad\det\widehat B=3.
\]
令 x=u, y=4u+v，则
\[
(x,y)\longmapsto(-x+2y,-x-y),
\]
这恰好是 Q(sqrt(-2)) 中乘以 -1-sqrt(-2)。因此
\[
q(u,v)=u^2+2(4u+v)^2=33u^2+16uv+2v^2,
\qquad q(\widehat Bz)=3q(z).
\tag{7}
\]
实际宏是 Bhat/9，故实际 q 缩为原来的1/27。对本原整数参数，共同因子只可能为1或3，因而本原 q 分别乘3或除3。

这给出一个确切的算术对应：3=(-1-sqrt(-2))(-1+sqrt(-2))，两个共轭素元对应3进两个特征方向。当前已实现的是其中一个乘法方向；其共轭方向或逆变换的正向实现仍须单独证明。仅由类数1或 theta 模性不能获得该实现，也不能保证任意输入都会进入 q 下降分支。

## 6. 第二个固定模式：十五元通用调用

先平均 (u^7,v^2)，令 a=(7u+2v)/9、d=(v-u)/9。选择子块
\[
(a^8,u^6,v)=u+d\,(2^8,0^6,9).
\]
系数差分 gcd为1，平均为5/3；中心化本原 G=3。因此已证十五元定理对全部参数适用，得到
\[
x=(22u+5v)/27,\qquad (x^{15},a,w).
\]
平均两个 x 与 a 或 w，可得另外两个通用宏
\[
D(u,v)=\left(\frac{22u+5v}{27},\frac{65u+16v}{81}\right),
\]
\[
E(u,v)=\left(\frac{22u+5v}{27},-\frac{307u+71v}{81}\right).
\tag{8}
\]
其整数射影代表的行列式分别为81、-81。D 保留前16个位置的平均，并将两块值之差缩小到1/81。

该子块也不必调用十五元完整算法。中心化并乘3后的系数状态是 (-5^6,1^8,22)，依次平均
\[
(22,-5,-5),\ (4,4,-5),\ (4,1,1),\
(-5,1,1)\text{ 三次},\
(2,-1,-1)\text{ 三次},\
(-1,0,1)\text{ 三次}.
\tag{8a}
\]
前三步后为 (-5^3,1^9,2^3)，再三步为 (-1^9,1^3,2^3)，再三步为 (-1^3,0^9,1^3)，最后全部归零。因此 D、E 各有**6+12+1=19步固定原子证书**。

五个新宏以及 A 的整数代表在模17都非奇异，并保持 u=v 的直线。因此所有合法 B17 参数都被送到合法 B17 参数。共同约分不会破坏这个结论，因为非奇异性排除了整体17因子。

## 7. 所有 B17 都能开启原十五元调用

原库的十五元子块 (u^12,v^2,w) 在本原合法输入上可调用，当且仅当 u+v=0 mod5。用 t=v/u 表示模5射影方向，A 的作用为
\[
t\longmapsto4+3t,
\]
固定无穷远。B 在六个方向上给出一个完整循环
\[
0\to1\to2\to4\to\infty\to3\to0.
\tag{9}
\]
A、B 的整数行列式都是5处单位，故模5射影方向沿实际路径始终有定义。下面的真实调度至多三步达到4=-1；表中词按时间顺序书写。

| 输入 t | 返回宏词 |
|---|---|
| 4 | 空词 |
| 0 | A |
| 2 | B |
| 1 | AB |
| 3 | BA |
| 无穷远 | BBA |

到达后 u、v 在5处都为单位且互不相等，所以目标十五元子块的仿射格条件成立。它同时含 u、v、w；原 B17 的合法性保证其差分 gcd 在本原整数代表上为1，故可独立核验中心化 G 只含3。

**结论：所有本原合法 B17 都可以用至多三次 A/B 返回宏进入原十五元调用域。** A 为一次原子平均，B 为17次原子平均；表中最长的 BBA 实际为35步。因此还得到统一的35步原子调度上界。这个上界只负责进入调用域，不是全部归零的常数步数上界，不违反缺失素数定理。

这严格加强了此前只处理奇背景局部陷阱的逃逸结论，也不再需要模7或模13单位条件。它没有声称本原高度下降，更没有把后续可重复调用自动当成终止算法。

## 8. 范数环面与真正可实现的 theta 分支

令 K=Q(sqrt(-2))，T=Res(K/Q) G_m / G_m。B 是 alpha=-1-sqrt(-2) 在这个有理环面中的作用。

- 实处 K 是复数，T 的实点为紧圆方向；
- 3在 K 中分裂，T 在3处是分裂环面，alpha与其共轭对应两个三进素元方向；
- 5在 K 中惰性，T(F5)=F25* / F5* 有6个元素，alpha 的类由(9)可见恰为生成元。

因此完整模5调度是一个**非分裂环面的传递作用**，并非偶然出现的六张余数表。它给出当前宏库与代数群的确切联系；尚不声称 A、B 生成整个算术群，也不声称正向半群含全部逆元。

写
\[
\theta(z)=\sum_{x,y\in\mathbb Z}z^{x^2+2y^2}.
\]
alpha 的整数矩阵为 [[-1,2],[-1,-1]]，像格恰是 X=Y mod3；其共轭的像格是 X=-Y mod3。由范数乘法得到严格恒等式
\[
\sum_{X\equiv Y\ (3)}z^{X^2+2Y^2}
=\sum_{X\equiv-Y\ (3)}z^{X^2+2Y^2}
=\theta(z^3).
\tag{10}
\]
两格交于3Z^2，且范数被3整除当且仅当 X=Y 或 X=-Y mod3，所以
\[
\sum_{3\mid X^2+2Y^2}z^{X^2+2Y^2}
=2\theta(z^3)-\theta(z^9).
\tag{11}
\]
第一条像格分支已由真实 B 宏实现，实际尺度是 Bhat/9；共轭分支暂时只有静态格解释，不能由恒等式直接认作正向宏。

该二次型的判别式为-8，其 theta 属于权1、级8、特征 chi_{-8} 的标准模形式空间。还可直接得到 Eisenstein 系数公式
\[
\theta(z)=1+2\sum_{m\ge1}\left(\sum_{d\mid m}\chi_{-8}(d)\right)z^m.
\tag{12}
\]
说明：O_K=Z[sqrt(-2)] 的 Minkowski 界为 (2/pi)sqrt(8)<2，故类数为1。每个范数为m的理想恰有两个生成元，理想计数由 zeta_K(s)=zeta(s)L(s,chi_{-8}) 给出，得到(12)。这里完全不需要猜测真实返回群等于某个同余容器。

## 9. 一般维数的模板设计

设 B_n=(u^r,v^3,-ru-3v)，r=n-4，m为至少3的三幂。相同构造给出两条参数化设计原则：

1. 先平均 (u^(m-1),v)，再调用 (a^(m-1),u^(r-m-1),v^2) 这个 r 元子块。若 r>=m+2、r 已解且 (3m-1)/r 属于 R，则其固定系数模式的差分 gcd为1，调用对所有参数合法。均值为 u+((3m-1)/r)(v-u)/m。
2. 先平均 (u^(m-2),v^2)，再调用 (a^(m-1),u^(r-m+2),v) 这个 r+2 元子块。若 r>=m-1、r+2 已解且 (3m-2)/(r+2) 属于 R，则系数模式含0、2、m，差分 gcd为1，仍得到通用调用。

取 r=13、m=9，两个比值正是2与5/3，产生本文的全部新宏。这些是任意维数上的构造与筛选规则；适用大小必须已解，且它们自身没有保证下降，不能据此声称任意 n 已完成。

## 10. 下一项明确缺口与核验

一个有价值且可证伪的充分猜想是：存在对全部合法 B17 参数可执行的正向返回，其射影作用等于
\[
\overline B=\begin{pmatrix}-9&-2\\33&7\end{pmatrix}
=\operatorname{adj}(\widehat B),\qquad
\overline B\widehat B=3I.
\tag{13}
\]
这将实现共轭素元方向，并给出 B 的正向射影逆元。需要同时提交真实位置词或已解子问题模板及其全域证明；矩阵在形式群中可逆不算证明。即使(13)实现，完整 B17 控制仍需要合法终端覆盖与终止论证。

另一条路线是保留单向范数乘法，联合 A、D、E 与条件宏证明某个算术高度的下降。q 在 B 后可能乘3也可能除3，故“q 是整数范数”并没有自动完成这一步。

### 10.1 当前通用库不能提供固定逆词

此处已经有一个严格的库内排除结果。记
\[
\Omega=\{[1:0],[0:1]\}\subset\mathbb P^1(\mathbb F_3).
\]
在这些点上，A、R、C、D、E 的本原整数矩阵都给出**非零**输出并落在 [0:1]；B 都给出非零输出并落在 [1:0]。所以任意正向整数矩阵乘积在 e_1 上仍模3非零。

但 Bbar 的第一列 (-9,33) 模3为零。若某个整数乘积 P 与 Bbar 射影相等，则 P=c Bbar；Bbar 的矩阵条目 gcd为1，故 c 必为整数。这样 P e_1 模3必为零，矛盾。

**因此仅由 A、R、B、C、D、E 组成的矩阵半群，不含 B 的射影逆元。** 扩大这种固定词搜索的深度没有帮助。若要实现(13)，必须引入另一类宏，例如有整除条件的十四元分支，或更多中间分层。此结论只排除固定矩阵词，不排除对每个输入单独选择不同的、无统一长度界的轨道路径。

### 10.2 十四元分支可打破该三进限制

原条件库的两条十四元返回为
\[
F_1=\frac1{42}\begin{pmatrix}-3&-6\\13&12\end{pmatrix},
\qquad
F_2=\frac1{42}\begin{pmatrix}-6&-3\\12&13\end{pmatrix}.
\tag{14}
\]
其合法条件分别是 u+2v=0 mod14 与 2u+v=0 mod14。如果再分别有 u=0 mod3 与 v=0 mod3，则矩阵分子在输入上同时被42整除。于是它们将**当前本原整数代表**送到整数代表，真实三平均的严格能量下降给出
\[
H(\operatorname{prim}(F_i z))<H(z),\qquad
H=91u^2+39uv+6v^2.
\tag{15}
\]
输入合法保证子块非恒等，并且输出仍合法。这里 F_i 内部调用已证十四元定理；该调用尚未被统一展开成一个固定原子词。

对于三进方向属于 Omega 的输入，只需记录
\[
\mathbb P^1(\mathbb F_2)\times\mathbb P^1(\mathbb F_7)\times\Omega,
\]
共3*8*2=48类。A、B 在这48类上的作用处处有定义。目标为
\[
(\infty,3,\infty)\quad\text{使用 }F_1,
\qquad (0,5,0)\quad\text{使用 }F_2.
\]
下表给出全部24种前两项的预备词，对 Omega 的两个初始方向都成立。行是 t_7，列是 t_2；按时间顺序执行。

| t_7 | t_2=0 | t_2=1 | t_2=无穷远 |
|---|---|---|---|
| 0 | BABB | BBB | BBA |
| 1 | BBBB | BBABB | BBBA |
| 2 | BBAB | ABBAB | BBAA |
| 3 | BBBBBB | BAB | BAA |
| 4 | AB | BBBBB | AA |
| 5 | ABBABB | ABBBB | ABBBA |
| 6 | ABAB | B | A |
| 无穷远 | BB | ABB | BA |

直接代入矩阵可核对：前两列到 F_2 的目标，第三列到 F_1 的目标。全部词长至多6。A、B 在 Omega 上不产生共同3因子，且行列式只含3，故预备阶段的本原整数参数可以直接用整数矩阵乘积跟踪。

这说明需要的十四元分支并不会因辅助同余条件而永远不可用。若初始三进方向为[1:1]，一次 A 将它送入 Omega；若为[1:2]，A 本身已是整数下降，除非三元组本来恒等，而后者对应不合法方向。

**仍然缺失的是净下降：** (15)比较的是预备词之后的高度，不是整个过程最初的高度。预备阶段可能增长，不能由48类全覆盖宣布全局终止。这一明确边界决定下一步应研究预备矩阵与 F_i 的复合二次型，或调整适用域内的词以控制总高度。

work/verify_b17_universal_subblocks.py 独立重放编译出的8个模板（其中3个为恒等、A、A平方，5个为新宏），共1008个含退化和高公因子参数的接口；额外按固定位置词重放630个实例，确认17、17、17、19、19步证书；核对684个合法参数的全六类调度及最后十五元调用；核对1440个本原范数分支和至600次的 theta 系数。此外检查固定正向逆词的模3障碍、48类图的完整覆盖、上述24词表以及48个十四元整数下降接口。一般无限量词由上面的模判据、固定模式和格恒等式证明，有限参数仅检验实现。

work/b17_universal_atomic_words.py 可直接输出五个完整原子词和输出位置账本。它只使用标准库，不导入十三元、十五元的定理验证器，也不调用子问题求解器。后续宏可以按输出账本重标位置，不需要执行额外的交换操作。

发现入口 work/explore_b17_universal_subblocks.py 按系数与重数枚举，约0.1秒量级完成，不展开位置树。当前程序实现二维行模包含；第2节的 Smith 标准形定理对任意参数维数成立。work/explore_b17_nine_thirteen_bridges.py 保留发现初期的保守模13模板搜索；它把模13全等类暂时排除，不能取代本文的本原模判据。旧文档与验证均保留：[旧 B17 实验](../sources/outputs/triple_average/history/triple_average_b17_guarded_subproblem_experiment.md)、[旧跨分块逃逸](../sources/outputs/triple_average/history/triple_average_b17_cross_stratum_escape.md)。

<!-- END SOURCE doc-a20253f0d3b0 -->

---

<a id="doc-35981543be1f"></a>

## 原文导签：危险素数的见证重置：局部约分为何必须纳入一般算法

来源：`outputs/triple_average/history/triple_average_witness_reset_lemma.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_witness_reset_lemma.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`multi-prime-core`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-35981543be1f -->
# 危险素数的见证重置：局部约分为何必须纳入一般算法

> **复核修正：** 以下重置引理仅在中心化状态的主余类本来就是 $0\pmod p$ 时保持目标为零。平移主余类后必须同时跟踪目标平均值，不能对未中心化商状态直接使用 $G$ 判据。精确区分及七元反例见 [研究勘误](../sources/outputs/triple_average/history/triple_average_research_corrections.md)。

覆盖设计说明了固定见证的安全下降会停住。这里把触发下一步的局部机制写成一个可直接使用的引理。

## 1. 引理

设 $p\ne3$ 是 $n$ 的素因子，$X$ 是零和整数状态。设 $F$ 是一组至多三个位置，且原中心化坐标满足：

\[
x_i\equiv0\pmod p\qquad(i\notin F).
\]

若选取三元组 (S) 满足 (F\subseteq S)、(|S|=3)，并且三平均是整数，则对选中和 (s=\sum_{i\in S}x_i) 有

\[
s\equiv0\pmod p,
\qquad q=s/3\equiv0\pmod p.
\]

所以平均后的所有坐标都被 (p) 整除。把新状态写成 (pY)，则 (Y) 是一个整数状态，并且

\[
X\longrightarrow X'=pY,
\qquad X'\text{ 可归零}\Longleftrightarrow Y\text{ 可归零}.
\]

这里的等价性来自三平均对平移和非零数乘都保持协变：对任意 (c) 和 (\lambda\ne0)，先对 (X) 作操作再变换为 (\lambda X+c)，与先变换再作同一位置操作完全相同。

## 2. 证明

这里不另作平移；主类已按假设为 $0\pmod p$。若 $|F|=3$，总和模 $p$ 给出

\[
\sum_{i\in F}x_i\equiv0\pmod p,
\]

因为 (p\mid n) 且所有 (F) 外坐标为零模 (p)。若 (|F|=2)，补入一个 (F) 外位置，所选第三个坐标仍为零模 (p)，结论相同。由于 (3) 在 (\mathbb F_p) 中可逆，(q\equiv0\pmod p)。未选坐标本来全为零模 (p)，选中位置被 (q) 替换后三个也为零模 (p)，故整态可除以 (p)。

## 3. 局部轮廓的精确变换

对一个整数状态 (X)，定义 (p^k) 层的缺口

\[
\epsilon_{p,k}(X)=
\min_{c\in\mathbb Z/p^k\mathbb Z}
\#\{i:x_i\not\equiv c\pmod{p^k}\}.
\]

对合法输入，危险素数正是 $\epsilon_{p,1}(X)\le3$ 的情形。按本引理进行零主类重置后，输出 $X'=pY$ 仍零和，并有精确关系

\[
\epsilon_{p,k}(Y)=\epsilon_{p,k+1}(X')
\qquad(k\ge1).
\]

因此一次局部约分不是简单地“删除一个素数障碍”，而是把该障碍从 (p) 的第一层推进到更深的 (p)-进层。若 (Y) 在模 (p) 下已经有两个不同余类，则 (p) 从 (G(Y)) 中消失；若没有，则新的危险见证位于原状态的模 (p^2) 结构中。

有一个直接可用的锚点判据。若重置前存在两个未选位置 (i,j) 满足

\[
x_i\equiv x_j\equiv0\pmod p,
\qquad x_i\not\equiv x_j\pmod {p^2},
\]

那么重置后的商状态 (Y) 中

\[
Y_i-Y_j=(x_i-x_j)/p\not\equiv0\pmod p,
\]

所以 (p\nmid G(Y))。只有当所有未选位置在模 (p^2) 下又落入同一余类时，(p) 才能继续作为新的危险素数出现。这把“见证交换”分成了两个可检验分支：锚点存在时局部障碍消失；没有锚点时，危险支持被推进到更深的 (p)-进层。

这给出了一个应当显式记录的局部状态：

\[
\bigl(\epsilon_{p,1},\epsilon_{p,2},\ldots\bigr)_{p\mid n, p\ne3}.
\]

有限坐标的位长给出有限的非平凡 (p)-进层，但重复值会使缺口在高层持续为小。后者正是高重数块必须与局部轮廓一起处理的原因。

## 4. 覆盖设计中的触发

在 [覆盖设计障碍](../sources/outputs/triple_average/history/triple_average_covering_design_obstruction.md) 的显式五例外构造中，每个危险素数 (p_F) 的非主类支持集正是 (F)。所有模 (3) 零和三元组都包含某个 (F)，所以它们都不是“见证保持安全”操作；但选中 (F) 后满足本引理，输出有一个可约去的 (p_F) 因子。

这解释了为何该构造不产生不可达反例：它把安全下降问题转换成了见证重置问题。

## 5. 一个可检验的统一桥命题

目前最自然的下一步不是要求每次操作都保持所有第一层见证，而是证明以下命题。

> **原桥猜想的范围修正。** 若不存在非恒等整数三平均，也不可能存在上述整数重置三元组。可继续研究的范围是：存在非恒等整数操作、且被击中的危险素数具有零主余类的状态；即便在此范围，重置后保持合法性仍需证明。一般桥必须允许分数宏和目标感知的深层局部检查。

可以用于寻找下一步的联合数据包括：

1. 平方能量 (E)；
2. 各危险素数的 (p)-进缺口轮廓；
3. 例外位置的覆盖超图复杂度。

若一步确为非恒等整数平均且约分后仍合法，本原平方能量已经严格下降，足以支持有限迭代。附加轮廓的用途是证明存在合法下一步，并处理分数宏，不能把它说成整数下降终止所必需。

## 6. 与单危险素数情形的关系

当只有一个非三素数 (pmid n) 时，支持集 (F) 最多三个位置，且高重数核心定理把状态压到四个例外；见证重置通常可直接改写成进入 (mathcal B_n) 的桥。因此单危险素数的二维控制器问题仍是一般理论的基本模型。

多个危险素数时，不同支持集之间会交叠，见证重置可能轮换危险素数。一般任意 (n) 的桥定理必须控制这种轮换，而不能简单地把多素数问题当作若干独立的单素数问题相乘。

## 7. 当前可核验内容

* `work/construct_five_exception_core.py` 构造 (r=5) 覆盖设计，并检查所有允许三元组都被支持集覆盖。
* `work/check_five_core_operations.py` 检查选中支持集后确实出现可约去的局部共同因子，并列出约分后仍为 (G=1) 的候选操作。
* `work/verify_multi_prime_core.py` 对小维数枚举验证原有 (n-3d-1) 核心界。

这些脚本验证的是局部机制和组合边界，不是任意 (n) 的充分性证明。

<!-- END SOURCE doc-35981543be1f -->

---

<a id="doc-22abc15be049"></a>

## 原文导签：可填充三幂块的统一收尾

来源：`outputs/triple_average/history/triple_average_zero_padding_theorem.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_zero_padding_theorem.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`zero-padding`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-22abc15be049 -->
# 可填充三幂块的统一收尾

现有的 \(3^k+1\) 维零坐标命题可以推广成一个适用于任意维数的充分条件。它揭示了三平均问题中一个比具体终端族更基本的收尾机制。

## 定理

设 \(X=(x_1,\ldots,x_n)\) 是有理数状态，平均值为 \(\mu\)。令

\[
r=\#\{i:x_i\ne\mu\},
\]

并令 \(q\) 是不超过 \(n\) 的最大三幂。若

\[
r\le q,
\]

则 \(X\) 可以有限步三平均到全体 \(\mu\)。

平移 \(\mu\) 后只需证明零和状态且至少有 \(n-r\) 个零坐标可达全零。

取满足

\[
r\le 3^k\le q
\]

的最小三幂 \(3^k\)。从全部 \(r\) 个非零位置和 \(3^k-r\) 个零位置组成一个块 \(B\)。块和等于全局和 \(0\)，所以块平均值为 \(0\)。对 \(B\) 施行标准三进张量网络，恰好把这 \(3^k\) 个位置全部变成零；块外原来也是零，故整个状态归零。

块网络的操作数为

\[
k3^{k-1},
\]

其余位置不参与操作。

## 等价的重数形式

该条件也可以写成：

\[
\#\{i:x_i=\mu\}\ge n-q.
\]

所以只要平均值的重数达到 \(n-q\)，就有一个与输入数值无关的显式归零证书。特别地：

* \(n=3^k+1\) 时，\(q=3^k\)，一个平均值坐标就足够；
* \(n\le2\cdot3^k\) 时，平均值重数至少 \(n-3^k\) 就足够；
* 若 \(n=3^k\)，条件自动成立，恢复标准三进网络。

## 与高重数终端的关系

一般安全下降得到的是某个重复值 \(u\) 的高重数，而不是平均值 \(\mu\)。这一区别是实质的：若 \(u\ne\mu\)，把所有例外坐标和若干个 \(u\) 坐标凑成三幂大小的块，块平均通常不是 \(\mu\)。因此“高重数”本身不能直接替代“高平均值重数”。

这给出一个清晰的桥接目标：

> 从 \((n-4)\) 重值或更一般的高重数终端，构造一个平均值坐标，或者构造一个三幂大小、平均等于全局平均的块。

十元例子中先制造三个零坐标，再对剩余九个位置使用三进网络，正是这个机制。该观点把零坐标终端、三进等块压缩和一般张量网络统一成一个“可填充三幂块”条件。

## 算法意义

对于给定状态，这个条件是可直接检查的。若中心化后有至少 \(n-q\) 个零坐标，算法立即输出块网络；不需要搜索二维宏，也不需要判断任何非三素数局部条件。

因此任意 \(n\) 的判定算法可以先加入这一层：

1. 中心化并清除分母；
2. 检查平均值重数是否至少 \(n-q\)；
3. 若是，直接按最小三幂块归零；
4. 否则再进入安全下降或二维核分析。

这不是一般充要条件。五元反例没有足够的零坐标，但它说明失败的根源是三进动态闭合；相反，许多成功状态会先经过一个短宏产生足够多的零坐标，再触发本定理。


<!-- END SOURCE doc-22abc15be049 -->

---

<a id="doc-07cd1b56f163"></a>

## 原文导签：有界切换之后的文献调查：Lucas赋值、混合逼近与Hecke周期

来源：`research/prime_arity_padic/five_torus_literature_20260917/switch_hecke_review_20260917.md` · [逐字节原样副本](../sources/research/prime_arity_padic/five_torus_literature_20260917/switch_hecke_review_20260917.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-07cd1b56f163 -->
# 有界切换之后的文献调查：Lucas赋值、混合逼近与Hecke周期

2026-09-17，续[上一轮适用性审查](../sources/research/prime_arity_padic/five_torus_literature_20260917/targeted_review_20260917.md)。本轮没有找到三平均五元的现成全分类，但找到一条确实能代入的Hecke／连分数定理，并借Lucas赋值定理识别D=1族的第一段。

查询保存在switch_query_*.json、gap_query_*.json、gap_followup_query_*.json、order_query_*.json。后者宽泛search再次给出大量无关结果，未据此声称类数文献适用。没有通过题录结果或论文标题推定定理成立。

## 1. Aka–Shapira：这次能够真正代入

Menny Aka, Uri Shapira, *On the evolution of continued fractions in a fixed quadratic field*, Journal d’Analyse Mathématique134 (2018),335–397，DOI[10.1007/s11854-018-0012-4](https://doi.org/10.1007/s11854-018-0012-4)。

- [作者稿](https://arxiv.org/pdf/1201.1280)，取得的是v2，2013-02-21，不以文件命名年份冒充稿件版本。
- [本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/aka_shapira_quadratic_continued_fractions_2018.pdf)、[文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/aka_shapira_quadratic_continued_fractions_2018.txt)、[来源散列](../sources/research/prime_arity_padic/five_torus_literature_20260917/aka_shapira_quadratic_continued_fractions_2018_source.json)。
- 实际读：摘要、§1、§2至Theorems2.8、2.12、Corollary2.10及Definition2.6；另检索§4中Hecke图与分裂／退化分支的定义位置。没有全文重审谱隙证明。
- 期刊PDF链接返回HTML而不是PDF，见[记录](../sources/research/prime_arity_padic/five_torus_literature_20260917/aka_shapira_journal_attempt.json)；未将其视为取得期刊全文。

定理2.8(2)对S中素数都不分裂于Q(θ)时，给γθ的普通实连分数周期测度随着ht(γ)→∞趋于Gauss测度，且误差对γ一致。这里ht是本原整数代表的行列式绝对值，**不是矩阵最大系数**。

本题取θ=(−7+3√5)/2、S={3}、γ=W⁻¹。3惰性，正词矩阵及其伴随本原，故ht(W⁻¹)=3^L。全部假设满足，得到长词拉回零方向的连分数周期等分布。定理2.12给周期长度与3^L同阶。

独立初等证明进一步说明，同长度词的拉回范数型在GL₂(Z)乃至SL₂(Z)下等价；所以这些二次无理点的普通连分数周期本来就相同。定理研究的是这个共同周期随导子增长的分布。

**准确边界：** 周期等分布不控制标记Ce，不能据此推出F_f(Ce)=±5D的命中有限。需一个将真实正词约束传到周期中指定位置的额外定理。本轮没有把这项缺口隐藏在“均匀”一词中。

## 2. Lucas赋值：直接使用的数列公式

Nadir Murru, Carlo Sanna, *On the k-regularity of the k-adic valuation of Lucas sequences*, J. Théor. Nombres Bordeaux30 (2018),227–237，DOI[10.5802/jtnb.1025](https://doi.org/10.5802/jtnb.1025)。

- [作者稿](https://arxiv.org/pdf/1603.09310)，实际v3，2016-06-04。
- [本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/lucas_valuations_regularity_2018.pdf)、[文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/lucas_valuations_regularity_2018.txt)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/lucas_valuations_regularity_2018_source.json)。
- 实际读：引言、Theorems1.1–1.6、§2初始定义及k-regular性质；所用公式为Theorem1.5的标准Lucas赋值式。

代入Fibonacci递推a=b=1、p=3、Δ=5、τ(3)=4、v₃(F₄)=1，得v₃(F_n)=1+v₃(n)当4|n，否则0。结合F_(2n)=F_nL_n和本项目D=1的Lucas表达式，得

\[
v_3(u_k)=v_3(2k+1),\qquad v_3(v_k)=v_3(2k-1).
\]

赋值恒等式也可直接由单位φ的二项式提升证明，正文给了这条自足来源。k-regular只用于解释这种字段可以很简单，不从它推出整个可解语言有限自动机可识别。

## 3. 混合Littlewood文献：有启发，但不作为原问题有限性的证明

Paloma Bengoechea, Evgeniy Zorin, *On the Mixed Littlewood Conjecture and continued fractions in quadratic fields*, Journal of Number Theory162 (2016),1–10，DOI[10.1016/j.jnt.2015.10.007](https://doi.org/10.1016/j.jnt.2015.10.007)。OpenAlex题录列2015；Crossref期刊出版日期为2016-05，本文采用后者。

- [作者稿](https://arxiv.org/pdf/1409.3439)，实际v1，2014-09-11。
- [PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/mixed_littlewood_quadratic_2015.pdf)、[文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/mixed_littlewood_quadratic_2015.txt)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/mixed_littlewood_quadratic_2015_source.json)。文件名2015保留下载时命名，不代表正式出版年份。
- 实际读：引言、Theorem2.1、Hypothesis1、Lemma2.3开头及Aka–Shapira的引用接点；未重审后半部分证明。

论文以Aka–Shapira结果处理二次无理数的实逼近与有限素集的整除条件。它说明“二次无理数实上难以逼近”与“加上某个p进整除条件仍可得到许多好逼近”并不冲突。其候选整数不要求落在本题正词轨道中，所以既不能给本题反例，也不能给固定D有限性。

Bernard de Mathan, *On a mixed Littlewood conjecture for quadratic numbers*, J. Théor. Nombres Bordeaux17 (2005),207–215，DOI[10.5802/jtnb.487](https://doi.org/10.5802/jtnb.487)。OpenAlex/Crossref在线日期显示2008；[期刊卷页](https://jtnb.centre-mersenne.org/item/JTNB_2005__17_1_207_0/)明确纸本年份2005。

- [PDF](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.487.pdf)、[本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/mixed_littlewood_quadratic_2005.pdf)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/mixed_littlewood_quadratic_2005_source.json)。
- 实际读摘要和引言文字；提取文本漏掉关键公式，因此**没有依此援引Theorem1.2的精确不等式**。相关背景从Bengoechea–Zorin清晰作者稿交叉读取。

## 4. 这一轮真正带回来的东西

外部工具并非完全无用：Lucas赋值给直接算术字段；Hecke／谱隙工具确实控制共同周期。另一方面，计算共同二次型类并不会产生所求判据，因为所有同长度词已经在同一类。

新重点是共同周期上的**标记位置**，不是重新追逐不同类。完整的新公式、格分解和仍缺的量词见[研究正文](../sources/research/prime_arity_padic/five_explicit_gap_common_hecke_form_20260917.md)。

<!-- END SOURCE doc-07cd1b56f163 -->

---

<a id="doc-a0991a965356"></a>

## 原文导签：五元问题的定向外部调查与适用性审查

来源：`research/prime_arity_padic/five_torus_literature_20260917/targeted_review_20260917.md` · [逐字节原样副本](../sources/research/prime_arity_padic/five_torus_literature_20260917/targeted_review_20260917.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-a0991a965356 -->
# 五元问题的定向外部调查与适用性审查

2026-09-17。目的不是搜到相似名词就引用，而是查是否已有直接答案，并核对轨道整数点定理能否处理本题的两个一次分支。本页记录实际取得、实际读取和未能适用的原因；不声称全文重审所有证明。

## 1. 检索记录

OpenAlex的12条标题查询、8条扩展标题查询、6条全文题录查询，分别保存在targeted_query_*.json、extended_query_*.json、broader_query_*.json。包括clique gossiping、perfect mixability、integral points in orbits、semigroup orbits、S-unit points、p-adic path set、Pell equation matrix semigroup等。宽泛查询出现大量无关结果，未当成证据。入口脚本：[search_five_orbit_literature.py](../sources/research/prime_arity_padic/five_torus_literature_20260917/search_five_orbit_literature.py)。

另用Stack Exchange公开API检索MathOverflow和Mathematics上的averaging、five numbers、Pell与p-adic Cantor，六条查询见community_query_*.json，读取的问答原文见community_*_questions.json及community_*_answers.json。没有发帖或向作者发送消息。

本轮没有找到直接覆盖“有理五元三平均静态分类”的现成答案。这不是已证明不存在相关文献，尤其题录搜索可能漏掉竞赛题、不同术语或未收录文稿。

## 2. 最贴近模型的来源：Clique Gossiping

Yang Liu, Bo Li, Brian D. O. Anderson, Guodong Shi, *Clique Gossiping*。

- [实际取得版本](https://arxiv.org/pdf/1706.02540)：PDF首页明确为arXiv:1706.02540v1，2017-06-08。
- 期刊题录DOI：[10.1109/TNET.2019.2952082](https://doi.org/10.1109/TNET.2019.2952082)。未取得并核对期刊最终正文。
- 本地[PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/clique_gossiping_2017.pdf)、[文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/clique_gossiping_2017.txt)、[SHA256](../sources/research/prime_arity_padic/five_torus_literature_20260917/clique_gossiping_2017_source.json)。

实际读：定义3的原子等权操作，§4开头及定义8，定义9，定理3，§4.2必要性证明及§4.3零测论证。其操作确实与固定位置平均一致；目标主要是一个网络对所有实初值有限收敛，区别于给定有理初值的分类。

**重要核查结果：不能引用该v1定理3的m|n必要性。** 项目已有六平均九位置固定四步网络与其直接冲突，不仅是量词不一样：该网络对全部实初值都有效。重新独立乘9×9有理矩阵，结果为J9/9，81项逐项精确验证。

错误所在：§4.2第二项声称约成最简后的分母始终含某个p的指定幂次；分子相消可消去该因子，平均分母包含p并不意味着最简分母始终包含p。取e1作为初值，四步网络最后成为(1/9,...,1/9)，最简分母没有2。此判断只针对取得的v1，不推断最终版未修正。

§4.3“可解实点是可数个线性子空间之并”的观察本身仍有用，但不能从实零测推断有理格点的零密度，也不给五元算术全分类。

## 3. 最直接的半群整数点定理：次数假设不符

Jorge Mello, *On quantitative estimates for quasiintegral points in orbits of semigroups of rational maps*, New York J. Math.25 (2019),1091–1111。

- [期刊PDF](https://nyjm.albany.edu/j/2019/25-47p.pdf)、[本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/mello_quasiintegral_semigroups_2019.pdf)、[文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/mello_quasiintegral_semigroups_2019.txt)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/mello_quasiintegral_semigroups_2019_source.json)。
- 实际读：第1091–1092页引言及Theorem A；检索正文相关次数假设，并读取第1099页末到§5开头。没有重审其Roth估计证明。
- Theorem A要求每个生成映射次数≥2，还有无全分歧／轨道不重复等条件。我们的α↦J(ε^±1α)次数1。不能代入，也不能把矩阵行列式−3误当映射次数3。
- 下载时两个猜测文件名404，后由期刊卷目录与摘要页取得正确的25-47p.pdf，记录保留。

Jorge Mello, *On intersections of polynomial semigroups orbits with plane lines*, Canadian Math. Bull.，DOI[10.4153/S0008439520000557](https://doi.org/10.4153/S0008439520000557)。

- [作者稿](https://arxiv.org/pdf/1907.03934)、[本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/semigroup_plane_lines_2020.pdf)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/semigroup_plane_lines_2020_source.json)。
- 实际读：引言、Theorem1.1、§2轨道定义。
- Theorem1.1要求成对多项式同次数>1，且排除双边线性共轭的单项式；还要求一个相容无限路径的交点无穷或映射可交换。本题既非这类多项式，也不满足次数条件。

Jorge Mello, Yu Yasufuku, *On higher dimensional integrality and multiplicative dependence in semi-group algebraic dynamics*, arXiv:2604.03745v1 (2026)。

- [作者稿](https://arxiv.org/pdf/2604.03745)、[本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/semigroup_integrality_2026.pdf)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/semigroup_integrality_2026_source.json)。
- 实际读：引言、Theorems1.1–1.2、Corollary1.3和Hypε讨论，以及引用表。
- 要求各射影态射次数≥2，并有指定的整数点非稠密假设。文中讨论Vojta猜想的关联，但不能据此把本题的正半群轨道有限性称为已由Vojta推出。

## 4. 代数对应的现成定理：核对了真正的缺失接口

Jorge Mello, *On sparsity of integral points in orbits and correspondences with big pullbacks under iterates*, arXiv:2501.04642v2 (2025)。

- [作者稿](https://arxiv.org/pdf/2501.04642)、[本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/mello_big_pullbacks_2025.pdf)、[文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/mello_big_pullbacks_2025.txt)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/mello_big_pullbacks_2025_source.json)。
- 实际读：引言Theorems1.2–1.5，§4的极化定义与Definition4.2（CIP），§5.1的Theorem5.1及Corollary5.2–5.3。未重审其引用的He–Ru与Ingram理论。

这篇比普通次数≥2映射更接近本题，因为允许多值对应。**但CIP不是简单地把所有前驱取并集。** 它要求除子逐步满足y*L_(i−1)=x*L_i。本题正规化投影x(t)=(t+1)²/t，y(t)=(t−4)²/[3(1−t)]均为二次；这条等式强迫每步deg L_i不变。一个点除子不能经CIP变成支撑至少三个点的有效除子，因此不满足Theorem1.5。

还直接算出范数点−5不具有第一步CIP：y*[-5]由t²−23t+31=0的两点组成，不在源投影的换支t↦1/t下不变。详细证明见[新研究第7节](../sources/research/prime_arity_padic/five_bounded_switches_and_correspondence_degree_20260917.md)。

这是一个有用的否定接口：五元已确实转成“对应轨道里的有界分母点”，只是这条对应没有该定理的扩张资源。不能把有两条分支与每条映射的代数次数混为一谈。

## 5. 三进分形及已有平均问答

William Abram, Jeffrey C. Lagarias, *p-adic path set fractals and arithmetic*, J. Fractal Geometry1 (2014)，DOI[10.4171/JFG/2](https://doi.org/10.4171/JFG/2)。

- [作者稿](https://arxiv.org/pdf/1210.2478)、[本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/padic_path_set_fractals_2014.pdf)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/padic_path_set_fractals_2014_source.json)。
- 实际读：摘要、§1至Theorems1.1–1.3（前三页）。对象按有限标号图中的普通p进数字路径定义，给维数及有理平移、Minkowski和的封闭性。
- 本题已有普通三进前缀非正则性，因此不能仅凭符号地址有两种字母就认定落在该有限自动机类。本文不引用其维数公式作为本题证明。

MathOverflow：[整数多重集的平均游戏](https://mathoverflow.net/questions/373175/an-averaging-game-on-finite-multisets-of-integers)，以及[2进整数上的平均过程](https://mathoverflow.net/questions/374084/an-averaging-procedure-on-finite-multisets-of-2-adic-integers)。已读取问题与API返回的现有答案。

前者限制同奇偶的整数二平均，问最长／最短终止及组合游戏；后者给四个2进数、可由无限二元序列编码的不终止例子。这与本项目“整数能量下降和p进无限边界分工”的视角相关，但不涉及三平均五元的静态判据。社区答案仅作为相关思路来源，不当作已发表的总分类定理。

## 6. 对研究路线的实际影响

本轮没有借外部论文宣布固定D有限性。受到“固定迭代”和“任意变换半群”需要分清的启发，补上了介于二者之间的通用定理：固定同方向段数时，任意独立段长都只有有限个固定D返回，而且有效。

证明完全初等：段长归一化后的参数只有一个有理极限0，模5标记阻止有限个极限投影消掉种子，Q_5的有理各向异性及实紧致性给正下界。见[完整证明](../sources/research/prime_arity_padic/five_bounded_switches_and_correspondence_degree_20260917.md)。外部检索改变了问题的分层和假设核对，但不是把一个不适用的深定理当作证明。

<!-- END SOURCE doc-a0991a965356 -->

---

<a id="doc-14572e4b2cbe"></a>

## 原文导签：全词逃逸方向：外部定理的实际贡献与适用边界

来源：`research/prime_arity_padic/five_torus_literature_20260917/uniform_escape_review_20260917.md` · [逐字节原样副本](../sources/research/prime_arity_padic/five_torus_literature_20260917/uniform_escape_review_20260917.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-14572e4b2cbe -->
# 全词逃逸方向：外部定理的实际贡献与适用边界

2026-09-17，接前两轮阅读。本轮主成果是[固定多块模板的统一逃逸](../sources/research/prime_arity_padic/five_bounded_templates_uniform_escape_20260917.md)，不是全词猜想已证。

## 1. ESS不再只用于相邻单位或一个周期

重新读取Evertse–Schlickewei–Schmidt作者稿第807–809页、Theorem1.1及非退化定义，来源仍为本目录已存[PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/evertse_schlickewei_schmidt_2002.pdf)。

这次的代入是固定r个重复块的特征值指数向量，其乘法群由r个参数方向生成，秩≤r。范数展开是有限个乘法特征之和。通过全部极小零子和划分，ESS把整数参数解集化成有限个格陪集。再由非负格中可比较的两点抽出指数射线，本题能量与三进谱排除所有恒值射线。

没有把非退化解有限误写成全部解有限；退化部分由格陪集归约处理。也没有把ESS解数上界当成指数最大值上界。因此多模板结论目前是有限性／统一逃逸，未给有效截止。

## 2. 固定周期的有效增长：实际使用Baker下界

Joël Ouaknine, James Worrell, *On the Positivity Problem for Simple Linear Recurrence Sequences*, ICALP2014，DOI[10.1007/978-3-662-43951-7_27](https://doi.org/10.1007/978-3-662-43951-7_27)。

- [作者稿](https://arxiv.org/pdf/1309.1550)，实际为v3，2014-04-28。
- [本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/positivity_simple_baker_2014.pdf)、[文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/positivity_simple_baker_2014.txt)、[下载散列](../sources/research/prime_arity_padic/five_torus_literature_20260917/positivity_simple_baker_2014_source.json)。
- 实际读：引言及§3关于有限极小点与Baker下界的说明；附录A Theorem7、Corollary8及其证明；引用表原Baker–Wüstholz来源。

Corollary8：对单位圆上的代数数λ、ζ，若λ^n≠ζ，则|λ^n−ζ|有可计算的n负幂下界。证明应用Theorem7的对数线性式下界，包含log(−1)来记录辐角的整周差。

本题固定混合块M的复特征值情形，把Q_5(M^nx)/det(M)^n化成单位圆上的一个固定二次Laurent多项式。其零点只有有限个；不会精确命中零，因为Q_5无非零有理零点。故该推论直接给有效指数／多项式逃逸下界。

原始来源是A. Baker, G. Wüstholz, *Logarithmic forms and group varieties*, J. Reine Angew. Math.442 (1993)。本轮使用上述正式论文的转述和推论，没有宣称取得或重审1993年原证明，也没有调用整篇正性判定算法。

同时取得Ouaknine–Worrell的 *Ultimate Positivity is Decidable for Simple Linear Recurrence Sequences*，[作者稿](https://arxiv.org/pdf/1309.1914)、[本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/ultimate_positivity_2014.pdf)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/ultimate_positivity_2014_source.json)。实际稿为v4，2017-04-05，文件名保留初始题录年份。阅读引言、非有效性与Baker方法的区别及引用表，用于追到上一来源；不援引其完整判定算法。

## 3. 分形逼近文献：为什么没有直接套用

Lior Fishman, David Simmons, *Extrinsic Diophantine approximation on manifolds and fractals*, DOI[10.1016/j.matpur.2015.02.002](https://doi.org/10.1016/j.matpur.2015.02.002)。

- [作者稿](https://arxiv.org/pdf/1406.0785)，实际v3，2015-01-10。
- [本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/extrinsic_fractals_2015.pdf)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/extrinsic_fractals_2015_source.json)。
- 实际读：摘要、引言、Theorem1.1与Corollary1.2。
- 其Dirichlet型结论研究实流形／实IFS极限集内的点，由集合外有理数逼近。我们的成功方向实稠密，限制却在三进处；此外目标是某个指定二次无理方向的**受限**逼近。不能据这个存在性结论推出本题禁止某类逼近。

Johannes Schleischitz, *On intrinsic and extrinsic rational approximation to Cantor sets*, DOI[10.1017/etds.2020.7](https://doi.org/10.1017/etds.2020.7)。

- [作者稿](https://arxiv.org/pdf/1812.10689)，实际v4，2019-09-09。
- [本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/cantor_intrinsic_extrinsic_2020.pdf)、[来源](../sources/research/prime_arity_padic/five_torus_literature_20260917/cantor_intrinsic_extrinsic_2020_source.json)。
- 实际读：摘要、§1.1及Definition1，辨认其收缩、实IFS与保有理假设。未声称读取并适配其全部高度估计。
- 本题两个Möbius分支不能直接当成该实仿射IFS，普通斜率三进前缀还已证明非正则，因此不能仅因为都称Cantor就搬用缺位数字结论。

## 4. 检索失败和未读范围也保留

查询记录：escape_query_*.json、escape_crossref_*.json、escape_context_query_*.json、escape_structure_query_*.json、escape_fractal_query_*.json、escape_recurrence_query_*.json等。OpenAlex本轮并行题录查询部分返回429，随后改用Crossref及单个DOI定位，没有把请求失败当作“无文献”。若干宽泛查询无关，不作为研究证据。

Mahler／Cantor论文取得题录及仓储页面，但仓储页面没有可用PDF链接；本轮未读全文，不引用其定理，详见mahler_cantor_*.json。另一些矩阵半群、Markoff、稀疏轨道搜索仅有题录，没有把表面相关性当成适用性。

目前真正承载新证明的是ESS的有限秩方程定理，以及用于单周期有效增长的Baker下界；任意换词的全局统一常数仍缺失。

<!-- END SOURCE doc-14572e4b2cbe -->

---

<a id="doc-16059490fecd"></a>

## 原文导签：整体结构调查的文献访问记录

来源：`research/prime_arity_padic/global_structure_investigation_20260916/source_index.md` · [逐字节原样副本](../sources/research/prime_arity_padic/global_structure_investigation_20260916/source_index.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-16059490fecd -->
# 整体结构调查的文献访问记录

2026-09-16。研究报告见[二维格几何与内容对偶](../sources/research/prime_arity_padic/global_structure_and_bounded_fiber_geometry_20260916.md)。本目录不修改原完成证明或全项目注册。

## 检索范围与筛选

保存32个OpenAlex请求、130条去重题录，涉及格宽／平坦性、二维整数凸包、参数整数规划、Graver与Markov基、低维矩阵半群可达、正则语言、有限时间共识和Clique Gossiping。`query_00`至`query_31`保留原查询及返回；泛关键词产生了明显无关的物理／医学等结果，均未作为证据。32次请求不是32个有用文献方向，130条题录不是130篇全文阅读。

以下5份PDF通过`%PDF`文件头验证并保存原始字节，再提取文本。每份`*_source.json`保存请求URL、最终URL、HTTP状态、字节数、SHA256。只引用下列实际读到的段落。

## 实际取得并阅读

1. **Gennadiy Averkov, Johannes Hofscheier, Benjamin Nill.** *Generalized flatness constants, spanning lattice polytopes, and the Gromov width*. Manuscripta Mathematica **170 (2023),147–165**，2021-12-31在线发表。DOI：[10.1007/s00229-021-01363-x](https://doi.org/10.1007/s00229-021-01363-x)。[正式PDF](https://link.springer.com/content/pdf/10.1007/s00229-021-01363-x.pdf)；[本地PDF](../sources/research/prime_arity_padic/global_structure_investigation_20260916/generalized_flatness_2021.pdf)、[文本](../sources/research/prime_arity_padic/global_structure_investigation_20260916/generalized_flatness_2021.txt)。
   - 阅读摘要、§§2.1–2.2（定理2.1、二维ILC(2)=3、与半群Hilbert基的区别）、§4定理2.1的证明相关段落。
   - 本题实际用到：宽凸体包含幺模单形；二维空格三角形幺模。后者在报告中另给自足证明。
   - 未将§3的Gromov宽度或辛几何结果用作平均可达性结论；文件名2021指在线年份，不把正式卷年写错。

2. **Igor Potapov, Pavel Semukhin.** *Vector Reachability Problem in SL(2,Z)*. MFCS2016, LIPIcs58,84:1–84:14。DOI：[10.4230/LIPIcs.MFCS.2016.84](https://doi.org/10.4230/LIPIcs.MFCS.2016.84)。[本地PDF](../sources/research/prime_arity_padic/global_structure_investigation_20260916/reachability_sl2_2016.pdf)、[文本](../sources/research/prime_arity_padic/global_structure_investigation_20260916/reachability_sl2_2016.txt)。
   - 阅读摘要、引言、§2定义、主定理14的收尾及§4命题15的正则语言限制版本与复杂度边界。
   - 仅用于确认有限菜单的向量／射影可达与词语言之间的准确接口。没有把其SL2(Z)前提扩成GL2(Q)，也没有调用算法来证明任意p的可达性。

3. **Thomas Colcombet, Joël Ouaknine, Pavel Semukhin, James Worrell.** *On Reachability Problems for Low-Dimensional Matrix Semigroups*. ICALP2019, LIPIcs132,44:1–44:15。DOI：[10.4230/LIPIcs.ICALP.2019.44](https://doi.org/10.4230/LIPIcs.ICALP.2019.44)。[本地PDF](../sources/research/prime_arity_padic/global_structure_investigation_20260916/low_dimensional_semigroups_2019.pdf)、[文本](../sources/research/prime_arity_padic/global_structure_investigation_20260916/low_dimensional_semigroups_2019.txt)。
   - 阅读摘要、引言的精确问题与群定义、§4定理16–17及证明收尾。
   - 该文GL2(Z)指整数逆，即行列式±1；不是所有满秩整数矩阵。半空间可达也不同于精确零超平面可达。未用其2019年引言判断2026年哪些一般问题仍开放。

4. **Alessio Mansutti, Mikhail R. Starchak.** *One-Parametric Presburger Arithmetic Has Quantifier Elimination*. MFCS2025, LIPIcs345,72:1–72:18。DOI：[10.4230/LIPIcs.MFCS.2025.72](https://doi.org/10.4230/LIPIcs.MFCS.2025.72)。[本地PDF](../sources/research/prime_arity_padic/global_structure_investigation_20260916/presburger_quantifiers_2025.pdf)、[文本](../sources/research/prime_arity_padic/global_structure_investigation_20260916/presburger_quantifiers_2025.txt)。
   - 阅读摘要、§1，含定理2–3、语言定义、CRT示例、适用性与复杂度说明；检索后文系数消元的接口，未通读全部算法正确性证明。
   - 一参数t允许t乘变量，并不允许任意两个计数变量相乘。本题p、r及来源／输出的双线性关系不能直接当作这一语言；只可作为某些已选一参数公式的验证工具。

5. **Imre Bárány.** *Random points and lattice points in convex bodies*. Bulletin AMS **45 (2008)**。DOI：[10.1090/S0273-0979-08-01210-X](https://doi.org/10.1090/S0273-0979-08-01210-X)。[作者稿PDF](https://real.mtak.hu/57662/1/rsurv.pdf)；[本地PDF](../sources/research/prime_arity_padic/global_structure_investigation_20260916/barany_lattice_survey_2008.pdf)、[文本](../sources/research/prime_arity_padic/global_structure_investigation_20260916/barany_lattice_survey_2008.txt)。
   - 阅读摘要及§13的整数凸包、定理13.1和引理13.2所述平坦性用途。
   - 仅作背景与来源追踪，未用随机多面体或渐近顶点计数作本题全参数非空证明。

## 已有来源的回读

读取[上一轮整数移动来源记录](../sources/research/prime_arity_padic/literature_integer_moves/README.md)，并对照项目中对Graver同号分解、Markov基以及有界库存的使用范围。没有把此前未取得全文的Diaconis–Sturmfels或Onn专著升级为已读全文。

## 未取得／仅题录

- Bogart–Goodrick–Woods 2017的Discrete Analysis下载返回HTTP200但**零字节**，未作为已读PDF。其背景由已读2025论文准确引用，未直接引用2017原文中的独立新定理。
- 1988年RAIRO *Parametric integer programming* 的公开PDF请求超时，未读正文。
- Bounded contingency tables、二维整数凸包算法、Clique Gossiping等本轮仅核对检索题录及其访问位置，未移用未读定理。
- 本轮没有联系作者、发送问题或发布成果；所有新增文件均为本地研究记录。

## 计算职责

`fiber_geometry_probe.py`及`verify_geometry_and_content.py`枚举的是限定来源的有界计数纤维，检查新结构引理的公式和实例；不搜索平均词，不证明全参数资源存在，不运行旧的大模群搜索。

研究报告的新一般证明与外部平坦性推论逐项分开。文件下载成功或有限核验通过都不代替该区分。

<!-- END SOURCE doc-16059490fecd -->
