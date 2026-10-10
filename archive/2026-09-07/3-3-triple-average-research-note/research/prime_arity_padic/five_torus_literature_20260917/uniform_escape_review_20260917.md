# 全词逃逸方向：外部定理的实际贡献与适用边界

2026-09-17，接前两轮阅读。本轮主成果是[固定多块模板的统一逃逸](../five_bounded_templates_uniform_escape_20260917.md)，不是全词猜想已证。

## 1. ESS不再只用于相邻单位或一个周期

重新读取Evertse–Schlickewei–Schmidt作者稿第807–809页、Theorem1.1及非退化定义，来源仍为本目录已存[PDF](evertse_schlickewei_schmidt_2002.pdf)。

这次的代入是固定r个重复块的特征值指数向量，其乘法群由r个参数方向生成，秩≤r。范数展开是有限个乘法特征之和。通过全部极小零子和划分，ESS把整数参数解集化成有限个格陪集。再由非负格中可比较的两点抽出指数射线，本题能量与三进谱排除所有恒值射线。

没有把非退化解有限误写成全部解有限；退化部分由格陪集归约处理。也没有把ESS解数上界当成指数最大值上界。因此多模板结论目前是有限性／统一逃逸，未给有效截止。

## 2. 固定周期的有效增长：实际使用Baker下界

Joël Ouaknine, James Worrell, *On the Positivity Problem for Simple Linear Recurrence Sequences*, ICALP2014，DOI[10.1007/978-3-662-43951-7_27](https://doi.org/10.1007/978-3-662-43951-7_27)。

- [作者稿](https://arxiv.org/pdf/1309.1550)，实际为v3，2014-04-28。
- [本地PDF](positivity_simple_baker_2014.pdf)、[文本](positivity_simple_baker_2014.txt)、[下载散列](positivity_simple_baker_2014_source.json)。
- 实际读：引言及§3关于有限极小点与Baker下界的说明；附录A Theorem7、Corollary8及其证明；引用表原Baker–Wüstholz来源。

Corollary8：对单位圆上的代数数λ、ζ，若λ^n≠ζ，则|λ^n−ζ|有可计算的n负幂下界。证明应用Theorem7的对数线性式下界，包含log(−1)来记录辐角的整周差。

本题固定混合块M的复特征值情形，把Q_5(M^nx)/det(M)^n化成单位圆上的一个固定二次Laurent多项式。其零点只有有限个；不会精确命中零，因为Q_5无非零有理零点。故该推论直接给有效指数／多项式逃逸下界。

原始来源是A. Baker, G. Wüstholz, *Logarithmic forms and group varieties*, J. Reine Angew. Math.442 (1993)。本轮使用上述正式论文的转述和推论，没有宣称取得或重审1993年原证明，也没有调用整篇正性判定算法。

同时取得Ouaknine–Worrell的 *Ultimate Positivity is Decidable for Simple Linear Recurrence Sequences*，[作者稿](https://arxiv.org/pdf/1309.1914)、[本地PDF](ultimate_positivity_2014.pdf)、[来源](ultimate_positivity_2014_source.json)。实际稿为v4，2017-04-05，文件名保留初始题录年份。阅读引言、非有效性与Baker方法的区别及引用表，用于追到上一来源；不援引其完整判定算法。

## 3. 分形逼近文献：为什么没有直接套用

Lior Fishman, David Simmons, *Extrinsic Diophantine approximation on manifolds and fractals*, DOI[10.1016/j.matpur.2015.02.002](https://doi.org/10.1016/j.matpur.2015.02.002)。

- [作者稿](https://arxiv.org/pdf/1406.0785)，实际v3，2015-01-10。
- [本地PDF](extrinsic_fractals_2015.pdf)、[来源](extrinsic_fractals_2015_source.json)。
- 实际读：摘要、引言、Theorem1.1与Corollary1.2。
- 其Dirichlet型结论研究实流形／实IFS极限集内的点，由集合外有理数逼近。我们的成功方向实稠密，限制却在三进处；此外目标是某个指定二次无理方向的**受限**逼近。不能据这个存在性结论推出本题禁止某类逼近。

Johannes Schleischitz, *On intrinsic and extrinsic rational approximation to Cantor sets*, DOI[10.1017/etds.2020.7](https://doi.org/10.1017/etds.2020.7)。

- [作者稿](https://arxiv.org/pdf/1812.10689)，实际v4，2019-09-09。
- [本地PDF](cantor_intrinsic_extrinsic_2020.pdf)、[来源](cantor_intrinsic_extrinsic_2020_source.json)。
- 实际读：摘要、§1.1及Definition1，辨认其收缩、实IFS与保有理假设。未声称读取并适配其全部高度估计。
- 本题两个Möbius分支不能直接当成该实仿射IFS，普通斜率三进前缀还已证明非正则，因此不能仅因为都称Cantor就搬用缺位数字结论。

## 4. 检索失败和未读范围也保留

查询记录：escape_query_*.json、escape_crossref_*.json、escape_context_query_*.json、escape_structure_query_*.json、escape_fractal_query_*.json、escape_recurrence_query_*.json等。OpenAlex本轮并行题录查询部分返回429，随后改用Crossref及单个DOI定位，没有把请求失败当作“无文献”。若干宽泛查询无关，不作为研究证据。

Mahler／Cantor论文取得题录及仓储页面，但仓储页面没有可用PDF链接；本轮未读全文，不引用其定理，详见mahler_cantor_*.json。另一些矩阵半群、Markoff、稀疏轨道搜索仅有题录，没有把表面相关性当成适用性。

目前真正承载新证明的是ESS的有限秩方程定理，以及用于单周期有效增长的Baker下界；任意换词的全局统一常数仍缺失。
