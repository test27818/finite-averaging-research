# 工作材料、历次快照及旧目录完整附卷 · 第21分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [三平均研究的计算核验指南](#doc-a3f6cc35dedf)
- [危险素数的见证重置：局部约分为何必须纳入一般算法](#doc-8f054d573887)
- [可填充三幂块的统一收尾](#doc-c2db819c6d1f)
- [统一四／六阶控制器完成2、3奇次幂临界点](#doc-15662833ecca)
- [临界双块系统的统一正向控制器：不再搜索种子周期](#doc-aa89bc3963b9)
- [`work/` 使用说明](#doc-ec386797a9bf)
- [Arena三平均网页审阅](#doc-dec765f2fc85)

---

<a id="doc-a3f6cc35dedf"></a>

## 原文导签：三平均研究的计算核验指南

来源：`work/document_reorganization_20260915/originals/outputs/triple_average_verification_guide.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_verification_guide.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-a3f6cc35dedf -->
# 三平均研究的计算核验指南

新增 two-prime-neighbour-complete（core/full）：[统一文稿第11节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)以直接整数选择和严格下降完成所有奇p>=5、omega(p+1)<=2的n=2p+2全输入判据，含五平均12元。43个元数的62870个选择步骤、18条核心全路径、24条原输入全路径均到全零；四种选择分支全部核验，原位置逐原子检查本原G。p29的控制例只排除所列一轮下降规则，不是不可达证明。此项不调用算术群或搜索平均词。

新增 even-core-dyadic-depth（core/full）：[统一文稿第10节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)给全部p>=5、全部偶数2<=r<p的核内二进深度下降。59组闭式计数、472条原位置路径和1180个严格下降阶段通过，逐原子使用本原G核验，包括r=2、p-1。它不证明深度一内终端覆盖，也不使用七平均特殊周期或算术群外部定理。

新增 seven-average-sharp-completion（core/full）：[七平均最优阈值](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_sharp_threshold_complete.md)补齐20、22元并接旧结果得N(7)=15。38个原位置双基循环/逆/根词、648个完整模9元素、20元1600个方向、22元3872个方向—单位尺度状态、5472个精确主同余目标矩阵、96条大整数入口及两个真实尾部通过。22元单位像不满，必须保留指数2尺度类；不是只检查射影方向。无限包含仍依赖Morris/Serre及深同余引理，不声称已提取任意主同余矩阵的完整平均词。

新增 uniform-two-block-entry（core/full）：[统一整数格与两轮入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)证明下半带r>=omega(n)的全输入入口，删除周期密度及gcd限制。482条原位置入口中100、94、30条分别不满足旧密度、旧gcd及两者；统一两带返回重放5520次，384组格/能量/终端公式、26组块数素数处终端代表，以及有限尺度和模2一阶误用对照通过。一般入口与有限轨道纤维定理由正文证明；不将一般偶数核心或全区间登记为已解。

新增 upper-band-coprime-six-complete（core/full）：[上半带完整族](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_coprime_six_complete.md)证明p>=13、3p+10<=n<=4p-3、gcd(n,6)=1的全输入G=1判据。核验24168个二三单位下降、274组参数、3465个主同余层式、230个原位置对合、822条精确终端矩阵、23条全输入入口、4组特殊逆及2组Smith一般逆、4条真实尾部。普遍量词由正文证明及明确的Morris/Serre依赖承担，没有由有限样本外推，也没有提取任意主同余矩阵的完整平均词。最终阈值未降低。

新增 upper-band-four-return-congruence（core/full）：[上半带四返回](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_four_return_congruence.md)核对2188组显式交换子和倍率环公式、2172组统一内部区间容量、344个双基原位置往返，并确认3p+1处的菜单容量缺失。由既有深同余引理得到任意p>=13、3p+10<=n<=4p-3的主同余控制；没有证明全终端覆盖、新完整维数或更低阈值。

新增 even-middle-eighteen-congruence（core/full）：[偶数同余与七平均十八元](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_middle_congruence_and_eighteen.md)核对62组通用根公式、84个原位置对合和100条新入口。模5184的1728个单位及全部5184个合法方向、15552条边、两个各2592点的终端轨道构成完整有限证书；每个方向另构造精确主同余目标矩阵。一般深同余包含依赖Morris、Serre及正文的任意有限商消元；不从小模样本外推无限群。新增七平均18元全输入结论，未降低N(7)<=23或完成一般偶数维数。

新增 uniform-odd-middle-cores（core/full）：[任意p奇余量核心](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_uniform_odd_middle_cores.md)核对71组参数公式、426个原位置返回、284个精确终端输送（52次小代表折返）、六个CRT取逆构造及69条既有全输入入口。任意模数/层级的群包含由外部定理及正文承担，不由有限核验外推。新增全部奇余量合法核心及相应入口范围的全输入判据，含七平均17、19；未降低最终阈值或给出高效完整群词提取。

新增 five-thirteen-congruence（core/full）：[五平均十三元](../sources/work/document_reorganization_20260915/originals/outputs/five_average_thirteen_congruence_complete.md)核对25个原位置宏及根、模169的2197元素主同余层、24个高阶幂零恒等式、156个合法模13向量、160个精确Bezout目标矩阵、80个既有全输入入口及三步尾部。一般群包含依赖Morris有限指数与Serre强同余定理，不由有限样本证明；没有展开任意输入的完整群词或声称高效求解。

新增 endpoint-congruence-completion（core/full）：[任意合数端点核心](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)。34个有限商/level组合共184597个目标元素比较，4947次任意有限环公式重放，9422个小单位及陪集归约，28个既有正向编译器检查通过。全称群等式由Morris 2007定理6.1(2)、Serre强同余子群性质和正文的任意模数消元承担。六素因子入口由此升级为完整端点判据；没有一般后续阈值或高效完整求解器。

新增 complete-local-unit-recovery（core/full）：[全碰撞单位分支统一补回](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_complete_unit_collision_recovery.md)。一般证明覆盖全部临界参数，有限核验检查3305个计数系统和627个实际入口，完整核心前缀不超过五步；此前十个局部菜单缺口全部重放。e=1重叠后使用模h^2-2的至多O(h)个余数，逐位置检查配比、两个后续组不交且使用了重叠产生的位置。983例同时验证不交整数组库存障碍。没有将局部补回当作全局递归或新的阈值证明。

新增 sharp-multiplicity-precision（core/full）：[重数弱化与精度锐界](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_sharp_repetition_and_precision_barriers.md)。132个三值停滞族实例完整枚举整数类型组并核对唯一非恒等输出G=n；44个精度接口核对现有大维数定理条件；24个纯整数冻结例达到第二重数p-2；161个截断重数安全选择、8组精度前缀反例与整数造零对照通过。精度一位的充分性来自已证定理，不把初始出口重放当作完整解。四值探索诊断未含输出安全性，不作为闭包证据。

新增 euclidean-witness-transfer（core/full）：[欧几里得见证转移](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_euclidean_witness_transfer.md)。4957个互素余数系统核验半周期最小正余数的逆元公式；1191个负余项、1222个正余项计数系统；p<=1000中226条负余项、248条正余项实际转移，并把全部248个正余项输出再接三次平均，消去旧高值、降低最大值并重新建立相邻重值对。10个当前菜单未覆盖入口保存在记录中。有限计数不证明后继可递归套用，不是新全维数阈值。

新增 unit-witness-replenishment（core/full）：[单位见证补回阶段](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unit_witness_replenishment.md)。手写证明二维非负关系锥的Hilbert基、两原子补回充要条件和两个三原子扩展。241187个整数容量系统、1051条实际补回、8条缺额1扩展、3条(h,d)=(3,2)扩展、3条直接保存通过。另完整消元核对29平均95元核心的单步相邻重值障碍并重放四步造零；49个实例核对任意k的统一反例。这里只证具体入口和阶段，不证明输出可递归套用，也不证明全维数阈值。

新增 provenance-dynamic-integer-stages（core/full）：[来源关系、动态见证与整数返回阶段](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_provenance_dynamic_and_integer_stages.md)。5566条r>=2后继和360条r=1后继逐原位置验证第二次安全整数续步；902个状态核对共同危险支持与gcd(3alpha-2,n)公式。另有七步实际核心冻结反例、固定重锚点统一障碍、原始模3坍缩后的合法本原化、五步整数返回正对照，以及固定A、C下的能量和整数两两距离障碍。普遍量词由正文证明承担；不把两步续行、保留来源或有限样本视为递归闭包与新阈值。

新增 core-exit-potential-scope（core/full）：[上半带核心整数出口与势函数范围](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_invariant_improvements_and_core_exit.md)给出任意p>=5和全部r的手写一原子出口证明；只剩四值后继的可重复性。144个参数、10800个选组验证原始同余危险仅在3|r且选尽C；944个大整数原位置出口保留双重值、G和整数性并严格降能；180例验证一般k的两两距离下降。没有把原始全同余为0的输出一概判成G非法，没有宣称新阈值。

新增 distinct-entry-gaussian-transfer（core/full）：[不同值整数入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_distinct_value_integer_reduction.md)与[旧合数/高斯路线迁移](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_revisiting_ternary_factor_gaussian_route.md)。六个k=2,3,4,5,7,11的实际整数入口逐位置保留见证、总和并严格降能；六个(p,ell)参数在完整系数基和真实位置上核对高斯全局标量周期，含5平均11元det(K_-1 K_1-I)=4的非单位边界；4503个临界因子关系核验。一般公式在正文，不将有限周期样本当作根生成、轨道覆盖或新阈值证明。外部小n搜索复核已停止。

2026-09-12新的实质结果：[单值零和最优界与极端冻结态三步逃逸](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_sharp_concentration_and_escape.md)否定旧3p-2猜想，证明所有N>=2p-1的最优两桶界N-floor((p-1)/3)。引用Balandraud定理并核对勘误；达到最坏界的合法整数冻结族在全部素数p>=13（另含p11）都有三次真实平均造p个零的公式，首次造零步数最优。45408个零和自由序列、319015个余数配置及91条原位置路径核验通过。未新增全维数判据或降低N(p)。ID `sharp-monochromatic-escape`。


新增 dominant-residue-reservoir（core/full）：[主余类储备](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_dominant_residue_reservoir.md)处理一个低重余类至少p-alpha份而其他轻值任意分余类的局部续步。367224个主类碰撞提升、15497个相容参数、37754个例外配比、13301个超额包装和834条原位置Fraction续步通过。文档明确保留“每个例外只有一个配比”的刚性边界，不宣称多余类闭包或N(p)<=3p。

新增 binary-collision-lattice（core/full）：[二类型碰撞整数格证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_binary_collision_lattice.md)以基本格三角形及单候选区间计数承担一般整性量词，再接总和和私人见证。130420组临界系统、113628组富余系统核验通过；2133条单实际轻值续步（816条保护、169条r=1）、300条三重值续步（21条r=1）、127条单余类多实际值续步逐位置检查整数性、G、双重值与严格能量下降；包括p29/n90的三个私人见证及G11的非法中间碰撞对照。只证明列明整数续步分支，未证明多余类类闭包或完整上半带终止。

新增 upper-band-descent-boundary（core/full）：[3p剩余缺口与核心逃逸](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_remaining_gap.md)核验2544组第二载体容量、484条六原子周期；9344个方向的有限单轮诊断中1703个未找到菜单下降或终端；对七平均22元(2^14,(-1)^7,-21)的十个不交返回给出完整原位置证书，完整性由正文均值区间证明承担。93个任意素数两步整数造零样本通过，正文给一般公式。共同因子先约去再检查G，未把未归一化全零余类误判为非法。不证明核心不可达、全部22元可达或统一3p阈值。

新增 upper-band-three-value-reduction（core/full）：[3p到4p的统一三值归约](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_three_value_reduction.md)由初等短区间筛选、原位置支持集中及重复运输行证明任意素数p>=5、整个3p<n<4p的全输入归约，次数至多12+3ω(n)，无r>=d或素因子数限制。1770组筛选、106534组容量、376条随机大整数入口（18条r<d）、5条强制多素数入口（最多5种）和4条强制主块修复逐原子Fraction重放通过；另564组核心能量、544组本原高度增长及700条真实全局对合周期通过。只搜索短区间副本参数，不搜索平均词。未证明核心终止或降低N(p)。

新增全局总览：[averaging_global_status_20260912.md](../sources/work/document_reorganization_20260915/originals/outputs/averaging_global_status_20260912.md)汇总从二平均到任意q的已证判据、自动G点、非自动边缘H(q)、最终阈值N(q)与临界线猜想。它是导航文档；各项无限证明仍以对应定理文档和manifest核验入口为准。

新增 ten-twelve-seventeen-complete（core/full）：[十、十二平均17元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/ten_twelve_average_seventeen_complete.md)分别使用(10,6,1)、(12,4,1)核和模17的18陪集、54条回路；十平均激活Delta(5)，十二平均激活Delta(3)，各自得到G=1充要，H(10)=H(12)=17。17个q<=200自动B点、各288本原模行、54回路、各60大整数入口、各3条完整路径通过。16元自动G点不计入H；不证明N或最短长度。

新增 six-prime-endpoint-entry（core/full）：[六素因子统一入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_six_prime_endpoint_entry.md)由五类非覆盖与d-1个实际坏类的证明承担一般量词。核对211040组五素数坏类、模24六类覆盖、6个大重数入口（含原K4障碍）及n15015的逐位置六步入口。大输入按精确重数保存，不展开上亿相等坐标，不搜索平均词。没有新的一般核心群包含或完整中间带结论。

新增 arena-triple-solver-review（core/full）：[外部Arena三平均算法审阅](../sources/work/document_reorganization_20260915/originals/outputs/arena_triple_solver_review.md)保存实际iframe算法快照并与48个旧输入比较。网页33题成功，旧构造48题成功；24个小整数实例的22题步数相同，1题更短、1题更长，预热后JS约0.85ms而旧Python约1.95ms。独立Fraction重放37条主测试成功路径、24条预热路径和33个宏基；另外核验整体放大导致浮点启发式不生成候选的例子。快检不重新计时，结论仅限该版本和样本，不更新数学可达性定理。

新增 four-prime-entry-and-band（core/full）：[四素因子入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_four_prime_endpoint_entry.md)的35784组坏指数类、64条原位置入口及12个强制见证合并通过；八个旧核心level的18192条回路重新核对，入口连接后得到其全部输入判据。另[中间带统一结构](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_band_period_and_involutions.md)核对127个维数参数对的381条全输入降维，以及1119组全r、全允许奇s的真实四原子标量周期和局部安全性。无限量词由正文的指数密度与矩阵公式证明；不搜索平均词，不生成新核心证书。七素数指数类可完全覆盖的边界另保留，不外推任意素因子数。

新增 averaging-algorithm-benchmark（core/full）：[算法测试集](../sources/work/document_reorganization_20260915/originals/outputs/averaging_algorithm_benchmark.md)核验584道唯一题面及580个冻结态结构、108条完整精确参考路径和1个阴性对照，并检查7项验解拒绝／大整数精度条件。不运行束搜索或重做完整高度枚举。p=7,n=15采用新定理真值，未获定理或证书的p=19,37扩展不计已知可达正确率。

新增 endpoint-reverse-diagnostic（core/full）：[端点反向诊断](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_counterexample_reverse.md)报告p=7,n=15高度5的35714个状态和7个整数陷阱；独立脚本确认7个均无整数出边、首步均无零和七元组但二步有理层均产生零和七元组。该有限诊断不证明n=15全称可达，也不构成反例。

新增 strategy-reassessment-20260912：路线重评估和文献缓存为研究记录，不是证明核验。策略脚本缓存44个查询、148个去重题录；障碍脚本通过56个多素数单位分离、3538个返回字符和117个一般合并恒等式。

本文回答三个接手问题：哪项数学结论对应哪个程序，程序的 PASS 究竟证明到哪里，以及怎样在相同参数下重现当前数字。它是导航和复核契约，不替代证明文档。

新增 composite-endpoint-transfer（core/full）：[合数端点CRT推广](../sources/work/document_reorganization_20260915/originals/outputs/composite_endpoint_crt_transfer.md)使用独立证书核验器确认36个指定模数的32112条完整Schreier回路，主元因子全部落在已证允许环。28个两素数模数由统一三步入口得到全输入判据，8个三/四素数模数的入口已由四素因子定理补齐，36个列明level均为全输入结论。另960条回路实际编译正向DAG、98个基参数宏、168个一般入口、84个强制入口、5条完整词重放。有限范围内所有奇p<=109的端点均已完成；不宣称任意level成立或最优阈值。

新增 seven-average-fifteen-complete（core/full）：[七平均十五元完整证明](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_fifteen_complete.md)给出至多两危险素数端点的统一三步入口，再用二进Gauss覆盖模15的24个陪集全部72条回路；62条左上、8条右下、2条半整数上剪切消除11和17主元，无需新宏种子。192个本原模行、10个实际基参数宏、1800个局部类型/安全性检查、160个大整数入口、72条强制三步入口和7条完整Fraction路径通过。G3/5/15排除，G1全称可达，H(7)=15；不证明后续全部维数或N(7)=15。

新增 six-average-ten-complete（core/full）：[六平均十元完整G判据](../sources/work/document_reorganization_20260915/originals/outputs/six_average_ten_complete.md)证明G=1或2恰好可达，G=5或10不可达。四个实际宏含一个两步R返回；三条精确周期给正向逆，DFD^-1F^-1=L(-5/3)产生模5下根，完整6陪集18回路覆盖Gamma_0(5)。核验8个基参数宏、24个本原模行、196种完整余数多重集、两种合法G各60个大整数入口和6条独立Fraction路径，最长1931步；另明确核对两个非法G例子。按用户以非自动G条件为主的标准，H(6)=10已证；N(6)及十一元仍未完成。

新增 composite-critical-scale（core/full）：[合数临界尺度报告](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md)证明S(q)=max p^ceil(v_p(q)/2)给出的G1反例下界及边界G=q/S+1；固定四步网络q=m(m-1),n=m²在相邻因子有素数时达到下界。25865个完整压缩原子后继、368个边界退出、199个元数算术检查和14个全矩阵网络通过。M(q)=B(q)与N(q)=M(q)仍为两条独立猜想，边界G合法不自动可达。

新增 eight-average-thirteen-complete（core/full）：同一报告第7节由(8,4,1)核和真实周期C^4=-I/64、(A²C²)^3=I/4096构造正向二进控制器；带符号2幂代表使模13的42条完整回路均可编译。6个基参数宏、168个本原模行、120个大整数入口、5条完整路径（最长3577步）通过。结合至12元的反例，严格证明M(8)=13；不证明N(8)=13、九平均13元或最短长度。

新增 arbitrary-arity-linear-threshold（core/full）：[任意元数线性阈值](../sources/work/document_reorganization_20260915/originals/outputs/arbitrary_arity_linear_threshold.md)证明所有整数q>=3在n>=4q-1+d_q(n)时的完整G支持判据。一般量词由非单位配比、唯一中点例外、一般EGZ及系数打包证明承担。核对987个配比、172个中点例外、3040个容量、4488个四/六平均完整余数多重集、2804个大整数闭包及39次初始化；70条完整路径最长94步，另24条四/六平均造零收尾路径。全部15种算法分支均触及，不修改旧素数求解器适用域。未证明最优阈值或位长多项式输出长度。

新增 four-average-nine-complete（core/full）：[四平均九元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/four_average_nine_complete.md)由显式(T2 Sigma)^2=-2I及仿射配对产生正向二进上下根，模9的12个陪集全部36条回路主元均为1、2、4，Schreier给出Gamma_0(9)包含，再接任意合法入口、Bezout和三步终端。检查72个本原模行、144个入口、50个大整数输送及6条完整四平均路径，最长621步。不做种子或路径搜索；不提供最短界或一位精度保证。

新增 four-average-seven-complete（core/full）：[四平均七元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/four_average_seven_complete.md)使用 (4,2,1) 核，C^3=I/8、(CA)^2=I/8、C²B=Sigma/8均核对真实尺度；Sigma由真实词实现，禁止免费交换不等块。改取有符号2幂陪集代表，24条回路主元全为二进单位；16806个入口、80个大整数输送和12条完整路径（最长527步）通过。只解决七元，未解决四平均11、13、15元或N(4)=7。

新增 six-average-nine-fixed-network（core/full）：[六平均九元独立复核](../sources/work/document_reorganization_20260915/originals/outputs/six_average_nine_fixed_network.md)以9个标准基证明固定四步词恰为J9/9；穷尽84种第二次操作的756行，配合“第三步保留三行”证明不存在固定三步全输入词。另160个有理样本精确通过。四步最优只指固定全输入网络，不指每个输入，也不推出N(6)=9。

新增 composite-four-six-transfer（core/full）：[合数平均的统一半块转译](../sources/work/document_reorganization_20260915/originals/outputs/composite_arity_four_six_transfer.md)手写证明偶数q、q/2|n且吸收奇素因子后的二平均商维数M=2或M>=4时的完整G判据。推论覆盖四平均所有偶数n>=8（另有n=4）、六平均全部3|n且n>=6；纯三幂六平均由九元四步固定网络补齐。533个标准基重放、35个副本宏、30915+1500个陷阱后继、169次独立分组修复与336条完整Fraction路径通过。四平均六元和六平均八元的G=1反例由无限不变量证明，程序只审计有限后继。未给出其他维数完整分类、最终阈值或最短解；不使用未经全文核查的Clique Gossiping摘要判据。

新增 carrier-energy-dyadic-neighbour（core/full）：[能量与 2p+2 完整族](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_energy_and_dyadic_neighbour.md)证明 p=2^s-1 的完整 n=2p+2 判据，允许合数 p。一般安全交换、CRT 单点等值化和正向除法返回使 |v| 严格阶段下降，新增七平均十六元，不调用十五元端点。核验18个共同二次型空间、1152个能量和本原高度实例、19968个模素数幂条件、274个CRT例子、160个原位置降维、362个分块入口、31278个方向、24条核路径和48条原输入完整Fraction路径；最长239步仅为样本数值。另核对50086个约分公式，保留五平均 (u,v)=(3,11) 的整个数字族单步下降失败，不外推一般p的中间维数。相对尺度前页的商阶、安全性和跨维数目标已修正。

新增 prime-power-endpoint-completion（core/full）：[素数幂端点与临界几何](../sources/work/document_reorganization_20260915/originals/outputs/prime_power_endpoint_and_critical_geometry.md)证明q=2p+1为素数幂时的全部端点判据。两张局部射影图、全部Schreier回路、正向Gauss编译与两步合法入口共同承担一般量词；独立核验15612条转移、55512个模行、168条正向编译、32个大整数入口、2754个范数恒等式和2条n=27完整路径。文档还给出判别式-q虚二次阶的theta联系及2p+2共同尺度失效。该ID新增十三平均二十七元完整定理，不推广到多素因子端点或相邻维数。

新增 prime-power-endpoint-entry（core/full）：[临界前沿交接报告](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_critical_frontier_handoff.md)第6节完整证明素数幂q=2p+1的两步合法双块入口，并指出奇素数平均元数下的合数素数幂端点必为3幂。独立Fraction重放核对n=27的133种模3重数模式及全部单点选择，共3591项，另有56个大整数原位置实例和6个边界族控制。入口结论不承担合数level的核轨道、全部端点判据、临界以上区间传播或更低完整阈值；报告中的后续方向不是已证结论。

新增 uniform-collision-structure（core/full）：[任意p的碰撞结构](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_uniform_collision_structure.md)手写证明保护后3p+1层中p-2重余类的统一闭包，给出全碰撞D=3p或3p-1与分数族除数参数；另证明两个不交短零和组的同向修复、明确总余数窗口及足够多不同余数时的闭包。51618个高重数模式以独立候选方程核对分类，779个整数原位置步骤包含419个非空保护集合实例；4824个零和分解、105760个窗口公式和144个受限和集构造通过。全部一般结论由正文推导及明确引用的Dias da Silva--Hamidoune定理承担，有限计数不代替任意p量词；没有重跑旧五／七平均完整证书。未证明全体中等重数模式、3p统一阈值或精确2p+1端点。

新增 seven-average-three-p-plus-two（core/full）：[七平均N(7)<=23](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_three_p_plus_two_threshold.md)以一般有效的余数对称平均压缩碰撞系统，57026个模7模式中仅11个相容唯一解，总和为整数且在0与未保护总维数之间。私人见证排除保护非空，类内部分选择迫使实际常值以排除无保护情形，解决23至26元；5628个大整数闭包和96条原位置路径（最长276步）独立核对一位额外精度。任意p与22元仍未完成。

新增 minimal-protection-and-exchange（core/full）：[一般保护交换](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_protected_exchange_and_mass.md)证明初始化可在3p+d-2完成，并给出p=23,n=70固定保护全碰撞、换保护即修复的非零合法例子及p=2 mod3的3p+1元五步整数族。核验3920个初始化、187组双候选族、6个保护交换和10条五步原位置路径；不增加一般完整维数或证明候选总和猜想。

新增 five-average-three-p-threshold（core/full）：[五平均N(5)<=15](../sources/work/document_reorganization_20260915/originals/outputs/five_average_three_p_threshold.md)以903个模5模式的完整有理线性系统和22个唯一解，证明碰撞总和的局部分母结论，再用最小保护横截集及私人见证排除合法失败，完整解决n=16、17、18；接独立15元与>=19得到统一界15。另核验2120个保护集合、5545个大整数闭包、120条逐原位置Fraction路径，最长201步，新三维数均一位额外精度。程序不导入探索系统生成器，正式分类允许每个位置有独立变量。任意p的3p界和五平均12、13、14仍开放。

新增 three-p-two-anchor-interface（core/full）：[3p双锚点接口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_additive_interface.md)以Savchev--Chen标准定理证明3p+d容量下安全整数候选必存在，并对长序列零和自由分支给出一／两个低重数位置修复。核验231060个小余数实例、105个独立极值算法对照、8个修复实例，以及4246个实际状态的局部诊断；另检查模同余基族不满足基交换及低于3p预算的边界。候选存在但全部实际和碰撞仍未普遍解决，不证明3p阈值。外部定理明确引用；本轮未重新证明它，也未取得原论文全文。

新增 inverse-egz-threshold（core/full）：[4p-2+d完整阈值](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_inverse_egz_threshold.md)将原统一条件减少一个位置，得到N(5)<=19、N(7)<=27，保留一位额外精度。三重值两位置修复和共同预留跨越给出新结构；逆EGZ强迫两个p-1余数类，借锚点闭合保护池最后缺口。核验19059个完整余数模式、1650个大整数闭包、64个借锚点修复、12个跨越和36条原位置路径，另独立核验869个三重值实例。约7p/2路线仍是条件目标；可选有限诊断不进入正式证明量词。

新增 inverse-zero-sum-transfer（core/full）：[逆零和原位置转译](../sources/work/document_reorganization_20260915/originals/outputs/inverse_zero_sum_averaging_progress.md)通过线性部分和扫描生成有容量保证的加权见证，证明相反碰撞的两步恢复、不同余锚点下十四元(5,5,2,2)核的安全单步分类，以及任意奇数p>=5的2p+4元二参数七步归零族。核验3102个完整小余数多重集、1095个一般副本实例、3192个十四元实例、5个碰撞恢复及117条原位置Fraction归零路径。未证明整个十四元或2p+4元维数，也未改进N(p)通用上界；没有平均词搜索。

新增 prime-arity-zero-trigger-bridge（core/full）：[支持数传播与加权均值格](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_interpolation_and_lattice_structure.md)证明所有奇素数p、n>=2p+1中，真实p平均一旦造零即可完整收尾；不需端点完整猜想。另证明余维一整块等化障碍、块均值仿射格判据和本原重数的有限商，解释两个Gamma_0来源，并记录p幂维数传播。核验120条低段与108条高段全局Fraction路径、8个余维一边界、426个重数格实例及398个支持数覆盖。未证明先造零必然发生，也没有证明两端内插或新增完整中间维数。

新增 prime-arity-middle-band（core/full）：[三块运输与3p定理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_middle_band_structure.md)用两张九项非负整数运输表统一实现U(+-1)，块重标记给L(3)，完整四陪集与模3入口解决所有奇素数p的n=3p；另证n>=3p+d时同余双重值闭包。核验40组实际运输、12条完整陪集边、7个旧反例族、7个G=p输入和56个其他输入的完整Fraction路径，最长105步；另核对996个闭包实例。未证明整个中间区间、3p级统一上界或一位额外精度。

新增 uniform-endpoint-controller（core/full）：[统一正向控制器](../sources/work/document_reorganization_20260915/originals/outputs/uniform_endpoint_positive_controller.md)不搜索平均词，以两种真实返回、仿射配对、必终止的整数链和欧拉迹零公式，证明所有奇数平均元数的U(R_q)、L(qR_q)及对角单位均有原位置正向实现。q=2p+1为素数时，完整Schreier、Bezout和两步入口证明全部输入可达 iff G=1。程序以共享无环表达式核验984组返回、25个平均元数种子、418个可逆倍率、528个完整回路及1656条边，并逐位置Fraction重放10条完整路径，最长2466步。q合数时的完整群／轨道与任意输入入口仍未证明；不声称N(p)=2p+1或统一精度、最短长度。

新增 five-average-n11-random-experiment（core/full）：[五平均十一元实验](../sources/work/document_reorganization_20260915/originals/outputs/five_average_n11_random_experiment.md)记录六档共120个独立随机原题，范围从正负20至正负2^128，只按G为5幂筛选，全部找到原位置证书；另有92个明确分开的K5核心压力例。默认核验重新生成抽样并独立Fraction重放全部212条保存路径，以及24个全位置后继和40个零坐标收尾。它只证明这些输入可达，不证明所有十一元、N(5)=11、统一精度或最短性。已有严格阈值仍为11<=N(5)<=25。

新增 pair-triple-solver-optimality（core/full，需要Node.js）：[二三平均求解器与最短性](../sources/work/document_reorganization_20260915/originals/outputs/pair_triple_solver_comparison_and_optimality.md)核对用户原HTML的16个内置测试、三平均精确IDA*和独立Fraction BFS，证明四组最短距离分别为3/1、3/4、1/1、3/2。151个零和打包数后继及100个数值三维匹配编码核验一般公式。正文从经典强NP完全的N3DM严格归约，证明即使G=1且保证可解，达到n/3步阈值仍强NP完全；这不否定可达性多项式判定或非最优多项式长度解。24例同题比较另存JSON，只是可行上界统计。

新增 double-triple-sequence-length（core/full）：[长度分析](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_sequence_length_analysis.md)证明两两距离数值界、适用于任意非恒等整数三平均序列的最大间隙递归界，以及固定非三幂维数的对数步数下界。固定 n 的构造已具位长多项式上界，次数随 n 增长；可变 n 的统一多项式界仍开放。程序核对69,926个势能不等式、150个最大安全降幅与独立枚举的对照、142个最大间隙阶段、6个单步比例下降障碍及23,466个短输出行排除。另存18组配对与12组大整数实验；它们是有限性能数据，原策略的三个100000步截断不能视为不可达或最终长度。

最新 all-dimensions-double-triple-invariant（smoke/core/full）：[任意维数双三重值直接证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_all_dimensions_double_triple_invariant.md)将新不变量推广到全部 n>=11，包括偶数和多素因子合数。多危险集至多留出 d 个位置，n>=d+10 保证容量；仿射见证处理模2，gcd(a-b,n)=1 替代素数性。全称结论由正文分类和整数能量证明。程序核对17,575个有界闭包、4,458个大坐标闭包、4,799个初始化、64个模2修复及80条完整精确路径；不运行词搜索。全部 n>=7 只另需7、8、10独立基例和9元网络，不再需要一般合数归约。n>=11的一位额外精度已证，位长多项式构造步数仍未证明。

新增 final-hecke-manin-audit（core/full）：[最后检验](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_final_hecke_audit.md)核对44个整数幺模共轭、308组共同星结构方程、1884个合法cusp输送，以及普通模符号的中心负号、删点非Möbius与有限／球面Hecke区别。一般障碍由正文公式证明，无词搜索。仅排除指定的直接酉表示和线性Manin接口，不否定原猜想或所有自守路线。

修订 iwahori-hecke-modular-interface（core/full）：[修订接口页](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_iwahori_hecke_modular_interface.md)保留有限Hecke二次／辫子关系、数字置换和、矩阵分解、能量、本征投影及根公式核验。原指数p格与全局Eisenstein／Steinberg、T_3解释不成立或未证明，已由最后检验明确纠正。旧PASS只核对这些代数恒等式，不承担全局接口。2084个返回矩阵的库存结果继续保留。

新增 nonsplit-hecke-chart-boundary（仅full）：17个非分裂素数至149的全部平移分层中，单层到任意B_p chart、两层到任意chart及三层回基准chart都只有恒等返回，没有非平凡参数3反射。程序用块系数和相同行分组识别全部角色，不展开p维有理矩阵。它不排除三层到其他chart、更长词、额外宏或奇异终端。

新增 atomic-hecke-wall-boundary（仅full）：对p=11至71的9个B_p系数状态，无遗漏遍历深度5以内的非恒等原子三平均计数状态，按(p-4,3,1)重数和Hecke迹方程筛选，没有非标准第二墙。每个稳定素数约83000状态，组合按重数签名缓存并按素数并行。它不排除更长词、子问题宏或直接终端。

新增 b71-symbolic-directed-terminal-cover（仅full）：一次符号系数--重数遍历同时处理B71(1,v)中-100至100的198个合法整数参数；至多6步准备后出现零和三元组，再平均一次可产生三个零。深度5在正负10000窗口覆盖1251/19720。稀疏性是有限线性终端方程的一般性质，不构成Manin结构证据；本项不覆盖任意有理斜率。

历史经验与有限实验汇总见[非分裂素数路线复盘](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_route_reassessment_2026-09-11.md)，其后提出的Hecke主线以本页最上方的最后检验为准。该页中的B71计数、贪心、同步窗口等数字仍为有限探索证据。

新增 equal-carrier-formal-freezing（core/full）：[等载体形式冻结定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_equal_carrier_formal_freezing.md)的16组整数平衡剪切、8个Q基SL接口和317844组素数gcd接口。一般证明给出SL--一次等载体交换--SL三段正规形，并证明每个合法素数形式轨道命中零叶块；有限域唯一避开轨道是q整除3r+2时的常值直线。两个SL块的现有构造使用形式逆，因此该条目不证明正向三平均实现，也不新增已解素数。

新增 carrier-sweep-catalyst（core/full）：[载体扫掠催化器](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_carrier_sweep_catalyst.md)的一般秩整数扫掠公式、秩二有限中心、秩三24个幺幂与12个同长度逆、可逆根的完整sl3 Lie闭包、方向／协向量格指数5／32、四个固定对立根及E3(4320^2 Z)包含、第二载体余边界及15个模20碰撞轨道。另用NumPy批量核对模2/3/4/5像为1/5616/4/3000。一般扫掠与局部均值余边界由正文公式证明，整数有限指数由标准初等同余群定理承担；有理碰撞由下一条目补齐，仍未证明任意p终止。

新增 carrier-catalyst-local-descent（core/full）：同页的十位置有理碰撞定理。六根约化域精确分成30个一般锥与50个根步长为零的异常锥；2805个深度至多三的扫掠／根二次型经适用域零面递归和有理重心细分得到538与274个证书叶，最大深度15／7，未解0。每个二次型在锥上的最大值由顶点、边驻点和内部驻点精确判定；不是有限高度样本。该定理不提供重叠窗口的全局下降。

新增 carrier-collision-global-interface（core/full）：局部碰撞在一／两次额外平均后进入两个等载体，两种情形均有显式反解，故完整Z[1/3]仿射差分模保持。根与正向逆的局部中心收缩给出重叠差(3^(8k)-1)/3^(8k)，程序核对k=1..12；一般指数族由闭式证明。它排除直接拼接局部本原Q作为全局高度，不排除同步窗口或冻结零和块。

新增 mixed-singleton-conditional-controller（smoke/core/full）：[混合单点条件控制器](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_mixed_singleton_controller.md)的50个迹零周期与仿射交换子、18个平方自由素数支撑根接口、1674个有符号Schreier参数、36组共同严格正三进运输边际及431对角影子边界。一般条件定理由正文恒等式、素因子支撑和对角吸收证明；程序不证明两个目标运输能在原p位置分解。

新增 reynolds-hodge-structure（core/full）：[内在代数结构](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_reynolds_hecke_hodge.md)的209个Reynolds／凸平均、110个根恢复与190个秩一乘积、27个Hodge恒等式、1238个合法到非法像、27个局部Iwahori共轭和1716个判别式赋值控制。一般生成代数与Hodge边界来自正文闭式证明，不宣称该对偶正向可实现。

新增 contingency-layer-semigroup（core/full）：同页的60个运输表层实际系数重放共336次原子平均，54个载体字母，25个终端超平面和205个交数秩。每个运输表都普遍合法，但紧凑层半群的终端覆盖仍是猜想；无损编码全部原子词的是较大的单三重块模型。

新增 n47-complete（smoke/core/full）：[47元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_forty_seven_arithmetic_complete.md)。重验170节点逆证书，核对固定尖点词、两个伸缩、18个完整Schreier回路的正向根分解、48陪集与独立标签、1434个输送、六步原子终端、928个桥及8项目录集成。47已加入因子闭包，最小未解53。正式核验不运行目标发现搜索。

新增 localized-iwahori-generation（core/full）：[一般局部化生成](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_localized_iwahori_generation.md)的2238个标准Schreier公式和单位消元、8个一般伸缩校正、32个奇次三进返回到尖点恒等式，以及73处固定单位像边界。一般p量词由正文的统一代表与公式证明；正向资源普遍存在仍是假设。

新增 b47-root-activation（core/full）：[正向根群饱和](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_positive_root_saturation.md)与固定170节点JSON，独立重放全部模板及无环依赖，三层46/113/2覆盖旧167宏；57次模板的共轭正向词及两个完整根群的矩阵恒等式均核验。正式入口不导入发现程序。尚未证明有限指数、合法单轨道或47元完整判据；一般迹根引理、全参数根族及统一素数条件定理见正文。

新增 b47-extra-atom-involutions（core/full）：[固定新宏](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_b47_extra_atom_and_adjoint.md)独立重放三个extra-stage模板、九个可逆生成元及三个周期；U(+-47)词验证正向替换，32个三进与6个二进共轭给出47Z[1/6]根群，18个参数对合族恒等式给出分裂环面边界。不是47元完整判据。

新增 adjoint-return-domain-audit（core/full）：重建旧167模板的物理子集和末尾置换，全部核对Gram伴随公式，逐步检查反向域；15个普遍合法，均在旧库。共享Fraction重放器现在支持可选extra阶段，旧宏的默认路径和矩阵数量不变。

新增 projective-spectral-balance（core/full）：[一般谱判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_projective_spectral_balance.md)的85个共轭／缩放周期例子、4个独立条件边界、10个Ad分圆算法输入及B47实二次范数宏接口。一般充要条件和复杂度由正文证明；不把给定宏的周期判定误称为原平均可达判定。

同一条目后续增加125个可交换Q(sqrt89)关系对照：相对素理想赋值和实单位指数同时为零才构成周期。一般可交换库的全正关系格判据见第8节，程序不实现通用S单位求解。

新增 b47-short-cycle-boundary（仅full）：[固定B47库的排除](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_b47_cycle_frontier.md)，167模板、4657463三因子词、27160个全指数方程和737665600个四因子组合。后者是NumPy int64精确模筛选，3896个候选再做任意精度整数判断，包含溢出界与行列式模零控制。历史浮点工具仅用于发现，不承担排除证明。

新增 paired-carrier-two-adic-reset（core/full）：[等值载体二进宏](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_paired_carrier_reset.md)的六秩矩阵／格／迹检查、132个完整系数基实际操作、120个双理想保持实例、9个入口／奇偶边界、54个虚拟质量反例及5160个输出置换的迹整性排除。一般4r-3步构造与det公式由两遍广播证明；单宏有限阶阴性结论仅限明列秩，词长赋值下界为一般结论。

新增 n41-complete（smoke/core/full）：[41元完整证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_forty_one_arithmetic_complete.md)固定21模板、10个三因子对合、10个整数词，独立核验42陪集、唯一合法尖点、1422个输送和928个桥，另有7项目录集成。子程序仅3/9/18/27/37/38/39。正式核验不运行发现搜索，最小未解维数为47。

新增 modular-primitive-height-barrier（core/full）：[有限模与高度边界](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_modular_height_barrier.md)在12个模恒等终点间实际重放2304个平均，核对实能量严格下降而本原高度按精确公式增长。任意h的结论来自闭式证明，不是12例外推；它不否定可以选择其他下降词。

新增 two-carrier-modular-bridge（core/full）：[全部n=5 mod6的二例外桥](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_two_carrier_modular_bridge.md)。165个混合好划分、9个不除以r的有限环拼接、34个整提升、模5下15624点正向轨道、20个有限模逆指数、5条共567个原子操作、480个子问题／输出接口，以及320个核内调用边界。一般量词由正文的主同余包含、CRT与有限群正向化证明；不把480个同余目标模式当成480条完整调度。该条目不证明二例外核终止。

同一条目还核对460个对角二次型、G公式和一步安全B核桥；因此该n族的标准核进入已证明。一般profinite正向启用原则由有限群中逆为正幂的正文论证给出，不是用模5样本外推。

此前 n29-complete（smoke/core/full）：[29元完整证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_twenty_nine_arithmetic_complete.md)固定18模板、9个三因子周期、7个整数词、30陪集及独立模29标签、1398个输送与928个桥，另有8项目录集成。仅调用3/9/25/27，最终使用冻结库1194模板；不运行浮点发现搜索。41元已另有后续证书。

新增 nonsplit-projective-layer-boundary（core/full），在5/11/17/23/29的原位置数上重放非分裂射影轨道层，核对奇异位移、不交换和全位移乘积非标量。该有限边界不否定其他非分裂控制器。

编译器的 `--expanded-first` 开启所有已证首步大小，默认首步库保持3/9及可选的特殊6不变。29元扩展库1242与旧当前库1195均可复现；正式29元证书进一步使用冻结子问题库1194。发现工具 `search_bn_three_cycle.py` 的浮点迹筛选只产生候选，精确证书另行固定。

新增 split-prime-gaussian-controller（smoke/core/full）：[全部p=1 mod3素数定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_split_prime_gaussian_controller.md)。4项抽象Eisenstein格恒等式，496个固定真实位置上的范数周期原子操作，10个素数的单位／根／仿射接口，800个单位剪切原子重放，320个仿射正规形与gcd消去输入，以及14项目录集成。一般剪切本原性由正文对每个素数的反证承担；没有用有限素数样本外推。剩余统一问题为p=2 mod3，29仍开放。

新增 flat-star-formal-arithmeticity（core/full）：[平坦核形式算术性](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_flat_star_arithmeticity.md)的12组幺幂／行剪切、18组64N与192根群接口、18组双载体拼接及79个第一层终端代表。一般有限指数证明明确使用Tits／Bass--Milnor--Serre初等同余群定理，第一层局部乘积使用Goursat引理；脚本不将形式逆认作正向平均。

新增 cyclotomic-level-entanglement（core/full）：[置换level与两处耦合](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_permutation_shadow_entanglement.md)的20组方差／置换式、240条尺度归一化词、旧容器严格反例及43008状态Schreier二重覆盖。新容器有192尖点、48合法尖点、属3473。旧n91-congruence-container继续复现21504容器，二者不能混用；旧24个合法尖点的终端计算不自动覆盖新48类。

新增 balanced-digit-congruence-group（smoke/core/full）：[完整数字同余群](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_digit_congruence_group.md)的380个列稳定子公式、160个独立主同余输入、118个数字倍率／周期和492个射影轨道迭代。群等式、有限指数、分裂扩张与轨道分类的无限量词由正文的列消元及整数初等生成证明承担。它不证明原维数宏库的算术性。

新增 b29-current-cycle-boundary（core/full）：[29元当前库边界](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_structural_picture_audit.md)核验1195模板的714610个二因子乘积，并用精确二次迹方程排除全部j>=0的A^jB周期。7个控制包含指数57和100的人工标量周期。边界只针对该固定模板库与词形，不是29元不可达结论。

最新新增 one-tripling-stabilization（smoke/core/full），对应[一次三份复制定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_one_tripling_stabilization.md)和[结构图景审计](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_structural_picture_audit.md)。核验64个数字算子、312个完整系数基原子操作、1589个零和正规形、475个一般仿射轨道、790个完整归零操作，以及108个划分／控制器接口（最大N=1827，包含87元）。一般Hilbert90、平衡欧几里得与所有三整除维数结论由正文证明。原维数复制消去、29元及统一素数定理仍开放。

同一条目后续补充：237组一般q区间恒等式、386个q平均系数重放；n=29的副本宏有1624个三平均的完整系数重放；原维数平坦载体的35对六项Artin关系、18个原子交换及局部中心不交换边界。q平均重放不计作三平均原子操作。

最新新增 even-prime-power-halving 和 all-dimensions-prime-reduction（core/full），对应[总归约定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_all_dimensions_to_primes.md)：1536个完整二进模式、8448个核心桥，14项容量证书、33329个有限因子计划、699个70/110/130接口。一般公式与强归纳在正文承担无限量词。全部n>=7现严格归约到素数p>=7；所有23光滑维数已解，最小未解29。

整系数编译器的默认子问题库已固定为旧证书使用的版本，避免新增定理改变历史矩阵数量；新探索可用 `--current-library` 启用任意N>=9的三整除维数，以及素因子属于2、5、11、17、23、29、41或任意p=1 mod3的因子闭包。独立证明仍须核对每个实际调用域，不能仅凭当前目录自动接受模板。

最新新增 n25-complete（smoke/core/full）：18个只使用3/9/21元调用的通用模板、正向逆关系、七个整数词、30陪集与独立模25射影标签、唯一合法cusp、858个输送及446个核心桥。[25元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_twenty_five_arithmetic_complete.md)补齐了奇数因子归约的独立小基例。

odd-composite-factor-closure（core/full）对应[奇数合数闭包与35元证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_odd_composite_factor_closure.md)：5项奇数边界、4404个因子计划、943个多例外接口、2210个35元核心。一般容量与强归纳在正文给出。结合n25-complete，它完成已解奇素数的任意乘积和素数幂，可另乘任意五幂及三幂；91元因此也已完整解决，不依赖旧同余容器等式。

同一入口再核验2项二幂边界和1654个8整除因子计划，对应完整的8整除乘法族，允许任意五幂。条目名保留发现先后顺序；其精确范围以最新manifest与证明第11节为准。

重新复核其他AI的文件后，新增 other-ai-local-global-synthesis（core/full）、ai3-template-report-audit 和 ai5-synchronized-replica-audit（full）。[综合页](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_other_ai_local_global_review.md)列出全GL Zariski闭包的一般Lie证明、完整仿射理想、非零均值链接口及复制商的秩障碍。程序核对相应公式和原报告的有限结果；不据此宣称算术有限指数或一般复制消去。AI-4轨道表仅用三个生成元重算，未重跑深度8整矩阵库。

最新新增 prime-factor-carry-bridge（core/full），对应[素数优先与因子归约](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_prime_first_factor_reduction.md)：核验133组特殊族参数、1062个一般二例外核心、X49两步最短修复、复制加法闭包和176条准备词的3424个两列行签名。一般桥与最优性由符号证明给出；不能把它解读为任意输入的因子分解或完整49元定理。

modern frame 已[重写](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_unified_modern_framework.md)，完整原稿保留在 history/；使用边界见[严格化说明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_modern_framework_review_and_contract.md)。不把“统一框架”登记为已解决一般问题的计算证书。

最新新增 n23-complete（smoke/core/full）：15、17、24步固定原子宏、含2因子的真实标量逆词、七个整数生成元、24陪集与独立标签、属2及唯一合法cusp、1390个输送和928个桥实例。见[二十三元证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_twenty_three_arithmetic_complete.md)。三个关键宏已全部原子化，不调用十九元求解器。

同轮 n19-complete（smoke/core/full）核验七个通用十五元调用模板、显式仿射格恒等式、正向逆词、六个整数词、20陪集与独立模19标签、1374个输送和928个桥实例。见[十九元证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_nineteen_arithmetic_complete.md)。该定理依赖已证十五元判据；不把每次调用计为一个原子操作。

同时登记 bn-integer-template-compiler 和 prime-congruence-structure（core/full）：前者对照95个十七元矩阵并独立重放222个十九元、60个二十三元模板；后者核验素数稳定子、实际尺度周期及共同第一行的仿射恒等式。一般稳定子与周期结论来自[证明正文](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_prime_congruence_structure.md)，不由六个素数的样本外推。

此前 n17-complete（smoke/core/full）核验固定原子宏、正向逆元、18陪集、1366个输送和928个桥，见[十七元证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_seventeen_arithmetic_complete.md)。最小未解维数现为29。

另登记 b17-old-integral-return-audit（full）保留旧24词调度的净高度检查：一支处处增高，23支二次型不定。新完整证明不依赖这个旧控制器下降。下面的旧B17条目继续按其原库范围复现，不能将“旧库仍开放”误读成“十七元仍开放”。

最新新增 b17-universal-subproblem-lattice（core/full）：核对任意参数模判据的实现、五个新通用宏、1008个完整接口、684个合法输入的至多三步调度，以及范数3和 theta 分支恒等式。详见[参数无关调用与范数环面](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_universal_subproblem_lattice.md)。这是全部 B17 上的“可开启十五元调用”定理，不是全部 B17 终止定理。

同一入口还逐条重放630个固定原子词实例（各宏17／19步）、证明旧五宏加A的模3逆词障碍、重算48类完整调度和独立24词表，并核对最后十四元调用为整数严格下降。该下降只比较预备词之后的当前高度，不能解读为整个组合已经净下降。

同时补齐 b17-guarded-library-trap、b17-cross-stratum-escape、finite-orbit-method-boundary 三项（core/full）。前两项保留旧库无限陷阱、受限跨核桥和一个下降例子的独立证据；后一项核对大有限模像不推出有限指数。每个条目在清单中有明确证明边界。

b17-guarded-subproblem-experiment（full）记录首个框架应用：10个条件模板、136次局部接口重放、有界下降仍剩141个方向；不是十七元完整判据。subproblem-prime-obstruction（core/full）则有独立一般证明，排除缺失障碍素数时的统一有界调用次数。

新增 all-even-B-kernel-halving（core/full），核对 n=2 mod4 的8212个接口和4整除的5088个接口。对应[结构核减半定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_all_even_B_kernel_halving.md)，不能解读为任意偶维判据。二三光滑完整判据还使用单危险素数高维归约及归纳基。

新增 subproblem-prime-obstruction（core/full）：检查子块大小与 p 互素时，符号 B 核经归并词仍保留模p非零常值方向。一般任意长度的下界由[缺失素数定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_subproblem_prime_obstruction.md)给出；720步有限核验不作为无限外推。

最新增加 `two-three-smooth-complete`（core/full）：核验八元、十二元、十八元依赖，再检查统一减半的5524个加权接口。全部2^a3^b维数的无限归纳在[证明正文](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_two_three_smooth_complete.md)，不是最大测试维数27648的外推。

2026-09-10 新增 `blocker-graph-safe-core` 与 `n14-complete`（core/full）：一般 n-d-2 核心有独立图论证明，十四元余数桥则独立重放全部512类及两个具体例子，共514个十二元／B14接口。完整命令同时核验七、八、十二元依赖，详见[十四元证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_fourteen_complete.md)。三个代理的独立方向见[团队交接](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_team_handoff_2026-09-10.md)，未完成的报告不自动算作已验证定理。

最新新增 `n12-complete`，列入 smoke/core/full：四个真实宏、正向逆元、五个整数生成元、完整 12 陪集、独立模 8 标签、唯一合法尖点和六步终端。[十二元证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_twelve_arithmetic_complete.md) 的一般高维归约在正文中单独证明。另登记 `b12-six-step-local-branches` 和 `b12-return-frontier-certificates`；后者只重放发现缓存及核对浅层完整性，不替代完整定理。

进一步新增 n18-via-twelve-complete：调用已证十二元子问题，把 B18 及 \(2\cdot3^k\) 核压到偶重数状态，再用两份三幂网络归零。平均数分母、子问题合法性与配对后的零和性均在[一般证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_eighteen_via_twelve_complete.md)中明确列出。B21 默认改用[本原整数引擎](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_b21_integer_search_optimization.md)，结果和旧引擎对照一致。

最新加入 n15-via-subblocks-complete（core/full）与 even-kernel-halving（full）：前者重跑十二元、十元证书，再核验模8循环和2578个子问题接口；后者检查8212个偶维 B 核的八元减半接口。通用结论以[十五元证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_fifteen_via_subblocks_complete.md)和[偶维核减半桥](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_even_kernel_halving_bridge.md)中的符号论证为准。

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

外部“减少暴力搜索”建议的逐项判断，以及九十一元开放尖点的新并行入口，见 [搜索优化建议复核](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_search_optimization_review_2026-09-09.md)。

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
| `n7-n8-complete` | [七元与八元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_seven_eight_complete.md) | 七元精确射影实根覆盖；八元真实宏、欧几里得下降和终端路径 | `exact certificate: PASS`；`B8 Euclidean macro certificate: PASS` |
| `n10-complete` | [十元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_ten_complete.md) | 模 10 配对、四步桥、真实返回词和精确局部实覆盖 | `ten-point complete theorem certificate: PASS`；`terminal local-real cover: PASS` |
| `n11-complete` | [十一元完整判据](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_eleven_complete.md) | 安全组合、五步桥、返回词、221,184 个局部类和射影覆盖 | `eleven-point safety and bridge certificate: PASS`；`B11 exact projective-core certificate: PASS` |
| `n13-complete` | [十三元算术群证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_thirteen_arithmetic_complete.md) | 真实宏、正向逆元、56 陪集、尖点、终端和 $G$ 公式 | `finite modular folding: 56 complete cosets PASS`；`both legal cusps ... PASS` |

这些项目属于 `theorem-certificate`。它们精确闭合各证明中的有限枚举或宏证书；从任意合法输入下降到有限证书所覆盖情形的论证仍在对应文档中。

## 5. 一般维数结构

| ID | 文档 | 程序实际核对 | 明确边界 |
|---|---|---|---|
| `stabilization-theorem` | [复制稳定化定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_stabilization_theorem.md)、[勘误](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_research_corrections.md) | 2,288 个精确构造样本、显式运输矩阵、下界排除和反例修正 | 一般定理由文档中的构造证明；程序不证明原维数中的复制消去 |
| `power-partition-compression` | [三幂分块压缩](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_power_partition_reduction.md) | 3,542,820 个危险边模式和 2,310 个完整网络样本 | 不证明压缩后对数秩核都可达 |
| `general-lifting` | [一般维数综合](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_general_n_synthesis.md) | 有界公式、提升、同步划分和十元显式路径 | 有限样本不能推出任意 $n$ |
| `zero-padding` | [零填充定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_zero_padding_theorem.md) | $3\le n<100$ 的 9,700 个精确网络样本 | 一般递归证明在文档中 |
| `burau-power-chain` | [Burau 幂链定理](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_burau_power_chain.md) | $3\le t\le8$、$s=3,9$ 的十二组精确关系和正向逆元 | 任意秩证明在文档中；链间耦合仍开放 |
| `power-block-macro` | [三幂块返回宏](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_power_block_macro.md) | $1\le k\le5$ 的真实平均重放 | 任意 $k$ 依靠归纳证明 |
| `cyclotomic-macros` | [十三元证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_thirteen_arithmetic_complete.md)、[Burau 幂链](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_burau_power_chain.md) | $s=3,9,27$ 的真实宏和矩阵恒等式 | 不证明真实宏群等于一般算术候选群 |

`isolated-prime-core`、`multi-prime-core` 和 `arithmetic-geometry-structure` 也登记在清单中，但属于支持性有限实验。它们适合检查公式或寻找反例，不能单独引用为任意维数定理。

## 6. 九十一元必须分成三层

九十一元最容易发生证据越界，必须区分：

1. `n91-congruence-container`：`cyclotomic_congruence.py` 精确得到含模 8 条件的已知容器。输出为 21,504 个标签、96 个尖点和 24 个合法尖点。它不证明真实宏群等于该容器。
2. `n91-corrected-witness`：`search_n91_missing_class.py` 验证 $(u,v)=(1,-3)$ 时单独坐标为 $-54$，并给出两步到 27 元零和块的真实证书。它只处理一个代表。
3. `n91-cusp-depth4`：`analyze_n91_terminal_cusps.py --depth 4` 在容器的 24 个合法尖点中覆盖 23 个。深度 3 时开放的尖点 30、32、35 已找到四步证书，只剩尖点 29 为 `OPEN`。这个标记表示深度 4 内未找到证书，并不表示不可达。
4. `n91-cusp29-depth5`：对 `cusp 29 = (-13,18)` 使用 `--cusp 29 --depth 5 --jobs 8 --split-depth 2`，得到五步终端证书；已知容器的有限深度覆盖因此达到 `24/24`。它仍是探索性有限搜索。

脚本默认 `--depth 2`，输出 `covered legal cusps 14 / 24`；深度 3 输出 `20 / 24`；深度 4 输出 `23 / 24`；单独的 cusp 29 深度 5 输出 `covered requested cusps 1 / 1`。整数子集和 DP 与八进程优化后，深度 3 从 540.794 秒降至 6.322 秒，深度 4 从 117.891 秒降至当前约 14.2 秒；新的存在性优先 DP 下，cusp 29 深度 4 约 6.2 秒、深度 5 约 272.8 秒。详见 [计算性能审计](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_computation_performance_audit.md)。

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

各新命令可用 `python work/run_verifications.py --id ID` 独立运行；`full` 还包含 B21 的较长有限搜索，总时间随并行负载变化，旧的约 6 分钟仅是加入这些条目前的估计。详见 [audit 修订记录](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_audit_resolution_2026-09-09.md) 和 [四核比较](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_single_prime_kernel_comparison.md)。

## 8. 本次审计发现并修正的复现问题

1. 九十一元覆盖数现在与搜索深度绑定：默认深度 2 为 `14/24`，深度 3 为 `20/24`，深度 4 为 `23/24`；单独搜索 cusp 29 的深度 5 已得到最后一条证书，清单同时保留深度 4 全量命令和深度 5 定向命令。
2. [三幂分块压缩](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_power_partition_reduction.md) 曾记录 1,055,056 个危险边模式，而当前脚本实际稳定输出 3,542,820；文档已按当前程序修正。
3. 总纲原来只列关键脚本名，未说明一项证明可能依赖多个程序，也未区分精确证书、有限实验和开放搜索；现在以机器清单为唯一运行索引。

后续每次修改验证程序时，应让预期输出变化导致统一运行器失败，并同步更新清单与对应数学文档。这样“脚本变了但旧数字仍留在论文中”的偏差会在复核时直接暴露。

新增 shape-changing-integer-potential：形状变化整数检查点势。整数检查点记录 E=sum x_i^2；已有两步重叠造零和碰撞增大背景公式作为局部宏实例。此条是框架整理，不宣称全局宏存在性或 N(p)<=3p。

shape-potential-literature-interface 已转为支持材料；修正2006计数公式及适用含义，加入Balandraud定理和已读勘误。不以打印成功消息充当证书。

旧 single-value-zero-sum-conjecture 已被 p=13、0^32 1^4 2^4 否定；现有核验改检查反例、最优界 N-floor((p-1)/3) 和三步极端族，不再使用打印占位命令。

EGZ截断分类已更正：对任意 N>=2p-1，无混合p项零和时，至多两个重桶；双重桶覆盖全池，单重桶外的至多p-1个例外必须零和自由。

撤回不必要的 N<4p 上限；正确分类对任意 N>=2p-1 成立。

<!-- END SOURCE doc-a3f6cc35dedf -->

---

<a id="doc-8f054d573887"></a>

## 原文导签：危险素数的见证重置：局部约分为何必须纳入一般算法

来源：`work/document_reorganization_20260915/originals/outputs/triple_average_witness_reset_lemma.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_witness_reset_lemma.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-8f054d573887 -->
# 危险素数的见证重置：局部约分为何必须纳入一般算法

> **复核修正：** 以下重置引理仅在中心化状态的主余类本来就是 $0\pmod p$ 时保持目标为零。平移主余类后必须同时跟踪目标平均值，不能对未中心化商状态直接使用 $G$ 判据。精确区分及七元反例见 [研究勘误](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_research_corrections.md)。

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

在 [覆盖设计障碍](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_covering_design_obstruction.md) 的显式五例外构造中，每个危险素数 (p_F) 的非主类支持集正是 (F)。所有模 (3) 零和三元组都包含某个 (F)，所以它们都不是“见证保持安全”操作；但选中 (F) 后满足本引理，输出有一个可约去的 (p_F) 因子。

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

<!-- END SOURCE doc-8f054d573887 -->

---

<a id="doc-c2db819c6d1f"></a>

## 原文导签：可填充三幂块的统一收尾

来源：`work/document_reorganization_20260915/originals/outputs/triple_average_zero_padding_theorem.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_zero_padding_theorem.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-c2db819c6d1f -->
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


<!-- END SOURCE doc-c2db819c6d1f -->

---

<a id="doc-15662833ecca"></a>

## 原文导签：统一四／六阶控制器完成2、3奇次幂临界点

来源：`work/document_reorganization_20260915/originals/outputs/two_three_odd_power_critical_grh_completion.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/two_three_odd_power_critical_grh_completion.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-15662833ecca -->
# 统一四／六阶控制器完成2、3奇次幂临界点

日期：2026-09-15。按用户要求继续在Dirichlet L函数GRH下推进；不研究去掉GRH的常数问题。

## 1. 完整结果

**定理（GRH）。** 设m属于{2,3}、s>=2为任意整数，令
\[
k=ms^2,\quad r=ms,\quad n=k+r+1.
\]
任意n个有理输入经有限原位置k平均可达全等，当且仅当非全等输入的本原中心化G=1。

这里gcd(k,n)=1，所以G=1恰为一般rad(G)|k判据。s不必为素数幂；这是两个完整的参数族。

取s=p^a、m=p属于{2,3}，便得到
\[
\boxed{M(p^{2a+1})=H(p^{2a+1})=p^{2a+1}+p^{a+1}+1
\quad(a\ge1,\ p=2,3).}
\]
结合已证素数情形和[平方族](../sources/work/document_reorganization_20260915/originals/outputs/general_k_grh_stage_and_remaining_tasks_20260915.md)，**2的每个幂、3的每个幂的最早临界点现在均已完成**。p=2、a=0的自动点为M(2)=4、H(2)=5，单独沿用二平均结果。本文不证明这些元数的最终阈值N。

本轮直接读平方控制器、旧八平均十三元周期、统一端点控制器和素数最终独立审核；后者关于新增倍率需显式扩环的提醒同样用于本证明。未做平均词搜索。

## 2. 统一宏与新增的两步恒等式

使用全系统核心
\[
K(u,v)=(u^k,v^r,-ku-rv),\qquad(x,y)=(u,u-v).
\]
本原合法性为gcd(x,y)=gcd(y,n)=1。已有三个实际一步宏为
\[
\mathcal A=\begin{pmatrix}1&-1/s\\0&-1/s\end{pmatrix},\quad
\mathcal B=k^{-1}\begin{pmatrix}-r-1&r\\-n&k+r\end{pmatrix},\quad
\mathcal C=k^{-1}C,
\quad C=\begin{pmatrix}-r-1&1\\-n&1\end{pmatrix}.
\]
原位置选组分别为u^(k-r)v^r、u^(k-1)w、u^(k-r)v^(r-1)w，w=-ku-rv。

因为r²=mk，特征多项式给
\[
m=2:\ C^4=-k^2I;\qquad m=3:\ C^6=-k^3I.
\]
恢复实际尺度后分别为-k^-2 I和-k^-3 I，所以C及逆均正向存在。

精确有C^-1 B=Sigma，其中Sigma=(1,-1;0,-1)。因此Sigma是真实返回的乘积，且Sigma²=I；不能免费交换不等大小块。

对每个1<=d<=r，先平均
\[
(u^{k-r+d-1},v^{r-d},w),
\]
得到k份D；保留r份D为新r块，再留一份未参与的旧u作单点，平均其余k份。这是两个真实原子。计数成立，因为首步外有r-d+1>=1份旧u。

所得实际矩阵为k^-2乘
\[
M_d=\begin{pmatrix}r^2+r-k&-rd\\rn&-(r+k)d\end{pmatrix}.
\]
关键恒等式是
\[
\boxed{M_d=C^2\Delta(d),\qquad\Delta(d)=\operatorname{diag}(1,d).}
\tag{2.1}
\]
所以C的正向逆直接给全部正向Delta(d)、1<=d<=r；同时Sigma mathcal A=Delta(1/s)。特别Delta(s)和Delta(1/s)都可执行。

这取代了把八平均特殊短词(A²C²)³逐参数推广的做法。

## 3. 初始深层以及允许素数的反演

置R0=Z[1/s]、h=s-1。Sigma与Delta(s)交换子给U((s-1)/s)，正逆共轭提供U(hR0)。

取P=(e1,Ce1)=(1,-r-1;0,-n)，则
\[
P^{-1}U(a)P=U(-na),\qquad
P^{-1}C U(ka)C^{-1}P=L(na).
\]
无需先反演k：取ka清分母。Morris／Serre深同余引理及换基账本给
\[
\Gamma(h^2n^3,R_0).
\tag{3.1}
\]
s>=2保证R0有无限单位。

还须获得Delta(m)^-1，不能把k的全部素因子预先算作实际共轭倍率：

- m|s时，Delta(s)^-1 Delta(s/m)=Delta(1/m)，两项均实际存在。
- m不整除s(s-1)时，m与(3.1)的level互素，安全整数返回取逆引理适用。
- m|(s-1)时，定义
  \[
  H_m=(mk)^{-1}\Delta(m)C^2\Delta(m)
  =\begin{pmatrix}
  ((m-1)s+1)/(ms)&-1/s\\n/s&-m(s+1)/s
  \end{pmatrix}.
  \]
  因s=1模m，左上分子的m可整除，故H_m属于SL2(R0)。它正向存在，有限逆提升给H_m^-1，而
  \[
  C^2\Delta(m)H_m^{-1}=mk\Delta(1/m)
  \]
  提供真实射影逆。

通过上述倍率的双向共轭扩环到Z[1/(ms)]，重新应用同样的双向根及换基引理，保持(3.1)的level。没有免费反演危险素数，因为gcd(ms,n)=1。

## 4. 全部参数都能反演2，重新交换后得到完整根

m=2时已经完成；m=3且s偶时，同样由Delta(s)^-1 Delta(s/2)得到Delta(1/2)。

余下m=3、s奇。C^4的行列式为k^4且左上项为k(k+r)，于是
\[
H_2=(2k^2)^{-1}\Delta(2)C^4\Delta(2)
=\begin{pmatrix}(s+1)/(2s)&-1/s\\n/s&-4-2/s\end{pmatrix}.
\]
s奇保证H2属于SL2(Z[1/(3s)])；它正向存在，有限逆提升后有
\[
C^4\Delta(2)H_2^{-1}=2k^2\Delta(1/2).
\]
由此统一取得Delta(2)及逆。与Sigma重新取交换子，
\[
\Sigma\Delta(2)\Sigma\Delta(1/2)=U(1/2).
\]
在R=Z[1/(2ms)]上已有全部U(R)，再用
\[
U(-1)\mathcal C\Delta(k)=L(-n/k)
\]
得到全部L(nR)。符号Delta(-1)=Sigma U(1)也可执行。

已证Gamma1生成引理在R上给Gamma1(n,R)。对每个1<=d<=r且gcd(d,n)=1，(2.1)的Delta(d)可由Gamma(n,R)激活逆，扩环到所有不大于r的安全素数。根通过共轭同步扩张，Gamma1引理在扩大的最终环上重新适用。

## 5. 全输入入口没有失效素数

只需把[平方入口](../sources/work/document_reorganization_20260915/originals/outputs/general_k_plan_review_and_square_entry_20260915.md)的单块交换子用于本组参数。n=k+r+1且r>=4，有2^(r+1)>n，故omega(n)<=r；保护一个基准和每个危险素数的一处见证后，仍可先建立一个k重块，外面有r+1个单点。

交换子系数为(k-1)/k。若g整除k-1和n，则g整除r+2。又
\[
m(k-1)-(r-2)(r+2)=4-m.
\]
m=3时g=1；m=2时g|2而k-1奇，所以也有
\[
\boxed{\gcd(k-1,n)=1.}
\]
因此所有危险素数都可用同一个三角色交换子转移。选择目标单点，按CRT正次数幂逐一集中全部见证；模意义逆由有限阶的正向幂实现。

最后保留目标w及r份旧a，平均其余k份，得到(u^k,v^r,w)。差为u-v=(a-w)/k模n，在每个危险素数处均非零。入口有限、原位置、全输入成立。

## 6. GRH尺度和小参数

第4节已实际提供全部不大于r的安全素数单位。若
\[
r=ms\ge3(\log(ms^2+ms+1))^2,
\]
GRH小非剩余界保证这些单位生成模n的完整单位群。

该不等式对m=2、3和全部s>=256成立。s=256时两者n<2^18，故3(log n)²<3(18·0.7)²<512<=r。此后f(s)=3(log(ms²+ms+1))²满足f(s)/s递减：n'/n<2/s，且log n>4，直接求导即可。

剩余m=2、3，2<=s<256共508组是完整有限参数集合。本次用已有有限阿贝尔商秩方法检验所有素数指数商，全部小单位像满射，见[完整证书](../work/two_three_square_multiple_small_units.json)。另外保留11组素数奇次幂的小参数专用证书作为较短复核接口。不是有限高度输入测试。

对本原合法(x,y)，按单位像选epsilon=y模n，再以真实对角校正和Gamma1中的Bezout矩阵送到(0,1)。终端为(0^k,(-1)^r,r)，因r+1<=k，取r份-1、单点r及k-r-1份零，一次平均全零。

这样入口、完整根、尺度及终端已经闭合，主定理得证。

## 7. 范围、证据及剩余

本定理包括混合平方倍数，如12平均19元、18平均25元、50平均61元；不宣称它们都在自己的最优边界。最优性只在m=p、s=p^a时由旧S(k)下界直接匹配。

[精确核验](../work/verify_two_three_odd_prime_power_critical.py)检查24组素数奇次幂的通用恒等式、32条原位置周期与两步倍率返回、两个强制使用见证转移的入口、11组专用小单位证书及508组完整小s单位证书。一般量词由本文推导承担，未枚举平均词；GRH及Morris／Serre均按已记录文献依赖使用。

一般p>=5的高奇次幂、其余混合元数的真正临界点和全部后续维数仍须继续。本文没有将部分主任务标成已全部完成。

<!-- END SOURCE doc-15662833ecca -->

---

<a id="doc-aa89bc3963b9"></a>

## 原文导签：临界双块系统的统一正向控制器：不再搜索种子周期

来源：`work/document_reorganization_20260915/originals/outputs/uniform_endpoint_positive_controller.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/uniform_endpoint_positive_controller.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-aa89bc3963b9 -->
# 临界双块系统的统一正向控制器：不再搜索种子周期

2026-09-15完整端点后续：[无条件入口与全输入证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unrestricted_endpoint_and_odd_band.md)已将本页控制器和任意核心同余闭合接成所有奇p>=3的2p+1全输入G=1判据，素因子数、指数和Theta条件均不再需要。下文一般入口开放的表述属于历史阶段；一般最终阈值仍未证明。

2026-09-14后续：[同余闭合证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)已借助Morris有限指数定理和Serre强同余子群性质，将本页正向资源扩展为任意合数level的整数Gamma0包含，全部合法核心可归零。六素因子或Theta(n)<1入口范围均得到完整端点判据；一般入口与后续维数仍独立开放。下文“合数核心尚未覆盖”属于原稿阶段。

日期：2026-09-12。

**同日后续：** [七平均十五元完整证明](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_fifteen_complete.md)在本页已有正向种子的基础上补齐了多素数level15：一般至多两素数端点有三步合法入口，模15的完整24陪集回路只需二进根和两种Gauss主元。本文后面“十五元仍未解决”描述旧阶段；一般多素数level的完整覆盖仍开放。

**进一步推广：** [统一CRT回路证书](../sources/work/document_reorganization_20260915/originals/outputs/composite_endpoint_crt_transfer.md)已经覆盖36个指定合数level，不再逐个手列新种子；28个两素因子level同时具有完整输入入口。任意level的全称根群包含仍是独立的代数猜想。

这里 p 表示一次平均的位置数，q=2p+1 表示总位置数。
本页统一三平均七元、五平均十一元的控制器，并解决此前未证明的一般正向种子存在性。
证明中的整数递推有显式规则和终止证明，不搜索原子词、有限周期或输入路径。

## 1. 已证明的范围

**定理 A（统一原位置控制器）。** 设 p>=3 为奇整数，q=2p+1，

\[
K_p(a,b)=(a^p,b^p,-p(a+b)),\qquad
R_q=\mathbb Z[1/\ell:\ell\le p\text{ 为素数且 }\ell\nmid q].
\]

在原 q 个位置上，p 平均及两个常值块的账本重标记可以正向实现

\[
\boxed{U(R_q),\quad L(qR_q),\quad\Delta(R_q^\times)}
\tag{1}
\]

的射影作用。所用的每个基本返回都在整个合法 K_p 域上保持合法性。
所有形式逆都有明确的正向实现。

这里 U(t)=[[1,t],[0,1]]、L(t)=[[1,0],[t,1]]、Delta(t)=diag(1,t)，
参数坐标为 (x,y)=(a,a-b)。合法性是本原参数满足 gcd(y,q)=1。

**定理 B（素数维数的完整端点）。** 若 q=2p+1 还是素数，则任意 q 个有理数，经中心化、清分母及本原化得到非零整数状态 X 后，

\[
\boxed{X\text{ 可经有限次 }p\text{ 平均归零}\iff G(X)=1.}
\tag{2}
\]

全等输入单独显然可达。特别地，(p,n)=(3,7),(5,11),(11,23),(23,47),(29,59),(41,83) 等都由同一证明覆盖。
定理甚至不要求平均元数 p 本身为素数；本页只用到 p 为奇数。

**尚未证明：** 当 q 为合数时，任意合法输入的完整端点结论。
定理 A 仍成立，但本页不声称一般合数 level 的完整 Gamma_0(q) 包含，也不声称任意输入必能安全进入 K_p。
例如七平均十五元仍不能据本页宣布全部解决。
另外，单独解决 n=2p+1 也不等于解决所有 n>=2p+1。

## 2. 两种返回都有直接的原位置实现

### 2.1 更换单点的返回

对 1<=j<=p，依次平均

\[
(a^{j-1},b^{p-j},-p(a+b)),\qquad(a^{p-j},b^j).
\]

两组选取的位置不交；剩余一个原 a 位置作为新单点。
输出的两个 p 重值为

\[
c=-\frac{(p+1-j)a+jb}{p},\qquad
d=\frac{(p-j)a+jb}{p},\qquad -p(c+d)=a.
\]

因此，在 (x,y)=(a,a-b) 坐标中，真实矩阵为 T_j/p，其中

\[
T_j=\begin{pmatrix}-(p+1)&j\\-q&2j\end{pmatrix},
\qquad\det T_j=-j.
\tag{3}
\]

交换两个块的名称记为

\[
\Sigma=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
\tag{4}
\]

Sigma 只更新原位置账本，不是假设可以额外置换实际数值。

### 2.2 保留单点的返回

对奇整数 r，|r|<=p，令 k=(p+r)/2。
保留单点，依次平均两个不交组

\[
(a^k,b^{p-k}),\qquad(a^{p-k},b^k).
\]

这同样回到 K_p，真实矩阵恰为

\[
F_r=\begin{pmatrix}1&(r-p)/(2p)\\0&r/p\end{pmatrix}.
\tag{5}
\]

F_{-r}=Sigma F_r；F_p 是恒等返回。
这一族是本次补充的资源。仅使用旧的 T_j 短周期表，不会自动看到下面的统一构造。

### 2.3 合法域与共同尺度

本原整数参数有

\[
G(K_p(a,b))=\gcd(a-b,q).
\]

对每个素数 l|q，只采用 gcd(j,q)=1 的 T_j 和 gcd(r,q)=1 的 F_r。
其行列式在模 l 下可逆，且 y 分别乘以 2j/p、r/p，因此保持 y 的 l 进单位性质。
参数约去公因子不会改变这一结论，因为模 l 的向量始终非零。

下文每次使用的 j、r 都满足这些限制。q 为合数时也不使用危险返回。

所有“逆”和“根”均指实际正向词所实现的非零共同缩放下的射影作用。
并不额外执行放大、除法或其他元数的平均。真实坐标的分母始终只含 p 的素因子。

## 3. 两个不依赖搜索的正向逆引理

**标量周期引理。** 若可执行正词 W 的矩阵满足 W^m=lambda I，lambda!=0，则 W 有正向射影逆。
循环旋转该标量词，还能给其中每个字母构造正向逆。
例如 (AB)^2=lambda I 时，A 的逆可取 BAB，B 的逆可取 ABA。

**仿射配对引理。** 设 A、B 都可正向执行，且 AB=U(t)。因为

\[
\Sigma U(t)\Sigma=U(-t),
\]

AB 的逆也可正向执行。于是

\[
A^{-1}=B(\Sigma AB\Sigma),\qquad
B^{-1}=(\Sigma AB\Sigma)A.
\tag{6}
\]

所以两个上三角操作只要倍率互为倒数，就同时获得正向逆。
无需预先假设其中任何一个可逆。

这些公式允许我们使用较长的确定性词，代替“等待某个短词恰好有有限阶”。

## 4. 每个奇数 p 都有第一组正向逆

令 h=(p+1)/2，J=T_h。由 Cayley--Hamilton 恒等式，

\[
\boxed{J^2=hI.}
\tag{7}
\]

因此 J 无条件正向可逆，并且

\[
J^{-1}T_j=\Delta(j/h).
\tag{8}
\]

先不要把右侧任意 Delta(j/h) 当作可逆；目前 (8) 只证明正向存在。

定义

\[
\epsilon=\begin{cases}1&p\equiv1\pmod4,\\-1&p\equiv3\pmod4,\end{cases}
\qquad a_0=\frac{q+\epsilon p}{4}.
\]

此时 a_0 是 1 至 p 中的整数，且 gcd(a_0,q)=1。
直接计算得到一般迹公式

\[
\operatorname{tr}(T_aF_r)=\frac{(4a-q)r-p}{2p}.
\tag{9}
\]

代入 a=a_0、r=epsilon，便有

\[
\boxed{(T_{a_0}F_\epsilon)^2=\frac{a_0\epsilon}{p}I.}
\tag{10}
\]

所以 T_{a_0}、F_epsilon 都正向可逆。结合 F_{-1}=Sigma F_1，得到 F_1 的正向逆。
上述矩阵恒等式中每个 T 的实际共同因子 1/p，展开成原子词时一并保留；所有标量仍非零。

记

\[
C_r=F_rF_1^{-1}
=\begin{pmatrix}1&(r-1)/2\\0&r\end{pmatrix}
\tag{11}
\]

对奇数 |r|<=p、gcd(r,q)=1 正向存在。
C_rC_s=C_{rs}，C_{-1}=Sigma。
这里 C_r 的普遍正向存在，仍不等于普遍可逆。

## 5. 先使倍率 h 可逆

Delta(1/h)=J^{-1}T_1 已正向存在。

若 h 为奇数，C_h 正向存在，且 Delta(1/h)C_h 为上根。
由仿射配对引理，两者都可逆。因此 Delta(h) 可逆。

若 h 为偶数，则 p=3 mod 4，a_0=h/2。
式 (10) 已给出 T_{h/2} 的逆，所以

\[
\Delta(1/2)=J^{-1}T_{h/2}
\]

已经可逆。记其逆为 Delta(2)。于是

\[
\Sigma\Delta(2)\Sigma\Delta(2)^{-1}=U(1/2),
\qquad C_2=U(1/2)\Delta(2)
\tag{12}
\]

均可逆。写 h=2^v r，其中 r 为奇数。C_r 正向存在，故 C_h=C_2^v C_r 正向存在。
再次把 C_h 与 Delta(1/h) 配对，得到 Delta(h) 的正向逆。

至此两种情形都已证明 Delta(h) 可逆。特别地 T_1=J Delta(1/h) 也可逆。
对每个安全的 1<=j<=p，

\[
\Delta(j)=J^{-1}T_j\Delta(h)
\tag{13}
\]

正向存在。h 偶数时 Delta(2) 的逆也已经解决。

## 6. h 为奇数时，一个必终止的整数链提供倍率 2

现在处理剩下的 h 奇数情形。初始 C_1=I 可逆。

假设 1<=r<=p 为奇数，gcd(r,q)=1，且 C_r 已经可逆。
取

\[
d=\begin{cases}r&r\equiv1\pmod4,\\-r&r\equiv3\pmod4,\end{cases}
\qquad j=\frac{q+d}{4}.
\tag{14}
\]

有 1<=j<=p，且 gcd(j,q)=1。C_d 的逆由 C_r 的逆及 Sigma 给出。

为看清周期，暂换到 (s,y)=(a+b,a-b) 坐标：

\[
T_j=\frac12\begin{pmatrix}-1&-1\\-q&d\end{pmatrix},
\qquad C_{1/d}=\operatorname{diag}(1,1/d).
\]

所以

\[
\boxed{(T_jC_{1/d})^2=\frac jd I.}
\tag{15}
\]

周期中的 C_{1/d} 已有正向实现；由标量周期引理，T_j 获得正向逆。
结合 (13)，Delta(j) 也可逆。

- 若 j 为偶数，Delta(j/2) 已由 (13) 正向存在。因此 Delta(j)^{-1}Delta(j/2)=Delta(1/2) 正向存在，给出 Delta(2) 的逆，过程结束。
- 若 j 为奇数，C_j 正向存在。把 Delta(j)^{-1} 与 C_j 用仿射配对引理组合，得到 C_j 的正向逆；置 r=j，继续。

**终止证明。** 在奇数集合 {1,3,...,p} 上定义 f(r)=(q+d)/4。
该函数在奇数输入上单射：相同输出迫使带符号的 d 相同，进而 r 相同。
并且

\[
\frac{p+1}{4}\le f(r)\le\frac{3p+1}{4}.
\]

h 奇数时 p>=5，所以 f(r)>1；1 没有前驱。
从 r=1 出发，若一直得到奇数，有限性必迫使重复。
单射性逐步追溯会迫使 1 也有前驱，矛盾。
因此至多 (p+1)/2 次更新必然遇到偶数。

这是一条有限集合上的确定性递推，不是平均词搜索。每个更新的正向逆由 (15) 直接给出。

例如：

\[
\begin{array}{c|c}
p&\text{从 1 出发，直到首次得到偶数}\\\hline
5&1\longrightarrow3\longrightarrow2\\
17&1\longrightarrow9\longrightarrow11\longrightarrow6\\
97&1\longrightarrow49\longrightarrow61\longrightarrow64
\end{array}
\]

p=3 则属于上一节的 h 偶数情形，直接取得倍率 2。

**结论：每个奇数 p>=3 都已经无条件得到正向可逆的 Delta(2)、Delta(h)。**

## 7. 两个单位根由同一恒等式产生

由 (12) 得到 U(1/2)，平方得到 U(1)，并且

\[
\Delta(-1)=\Sigma U(1).
\]

J 的统一下根公式为

\[
\boxed{J\,U(1/2)\,\Delta(-4h)=-2h\,L\!\left(\frac{q}{2h}\right).}
\tag{16}
\]

所有左侧因子都已经可逆且正向可执行。
再用 Delta(2h) 共轭，得到 L(q) 及其逆。

因此

\[
\boxed{U(1),\quad L(q)}
\tag{17}
\]

是每个奇数平均元数的统一正向单位根，不再依赖 3、5 的特殊短周期。
上根没有遗留的固定公因子；下根恰好带合法域要求的 q。

## 8. 欧拉同余统一替代其余所有周期搜索

取任意 1<=j<=p 且 gcd(j,q)=1。Delta(j) 已正向存在。
令 e=phi(q)、t=j^e，则 t=1 mod q。
由 (17)，U(1)、L(t-1)=L(q)^{(t-1)/q} 都已可逆且正向存在。

直接相乘得

\[
W_j=\Delta(-t)U(1)L(t-1)
=\begin{pmatrix}t&1\\-t(t-1)&-t\end{pmatrix},
\]

\[
\boxed{W_j^2=tI.}
\tag{18}
\]

其中 Delta(-t)=Delta(-1)Delta(j)^e 是正词。
式 (18) 是包含 Delta(j) 的正向标量循环，故为 Delta(j) 提供正向逆。

这只使用欧拉定理和一个迹零恒等式。
不需要短周期存在性猜想，也不需计算或猜测有限模群的大小。
q 合数时仅对与 q 互素的 j 使用它，完全符合安全域。

每个不超过 p 且不整除 q 的素数都已成为可逆对角倍率。
用整数幂、逆及

\[
\Delta(d)U(t)\Delta(d)^{-1}=U(t/d),\qquad
\Delta(d)L(t)\Delta(d)^{-1}=L(dt),
\]

即可得到 (1)。定理 A 证毕。

## 9. q 为素数时的完整同余群与全部输入

此时 R_q=Z[1/p!]，所有 1<=j<=p 都安全。
Gamma_0(q) 在 PSL_2(Z) 中的完整右陪集可取

\[
I,\qquad \mathsf S\mathsf T^j\quad(-p\le j\le p),
\qquad
\mathsf S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad\mathsf T=U(1).
\]

其底行分别给出 [0:1] 与 [1:j]，共 q+1 个标签。
非平凡 Schreier 回路由 U(1)、L(-q)，以及

\[
g_j=\begin{pmatrix}-k&-1\\jk+1&j\end{pmatrix},\quad
0<|j|\le p,\quad k\equiv-j^{-1}\pmod q,\quad0<|k|\le p
\]

组成。每个回路都有精确分解

\[
g_j=L\!\left(-\frac{jk+1}{k}\right)
\operatorname{diag}(-k,-1/k)U(1/k).
\tag{19}
\]

k 是 R_q 的单位；jk+1 被 q 整除；中间因子射影等于 Delta(1/k^2)。
因此定理 A 正向实现全部回路，Schreier 定理给出完整 Gamma_0(q) 包含。
这里的标准模群矩阵 S 只用于证明生成定理，并没有被当成自由物理操作。

对本原整数参数 (x,y)，q 不整除 y。先取 alpha*x+beta*y=1，再调整

\[
\alpha\gets\alpha+ky,\qquad\beta\gets\beta-kx
\]

使 q 整除 alpha。于是

\[
H=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}\in\Gamma_0(q),
\qquad H(x,y)^T=(0,1)^T.
\]

因此所有合法 K_p 参数都正向到达某个 K_p(0,s)，s!=0。
先平均单点 -ps 和 p-1 个零，得到 (s^p,(-s)^p,0)。
再依次平均

\[
(s^{(p-1)/2},(-s)^{(p-1)/2},0),\quad
(s^{(p-1)/2},(-s)^{(p-1)/2},0),\quad
(s,-s,0^{p-2}),
\]

四次原子平均完成终端。

最后补全入口：对任意合法整数零和 q 元输入，保留单点 c，把其余位置分成两个 p 元组。
一组和为 S，则平均后块差为 (2S+c)/p。
若 2S+c=0 mod q，两个组间必有模 q 不同的 x、y；否则原输入模 q 全同余。
交换这两个位置在划分中的归属，令 2S+c 改变 2(y-x)，就修复为合法划分。
实际只执行修复后两个不交组的 p 平均。

必要性由 G|q 及非零共同模 q 余数在 p 平均下保持得到。
这证明定理 B；无界参数覆盖来自群包含、Bezout 和入口，有限程序样本不承担这个量词。

## 10. 与旧种子路线的关系，以及合数端点的边界

旧三平均大维数路线的困难是：统一目标矩阵未证明能在原位置实现，或已实现宏的正向逆仍只能逐个寻找。
本页的 T_j、F_r 从开始就是原 q 个位置上的两步分组操作。
式 (10)、整数链 (14)、单位根 (16)、欧拉周期 (18) 共同闭合了正向逆和根的存在性。
因此这里已经实际证明了以前缺失的部分，并非再把同一个缺口改名。

真正通用的结构是：两种保留方式产生两个上三角倍率族；互补倍率配对提供逆；
一个必碰到偶数的有限整数链激活倍率 2；两个单位根随后把有限同余周期提升为精确正向周期。

q 合数时，定理 A 已解决上述种子问题，但还有两个未在本页闭合的接口：

1. 本页的 q+1 个 Schreier 代表只适用于 q 为素数。合数 q 的 P^1(Z/qZ) 有其他标签，不能直接照搬第 9 节声称完整 Gamma_0(q) 或全部合法轨道覆盖。
2. 任意合法输入的直接 (p,p,1) 两组入口可能失败。已有 K4/CRT 反例仍有效；允许更多预备平均后的入口尚需证明。

具体的直接分组反例在 p=217717、q=435435 存在：

\[
(1^{435429},2641,8295,82447,342056,435436,-1306304).
\]

该输入本原、零和、G=1，但每个直接 (p,p,1) 划分都会损失某个非 p 模见证。
这不证明它不可达；只说明全体合数端点仍需额外的原位置准备机制。

下一步应把“合数 level 的核轨道”和“核外入口”分别证明，不能退回逐 p 搜索种子。
从本页也不能宣布 N(p)=2p+1，因为端点之后的维数带仍有独立问题。

## 11. 核验方式与计算边界

独立核验器 `work/verify_uniform_endpoint_controller.py` 不调用发现程序或其他平均求解器。
正向词以无环乘积图保存，重复节点共享，大整数幂用二进制重复平方。
不会把欧拉指数所产生的巨大原子词逐字展开后再验证矩阵。

每个叶节点都是带原位置账本的 T_j、F_r 或零成本块重标记。
每次补逆均核对精确有理射影矩阵；依赖只指向已存在节点，因此不会把尚未获得的形式逆偷渡进构造。
小参数样本另用不做本原化的 Fraction 坐标，逐次执行真实平均直到全零。

核验覆盖所有奇数 p=3,5,...,43，并加入 53、73、97、127，含素数和合数 q。
有限检查用于核对公式、符号、适用域、无环依赖和位置重数；一般量词由正文各引理证明。

本次通过：984 组双基输入的真实返回重放，25 个平均元数的公式种子与终止链，
418 个可逆对角倍率，528 个素数 level 的完整 Schreier 回路及 1656 条生成元转移，
10 条逐位置 Fraction 完整归零路径，最长 2466 次原子平均。全部核验约需数秒。

本页不承诺最短路径、位长多项式的原子输出长度、统一的一位额外 p 进精度，或所有合数端点已解。
项目入口：`python work/run_verifications.py --id uniform-endpoint-controller`。

<!-- END SOURCE doc-aa89bc3963b9 -->

---

<a id="doc-ec386797a9bf"></a>

## 原文导签：`work/` 使用说明

来源：`work/document_reorganization_20260915/originals/work/README.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/work/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ec386797a9bf -->
# `work/` 使用说明

无条件端点入口核验：unrestricted-endpoint-entry，对应[完整端点及全部奇数下半带](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unrestricted_endpoint_and_odd_band.md)。79组有理交换子、1965组有限模正向编译、28条逐位置入口和16条完整核心归约均通过；另以压缩账本跨过七素因子覆盖例及旧r<omega(n)入口缺口。程序不搜索平均词，不展开巨大群论归零尾部；完整定理由新入口与已有核心证明连接承担。

内部偶余量核验：even-interior-completion，对应[内部偶余量完整证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_interior_completion.md)。65组奇半核代数、110组全部内部参数、9200个单位类、520个终端输送、64类r=4二进制状态、256类r=p-3状态和48条边界输送通过。完整证明保留Morris/Serre依赖，并不覆盖r=2或r=p-1。

缺口复查核验：core-gap-four-lifts，对应[常高度乘法与有限例外](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_core_gap_reassessment_20260915.md)。约一秒验证精确四lift判据、无限失败锥、两种逃逸、前缀约分、终端分母以及任意奇p的小分母完整算法。Furstenberg拓扑定理及其有限例外推论由文档明确引用和证明，程序不代替外部定理，也不证明一般阈值。

完整邻点算法：two-prime-neighbour-complete，对应[统一文稿第11节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)。验证所有奇p>=5且omega(p+1)<=2时n=2p+2的严格整数下降，输出包含完整原位置归零路径；五平均12元因此完成。多奇素因子情形、其他偶余量不由本条目覆盖。

七平均最优阈值核验：seven-average-sharp-completion，对应[完整证明](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_sharp_threshold_complete.md)。固定正向循环和有限证书补齐20、22元，接旧维数得到N(7)=15；程序保留22元有限单位像的两个尺度类。证书数据为seven_average_sharp_completion_records.json，未展开任意主同余矩阵的全长平均词。

统一中间带入口核验为 uniform-two-block-entry，对应[统一证明文稿](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)及verify_uniform_two_block_entry.py。它验证不带旧周期/gcd条件的两轮入口，并检查两带公共格、返回及终端公式；不证明一般偶数核内终止。完整有限方向模型须保留R单位像，不能直接用普通有限射影线替代。

当前研究状态及已尝试路线先见 [研究索引](../sources/work/document_reorganization_20260915/originals/outputs/README.md)。以下保留核验程序的历史说明，其中旧的未解维数、入口范围和“下一步”须结合索引及后续专题确认；不能据旧说明重开已经完成或已排除的任务。

全局数学状态见 `outputs/averaging_global_status_20260912.md`：按固定维数判据、自动G、非自动G边缘H和最终阈值N四类量词整理，避免把无条件网络点误当作G等价结果。

十平均与十二平均17元入口是 `ten-twelve-seventeen-complete`，对应 `outputs/ten_twelve_average_seventeen_complete.md` 与 `verify_ten_twelve_average_seventeen.py`；均得到G=1充要，H(10)=H(12)=17。程序保存6条完整路径及q<=200自动B表。两个17元控制器使用不同的Delta(5)/Delta(3)局部激活，不能将一种平均元数的矩阵词混用于另一种。

外部Arena三平均网页的审阅独立放在 `arena_triple_solver_review/`，对应 `outputs/arena_triple_solver_review.md`；核验ID `arena-triple-solver-review`。48个同题比较、预热计时、源码SHA256、数值尺度反例和所有成功索引均保存。快速核验只重放已有证据，不重新访问网页或运行长搜索；本任务不修改数学构造算法。

`work/` 保存研究计算的完整历史，因此仍是平铺目录。为保留旧文档引用，本次没有移动或重命名文件。新接手者不应通过文件名前缀猜测数学结论，而应从 `verification_manifest.json` 查找结论到程序的明确对应关系。

合数端点统一核验入口 `composite-endpoint-transfer` 对应 `outputs/composite_endpoint_crt_transfer.md`。`composite_endpoint_pivot_certificates.json` 存36个模数的全部32112条回路；`verify_composite_endpoint_transfer.py` 独立检查，不导入构造器或主元搜索。28个两素因子模数得到完整输入判据，另8个仅核心覆盖；结果明确保存在 `composite_endpoint_transfer_results.json`。`build_composite_endpoint_certificates.py` 和 `explore_composite_endpoint_transversals.py` 负责有限证书生成，失败不等于不可达。无限两素数入口已证明；任意level的群包含及多素数入口仍是不同问题。

最新入口 `seven-average-fifteen-complete` 对应 `outputs/seven_average_fifteen_complete.md` 与 `verify_seven_average_fifteen_complete.py`。使用已证七平均端点种子，新增两素数三步入口和模15的完整24陪集、72回路编译，严格证明G=1充要及H(7)=15。`seven_average_fifteen_witnesses.json` 保存7条完整路径与72个特殊入口输入。用户取消的六平均十一元探索文件保留但不继续推进，也不登记为完整定理；后续按平均元数增加研究，8平均13元已证，下一候选为9平均13元。

最新非自动G判据入口为 `six-average-ten-complete`，对应 `outputs/six_average_ten_complete.md` 与 `verify_six_average_ten_complete.py`。它完整覆盖G1和G2、排除G5和G10，严格给出H(6)=10。`six_average_ten_witnesses.json` 保存6条完整路径；`explore_six_average_ten_macros.py` 及其发现表只作溯源，正式核验不导入。新的两步R返回、实际尺度周期和模5交换子全部明确实现，不能把Sigma当成免费交换不等块。

当前合数临界线入口为 `composite-critical-scale` 与 `eight-average-thirteen-complete`，共同对应 `outputs/composite_critical_scale_and_conjecture.md`。前者核验局部素数幂平方根尺度的反例下界和连续整数乘积的固定四步网络；后者完成八平均13元并结合下界证明其为排除n=q后的最早成功维数。`composite_critical_scale_results.json` 保存下界表和网络，`eight_average_thirteen_witnesses.json` 保存5条完整路径。`explore_composite_minimal_core_periods.py` 仅记录短周期发现，预算未命中无不可达含义；正式核验不导入它。M最早成功与N最终阈值必须区分。

任意平均元数的充分大维数统一入口是 `arbitrary-arity-linear-threshold`，对应 `verify_arbitrary_arity_linear_threshold.py` 与同名证明文档；保存70条一般路径和24条造零收尾路径。四平均九元的完整入口是 `four-average-nine-complete`，对应 `verify_four_average_nine_complete.py` 与 `outputs/four_average_nine_complete.md`；保存6条经真实尺度重放的原位置路径。两者都没有平均词发现搜索，均由正文证明全称结论。

四平均七元的精确入口是 `four-average-seven-complete`，对应 `verify_four_average_seven_complete.py` 与 `outputs/four_average_seven_complete.md`；它用 (4,2,1) 加权核心和模7陪集控制器证明七元本身的完整判据，保存12条完整路径。

六平均九元独立入口是 `six-average-nine-fixed-network`，对应 `verify_six_average_nine_fixed_network.py`：只用标准库核对固定四步矩阵、全部756个二步后继行和160个有理输入，证明四步为固定全输入网络的最优长度。四平均七元的Sigma由真实C²B词实现，不能免费交换不等大小块；其文档明确区分实际周期尺度与射影等式。两个入口均不证明整体N(4)=7或N(6)=9。

合数平均入口是 `composite-four-six-transfer`。`verify_composite_arity_transfer.py` 对应 `outputs/composite_arity_four_six_transfer.md`，核验偶数元数半块转译、四平均偶数维数和六平均三的倍数维数；生成的 `composite_arity_transfer_witnesses.json` 保存336条原始输入与1基完整序列。商层调用已有二平均HTML，最终Fraction重放只信任原输入和操作索引。全称证明在文档；未解决维数不能据此标为不可达。

## 统一入口

从项目根目录运行：

```text
python work/run_verifications.py --list
python work/run_verifications.py --profile smoke
python work/run_verifications.py --profile core
python work/run_verifications.py --id n13-complete
```

运行器会检查清单结构、引用文件是否存在、程序退出码和预期输出标记。这里的 `PASS` 只表示该程序重现了清单声明的计算结果；它的数学效力不能超出同一条目的 `evidence_scope`。

`reynolds-hodge-structure` 核对原子Reynolds恒等式、完整生成代数及危险素数处的Hodge／Fricke边界；`contingency-layer-semigroup` 实际重放运输表层及交数秩，给出无需子问题调用的有限半群模型。其终端覆盖没有被宣称已证。

`final-hecke-manin-audit`是当前Hecke路线入口：核对整数幺模共轭、第二算子的共同正定星结构障碍、三角方向、普通Manin中心负号及两个位置／卷积模型的区别。旧`iwahori-hecke-modular-interface`的ID保留，但只核对有限代数恒等式；局部特征线并非已识别的自守分量，数字置换和也并非已实现的T_3。旧推导存档与纠正见`outputs/triple_average_final_hecke_audit.md`。

`explore_nonsplit_hecke_charts.py`检查非分裂Reynolds的一至三层B_p chart返回；`explore_bcore_atomic_hecke_walls.py`按二维系数类型和重数穷尽短原子词中的非标准Hecke墙。二者都是有界阴性诊断，不排除直接终端或带子问题的长gallery。

`explore_bcore_symbolic_terminal_cover.py`把整个B_p(1,v)参数族保留为二维整数系数，一棵状态树同时求出所有整数v终端超平面。登记的B71窗口覆盖是有限探索证据；大窗口显示固定深度语言稀疏，不能外推为统一六步定理。

2026-09-11的载体路线复盘见`outputs/triple_average_route_reassessment_2026-09-11.md`。`explore_equal_carrier_*`检查等载体有限域轨道、正向协向量、B核特殊族与固定中心收缩同步；`explore_bcore_zero_triple.py`用整数值--重数状态寻找真实零和三元组，`explore_bcore_zero_triple_greedy.py`比较局部贪心规则。这些`explore_*`文件都是有限诊断；其中一次具体等载体搜索的共同尺度错误已在脚本和复盘中明确修正，旧输出不得引用。

`n47-complete` 完成47元：固定尖点词和校正伸缩、18个Schreier回路正向消元、48陪集及独立标签、全部合法方向输送。`localized-iwahori-generation` 核对任意素数的标准根／单位生成接口和通用奇次三进尖点恒等式，实际资源的普遍正向实现仍开放。发现工具 `explore_b47_schreier_roots.py` 只负责定向找词，不是正式核验入口。

`b47-root-activation` 独立检查固定 `b47_root_activation_certificate.json`，三层46/113/2激活全部167旧宏的逆，连同种子共170节点；核验不导入发现工具 `explore_b47_root_activation.py`。另检查57模板正向共轭词及两个完整相对根群。它单独不承担47元完整判据，后续n47-complete补齐。

`b47-extra-atom-involutions` 固定三个新extra-stage模板及47Z[1/6]平移；`adjoint-return-domain-audit` 检查倒序投影是否真的满足普遍调用域。共享 `verify_bn_integer_templates.py` 的extra字段可选，旧输入沿用两阶段流程。两个搜索文件的阴性结果仅限记录的模板范围，不是不可达证明。

`projective-spectral-balance` 包含任意秩给定矩阵的精确Ad分圆算法。`b47-short-cycle-boundary`（仅full）使用NumPy整数数组作无遗漏模筛选，完整整数复核全部幸存者；`search_four_factor_cycles.py` 是单独的浮点发现工具，阴性结果没有证明效力。

`paired-carrier-two-adic-reset` 核验原维数的等值载体二进宏、两个R理想的精确共同缩放，以及受限宏库的周期障碍；构造有效不等于它已有正向逆。全部操作用真实原位置系数重放。

`n41-complete` 固定21宏、10个三因子对合和10个整数词，正式核验不运行发现搜索。`explore_integral_cycle_closure.py` 使用行列式平方类和两字母状态作有界发现；`modular-primitive-height-barrier` 则重放有限模调度中实能量下降而本原高度指数增长的精确族。

`two-carrier-modular-bridge` 核验一般n=5 mod6的正向降维接口。有限模逆由正向幂实际重放；大子问题只在明确同余域调用，并再次检查全局G。一般群论控制的存在性在正文，脚本未实现大维数任意输入的完整词求解器。

`n29-complete` 是冻结旧子问题库上的独立29元证书，不运行发现搜索。`search_bn_three_cycle.py` 用浮点提出候选并精确复核，阴性输出没有不存在证明效力。`--expanded-first` 只扩充探索用首步大小，不改变默认库。非分裂射影层的有限精确边界登记为 `nonsplit-projective-layer-boundary`。

`split-prime-gaussian-controller` 核验原位置数的高斯周期正向控制器，对应全部p=1 mod3的统一证明。`explore_gaussian_period_layers.py` 同时提供构造辅助函数，不是通过有限素数表宣称全称结论。当前solved_size包含该无限素数族的因子闭包。

新增 `one-tripling-stabilization` 对应一次三份复制、整数仿射轨道及所有三整除维数定理；包含87元接口，但不证明29元。`compile_bn_integer_templates.py` 的 `certificate_size` 保留旧证书库，`solved_size` 才使用新增维数，避免历史证书的矩阵数量随库增长而变化。

`balanced-digit-congruence-group` 核验副本数字库的完整整数同余群生成接口。`b29-current-cycle-boundary` 核验当前B29库的二因子周期排除及全部指数A^jB的精确迹方程；它不运行不断增长的词搜索。

`flat-star-formal-arithmeticity` 核验原维数形式群的显式幺幂和第一层局部接口，有限指数证明另使用已声明的标准初等同余群定理。`cyclotomic-level-entanglement` 建立旧21504容器的43008状态耦合二重覆盖；旧自动机的标签没有改号，旧终端缓存不视为新容器证书。

三档用途如下：

- `smoke`：最新关键结构和九十一元同余容器，通常少于 10 秒。
- `core`：已完成基维数证书和主要一般归约，通常约 1 至 2 分钟。
- `full`：清单中的全部项目，包括九十一元深度四、cusp 29 深度五和新增四维数核实验。长搜索集中于 cusp 29 与 B21；不保证固定总时长。

## 证据等级

- `theorem-certificate`：精确有限证书，闭合证明中明确陈述的有限子问题。一般归约仍需阅读对应证明文档。
- `symbolic-check`：用精确整数或有理数检查恒等式、真实宏和有限参数实例。
- `finite-sanity`：有限穷举或固定随机种子的有界实验，用于防止公式和实现错误，不能承担无限量词。
- `exploratory-search`：有限深度或有限高度搜索。没有找到见证不等于不可达证明。

## 历史文件前缀

- `verify_*`：作者当时用于核对某个公式或证书；强度可能属于上述任一等级。
- `check_*`：局部一次性核对，通常没有稳定输出契约。
- `search_*`、`explore_*`、`analyze_*`：搜索、数据生成或诊断，默认不能引用为完整证明。
- 其他 `.py` / `.js`：共享辅助模块、数据整理或早期实验。
- `.pickle`：历史搜索缓存，不是独立证书。
- `__pycache__/`：运行产物，可忽略。

新增或修改一项可引用的计算结论时，应同时更新：

1. 对应数学文档中的结论和证明边界；
2. `verification_manifest.json` 的命令、输出标记、证据等级和运行时间；
3. 必要时更新 `outputs/triple_average_verification_guide.md` 的人工索引。

有限搜索必须记录全部参数，例如深度、模数、输入界、覆盖数和未覆盖数。九十一元脚本默认深度 2，得到 `14/24`；深度 3 得到 `20/24`；深度 4 得到 `23/24`；定向深度 5 搜索 cusp 29 得到最后一条证书，容器内有限深度覆盖为 `24/24`。脚本默认使用全部逻辑处理器，也可用 `--jobs 1` 做串行对照。

<!-- END SOURCE doc-ec386797a9bf -->

---

<a id="doc-dec765f2fc85"></a>

## 原文导签：Arena三平均网页审阅

来源：`work/document_reorganization_20260915/originals/work/arena_triple_solver_review/README.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/work/arena_triple_solver_review/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-dec765f2fc85 -->
# Arena三平均网页审阅

来源与完整结论见 ../../outputs/arena_triple_solver_review.md。这里只保存外部网页快照、未改动的计算函数和独立审阅工具，不替换项目正式求解器。

快速核验（不访问网络、不重新计时）：

~~~text
python work/arena_triple_solver_review/verify_saved_review.py
~~~

重新做同题基准，必须串行执行以下步骤，避免计时相互干扰：

~~~text
python work/arena_triple_solver_review/benchmark_arena.py --output comparison_single.json
python work/arena_triple_solver_review/remeasure_baseline.py
python work/arena_triple_solver_review/check_structure.py
python work/arena_triple_solver_review/check_warm_and_macros.py
python work/arena_triple_solver_review/verify_saved_review.py
~~~

完整网页束搜索复测约需数分钟；每题有独立16秒外部保护，超时不表示不可达。原网页单题预算9000ms、批量预算1500ms不是同一配置，主报告使用单题默认配置。benchmark_arena.py 的 --batch 选项仅用于另行诊断。

frame1.html 是实际浏览器iframe渲染后的快照；arena_solver.js 是其中计算部分的原文，统一LF换行，并由 provenance.json 的SHA256绑定。page.html 和 frame0.html 是Arena外壳，不包含被审阅的求解算法。

run_arena.cjs 只运行已经读取检查的计算段，放在Node VM Worker中，不执行原页面网络脚本或DOM事件。外部Worker是审阅隔离工具；原网页本身没有把求解放进Worker。

comparison_single.json：48个历史同题和4个额外示例；baseline_current.json：旧算法同机串行复测；warm_small.json：同一个JS上下文的24题预热复测；structure_checks.json：缩放和预算问题；macro_basis_checks.json：33个独立宏基重放；summary.json：从记录重新计算的统计。

读取大整数原题请使用Python整数或无损JSON工具，避免将JSON数值直接转成JavaScript Number。提供给网页算法的所有输入都通过十进制字符串转BigInt。

审阅结论属于有限性能和实现检查，不是新的平均可达性数学定理。历史数学项目和其他AI同时进行的研究不受这组文件影响。

<!-- END SOURCE doc-dec765f2fc85 -->
