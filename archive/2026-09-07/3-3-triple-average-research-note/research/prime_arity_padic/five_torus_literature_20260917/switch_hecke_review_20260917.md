# 有界切换之后的文献调查：Lucas赋值、混合逼近与Hecke周期

2026-09-17，续[上一轮适用性审查](targeted_review_20260917.md)。本轮没有找到三平均五元的现成全分类，但找到一条确实能代入的Hecke／连分数定理，并借Lucas赋值定理识别D=1族的第一段。

查询保存在switch_query_*.json、gap_query_*.json、gap_followup_query_*.json、order_query_*.json。后者宽泛search再次给出大量无关结果，未据此声称类数文献适用。没有通过题录结果或论文标题推定定理成立。

## 1. Aka–Shapira：这次能够真正代入

Menny Aka, Uri Shapira, *On the evolution of continued fractions in a fixed quadratic field*, Journal d’Analyse Mathématique134 (2018),335–397，DOI[10.1007/s11854-018-0012-4](https://doi.org/10.1007/s11854-018-0012-4)。

- [作者稿](https://arxiv.org/pdf/1201.1280)，取得的是v2，2013-02-21，不以文件命名年份冒充稿件版本。
- [本地PDF](aka_shapira_quadratic_continued_fractions_2018.pdf)、[文本](aka_shapira_quadratic_continued_fractions_2018.txt)、[来源散列](aka_shapira_quadratic_continued_fractions_2018_source.json)。
- 实际读：摘要、§1、§2至Theorems2.8、2.12、Corollary2.10及Definition2.6；另检索§4中Hecke图与分裂／退化分支的定义位置。没有全文重审谱隙证明。
- 期刊PDF链接返回HTML而不是PDF，见[记录](aka_shapira_journal_attempt.json)；未将其视为取得期刊全文。

定理2.8(2)对S中素数都不分裂于Q(θ)时，给γθ的普通实连分数周期测度随着ht(γ)→∞趋于Gauss测度，且误差对γ一致。这里ht是本原整数代表的行列式绝对值，**不是矩阵最大系数**。

本题取θ=(−7+3√5)/2、S={3}、γ=W⁻¹。3惰性，正词矩阵及其伴随本原，故ht(W⁻¹)=3^L。全部假设满足，得到长词拉回零方向的连分数周期等分布。定理2.12给周期长度与3^L同阶。

独立初等证明进一步说明，同长度词的拉回范数型在GL₂(Z)乃至SL₂(Z)下等价；所以这些二次无理点的普通连分数周期本来就相同。定理研究的是这个共同周期随导子增长的分布。

**准确边界：** 周期等分布不控制标记Ce，不能据此推出F_f(Ce)=±5D的命中有限。需一个将真实正词约束传到周期中指定位置的额外定理。本轮没有把这项缺口隐藏在“均匀”一词中。

## 2. Lucas赋值：直接使用的数列公式

Nadir Murru, Carlo Sanna, *On the k-regularity of the k-adic valuation of Lucas sequences*, J. Théor. Nombres Bordeaux30 (2018),227–237，DOI[10.5802/jtnb.1025](https://doi.org/10.5802/jtnb.1025)。

- [作者稿](https://arxiv.org/pdf/1603.09310)，实际v3，2016-06-04。
- [本地PDF](lucas_valuations_regularity_2018.pdf)、[文本](lucas_valuations_regularity_2018.txt)、[来源](lucas_valuations_regularity_2018_source.json)。
- 实际读：引言、Theorems1.1–1.6、§2初始定义及k-regular性质；所用公式为Theorem1.5的标准Lucas赋值式。

代入Fibonacci递推a=b=1、p=3、Δ=5、τ(3)=4、v₃(F₄)=1，得v₃(F_n)=1+v₃(n)当4|n，否则0。结合F_(2n)=F_nL_n和本项目D=1的Lucas表达式，得

\[
v_3(u_k)=v_3(2k+1),\qquad v_3(v_k)=v_3(2k-1).
\]

赋值恒等式也可直接由单位φ的二项式提升证明，正文给了这条自足来源。k-regular只用于解释这种字段可以很简单，不从它推出整个可解语言有限自动机可识别。

## 3. 混合Littlewood文献：有启发，但不作为原问题有限性的证明

Paloma Bengoechea, Evgeniy Zorin, *On the Mixed Littlewood Conjecture and continued fractions in quadratic fields*, Journal of Number Theory162 (2016),1–10，DOI[10.1016/j.jnt.2015.10.007](https://doi.org/10.1016/j.jnt.2015.10.007)。OpenAlex题录列2015；Crossref期刊出版日期为2016-05，本文采用后者。

- [作者稿](https://arxiv.org/pdf/1409.3439)，实际v1，2014-09-11。
- [PDF](mixed_littlewood_quadratic_2015.pdf)、[文本](mixed_littlewood_quadratic_2015.txt)、[来源](mixed_littlewood_quadratic_2015_source.json)。文件名2015保留下载时命名，不代表正式出版年份。
- 实际读：引言、Theorem2.1、Hypothesis1、Lemma2.3开头及Aka–Shapira的引用接点；未重审后半部分证明。

论文以Aka–Shapira结果处理二次无理数的实逼近与有限素集的整除条件。它说明“二次无理数实上难以逼近”与“加上某个p进整除条件仍可得到许多好逼近”并不冲突。其候选整数不要求落在本题正词轨道中，所以既不能给本题反例，也不能给固定D有限性。

Bernard de Mathan, *On a mixed Littlewood conjecture for quadratic numbers*, J. Théor. Nombres Bordeaux17 (2005),207–215，DOI[10.5802/jtnb.487](https://doi.org/10.5802/jtnb.487)。OpenAlex/Crossref在线日期显示2008；[期刊卷页](https://jtnb.centre-mersenne.org/item/JTNB_2005__17_1_207_0/)明确纸本年份2005。

- [PDF](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.487.pdf)、[本地PDF](mixed_littlewood_quadratic_2005.pdf)、[来源](mixed_littlewood_quadratic_2005_source.json)。
- 实际读摘要和引言文字；提取文本漏掉关键公式，因此**没有依此援引Theorem1.2的精确不等式**。相关背景从Bengoechea–Zorin清晰作者稿交叉读取。

## 4. 这一轮真正带回来的东西

外部工具并非完全无用：Lucas赋值给直接算术字段；Hecke／谱隙工具确实控制共同周期。另一方面，计算共同二次型类并不会产生所求判据，因为所有同长度词已经在同一类。

新重点是共同周期上的**标记位置**，不是重新追逐不同类。完整的新公式、格分解和仍缺的量词见[研究正文](../five_explicit_gap_common_hecke_form_20260917.md)。
