# 七元算术几何：实际阅读、外部接口与自足证明

2026-09-17。本轮以已有七元结构证明为主要数学来源，并核对尖点／模形式标准资料。没有向外发送消息。宽泛题录搜索部分429或无关，原始结果保存在query_*.json；不据其断言文献不存在。

## 1. 项目内直接读取并重核的基础

- [七元端点结构证明](../../../outputs/prime_arity/examples/seven_exact_threshold_structure.md)：第1—5节，包括两步入口、三宏周期、全部Γ₀(7)陪集回路及终端。第6节一般p的历史“未解”状态按文首后续说明理解。
- [原七／八元证明](../../../outputs/triple_average/proofs/triple_average_seven_eight_complete.md)：七元范数与宏部分。原十八词覆盖不是本轮充分性证明的依赖。
- [统一端点控制器](../../../outputs/prime_arity/tools/uniform_endpoint_positive_controller.md)：原位置返回、正向逆与局部化根的公式；七元只用既有短周期特例。
- [G障碍模](../G_as_obstruction_group_and_stable_threshold_20260916.md)：G的仿射格、余核、操作满射及目标饱和的量词。
- [早期算术几何整理](../../../outputs/triple_average/history/triple_average_arithmetic_geometry_view.md)：能量型、判别式以及“类数不能自动决定可达性”的边界。

已重跑原七元结构核验器，不修改原文件。新增核验进一步将一般Bezout矩阵作Euclid／Schreier改写并重放实际位置操作。

本目录向outputs的相对路径需经过research/prime_arity_padic/子目录；以上链接在提交前按实际文件位置核对。

## 2. Sage官方文档：尖点与亏格的标准交叉核对

- [Γ₀(N)文档](https://doc.sagemath.org/html/en/reference/arithgroup/sage/modular/arithgroup/congroup_gamma0.html)：实际读ncusps条目，素数level均有两个尖点；[本地页面](sage_gamma0.html)、[来源](sage_gamma0_source.json)。
- [Arithmetic subgroup文档](https://doc.sagemath.org/html/en/reference/arithgroup/sage/modular/arithgroup/arithgroup_generic.html)：实际读cusp_width和genus条目。前者示例显示Γ₀(11)的∞宽1、0宽11；后者Γ₀(n)表确认n=7亏格0。[本地页面](sage_arithmetic.html)、[来源](sage_arithmetic_source.json)。

七元两个轨道与宽度1、7在新文稿中用Bezout和矩阵直接证明，不依赖运行Sage。亏格0仅作模曲线背景，不用于G充分性推理。没有在当前Python环境假装安装或执行Sage。

## 3. Stein书：实际读取的Eisenstein模性定理

William Stein, *Modular Forms, a Computational Approach*，在线章节[Eisenstein Series and Bernoulli Numbers](https://wstein.org/books/modform/modform/eisenstein.html)。

- [保存页面](stein_eisenstein.html)、[带公式的可读文本](stein_eisenstein_readable.txt)、[来源散列](stein_eisenstein_source.json)。
- 实际读“Explicit Basis for the Eisenstein Subspace”，公式(4)、Theorem5.8及附近的定义和常数项。该页公式使用图片alt文本，已将alt恢复入可读文本；不把丢失公式的普通HTML去标签结果当成完整陈述。
- 定理5.8：原始Dirichlet特征χ、ψ满足χ(−1)ψ(−1)=(−1)^k时，除weight2平凡特征例外，所定义E_(k,χ,ψ)(q^t)属于对应level和特征的模形式空间。
- 本题k=1、χ=1、ψ=χ₋₇、t=1，故theta计数恒等式识别出的2E_(1,1,χ₋₇)为level7、weight1、特征χ₋₇的模形式。

本页一般模性引用Stein对Miyake第7章结论的整理；没有取得并重审Miyake原章证明。系数恒等式、Euclidean环、理想范数计数在研究正文中自足证明。未引用该章其它basis/eigenform断言作为额外必要依赖。

另读取[dimension formulas章节](https://wstein.org/books/modform/modform/dimension_formulas.html)的权重适用范围；未将k≥2的公式用于本题weight1。保存页面和来源仅用于记录这次适用性检查。

## 4. 取得但不作为数学来源的材料

LMFDB尝试页面返回HTTP200但只有650字节、无可用曲线数据，故不引用；记录见lmfdb_7_source.json。最初猜测的Stein章节URL404，后从书目录定位到实际Eisenstein章节，错误访问保留在stein_modular_source.json。

取得Sage二元二次型页面，但本文没有借其算法或输出证明类数；Q(√−7)范数Euclidean性有11/16覆盖界的直接证明。因此不把下载文件视为已引用的定理。

## 5. 本轮结论的来源边界

- 七元可平均当且仅当G=1：已有项目定理，本轮用结构版重新接通。
- 指定宏菜单恰生成𝔅₇(Z[1/6])：由既有根与整数群包含新增R点补齐证明。
- 分歧素理想单位条件、两个尖点轨道、能量层本原表示公式：正文直接证明。
- theta级数的模性：引用已读Stein Theorem5.8；不是可达性证明前提。

因此本轮不是借“模曲线／自守形式”替代真实操作，而是标明它们与真实操作已经能够严格对接的七元实例。
