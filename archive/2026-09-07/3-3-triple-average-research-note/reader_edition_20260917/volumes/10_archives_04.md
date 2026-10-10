# 工作材料、历次快照及旧目录完整附卷 · 第4分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [三平均有限步可达性研究](#doc-f7cb17430ef6)
- [允许块形状变化的整数检查点势](#doc-e0ada002f2f3)
- [形状变化势与零和组合文献的接口](#doc-cdb5653a63f7)
- [形状变化势的关键组合猜想：单值零和迫使双重高重](#doc-35e2922634c7)
- [三平均研究的计算核验指南](#doc-8100ea423b9b)
- [核内缺口文献访问记录](#doc-dca8aa725c28)

---

<a id="doc-f7cb17430ef6"></a>

## 原文导签：三平均有限步可达性研究

来源：`work/audit_before_sharp_structure_20260912/README.md` · [逐字节原样副本](../sources/work/audit_before_sharp_structure_20260912/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-f7cb17430ef6 -->
# 三平均有限步可达性研究

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

2026-09-12形状变化势的关键未解结构：[单值零和双高重猜想](outputs/prime_arity/structure/prime_arity_single_value_zero_sum_conjecture.md)：长度N>=3p+1的C_p序列若所有p项零和都单值，猜想两大余数重数和至少3p-2；这将直接接上已有双重值整数闭包。与Grynkiewicz零和计数和逆EGZ文献相符，p=3,5,7有限枚举支持，但目前仍是猜想。

2026-09-12结构定理：无混合p项零和的余数池中，重余数桶至多两个；双桶覆盖全池，单桶至少N-p+1。该结论由删至p-1后应用EGZ严格证明，单桶背景宏仍需历史约束。

修正：无混合零和重数结构定理的适用范围明确为 3p+1≤N<4p；超出上半带不外推。
<!-- END SOURCE doc-f7cb17430ef6 -->

---

<a id="doc-e0ada002f2f3"></a>

## 原文导签：允许块形状变化的整数检查点势

来源：`work/audit_before_sharp_structure_20260912/outputs__prime_arity_shape_changing_integer_potential.md` · [逐字节原样副本](../sources/work/audit_before_sharp_structure_20260912/outputs__prime_arity_shape_changing_integer_potential.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-e0ada002f2f3 -->
# 允许块形状变化的整数检查点势

日期：2026-09-12。

前面的固定核心方法把注意力放在保持 \((2p,p,r)\) 形状上；本页改用一个更宽的状态类。关键不是寻找每一步都回到同一形状的宏，而是只在整数状态之间记录势。

设当前整数零和状态为 \(X=(x_1,\ldots,x_n)\)，并在每个原子平均后仍保持合法。定义
\[
E(X)=\sum_i x_i^2.
\]
对一个真实的 \(p\) 元组 \(S\)，平均后该组变成 \(\bar x\)，有精确恒等式
\[
E(X)-E(T_SX)=\sum_{i\in S}(x_i-\bar x)^2
=\frac1p\sum_{i<j\in S}(x_i-x_j)^2.
\tag{1}
\]
因此只要组内不全相等，能量严格下降；整数状态的能量是非负整数。

## 1. 新的终止目标

允许中间步骤改变重数、改变块形状，甚至暂时产生分母。把一个有限真实词称为**整数返回宏**，如果它从整数状态出发，在所有中间状态保持合法，最后又回到整数状态。若宏中至少一个原子平均非恒等，则由 (1) 得
\[
E(X_{\rm out})<E(X_{\rm in}).
\tag{2}
\]

所以足以证明以下宏存在性命题：

> 每个非终端合法整数状态，都存在一个安全的非恒等整数返回宏。

一旦这个命题成立，反复选择宏必在有限步内停止；停止状态不能是非零合法状态。若宏最后直接制造一个零和 \(p\) 元组，则接已有零触发定理完成全系统。

这把原来的固定形状终止问题改成了“整数检查点之间的形状变化”问题。它避免把清分母后的本原能量误当成单调量；中间分母只影响宏设计，不影响检查点势 (2)。

## 2. 已有的形状变化宏

### 两步重叠造零

对任意素数 \(p\ge5\)，状态
\[
X_p=(2^{2p},(-1)^p,-3p),\qquad n=3p+1
\]
有两步整数返回宏。若 \(p\equiv2\pmod3\)，先取
\[
(2^{(2p-1)/3},(-1)^{(p-2)/3},-3p)\longmapsto(-2)^p,
\]
再取
\[
(2^{(p-1)/2},(-1)^2,(-2)^{(p-3)/2})\longmapsto0^p.
\]
若 \(p\equiv1\pmod3\)，第一步得到 \((-3)^p\)，第二步使用模5选择的三个整数配比得到 \(0^p\)。两步中第二组与第一组重叠；它们都保持整数，且总能量严格下降。

这说明固定核心内的一步不降并不代表没有下降宏。七平均22元的陷阱正是这族在 \(p=7\) 的实例。

### 碰撞后增大背景

若一个整数候选选取 \(i\) 份旧大值 \(a\)、若干低重位置和其余 \(b\)，但均值碰撞到 \(a\)，则选中位置全部变成 \(a\)，并有
\[
f'(a)=f(a)+p-i.
\tag{3}
\]
在标准参数 \(f(a)=p+\alpha\)、\(i\le\alpha\) 下，
\[
f'(a)\ge2p.
\]
这不是“失败而回到原状态”，而是一次形状变化：系统进入一个大背景分支。随后应允许背景值继续吸收低重位置，直到产生第二个重值或零和组；不能要求下一步立即恢复原来的两个大块。

## 3. 为什么这是真正不同的势函数路线

固定 \((2p,p,r)\) 核时，安全射影收缩清分母后可能增加本原整数能量。式 (1) 使用的是实际有理状态的能量，而整数检查点只在返回时比较；因此允许在核外改变块形状，同时保持严格的整数下降。

势函数本身很简单，困难转移到了宏存在性：必须证明每个形状变化边界都能找到一条回到整数格的安全路径。这个困难是明确的，不再是假设一个形式逆可以执行。

## 4. 与零和组合的接口

在一个受保护位置集之外，若能找到一个非恒等的 \(p\) 项余数零和组，且其实际和不是旧值的碰撞和，就得到一步整数下降。若该组实际全相等，操作只是恒等；这时要使用同一余数桶中的不同实际值，或改变组的重数配比。

长度 \(2p-2\) 的逆 EGZ结构说明：没有任何 \(p\) 项零和时，余数序列只能是两个各重 \(p-1\) 的余数类。这是一个极强的形状约束。上半带的保护池长度远大于 \(2p-2\)，所以剩余障碍应集中在“所有零和组都单值”的两类大桶结构及其保护交换，而不是任意余数序列。

下一步应证明一个**非恒等零和返回引理**：在保护后池中，若所有 \(p\) 项零和组都是单值组，则要么同一余数桶含有不同实际值（立即给出下降），要么状态具有两个大背景；对两个大背景使用碰撞增大式 (3)，再接一个重叠返回宏。

## 5. 当前边界与证据

这页没有声称已经证明上述宏存在性命题。已严格证明的只是：

- 整数检查点能量的下降恒等式；
- 两步重叠造零族；
- 碰撞必然增加背景重数的形状变化公式；
- 固定核心单轮下降失败不排除核外下降宏。

因此，当前最有价值的具体任务是分类“所有 (p) 项零和组均为单值组”的保护池。这个分类若能闭合，便可能把上半带从固定核心入口推进到完整终止；若出现新的无限结构，则可直接作为反例候选检验。

相关文档：[3p剩余缺口](prime_arity_three_p_remaining_gap.md)、[二类型碰撞整数格](prime_arity_binary_collision_lattice.md)、[主余类储备](prime_arity_dominant_residue_reservoir.md)。

<!-- END SOURCE doc-e0ada002f2f3 -->

---

<a id="doc-cdb5653a63f7"></a>

## 原文导签：形状变化势与零和组合文献的接口

来源：`work/audit_before_sharp_structure_20260912/outputs__prime_arity_shape_potential_literature_interface.md` · [逐字节原样副本](../sources/work/audit_before_sharp_structure_20260912/outputs__prime_arity_shape_potential_literature_interface.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-cdb5653a63f7 -->
# 形状变化势与零和组合文献的接口

日期：2026-09-12。

当前形状变化路线的关键子命题是：保护位置删去后，是否必有一个非恒等的 (p) 项模 (p) 零和组。这个组若实际值不全相等，就给出严格降低整数能量的真实平均；若全相等，则只产生恒等操作，需要转入高重数形状分析。

## 1. 可直接借用的结果

### Grynkiewicz：(m) 项零和子序列计数

D. J. Grynkiewicz, *On the number of (m)-term zero-sum subsequences*, Acta Arithmetica 121.3 (2006), 275--293, DOI [10.4064/aa121-3-5](https://doi.org/10.4064/aa121-3-5)。全文已从 Instytut Matematyczny PAN 下载并阅读。

其定理 1.1：若序列 (S) 取自阶为 (m) 的有限交换群、长度为 (n)、且 (mge30)，则 (S) 含有至少
\[
min\left{
\binom{\lceil n/2\rceil}{m}+\binom{\lfloor n/2\rfloor}{m},
\binom{\lceil (n-m)/(\lceil(2m-1)/3\rceil)\rceil}{m}
\right\}
\]
个 (m) 项零和子序列（原文公式按排版记号给出；使用时应回到原式核对）。论文还指出，少量零和的极端情形接近两值序列，并给出了足以验证 Bialostocki 计数猜想的长度范围。

在本项目中取群 (C_p)。当保护后池的长度超过 (2p-1) 时，该定理给出的零和组数量增长；若所有这些组在实际值上都单值，则每个高重数余数桶必须承受大量零和组。这个结论不直接给出非单值组，但把失败状态压缩到高重数桶结构。

### Grynkiewicz--Ordaz--Varela--Villarroel：逆 EGZ

D. J. Grynkiewicz, Ó. Ordaz, M. T. Varela, F. Villarroel, *On Erdős--Ginzburg--Ziv inverse theorems*, Acta Arithmetica 129.4 (2007), 307--324, DOI [10.4064/aa129-4-1](https://doi.org/10.4064/aa129-4-1)。全文已从 Instytut Matematyczny PAN 下载并阅读。

其循环群结论研究长度 (|G|+k) 而没有 (|G|) 项零和的序列，并证明高重数阈值下的完整结构；定理 1.2 给出：若
\[
|S|\ge m+\max\{h(S),m/p_0-1\},
\]
其中 (p_0) 是 (m) 的最小素因子，则 (0\in\Sigma_m(S))，且 (m) 项零和和集具有周期性。对 (G=C_p)，周期性大幅简化为全群结构。

该文还明确指出，低于高重数阈值的逆命题会出现复合模数的多余结构；这提醒我们不能把 (C_p) 的结论直接搬到危险素数集合的乘积模数上。

### Graham 型“同长度零和”结构

D. J. Grynkiewicz, *Note on a conjecture of Graham*, European Journal of Combinatorics 32 (2011), DOI [10.1016/j.ejc.2011.06.004]。全文通过 Europe PMC XML 阅读。

Graham 猜想及其证明说明：若 (C_p) 中长度为 (p) 的序列，其所有非平凡零和子序列长度相同，则支撑至多两个。论文给出只用 Cauchy--Davenport 和抽屉原理的短证明，并能列出精确结构。

这与“所有可执行 (p) 项零和组都是单值组”相近但不相同：项目只控制固定长度 (p)，而 Graham 条件控制所有非平凡长度。因此该定理不能直接宣布核心终止；它提供的是失败状态低支撑的结构模板。

## 2. 能怎样翻译成原位置宏

对保护后的原位置池 (P)，把每个位置的值取模 (p) 得到序列 (S_P)。若存在一个 (p) 项零和子序列 (Qsubseteq S_P)，且对应实际值不全相等，则平均这些原位置：

- 组长恰为 (p)，实际和被 (p) 整除，故均值为整数；
- 若保护位置全部留在池外，危险素数见证不丢失；
- 由能量恒等式，操作严格降低整数检查点势。

如果每个这样的 (Q) 都实际单值，则其余数支持和实际重数被计数定理压缩。特别是，若某个余数桶含有至少 (p) 个位置但实际值不全相等，直接在该桶中取 (p) 个位置也给出下降；所以真正危险的是：高重数余数桶内部实际值也全部相等。

这使失败状态接近
\[
(u^{f_1},v^{f_2},\ldots),
\]
其中每个高重数桶均为实际常值。此时问题回到已建立的块形状操作，而不是任意坐标问题。

## 3. 当前不能直接使用的地方

1. 计数定理作用在模 (p) 的序列上，不记录危险素数 \(\ell\mid n\) 的保护见证；需要先选择不碰保护池的子序列。
2. “存在很多零和子序列”不等于“存在实际非单值零和子序列”；若每个桶内部是常值，所有组仍可能恒等。
3. 逆 EGZ 的周期和支撑结论是余数层结论，不能自动生成原位置的正向平均词。
4. 中间有理状态的能量不提供整数良序；必须把每个组合步骤编成整数返回宏。

## 4. 文献启发出的明确新目标

证明下面的保护池引理：

> 设 (P) 是长度至少 (2p-1) 的原位置池，保护位置在外部；若 (P) 的每个 (p) 项模 (p) 零和子组都由一个实际常值桶组成，则这些桶至多两个，或存在一个两步重叠整数返回宏使能量严格下降。

“至多两个桶”不能直接由 Graham 定理推出，需要结合 Grynkiewicz 的零和计数和全局零和关系。若该引理成立，便能把形状变化势应用到整个上半带；若不成立，反例会给出一个新的、可明确描述的块形状族。

## 5. 核验和访问记录

已保存文献缓存：

- `work/literature_20260912/impan_0.pdf` 及 `impan_0.txt`：Grynkiewicz 2006；
- `work/literature_20260912/impan_1.pdf` 及 `impan_1.txt`：Grynkiewicz--Ordaz--Varela--Villarroel 2007；
- `work/literature_20260912/grykniewicz_graham_2011.txt`：Grynkiewicz 2011 的全文 XML 提取；
- OpenAlex 定向检索记录：`work/literature_20260912/` 中对应带标题哈希的 JSON。

文献只用于缩小失败结构，不替代原位置安全性和可执行路径证明。

<!-- END SOURCE doc-cdb5653a63f7 -->

---

<a id="doc-35e2922634c7"></a>

## 原文导签：形状变化势的关键组合猜想：单值零和迫使双重高重

来源：`work/audit_before_sharp_structure_20260912/outputs__prime_arity_single_value_zero_sum_conjecture.md` · [逐字节原样副本](../sources/work/audit_before_sharp_structure_20260912/outputs__prime_arity_single_value_zero_sum_conjecture.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-35e2922634c7 -->
# 形状变化势的关键组合猜想：单值零和迫使双重高重

日期：2026-09-12。

形状变化势只需要一个整数 (p) 元组：若其实际值不全相等，平方能量严格下降；若所有可选 (p) 项零和组都单值，则余数序列必须有很强的重数结构。本页记录目前最接近闭合的组合命题，并把它与已发表的零和计数结果接上。

## 猜想 A（双重高重猜想）

设 (p) 为奇素数，(S) 是 (C_p) 中长度 (Nge3p+1) 的序列。假设每个 (p) 项零和子序列都由同一个余数重复 (p) 次组成，即不存在混合余数的 (p) 项零和子序列。令 (f_1ge f_2gecdots) 为各余数重数，则
\[
\boxed{f_1+f_2ge3p-2.}
\tag{1}
\]

若 (1) 成立，项目中的已有双重值整数闭包立即适用：两个实际大块总重数至少 (3p-2) 时，总有一次安全非恒等整数平均保持两个 (p) 重值，或进入可收尾状态。因此，保护池中所有 (p) 项零和组都单值的失败状态将被压回已处理分支。

这正是把“块形状变化势”转成组合定理的最短接口。

## 1. 为什么猜想与已有文献相符

D. J. Grynkiewicz 的 *On the number of (m)-term zero-sum subsequences*（Acta Arith. 121.3 (2006), DOI 10.4064/aa121-3-5）给出长度 (N>2p-1) 时 (p) 项零和子序列数量的统一下界，并强调低支撑序列是避免混合零和的极端结构。其定理不能直接推出 (1)：数量下界需要与所有单值零和组的二项式总数比较，而在 (N=3p+1) 附近这个比较仍不够锐。

Grynkiewicz--Ordaz--Varela--Villarroel 的 *On Erdős--Ginzburg--Ziv inverse theorems*（Acta Arith. 129.4 (2007), DOI 10.4064/aa129-4-1）刻画高重数边界的无 (p) 项零和序列。它同样说明极端序列接近少数桶，但其假设是完全没有 (p) 项零和，而猜想 A 允许单值零和，因此仍需新的“单值零和”逆定理。

Grynkiewicz 的 Graham 猜想短证明（EJC 32 (2011), DOI 10.1016/j.ejc.2011.06.004）表明，如果所有非平凡零和子序列长度相同，则支撑至多两类。项目条件只固定长度 (p)，所以可把它视为猜想 A 的方向性启发，不能直接代替证明。

## 2. 与原位置操作的精确翻译

设保护池中对应余数桶内部的实际值均为常数。若存在混合余数的 (p) 项零和组，平均该组便得到非恒等整数下降；若混合组的实际和恰为某旧值的 (p) 倍，则碰撞会增加该旧值的重数，进入双重值闭包。

因此，假设没有可接受的形状变化宏时，余数层必须满足猜想 A 的前提。若 (1) 成立，取两个最大桶并调用已有总重数引理；不需要恢复原始 ((2p,p,r)) 形状。

保护位置只影响是否安全。每个危险素数保留一个池外见证后，任何选组都不会完整消灭见证；余数层的猜想 A 与原位置安全性可以分开处理。

## 3. 有限结构核验

对 (p=3,5,7)，以及 (N=2p+1,2p+2,3p-1,3p,3p+1) 的完整余数重数枚举，所有满足“没有混合 (p) 项零和组”的序列都满足 (1)。例如 (p=7,N=22) 的陷阱重数型包括
\[
(19,2,1),(18,3,1),(15,7),(12,10),(11,11)
\]
及其更集中型；其最大两桶总重数均至少 (19=3p-2)。

这些枚举只验证余数层结构，不验证实际值、保护见证或终端可达性。对应脚本仍是有限实验，不承担猜想 A 的无限量词。

## 4. 证明上的真正难点

最直接的 EGZ 只保证存在某个 (p) 项零和组，不能控制它是否混合。要证明 A，需要一个“混合零和计数”或“单值零和逆定理”：当最大两桶总重数小于 (3p-2) 时，必须产生混合零和组。

已有数量下界可能不足以达到这个阈值，因此不能只引用 EGZ 或现有计数定理。可能的工具包括：

- Cauchy--Davenport 对带重数部分和的迭代；
- Grynkiewicz 的分割和集定理；
- 受限和集（Dias da Silva--Hamidoune）控制不同位置的选取；
- 直接对三大桶先证，再用归纳减少支撑。

若猜想 A 被证明，当前形状变化路线会实质性前进；若出现反例，它将给出一个新的、明确的块形状族，而不是无结构的搜索失败。

## 5. 状态判断

猜想 A 尚未证明。当前已证明的是：任何混合实际值的 (p) 项零和组给出整数能量下降；碰撞给出高重背景；两个大值总重数至少 (3p-2) 时已有安全闭包。缺口只在余数层把“无混合零和”转成“双高重”这一组合命题。

## 6. 可证明的重数结构定理

上面的猜想 A 实际可先拆出一个完全证明的部分。若 (Nge3p+1)，且没有混合余数的 (p) 项零和，则重余数桶（重数至少 (p)）至多两个。

证明如下。对每个重桶删去全部多余位置，只保留 (p-1) 份，得到序列 (R)。由于 (N<4p)，若有三个重桶则删去后的长度仍至少 (N-3ge3p-2>2p-2)。(R) 中不能含任何 (p) 项零和：若有，则每个余数桶都少于 (p) 份，所以该零和必为混合的，矛盾。由 EGZ，(|R|le2p-2)。

若有三个重桶，删除数为
[
sum_{i=1}^3(f_i-p+1),
]
而 (Nge3p+1) 会使 (|R|>2p-2)，矛盾。若恰有两个重桶，删除数为 (f_1+f_2-2p+2)，于是 (|R|le2p-2) 给出 (f_1+f_2ge N)；所以两个桶覆盖整个序列。若只有一个重桶，因其余所有桶至多 (p-1) 份，(|R|le2p-2) 给出
[
f_1ge N-p+1.
]

所以无混合零和的失败形状只有两类：
[
	ext{一个桶至少 }N-p+1	ext{ 份，或两个桶覆盖全部位置。}
]

这一定理不需要猜想 A 的强结论 (f_1+f_2ge3p-2)，并且对保护池长度 (N=3p+r-h) 也有相应版本：单桶至少 (N-p+1)，双桶时覆盖整个保护池。

它对原位置势函数的意义是：若池中存在混合零和组，直接得到整数能量下降；若不存在，池的形状已高度集中。双桶覆盖时可尝试调用已有双重值总重数引理；单桶情形则把所有未选位置压缩到不超过 (p-1) 个例外，下一步只需构造一个历史相关的背景吸收宏。

<!-- END SOURCE doc-35e2922634c7 -->

---

<a id="doc-8100ea423b9b"></a>

## 原文导签：三平均研究的计算核验指南

来源：`work/audit_before_sharp_structure_20260912/outputs__triple_average_verification_guide.md` · [逐字节原样副本](../sources/work/audit_before_sharp_structure_20260912/outputs__triple_average_verification_guide.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-8100ea423b9b -->
# 三平均研究的计算核验指南

新增 dominant-residue-reservoir（core/full）：[主余类储备](prime_arity_dominant_residue_reservoir.md)处理一个低重余类至少p-alpha份而其他轻值任意分余类的局部续步。367224个主类碰撞提升、15497个相容参数、37754个例外配比、13301个超额包装和834条原位置Fraction续步通过。文档明确保留“每个例外只有一个配比”的刚性边界，不宣称多余类闭包或N(p)<=3p。

新增 binary-collision-lattice（core/full）：[二类型碰撞整数格证明](prime_arity_binary_collision_lattice.md)以基本格三角形及单候选区间计数承担一般整性量词，再接总和和私人见证。130420组临界系统、113628组富余系统核验通过；2133条单实际轻值续步（816条保护、169条r=1）、300条三重值续步（21条r=1）、127条单余类多实际值续步逐位置检查整数性、G、双重值与严格能量下降；包括p29/n90的三个私人见证及G11的非法中间碰撞对照。只证明列明整数续步分支，未证明多余类类闭包或完整上半带终止。

新增 upper-band-descent-boundary（core/full）：[3p剩余缺口与核心逃逸](prime_arity_three_p_remaining_gap.md)核验2544组第二载体容量、484条六原子周期；9344个方向的有限单轮诊断中1703个未找到菜单下降或终端；对七平均22元(2^14,(-1)^7,-21)的十个不交返回给出完整原位置证书，完整性由正文均值区间证明承担。93个任意素数两步整数造零样本通过，正文给一般公式。共同因子先约去再检查G，未把未归一化全零余类误判为非法。不证明核心不可达、全部22元可达或统一3p阈值。

新增 upper-band-three-value-reduction（core/full）：[3p到4p的统一三值归约](prime_arity_upper_band_three_value_reduction.md)由初等短区间筛选、原位置支持集中及重复运输行证明任意素数p>=5、整个3p<n<4p的全输入归约，次数至多12+3ω(n)，无r>=d或素因子数限制。1770组筛选、106534组容量、376条随机大整数入口（18条r<d）、5条强制多素数入口（最多5种）和4条强制主块修复逐原子Fraction重放通过；另564组核心能量、544组本原高度增长及700条真实全局对合周期通过。只搜索短区间副本参数，不搜索平均词。未证明核心终止或降低N(p)。

新增全局总览：[averaging_global_status_20260912.md](averaging_global_status_20260912.md)汇总从二平均到任意q的已证判据、自动G点、非自动边缘H(q)、最终阈值N(q)与临界线猜想。它是导航文档；各项无限证明仍以对应定理文档和manifest核验入口为准。

新增 ten-twelve-seventeen-complete（core/full）：[十、十二平均17元完整判据](ten_twelve_average_seventeen_complete.md)分别使用(10,6,1)、(12,4,1)核和模17的18陪集、54条回路；十平均激活Delta(5)，十二平均激活Delta(3)，各自得到G=1充要，H(10)=H(12)=17。17个q<=200自动B点、各288本原模行、54回路、各60大整数入口、各3条完整路径通过。16元自动G点不计入H；不证明N或最短长度。

新增 six-prime-endpoint-entry（core/full）：[六素因子统一入口](prime_arity_six_prime_endpoint_entry.md)由五类非覆盖与d-1个实际坏类的证明承担一般量词。核对211040组五素数坏类、模24六类覆盖、6个大重数入口（含原K4障碍）及n15015的逐位置六步入口。大输入按精确重数保存，不展开上亿相等坐标，不搜索平均词。没有新的一般核心群包含或完整中间带结论。

新增 arena-triple-solver-review（core/full）：[外部Arena三平均算法审阅](arena_triple_solver_review.md)保存实际iframe算法快照并与48个旧输入比较。网页33题成功，旧构造48题成功；24个小整数实例的22题步数相同，1题更短、1题更长，预热后JS约0.85ms而旧Python约1.95ms。独立Fraction重放37条主测试成功路径、24条预热路径和33个宏基；另外核验整体放大导致浮点启发式不生成候选的例子。快检不重新计时，结论仅限该版本和样本，不更新数学可达性定理。

新增 four-prime-entry-and-band（core/full）：[四素因子入口](prime_arity_four_prime_endpoint_entry.md)的35784组坏指数类、64条原位置入口及12个强制见证合并通过；八个旧核心level的18192条回路重新核对，入口连接后得到其全部输入判据。另[中间带统一结构](prime_arity_band_period_and_involutions.md)核对127个维数参数对的381条全输入降维，以及1119组全r、全允许奇s的真实四原子标量周期和局部安全性。无限量词由正文的指数密度与矩阵公式证明；不搜索平均词，不生成新核心证书。七素数指数类可完全覆盖的边界另保留，不外推任意素因子数。

新增 averaging-algorithm-benchmark（core/full）：[算法测试集](averaging_algorithm_benchmark.md)核验584道唯一题面及580个冻结态结构、108条完整精确参考路径和1个阴性对照，并检查7项验解拒绝／大整数精度条件。不运行束搜索或重做完整高度枚举。p=7,n=15采用新定理真值，未获定理或证书的p=19,37扩展不计已知可达正确率。

新增 endpoint-reverse-diagnostic（core/full）：[端点反向诊断](prime_arity_endpoint_counterexample_reverse.md)报告p=7,n=15高度5的35714个状态和7个整数陷阱；独立脚本确认7个均无整数出边、首步均无零和七元组但二步有理层均产生零和七元组。该有限诊断不证明n=15全称可达，也不构成反例。

新增 strategy-reassessment-20260912：路线重评估和文献缓存为研究记录，不是证明核验。策略脚本缓存44个查询、148个去重题录；障碍脚本通过56个多素数单位分离、3538个返回字符和117个一般合并恒等式。

本文回答三个接手问题：哪项数学结论对应哪个程序，程序的 PASS 究竟证明到哪里，以及怎样在相同参数下重现当前数字。它是导航和复核契约，不替代证明文档。

新增 composite-endpoint-transfer（core/full）：[合数端点CRT推广](composite_endpoint_crt_transfer.md)使用独立证书核验器确认36个指定模数的32112条完整Schreier回路，主元因子全部落在已证允许环。28个两素数模数由统一三步入口得到全输入判据，8个三/四素数模数的入口已由四素因子定理补齐，36个列明level均为全输入结论。另960条回路实际编译正向DAG、98个基参数宏、168个一般入口、84个强制入口、5条完整词重放。有限范围内所有奇p<=109的端点均已完成；不宣称任意level成立或最优阈值。

新增 seven-average-fifteen-complete（core/full）：[七平均十五元完整证明](seven_average_fifteen_complete.md)给出至多两危险素数端点的统一三步入口，再用二进Gauss覆盖模15的24个陪集全部72条回路；62条左上、8条右下、2条半整数上剪切消除11和17主元，无需新宏种子。192个本原模行、10个实际基参数宏、1800个局部类型/安全性检查、160个大整数入口、72条强制三步入口和7条完整Fraction路径通过。G3/5/15排除，G1全称可达，H(7)=15；不证明后续全部维数或N(7)=15。

新增 six-average-ten-complete（core/full）：[六平均十元完整G判据](six_average_ten_complete.md)证明G=1或2恰好可达，G=5或10不可达。四个实际宏含一个两步R返回；三条精确周期给正向逆，DFD^-1F^-1=L(-5/3)产生模5下根，完整6陪集18回路覆盖Gamma_0(5)。核验8个基参数宏、24个本原模行、196种完整余数多重集、两种合法G各60个大整数入口和6条独立Fraction路径，最长1931步；另明确核对两个非法G例子。按用户以非自动G条件为主的标准，H(6)=10已证；N(6)及十一元仍未完成。

新增 composite-critical-scale（core/full）：[合数临界尺度报告](composite_critical_scale_and_conjecture.md)证明S(q)=max p^ceil(v_p(q)/2)给出的G1反例下界及边界G=q/S+1；固定四步网络q=m(m-1),n=m²在相邻因子有素数时达到下界。25865个完整压缩原子后继、368个边界退出、199个元数算术检查和14个全矩阵网络通过。M(q)=B(q)与N(q)=M(q)仍为两条独立猜想，边界G合法不自动可达。

新增 eight-average-thirteen-complete（core/full）：同一报告第7节由(8,4,1)核和真实周期C^4=-I/64、(A²C²)^3=I/4096构造正向二进控制器；带符号2幂代表使模13的42条完整回路均可编译。6个基参数宏、168个本原模行、120个大整数入口、5条完整路径（最长3577步）通过。结合至12元的反例，严格证明M(8)=13；不证明N(8)=13、九平均13元或最短长度。

新增 arbitrary-arity-linear-threshold（core/full）：[任意元数线性阈值](arbitrary_arity_linear_threshold.md)证明所有整数q>=3在n>=4q-1+d_q(n)时的完整G支持判据。一般量词由非单位配比、唯一中点例外、一般EGZ及系数打包证明承担。核对987个配比、172个中点例外、3040个容量、4488个四/六平均完整余数多重集、2804个大整数闭包及39次初始化；70条完整路径最长94步，另24条四/六平均造零收尾路径。全部15种算法分支均触及，不修改旧素数求解器适用域。未证明最优阈值或位长多项式输出长度。

新增 four-average-nine-complete（core/full）：[四平均九元完整判据](four_average_nine_complete.md)由显式(T2 Sigma)^2=-2I及仿射配对产生正向二进上下根，模9的12个陪集全部36条回路主元均为1、2、4，Schreier给出Gamma_0(9)包含，再接任意合法入口、Bezout和三步终端。检查72个本原模行、144个入口、50个大整数输送及6条完整四平均路径，最长621步。不做种子或路径搜索；不提供最短界或一位精度保证。

新增 four-average-seven-complete（core/full）：[四平均七元完整判据](four_average_seven_complete.md)使用 (4,2,1) 核，C^3=I/8、(CA)^2=I/8、C²B=Sigma/8均核对真实尺度；Sigma由真实词实现，禁止免费交换不等块。改取有符号2幂陪集代表，24条回路主元全为二进单位；16806个入口、80个大整数输送和12条完整路径（最长527步）通过。只解决七元，未解决四平均11、13、15元或N(4)=7。

新增 six-average-nine-fixed-network（core/full）：[六平均九元独立复核](six_average_nine_fixed_network.md)以9个标准基证明固定四步词恰为J9/9；穷尽84种第二次操作的756行，配合“第三步保留三行”证明不存在固定三步全输入词。另160个有理样本精确通过。四步最优只指固定全输入网络，不指每个输入，也不推出N(6)=9。

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

新增 shape-changing-integer-potential：形状变化整数检查点势。整数检查点记录 E=sum x_i^2；已有两步重叠造零和碰撞增大背景公式作为局部宏实例。此条是框架整理，不宣称全局宏存在性或 N(p)<=3p。

新增 shape-potential-literature-interface：定向阅读Grynkiewicz 2006零和子序列计数、Grynkiewicz--Ordaz--Varela--Villarroel 2007逆EGZ及Grynkiewicz 2011 Graham猜想。文档说明其可将失败余数层压缩到少数高重桶，但不能直接替代原位置安全平均；它们被用来设计保护池引理，而非宣称可达性。

新增 single-value-zero-sum-conjecture：记录“无混合p项零和则两大余数重数和≥3p-2”这一关键结构猜想，连接Grynkiewicz零和计数与形状变化势。有限p=3,5,7枚举支持但未证明无限量词。

补充：文档后半证明了一个独立重数结构定理：无混合p项零和时，重余数桶至多两个；双桶覆盖全池，单桶重数至少N-p+1。它是EGZ截断的正式结论，仍不等于原位置背景分支的终止证明。

修正结构定理范围：3p+1≤N<4p。
<!-- END SOURCE doc-8100ea423b9b -->

---

<a id="doc-dca8aa725c28"></a>

## 原文导签：核内缺口文献访问记录

来源：`work/core_gap_literature_20260914/README.md` · [逐字节原样副本](../sources/work/core_gap_literature_20260914/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`core-gap-four-lifts`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-dca8aa725c28 -->
# 核内缺口文献访问记录

整理日期：2026-09-15。目录名保留最初创建日期。数学复查见[正文](../sources/outputs/prime_arity/history/prime_arity_core_gap_reassessment_20260915.md)。

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

<!-- END SOURCE doc-dca8aa725c28 -->
