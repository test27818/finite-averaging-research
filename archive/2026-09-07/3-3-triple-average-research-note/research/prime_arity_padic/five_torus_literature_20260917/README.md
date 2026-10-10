# 五元环面研究的外部定理记录

2026-09-17。本目录保存实际使用的外部来源，以及后续定向查询和适用性核对记录。新增调查先读[六份全文与相关问答的适用性审查](targeted_review_20260917.md)；其中不适用的定理没有被引作证明。

**后续连分数／Hecke调查：** [Lucas赋值与共同Hecke周期](switch_hecke_review_20260917.md)。Aka–Shapira的不分裂素数情形确实适用于本题零方向的拉回，给普通连分数周期等分布；Murru–Sanna赋值公式给D=1族第一段长度。两项均不直接解决任意切换的固定D有限性。记录了实际稿件版本、期刊年份纠正和不能引用的公式提取缺失。

**统一逃逸方向：** [ESS多参数归约与Baker有效增长](uniform_escape_review_20260917.md)。ESS此次通过极小零子和把固定多块模板的指数解集化成有限个格陪集，再由本题实能量／三进谱排除恒值非负射线。固定混合周期另用正式转述的Baker–Wüstholz推论给有效指数增长。分形逼近资料虽相关，未直接适用，不作为全词逃逸的证明。

**来源：** J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics **155 (2002), 807–836**。arXiv上传日期2004不是正式出版年份。

- [arXiv作者稿PDF](https://arxiv.org/pdf/math/0409604)
- [本地PDF](evertse_schlickewei_schmidt_2002.pdf)
- [提取文本](evertse_schlickewei_schmidt_2002.txt)
- [访问URL、字节数及SHA256](source.json)

实际读取：第807页摘要／定义，第808页定理1.1，第809页两变量先前界，第810—811页关于S单位及有限生成群的适用说明。没有声称重审全部证明。

**所用结论：** 特征0域中有限秩乘法群Γ⊂(K^×)^n，方程Σa_i x_i=1的非退化解有限。原定理还给仅依n及秩的显式上界；最初相邻S单位研究只用有限性，后续固定周期返回定理使用其参数一致上界，不将巨大上界用作实际搜索截止。

**本题代入：** F=Q(√5)，S有限且含所有无穷位与2、3上方素位，Γ=(O_(F,S)^×)²，n=2，a_1=a_2=1。群为有限秩，非零两项的和为1自动无零真子和，因此所有相关解均非退化。先由J(γ)=−(2γ+1)/(γ+2)及2(γ+2)−(2γ+1)=3，证明γ、Jγ均为S单位迫使2γ+1也是S单位；然后应用定理，不能省略这段归约。

**结论边界：** 只证明固定S内相邻环面点对有限，不枚举它们、不宣称高效可计算界、不把这条有限性当成平均可解判据。原位置数值的分母仍只含3；这里的辅助素数由环面有理坐标引入。

前期宽泛题录查询含无关结果，未用作证明。下载后的Python PDF解析库不可用，实际以本机pdftotext提取成功；原PDF保存并校验文件头，不因最初文本提取失败而重复声称阅读。

## Baker--Brumer定理的正式转述

Adel Betina, Mladen Dimitrov, *Geometry of the eigencurve at CM points and trivial zeros of Katz p-adic L-functions*, Advances in Mathematics **384 (2021),107724**，DOI [10.1016/j.aim.2021.107724](https://doi.org/10.1016/j.aim.2021.107724)。取得arXiv:1907.09422v3作者稿：

- [公开PDF](https://arxiv.org/pdf/1907.09422)
- [本地PDF](eigencurve_cm_baker_brumer_2021.pdf)、[文本](eigencurve_cm_baker_brumer_2021.txt)
- [访问与SHA256记录](eigencurve_cm_source.json)
- [已目视核对的第8页](baker_brumer_statement_page8.png)

实际阅读：摘要／标题信息，§1.5定理1.6及相关定义，引用表中[7]。定理1.6说明相应p进对数在Q上线性独立可提升到Qbar上线性独立；文本提取会把两种Q都显示为Q，所以已渲染原页并目视核对横线。

原始来源为A. Brumer, *On the units of algebraic number fields*, Mathematika **14 (1967),121–124**，本轮只取得题录而未取得原全文。因此本项目引用的是正式论文中的标准定理转述，没有声称重新证明／全文审查Brumer定理。

**本题代入：** α∈Q(√5)的范数1主单位、ρ=ε⁴。若α的最小整环分母D>1，则其某个素位赋值非零、而ρ处处单位，故α与ρ乘法独立。3进log在该主单位群上单射，得到两个对数Q线性独立；定理推出它们Qbar线性独立，因而log_3α/log_3ρ超越。没有使用文中强四指数猜想、六指数定理、eigencurve几何或p进L函数结论。

## Skolem–Mahler–Lech零点定理的标准转述

Jason P. Bell, Jeffrey C. Lagarias, *A Skolem–Mahler–Lech theorem for iterated automorphisms of K-algebras*, Canadian J. Math.67(2) (2015),286–314，DOI[10.4153/CJM-2013-048-3](https://doi.org/10.4153/CJM-2013-048-3)。

- [作者稿](https://arxiv.org/pdf/1312.5305)、[本地PDF](bell_lagarias_skolem_mahler_lech_2013.pdf)、[来源与阅读范围](skolem_mahler_lech_source.json)。
- 实际读：作者稿前三页，引言§1.1的经典递推零点定理1.3；未调用较强的K代数自同构结果。
- 只应用于固定M时Q_5(M^nx)−c的线性递推。配合不同特征根比不是单位根，零点有限；不由此宣称有效截止，更不应用于任意变化的平均词。

后续[固定周期返回文稿](../five_fixed_D_effective_sparsity_and_periodic_return_20260917.md)以ESS给统一有限次数，SML为另一有限性证明。最新[有界切换文稿](../five_bounded_switches_and_correspondence_degree_20260917.md)独立使用初等紧致性，不需要以上深定理。
