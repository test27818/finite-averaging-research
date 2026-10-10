# 整体结构调查的文献访问记录

2026-09-16。研究报告见[二维格几何与内容对偶](../global_structure_and_bounded_fiber_geometry_20260916.md)。本目录不修改原完成证明或全项目注册。

## 检索范围与筛选

保存32个OpenAlex请求、130条去重题录，涉及格宽／平坦性、二维整数凸包、参数整数规划、Graver与Markov基、低维矩阵半群可达、正则语言、有限时间共识和Clique Gossiping。`query_00`至`query_31`保留原查询及返回；泛关键词产生了明显无关的物理／医学等结果，均未作为证据。32次请求不是32个有用文献方向，130条题录不是130篇全文阅读。

以下5份PDF通过`%PDF`文件头验证并保存原始字节，再提取文本。每份`*_source.json`保存请求URL、最终URL、HTTP状态、字节数、SHA256。只引用下列实际读到的段落。

## 实际取得并阅读

1. **Gennadiy Averkov, Johannes Hofscheier, Benjamin Nill.** *Generalized flatness constants, spanning lattice polytopes, and the Gromov width*. Manuscripta Mathematica **170 (2023),147–165**，2021-12-31在线发表。DOI：[10.1007/s00229-021-01363-x](https://doi.org/10.1007/s00229-021-01363-x)。[正式PDF](https://link.springer.com/content/pdf/10.1007/s00229-021-01363-x.pdf)；[本地PDF](generalized_flatness_2021.pdf)、[文本](generalized_flatness_2021.txt)。
   - 阅读摘要、§§2.1–2.2（定理2.1、二维ILC(2)=3、与半群Hilbert基的区别）、§4定理2.1的证明相关段落。
   - 本题实际用到：宽凸体包含幺模单形；二维空格三角形幺模。后者在报告中另给自足证明。
   - 未将§3的Gromov宽度或辛几何结果用作平均可达性结论；文件名2021指在线年份，不把正式卷年写错。

2. **Igor Potapov, Pavel Semukhin.** *Vector Reachability Problem in SL(2,Z)*. MFCS2016, LIPIcs58,84:1–84:14。DOI：[10.4230/LIPIcs.MFCS.2016.84](https://doi.org/10.4230/LIPIcs.MFCS.2016.84)。[本地PDF](reachability_sl2_2016.pdf)、[文本](reachability_sl2_2016.txt)。
   - 阅读摘要、引言、§2定义、主定理14的收尾及§4命题15的正则语言限制版本与复杂度边界。
   - 仅用于确认有限菜单的向量／射影可达与词语言之间的准确接口。没有把其SL2(Z)前提扩成GL2(Q)，也没有调用算法来证明任意p的可达性。

3. **Thomas Colcombet, Joël Ouaknine, Pavel Semukhin, James Worrell.** *On Reachability Problems for Low-Dimensional Matrix Semigroups*. ICALP2019, LIPIcs132,44:1–44:15。DOI：[10.4230/LIPIcs.ICALP.2019.44](https://doi.org/10.4230/LIPIcs.ICALP.2019.44)。[本地PDF](low_dimensional_semigroups_2019.pdf)、[文本](low_dimensional_semigroups_2019.txt)。
   - 阅读摘要、引言的精确问题与群定义、§4定理16–17及证明收尾。
   - 该文GL2(Z)指整数逆，即行列式±1；不是所有满秩整数矩阵。半空间可达也不同于精确零超平面可达。未用其2019年引言判断2026年哪些一般问题仍开放。

4. **Alessio Mansutti, Mikhail R. Starchak.** *One-Parametric Presburger Arithmetic Has Quantifier Elimination*. MFCS2025, LIPIcs345,72:1–72:18。DOI：[10.4230/LIPIcs.MFCS.2025.72](https://doi.org/10.4230/LIPIcs.MFCS.2025.72)。[本地PDF](presburger_quantifiers_2025.pdf)、[文本](presburger_quantifiers_2025.txt)。
   - 阅读摘要、§1，含定理2–3、语言定义、CRT示例、适用性与复杂度说明；检索后文系数消元的接口，未通读全部算法正确性证明。
   - 一参数t允许t乘变量，并不允许任意两个计数变量相乘。本题p、r及来源／输出的双线性关系不能直接当作这一语言；只可作为某些已选一参数公式的验证工具。

5. **Imre Bárány.** *Random points and lattice points in convex bodies*. Bulletin AMS **45 (2008)**。DOI：[10.1090/S0273-0979-08-01210-X](https://doi.org/10.1090/S0273-0979-08-01210-X)。[作者稿PDF](https://real.mtak.hu/57662/1/rsurv.pdf)；[本地PDF](barany_lattice_survey_2008.pdf)、[文本](barany_lattice_survey_2008.txt)。
   - 阅读摘要及§13的整数凸包、定理13.1和引理13.2所述平坦性用途。
   - 仅作背景与来源追踪，未用随机多面体或渐近顶点计数作本题全参数非空证明。

## 已有来源的回读

读取[上一轮整数移动来源记录](../literature_integer_moves/README.md)，并对照项目中对Graver同号分解、Markov基以及有界库存的使用范围。没有把此前未取得全文的Diaconis–Sturmfels或Onn专著升级为已读全文。

## 未取得／仅题录

- Bogart–Goodrick–Woods 2017的Discrete Analysis下载返回HTTP200但**零字节**，未作为已读PDF。其背景由已读2025论文准确引用，未直接引用2017原文中的独立新定理。
- 1988年RAIRO *Parametric integer programming* 的公开PDF请求超时，未读正文。
- Bounded contingency tables、二维整数凸包算法、Clique Gossiping等本轮仅核对检索题录及其访问位置，未移用未读定理。
- 本轮没有联系作者、发送问题或发布成果；所有新增文件均为本地研究记录。

## 计算职责

`fiber_geometry_probe.py`及`verify_geometry_and_content.py`枚举的是限定来源的有界计数纤维，检查新结构引理的公式和实例；不搜索平均词，不证明全参数资源存在，不运行旧的大模群搜索。

研究报告的新一般证明与外部平坦性推论逐项分开。文件下载成功或有限核验通过都不代替该区分。
