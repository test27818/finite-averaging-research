# 五元问题的定向外部调查与适用性审查

2026-09-17。目的不是搜到相似名词就引用，而是查是否已有直接答案，并核对轨道整数点定理能否处理本题的两个一次分支。本页记录实际取得、实际读取和未能适用的原因；不声称全文重审所有证明。

## 1. 检索记录

OpenAlex的12条标题查询、8条扩展标题查询、6条全文题录查询，分别保存在targeted_query_*.json、extended_query_*.json、broader_query_*.json。包括clique gossiping、perfect mixability、integral points in orbits、semigroup orbits、S-unit points、p-adic path set、Pell equation matrix semigroup等。宽泛查询出现大量无关结果，未当成证据。入口脚本：[search_five_orbit_literature.py](search_five_orbit_literature.py)。

另用Stack Exchange公开API检索MathOverflow和Mathematics上的averaging、five numbers、Pell与p-adic Cantor，六条查询见community_query_*.json，读取的问答原文见community_*_questions.json及community_*_answers.json。没有发帖或向作者发送消息。

本轮没有找到直接覆盖“有理五元三平均静态分类”的现成答案。这不是已证明不存在相关文献，尤其题录搜索可能漏掉竞赛题、不同术语或未收录文稿。

## 2. 最贴近模型的来源：Clique Gossiping

Yang Liu, Bo Li, Brian D. O. Anderson, Guodong Shi, *Clique Gossiping*。

- [实际取得版本](https://arxiv.org/pdf/1706.02540)：PDF首页明确为arXiv:1706.02540v1，2017-06-08。
- 期刊题录DOI：[10.1109/TNET.2019.2952082](https://doi.org/10.1109/TNET.2019.2952082)。未取得并核对期刊最终正文。
- 本地[PDF](clique_gossiping_2017.pdf)、[文本](clique_gossiping_2017.txt)、[SHA256](clique_gossiping_2017_source.json)。

实际读：定义3的原子等权操作，§4开头及定义8，定义9，定理3，§4.2必要性证明及§4.3零测论证。其操作确实与固定位置平均一致；目标主要是一个网络对所有实初值有限收敛，区别于给定有理初值的分类。

**重要核查结果：不能引用该v1定理3的m|n必要性。** 项目已有六平均九位置固定四步网络与其直接冲突，不仅是量词不一样：该网络对全部实初值都有效。重新独立乘9×9有理矩阵，结果为J9/9，81项逐项精确验证。

错误所在：§4.2第二项声称约成最简后的分母始终含某个p的指定幂次；分子相消可消去该因子，平均分母包含p并不意味着最简分母始终包含p。取e1作为初值，四步网络最后成为(1/9,...,1/9)，最简分母没有2。此判断只针对取得的v1，不推断最终版未修正。

§4.3“可解实点是可数个线性子空间之并”的观察本身仍有用，但不能从实零测推断有理格点的零密度，也不给五元算术全分类。

## 3. 最直接的半群整数点定理：次数假设不符

Jorge Mello, *On quantitative estimates for quasiintegral points in orbits of semigroups of rational maps*, New York J. Math.25 (2019),1091–1111。

- [期刊PDF](https://nyjm.albany.edu/j/2019/25-47p.pdf)、[本地PDF](mello_quasiintegral_semigroups_2019.pdf)、[文本](mello_quasiintegral_semigroups_2019.txt)、[来源](mello_quasiintegral_semigroups_2019_source.json)。
- 实际读：第1091–1092页引言及Theorem A；检索正文相关次数假设，并读取第1099页末到§5开头。没有重审其Roth估计证明。
- Theorem A要求每个生成映射次数≥2，还有无全分歧／轨道不重复等条件。我们的α↦J(ε^±1α)次数1。不能代入，也不能把矩阵行列式−3误当映射次数3。
- 下载时两个猜测文件名404，后由期刊卷目录与摘要页取得正确的25-47p.pdf，记录保留。

Jorge Mello, *On intersections of polynomial semigroups orbits with plane lines*, Canadian Math. Bull.，DOI[10.4153/S0008439520000557](https://doi.org/10.4153/S0008439520000557)。

- [作者稿](https://arxiv.org/pdf/1907.03934)、[本地PDF](semigroup_plane_lines_2020.pdf)、[来源](semigroup_plane_lines_2020_source.json)。
- 实际读：引言、Theorem1.1、§2轨道定义。
- Theorem1.1要求成对多项式同次数>1，且排除双边线性共轭的单项式；还要求一个相容无限路径的交点无穷或映射可交换。本题既非这类多项式，也不满足次数条件。

Jorge Mello, Yu Yasufuku, *On higher dimensional integrality and multiplicative dependence in semi-group algebraic dynamics*, arXiv:2604.03745v1 (2026)。

- [作者稿](https://arxiv.org/pdf/2604.03745)、[本地PDF](semigroup_integrality_2026.pdf)、[来源](semigroup_integrality_2026_source.json)。
- 实际读：引言、Theorems1.1–1.2、Corollary1.3和Hypε讨论，以及引用表。
- 要求各射影态射次数≥2，并有指定的整数点非稠密假设。文中讨论Vojta猜想的关联，但不能据此把本题的正半群轨道有限性称为已由Vojta推出。

## 4. 代数对应的现成定理：核对了真正的缺失接口

Jorge Mello, *On sparsity of integral points in orbits and correspondences with big pullbacks under iterates*, arXiv:2501.04642v2 (2025)。

- [作者稿](https://arxiv.org/pdf/2501.04642)、[本地PDF](mello_big_pullbacks_2025.pdf)、[文本](mello_big_pullbacks_2025.txt)、[来源](mello_big_pullbacks_2025_source.json)。
- 实际读：引言Theorems1.2–1.5，§4的极化定义与Definition4.2（CIP），§5.1的Theorem5.1及Corollary5.2–5.3。未重审其引用的He–Ru与Ingram理论。

这篇比普通次数≥2映射更接近本题，因为允许多值对应。**但CIP不是简单地把所有前驱取并集。** 它要求除子逐步满足y*L_(i−1)=x*L_i。本题正规化投影x(t)=(t+1)²/t，y(t)=(t−4)²/[3(1−t)]均为二次；这条等式强迫每步deg L_i不变。一个点除子不能经CIP变成支撑至少三个点的有效除子，因此不满足Theorem1.5。

还直接算出范数点−5不具有第一步CIP：y*[-5]由t²−23t+31=0的两点组成，不在源投影的换支t↦1/t下不变。详细证明见[新研究第7节](../five_bounded_switches_and_correspondence_degree_20260917.md)。

这是一个有用的否定接口：五元已确实转成“对应轨道里的有界分母点”，只是这条对应没有该定理的扩张资源。不能把有两条分支与每条映射的代数次数混为一谈。

## 5. 三进分形及已有平均问答

William Abram, Jeffrey C. Lagarias, *p-adic path set fractals and arithmetic*, J. Fractal Geometry1 (2014)，DOI[10.4171/JFG/2](https://doi.org/10.4171/JFG/2)。

- [作者稿](https://arxiv.org/pdf/1210.2478)、[本地PDF](padic_path_set_fractals_2014.pdf)、[来源](padic_path_set_fractals_2014_source.json)。
- 实际读：摘要、§1至Theorems1.1–1.3（前三页）。对象按有限标号图中的普通p进数字路径定义，给维数及有理平移、Minkowski和的封闭性。
- 本题已有普通三进前缀非正则性，因此不能仅凭符号地址有两种字母就认定落在该有限自动机类。本文不引用其维数公式作为本题证明。

MathOverflow：[整数多重集的平均游戏](https://mathoverflow.net/questions/373175/an-averaging-game-on-finite-multisets-of-integers)，以及[2进整数上的平均过程](https://mathoverflow.net/questions/374084/an-averaging-procedure-on-finite-multisets-of-2-adic-integers)。已读取问题与API返回的现有答案。

前者限制同奇偶的整数二平均，问最长／最短终止及组合游戏；后者给四个2进数、可由无限二元序列编码的不终止例子。这与本项目“整数能量下降和p进无限边界分工”的视角相关，但不涉及三平均五元的静态判据。社区答案仅作为相关思路来源，不当作已发表的总分类定理。

## 6. 对研究路线的实际影响

本轮没有借外部论文宣布固定D有限性。受到“固定迭代”和“任意变换半群”需要分清的启发，补上了介于二者之间的通用定理：固定同方向段数时，任意独立段长都只有有限个固定D返回，而且有效。

证明完全初等：段长归一化后的参数只有一个有理极限0，模5标记阻止有限个极限投影消掉种子，Q_5的有理各向异性及实紧致性给正下界。见[完整证明](../five_bounded_switches_and_correspondence_degree_20260917.md)。外部检索改变了问题的分层和假设核对，但不是把一个不适用的深定理当作证明。
