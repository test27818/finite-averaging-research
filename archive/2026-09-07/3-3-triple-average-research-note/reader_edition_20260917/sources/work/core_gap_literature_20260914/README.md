# 核内缺口文献访问记录

整理日期：2026-09-15。目录名保留最初创建日期。数学复查见[正文](../../outputs/prime_arity/history/prime_arity_core_gap_reassessment_20260915.md)。

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
