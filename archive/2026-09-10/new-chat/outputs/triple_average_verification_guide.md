# 三平均研究的计算核验指南

新增 strategy-reassessment-20260912：路线重评估和文献缓存为研究记录，不是证明核验。策略脚本缓存44个查询、148个去重题录；障碍脚本通过56个多素数单位分离、3538个返回字符和117个一般合并恒等式。

本文回答三个接手问题：哪项数学结论对应哪个程序，程序的 PASS 究竟证明到哪里，以及怎样在相同参数下重现当前数字。它是导航和复核契约，不替代证明文档。

新增 arbitrary-arity-linear-threshold（core/full）：[任意元数线性阈值](arbitrary_arity_linear_threshold.md)证明所有整数q>=3在n>=4q-1+d_q(n)时的完整G支持判据。一般量词由非单位配比、唯一中点例外、一般EGZ及系数打包证明承担。核对987个配比、172个中点例外、3040个容量、4488个四/六平均完整余数多重集、2804个大整数闭包及39次初始化；70条完整路径最长94步，另24条四/六平均造零收尾路径。全部15种算法分支均触及，不修改旧素数求解器适用域。未证明最优阈值或位长多项式输出长度。

新增 four-average-nine-complete（core/full）：[四平均九元完整判据](four_average_nine_complete.md)由显式(T2 Sigma)^2=-2I及仿射配对产生正向二进上下根，模9的12个陪集全部36条回路主元均为1、2、4，Schreier给出Gamma_0(9)包含，再接任意合法入口、Bezout和三步终端。检查72个本原模行、144个入口、50个大整数输送及6条完整四平均路径，最长621步。不做种子或路径搜索；不提供最短界或一位精度保证。

新增 composite-four-six-transfer（core/full）：[合数平均的统一半块转译](composite_arity_four_six_transfer.md)手写证明偶数q、q/2|n且吸收奇素因子后的二平均商维数M=2或M>=4时的完整G判据。推论覆盖四平均所有偶数n>=8（另有n=4）、六平均全部3|n且n>=6；纯三幂六平均由九元四步固定网络补齐。533个标准基重放、35个副本宏、30915+1500个陷阱后继、169次独立分组修复与336条完整Fraction路径通过。四平均六元和六平均八元的G=1反例由无限不变量证明，程序只审计有限后继。未给出其他维数完整分类、最终阈值或最短解；不使用未经全文核查的Clique Gossiping摘要判据。

新增 carrier-energy-dyadic-neighbour（core/full）：[能量与 2p+2 完整族](prime_arity_energy_and_dyadic_neighbour.md)证明 p=2^s-1 的完整 n=2p+2 判据，允许合数 p。一般安全交换、CRT 单点等值化和正向除法返回使 |v| 严格阶段下降，新增七平均十六元，不调用十五元端点。核验18个共同二次型空间、1152个能量和本原高度实例、19968个模素数幂条件、274个CRT例子、160个原位置降维、362个分块入口、31278个方向、24条核路径和48条原输入完整Fraction路径；最长239步仅为样本数值。另核对50086个约分公式，保留五平均 (u,v)=(3,11) 的整个数字族单步下降失败，不外推一般p的中间维数。相对尺度前页的商阶、安全性和跨维数目标已修正。

新增 prime-power-endpoint-completion（core/full）：[素数幂端点与临界几何](prime_power_endpoint_and_critical_geometry.md)证明q=2p+1为素数幂时的全部端点判据。两张局部射影图、全部Schreier回路、正向Gauss编译与两步合法入口共同承担一般量词；独立核验15612条转移、55512个模行、168条正向编译、32个大整数入口、2754个范数恒等式和2条n=27完整路径。文档还给出判别式-q虚二次阶的theta联系及2p+2共同尺度失效。该ID新增十三平均二十七元完整定理，不推广到多素因子端点或相邻维数。

新增 prime-power-endpoint-entry（core/full）：[临界前沿交接报告](prime_arity_critical_frontier_handoff.md)第6节完整证明素数幂q=2p+1的两步合法双块入口，并指出奇素数平均元数下的合数素数幂端点必为3幂。独立Fraction重放核对n=27的133种模3重数模式及全部单点选择，共3591项，另有56个大整数原位置实例和6个边界族控制。入口结论不承担合数level的核轨道、全部端点判据、临界以上区间传播或更低完整阈值；报告中的后续方向不是已证结论。

新增 uniform-collision-structure（core/full）：[任意p的碰撞结构](prime_arity_uniform_collision_structure.md)手写证明保护后3p+1层中p-2重余类的统一闭包，给出全碰撞D=3p或3p-1与分数族除数参数；另证明两个不交短零和组的同向修复、明确总余数窗口及足够多不同余数时的闭包。51618个高重数模式以独立候选方程核对分类，779个整数原位置步骤包含419个非空保护集合实例；4824个零和分解、105760个窗口公式和144个受限和集构造通过。全部一般结论由正文推导及明确引用的Dias da Silva--Hamidoune定理承担，有限计数不代替任意p量词；没有重跑旧五／七平均完整证书。未证明全体中等重数模式、3p统一阈值或精确2p+1端点。

新增 seven-average-three-p-plus-two（core/full）：[七平均N(7)<=23](seven_average_three_p_plus_two_threshold.md)以一般有效的余数对称平均压缩碰撞系统，57026个模7模式中仅11个相容唯一解，总和为整数且在0与未保护总维数之间。私人见证排除保护非空，类内部分选择迫使实际常值以排除无保护情形，解决23至26元；5628个大整数闭包和96条原位置路径（最长276步）独立核对一位额外精度。任意p与22元仍未完成。

新增 minimal-protection-and-exchange（core/full）：[一般保护交换](prime_arity_protected_exchange_and_mass.md)证明初始化可在3p+d-2完成，并给出p=23,n=70固定保护全碰撞、换保护即修复的非零合法例子及p=2 mod3的3p+1元五步整数族。核验3920个初始化、187组双候选族、6个保护交换和10条五步原位置路径；不增加一般完整维数或证明候选总和猜想。

新增 five-average-three-p-threshold（core/full）：[五平均N(5)<=15](five_average_three_p_threshold.md)以903个模5模式的完整有理线性系统和22个唯一解，证明碰撞总和的局部分母结论，再用最小保护横截集及私人见证排除合法失败，完整解决n=16、17、18；接独立15元与>=19得到统一界15。另核验2120个保护集合、5545个大整数闭包、120条逐原位置Fraction路径，最长201步，新三维数均一位额外精度。程序不导入探索系统生成器，正式分类允许每个位置有独立变量。任意p的3p界和五平均12、13、14仍开放。

新增 three-p-two-anchor-interface（core/full）：[3p双锚点接口](prime_arity_three_p_additive_interface.md)以Savchev--Chen标准定理证明3p+d容量下安全整数候选必存在，并对长序列零和自由分支给出一／两个低重数位置修复。核验231060个小余数实例、105个独立极值算法对照、8个修复实例，以及4246个实际状态的局部诊断；另检查模同余基族不满足基交换及低于3p预算的边界。候选存在但全部实际和碰撞仍未普遍解决，不证明3p阈值。外部定理明确引用；本轮未重新证明它，也未取得原论文全文。

新增 inverse-egz-threshold（core/full）：[4p-2+d完整阈值](prime_arity_inverse_egz_threshold.md)将原统一条件减少一个位置，得到N(5)<=19、N(7)<=27，保留一位额外精度。三重值两位置修复和共同预留跨越给出新结构；逆EGZ强迫两个p-1余数类，借锚点闭合保护池最后缺口。核验19059个完整余数模式、1650个大整数闭包、64个借锚点修复、12个跨越和36条原位置路径，另独立核验869个三重值实例。约7p/2路线仍是条件目标；可选有限诊断不进入正式证明量词。

新增 inverse-zero-sum-transfer（core/full）：[逆零和原位置转译](inverse_zero_sum_averaging_progress.md)通过线性部分和扫描生成有容量保证的加权见证，证明相反碰撞的两步恢复、不同余锚点下十四元(5,5,2,2)核的安全单步分类，以及任意奇数p>=5的2p+4元二参数七步归零族。核验3102个完整小余数多重集、1095个一般副本实例、3192个十四元实例、5个碰撞恢复及117条原位置Fraction归零路径。未证明整个十四元或2p+4元维数，也未改进N(p)通用上界；没有平均词搜索。

新增 prime-arity-zero-trigger-bridge（core/full）：[支持数传播与加权均值格](prime_arity_interpolation_and_lattice_structure.md)证明所有奇素数p、n>=2p+1中，真实p平均一旦造零即可完整收尾；不需端点完整猜想。另证明余维一整块等化障碍、块均值仿射格判据和本原重数的有限商，解释两个Gamma_0来源，并记录p幂维数传播。核验120条低段与108条高段全局Fraction路径、8个余维一边界、426个重数格实例及398个支持数覆盖。未证明先造零必然发生，也没有证明两端内插或新增完整中间维数。

新增 prime-arity-middle-band（core/full）：[三块运输与3p定理](prime_arity_middle_band_structure.md)用两张九项非负整数运输表统一实现U(+-1)，块重标记给L(3)，完整四陪集与模3入口解决所有奇素数p的n=3p；另证n>=3p+d时同余双重值闭包。核验40组实际运输、12条完整陪集边、7个旧反例族、7个G=p输入和56个其他输入的完整Fraction路径，最长105步；另核对996个闭包实例。未证明整个中间区间、3p级统一上界或一位额外精度。

新增 uniform-endpoint-controller（core/full）：[统一正向控制器](uniform_endpoint_positive_controller.md)不搜索平均词，以两种真实返回、仿射配对、必终止的整数链和欧拉迹零公式，证明所有奇数平均元数的U(R_q)、L(qR_q)及对角单位均有原位置正向实现。q=2p+1为素数时，完整Schreier、Bezout和两步入口证明全部输入可达 iff G=1。程序以共享无环表达式核验984组返回、25个平均元数种子、418个可逆倍率、528个完整回路及1656条边，并逐位置Fraction重放10条完整路径，最长2466步。q合数时的完整群／轨道与任意输入入口仍未证明；不声称N(p)=2p+1或统一精度、最短长度。

新增 five-average-n11-random-experiment（core/full）：[五平均十一元实验](five_average_n11_random_experiment.md)记录六档共120个独立随机原题，范围从正负20至正负2^128，只按G为5幂筛选，全部找到原位置证书；另有92个明确分开的K5核心压力例。默认核验重新生成抽样并独立Fraction重放全部212条保存路径，以及24个全位置后继和40个零坐标收尾。它只证明这些输入可达，不证明所有十一元、N(5)=11、统一精度或最短性。已有严格阈值仍为11<=N(5)<=25。

新增 pair-triple-solver-optimality（core/full，需要Node.js）：[二三平均求解器与最短性](pair_triple_solver_comparison_and_optimality.md)核对用户原HTML的16个内置测试、三平均精确IDA*和独立Fraction BFS，证明四组最短距离分别为3/1、3/4、1/1、3/2。151个零和打包数后继及100个数值三维匹配编码核验一般公式。正文从经典强NP完全的N3DM严格归约，证明即使G=1且保证可解，达到n/3步阈值仍强NP完全；这不否定可达性多项式判定或非最优多项式长度解。24例同题比较另存JSON，只是可行上界统计。

新增 double-triple-sequence-length（core/full）：[长度分析](triple_average_sequence_length_analysis.md)证明两两距离数值界、适用于任意非恒等整数三平均序列的最大间隙递归界，以及固定非三幂维数的对数步数下界。固定 n 的构造已具位长多项式上界，次数随 n 增长；可变 n 的统一多项式界仍开放。程序核对69,926个势能不等式、150个最大安全降幅与独立枚举的对照、142个最大间隙阶段、6个单步比例下降障碍及23,466个短输出行排除。另存18组配对与12组大整数实验；它们是有限性能数据，原策略的三个100000步截断不能视为不可达或最终长度。

最新 all-dimensions-double-triple-invariant（smoke/core/full）：[任意维数双三重值直接证明](triple_average_all_dimensions_double_triple_invariant.md)将新不变量推广到全部 n>=11，包括偶数和多素因子合数。多危险集至多留出 d 个位置，n>=d+10 保证容量；仿射见证处理模2，gcd(a-b,n)=1 替代素数性。全称结论由正文分类和整数能量证明。程序核对17,575个有界闭包、4,458个大坐标闭包、4,799个初始化、64个模2修复及80条完整精确路径；不运行词搜索。全部 n>=7 只另需7、8、10独立基例和9元网络，不再需要一般合数归约。n>=11的一位额外精度已证，位长多项式构造步数仍未证明。

新增 final-hecke-manin-audit（core/full）：[最后检验](triple_average_final_hecke_audit.md)核对44个整数幺模共轭、308组共同星结构方程、1884个合法cusp输送，以及普通模符号的中心负号、删点非Möbius与有限／球面Hecke区别。一般障碍由正文公式证明，无词搜索。仅排除指定的直接酉表示和线性Manin接口，不否定原猜想或所有自守路线。

修订 iwahori-hecke-modular-interface（core/full）：[修订接口页](triple_average_iwahori_hecke_modular_interface.md)保留有限Hecke二次／辫子关系、数字置换和、矩阵分解、能量、本征投影及根公式核验。原指数p格与全局Eisenstein／Steinberg、T_3解释不成立或未证明，已由最后检验明确纠正。旧PASS只核对这些代数恒等式，不承担全局接口。2084个返回矩阵的库存结果继续保留。

新增 nonsplit-hecke-chart-boundary（仅full）：17个非分裂素数至149的全部平移分层中，单层到任意B_p chart、两层到任意chart及三层回基准chart都只有恒等返回，没有非平凡参数3反射。程序用块系数和相同行分组识别全部角色，不展开p维有理矩阵。它不排除三层到其他chart、更长词、额外宏或奇异终端。

新增 atomic-hecke-wall-boundary（仅full）：对p=11至71的9个B_p系数状态，无遗漏遍历深度5以内的非恒等原子三平均计数状态，按(p-4,3,1)重数和Hecke迹方程筛选，没有非标准第二墙。每个稳定素数约83000状态，组合按重数签名缓存并按素数并行。它不排除更长词、子问题宏或直接终端。

新增 b71-symbolic-directed-terminal-cover（仅full）：一次符号系数--重数遍历同时处理B71(1,v)中-100至100的198个合法整数参数；至多6步准备后出现零和三元组，再平均一次可产生三个零。深度5在正负10000窗口覆盖1251/19720。稀疏性是有限线性终端方程的一般性质，不构成Manin结构证据；本项不覆盖任意有理斜率。

历史经验与有限实验汇总见[非分裂素数路线复盘](triple_average_route_reassessment_2026-09-11.md)，其后提出的Hecke主线以本页最上方的最后检验为准。该页中的B71计数、贪心、同步窗口等数字仍为有限探索证据。

新增 equal-carrier-formal-freezing（core/full）：[等载体形式冻结定理](triple_average_equal_carrier_formal_freezing.md)的16组整数平衡剪切、8个Q基SL接口和317844组素数gcd接口。一般证明给出SL--一次等载体交换--SL三段正规形，并证明每个合法素数形式轨道命中零叶块；有限域唯一避开轨道是q整除3r+2时的常值直线。两个SL块的现有构造使用形式逆，因此该条目不证明正向三平均实现，也不新增已解素数。

新增 carrier-sweep-catalyst（core/full）：[载体扫掠催化器](triple_average_carrier_sweep_catalyst.md)的一般秩整数扫掠公式、秩二有限中心、秩三24个幺幂与12个同长度逆、可逆根的完整sl3 Lie闭包、方向／协向量格指数5／32、四个固定对立根及E3(4320^2 Z)包含、第二载体余边界及15个模20碰撞轨道。另用NumPy批量核对模2/3/4/5像为1/5616/4/3000。一般扫掠与局部均值余边界由正文公式证明，整数有限指数由标准初等同余群定理承担；有理碰撞由下一条目补齐，仍未证明任意p终止。

新增 carrier-catalyst-local-descent（core/full）：同页的十位置有理碰撞定理。六根约化域精确分成30个一般锥与50个根步长为零的异常锥；2805个深度至多三的扫掠／根二次型经适用域零面递归和有理重心细分得到538与274个证书叶，最大深度15／7，未解0。每个二次型在锥上的最大值由顶点、边驻点和内部驻点精确判定；不是有限高度样本。该定理不提供重叠窗口的全局下降。

新增 carrier-collision-global-interface（core/full）：局部碰撞在一／两次额外平均后进入两个等载体，两种情形均有显式反解，故完整Z[1/3]仿射差分模保持。根与正向逆的局部中心收缩给出重叠差(3^(8k)-1)/3^(8k)，程序核对k=1..12；一般指数族由闭式证明。它排除直接拼接局部本原Q作为全局高度，不排除同步窗口或冻结零和块。

新增 mixed-singleton-conditional-controller（smoke/core/full）：[混合单点条件控制器](triple_average_mixed_singleton_controller.md)的50个迹零周期与仿射交换子、18个平方自由素数支撑根接口、1674个有符号Schreier参数、36组共同严格正三进运输边际及431对角影子边界。一般条件定理由正文恒等式、素因子支撑和对角吸收证明；程序不证明两个目标运输能在原p位置分解。

新增 reynolds-hodge-structure（core/full）：[内在代数结构](triple_average_reynolds_hecke_hodge.md)的209个Reynolds／凸平均、110个根恢复与190个秩一乘积、27个Hodge恒等式、1238个合法到非法像、27个局部Iwahori共轭和1716个判别式赋值控制。一般生成代数与Hodge边界来自正文闭式证明，不宣称该对偶正向可实现。

新增 contingency-layer-semigroup（core/full）：同页的60个运输表层实际系数重放共336次原子平均，54个载体字母，25个终端超平面和205个交数秩。每个运输表都普遍合法，但紧凑层半群的终端覆盖仍是猜想；无损编码全部原子词的是较大的单三重块模型。

新增 n47-complete（smoke/core/full）：[47元完整判据](triple_average_forty_seven_arithmetic_complete.md)。重验170节点逆证书，核对固定尖点词、两个伸缩、18个完整Schreier回路的正向根分解、48陪集与独立标签、1434个输送、六步原子终端、928个桥及8项目录集成。47已加入因子闭包，最小未解53。正式核验不运行目标发现搜索。

新增 localized-iwahori-generation（core/full）：[一般局部化生成](triple_average_localized_iwahori_generation.md)的2238个标准Schreier公式和单位消元、8个一般伸缩校正、32个奇次三进返回到尖点恒等式，以及73处固定单位像边界。一般p量词由正文的统一代表与公式证明；正向资源普遍存在仍是假设。

新增 b47-root-activation（core/full）：[正向根群饱和](triple_average_positive_root_saturation.md)与固定170节点JSON，独立重放全部模板及无环依赖，三层46/113/2覆盖旧167宏；57次模板的共轭正向词及两个完整根群的矩阵恒等式均核验。正式入口不导入发现程序。尚未证明有限指数、合法单轨道或47元完整判据；一般迹根引理、全参数根族及统一素数条件定理见正文。

新增 b47-extra-atom-involutions（core/full）：[固定新宏](triple_average_b47_extra_atom_and_adjoint.md)独立重放三个extra-stage模板、九个可逆生成元及三个周期；U(+-47)词验证正向替换，32个三进与6个二进共轭给出47Z[1/6]根群，18个参数对合族恒等式给出分裂环面边界。不是47元完整判据。

新增 adjoint-return-domain-audit（core/full）：重建旧167模板的物理子集和末尾置换，全部核对Gram伴随公式，逐步检查反向域；15个普遍合法，均在旧库。共享Fraction重放器现在支持可选extra阶段，旧宏的默认路径和矩阵数量不变。

新增 projective-spectral-balance（core/full）：[一般谱判据](triple_average_projective_spectral_balance.md)的85个共轭／缩放周期例子、4个独立条件边界、10个Ad分圆算法输入及B47实二次范数宏接口。一般充要条件和复杂度由正文证明；不把给定宏的周期判定误称为原平均可达判定。

同一条目后续增加125个可交换Q(sqrt89)关系对照：相对素理想赋值和实单位指数同时为零才构成周期。一般可交换库的全正关系格判据见第8节，程序不实现通用S单位求解。

新增 b47-short-cycle-boundary（仅full）：[固定B47库的排除](triple_average_b47_cycle_frontier.md)，167模板、4657463三因子词、27160个全指数方程和737665600个四因子组合。后者是NumPy int64精确模筛选，3896个候选再做任意精度整数判断，包含溢出界与行列式模零控制。历史浮点工具仅用于发现，不承担排除证明。

新增 paired-carrier-two-adic-reset（core/full）：[等值载体二进宏](triple_average_paired_carrier_reset.md)的六秩矩阵／格／迹检查、132个完整系数基实际操作、120个双理想保持实例、9个入口／奇偶边界、54个虚拟质量反例及5160个输出置换的迹整性排除。一般4r-3步构造与det公式由两遍广播证明；单宏有限阶阴性结论仅限明列秩，词长赋值下界为一般结论。

新增 n41-complete（smoke/core/full）：[41元完整证明](triple_average_forty_one_arithmetic_complete.md)固定21模板、10个三因子对合、10个整数词，独立核验42陪集、唯一合法尖点、1422个输送和928个桥，另有7项目录集成。子程序仅3/9/18/27/37/38/39。正式核验不运行发现搜索，最小未解维数为47。

新增 modular-primitive-height-barrier（core/full）：[有限模与高度边界](triple_average_modular_height_barrier.md)在12个模恒等终点间实际重放2304个平均，核对实能量严格下降而本原高度按精确公式增长。任意h的结论来自闭式证明，不是12例外推；它不否定可以选择其他下降词。

新增 two-carrier-modular-bridge（core/full）：[全部n=5 mod6的二例外桥](triple_average_two_carrier_modular_bridge.md)。165个混合好划分、9个不除以r的有限环拼接、34个整提升、模5下15624点正向轨道、20个有限模逆指数、5条共567个原子操作、480个子问题／输出接口，以及320个核内调用边界。一般量词由正文的主同余包含、CRT与有限群正向化证明；不把480个同余目标模式当成480条完整调度。该条目不证明二例外核终止。

同一条目还核对460个对角二次型、G公式和一步安全B核桥；因此该n族的标准核进入已证明。一般profinite正向启用原则由有限群中逆为正幂的正文论证给出，不是用模5样本外推。

此前 n29-complete（smoke/core/full）：[29元完整证明](triple_average_twenty_nine_arithmetic_complete.md)固定18模板、9个三因子周期、7个整数词、30陪集及独立模29标签、1398个输送与928个桥，另有8项目录集成。仅调用3/9/25/27，最终使用冻结库1194模板；不运行浮点发现搜索。41元已另有后续证书。

新增 nonsplit-projective-layer-boundary（core/full），在5/11/17/23/29的原位置数上重放非分裂射影轨道层，核对奇异位移、不交换和全位移乘积非标量。该有限边界不否定其他非分裂控制器。

编译器的 `--expanded-first` 开启所有已证首步大小，默认首步库保持3/9及可选的特殊6不变。29元扩展库1242与旧当前库1195均可复现；正式29元证书进一步使用冻结子问题库1194。发现工具 `search_bn_three_cycle.py` 的浮点迹筛选只产生候选，精确证书另行固定。

新增 split-prime-gaussian-controller（smoke/core/full）：[全部p=1 mod3素数定理](triple_average_split_prime_gaussian_controller.md)。4项抽象Eisenstein格恒等式，496个固定真实位置上的范数周期原子操作，10个素数的单位／根／仿射接口，800个单位剪切原子重放，320个仿射正规形与gcd消去输入，以及14项目录集成。一般剪切本原性由正文对每个素数的反证承担；没有用有限素数样本外推。剩余统一问题为p=2 mod3，29仍开放。

新增 flat-star-formal-arithmeticity（core/full）：[平坦核形式算术性](triple_average_flat_star_arithmeticity.md)的12组幺幂／行剪切、18组64N与192根群接口、18组双载体拼接及79个第一层终端代表。一般有限指数证明明确使用Tits／Bass--Milnor--Serre初等同余群定理，第一层局部乘积使用Goursat引理；脚本不将形式逆认作正向平均。

新增 cyclotomic-level-entanglement（core/full）：[置换level与两处耦合](triple_average_permutation_shadow_entanglement.md)的20组方差／置换式、240条尺度归一化词、旧容器严格反例及43008状态Schreier二重覆盖。新容器有192尖点、48合法尖点、属3473。旧n91-congruence-container继续复现21504容器，二者不能混用；旧24个合法尖点的终端计算不自动覆盖新48类。

新增 balanced-digit-congruence-group（smoke/core/full）：[完整数字同余群](triple_average_digit_congruence_group.md)的380个列稳定子公式、160个独立主同余输入、118个数字倍率／周期和492个射影轨道迭代。群等式、有限指数、分裂扩张与轨道分类的无限量词由正文的列消元及整数初等生成证明承担。它不证明原维数宏库的算术性。

新增 b29-current-cycle-boundary（core/full）：[29元当前库边界](triple_average_structural_picture_audit.md)核验1195模板的714610个二因子乘积，并用精确二次迹方程排除全部j>=0的A^jB周期。7个控制包含指数57和100的人工标量周期。边界只针对该固定模板库与词形，不是29元不可达结论。

最新新增 one-tripling-stabilization（smoke/core/full），对应[一次三份复制定理](triple_average_one_tripling_stabilization.md)和[结构图景审计](triple_average_structural_picture_audit.md)。核验64个数字算子、312个完整系数基原子操作、1589个零和正规形、475个一般仿射轨道、790个完整归零操作，以及108个划分／控制器接口（最大N=1827，包含87元）。一般Hilbert90、平衡欧几里得与所有三整除维数结论由正文证明。原维数复制消去、29元及统一素数定理仍开放。

同一条目后续补充：237组一般q区间恒等式、386个q平均系数重放；n=29的副本宏有1624个三平均的完整系数重放；原维数平坦载体的35对六项Artin关系、18个原子交换及局部中心不交换边界。q平均重放不计作三平均原子操作。

最新新增 even-prime-power-halving 和 all-dimensions-prime-reduction（core/full），对应[总归约定理](triple_average_all_dimensions_to_primes.md)：1536个完整二进模式、8448个核心桥，14项容量证书、33329个有限因子计划、699个70/110/130接口。一般公式与强归纳在正文承担无限量词。全部n>=7现严格归约到素数p>=7；所有23光滑维数已解，最小未解29。

整系数编译器的默认子问题库已固定为旧证书使用的版本，避免新增定理改变历史矩阵数量；新探索可用 `--current-library` 启用任意N>=9的三整除维数，以及素因子属于2、5、11、17、23、29、41或任意p=1 mod3的因子闭包。独立证明仍须核对每个实际调用域，不能仅凭当前目录自动接受模板。

最新新增 n25-complete（smoke/core/full）：18个只使用3/9/21元调用的通用模板、正向逆关系、七个整数词、30陪集与独立模25射影标签、唯一合法cusp、858个输送及446个核心桥。[25元完整判据](triple_average_twenty_five_arithmetic_complete.md)补齐了奇数因子归约的独立小基例。

odd-composite-factor-closure（core/full）对应[奇数合数闭包与35元证明](triple_average_odd_composite_factor_closure.md)：5项奇数边界、4404个因子计划、943个多例外接口、2210个35元核心。一般容量与强归纳在正文给出。结合n25-complete，它完成已解奇素数的任意乘积和素数幂，可另乘任意五幂及三幂；91元因此也已完整解决，不依赖旧同余容器等式。

同一入口再核验2项二幂边界和1654个8整除因子计划，对应完整的8整除乘法族，允许任意五幂。条目名保留发现先后顺序；其精确范围以最新manifest与证明第11节为准。

重新复核其他AI的文件后，新增 other-ai-local-global-synthesis（core/full）、ai3-template-report-audit 和 ai5-synchronized-replica-audit（full）。[综合页](triple_average_other_ai_local_global_review.md)列出全GL Zariski闭包的一般Lie证明、完整仿射理想、非零均值链接口及复制商的秩障碍。程序核对相应公式和原报告的有限结果；不据此宣称算术有限指数或一般复制消去。AI-4轨道表仅用三个生成元重算，未重跑深度8整矩阵库。

最新新增 prime-factor-carry-bridge（core/full），对应[素数优先与因子归约](triple_average_prime_first_factor_reduction.md)：核验133组特殊族参数、1062个一般二例外核心、X49两步最短修复、复制加法闭包和176条准备词的3424个两列行签名。一般桥与最优性由符号证明给出；不能把它解读为任意输入的因子分解或完整49元定理。

modern frame 已[重写](triple_average_unified_modern_framework.md)，完整原稿保留在 history/；使用边界见[严格化说明](triple_average_modern_framework_review_and_contract.md)。不把“统一框架”登记为已解决一般问题的计算证书。

最新新增 n23-complete（smoke/core/full）：15、17、24步固定原子宏、含2因子的真实标量逆词、七个整数生成元、24陪集与独立标签、属2及唯一合法cusp、1390个输送和928个桥实例。见[二十三元证明](triple_average_twenty_three_arithmetic_complete.md)。三个关键宏已全部原子化，不调用十九元求解器。

同轮 n19-complete（smoke/core/full）核验七个通用十五元调用模板、显式仿射格恒等式、正向逆词、六个整数词、20陪集与独立模19标签、1374个输送和928个桥实例。见[十九元证明](triple_average_nineteen_arithmetic_complete.md)。该定理依赖已证十五元判据；不把每次调用计为一个原子操作。

同时登记 bn-integer-template-compiler 和 prime-congruence-structure（core/full）：前者对照95个十七元矩阵并独立重放222个十九元、60个二十三元模板；后者核验素数稳定子、实际尺度周期及共同第一行的仿射恒等式。一般稳定子与周期结论来自[证明正文](triple_average_prime_congruence_structure.md)，不由六个素数的样本外推。

此前 n17-complete（smoke/core/full）核验固定原子宏、正向逆元、18陪集、1366个输送和928个桥，见[十七元证明](triple_average_seventeen_arithmetic_complete.md)。最小未解维数现为29。

另登记 b17-old-integral-return-audit（full）保留旧24词调度的净高度检查：一支处处增高，23支二次型不定。新完整证明不依赖这个旧控制器下降。下面的旧B17条目继续按其原库范围复现，不能将“旧库仍开放”误读成“十七元仍开放”。

最新新增 b17-universal-subproblem-lattice（core/full）：核对任意参数模判据的实现、五个新通用宏、1008个完整接口、684个合法输入的至多三步调度，以及范数3和 theta 分支恒等式。详见[参数无关调用与范数环面](triple_average_universal_subproblem_lattice.md)。这是全部 B17 上的“可开启十五元调用”定理，不是全部 B17 终止定理。

同一入口还逐条重放630个固定原子词实例（各宏17／19步）、证明旧五宏加A的模3逆词障碍、重算48类完整调度和独立24词表，并核对最后十四元调用为整数严格下降。该下降只比较预备词之后的当前高度，不能解读为整个组合已经净下降。

同时补齐 b17-guarded-library-trap、b17-cross-stratum-escape、finite-orbit-method-boundary 三项（core/full）。前两项保留旧库无限陷阱、受限跨核桥和一个下降例子的独立证据；后一项核对大有限模像不推出有限指数。每个条目在清单中有明确证明边界。

b17-guarded-subproblem-experiment（full）记录首个框架应用：10个条件模板、136次局部接口重放、有界下降仍剩141个方向；不是十七元完整判据。subproblem-prime-obstruction（core/full）则有独立一般证明，排除缺失障碍素数时的统一有界调用次数。

新增 all-even-B-kernel-halving（core/full），核对 n=2 mod4 的8212个接口和4整除的5088个接口。对应[结构核减半定理](triple_average_all_even_B_kernel_halving.md)，不能解读为任意偶维判据。二三光滑完整判据还使用单危险素数高维归约及归纳基。

新增 subproblem-prime-obstruction（core/full）：检查子块大小与 p 互素时，符号 B 核经归并词仍保留模p非零常值方向。一般任意长度的下界由[缺失素数定理](triple_average_subproblem_prime_obstruction.md)给出；720步有限核验不作为无限外推。

最新增加 `two-three-smooth-complete`（core/full）：核验八元、十二元、十八元依赖，再检查统一减半的5524个加权接口。全部2^a3^b维数的无限归纳在[证明正文](triple_average_two_three_smooth_complete.md)，不是最大测试维数27648的外推。

2026-09-10 新增 `blocker-graph-safe-core` 与 `n14-complete`（core/full）：一般 n-d-2 核心有独立图论证明，十四元余数桥则独立重放全部512类及两个具体例子，共514个十二元／B14接口。完整命令同时核验七、八、十二元依赖，详见[十四元证明](triple_average_fourteen_complete.md)。三个代理的独立方向见[团队交接](triple_average_team_handoff_2026-09-10.md)，未完成的报告不自动算作已验证定理。

最新新增 `n12-complete`，列入 smoke/core/full：四个真实宏、正向逆元、五个整数生成元、完整 12 陪集、独立模 8 标签、唯一合法尖点和六步终端。[十二元证明](triple_average_twelve_arithmetic_complete.md) 的一般高维归约在正文中单独证明。另登记 `b12-six-step-local-branches` 和 `b12-return-frontier-certificates`；后者只重放发现缓存及核对浅层完整性，不替代完整定理。

进一步新增 n18-via-twelve-complete：调用已证十二元子问题，把 B18 及 \(2\cdot3^k\) 核压到偶重数状态，再用两份三幂网络归零。平均数分母、子问题合法性与配对后的零和性均在[一般证明](triple_average_eighteen_via_twelve_complete.md)中明确列出。B21 默认改用[本原整数引擎](triple_average_b21_integer_search_optimization.md)，结果和旧引擎对照一致。

最新加入 n15-via-subblocks-complete（core/full）与 even-kernel-halving（full）：前者重跑十二元、十元证书，再核验模8循环和2578个子问题接口；后者检查8212个偶维 B 核的八元减半接口。通用结论以[十五元证明](triple_average_fifteen_via_subblocks_complete.md)和[偶维核减半桥](triple_average_even_kernel_halving_bridge.md)中的符号论证为准。

## 1. 当前可复核性判断

在本指南建立之前，项目的数学总览已经较清楚，但验证工程不足以让陌生 AI 可靠接手：`work/` 中 124 个文件平铺混放，没有根目录入口、机器可读映射或统一命令；部分结论文档只列脚本名而未说明证据边界；`verify_*` 同时包含精确有限证书、随机样本和有限深度搜索。

现在新增了三层入口：

1. 根目录 `README.md` 给出阅读顺序；
2. `work/verification_manifest.json` 逐项记录结论、状态、文档、脚本、结构化命令、输出标记、证据范围和运行档位；
3. `work/run_verifications.py` 校验清单并统一运行。

现有历史文件没有移动。新核验者可以快速上手，但仍必须阅读每项的 `does_not_establish`，不能把程序 PASS 自动升级为整篇定理的形式化证明。

## 2. 快速复核

所有命令从项目根目录执行，当前脚本只依赖 Python 标准库和本地模块：

```text
python work/run_verifications.py --list
python work/run_verifications.py --profile smoke
python work/run_verifications.py --profile core
```

`smoke` 通常少于 10 秒，覆盖十三元、稳定化、Burau 幂链和修正后的九十一元同余容器。`core` 通常约 1 至 2 分钟，加入七、八、十、十一元的完整有限证书、一般提升、三幂分块和零填充。

完整档运行：

```text
python work/run_verifications.py --profile full
```

其中九十一元深度 4 搜索在本机实测约 14 秒；`full` 还包含约 273 秒的定向 cusp 29 深度 5 搜索，完整运行时间通常约 6 分钟。按 ID 单独运行示例：

外部“减少暴力搜索”建议的逐项判断，以及九十一元开放尖点的新并行入口，见 [搜索优化建议复核](triple_average_search_optimization_review_2026-09-09.md)。

```text
python work/run_verifications.py --id n11-complete
python work/run_verifications.py --id n91-cusp-depth4
python work/run_verifications.py --id n91-cusp29-depth5
```

## 3. 证据等级

| 等级 | 可以据此声称 | 不能据此声称 |
|---|---|---|
| `theorem-certificate` | 一个已明确归约为有限问题的证书被精确复算 | 证明文档中的一般归约也已被形式化 |
| `symbolic-check` | 所列精确恒等式、宏和参数实例成立 | 有限参数自动推广到任意参数 |
| `finite-sanity` | 当前实现通过有限穷举或固定种子样本 | 带无限量词的定理由实验得到证明 |
| `exploratory-search` | 在给定界内找到或未找到见证 | `OPEN` 类不可达，或搜索已经完备 |

统一运行器中的 PASS 表示“退出码为零且全部预期标记出现”。对开放搜索，PASS 只表示预期的开放结果被重现。

## 4. 已完成基维数

最新完成的是 n19-complete 与 n23-complete，分别核验通用十五元调用和固定原子词，并闭合20／24陪集及一般进入桥。此前 n17-complete 已闭合18陪集。下表保留更早基维数的导航。

| ID | 数学结论与文档 | 核验内容 | 直接运行的关键输出 |
|---|---|---|---|
| `n7-n8-complete` | [七元与八元完整判据](triple_average_seven_eight_complete.md) | 七元精确射影实根覆盖；八元真实宏、欧几里得下降和终端路径 | `exact certificate: PASS`；`B8 Euclidean macro certificate: PASS` |
| `n10-complete` | [十元完整判据](triple_average_ten_complete.md) | 模 10 配对、四步桥、真实返回词和精确局部实覆盖 | `ten-point complete theorem certificate: PASS`；`terminal local-real cover: PASS` |
| `n11-complete` | [十一元完整判据](triple_average_eleven_complete.md) | 安全组合、五步桥、返回词、221,184 个局部类和射影覆盖 | `eleven-point safety and bridge certificate: PASS`；`B11 exact projective-core certificate: PASS` |
| `n13-complete` | [十三元算术群证明](triple_average_thirteen_arithmetic_complete.md) | 真实宏、正向逆元、56 陪集、尖点、终端和 $G$ 公式 | `finite modular folding: 56 complete cosets PASS`；`both legal cusps ... PASS` |

这些项目属于 `theorem-certificate`。它们精确闭合各证明中的有限枚举或宏证书；从任意合法输入下降到有限证书所覆盖情形的论证仍在对应文档中。

## 5. 一般维数结构

| ID | 文档 | 程序实际核对 | 明确边界 |
|---|---|---|---|
| `stabilization-theorem` | [复制稳定化定理](triple_average_stabilization_theorem.md)、[勘误](triple_average_research_corrections.md) | 2,288 个精确构造样本、显式运输矩阵、下界排除和反例修正 | 一般定理由文档中的构造证明；程序不证明原维数中的复制消去 |
| `power-partition-compression` | [三幂分块压缩](triple_average_power_partition_reduction.md) | 3,542,820 个危险边模式和 2,310 个完整网络样本 | 不证明压缩后对数秩核都可达 |
| `general-lifting` | [一般维数综合](triple_average_general_n_synthesis.md) | 有界公式、提升、同步划分和十元显式路径 | 有限样本不能推出任意 $n$ |
| `zero-padding` | [零填充定理](triple_average_zero_padding_theorem.md) | $3\le n<100$ 的 9,700 个精确网络样本 | 一般递归证明在文档中 |
| `burau-power-chain` | [Burau 幂链定理](triple_average_burau_power_chain.md) | $3\le t\le8$、$s=3,9$ 的十二组精确关系和正向逆元 | 任意秩证明在文档中；链间耦合仍开放 |
| `power-block-macro` | [三幂块返回宏](triple_average_power_block_macro.md) | $1\le k\le5$ 的真实平均重放 | 任意 $k$ 依靠归纳证明 |
| `cyclotomic-macros` | [十三元证明](triple_average_thirteen_arithmetic_complete.md)、[Burau 幂链](triple_average_burau_power_chain.md) | $s=3,9,27$ 的真实宏和矩阵恒等式 | 不证明真实宏群等于一般算术候选群 |

`isolated-prime-core`、`multi-prime-core` 和 `arithmetic-geometry-structure` 也登记在清单中，但属于支持性有限实验。它们适合检查公式或寻找反例，不能单独引用为任意维数定理。

## 6. 九十一元必须分成三层

九十一元最容易发生证据越界，必须区分：

1. `n91-congruence-container`：`cyclotomic_congruence.py` 精确得到含模 8 条件的已知容器。输出为 21,504 个标签、96 个尖点和 24 个合法尖点。它不证明真实宏群等于该容器。
2. `n91-corrected-witness`：`search_n91_missing_class.py` 验证 $(u,v)=(1,-3)$ 时单独坐标为 $-54$，并给出两步到 27 元零和块的真实证书。它只处理一个代表。
3. `n91-cusp-depth4`：`analyze_n91_terminal_cusps.py --depth 4` 在容器的 24 个合法尖点中覆盖 23 个。深度 3 时开放的尖点 30、32、35 已找到四步证书，只剩尖点 29 为 `OPEN`。这个标记表示深度 4 内未找到证书，并不表示不可达。
4. `n91-cusp29-depth5`：对 `cusp 29 = (-13,18)` 使用 `--cusp 29 --depth 5 --jobs 8 --split-depth 2`，得到五步终端证书；已知容器的有限深度覆盖因此达到 `24/24`。它仍是探索性有限搜索。

脚本默认 `--depth 2`，输出 `covered legal cusps 14 / 24`；深度 3 输出 `20 / 24`；深度 4 输出 `23 / 24`；单独的 cusp 29 深度 5 输出 `covered requested cusps 1 / 1`。整数子集和 DP 与八进程优化后，深度 3 从 540.794 秒降至 6.322 秒，深度 4 从 117.891 秒降至当前约 14.2 秒；新的存在性优先 DP 下，cusp 29 深度 4 约 6.2 秒、深度 5 约 272.8 秒。详见 [计算性能审计](triple_average_computation_performance_audit.md)。

旧九十一元群路线仍有两项独立缺口：特定正向宏群是否等于同余容器，以及任意输入如何进入其(81,9,1)核。覆盖容器24个尖点本身仍不能省略它们。但整体91元可达判据现已由 odd-composite-factor-closure 的7*13真实因子归约另行完成，不能再将旧群路线的开放状态写成91元未解。

## 7. 历史与探索程序

`verify_five_theorem.py` 虽含 `verify` 和 `theorem` 字样，实际只是小状态的有限深度 BFS，已登记为 `n5-bounded-search` / `exploratory-search`。`verify_cascade_bound.py` 是确定性有界样本，登记为 `finite-sanity`。

下表列出历史支持文件。manifest 的 `referenced_support_files` 当前为 17 项，包含已有独立核验入口的 B12 探索器和已被十五元定理替代的手写候选矩阵实验；实际条目数以 `--list` 输出为准。统一入口会检查所有引用路径。

| 程序 | 当前角色 | 应如何引用 |
|---|---|---|
| `check_five_core_operations.py` | 五支持操作的辅助有限检查 | 仅作为见证重置方向的候选数据 |
| `check_n13_macro_cover.py` | 已被替代的十三元实收缩检查 | 当前十三元结论引用 `n13-complete` |
| `classify_ten_safe_core.py` | 十元模 30 安全核心的独立枚举 | 可作补充交叉检查；稳定入口是 `n10-complete` |
| `construct_five_exception_core.py` | 五支持覆盖设计构造 | 说明覆盖障碍，不证明可达或不可达 |
| `cyclotomic_schreier.py` | 已降级的模 $91\times2$ 粗商 | 修正模型引用 `n91-congruence-container` |
| `explore_reverse_cascades.py` | 有界反向级联实验 | 只支持有限代价范围内的观察 |
| `explore_ten_descent.py` | 十元发现程序兼证书依赖模块 | 定理入口仍是 `n10-complete` |
| `explore_thirteen_group.py` | 十三元精确矩阵辅助模块 | 由 `n13-complete` 间接调用，无独立结论 |
| `explore_thirteen_modular.py` | 十三元精确模群辅助模块 | 由 `n13-complete` 间接调用，无独立结论 |
| `explore_weighted_kernel_group.py` | 加权核精确计算兼 Burau 依赖 | 旧浮点行列式输出已撤回；当前结构引用 `burau-power-chain` |
| `height_truncated_reverse_tree.py` | 高度截断完整枚举 | 完备性只在显式高度界内成立 |
| `n13_matrix_height.py` | 早期十三元参数格诊断 | 用来说明分母尺度问题，不承担完成证明 |
| `research_precision_boundary.py` | 六至八元历史综合实验 | 七、八元当前证书引用 `n7-n8-complete` |
| `search_ten_four_parameter_macros.py` | 十元候选宏发现搜索 | 当前证明只引用筛选后的正式宏证书 |
| `weighted_local_tangent.py` | 四十元局部像精确诊断 | 不构成一般 Burau 或可达性证明 |
| `explore_b12_kernel.py` | B12 有限搜索，默认含 G=1 和 G=3 | 独立入口 `b12-complete-bounded-domain`；历史 44 类加 `--g1-only` |
| `explore_b15_twelve_returns.py` | 未作为证书的手写条件宏候选 | 由 `n15-via-subblocks-complete` 的独立一般归约替代 |

其他未被数学文档明确引用的 `search_*`、`explore_*`、`analyze_*` 默认作为研究草稿；只有在 manifest 中登记命令、预期输出和证据边界后，才能作为可复现的当前结论引用。

## 新接口与控制器实验

search-contracts 现另核对48个新旧 BFS 最短路径和1525条后继边，保证整数化状态商及实际数值恢复与 Fraction 引擎一致。

新增均值碰撞剪枝回归。旧符号宏表的深层完备性声明已撤回，仍逐条重放其正向证书；完整十二元与十八元定理不依赖发现表的穷尽性，见研究勘误第13节。

| 核验 ID | 范围 | 证据边界 |
|---|---|---|
| `standard-kernel-interface` | 229 个压缩证书和 9 个无效证书案例 | 具体证书接口，不是全部核可达定理 |
| `search-contracts` | 720 个独立子集对照及两种断言禁用拒绝测试 | 实现正确性回归 |
| `bn-arithmetic-structure` | B12 三宏、一般扩张修复族、二元型和 theta 格对应 | 一般证明在数学文档，theta 模性来自标准定理 |
| `b12-complete-bounded-domain` | 高度 8、深度 4 的完整 62 类 | 有限实验，不是 n=12 定理 |
| `bn-comparison-depth4` | 四维数统一深度四比较 | 62/62、71/73、62/62、66/79 |
| `b15-two-depth5` | B15 两个深度四缺口 | 两条五步证书 |
| `b21-depth5` | B21 高度 8 的 79 类 | 已知可解维数的控制器实验 |
| `bn-symbolic-returns-depth5` | 规范化符号状态的短返回搜索 | 包括奇异矩阵；不证明宏群大小 |

运行器现在拒绝 `-O` 和导致断言禁用的 `PYTHONOPTIMIZE`，子环境也清除此变量。直接绕过统一入口以优化模式运行老脚本，不是有效证书核验。

各新命令可用 `python work/run_verifications.py --id ID` 独立运行；`full` 还包含 B21 的较长有限搜索，总时间随并行负载变化，旧的约 6 分钟仅是加入这些条目前的估计。详见 [audit 修订记录](triple_average_audit_resolution_2026-09-09.md) 和 [四核比较](triple_average_single_prime_kernel_comparison.md)。

## 8. 本次审计发现并修正的复现问题

1. 九十一元覆盖数现在与搜索深度绑定：默认深度 2 为 `14/24`，深度 3 为 `20/24`，深度 4 为 `23/24`；单独搜索 cusp 29 的深度 5 已得到最后一条证书，清单同时保留深度 4 全量命令和深度 5 定向命令。
2. [三幂分块压缩](triple_average_power_partition_reduction.md) 曾记录 1,055,056 个危险边模式，而当前脚本实际稳定输出 3,542,820；文档已按当前程序修正。
3. 总纲原来只列关键脚本名，未说明一项证明可能依赖多个程序，也未区分精确证书、有限实验和开放搜索；现在以机器清单为唯一运行索引。

后续每次修改验证程序时，应让预期输出变化导致统一运行器失败，并同步更新清单与对应数学文档。这样“脚本变了但旧数字仍留在论文中”的偏差会在复核时直接暴露。
