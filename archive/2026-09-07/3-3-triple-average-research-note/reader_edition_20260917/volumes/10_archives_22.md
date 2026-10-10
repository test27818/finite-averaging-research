# 工作材料、历次快照及旧目录完整附卷 · 第22分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [三平均有限步可达性研究](#doc-437d08f2e4fd)
- [核内缺口文献访问记录](#doc-7fe8564de066)
- [H_t文献来源与访问等级](#doc-2632e7b8ffd6)
- [Literature retrieval, 2026-09-12](#doc-c65dbe373e50)
- [2026-09-14研究审查材料](#doc-dc13379c0453)
- [Danus — Architecture](#doc-d3d10b427f39)
- [Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory](#doc-37cf6743b1ed)
- [Proof Verification Agent](#doc-ee9f3da2a832)

---

<a id="doc-437d08f2e4fd"></a>

## 原文导签：三平均有限步可达性研究

来源：`work/document_reorganization_20260915/originals/work/audit_before_sharp_structure_20260912/README.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/work/audit_before_sharp_structure_20260912/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-437d08f2e4fd -->
# 三平均有限步可达性研究

2026-09-12主余类储备推进：[主余类储备与刚性例外](outputs/prime_arity_dominant_residue_reservoir.md)把多余轻余数分支压缩为：主余类碰撞先锁定小整数提升；任意例外余数有合法配比；两个配比同时碰撞时提升满足唯一整数仿射关系；总超额达到p时有严格能量下降。367224个碰撞提升、37754个例外配比、13301个容量包装和834条原位置续步通过。多余类全局闭包仍未证明。核验ID `dominant-residue-reservoir`。

2026-09-12整数闭包新证明：[二类型碰撞的整数格结构](outputs/prime_arity_binary_collision_lattice.md)用平面空三角形的指数1性质，证明临界p预算下二类型全碰撞参数必为整数，并给富余预算的总和界。对(a^(p+alpha),b^p,轻值)且一个低重模p余类、保护数h<=r的上半带状态，得到安全非恒等整数续步；只有一种实际轻值时h<=1，覆盖r=1。另通过G=1直接补齐三个重值在3p+1的一个额外位置分支。2133条单轻值、300条三重值、127条同余多实际值原位置续步通过；一般多余类闭包及N(p)<=3p仍未证明。核验ID `binary-collision-lattice`。

2026-09-12核心终止审计：[距离3p的真实缺口](outputs/prime_arity_three_p_remaining_gap.md)给出七平均22元(2^14,(-1)^7,-21)：所有十个非恒等三组不交核心返回均非法或增大本原能量，且无终端后继，但两次重叠整数平均即可造七个零。该逃逸推广到任意素数p>=5的(2^(2p),(-1)^p,-3p)族，首次造零恰需两步。另给所有r>=4的第二载体对合，明确终止步数必须随输入高度无界，以及p761/n3045未被旧4p-2+d不等式覆盖。未完成一般核心终止或降低N(p)。核验ID `upper-band-descent-boundary`。

2026-09-12上半带统一归约：[3p到4p的任意素因子数三值归约](outputs/prime_arity_upper_band_three_value_reduction.md)证明每个素数p>=5、每个3p<n<4p的全部合法输入，至多12+3ω(n)次原位置平均进入合法(2p,p,n-3p)二维核心。初等短区间筛选、双块集中见证和三行折叠消除r>=d及素因子数限制。核心G=gcd(y,n)，二次型判别式-8n(n-3p)；所有r>=4还有显式三步全局射影对合。385条归约路径、700条六原子标量周期及本原高度增长恒等式通过。不宣称核心终止、七平均22元已解或最终阈值降低。核验ID `upper-band-three-value-reduction`。

全局总览（2026-09-12）：[从二平均到任意平均元数：证明、自动G、非自动G边缘和临界猜想](outputs/averaging_global_status_20260912.md)。统一区分固定维数完整判据、G自动成立的无条件维数、G真正筛选输入的H(q)，以及要求所有后续维数的最终阈值N(q)。当前已证非自动边缘为H(2)=5、H(3)=7、H(4)=7、H(5)=11、H(6)=10、H(7)=15、H(8)=13、H(10)=H(12)=17；九平均13、十四平均22、十五平均21等仍是候选。任意q的大维数定理为n>=4q-1+d_q(n)，精确临界线H(q)=C(q)仍为猜想。



2026-09-12十、十二平均17元完整解决：[十平均与十二平均的非自动G判据](outputs/ten_twelve_average_seventeen_complete.md)证明两者均可达当且仅当G=1，因此H(10)=H(12)=17；16元的G自动满足不计入非自动边缘。两步进入(10,6,1)/(12,4,1)核，18陪集Gamma_0(17)分别由十平均的Delta(5)和十二平均的Delta(3)配合二进根覆盖。17个q<=200的旧B自动点也已独立列出。各自60个大整数入口和3条完整路径通过；不宣称N(10)=17或N(12)=17。核验ID `ten-twelve-seventeen-complete`。



2026-09-12入口继续缩小范围：[六素因子入口与覆盖系统边界](outputs/prime_arity_six_prime_endpoint_entry.md)证明任意至多六个不同素因子的2p+1输入可进入合法双p块。五个任意乘法阶坏类不能覆盖；真正合并时坏类只来自一个非全支持单点，至多d-1个，因此得到六素因子结论。原p217717/n435435的K4直接分组障碍可至多五次真实平均绕开并进入核心，未宣称该巨大level已完成归零。另给任意d下Theta(n)=sum 1/ord_ell(2)-min 1/ord_ell(2)<1的入口充分条件，六个坏类的模24覆盖说明继续外推需要不同见证选择。核验ID six-prime-endpoint-entry。核心群包含与中间带终止仍独立。



2026-09-12两方向新推进：[四素因子端点入口](outputs/prime_arity_four_prime_endpoint_entry.md)证明任意至多四种危险素数的2p+1输入都能有限步进入合法双p块。交换在各端点素数下统一产生2^k，每处只禁止一个指数类；3、5的奇偶筛选与剩余密度界保证指数存在。接原核心证书，195、231、255、315、399、435、455、1155八个端点新增全输入判据，p=97不再缺入口。另见[中间带周期密度归约与全部r的对合](outputs/prime_arity_band_period_and_involutions.md)：r>=d且局部交换阶倒数和<1时，所有2p+r输入可降到(p,p,r)，包括中间带所有素数维数；每个r还显式具有合法两步射影对合，四原子成非零标量周期。尚未证明任意level的核心群包含或一般三块核心终止。核验ID four-prime-entry-and-band。



2026-09-12合数端点统一推广：[CRT陪集证书与两素数入口](outputs/composite_endpoint_crt_transfer.md)。十五元方法已编译为统一流程，36个列明模数的32112条回路全部通过独立精确核验；28个双素因子模数由一般三步入口得到全输入G=1充要判据，包括十七平均35元、十九平均39元、三十一平均63元、三十七平均75元及含重复素因子的135、147、175、207等。结合旧素数幂定理，全部奇整数3<=p<=109的2p+1端点均已覆盖。p97/n195等8个多素数模数的入口已由四素因子入口定理补齐，36个列明端点均已完成全输入判据。未证明任意合数的全称群包含，有限主元菜单全成功也不外推；最小非自动G边缘对合数平均元数仍须单独研究。ID `composite-endpoint-transfer`。



2026-09-12算法回归交付：[困难输入测试集](outputs/averaging_algorithm_benchmark.md)保存584道去重题、19道精选题及2道历史束搜索深度24未出解的大整数题。其中196道七平均十五元冻结态已由新端点定理保证可达；108条参考原位置路径独立精确重放通过。p=19、37扩展题按有无直接证书标注，332道不设可达性真值。附1基索引验解器、新题生成器及旧预算记录；不重新搜索，不把路径未找到记为反例。核验ID averaging-algorithm-benchmark。



2026-09-12七平均十五元完整解决：[两素数入口与二进Gamma_0(15)](outputs/seven_average_fifteen_complete.md)证明可达恰在G=1，故按非自动G标准H(7)=15。任意至多两种危险素数的端点输入可用至多三次平均进入合法双p重块；十五元CRT给24个陪集，全部72条回路用62个左上主元、8个右下主元及2次半整数剪切完成正向编译，完全使用已证二进根，不另搜索种子或激活11、17倍率。192个本原模行、72个强制三步入口与7条完整Fraction路径通过；最长样本7746步不代表最短界。平均元数7的候选端点15现已证，8的13也已证，下一个待攻的元数是9、候选13元。七平均更高维数17、18、19、20、22仍未解决，因此不宣称N(7)=15。核验ID `seven-average-fifteen-complete`。



2026-09-12非自动G条件的新完整结果：[六平均十元](outputs/six_average_ten_complete.md)证明可达恰在G=1或2，G=5或10由模5障碍排除，故按“G确实筛选输入”的标准H(6)=10。两步进入(6,3,1)核后，新增两步宏R满足R^4=-I/324、(AR)^2=I/36、(RAC)^2=I/216；正向逆与真实交换子给出L(-5/3)，进而实现Gamma_0(5)的全部18条回路。两类合法G各60个大整数入口、196种余数多重集和6条完整原位置路径（最长1931步）通过。后续研究以非自动算术边缘H为主，无条件网络作为辅助工具。六平均当前首个未解维数为11；不宣称最终阈值已确定。ID `six-average-ten-complete`。



2026-09-12历史反向诊断已更正：[整数冻结态与分数逃离](outputs/prime_arity_endpoint_counterexample_reverse.md)。高度5的35714个合法状态全部可达；其中7个无整数出边，87个首步值类型均无零触发，但七条完整分数路径均独立重放通过。旧“最低层重叠自动下降”说法已撤回：部分相交实际加深分母，成功路径通过不交分组留下单点。七平均十五元随后已完整证明，困难题现转作算法测试。ID endpoint-reverse-diagnostic。



2026-09-12合数临界线新结构：[局部平方根尺度与精确猜想](outputs/composite_critical_scale_and_conjecture.md)。定义S(q)=max p^ceil(v_p(q)/2)。赋值间隙不变量证明q<n<q+S全部有G1反例；边界q+S除非只有q允许的素因子，否则也有反例。因此B(q)=q+S或q+S+1是已证下界，猜想M(q)=N(q)=B(q)，其中M排除n=q后表示最早成功，N要求之后所有维数成功。新固定四步族q=m(m-1),n=m²在m或m-1为素数时与下界吻合，严格给出M(12)=16、M(20)=25、M(30)=36、M(42)=49、M(56)=64等。另由(8,4,1)核、两个精确周期及模13全部42条回路证明M(8)=13。二平均的4与六平均的9属于G自动合法的固定网络点；5与10则是随后第一个非自动G维数，六平均10现已由独立模5控制器证明。核验ID `composite-critical-scale`、`eight-average-thirteen-complete`。



2026-09-12路线重评估：[任意 p 的结构、分段高度与文献](outputs/prime_arity_strategy_reassessment_20260912.md)。第二轮检索44个结构关键词、148篇去重题录并阅读4份全文后，最有希望的不是寻找新的固定二次能量，而是建立带局部同余、p进内容和块形状节点的 path-complete 离散高度；算术群的相对有界生成可作为已实现根之后的后处理。同步记录了多素数单位分离障碍和一般 r 合并恒等式。当前完整新族仍是 p=2^s-1 的 n=2p+2；全中间带开放。ID strategy-reassessment-20260912。



2026-09-12合数平均的统一突破：[任意元数的线性阈值](outputs/arbitrary_arity_linear_threshold.md)把充分大维数定理推广到每个整数q>=3：n>=4q-1+d_q(n)时，完整判据为G的素因子均整除q，且整数零和输入只需一位额外q进精度。非单位差分delta用q/gcd(delta,q)份配比直接平均；偶数元数唯一中点碰撞由顺序结构或相反值终端解决。由此N(4)<=16、N(6)<=24，不再留下无限多未解维数。同时[四平均九元](outputs/four_average_nine_complete.md)用显式四步周期、二进根和模9全部36条Schreier回路完全解决，无种子搜索。结合半块转译，候选临界带内尚未证明G充分的仅四平均11、13、15元，六平均11、13、14、16、17、19、20、22、23元。新核验ID `arbitrary-arity-linear-threshold`、`four-average-nine-complete`；不宣称最短解或精确阈值。



同日更新：[四平均七元](outputs/four_average_seven_complete.md)通过 (4,2,1) 核和三个真实一步宏完成；实际周期为 C^3=I/8、(CA)^2=I/8，Sigma也由真实三步词实现。改用模7的0、±1、±2、±4代表，24条回路全部采用二进单位主元，无种子或平均词搜索。[六平均九元](outputs/six_average_nine_fixed_network.md)独立复核固定四步网络，并证明三步固定全输入网络不可能。入口 `four-average-seven-complete`、`six-average-nine-fixed-network`。两项结论只确定7和9这两个维数；最终阈值仍为 \(7\le N(4)\le16\)、\(9\le N(6)\le24\)，不能由端点成功直接取等号。



2026-09-12新完整中间维数族：[统一能量与 2p+2](outputs/prime_arity_energy_and_dyadic_neighbour.md)。对每个 p=2^s-1、s>=2（允许奇合数平均元数），全部 n=2p+2 输入恰在本原中心化 G=1 时可达，特别新增七平均十六元。安全分块、CRT 单点等值化、真实两步上平移及除法返回使本原奇数方向高度 |v| 在完整阶段间严格下降，不依赖 2p+1 端点。一般 p 的双单点也能在至多 p+1 步归约到合法 (p,p,2) 二维核。另证明共同单调正定二次型只有平方能量，非整数交换的本原平方高度反而增加。31278 个方向、24 条核路径、48 条原输入 Fraction 路径等核验通过。ID carrier-energy-dyadic-neighbour。



2026-09-12合数平均新结果：[四平均、六平均与统一半块转译](outputs/composite_arity_four_six_transfer.md)。对偶数q，原位置重叠块制造q/2的倍数份副本，再把所有允许的奇素因子吸收到副本数c中；剩余二平均商维数M=2或M>=4时，完整G判据成立。这覆盖任意偶数q的全部q倍数维数，并证明四平均全部偶数n>=8（另有n=4）、六平均全部3|n且n>=6。六平均九元有固定四步网络，其三进张量推广补齐纯三幂维数。四平均六元(-1^4,0,4)、六平均八元(-1^6,0,6)均为G=1的严格不可达例，由局部赋值与同余分支证明。533个标准基、35个副本宏、32415个陷阱后继及336条完整路径精确通过。核验ID `composite-four-six-transfer`；未证明四平均全部奇数维数、六平均3不整除的维数或最终阈值。



2026-09-12中间带接口已修订：[相对尺度与单点—块交换](outputs/prime_arity_middle_band_relative_scale.md)。该交换自动保持全部非 p 同余见证，模 p 匹配只为整数中间值所需；允许分数后必须另证终止。(p,p,1^r) 的均值格商阶为 2p+r，只有实际等值化成 (p,p,r) 才能除去 gcd(p,r)。旧的“同时匹配与动态保护均未解决”表述不再适用于这个交换子类。



2026-09-12临界端点的深层结构：[素数幂端点与临界几何](outputs/prime_power_endpoint_and_critical_geometry.md)。对任意奇p，q=2p+1为素数幂时，两张局部射影坐标图的全部Schreier回路均可由已证正向控制器编译，得到射影Gamma_0(q)包含；配合两步合法入口和Bezout输送，完整解决所有素数幂端点，特别是十三平均二十七元与形式上的1093平均2187元。临界能量是判别式-q虚二次阶的范数，产生权一theta级数；但level27、weight1的LMFDB空间全为Eisenstein，模形式解释计数而不直接提供原位置路径。相邻2p+2的真正障碍是局部逆只给共同收缩lambda，外部单点固定后变成diag(lambda,lambda,1)，不再是全局射影单位。独立核验15612条回路、55512个模行、168条编译回路、32个入口及2754个范数恒等式。ID `prime-power-endpoint-completion`。



2026-09-12临界前沿交接：[当前方法的障碍与2p+1结构](outputs/prime_arity_critical_frontier_handoff.md)。区分一步双重值闭包、固定保护、有限短词表、直接多素数分块和余维一黑箱调用的已证障碍，明确这些是特定方法边界而非总猜想的反例。建议将碰撞总和保留为上界支线，优先研究素数幂端点的真实正向轨道和2p+2双单点的部分控制。新增完整证明：q=2p+1为素数幂时，任意G=1输入都能两步进入合法K_p；p本身为奇素数且q合数时，q必为3的幂。入口不解决核内轨道，未新增完整端点或降低阈值。独立原位置核验ID：prime-power-endpoint-entry。



2026-09-12任意p的统一碰撞结构：[两组相加、总和窗口与高重数分类](outputs/prime_arity_uniform_collision_structure.md)。在保护后3p+1层，任一低重数余类达到p-2重即可统一闭合：全碰撞只允许D=3p或3p-1，再由私人见证／全局零和排除。分数坐标族有显式除数参数，包含所有p=2 mod3的一族，不需逐p求表。另由Dias da Silva--Hamidoune受限和集定理处理至少sigma(p)=min_k(2k+ceil((p-1)/k))种余数；零和因子分解给两个明确的总余数窗口。二平均最近对也推广为安全连续p块的新生重值引理，但一般保护容量仍在。核对51618个高重数符号模式、779个原位置合法步骤、4824个零和分解、105760个窗口公式及144个受限和集构造。剩余是中等重数余类交互；未降低一般4p级完整阈值。ID `uniform-collision-structure`。



2026-09-12七平均推进到3p+2：[对称碰撞总和证书](outputs/seven_average_three_p_plus_two_threshold.md)完整解决七平均23、24、25、26元，接已有>=27，得到15<=N(7)<=23；21元另已解，22元仍开放。一般有效的余数类对称压缩只保留总和，57026个完整模7模式仅有11个相容解，再接最小保护总和矛盾；新增四维数均只需一位额外精度。另见[可交换保护与统一初始化](outputs/prime_arity_protected_exchange_and_mass.md)：初始化降至n>=3p+d-2，p=23,n=70反例说明不能固定任意极小保护集；交换后产生一整个p=2 mod3的3p+1元五步整数族。任意p的3p级阈值仍未证明，p=11总和数据仅为探索。ID `seven-average-three-p-plus-two`、`minimal-protection-and-exchange`。



2026-09-12五平均达到3p：[最小同余见证与碰撞总和证书](outputs/five_average_three_p_threshold.md)。完整解决五平均n=16、17、18；结合已证n=15及全部n>=19，得到11<=N(5)<=15=3p。低总重数不同余双重值的全部碰撞对应903个模5模式的有理线性系统，只有22个相容解，且总和的局部分母可控；最小保护横截集的私人见证与全局零和排除所有合法例外。新增三维数都保持一位额外精度；本证明是完整有限符号证书辅助，不是平均词搜索或有限输入外推。五平均尚未解决12、13、14；任意p的3p级阈值仍开放。新的通用方向是证明碰撞关联方程的总和证书，无需逐个确定所有坐标。ID `five-average-three-p-threshold`。



2026-09-12直接面向3p：[长零和自由序列与双锚点接口](outputs/prime_arity_three_p_additive_interface.md)。引用Savchev--Chen长序列结构，重复锚点将其单位缩放锁为1，证明n>=3p+d时低总重数不同余双重值必有安全非恒等整数候选，保留一个旧p重块；较长序列零和自由时用一／两个低重数位置进一步修复碰撞，完整保持双重值。剩余是候选存在但实际和全部碰撞的恢复／造零，尚未证明3p统一上界。新核验器精确计算模p子序列和的实际最小／最大值，避免过早截断安全池；4246个样本未留全碰撞不承担无限结论。与2024年同余拟阵基／群标签基理论的具体对应和适用边界已记录。ID `three-p-two-anchor-interface`。



2026-09-12阈值实际下降：[逆EGZ的4p-2+d定理](outputs/prime_arity_inverse_egz_threshold.md)。对奇素数p>=5，完整判据已在n>=4p-2+d_p(n)成立，故N(p)<=4p+ceil(log_2 p)，特别N(5)<=19、N(7)<=27。三重值的单份／双份中间值修复把该分支降到3p+2；两个不同余重值总重数>=3p-2时有共同预留跨越。保护后2p-2池若无整数p子集，逆EGZ强迫两个p-1余数类，再借一份／两份锚点修复碰撞。全部整数能量闭包保持，一位额外精度仍成立。约7p/2+d路线已有明确容量，但低重数池的统一碰撞恢复尚未证明，不列为新上界。ID `inverse-egz-threshold`。



2026-09-12逆零和工具已转译：[碰撞修复与2p+4七步族](outputs/inverse_zero_sum_averaging_progress.md)。2022逆加权零和定理给出O(p)模运算的真实副本选择；两次相反碰撞在不交副本和保留见证下恢复双重值。五平均十四元的(5,5,2,2)核在两个锚点模5不同、低重数两值模5不同或有锚点同余时，已有完整安全整数闭包；余数集中情形确实可能每步失去不变量。另有任意奇数p>=5的2p+4元二参数族，两次平均造零、总计至多七步；其中(6^p,8^p,[p(18-p)]^2,[p(p-25)]^2)对所有奇素数合法且没有非恒等整数一步双重值闭包。没有新增完整维数或降低统一阈值。ID `inverse-zero-sum-transfer`。



2026-09-12外部文献检索：[2018--2026年的二平均后续与可借用工具](outputs/averaging_literature_survey_2018_2026.md)。核对原论文2019会议／2020期刊版本、作者2019博士论文、2020 RPRIS、2019 Clique Gossiping、2021--2022块Kaczmarz、2022逆加权零和和EGZ近线性算法，以及2024 splitter和2025--2026相关题录。本轮未找到一般p平均完整判据或最优阈值的已核验外部证明。已读逆零和全文给出一个可由两份副本实现的整数平均候选引理，但安全性与碰撞仍需另证。没有更改正式求解算法或新增完整维数；综述明确标注全文与摘要的证据边界。



2026-09-12维数传播与统一终端：[造零收尾、余维一障碍和加权均值格](outputs/prime_arity_interpolation_and_lattice_structure.md)。对所有奇素数p及n>=2p+1，一旦真实p平均产生p个零，就能完整归零。下半区间只需已证的2p+1含零尾部，无需端点完整猜想；上半区间用3p、4p和大维数定理按支持数传播。另证n非p幂时整块等化n-1个位置必归零或陷入G=n障碍，因此不能用相邻已解维数黑箱直接内插。块重数除公因子后的总和s给出Z^k/(零和格+常值方向)=Z/s，统一解释端点的Gamma_0(2p+1)和三块的Gamma_0(3)。未证明任意合法输入必能先造零，未新增完整中间维数。ID `prime-arity-zero-trigger-bridge`。



2026-09-12中间维数推进：[三块运输与3p完整定理](outputs/prime_arity_middle_band_structure.md)。对每个奇素数p，n=3p的完整p幂G判据已证；p>=5时写p=3m+epsilon，两张明确非负运输表mJ+epsilon(I+-D)在原3p位置实现U(+-1)，块重标记再给L(3)，同一个四陪集Gamma_0(3)及模3分组修复完成全部输入。无种子或平均词搜索，旧3p一步闭包反例族也全部解决。另证n>=3p+d时两个模p同余重值的安全整数闭包。五平均新增n=15，尚待覆盖12、13、14、16、17、18、19；统一N(p)上界不变。ID `prime-arity-middle-band`。



2026-09-12统一正向控制器：[无需搜索的临界种子证明](outputs/uniform_endpoint_positive_controller.md)。对每个奇数平均元数 p>=3，在原 q=2p+1 个位置上的两种两步返回、互补仿射倍率和必碰偶数的整数递推，统一给出可逆倍率2、U(1)、L(q)。欧拉同余随后为全部安全的 j<=p 构造正向逆，得到 R_q=Z[1/l:l<=p且l不整除q] 上的完整上根、q倍下根及对角单位。q为素数时，完整Schreier与入口证明遂解决全部输入，统一(3,7)、(5,11)、(11,23)、(23,47)等，无平均词搜索。q为合数时种子已解决，但合数level轨道与任意输入安全入口仍未闭合，七平均十五元仍不宣称全解。ID `uniform-endpoint-controller`。



2026-09-12七元精确端点结构：[为什么阈值是七](outputs/seven_exact_threshold_structure.md)。双三重块与全系统载体的六次交换给出 -1/27 的正向标量周期；三个明确跨块返回满足三条短周期，生成 Z[1/6] 上的上根、7倍下根及对角单位，八陪集与六个 Schreier 回路遂给出完整 Γ₀(7)。这是不依赖旧十八词下降覆盖的另一份七元充分性证明。一般p双块扫掠的判别式为p(p-4)，解释p=3的有限周期与p>=5的双曲分界；精确端点不必通过不断压低大维数常数获得。ID `seven-endpoint-structure`。



2026-09-12上界降至4p级：[三个重值的顺序结构与3p边界](outputs/prime_arity_four_p_threshold.md)。对奇素数平均元数p，n>=d_p(n)+4p-1 已足够，故 N(p)<=4p+ceil(log_2 p)+1。三个重值用实际极值和单份参与直接处理，只对两个重值预留2p位置，再调用保护后的EGZ。因此五平均全部 n>=20 已解，结合 n=11，尚待覆盖 n=12,...,19。另有任意p>=5的合法3p元族，所有非恒等整数平均都会只剩一个p重值且不造零；这只否定未经补充的双重值一步闭包，不证明3p不可达。ID `prime-arity-four-p-threshold`。



2026-09-12五平均十一元已证：[完整证明](outputs/five_average_eleven_complete.md)。五个两步原位置返回和三条短标量周期提供全部正向逆；在 (a,a-b) 坐标中生成 Z[1/30] 上完整上根、11倍下根和对角单位。有符号十二陪集与十个明确 Schreier 回路证明包含 Γ₀(11)，Bezout 输送和四步终端解决全部合法输入。因此五平均 n=11 的充要判据是 G=1，不再只是有限样本结果。全程只用五平均，未调用三平均或子维数求解器。n=12,...,24 尚未由此解决，N(5)=11 仍未证明；不承诺一位额外精度或最短构造。ID `five-average-eleven-complete`。



2026-09-12边界推进：[预留重数与临界结构](outputs/prime_arity_boundary_progress.md)将素数元平均的充分界改进为 n>=d_p(n)+5p-1，特别 N(p)<=5p+ceil(log_2 p)+1<=6p，且 11<=N(5)<=25。n=2p+1 中含零状态统一至多五步收尾，Y_p=(1^p,2^p,-3p) 恰好四步可解。若2p+1为素数，全输入两步可进入合法K_p；若含六个不同素因子，K4/CRT构造会阻塞每个直接(p,p,1)划分。p>=5的两个自然核返回保留避零实区间，必须加入跨块操作；第一未解实例是五平均十一元的全参数核终止。ID `prime-arity-boundary-progress`。



2026-09-12阈值细化：[素数元平均的线性阈值与 2p 边界](outputs/prime_arity_linear_threshold.md)。EGZ 保护池、四重值的极端锚点及系数跨越打包，将 n>=2p^3 改进为 n>=d_p(n)+8p-7，特别是 n>=9p-5。对奇素数 p，(-p,0^(p-1),1^p) 在 n=2p 处不可达，故 2p+1<=N(p)<=9p-5。N(2)=4、N(3)=7；p>=5 的 N(p)=2p+1 仍为猜想。n=2p+1 的 (1^p,2^p,-3p) 还明确否定无例外的双 p 重值一步闭包，不能只靠调小常数声称最优界。ID `prime-arity-linear-threshold`。



2026-09-12素数平均元数推广：[素数元平均的充分大维数定理](outputs/prime_arity_averaging_large_dimension.md)。这里 p 是一次平均的位置数，n 是任意总维数。对每个素数 p、n>=2p^3，完整可达判据为本原中心化 G 是 p 幂；整数零和合法输入只需分母 p。证明通过双 p 重值、保护池和一次模逆调节，把不能继续的状态限制为可直接消去的短等差数列，不调用三平均定理或任何子维数。阈值只求充分，不声称最优；合数平均元数尚未由此证明。ID `prime-arity-large-dimension`。



本目录保留全部研究过程，同时提供一层稳定的接手入口。2026-09-11：[双三重值不变量](outputs/triple_average_prime_double_triple_invariant.md)给出全部素数 p>=11 的统一原位置证明，结合既有七元证明和合数归约，闭合原判据：对任意 n>=7，中心化、本原化后的非零状态恰在 G 为三幂时可达；全零状态单独显然可达。



新证明先研究 3X，至多两次整数三平均建立“至少两个不同三重值”，再按模3余类与重数选择真实原子，保持模p不全同余，直至 (a^3,(-a)^3,0^(p-6)) 终端。固定整数格上的平方能量给出有限终止，因此 p>=11 的整数零和合法输入只需一位额外三进精度。全称结论由正文证明，程序只做有限独立重放；未证明位长多项式构造长度或七元／任意合数的一位精度界。核验ID `prime-double-triple-invariant`。



本轮的原文阅读、外部文献及研究复盘见[重读二平均与统一证明](outputs/triple_average_binary_source_reassessment_2026-09-11.md)。旧控制器仍保留为历史证书库；下文“最小未解”等表述描述各自的历史阶段，不代表当前状态。



此前结论：[Hecke与模符号路线的最后检验](outputs/triple_average_final_hecke_audit.md)。该阶段没有得到任意p证明，暂停直接模形式方案。标准矩阵对任意奇p都有整数幺模共轭，旧指数p换基不是内在level；有根的第二算子与标准生成元没有共同正定Hecke星结构；整个下三角族不能从u非零到u=0；直接线性普通Manin编码被中心负号排除。此前将局部投影称为全局Eisenstein／Steinberg分量、将数字算子称为已实现T_3、将删点置换放入PGL2自然位置表示的说法已撤回。[修订接口页](outputs/triple_average_iwahori_hecke_modular_interface.md)保留正确恒等式及历史实验，原稿已存档。ID `final-hecke-manin-audit`；旧核验ID仅证明有限代数恒等式。该阶段最小未解为71，现由上述直接证明覆盖。



此前路线复盘：[停止局部拼接，返回二维除法结构](outputs/triple_average_route_reassessment_2026-09-11.md)。它记录载体路线的局部成果与全局困难；其中后来提出的直接Hecke／Manin主线现由上面的最后检验取代。弱的输入相关终端覆盖仍开放，但尚无分支提升定理或全局下降量。仿射交换子理想、参数周期刚性、混合迹零条件归约继续保留各自已经证明的范围。



结构结果：[载体扫掠催化器](outputs/triple_average_carrier_sweep_catalyst.md)。r个三重块与一个载体各交换一次，始终得到1/3乘整数幺模矩阵；r=2恰恢复七元Artin中心，r=3则在固定十位置窗口中产生24个正向幺幂，其中12个具有同长度正向逆。四个固定共轭根显式给出E12(36)、E13(96)、E21(720)、E31(2160)，进而包含E3(4320^2 Z)，所以局部群的算术有限指数已经证明。更进一步，根约化与至多三次扫掠的精确有理锥证书证明：任意三个三重块加一个载体都能在这十个原位置内有限步产生叶／载体或叶／叶碰撞，不要求局部G条件，也不依赖p。固定窗口的外部耦合是以局部均值为中心后消失的1-coboundary。其全局拼接边界和路线降级见上面的最新复盘。ID `carrier-sweep-catalyst`、`carrier-catalyst-local-descent`。



最新终端化简：[等载体形式冻结定理](outputs/triple_average_equal_carrier_formal_freezing.md)。在D_r=(u_1^3,...,u_r^3,a^2)中，形式交换群显式包含左上SL_(r-1)(Z)；任意合法素数核先以SL把叶差化成单gcd坐标，做一次真实等载体交换后，新叶差gcd自动整除新基值，再用第二个SL便产生零叶块。有限域中唯一避开零叶超平面的轨道是q|3r+2时的常值直线，素数维数下它恰为非法方向。因此形式轨道终端已闭合。正文同时证明正向局部化锥障碍：任何不依赖未参与叶的正向输出行只能有非负叶系数，故不能直接实现平衡SL剪切。剩余目标必须使用全局边界的状态相关抵消，或直接命中零叶。ID `equal-carrier-formal-freezing`。



最新完整结果：[59元判据与结构总结](outputs/triple_average_fifty_nine_arithmetic_complete.md)。一次额外原子库给出正向种子，33节点无环逆证书经仿射消元产生上下三进根，21个Schreier回路实现共轭Gamma_0(59)，独立折叠60陪集并接九元终端。59已加入因子闭包，最小未解维数更新为71。入口 `python work/run_verifications.py --id n59-complete`。此后主线停止逐素数推进，转向统一的非分裂素数种子定理。



17至59证书中可预测与不可预测的部分见[非分裂素数结构综合](outputs/triple_average_nonsplit_prime_structure_synthesis.md)。根提取、尖点、Schreier消元与终端已有统一公式；未统一的是原位置返回半群中正向可逆种子的存在。下一阶段优先研究PGL2(F_p)非分裂三阶轨道的p+1到p位置商实现，避免继续逐素数搜索。



备选条件归约：[混合单点迹零返回控制器](outputs/triple_average_mixed_singleton_controller.md)。令B为不超过(p-1)/2且不等于3、5的素数乘积，两个显式返回R_0与R_(1/(10B))一旦能在原p个位置实现，其周期、仿射交换子和显式Bezout恒等式便统一产生U(R)、L(pR)；固定因子15补齐3、5，对角吸收随后覆盖全部合法方向并接九元终端。两个目标已有共同严格正三进运输和副本实现。这条特定充分路线内部只差两运输的原位置分解；该条件不等价于一般种子存在，也不排除条件宏、奇异降秩或直接终端命中的其他证明路径。ID `mixed-singleton-conditional-controller`。



原位置分解的精确半群方程、两个返回的相对混合器、现有返回库二因子边界、非分裂平移闭路边界及叶数字控制器边界见[原位置分解前沿](outputs/triple_average_original_position_factorization_frontier.md)。这些有限阴性结果用于收缩统一语法，不构成不可达性证明。



最新：[53元完整判据](outputs/triple_average_fifty_three_arithmetic_complete.md)已登记n53-complete并加入已解因子目录。74节点正向逆证书、三进根和20个Schreier回路消元给出共轭Gamma_0(53)，独立折叠54陪集并重放九元终端。最小未解维数更新为59；下文更早的未解起点属于历史状态。全部素数统一证明仍开放。



最新结构：[Reynolds半群、交叉计数与判别式对偶](outputs/triple_average_reynolds_hecke_hodge.md)。原子生成代数对全部n>=5已是整个End(V)，因此线性化不能区分五元失败；固定1／3重数的整数运输表则精确参数化普遍可执行层，自动关于加权伴随封闭，并有有限Hecke角解释。能量Hodge对偶在危险p处交换Iwahori边两侧，把合法方向送进非法余类，解释自然伴随取逆的障碍。已给出无隐藏宏适用条件的运输半群终端猜想，未新增已解维数。ID `reynolds-hodge-structure`、`contingency-layer-semigroup`。



当前素数路线总览：[证明路径与剩余猜想](outputs/triple_average_prime_proof_roadmap.md)。按已解无限族、统一标准核入口、正向种子、同余生成与终端分层，分别列出强资源猜想、有限Schreier目标及更弱的合法单轨道目标，避免把充分条件当成必要条件。该页主体写于47元完成后；后续53、59已经补齐，当前最小未解为71。



最新完整结果：[47元判据](outputs/triple_average_forty_seven_arithmetic_complete.md)。一个固定宽度一尖点词与两个伸缩校正给出E12(Z[1/6])及E21(47Z[1/6])；18个完整Schreier生成元逐个正向消元，实现共轭Gamma_0(47)，独立折叠为48陪集。统一桥与Bezout输送完成全部47元输入。47已进入因子闭包，最小未解维数现在为53。入口 `python work/run_verifications.py --id n47-complete`。



最新一般定理：[局部化Iwahori生成与通用尖点公式](outputs/triple_average_localized_iwahori_generation.md)。对任意素数p，若正向群提供Z[1/(p-1)!]上的上根、p倍下根及相应对角单位，则统一标准代表和三因子消元证明包含Gamma_0(p)。另有任意奇次三进返回产生宽度一尖点的恒等式。剩余统一任务是这些资源的原维数物理实现，非再次逐素数猜同余群。



此前：[正向根群饱和与统一素数策略](outputs/triple_average_positive_root_saturation.md)。一般迹根引理将逆元构造化为一个线性有理方程；固定三层证书已让旧167个B47宏全部获得正向逆，连同新增对合共170个。原Q(sqrt89)共轭目标已有57次模板的正向实现；整数换基后正向群包含E12(47Z[1/6])、E21(47Z[1/6])两整族。该阶段未完成的同余包含已由上面的n47-complete补齐。独立入口 `python work/run_verifications.py --id b47-root-activation`，不运行发现搜索。



该页同时给出统一素数猜想的准确形式：正向群包含共轭Gamma_0(p)即足够，由同一个Bezout公式收尾。全部p=1 mod3素数与合数归约已经统一；剩余难点是p=2 mod3的普遍正向生成，不是逐素数重做终端分类。



此前47元进展：[额外原子平均、正向对合与平移根群](outputs/triple_average_b47_extra_atom_and_adjoint.md)。一次额外预备三平均产生三个新对合，并使标准A0等六个旧宏获得正向逆；固定词进一步生成全部U(47t)、t属于Z[1/6]，为后来n47-complete提供种子。入口 `python work/run_verifications.py --id b47-extra-atom-involutions`。



同页给出倒序平均的能量伴随接口：旧167库只有15个反向模板通过全参数适用域，均未新增宏。一般同型对合的两两乘积还落在同一分裂环面，不能仅靠该族对合推断模群有限指数。



最新统一工具：[全局谱平衡与周期判据](outputs/triple_average_projective_spectral_balance.md)。Newton多边形与Kronecker定理将任意秩有理宏的有限射影阶，等价为半单性、实谱等模及一组特征系数整数性；Ad表示给出给定矩阵的多项式时间分圆验证算法。它不解决宏词的存在性，最小未解仍为47。



[47元当前库周期边界](outputs/triple_average_b47_cycle_frontier.md)精确排除167模板中长度至多4的有限周期，以及全部j>=0的A0^jBC。四因子部分用整数模筛选，737665600组合仅3896个需要完整整数复核。该排除不延伸到更长词或其他宏库。



最新一般结构：[等值载体与二进重分组](outputs/triple_average_paired_carrier_reset.md)。全部n=3r+2、奇数r>=5的合法状态可进入二重等值载体核；一个4r-3步的原维数宏给出W=2V、V属于GL_r(Z[1/3])，坐标和差分理想都恰乘2。单独载体交换的标量周期被奇偶不变量排除，新宏的全局周期仍未证明。入口 `python work/run_verifications.py --id paired-carrier-two-adic-reset`，最小未解维数仍是47。



最新：[四十一元完整判据](outputs/triple_average_forty_one_arithmetic_complete.md)。21个通用宏、10个正向三因子对合和10个整数词给出完整42陪集的共轭Gamma_0(41)，唯一合法尖点归零。41已加入因子闭包，最小未解维数现在为47。入口为 `python work/run_verifications.py --id n41-complete`。



[有限模调度的高度边界](outputs/triple_average_modular_height_barrier.md)给出一个统一精确族：全部指定非三剩余类和G保持不变、实能量下降，但本原整数高度按3^(2h)增长。它不否定已证的模调度桥，说明终止还需完整操作词的实／三进联合控制。



统一接口：[有限模正向控制与二例外归约](outputs/triple_average_two_carrier_modular_bridge.md)。对全部n>=17且n=5 mod6，包括合数，直接用混合好划分、双载体有限模调度及合法n-2元调用进入(u^(n-2),a,b)核；不需安全能量下降或因子归纳。形式逆只在有限模数上正向化，不能据此声称核必终止。入口为 `python work/run_verifications.py --id two-carrier-modular-bridge`。



再用一步真实三平均可安全进入标准B_n，故这个n族的多危险素数标准核接口也已闭合。其一般原则是：全域可执行且行列式为三进单位的正向宏，与形式群在所有非三有限商上轨道相同；精确归零仍需另证。



此前：[二十九元完整判据](outputs/triple_average_twenty_nine_arithmetic_complete.md)。18个通用宏、9个三因子正向周期和7个整数词给出共轭Gamma_0(29)的完整30陪集证书，唯一合法尖点可归零。29已进入因子闭包。入口为 `python work/run_verifications.py --id n29-complete`，不运行浮点发现搜索。



无限族：[全部p=1 mod3素数的完整判据](outputs/triple_average_split_prime_gaussian_controller.md)。原p个位置上的高斯周期层提供全局正向标量循环；一个范数一分圆单位保证单位剪切，再由整数仿射格正规形完整归零。所有这类素数及其因子闭包已解决，包含31、37、43、61、97等。结合29、41元证书，剩余统一问题归约到p=2 mod3、从47开始的素数。核验入口 `python work/run_verifications.py --id split-prime-gaussian-controller`。



此前原维数进展：[平坦核形式群的统一算术性](outputs/triple_average_flat_star_arithmeticity.md)。所有p>=13的素数核可进入同一个一／二载体框架；显式幺幂与高秩初等同余群定理证明其形式群整数部分有限指数。模2和模p的第一层联合像及终端代表也已统一。该一般框架的整体正向实现仍开放；29元后来由独立三因子周期证书解决。



[置换剩余像与局部耦合](outputs/triple_average_permutation_shadow_entanglement.md)证明：九十一元旧21504容器严格大于特定宏群，新的必要容器指数为43008。对应紧模曲线有无分歧二重覆盖和Jacobian二阶线丛解释。旧容器及其有限搜索标签完整保留。



最新结构定理：[数字算子的完整同余群](outputs/triple_average_digit_congruence_group.md)。平衡剪切与置换恰生成全部整数保和／保常值群；加入数字算子后，群恰为模n倍率属于3的循环子群的同余群，并有显式分裂扩张和全部有理射影轨道分类。所有合法方向只有一个轨道，但正向实现仍使用三份复制。入口为 `python work/run_verifications.py --id balanced-digit-congruence-group`。



此前结果：[一次三份复制稳定化](outputs/triple_average_one_tripling_stabilization.md)。所有 $N\ge9$ 且 $3\mid N$ 的维数已无条件解决，包括含当前未解素数47的141元；任意合法有理输入只需复制三份即可归零。证明把离散梯度／Hilbert 90、真实副本剪切与整数仿射格轨道分类接起来。原维数复制消去仍开放。入口为 `python work/run_verifications.py --id one-tripling-stabilization`。



其他AI结构图景的最新复核见[局部到整体与数域边界](outputs/triple_average_structural_picture_audit.md)：保留原稿，纠正合法域不能单独决定高次level、数域扩张不改变固定输入可达性、内容理想不能替代R加法模等问题。



该复核第11节记录29元原1195模板的周期边界：没有二因子有限周期，且所有指数j>=0的A^jB均被排除。新完整证书使用三个不同因子，因而不与旧边界冲突。



一般结果：[任意维数严格归约到素数](outputs/triple_average_all_dimensions_to_primes.md)。全部合数的接口已闭合，原猜想等价于仅证明全部素数p>=7。当前结合分裂素数族与29、41元基例，已解所有n>=7且素因子属于2、5、11、17、23、29、41或p=1 mod3的维数，并另有全部三整除维数。入口为 `python work/run_verifications.py --id even-prime-power-halving --id all-dimensions-prime-reduction`。



最新一般突破：[奇数合数的乘法闭包](outputs/triple_average_odd_composite_factor_closure.md)与[25元完整判据](outputs/triple_average_twenty_five_arithmetic_complete.md)结合后，全部奇数n>=7已严格归约到全部p>=7素数。当前已解P={7,11,13,17,19,23}的任意乘积和素数幂，再乘任意三幂、五幂都已解决，包括25、35、49、77、91、121、125等无限族。入口为 `python work/run_verifications.py --id n25-complete --id odd-composite-factor-closure`。



此前该证明先覆盖8整除维数；最新的低二进重数桥已将v2=1、2也接入因子归约，所以现在允许任意二幂因子。



此前[二例外因子桥](outputs/triple_average_prime_first_factor_reduction.md)的最优准备步数结论仍保留，构造已推广到d+2例外核心。剩余统一任务是素数核的正向可达性。



现代框架的主线复核与可执行定义见 [Modern Frame 严格化契约](outputs/triple_average_modern_framework_review_and_contract.md)；奇素数维数的策略限制见 [子问题调用下界](outputs/triple_average_subproblem_prime_obstruction.md)。



项目背后的统一结构猜测见[局部算术轨道图景](outputs/triple_average_structural_picture_conjecture.md)：它区分已证的同余子群样本、因子归约的组合接口，以及尚待证明的正向算术轨道与终端覆盖。



此前基例：[二十三元完整判据](outputs/triple_average_twenty_three_arithmetic_complete.md)。三个固定原子宏生成共轭 Gamma_0(23) 的指数24充分子群。入口为 `python work/run_verifications.py --id n23-complete`；原固定词证书保持可复现。



同轮完成：[十九元及其三进塔](outputs/triple_average_nineteen_arithmetic_complete.md)，通过通用十五元调用生成指数20充分子群。其内部子问题路径允许依赖参数，与二十三元的固定原子词证书不同。



[素数维数与同余子群的准确关系](outputs/triple_average_prime_congruence_structure.md)给出一般p进稳定子定理和真实循环的尺度约束，不能据已解例子断言所有素数都自动生成足够大的群。整系数宏编译器在搜索前加入重数与支撑格缓存，并与旧版95个十七元矩阵逐项对照。



此前完成：[十七元及其三进塔](outputs/triple_average_seventeen_arithmetic_complete.md)。固定原子逆词给出共轭 Gamma_0(17) 的指数18充分子群，独立入口为 `python work/run_verifications.py --id n17-complete`。



发现方法见[参数无关子问题模判据与范数环面](outputs/triple_average_universal_subproblem_lattice.md)：任意参数维数的模板合法性可用局部化整数模包含判定。该页保留旧库与局部调度阶段，当前完成状态以上面的十七元定理为准。



此前的一般族：[全部二三光滑维数的完整判据](outputs/triple_average_two_three_smooth_complete.md)，涵盖所有 n=2^a·3^b≥7。独立入口为 `python work/run_verifications.py --id two-three-smooth-complete`。



此前完成：[十四元及其三进塔](outputs/triple_average_fourteen_complete.md)。[图论核心定理](outputs/triple_average_blocker_graph_core.md) 同时将一般安全终端的重复值下界提高为 n-d-2。核验入口为 `python work/run_verifications.py --id blocker-graph-safe-core --id n14-complete`。



此前完成：[十五元及其三进塔的完整判据](outputs/triple_average_fifteen_via_subblocks_complete.md)，通过模8调度调用十二元和十元子问题。[偶维 B 核减半桥](outputs/triple_average_even_kernel_halving_bridge.md) 仅提供核内接口，十四元高维部分由最新证明补齐。入口为 `python work/run_verifications.py --id n15-via-subblocks-complete`。



此前完成：[十二元及其三进塔的完整判据](outputs/triple_average_twelve_arithmetic_complete.md)。真实正向宏含共轭于 Gamma_0(8) 的指数 12 子群，唯一合法尖点可终止。独立核验入口为 `python work/run_verifications.py --id n12-complete`。



进一步完成：[十八元及其三进塔](outputs/triple_average_eighteen_via_twelve_complete.md)，通过可解十二元子块和重数配对归零。B21 搜索已改用[整数状态引擎](outputs/triple_average_b21_integer_search_optimization.md)，同样八进程约 11 秒完成。



## 从哪里开始



1. 先读[统一素数证明](outputs/triple_average_prime_double_triple_invariant.md)及[本轮复盘](outputs/triple_average_binary_source_reassessment_2026-09-11.md)，再按需要查阅 [`outputs/triple_average_research_handoff_2026-09-09.md`](outputs/triple_average_research_handoff_2026-09-09.md)中的历史结构。

2. 再读 [`outputs/triple_average_research_corrections.md`](outputs/triple_average_research_corrections.md)，避免继续使用已经撤回或修正的旧结论。

3. 用 [`outputs/triple_average_verification_guide.md`](outputs/triple_average_verification_guide.md) 查找每项结论对应的文档、脚本、命令、预期输出和证据边界。

4. 机器可读映射位于 [`work/verification_manifest.json`](work/verification_manifest.json)，统一入口为 [`work/run_verifications.py`](work/run_verifications.py)。



计算资源使用、性能剖析和九十一元 `24/24` 有限深度覆盖见 [`outputs/triple_average_computation_performance_audit.md`](outputs/triple_average_computation_performance_audit.md)；外部减暴力建议的逐项核对见 [`outputs/triple_average_search_optimization_review_2026-09-09.md`](outputs/triple_average_search_optimization_review_2026-09-09.md)。



标准核接口、自守/adelic 路线与 n=12 首个二维核实验见 [`outputs/triple_average_kernel_interface_and_automorphic_route.md`](outputs/triple_average_kernel_interface_and_automorphic_route.md) 和 [`outputs/triple_average_b12_kernel_experiment.md`](outputs/triple_average_b12_kernel_experiment.md)。



统一的现代结构语言见 [`outputs/triple_average_unified_modern_framework.md`](outputs/triple_average_unified_modern_framework.md)：将状态视为有向重写纤维，把三平均视为 A2 投影，并用带适用域的有向范畴组织跨核操作。只有具有正向逆词的部分才构成群胚。主文件已重写，原稿完整存档在 outputs/history/。



最新的可执行统一接口见 [`outputs/triple_average_template_compiler_and_torus.md`](outputs/triple_average_template_compiler_and_torus.md)：用 Smith 格判据编译参数无关子问题调用，并用虚二次范数环面组织 B17 的行列式 3 宏。



任意 \(q\)-平均的根格必要条件、原子秩与宏秩区分、\(S\)-算术控制器猜想见 [`outputs/triple_average_q_average_arithmetic_geometry.md`](outputs/triple_average_q_average_arithmetic_geometry.md)。



从本目录运行：



```text

python work/run_verifications.py --list

python work/run_verifications.py --profile smoke

python work/run_verifications.py --profile core

```



`full` 档包含九十一元深度四、cusp 29 深度五及 B12/B15/B18/B21 的有限实验，会运行数分钟。新增标准接口、宏族和 theta 格对应见 [三进扩张修复](outputs/triple_average_carry_repair_and_arithmetic_interface.md)；审核修订见 [audit 修订记录](outputs/triple_average_audit_resolution_2026-09-09.md)。单项核验可用 `python work/run_verifications.py --id <ID>`。



## 目录约定



- `outputs/`：证明、综合、勘误、交接和验证指南。最新交接稿与勘误优先于早期探索稿。

- `work/`：验证证书、有限实验、搜索程序、辅助模块和历史缓存。其内部说明见 [`work/README.md`](work/README.md)。



现有文件保持原位，以免破坏旧文档中的路径和历史可追溯性。文件名前缀只能表示作者当时的用途；一个 `verify_*` 文件是否构成证明证书，必须以验证清单中的 `evidence_level` 和 `evidence_scope` 为准。


����߽磺�����ഢ���ƽ��У�v=0��1��ֱ�ӽ�������alpha=p-2ʱ�������޵���������壻��˶�����հ�������ȱ�ڡ�


2026-09-12形状势的文献接口：[零和组合文献接口](outputs/prime_arity_shape_potential_literature_interface.md)已阅读Grynkiewicz 2006计数定理、2007逆EGZ及2011 Graham结构。它们支持“失败池低支撑/高重桶”方向，但仍需原位置保护与整数返回宏；不宣称已解决全局终止。

2026-09-12形状变化势的关键未解结构：[单值零和双高重猜想](outputs/prime_arity_single_value_zero_sum_conjecture.md)：长度N>=3p+1的C_p序列若所有p项零和都单值，猜想两大余数重数和至少3p-2；这将直接接上已有双重值整数闭包。与Grynkiewicz零和计数和逆EGZ文献相符，p=3,5,7有限枚举支持，但目前仍是猜想。

2026-09-12结构定理：无混合p项零和的余数池中，重余数桶至多两个；双桶覆盖全池，单桶至少N-p+1。该结论由删至p-1后应用EGZ严格证明，单桶背景宏仍需历史约束。

修正：无混合零和重数结构定理的适用范围明确为 3p+1≤N<4p；超出上半带不外推。
<!-- END SOURCE doc-437d08f2e4fd -->

---

<a id="doc-7fe8564de066"></a>

## 原文导签：核内缺口文献访问记录

来源：`work/document_reorganization_20260915/originals/work/core_gap_literature_20260914/README.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/work/core_gap_literature_20260914/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-7fe8564de066 -->
# 核内缺口文献访问记录

整理日期：2026-09-15。目录名保留最初创建日期。数学复查见[正文](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_core_gap_reassessment_20260915.md)。

## 已取得并阅读相关正文

* Kim--Lee--Liao, “Odd-odd continued fraction algorithm” (2022)，[DOI](https://doi.org/10.1007/s00605-022-01704-2)。文件 odd_odd_publisher.pdf/txt。阅读引言、第2节及有理终端讨论：两种 cusp 和有限/形式周期行为。未把最佳逼近性质当作平均可达性定理。
* Alahmadi--Jain--Lam--Leroy, “Euclidean pairs and quasi-Euclidean rings” (2014)，[DOI](https://doi.org/10.1016/j.jalgebra.2014.02.009)。出版下载受阻后，从[作者页面所列PDF](https://leroy.perso.math.cnrs.fr/Articles/SubmitRevised-EucDom.pdf)取得稿件，文件 quasi_euclidean_author.pdf/txt。已读定义、定理8、命题10、定理11及对应证明。另存作者2014年讲义 quasi_euclidean_lecture.pdf/txt。正文与讲义的定理编号不同，以正文编号引用。
* Fiacchini--Jungers--Girard (2018)，[DOI](https://doi.org/10.1016/j.automatica.2018.03.039)。复用旧缓存 ../literature_strategy_20260912/control_language_2018.txt，重读定义6--7与定理1--2；没有重新下载。

## 外部定理引用和全文边界

Furstenberg (1967)，[Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation](https://doi.org/10.1007/BF01692494)。本轮引用其标准一维拓扑定理：乘法独立整数作用下的无限闭不变子集只能为整个圆周。原文PDF请求实际返回出版HTML，保存为 furstenberg_minimal_sets.html；未宣称读到原证明。

Berend (1983)，[Multi-invariant sets on tori](https://doi.org/10.1090/S0002-9947-1983-0716835-6)。保存的 furstenberg_berend.html 是AMS出版页面，不是PDF。页面中相应文章摘要明确说其推广一维结果，研究的性质是唯一无限闭不变集为整个群。它支持定理性质与来源核对，不替代原文证明。本轮有限例外推论明确把Furstenberg拓扑定理列为外部依赖。

取得的Tao 2020年获奖介绍没有提供所需具体定理，不把该页面计作证明来源。Furstenberg的一维拓扑定理与测度版本的乘法不变测度猜想不是同一个命题。

## 只有摘要或题录

* Kushwaha--Sarma, “Farey-Subgraphs and Continued Fractions” (2022)，[DOI](https://doi.org/10.1556/012.2022.01525)，arXiv:2106.14856。OpenAlex摘要写明其图仅在1或素数幂时连通；arXiv、export、ar5iv及出版下载未取得正文。图定义没有核对，不能认作本题的轨道图。
* Cooke--Weinberger (1975)，[DOI](https://doi.org/10.1080/00927877508822057)。题录来自本轮及旧检索；定理假设、可能的条件性及商的允许集合未全文核对，不作为证明依赖。
* Kontorovich (2013)，[DOI](https://doi.org/10.1090/S0273-0979-2013-01402-2)。AMS请求返回HTML而非PDF；不能称阅读全文。
* Bourgain--Kontorovich (2014)，[DOI](https://doi.org/10.4007/annals.2014.180.1.3)。题录核对，PDF请求失败；没有移植密度一为逐输入结论。

## 检索和数据含义

query_00.json 至 query_15.json 保留16组关键词查询，涉及受限连分数、Farey图、除法链、互素间隙、控制Lyapunov函数和薄轨道。部分查询遇到HTTP429，部分只有不相关结果。16组查询不代表16篇全文阅读。

每个下载的 *_source.json 保留请求URL、实际URL、内容类型及取得文件的SHA256；失败请求保存错误。只有文件头确为PDF的结果才交给pdftotext。零字节、HTML和挑战页不计入全文证据。

相关数学程序为 ../verify_core_gap_four_lifts.py。程序不验证任何上述外部一般定理。

<!-- END SOURCE doc-7fe8564de066 -->

---

<a id="doc-2632e7b8ffd6"></a>

## 原文导签：H_t文献来源与访问等级

来源：`work/document_reorganization_20260915/originals/work/ht_literature_20260915/source_index.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/work/ht_literature_20260915/source_index.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-2632e7b8ffd6 -->
# H_t文献来源与访问等级

检索日期：2026-09-15。研究结论见[报告](../sources/work/document_reorganization_20260915/originals/outputs/ht_literature_and_eventual_square_completion_20260915.md)。*_source.json记录原URL、最终URL、时间、状态、文件长度和SHA256；失败也保留。

## 取得全文并实际阅读相关段落

1. Paul Pollack, *Bounds for the first several prime character nonresidues*, Proc. Amer. Math. Soc.145(2017),2815–2826，DOI [10.1090/proc/13432](https://doi.org/10.1090/proc/13432)。
   [作者PDF](https://www.pollack-math.net/hudson.pdf)；本地pollack_hudson.pdf／.txt。直接读第1–4页、第8页和参考文献；定理2.7页图像pollack_theorem27.png已查看。最重要来源：定理1.1覆盖所有非主字符，定理2.7覆盖所有真子群。
2. Greg Martin、Paul Pollack, *The average least character non-residue and further variations on a theme of Erdős*, J. London Math. Soc.87(2013),22–42，DOI [10.1112/jlms/jds036](https://doi.org/10.1112/jlms/jds036)。
   [作者保存的出版PDF](https://personal.math.ubc.ca/~gerg/papers/downloads/ALCNFVTE.pdf)；本地martin_pollack2013_author.pdf／.txt。直接读印刷第22–25页，特别是Bach3log²n引用、Norton界和特征群引理；没有把平均值定理用作最坏情形界。
3. Elchin Hasanalizade、Hua Lin、Greg Martin、Andradis Luna Martínez、Enrique Treviño, *Explicit Burgess inequalities for cubefree moduli*, [arXiv:2511.17778](https://arxiv.org/abs/2511.17778)，作者当前预印本。
   [作者PDF](https://personal.math.ubc.ca/~gerg/papers/downloads/EBICM.pdf)；本地cubefree2025_author.pdf／.txt。直接读第1–3页及相关证明条件、参考文献；第2页图像cubefree_page2.png已查看，确认10^1145门槛。

## 题录、摘要或经已读文献间接核对

4. Karl K. Norton, *A character-sum estimate and applications*, Acta Arith.85(1998),51–78，[DOI](https://doi.org/10.4064/aa-85-1-51-78)。期刊页norton1998_journal.html确认题录；PDF下载403。定理1.20／1.30由Pollack正文明确引用，未声称读过Norton原证明。
5. Glyn Harman, *Integers without large prime factors in short intervals and arithmetic progressions*, Acta Arith.91(1999),279–289，[DOI](https://doi.org/10.4064/aa-91-3-279-289)。Crossref题录harman_metadata.json。MathOverflow答复指向定理3；原PDF403。一次猜测式期刊URL返回期刊首页，不作为论文正文。
6. Eric Bach、Lorenz Huelsbergen, *Statistical evidence for small generating sets*, Math.Comp.61(1993),69–82，[DOI](https://doi.org/10.1090/S0025-5718-1993-1195432-5)。OpenAlex摘要oa_bach1993.json、Crossref元数据。读到的是题录和摘要，PDF403。其对数级最坏界是启发性猜想。
7. Eric Bach, *Explicit bounds for primality testing and related problems*, Math.Comp.55(1990),355–380，[DOI](https://doi.org/10.1090/S0025-5718-1990-1023756-8)。PDF403；准确GRH条件性3log²n版本在上面的Martin–Pollack出版论文第22页读到。
8. Niraek Jain-Sharma、Tanmay Khale、Mengzhen Liu, *Explicit Burgess bound for composite moduli*, IJNT17(2021),2207–2219，[DOI](https://doi.org/10.1142/S1793042121500834)。出版元数据、arXiv:2010.09530题录；原文访问失败。其精确r=2定理在2025预印本第1页Theorem A直接读到。
9. Forrest J. Francis, *An investigation into explicit versions of Burgess' bound*, JNT228(2021),87–107，[DOI](https://doi.org/10.1016/j.jnt.2021.03.018)。题录及2025论文对其素数模数范围的介绍；未读全文，不用于独立推论。

## 论坛检索线索

- [2014年小生成元问题](https://mathoverflow.net/questions/165809/)，及[Lucia答复](https://mathoverflow.net/a/165816)：完整读取，明确联系Harman定理3、光滑数和短特征和。正式证明引用Pollack全文。
- [2023年小比值表示](https://mathoverflow.net/questions/451422/)及两条回答：完整读取，抽屉原理适用于素数模数，论文报告已给自足证明；没有把论坛的素数结论扩为所有合数。

## 检索与计算边界

- research_ht_literature.py保存12个通用网页查询和20个主题题录查询；另外的oa_*、cross_*、mo_*、mse_*文件记录适应性追查。通用网页有明显不相关结果，未将这些条目当文献证据。
- 三份PDF通过文件头确认，使用pdftotext读取；关键公式另核对页面图像。
- 题录去重数是检索覆盖指标，不是阅读全文数。数学结论仅依据报告明确列出的原文段落。
- ht_through999_certificate.json是全部2<=t<1000的有限群生成证书。它不提供无条件大参数界，也不证明外部定理。
- 本次没有联系作者或发表帖子，没有以GRH为无条件前提。

<!-- END SOURCE doc-2632e7b8ffd6 -->

---

<a id="doc-c65dbe373e50"></a>

## 原文导签：Literature retrieval, 2026-09-12

来源：`work/document_reorganization_20260915/originals/work/literature_20260912/README.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/work/literature_20260912/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-c65dbe373e50 -->
# Literature retrieval, 2026-09-12

The dated survey is `../../outputs/averaging_literature_survey_2018_2026.md`.
`../literature_survey_20260912.py` retrieves public metadata and pages with a
content cache. JSON filenames are hashes of request URLs and parameters; each
record preserves the final URL, HTTP status, retrieval date, and response body.
Text files with hashed names contain parsed page text.

Downloaded primary documents:

- `gonzalez_thesis_2019.pdf` / `.txt`: Miguel Coviello Gonzalez's UC Riverside dissertation, September 2019; https://escholarship.org/uc/item/4wb2g5z2
- `weighted_inverse_2022.pdf` / `.txt`: Adhikari, Hegde, Molla, Sarkar, Integers 22 (2022), A7; https://math.colgate.edu/~integers/w7/w7.pdf
- `splitter_2024.pdf` / `.txt`: Couetoux, Gastaldi, Naves, FUN 2024; https://doi.org/10.4230/LIPIcs.FUN.2024.9

The PDF text was extracted with TeX Live's pdftotext. No network execution,
messages to authors, account sign-in, or access-control changes were performed.

Limits: direct arXiv and Google connections failed; Semantic Scholar later
requests were rate-limited; several publishers exposed only abstracts. OpenAlex
author records and publication versions had merge errors. Bibliographic matches
were checked against publisher or author records where available. Citation
counts and absence of search hits do not prove that a result is absent from the
literature. The survey distinguishes primary-text reading from abstract-only
inspection and does not integrate unreviewed external algorithms into solvers.

<!-- END SOURCE doc-c65dbe373e50 -->

---

<a id="doc-dc13379c0453"></a>

## 原文导签：2026-09-14研究审查材料

来源：`work/document_reorganization_20260915/originals/work/research_audit_20260914/README.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/work/research_audit_20260914/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-dc13379c0453 -->
# 2026-09-14研究审查材料

## 2026-09-15 强CSP专项补核

新增取得Prasad--Rapinchuk正式出版综述 *Developments on the congruence subgroup problem after the work of Bass, Milnor and Serre*, Collected Papers of John Milnor, Vol.V, AMS,2010,307-325。

- [19页重印PDF](prasad_rapinchuk_milnor_survey_2010.pdf)、[提取文本](prasad_rapinchuk_milnor_survey_2010.txt)、[第309页图像](prasad_rapinchuk_survey_page309.png)。已读取第2.1至2.3节、命题1、第4节定理3的相关陈述及参考文献[49]，并查看第309页原图。
- [作者题录](https://uva.theopenscholar.com/andrei-rapinchuk/publications/developments-congruence-subgroup-problem-after-work-bass-milnor-and)直接链接[重印文件](https://uva.theopenscholar.com/files/ixqrlw/files/milnor_survey_8.pdf)。实际下载为application/pdf，571108字节；SHA256：`CA19042C85BDF4E7E3E62F7ED66BD81E6CEC33456F65902715E472E7C9B140A1`。
- 第309页第2.3节明确给出SL2在|S|>1且S含非复数处时同余核平凡；同页命题1和第308页经典CSP定义给出每个有限指数子群包含主同余子群。第324页[49]对应Serre 1970。
- 对R=Z[1/q]、q>1，S包括实无穷处与至少一个有限素数处，因而适用。此来源同时支持奇素数局部化环，不局限于Z[1/2]。
- Serre 1970原文仍未全文取得：Annals官方题录页仅提供DOI，JSTOR请求返回HTML；arXiv访问连接重置。未将这些失败请求计作论文全文。成功取得的是上述作者提供的正式综述。

适用性与区间证明的完整审核见[专项报告](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_lower_band_external_theorems_audit_20260915.md)。下面保留9月14日原始访问范围，勿将旧的“仅二进交叉支持”当作补核后的全部证据。

本次先复查双锚点碰撞、不同值归约、单位补回、精度反例、端点主元与CRT证书。实质推进发生在端点受限群生成：找到Morris 2007的有限指数子群内部生成定理，与Serre同余子群性质及显式有限环消元接通。证明见[合数端点核心闭合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)。

## 实际使用的来源

| 材料 | 核对内容 | 证据边界 |
|---|---|---|
| [Morris 2007 PDF](morris_muni.pdf)、[提取文本](morris_2007.txt) | 定义、定理6.1(2)、5.13、引理6.9及推论6.10；秩二及无限单位条件 | 已读相关原文；没有重新证明Carter-Keller-Paige的深结果 |
| Serre 1970，DOI 10.2307/1970630 | 所用标准特例：SL2(Z[1/2])有限指数子群包含主同余子群 | 原文全文下载未成功；[专家答复原始记录](serre_special_case_crosscheck.json)交叉确认特例；正式证明明确以Serre定理为外部依赖 |
| [Mennicke 2000 PDF](mennicke_2000.pdf)、[文本](mennicke_2000.txt) | 区分直接初等生成与正规闭包，及定理中的阶数>=3前提 | 未把该高阶结果套用于SL2 |
| 原有Morgan-Rapinchuk-Sury 2018缓存 | 整个SL2的9因子定理及参考文献 | 该定理本身不解决本题受限根群；它的参考文献帮助定位Morris原文 |

Morris来源：https://emis.muni.cz/journals/NYJM/j/2007/13-17.pdf 。作者出版列表确认刊名、年份、页码。Morris PDF SHA256：F690AD629791A30284E3E7FF7EDE152B874314D218138CB2A41CEFB24FAB902E。

Mennicke来源：https://journals.msp.org/mscand/article/download/916/915 。PDF SHA256：E2DD023379F87B82DA56BE88F74042FCB1C16EEB5D538CD60B14AF4A7003AC57。

## 检索与未使用材料

通过OpenAlex题录、作者出版页、期刊/EMIS镜像定向查询relative elementary groups、congruence subgroup generators、Mennicke symbols、Farey symbols、Carter-Keller-Paige及相关零和结构。题录命中只作线索，不作为定理证明。

Morris《Introduction to Arithmetic Groups》下载后仅检索了同余与S算术相关部分，未用于新增证明。Milne的AG.pdf实际为《Algebraic Geometry》，已按实际标题更名且未使用。若干所谓PDF地址返回的是HTML跳转页，已改名为redirect.html，不能当作已下载论文。首页、错误跳转和目录页保留为访问记录。

## 核验范围

[核验程序](../verify_endpoint_congruence_completion.py)及[结果](../endpoint_congruence_completion_records.json)只核查任意商分解公式、平衡单位、陪集归约与既有正向编译接口。完整一般量词由专题证明及其明确外部定理承担。没有平均词发现搜索，没有新增高效任意核心分解算法。

<!-- END SOURCE doc-dc13379c0453 -->

---

<a id="doc-d3d10b427f39"></a>

## 原文导签：Danus — Architecture

来源：`work/documentation_memory_20260917/harness_sources/danus/ARCHITECTURE.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/danus/ARCHITECTURE.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-d3d10b427f39 -->
# Danus — Architecture

Danus turns the Rethlas single-problem proof engine (a codex agent plus proving
skills, inherited rather than redesigned) into a multi-agent, long-running,
strategy-steered research system, and renders verified results into papers and
human progress reports. This is the as-built map: the layered model, the folder
layout, the invariants, and the pinned cross-module contracts.

For the main agent's operating contract, see `AGENTS.md`
(→ `agents/contracts/main_agent.md`).

---

## 1. Layered model

```
operator → ① orchestration (main agent + danus CLI)   — conducts, never does math
              ② strategy   (the main agent's own periodic synthesis: elaboration → master_guidance)
              ③ execution  (worker swarm; each round = one codex session running the Rethlas proving skills)
   gm_* │         │ fact_submit
        ▼         ▼
   ⑤ truth      ④ verification (cold-start codex judge; correct ⟺ no critical_errors AND no gaps)
   (fact graph + memory)   — a fact exists iff the verifier accepted it
        ▲
        │ every read/write goes through …
   ⑥ gateway (role-gated MCP: 6 tools; main has NO fact_submit; verifier read-only)

cross-cutting: ⑦ observability (dashboard · theorem-search · human-summary · initialize)
               ⑧ ops/runtime (bootstrap · services · doctor · config)
bottom (inherited, don't redesign): Rethlas proof core = codex + worker proving skills
output: write-paper (publication) · human-summary (progress report) — each rendered by an isolated codex
```

---

## 2. Folder layout

```
Danus/
├─ ARCHITECTURE.md              this file (map + invariants + interface contract)
├─ README.md   pyproject.toml   top-level intro + the installable `danus` package
├─ .gitignore  .codex/          MCP wiring (`config.toml`): the `danus` gateway + the `write-paper` and `human-summary` services
├─ config/                      env templates (BYO key; only *.env.example committed)
├─ danus/                       THE ENGINE (installable Python package)
│  ├─ core/                     ⑤ truth: schema · factgraph · global/local memory · bm25 · glossary
│  ├─ gateway/                  ⑥ role-gated MCP: 6 tools · role table (roles.py)
│  ├─ verify/                   ④ verification HTTP service · prechecks · cold-start codex launcher
│  ├─ execution/                ③ worker swarm: round loop · project/worker lifecycle + layout
│  ├─ orchestration/            ① the `danus` CLI verbs
│  ├─ integrations/             arXiv theorem search (Matlas)
│  ├─ observability/            read-only dashboard
│  ├─ authoring/                shared main-only renderer primitives: the one-shot isolated codex driver + common helpers
│  ├─ write_paper/              write-paper MCP service: assembler + tools (drives `danus.authoring`)
│  └─ human_summary/            human-summary MCP service: scrubbing assembler + tool (drives `danus.authoring`)
├─ agents/                      AGENT CONTRACTS + CODEX-FACING SKILLS (data, not Python)
│  ├─ contracts/                main_agent.md · worker.md · verifier.md
│  └─ skills/
│     ├─ worker/                9 proving skills (inherited from Rethlas)
│     ├─ verify/                3 verify skills
│     └─ write-paper/           paper role prompts + house style (embedded by the write-paper MCP)
├─ .agents/skills/              MAIN-AGENT SKILLS (codex auto-discovers)
│  ├─ elaboration/  human-summary/  initialize/
│  └─ write-paper/              the recipe SKILL.md + driver/ scripts + templates/
├─ bin/                         thin wrappers: danus · danus-mcp · write-paper-mcp · human-summary-mcp · codex
├─ scripts/                     bootstrap · doctor · services · env · setup/check-codex · start-verify/-dashboard · recover · install-tex
├─ docs/                        human docs: getting started · concepts · operating guide · security & trust · …
└─ examples/                    unattended-ops examples + a toy project
```

---

## 3. Design invariants (must not regress)

1. Three memory tiers, one correctness boundary: local (private) → global
   (shared awareness) → fact graph (the only truth). A proof may build only on
   `fact_id`s; global memory is never a correctness source.
2. Permission is enforced by which tools a role can even see (the gateway role
   table), not by prompt convention. `main` cannot `fact_submit`; `verifier` is
   read-only.
3. The verifier is the sole write-gate. A fact exists only if a `correct` verdict
   came back; the gate lives in the `fact_submit` code path, not in prose.
4. Content-addressed, cascade-revocable fact graph. `fact_id` hashes content
   (problem_id + predecessors + glossary_introduces + statement + proof);
   `external_refs` is deliberately excluded so the paper pipeline can rewrite
   citations without breaking the DAG.
5. Autonomy and resumability. Workers run detached; a "round" continues from
   persisted memory rather than adding one increment, so no single crash loses
   verified work.
6. The main agent's own reasoning is the brain. Between rounds the main agent
   reasons over the shared stores itself — optionally spawning exploratory codex
   subagents — distills the project's state into an `elaboration`, and writes the
   direction it decides on as the swarm's `master_guidance`. This periodic steer
   is not optional — it is how the swarm gets steered.
7. Portable and BYO. No hardcoded absolute paths, no committed secrets; keys come
   from gitignored `config/*.env` (templates committed as `*.example`).
8. Clean author context. Any agent that produces an artifact for an outside
   audience (a paper, a human report) is a fresh isolated codex fed a scoped,
   machinery-free prompt, never the orchestrator's own contaminated window. It
   cannot leak `fact_id`s or swarm vocabulary it never received.

---

## 4. Interfaces & ports — the coordination contract

> **Rule:** these rows are the seams where two modules meet. If a change touches a
> row, update both ends in the same change. Ports and contract shapes are pinned:
> one side must treat the other's contract as fixed, and must not change a port or
> interface unilaterally.

**Network ports (loopback — do not renumber):**

| port | service | producer → consumer |
|---|---|---|
| 8091 | verify `/verify`, `/health` | `danus.gateway` `fact_submit` → `danus.verify` (via `DANUS_VERIFY_URL`) |
| 8099 | dashboard | operator browser → `danus.observability` (read-only) |

**Cross-module contracts (both ends must agree):**

| contract | pinned shape | ends |
|---|---|---|
| MCP tool set + role gating | 6 tools; `roles.py` `ROLE_TOOLS` (main has NO `fact_submit`; verifier read-only) | `danus.gateway` ↔ worker/main/verifier agents |
| MCP launch | `python -m danus.gateway` + `DANUS_ROLE` env | `danus.verify` launcher · worker `.codex/config.toml` · `.codex/config.toml` (main) → `danus.gateway` |
| verify HTTP | `POST /verify {statement,proof}` → `{verification_report,verdict,repair_hints}`; verdict ⟺ no critical_errors & no gaps | `danus.gateway.fact_submit` ↔ `danus.verify` |
| fact id inputs | `problem_id + sorted(predecessors) + sorted(glossary) + normalized(statement,proof)`; **external_refs EXCLUDED** | `danus.core` ↔ everyone (write-paper reads `external_refs`) |
| global-memory kinds | the 11 `GLOBAL_KINDS` (incl. `master_guidance`/`elaboration`/`verification`) | `danus.core` ↔ agents |
| write-paper prompt assets | codex role prompts + style read from `agents/skills/write-paper/` (via `DANUS_WRITE_PAPER_SKILL_DIR`) | `danus.write_paper` assembler ↔ `agents/skills/write-paper/` |
| env-var contract | `DANUS_* / CODEX_* / VERIFY_*` names; the codex CALL + env (bin/model/effort/PATH/`exec` prefix) is resolved through the shared `danus.codex` launcher: neutral `DANUS_CODEX_BIN` / `DANUS_MAIN_MODEL` / `DANUS_MAIN_EFFORT` (back-compat aliases `DANUS_CODEX_MODEL` / `DANUS_CODEX_EFFORT`) + `DANUS_WORKER_MODEL` for workers + per-service `DANUS_{VERIFY,WRITE_PAPER,HUMAN_SUMMARY}_{MODEL,EFFORT}` overrides | `danus.codex` + `config/` + `scripts/env.sh` ↔ every codex-exec site (`danus.execution.loop` · `danus.verify.launcher` · `danus.authoring.driver`) |

<!-- END SOURCE doc-d3d10b427f39 -->

---

<a id="doc-37cf6743b1ed"></a>

## 原文导签：Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory

来源：`work/documentation_memory_20260917/harness_sources/danus/README.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/danus/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-37cf6743b1ed -->
# Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory

<p align="center">
  <a href="https://arxiv.org/abs/2607.06447"><img src="https://img.shields.io/badge/arXiv-2607.06447-b31b1b" alt="Danus paper on arXiv"></a>
  <a href="https://frenzymath.com/blog/danus/"><img src="https://img.shields.io/badge/Technical%20Report-frenzymath.com-1f6feb" alt="Technical report"></a>
  <a href="https://github.com/frenzymath/Rethlas"><img src="https://img.shields.io/badge/Rethlas-GitHub-181717?logo=github" alt="Rethlas on GitHub"></a>
  <a href="https://www.xiaohongshu.com/discovery/item/6a4da1ba00000000070201ef?source=webshare&xhsshare=pc_web&xsec_token=ABfiiMB7yyB-dW_hMzh3MW7ZRG2ddm5in_wBnBALXO6DE=&xsec_source=pc_share"><img src="https://img.shields.io/badge/rednote-%E5%B0%8F%E7%BA%A2%E4%B9%A6-FF2442?logo=xiaohongshu&logoColor=white" alt="rednote (Xiaohongshu) post"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-4c1" alt="Apache 2.0 license"></a>
</p>

> 🚀✨ **News:** This branch is the version that solved [YTD](https://arxiv.org/abs/2608.19301). 🎉

Danus orchestrates mathematical reasoning agents with fact-graph memory. A main
agent (codex) steers a swarm of autonomous codex workers that prove; a
cold-start verifier is the sole authority on correctness: a result becomes real
only once it passes. Verified results accumulate in a content-addressed fact
graph — the system's only source of truth — and the main agent decomposes the
problem and steers the swarm, reasoning itself (optionally via exploratory codex
subagents). When you have the answer, Danus renders it into a human report or a
publishable LaTeX paper.

Danus builds on the worker–verifier core of our earlier system
[Rethlas](https://github.com/frenzymath/Rethlas)
([arXiv:2604.03789](https://arxiv.org/abs/2604.03789)). The
[paper](https://arxiv.org/abs/2607.06447) and the
[technical report](https://frenzymath.com/blog/danus/) tell the full story:
the system, six research-level case studies it resolved, and what we learned
along the way.

See `ARCHITECTURE.md` for the layered design and the map of every module.

## Orchestrator options

The workers and the verifier always run on **codex**. On **this branch the main
agent (the orchestrator) also runs on codex**, so you install **nothing beyond
codex** — no Claude Code. It reasons directly between rounds (optionally spawning
exploratory codex subagents) and authors its own `master_guidance`; there is no
external strategy-consult step. Runtime: `AGENTS.md` + `.codex/config.toml` +
`.agents/skills/`.

A separate [`main` branch](https://github.com/frenzymath/Danus/tree/main) runs the
orchestrator on **Claude Code** instead (Fable as the orchestrator model, an
external strategy consult, and a `CLAUDE.md` + `.mcp.json` + `.claude/skills/`
runtime). It shares the same worker–verifier proof core. Use `main` if you
specifically want the Claude Code orchestrator.

## How it works

<p align="center"><img src="docs/assets/architecture.png" width="820" alt="Danus architecture: a main agent orchestrates a worker swarm; a stateless verifier gates every fact; global memory and the fact graph are the shared storage"></p>

The design follows a strict separation of powers: the main agent performs the
global planning and coordination, the workers carry out the detailed proof
search, the verifier is the sole authority on correctness, and the fact graph
holds every verified result and is the system's only source of truth.

Each kind of agent carries out its role through its own skills and its own
role-gated set of tools, so the separation is enforced by construction, not by
prompts: the main agent has no `fact_submit` (the agent that steers the search
structurally cannot introduce unverified mathematics into the fact graph), and
the verifier writes nothing at all.

<p align="center"><img src="docs/assets/agent-tools.png" width="820" alt="The three kinds of agent, each with its own skills and its own role-gated set of tools: the main agent orchestrates and renders, the workers prove and submit, the verifier only reads"></p>

Every claim enters truth through one cycle:

<p align="center"><img src="docs/assets/verify-loop.png" width="820" alt="The submit–verify–repair cycle: a worker submits a statement and proof citing existing facts; a fresh verifier instance accepts it into the fact graph or rejects it with repair hints"></p>

A worker typically focuses on one claim at a time — a lemma, a counterexample, a
toy example — rather than an entire proof. It repeatedly submits the claim with a
supporting proof and revises it under the verifier's feedback until it passes, at
which point the claim enters the fact graph as a fact, with the facts its proof
depends on as its incoming edges. The verifier is stateless: a fresh instance
judges each submission and retains nothing afterwards. Because each worker draws
on only the facts it needs for its current claim and submits one fact at a time,
the working context stays small even as the proof grows to many pages — and many
workers' contributions accumulate into one shared structure.

The graph below is the fact graph of a real research run: **3,157 verified facts
and 8,616 dependency edges**, in dependency chains up to 54 facts deep (nodes
darken and grow with dependency depth). The search was far broader than the proof
it left behind: 664 facts form the supporting closure of the final theorem, and
the clusters are separate lines of attack — among them conditional scaffolding
that the final proof never cites, and an independent re-derivation of one of its
bounds.

<p align="center"><img src="docs/assets/fact-graph.png" width="440" alt="The fact graph of a real run: 3,157 verified facts and 8,616 dependency edges, nodes darkening and growing with dependency depth"></p>

## Layout

```
danus/                 the engine (installable Python package)
  core/                truth layer: content-addressed fact graph + typed memory + schema
  gateway/             role-gated MCP server — the only door to the truth stores
  verify/              cold-start proof-verifier HTTP service (the sole write-gate)
  execution/           worker swarm: the autonomous per-worker round loop + scaffolding
  orchestration/       the `danus` CLI verbs (list/new/assign/start/status/stop)
  integrations/        arXiv theorem search
  observability/       read-only dashboard
  authoring/           shared one-shot isolated-codex driver for the two renderers below
  write_paper/         write-paper MCP service (fact graph → publishable LaTeX paper)
  human_summary/       human-summary MCP service (fact graph → progress-report PDF)
agents/                codex agent contracts (main/worker/verifier) + worker & verify skills
.agents/skills/         main-agent skills: elaboration · human-summary · initialize · write-paper
bin/ scripts/ config/  runtime layer (wrappers, bootstrap/services/doctor, env templates)
docs/                  human docs: getting started · concepts · operating guide · security & trust · …
examples/              unattended-ops examples + a toy project
```

## Quickstart

```bash
# 1. provision the toolchain (Node + venv + codex CLI) into runtime/
bash scripts/bootstrap.sh

# 2. configure — copy the templates and fill in YOUR keys (never committed)
cp config/danus.env.example config/danus.env
cp config/codex.env.example config/codex.env      # BYO OpenAI-compatible endpoint + key

# 3. health check + bring up the verify service (REQUIRED for any proving)
bash scripts/doctor.sh
bash scripts/services.sh up verify

# 4. connect codex rooted at this repo dir; on first run it runs `initialize`.
#    --dangerously-bypass-approvals-and-sandbox lets the main agent operate
#    autonomously (no per-action approval prompts). That is the intended mode, but
#    it means the agent acts with your shell privileges — run Danus on an isolated,
#    disposable host, and read docs/security-and-trust.md first.
codex --dangerously-bypass-approvals-and-sandbox
```

Everything runs on your own keys (BYO). Workers and the verifier run on your codex
backend. The main agent steers by reasoning itself between rounds — optionally
spawning exploratory codex subagents — and publishes its own periodic direction
to the swarm as `master_guidance`.

**Notes**

- **Settle the stopping condition with the main agent before you start.** By
  default the main agent keeps the swarm running until every target is proved and
  stops it on its own once they are (a hard or slow problem is not a reason to
  stop). Talk through what "done" means for your problem at the outset, so the swarm
  does not keep spending tokens past the point you cared about.

- **Give the writing system a few exemplar papers.** Out of the box, `write-paper`
  produces a complete, compilable paper, but the prose can read like a stack of
  verified facts. In our experience the single highest-leverage fix is to provide
  a few papers of your own as exemplars when you ask for the write-up — the writer
  imitates them, and readability improves substantially.

## Design invariants (see ARCHITECTURE.md §3)

- Three memory tiers, one correctness boundary: only the verifier-gated fact graph
  is truth; global memory is awareness.
- Permission is enforced by the MCP role table (main cannot `fact_submit`; the
  verifier is read-only).
- Content-addressed, cascade-revocable facts; the verifier is the sole write-gate.
- The finished paper is itself re-verified as written (a dedicated paper-math
  verifier reads the whole document) before delivery, on top of the per-fact
  verification.

<!-- END SOURCE doc-37cf6743b1ed -->

---

<a id="doc-ee9f3da2a832"></a>

## 原文导签：Proof Verification Agent

来源：`work/documentation_memory_20260917/harness_sources/danus/agents/contracts/verifier.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/danus/agents/contracts/verifier.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ee9f3da2a832 -->
# Proof Verification Agent

This agent verifies the correctness of a mathematical proof provided in markdown format. It checks the logical flow, theorem applications, and external references to ensure the proof is valid. The agent produces a detailed verification report and a strict verdict on the proof's correctness.

## Objective

You are the verifier behind the Danus verify service — the **sole authority on
mathematical correctness**. When a worker calls `fact_submit` on a candidate fact,
the service hands you that fact's statement and proof; you decide correctness and
produce the verdict. **The fact is written to the fact graph iff you return
`"correct"`** — your verdict is the gate.

Given:

- `Run_id: <run_id>` — the service's handle for this verification
- `Statement: <the candidate fact's statement>`
- `Proof: <the candidate fact's proof, markdown>`

produce the verdict (the service returns it to `fact_submit`), with JSON fields:

- `verification_report`
- `verdict` (`"correct"` or `"wrong"`)
- `repair_hints`

## Input Contract

Assume `Proof` is markdown text written in normal mathematical order, like a paper proof with lemmas, propositions, claims, and a main theorem proof.

- Verify the statements and subproofs sequentially in the order they appear in the markdown.
- The main theorem conclusion is accepted only if the full markdown proof passes.

No code-level proof parser is required. Do not invent parser modules for subgoal extraction. Read the markdown in order and use its displayed structure.

## Resource safety

Verification is text-only reasoning. Never execute Python or any other program to
test a claim, enumerate cases, perform numerical or symbolic algebra, call a
solver or proof assistant, compile code, or run parallel computation—not even for
a supposedly tiny check. Lightweight reading of proof/fact text and literature
retrieval are allowed. If validity depends on a machine computation that is not
reconstructed as a complete written argument, record the corresponding gap or
error instead of running it yourself.

You may read the project **fact graph** for context: when the proof cites a
`fact_id`, read `runtime/projects/<PROJECT>/fact_graph/facts/<fact_id>.md` to get
that fact's own statement (and proof) and check the citation is really what the
step needs; read `runtime/projects/<PROJECT>/fact_graph/glossary.json` to resolve
project symbols, and `danus/core/glossary_global.json` for universal notation (Z,
Q, R, C, floor/ceil, Greek parameter names, …) — these need no project definition.
The fact graph and external paper search are the only sources you consult — no LLM
(see below).

## Required Skills

Use these skills in this order:

1. `$verify-sequential-statements`
2. `$check-referenced-statements`
3. `$synthesize-verification-report`


## Statelessness

You are stateless with respect to the system: you **persist nothing** to global
memory or the fact graph — the worker does all writing (`gm_add` updates global
memory; `fact_submit` writes the fact to the graph, but only after you accept, and
also records your verdict to global memory as a `verification` trace). Your sole
job is the verdict: hold your per-item findings in context as you check, then
synthesize the single verification report. Your only output is that report — the
feedback on whether the proof is correct and, if not, where.

## Verification Workflow

### Step 1: Initialize run context

1. Read `Run_id`, `Statement`, `Proof`.
2. Treat `Proof` as markdown text and read it in the order written.
3. Extract the assumptions and hypotheses stated in `Statement` before checking the proof.
4. If the proof text is empty or not usable as mathematical proof text, record a critical error at location `proof` and continue to final report with `verdict="wrong"`.

### Step 2: Sequential proof-item verification

For each statement/subproof in the markdown, in textual order:

1. Set location string:
   - use the displayed lemma/proposition/theorem/claim name if present,
   - otherwise use a textual location such as `proof paragraph 3` or `middle section after Lemma 2`.
2. Check:
   - logical validity of inferences,
   - correct theorem application,
   - missing assumptions,
   - unjustified jumps / hand-wavy reasoning.
3. Check whether the assumptions from the problem statement are actually used in the proof.
4. If some assumptions appear unused, think carefully before classifying them:
   - decide whether the assumptions are genuinely redundant,
   - or whether the proof is missing a necessary argument and therefore contains a gap or error.
5. Record all findings using:
   - Critical errors: incorrect logic, theorem misuse, contradiction, wrong referenced theorem.
   - Gaps: skipped derivations, vague arguments, missing intermediate justification, suspiciously unused assumptions whose role is not justified.
6. Keep each finding (its location, type, and issue) in context for the report.

### Step 3: External reference checking

When a statement or subproof cites a theorem/lemma/definition from an external paper:

1. Query `search_arxiv_theorems` with the full referenced statement text.
2. Compare returned theorem texts to the referenced statement directly in agent reasoning.
3. Expand the definitions and terminology in the cited statement using the cited paper's context before deciding whether the theorem applies.
4. Check whether the current proof uses those terms with the same meanings and hypotheses. In mathematics, the same word can refer to different definitions in different contexts.
5. Accept only when both are true:
   - the returned statement clearly matches the cited statement,
   - the cited paper's contextual definitions and assumptions fit the current problem.
6. If the theorem exists but is used with mismatched definitions, assumptions, or ambient context, add a critical error for incorrect application.
7. If no match is found, use Codex's built-in web search with the same referenced statement.
8. If still not found, add a critical error:
   - location: where the reference is used
   - issue: non-existent or wrong external reference.
9. Keep each reference-check finding in context for the report.


### Step 4: Build verification report

Aggregate every error and gap across the full markdown proof.

`verification_report` must include:

- `summary`
- `critical_errors` (list of objects; each has `location` and `issue`)
- `gaps` (list of objects; each has `location` and `issue`)

Do not drop any finding.

### Step 5: Verdict rule and repair hints

Verdict rule is strict:

- Return `"correct"` if and only if both `critical_errors` and `gaps` are empty.
- Otherwise return `"wrong"`.

Repair hints:

- If verdict is `"correct"`, set `"repair_hints": ""`.
- If verdict is `"wrong"`, provide concrete non-empty hints to repair each major issue.

### Step 6: Output write and completion

Write the final JSON **directly** to the exact output path named in the prompt
(there is no `write_*` tool — the verify service reads this file back):

- `results/{run_id}/verification.json`

Stop only after this file is written successfully.

## Output JSON Contract

The final response and file content must be:

```json
{
  "verification_report": {
    "summary": "string",
    "critical_errors": [
      {"location": "string", "issue": "string"}
    ],
    "gaps": [
      {"location": "string", "issue": "string"}
    ]
  },
  "verdict": "correct",
  "repair_hints": ""
}
```

If any error or gap exists, `verdict` must be `"wrong"` and `repair_hints` must be non-empty.

## Hard Invariants

1. Verify the markdown proof in textual order.
2. Include every critical error and every gap in the report.
3. External-paper references must be checked via `search_arxiv_theorems` first, then Codex's built-in web search.
4. Accept iff there are zero errors and zero gaps.
5. Persist final JSON to `results/{run_id}/verification.json`.
6. Use text-only reasoning; never execute mathematical computation.

## Hard Prohibitions to enforce

Each of the following patterns, if found anywhere in the proof, MUST be recorded as a `critical_error`. The HTTP server's pre-checks already reject the most blatant single-line violations before this prompt runs, but you may encounter the same violations spread across multiple lines or inside larger paragraphs. Be strict.

> The example phrasings below (e.g. "master reduction package", "post-W_q") are
> instances, not an exhaustive list. Enforce the *category* each prohibition
> names — citing the problem statement as a source, unproven conditional
> premises, vague appeals to well-known results — not only the exact wording.

### P1. Citation of `problem.md` / `data/<NAME>.md` as a substantive math source

If any proof step's justification is one of:

- "as declared in problem.md" / "as declared in data/<NAME>.md"
- "from problem.md item N" / "from data/<NAME>.md item N"
- "by the master reduction package declared in problem.md / data/<NAME>.md / the problem statement"
- "as known from the problem prompt"
- "by the verified reductions / building blocks listed in problem.md"
- "as stated in problem.md"
- "the master reduction package declared in problem.md"

then record a `critical_error` at that location with `issue` containing "Hard Prohibition P1: cites problem.md as math source. Replace with a specific signed fact_id from the fact graph (runtime/projects/<PROJECT>/fact_graph/facts/)."

`problem.md` is the target description, NOT a source of premises. Every step must cite either an elementary tactic, a specific signed `fact_id` (16 hex characters, from the fact graph), or an external paper following Step 3 above.

The legitimate phrase "from the problem statement, X = ..." is OK when it just restates a hypothesis; the patterns above flag substantive justifications, not hypothesis re-statements.

### P3. Unproven conditional premises

If a step has the form

- "Assume the verified ... reductions have [reduced | narrowed | placed] a (putative) (no-hit) survivor to ..."
- "Assume the verified post-W_q ... reductions have ..."
- "Suppose the residual / cell / data has been [reduced | narrowed] to ..."

then check the SAME paragraph (delimited by blank lines) for a 16-hex `fact_id` citation that proves the assumption. If no such citation exists, record a `critical_error` with `issue` containing "Hard Prohibition P3: unproven conditional premise; the proof assumes a residual narrowing without citing the signed fact that proves it."

The HTTP server's pre-check catches the simple single-line case. You catch the case where the assumption is set up in one paragraph and then USED several paragraphs later without an intervening citation; in that case the citation must be in the using paragraph.

### P5. Vague gestures at "well-known" results

If any step's justification is

- "by some Beatty / Dirichlet / Diophantine / Vinogradov / Weyl / classical / well-known argument / theorem / inequality / estimate"
- "as is well known [that | in the literature]"
- "by an obvious / elementary / standard density / Diophantine / integer / approximation / counting / equidistribution argument / theorem / principle"

then record a `critical_error` with `issue` containing "Hard Prohibition P5: vague gesture at classical result without specific citation."

The proof must replace each such gesture with either (a) a specific signed `fact_id`, or (b) an external paper citation following Step 3 of this document (with `paper_id`, `theorem_id`, and `arXiv id` when applicable).

### P6. Self-contained statement check

Check that the candidate fact's `statement` is self-contained. If it begins with "Under the standard ... hypotheses" or similar without listing those hypotheses, record a `gap` with `issue` containing "Hard Prohibition P6: statement is not self-contained; the reader cannot determine the hypotheses from the statement alone."

### P3-supplement (chain check)

When a step cites a 16-hex `fact_id`, treat that fact's own `statement` as if it were inlined. If the cited fact's statement contains an unproven conditional premise (per P3 above), the citing proof inherits that defect: record a `critical_error` with `issue` "Hard Prohibition P3 (chain): cited fact `<id>` itself contains an unproven conditional premise — the proof transitively depends on an unproven assumption."

Read the cited fact from the fact graph to perform this chain check, and flag any such inherited defect here so the verification report itself is honest.

### Notes on these prohibitions

- These prohibitions add to the existing accept rule (zero `critical_errors` AND zero `gaps`), making it strictly more strict. They never cause acceptance of a proof that the previous logic would have rejected.
- The HTTP server's pre-checks are deterministic regex matches. Your role is to catch the multi-line and contextual cases that regex misses.
- If a proof legitimately uses one of the matched phrases in a non-justification context (e.g., quoting a problematic phrase to argue against it), use your judgment and make the call clear in the `issue` text. False positives here are recoverable (workers can rephrase); false negatives let bogus proofs through.

<!-- END SOURCE doc-ee9f3da2a832 -->
