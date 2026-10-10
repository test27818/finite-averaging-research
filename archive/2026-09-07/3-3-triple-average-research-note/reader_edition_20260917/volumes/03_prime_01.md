# 一般素数平均：基线、区间与独立简化 · 第1分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/03_prime_proof.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [素数平均最优最终阈值：总证明与技术依赖](#doc-a67f17315652)
- [本次整理的阅读、修改与核验范围](#doc-9fe4112b0e61)
- [移动见证再合并：全部元数、全部超临界维数的同一入口](#doc-dfc1a57b3531)
- [临界带的共同形状与整数关系：从局部配方到可比较的结构](#doc-911de441bfd4)
- [全部 2p+2：可逆缩放、三步反射与两次 CRT 返回](#doc-583d4cabdc53)
- [全部内部偶余量的完整证明：有限逆提升、局部循环与尺度](#doc-3e4834660712)
- [全部 3p-1 的统一完成与五平均最优阈值](#doc-2403827e76f3)
- [2p 与 4p 之间：三块运输解掉 3p，并缩小双重值障碍](#doc-90dc128dc488)
- [小参数怎样自然闭合：格指数、退化纤维和真正尚缺的定理](#doc-ce510dd1fb98)
- [分散证明怎样统一：本轮框架审计与实际取得的分支合并](#doc-aa555515ca84)
- [一对边界反射统一整个奇数下半区：端点不再另作启动](#doc-3ccbd6997b58)
- [深核只建一次：有限对应自动群化与不扩环的共同终端](#doc-28bfaf55d663)
- [为什么三平均的精确阈值是七：资源边界、有限周期与合法单轨道](#doc-f496eaf9576b)

---

<a id="doc-a67f17315652"></a>

## 原文导签：素数平均最优最终阈值：总证明与技术依赖

来源：`outputs/prime_arity/proof.md` · [逐字节原样副本](../sources/outputs/prime_arity/proof.md)

**PRIME-TOTAL · 原证明已完成（沿用登记，非本次重审）**

所有奇素数p：N(p)=2p+1，阈值以上G为p幂充要；N(2)=4。原主证明覆盖表完整。

**边界：** 已完成存在性不等于新统一无证书证明或通用高效群词提取。162组是冻结基线，后续独立简化不自动重写它。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-TOTAL`）
<!-- BEGIN SOURCE doc-a67f17315652 -->
# 素数平均最优最终阈值：总证明与技术依赖

2026-09-15整理。本文给出定理、共同机制与无遗漏的覆盖证明；容量公式、局部提升和有限证书留在所链接的技术附录。本文不是对全部旧文的替代，也不声称是一篇自包含论文。

## 1. 定义与主定理

对 x∈Qⁿ，p 平均选择一个 p 元位置集合，以所选均值同时替换其值。每步保总和，故唯一可能的全等终点是原均值。平移与非零共同有理缩放和每步操作交换。因此可研究本原整数零和向量 X；非零时定义
\[
G(X)=\gcd_{i<j}|X_i-X_j|.
\]

**定理。** 对奇素数 p 和任意 n≥2p+1，X 可有限步归零当且仅当 G(X)=pᵉ，e≥0。对 p=2，相同判据在每个 n≥4 成立。奇素数的最终阈值 2p+1 最优；二平均最终阈值为4。

证明分为必要性、上方全部维数的充分性以及下界。后两者不需要下方每个输入的分类。

## 2. 必要性：不能消掉的共同余数

若素数 ℓ|G，则全部 Xᵢ≡c mod ℓ。本原性保证 c≠0。若 ℓ≠p，平均只产生 Z[1/p] 中的数，约化到 Fℓ 后 p 可逆，每步仍保持全体为 c，无法归零。因此 G 只能含 p 因子。

此外 G|n：所有坐标在模 G 下等于 c，本原性给 gcd(c,G)=1，而零和给 nc≡0 mod G。由此 p∤n 时判据恰为 G=1。**在 p|n 的行，不能把这一步的特例当成一般定义。**

## 3. 共同机制：先压缩状态，再消掉有限障碍

### 3.1 合法入口与均值格

在 gcd(p,r)=1 的范围，常用核心是
\[
K_{m,p,r}(a,z)=
\bigl(a^{mp},(-ma+rz)^p,(-pz)^r\bigr),
\qquad n=(m+1)p+r,
\]
其中 m=1 或2。指数是位置重数。零和自动成立，坐标公因子为 gcd(a,z)。本原时，令 y=a+pz，有
\[
G=\gcd(y,n).
\]
证明见[统一核心附录](../sources/outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)，不能把任意三块都未经参数化就套入此式。

入口不是“随机分组直到成功”。[三单点交换子入口](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)先用真实块—单点交换保留全部危险素数处的见证，再用有限环中可由正幂替代的逆迁移见证，最后整理重数。有限模逆在这里用于有限状态控制，不被宣称为有理系统的真实逆。

对上半带，使用其独立的[三值归约](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_three_value_reduction.md)。n=3p+s、1≤s≤9 时，再用**两次实际平均**把 (2p,p,s) 改成 (p,p,p+s)，使两个 p 块可交换。这是[最后九偏移证明](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)共同容量的来源。

### 3.2 真实逆怎样产生

标量周期是决定性资源：若一个真实返回 J 满足 J²=cI，c≠0，则再做同一返回即提供射影逆。这个等式必须在整个所用核心上成立，允许重建相同形状的角色账本。它不是平均投影在全 Qⁿ 上可逆。

两个相邻返回之商常为三角矩阵；其与换块的交换子产生 U(t)，再用横向返回产生另一方向的根。所有单位分母来自这些真实三角倍率及其逆。新增倍率需扩环并重建同一 level 的群控制，不能只记在有限单位表中。

这一环账本已在[九偏移第6节](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)补全：522组中99组的二进补充确有额外单位因子，同一个共轭扩环引理处理它们。

### 3.3 从根到精确终端

设 R=Z[1/D]，D>1，由真实根得到 U(hR)、L(hR)。Morris 与 Serre 的已核对特例，再接任意有限环消元，给
\[
\Gamma(h^2,R)\subseteq\langle U(hR),L(hR)\rangle.
\]
横向根若经非幺模换基取得，必须先计入分母造成的 level 损失。这里真正需要的是某个深主同余群，不必先证明完整 Γ₀。

然后只剩有限问题：把当前本原列的剩余类送到某个终端列的剩余类，允许的缩放只能来自 R 的单位。主同余群对每个**精确本原列剩余类纤维**传递，因而完成有限数据后就能精确到终端。[通用引理](../sources/outputs/prime_arity/arithmetic_toolkit.md)给出完整证明。

若 R 的单位像满射，可以分别处理方向与尺度；若不满射，必须保留二者联合的有限分类。各附录的局部单循环、CRT 和二进证书是在验证这个有限接口，不是另外九套终止哲学。

九偏移现在有更短的实现：已有根及粗略平移的三个共轭在切空间张满，先把深核提升到奇数n的Γ(n,R)或偶数n的Γ(2δn,R)。因此奇数n只需模n的一次线性方向调整；偶数n仅多至多8个二进类。详见[浅层提升](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)，它替代该附录原先的高阶轨道接口，不声称其余区间已逐篇改写。

### 3.4 造零与离散能量收尾

已到达零和 p 元组时，一次平均产生 p 个零。[统一造零收尾](../sources/outputs/prime_arity/tools/prime_arity_interpolation_and_lattice_structure.md)按支持数调用 2p+1 元含零状态的显式五步尾部，以及较早独立完成的 3p、4p 和宽尾部结果。低维段不需要完整端点定理；这些依赖有先后，不能反过来调用待证总定理。

更远处可直接维持两个不同的 p 重值和全部危险素数见证，选择安全非恒等整数平均。能量严格下降且取离散值，故有限终止。这一部分的组合容量由[逆 EGZ 上界](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_inverse_egz_threshold.md)及[尾部补全](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_four_p_tail_completion.md)处理。

## 4. 全部维数的无遗漏覆盖

先单独处理 p=2、3；下表设 p≥5。前三行区间两两不交，覆盖所有 n≥2p+1。

| 范围 | 完成来源 | 需要保留的细节 |
|---|---|---|
| 2p+1≤n≤3p | 下方细分表 | 包含两条偶数边界；3p 保留 p 幂 G 条件 |
| 3p+1≤n≤3p+9 | [大载体共同证明](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md) | [三个共轭根与浅层提升](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)：p≥83 三连参数公式；11≤p<83 的162组反射证书；p=5、7 用各自锐界 |
| n≥3p+10 | [全部素数上方拼接](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_all_prime_three_p_plus_ten.md) | 已包括小 p、4p−2、4p−1 与所有旧 dₚ 缺口 |

下半带写 n=2p+r：

| 参数 | 全输入入口／核心到终端 |
|---|---|
| r=1 | [无条件入口](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)＋[任意 level 端点核心](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md) |
| 奇数 3≤r≤p−2 | 同一入口＋[奇余量核心](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_uniform_odd_middle_cores.md) |
| 偶数 4≤r≤p−3 | 同一入口＋[内部偶余量完成](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md) |
| r=2 | [2p+2 统一双载体与 CRT](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md) |
| r=p−1 | [3p−1 统一重叠证明](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md)，含 p=5 的14元补充 |
| r=p | [3p 三块运输](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md)，本原重数变为 (1,1,1)，控制 level 为3 |

当区间为空时相应行不承担实例。p=5 的锐界在14元补齐后完成；p=7 用[七平均锐界](../sources/outputs/prime_arity/examples/seven_average_sharp_threshold_complete.md)。没有把 p=5、s=5 等 p|n 情形交给仅适用 p∤n 的九偏移主体。

p=3 用[双三重值任意维数证明](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md)覆盖 n≥11，接[7、8元](../sources/outputs/triple_average/proofs/triple_average_seven_eight_complete.md)、9元三幂固定网络及[10元](../sources/outputs/triple_average/proofs/triple_average_ten_complete.md)。二平均沿用已复核的2018年证明，见[二平均来源复核](../sources/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)；4元有两层配对全平均网络。素数总证明不要求用合数位置数归约来补这些小基例。

因此所有 n≥2p+1 均满足充分性。覆盖不是由相邻维数插值所得。

## 5. 为什么阈值不能更低

对奇素数 p，取
\[
X_p=(-p,0^{p-1},1^p)\in\mathbb Z^{2p}.
\]
它本原、零和、G=1，但不可归零。

先说明分数绕路无效。在 n≤2p 时，首次非整数平均产生恰好 p 个相同位置，其 p 进赋值严格低于其他位置。后续操作若部分交叠这 p 个位置，最低赋值再降1，仍由新选中的 p 个相同位置承担；若恰好相同则恒等；若不交叠，只可能 n=2p 且选补集，由零和变成相反的两个 p 块。整体缩放后所有值模2均为1，奇数元平均保持此非零共同余数。因此成功路径不可能首次产生分数。

对 Xₚ 的整数平均，若选 j 份1及 e 份−p，选中和为 j−ep，必须 j=0 或 p。唯一非恒等可能是把 −p 与 p−1 个零平均，得到 (−1ᵖ,1ᵖ)，仍落入模2陷阱。故不可达，N(p)≥2p+1。详见[原下界第8节](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_linear_threshold.md)。

二平均3元取 (−3,1,2)。任意两项的和均非零，故首次平均后必为 (a,a,−2a)，a≠0；后续恒等或变成同形状、参数 −a/2，所以不会归零，而原输入 G=1。与 n≥4 的充分性合并，N(2)=4。

## 6. 证明现在的自然程度与尚未完成的简化

核心到终端已有统一的算术结构：带标记的均值格、真实返回、深同余纤维、有限商。复杂性主要保留在**哪些块形状有足够容量提供这些返回**，以及少数素数处的方向／单位提升。

目前[浅层提升](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)已把九偏移所需反射证书从522组减到162组，并删除奇数n的高阶轨道与主单位逐层计算；入口和基础单位生成不再靠有限证书。尚未证明一套闭式返回计数覆盖全部 p、n，也没有消去剩余162组与两个局部补充；不能将这份整理描述成无计算的统一初等证明。可以进一步统一反射族、消除偶数的二进有限类、整理可执行词编译器；用模形式改写解释层则见[几何说明](../sources/outputs/prime_arity/geometry.md)。

本证明的审核依据分别为[下半带及外部定理](../sources/outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md)、[3p+10专项](../sources/outputs/prime_arity/audits/prime_arity_three_p_plus_ten_audit_20260915.md)、[最终独立审核](../sources/outputs/prime_arity/audits/prime_arity_optimal_threshold_independent_audit_20260915.md)。这些审核支持经扩环补强后的研究证明，不等于形式化认证。

<!-- END SOURCE doc-a67f17315652 -->

---

<a id="doc-9fe4112b0e61"></a>

## 原文导签：本次整理的阅读、修改与核验范围

来源：`outputs/prime_arity/verification.md` · [逐字节原样副本](../sources/outputs/prime_arity/verification.md)

**PRIME-TOTAL · 原证明已完成（沿用登记，非本次重审）**

所有奇素数p：N(p)=2p+1，阈值以上G为p幂充要；N(2)=4。原主证明覆盖表完整。

**边界：** 已完成存在性不等于新统一无证书证明或通用高效群词提取。162组是冻结基线，后续独立简化不自动重写它。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-TOTAL`）

旧核验ID：`prime-final-independent-audit`
<!-- BEGIN SOURCE doc-9fe4112b0e61 -->
# 本次整理的阅读、修改与核验范围

2026-09-15。本页按阶段保留实际阅读和核验记录；当前浅层同余提升见第10节，162组证书是最新版本。前节中的180／522组均指对应历史阶段。文档重组不等于独立重证全部数学。

## 1. 实际阅读的项目文本

以下是正文阅读，不只是文件名检索；“相关节”不表示通读整篇。

| 文档 | 本次读取范围／用途 |
|---|---|
| [最终独立审核](../sources/outputs/prime_arity/audits/prime_arity_optimal_threshold_independent_audit_20260915.md) | 全文；量词、99组额外扩环、两项特殊补充、下界、证书及审核边界 |
| [下半带外部定理审核](../sources/outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md) | 主结论及§§2—5；Morris/Serre前提、任意有限环消元 |
| [3p+10审核](../sources/outputs/prime_arity/audits/prime_arity_three_p_plus_ten_audit_20260915.md) | 上端与尾部拼接、外部依赖和证据说明 |
| [九偏移共同证明](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md) | 入口、四原子反射、§§4—9；容量、换基、扩环、局部方向和尺度 |
| [内部偶余量](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md) | §§1—6；取逆、有限循环、纤维接口及分支范围 |
| [2p+2统一证明](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md) | §§1—4；统一返回、CRT与精确终端 |
| [中间维数结构](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md) | §§1—4；3p的三块运输与固定level |
| [逆EGZ](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_inverse_egz_threshold.md)及[4p尾部](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_four_p_tail_completion.md) | 各§§1—4；旧不等式与已补齐范围 |
| [全部3p+10以上](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_all_prime_three_p_plus_ten.md) | §§8—10及相关接口；小p收口、旧九偏移状态定位 |
| [插值与均值格](../sources/outputs/prime_arity/tools/prime_arity_interpolation_and_lattice_structure.md) | §§1—3、6—7；造零、禁止免费插值、整数格指数 |
| [旧端点几何](../sources/outputs/prime_arity/tools/prime_power_endpoint_and_critical_geometry.md) | §§5—6，并回查相关两图／Schreier段；范数、theta与外部尺度障碍 |
| [Hecke最终审核](../sources/outputs/triple_average/history/triple_average_final_hecke_audit.md) | §§1—8；分支求和、正向实现和符号边界 |
| [无条件入口](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md) | 定理、依赖和§2块—单点交换；其余入口细节此次依照专项审核，未逐式重证 |
| [线性阈值](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_linear_threshold.md) | 不变量与能量结论、§§8—9的2p反例和最低p进赋值论证 |
| [三平均任意维数](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md) | 定理、适用范围与不变量；7—10基例的完整证明未在本次重跑 |
| [二平均与三平均比较](../sources/outputs/literature/binary_vs_ternary_averaging_followup.md) | 结论与共同算术层；2018原证明的完整源文审核沿用既有记录 |
| [合数交接](../sources/outputs/general_arity/general_k_three_tasks_progress_20260915.md) | 当前结果、GRH条件、三项剩余范围，用于保持导航正确；不推进合数证明 |

另直接读取两个原 README 的导航、结论表及历史组织，查看全项目核验注册的相关条目与运行器，并读取最终独立审核脚本及固定证书接口。[此前阅读日志](../sources/outputs/history/research_reading_log_20260915.md)记录其他回合，不能混称本次全部新读。

3p−1、端点一般核心、奇余量核心及部分上半带的细节此次主要通过已读专项审核与被引用接口组织；不声称再次逐行独立审定。总证明链接这些来源，供新读者继续核对。

## 2. 外部文献实际访问层级

| 来源 | 本次访问等级 |
|---|---|
| [Milne v1.31](https://www.jmilne.org/math/CourseNotes/MF.pdf) | 下载PDF并读取相关正文：§2商曲线/cusp，Remark4.8，§5几何Hecke，§8的8.5—8.8，Lemma11.10；不是全书通读 |
| [Stein书目导航](https://wstein.org/books/modform/modform/) | 仅目录网页；另一个 modular_curves 子页404，未用作定理依据 |
| [MIT 18.783课程导航](https://math.mit.edu/classes/18.783/2025/lectures.html) | 仅课程页面，不称为已读讲义 |
| Morris 2007、Prasad–Rapinchuk正式综述、Serre 1970 | 本轮沿用并阅读项目的原文专项审核；未重新通读外部原文，Serre原始全文仍未取得 |
| Kani，二元theta与CM | 继承旧文的题录／摘要层级；未取得或声称读过全文 |

Milne缓存的SHA256：`977f06a4e838c43c77a7c9398c090789e60d67f64e013e1dcd9bcce0e0c27b8d`。[来源元数据](../sources/work/prime_proof_editorial_20260915/milne_modular_forms_source.json)保留URL等信息。

## 3. 本次数学修改和没有作出的声明

- 在九偏移原文§6并入全部二进补充及隔一反射倍率的扩环。以−39/29所需13为具体例子，说明新增分母必须来自真实三角共轭；原level在扩环后重新取得。
- 集中写出标量周期、深主同余、非幺模换基、Smith—CRT取逆及精确纤维引理。
- 把各附录的方向／尺度收尾写成一个有限终端提升定理，并给出 `Um₂(B)/单位像` 的精确轨道分类及缺失尺度的反例。
- 复述已有均值格和权一theta结构，解释Γ₀／Γ₁／Γ的标记层级及局部化的区别；未借模形式证明新的阈值、容量公式或效率界。

最终素数定理仍含原来的完整有限参数证书，也仍依赖已注明的Morris/Serre。本文整理不是外部同行评审或证明助手认证。

## 4. 可重跑的素数核验集

```text
python work/run_verifications.py --profile prime-proof
```

首次整理的 profile 选择素数主线与最终独立证书检查；当前按第10节改为162组浅层提升证书，不包含合数GRH或旧失败路线大搜索。各条purpose和证据边界均在[注册清单](../sources/work/verification_manifest.json)保留。

本轮数学正文改动集中于最终九偏移扩环，因此实际重跑这两项：

```text
python work/run_verifications.py --id nine-offsets-large-symmetric-carrier --id prime-final-independent-audit
```

其余 profile 条目是复现入口，未因重写导航而全部再跑。一般量词来自所引正文；有限公式检查与完整有限参数证书的逻辑地位不同。

本轮执行结果：**PASS=2，FAIL=0，SKIP=0**。原核验器通过522组完整参数和1440组公式／局部提升检查；独立审核通过3540条实际均值记录、521组普通level检查，并识别99组额外扩环，辅助13处完整群为2184元。详见[运行记录](../sources/work/prime_proof_editorial_20260915/verification_run.txt)。

另以精确有理数核对16个矩阵等式实例及两个明确反例接口，记录在[通用公式复核](../sources/work/prime_proof_editorial_20260915/toolkit_identity_checks.json)。这是含非幺模换基的有限抽查；一般恒等式与纤维结论由正文证明，未进行符号库认证。

本目录的路径、锚点、机器依赖图、核验ID、中文编码及归档完整性检查写入[文档检查](../sources/work/prime_proof_editorial_20260915/document_validation.json)。新导航出现的编码问题已修正，归档中的原文内容按原SHA256保留。检查范围不含全体历史链接。

## 5. 文档迁移与维护

首次整理将原根 README 保存在[HISTORY.md](../sources/HISTORY.md)，原 outputs README 及E/H/I路线表现位于[历史路线账本](../sources/outputs/history/research_routes_history_20260915.md)。后续迁移已经修复其中的相对链接；迁移前完整字节另存于原文快照，不能再用首次整理的原文SHA256核对迁移后的链接文本。首次归档记录见[原记录](../sources/work/prime_proof_editorial_20260915/archive_record.json)，最新位置及快照见第6节。

首次整理未批量移动附录；后续已实际迁移220篇，文件名保持不变。[proof_map.json](../sources/outputs/prime_arity/proof_map.json)同步更新了技术来源与证书，不是自动形式化证明。

## 6. 当前文件夹结构与证明简化

后续直接回读九偏移全文、独立核验器的计数／方向／二进补充／辅助13、上半带三值归约与现有结构说明。推导并写出[整数区间与最小缺失单位](../sources/outputs/prime_arity/structure/carrier_interval_and_unit_descent.md)：

- p≥97 的所有反射来自统一闭式整数区间，替代旧 p≥307 的构造分界。
- 11≤p<97 只保留180组反射证书及原来的两项局部修补；其余342组已由一般公式承担。
- 全范围入口改为直接计数；模n基础单位生成改为最小反例下降和固定有理区间覆盖，不再枚举各参数的有限单位群。
- 18组容量不等式接口、15个四单位区间覆盖、180组完整剩余证书、342组旧参数交叉核验及45组较大参数核验均通过。一般量词由正文证明，后两组只是公式对照。

新核验ID为`carrier-interval-reduction`。当前`prime-proof`有18项，改用此项替代旧522组核验；原核验及独立审核保留为可单独执行的历史证据。因为本轮迁移修改了注册与大量引用，已执行整个当前profile：**PASS=18，FAIL=0，SKIP=0，83.39秒**，见[完整运行记录](../sources/work/document_reorganization_20260915/prime_profile_run.txt)。

文件夹地图见[成果索引](../sources/outputs/README.md)。220篇文档实际迁移，各文件夹有索引；[旧新路径表](../sources/work/document_reorganization_20260915/path_map.json)供旧引用定位，[迁移报告](../sources/work/document_reorganization_20260915/migration_report.json)记录范围。原文快照在work/document_reorganization_20260915/originals。全部成果Markdown目标和核验路径检查见[迁移验证](../sources/work/document_reorganization_20260915/validation.json)。HISTORY中一段原有编码损坏按迁移前内容保留，没有猜写数学原文。

未新增外部深定理，未声称模形式替代容量，也未消除剩余180组或一般算法长度问题。合数研究本轮只迁移归类，条件与开放范围保持原文。

## 7. 构造原则的进一步提炼

[整格拼接与正运输](../sources/outputs/prime_arity/structure/integral_gluing_and_positive_transport.md)给出两项直接证明：指定常值方向的整提升条件Bη=cη modN；等大块上有限个保总和／保常值的整数自同构及其逆，在充分大平均元数下均有一层真实运输实现。它统一解释原3p构造，不声称降低任何新阈值或消去180组。

本轮直接阅读章节详列于该文第7节；特别回查旧Reynolds、有向范畴、数字同余群和根格文本，避免把旧术语当成新发现。没有运行参数搜索或重跑未修改的数学核验；两个命题以正文代数和逐位置计数证明。新增导航经过链接检查。

## 8. p进翻译与外部结构核对

[p进局部说明](../sources/outputs/prime_arity/structure/padic_places_and_canonical_branches.md)新增直接推导：pP_S在模p下秩一且平方为零；端点合法及非法有理方向在P¹(Qp)中各自稠密；已证的各层完整循环通过逆极限与ℓ进加一机共轭。没有改变阈值或证书数。

实际取得并阅读Buzzard《Analytic continuation of overconvergent eigenforms》的引言、典范子群定理3.3及迹／U_p命题5.1，Buzzard《Eigenvarieties》引言及§6开头，Buzzard—Gee《Slopes of modular forms》引言前3页。未通读这些全文；Katz／Lubin为前者的明确引用。准确链接、下载哈希与访问边界在专题末节及work/padic_structure_20260915。没有新外部定理作为可达性证明依赖，没有运行参数搜索。

## 9. 二次局部群与原子首位的进一步研究

[局部二次群](../sources/outputs/prime_arity/structure/padic_quadratic_group_and_orbit_defect.md)直接证明：合法分式线性图是群律(x+y)/(1+cxy)；深层形式对数线性化；首层倍映射的赋值d决定高层轨道长度与稳定轨道数。它重证原三进条件，并把坏类分成有限指数缺陷与真实三周期。一般二进迹条件和单位尺度的二进扭点仍分别保留。

新核验`padic-quadratic-group`通过4项符号群律恒等式、36项明确好／坏／扭点轨道实例、5项深度40的快速幂阶检查，以及全部180组保留证书的364个局部正规形，其中二进100处。不搜索平均词，不遍历深层全部状态。无限层分类由正文证明。

[Kneser边界](../sources/outputs/prime_arity/structure/padic_leading_symbols_and_kneser_boundary.md)从原子首位秩一乘法直接推导任意词的交数乘积，解释n=2p与2p+1不交图的连通性突变。没有把首位连通当成完整算术可达性。

同文第3.1节进一步精确计算两次不交平均：pP_TP_S=B_S+B_T+pD_R；在零和空间上的首位秩由n=2p时的1变成n≥2p+1时的2，且端点的完整有理像恰是既有双块—单点核心。这是直接矩阵恒等式，不是有限图样本外推；合法入口仍需已有见证交换。

实际读过：旧局部循环及方向、尺度证明和对应逐位核验程序；Conrad强逼近讲义§1命题1.1及证明；Buzzard主系列讲义§1和§4。Fan—Fan—Liao—Wang的2014分式线性动力系统论文只核对题录、摘要，全文多种公开地址获取失败；未引用其定理。外部来源与尝试记录见work/padic_structure_20260915。Kneser文献只查标准题录，连通性由本文两步构造证明。

当前阈值与180组证书数不变；本轮新增的是结构定理、局部缺陷诊断和首位边界解释，没有再跑未变动的整个18项主线。

## 10. 三个共轭根替代高阶轨道

当前[浅层提升定理](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)把九偏移的控制层降到奇数n的Γ(n,R)，及偶数n的Γ(2δn,R)、δ∈{2,4}。它由三个真实共轭根的切向行列式−b³tr(T)/(det T)²、逐层线性修正和既有精确深核证明；没有用局部闭包替代真实包含。分母清除及扩环后重建均写明。

奇数n的高阶方向循环和主单位提升从证明中删除；偶数n模n以上只需至多8个二进方向和尺度类。三进好轨道条件不再需要，连续三个反射参数已够，统一公式覆盖p≥83，有限反射证书由180减到162。旧辅助13及(13,3)二进补充仍保留。

本轮实际读取：九偏移第5—9节、最新容量区间第3—6节、二次局部群全文的相关规则、原核验器的计数／方向／二进分支。新核验`transverse-root-shallow-lifting`通过符号切向行列式、36项精确逐层修正（包含一个本身为三阶周期的宏）、162组676条根反射记录、387组从83起的三连参数接口及15组单位区间覆盖。没有搜索新平均词或枚举深层轨道。

当前18项profile改用此核验；运行记录为[浅层版核验记录](../sources/work/document_reorganization_20260915/prime_profile_shallow_run.txt)。一般提升和无限参数由正文证明，有限接口重放不替代Morris／Serre。

<!-- END SOURCE doc-9fe4112b0e61 -->

---

<a id="doc-dfc1a57b3531"></a>

## 原文导签：移动见证再合并：全部元数、全部超临界维数的同一入口

来源：`research/prime_arity_padic/move_witnesses_then_merge.md` · [逐字节原样副本](../sources/research/prime_arity_padic/move_witnesses_then_merge.md)

**PRIME-MOVE-MERGE · 本地已给证明，未独立重审**

k≥2、n≥2k+1，完整危险素数见证可保留到两个k重块加剩余单点。

**边界：** 入口完整不等于核心内终止；单载体格障碍仍需不同资源。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-MOVE-MERGE`）
<!-- BEGIN SOURCE doc-dfc1a57b3531 -->
# 移动见证再合并：全部元数、全部超临界维数的同一入口

2026-09-15。设平均元数k≥2，n≥2k+1。本页把旧下半带入口机制写成一个不要求k为素数、不要求k与n互素、也不要求n<3k的定理。它统一入口层，未用作整个可达性的新证明。

## 1. 通用入口定理

令R=Z[1/k]，X∈Rⁿ零和。称X具有完整见证，如果对于每个素数ℓ|n、ℓ∤k，X模ℓ不全相同。非全等有理输入中心化、清分母、本原化后，合法算术判据rad(G)|k恰保证初态有此见证。

**定理。** 对任意k≥2、n=2k+r、r≥1，任意具有完整见证的零和状态，均能通过有限次原位置k平均，在全过程保留完整见证，得到
\[
\boxed{(a^k,b^k,c_1,\ldots,c_r).}
\tag{1.1}
\]
两个k块只是位置组，允许a=b。结论不依赖r奇偶、大小、n因子数以及gcd(k,n)。若危险素数集合为空，见证条件为空条件。

## 2. 建立一个载体只需一次平均

设危险素数集合为P，d=|P|，m=n−k=k+r。选一个基准位置0，并对每个ℓ∈P选一个与它不同余的位置，共保护至多d+1个位置。

有d+1≤m。否则d≥m，n≥2ᵈ≥2ᵐ>2m≥k+m=n，矛盾；这里m≥k+1≥3。故保护集以外至少有k个位置。平均这些位置，就得到一个k块a和m个单点角色c_i，原见证由未参与位置保留。

记δ_i=c_i−a。对于每个危险ℓ，至少一个δ_i非零；又
\[
\sum_{i=1}^m\delta_i=-na\equiv0\pmod\ell.
\tag{2.1}
\]
所以非零差分支持至少含两个角色。这是后续安全性的共同原因。

## 3. 同一真实操作同时包含“移动”和“合并”

选t个单点I与k−t个载体位置，1≤t≤min(k,m)，平均后用t个旧a位置接替选中角色。令s_I=Σ_{i∈I}δ_i，则新差分为
\[
\delta'_j=
\begin{cases}
-s_I/k,&j\in I,\\
\delta_j-s_I/k,&j\notin I.
\end{cases}
\tag{3.1}
\]
这是一次实际k平均，有完整位置账本。

对危险ℓ，因k可逆，(3.1)使所有差分归零当且仅当δ在I外全为0且s_I=0。而(2.1)使后一条件在前者成立时自动满足。故有精确判据
\[
\boxed{\text{完整ℓ见证保留}\iff
\operatorname{supp}(\delta\bmod\ell)\not\subseteq I.}
\tag{3.2}
\]
这里保留的是未本原化的强见证。若全部输出模ℓ为0，再除共同因子可能恢复合法性；本定理不依赖这种可能性。

t=1时支持至少含两个角色，(3.2)自动成立。这些安全、满秩交换负责移动见证。t≥2时映射核是I内总和为0的差分空间，维数t−1，负责合并信息。因此“移动—合并”是同一操作公式的两个秩分支。

## 4. 三角色交换子移动可移动的见证

t=1时
\[
A_i=I+(\lambda\mathbf1-e_i)e_i^T,\qquad\lambda=-1/k.
\]
三个互异角色i,j,j'满足旧恒等式
\[
\boxed{
[A_{j'}^{-1}A_jA_{j'},A_i]
=I+\frac{k-1}{k}(e_{j'}-e_j)e_i^T.}
\tag{4.1}
\]
令M为所有危险素数的乘积。每个A_i来自作用于载体a和角色c_i的同一个2×2交换，在每个Fℓ上可逆。因此可选共同正整数L，使A_i^L≡I modM，对所有角色i成立。(4.1)中的逆由L−1次实际正交换替代，得到模M下准确实现剪切的有限词。

不得把这个正词在Q上的矩阵也认作(4.1)。实际中间操作始终是t=1，所以由(3.2)逐步保留全部见证，无须有理正向逆。

## 5. 不可移动的素数数量由剩余质量控制

定义坏素数B={ℓ∈P:ℓ|k−1}。它们恰使(4.1)的系数归零。而
\[
\gcd(k-1,n)=\gcd(k-1,r+2),
\]
故
\[
\prod_{\ell\in B}\ell\mid r+2,\qquad |B|\le r.
\tag{5.1}
\]
后式对每个r≥1成立：若坏素数至少r+1个，则r+2≥2^{r+1}>r+2，矛盾。

为每个坏素数选一个δ非零的角色，加入J，再补足到|J|=r。固定目标角色j∈J。

若某个好素数ℓ∈P\B在j处没有见证，选δ_i非零的i≠j，并另选j'不同于两者。m≥3，故可选。使用(4.1)，参数t由CRT选成在ℓ处为1、其它好素数处为0。

目标差分变为δ_j−((k−1)/k)tδ_i，因此在ℓ处非零；其余好素数上的目标差分不变。所有坏素数处整个剪切为恒等，放在J内的见证保留。每阶段至少修复一个好素数，至多d−|B|阶段完成。

全过程见证安全由实际t=1操作保证，不依赖形式剪切的中间因子在Q上是否保持选定差分。

## 6. 最后一次合并及全参数覆盖

此时J在每个坏素数处至少保留一个非零差分，目标j在每个好素数处非零，因此J击中所有危险支持。

角色池有m=k+r个位置，I为其补集时恰有k个位置。保留原载体和J，平均I。由(3.2)，全部危险见证保留，得到(1.1)。总共是一次建立载体、有限次同模板见证交换、一次合并。证毕。

当p|n时，p并非危险素数，正应排除在P之外；G可以是p幂，不能错误要求G=1。合数元数也适用，因为唯一用到的是ℓ∤k时1/k有定义。

## 7. 已统一的层与真正剩余

这个定理统一了入口，并给出明确安全规则(3.2)。n=2k时r=0，没有保护角色，最终将全部k个角色合并会包含每个非零差分支持；n=2k+1时首次有一个保护角色，(5.1)又保证至多一个坏素数。这是质量与算术共同出现的临界点。

但进入两块后仍有r个单点。重复本定理只会回到同样形状，不能保证减少自由度；把其中2k+1个位置交给已解端点，其共同尺度也不能自动作用于外部单点。[单载体刚性分析](../sources/research/prime_arity_padic/carrier_balance_and_uniform_mechanism.md)说明仅靠t=1交换不能通过更长词得到通用正向逆。

尚需新内容：保留足够的已知等值关系，选择t≥2，使合并后仍有可继续使用的结构；或让多个载体共同平衡格位移。不能用“安全合并一定存在”代替证明。

这里还需防止一个看似简单的错误：虽然(3.1)在完整角色空间上的核维数为t−1，但一个已经执行过多次操作的词，其当前像空间L可能避开这个核。实际秩下降恰为dim(L∩ker M_I)，不一定是t−1。因此“每次选择t≥2就减少自由度，有限次便结束”不成立。要用秩作终止量，必须实际证明这个交非零，并保持见证；若做不到，不能把维数变化当作自动下降。

本页没有把全范围入口等同于全范围无证书终止。实质是旧证明多个区间共享一条明确入口规则，并删除了不必要的互素和余量上界。

## 8. 来源与独立目录

交换子及原下半带入口来自只读[无条件入口第2—5节](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)。本页重新核对前提，证明对所有k≥2、n≥2k+1的扩展；不宣称交换子本身是新发现，也未沿用m=2时误算剩余位置的草稿。

核验仅在本目录生成，检查多角色公式、见证判据、有限模逆及边界输入。任意k、n的量词由正文证明承担；已有证明和注册清单未修改。

[原位置核验记录](../sources/research/prime_arity_padic/carrier_balance_verification.json)包含144个完整入口实例、其中66个元数与维数不互素、14次实际交换子修复阶段，总计592步原子操作独立重放。其作用是核对实现，并不替代全参数证明。[程序](../sources/research/prime_arity_padic/verify_carrier_balance.py)只用确定的入口规则，没有词搜索。

<!-- END SOURCE doc-dfc1a57b3531 -->

---

<a id="doc-911de441bfd4"></a>

## 原文导签：临界带的共同形状与整数关系：从局部配方到可比较的结构

来源：`research/prime_arity_padic/common_shape_integer_relations_and_mainstream_structure.md` · [逐字节原样副本](../sources/research/prime_arity_padic/common_shape_integer_relations_and_mainstream_structure.md)

**PRIME-COMMON-SHAPE · 本地已给证明，未独立重审**

整个2p<n<4p可进入共同形状；固定来源的迹零输出关系格及有效方向可显式算出。

**边界：** 无界关系格的像不保证容量内可用移动；共同形状不等于全参数终止。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-COMMON-SHAPE`）
<!-- BEGIN SOURCE doc-911de441bfd4 -->
# 临界带的共同形状与整数关系：从局部配方到可比较的结构

2026-09-16。重新阅读2p<n<4p的完整分支后所得。本页有两项具体结论：把九偏移的安全形状转换推广到整个上半带；完整求出固定来源、迹零输出的整数关系格及其对返回矩阵的作用。它们统一入口形状与一类构造的代数来源，尚未给出整个临界带的新终止证明。原完成证明与注册冻结。

## 1. 对照各段后，哪些区别来自问题，哪些来自构造

| 已证分支 | 使用的实际自由度 | 旧分段的直接原因 |
|---|---|---|
| 2p+1端点 | 单载体更新、换块、上下根与小整数单位 | 载体只有一份，标准相邻两反射不齐，但有更强的特定剪切 |
| 奇余量内部 | 两个相邻旧载体对合 | 相邻平方系数互素且奇偶相反，2可反演 |
| 偶余量内部 | 相邻对合、保载体倍率、夹乘激活逆 | 2不能反演，需保留完整整数格与二进尺度 |
| 2p+2 | 新载体反射＋两次按输入选择的CRT数字返回 | 用单向准备直接指定终端尺度，不要求单位群事先满射 |
| 3p−1 | 一次新载体制造＋重叠输出 | 旧不交反射族在容量端点缩短 |
| 3p | 三个等大块的非负整数运输 | 本原重数变成(1,1,1)，控制的均值格模数为3 |
| 上半带内部 | (2p,p,s)的两种载体族 | 两个活动块不等大，缺少免费换块对称 |
| 靠近4p | 重叠返回制造载体 | 原载体计数不足，而重叠重新分配库存 |
| 九偏移 | 改为(p,p,p+s)，再按输出计数取相邻反射 | 历史上为补3p+10以前的缺口选择此形状，并非九种动力学 |

来源与具体阅读章节列在末节。表中“原因”指原证明为何分支，不表示每项分支都是不可消除的数学相变。尤须区别：模2的整性必须被处理，但不必保留原二进轨道表；3p的本原重数变化是真的，但可以用一般带权整格语言容纳。

## 2. 上半带两次平均的转换其实覆盖所有余量

设p≥5为素数、1≤s<p、n=3p+s。已有全输入入口得到
\[
(A^{2p},B^p,C^s),\qquad A=a,\ B=-2a+sz,\ C=-pz.
\]
欲转成两个等大p块及r=p+s份载体，只需选
\[
0\le u\le s,\qquad s\le t+u\le p,\qquad
\gcd(q,n)=1,\quad q=3t+u.
\tag{2.1}
\]
先平均(A^{p−t−u},B^t,C^u)，产生p份D。从剩余旧A中保留r份；它们足够正是t+u≥s。再平均全部其余p份。两次平均覆盖除载体外的原位置，输出为
\[
((a')^p,(rz'-a')^p,(-pz')^r),
\]
其中
\[
\binom{a'}{z'}=\frac1p
\begin{pmatrix}p-q&st-pu\\-1&0\end{pmatrix}\binom az.
\tag{2.2}
\]

**全余量选择规则。**
\[
(t,u)=
\begin{cases}
(s,0),&3\nmid s,\\
((p-u)/3,\ s-3+\rho),&3\mid s,\ \rho=p\bmod3,\ (\rho,s)\ne(1,p-1),\\
((p+1)/2,(p-3)/2),&p\equiv1\pmod3,\ s=p-1.
\end{cases}
\tag{2.3}
\]
第二行先定义u=s−3+ρ，再定义t，避免把它读成隐式方程。

证明：第一行gcd(3s,3p+s)=gcd(3,s)=1，因为p>s且p素；容量直接成立。第二行q=p，且u∈[1,s−1]。条件t+u≥s等价于p−s≥6−2ρ。ρ=2时p−s≥2；ρ=1时p−s≡1 mod3，唯一不满足的值为p−s=1，恰是第三行。第三行t+u=p−1=s、q=2p，而n=4p−1，所以gcd(q,n)=1，全部容量成立。

**安全性。** 记y=a+pz。式(2.2)给
\[
y'=a'+pz'\equiv-\frac qp y\pmod n,
\qquad
\det\begin{pmatrix}p-q&st-pu\\-1&0\end{pmatrix}
=st-pu\equiv-pq\pmod n.
\tag{2.4}
\]
因此在每个ℓ|n处局部可逆，且合法见证仍为单位；清分母／本原化不改变这一点。最终合法又保证两次原子之间不会陷入全体同余。这里不声称转换具有正向逆，只需安全地进入新形状。

旧九偏移入口已经包含(2.3)前两行；本页识别其真实适用范围，并用第三行补齐整族边界。结合旧下半带入口以及3p的独立三块入口，得到：

> 对p≥5和整个2p<n<4p，合法输入都能进入同一物理形状(p,p,r)，r=n−2p。r=p时使用三个p块的正确本原整数格；其余r满足gcd(p,r)=1。

这是共同入口形状定理，不是新的全区间终止证明。旧(2p,p,s)上的控制器不能经单向转换自动变成新形状的控制器；不存在未经证明的逆搬运。

## 3. 固定来源后的全部迹零计数移动

现在用共同核心
\[
K_{p,r}(a,z)=(a^p,(rz-a)^p,(-pz)^r),\qquad n=2p+r,
\quad 1\le r<2p,\ r\ne p.
\]
先平均两个不交且组成相同的来源组c=(i,j,k)，i+j+k=p，产生2p份D，再保留r份D为新载体。令
\[
\alpha=i-j,\qquad \beta=rj-pk.
\]
假设α≠0；交换等大块可使0<α<p，故gcd(α,p)=1。剩余库存为
\[
h=(p-2i,p-2j,r-2k,2p-r).
\tag{3.1}
\]
一个输出o=(x,y,u,v)要满足0≤o≤h、各项和为p；其p元补组再平均，得到实际矩阵p⁻²M(o)，其中
\[
M(o)=\begin{pmatrix}
p(x-y)+\alpha v&pry-p^2u+\beta v\\
-\alpha&-\beta
\end{pmatrix}.
\tag{3.2}
\]
迹零只要求
\[
p(x-y)+\alpha v=\beta.
\tag{3.3}
\]

本节量词只覆盖这一双来源载体更新模板。保留旧载体的两步返回、不同来源的多阶段返回，以及α=0的纯对称配平，不由本节自动分类。第2节统一形状也没有将它们的成功路径全部变成这个模板。

**完整整数核定理。** 对任何两个满足输出总数与迹零条件的整数输出，其差唯一写为
\[
\boxed{\Delta o=h_0b_2+e b_1,\quad h_0,e\in\mathbb Z,}
\]
\[
\boxed{b_1=(-1,-1,2,0),\qquad b_2=(-i,-j,-k,p).}
\tag{3.4}
\]
这里h_0是整数系数，不是库存向量h。

证明：令差为(X,Y,U,V)，则X+Y+U+V=0、p(X−Y)+αV=0。互素性给V=ph_0及X−Y=−αh_0。令e=−Y−jh_0，即得X=−ih_0−e、Y=−jh_0−e、U=−kh_0+2e、V=ph_0，且唯一。证毕。

这正是矩阵
\[
T=\begin{pmatrix}1&1&1&1\\p&-p&0&\alpha\end{pmatrix}
\]
的整数核；其二阶子式的gcd为gcd(p,α)=1，Smith不变因子为1、1。因而在无容量上界时，迹零仿射纤维没有额外整除障碍；不能由此忽略非负库存。

### 3.1 两种移动有不同的数学作用

b₂把一份来源组合(i,j,k)替换为p份D。由pD=iA+jB+kC，它的均值效果完全为零：
\[
M(o+b_2)=M(o).
\tag{3.5}
\]
b₁才是有效方向：
\[
M(o+b_1)=M(o)-pnE_{12}.
\tag{3.6}
\]
因此全部固定来源的迹零返回，去掉不改变作用的重新分组后，恰是一条仿射整数直线，而不是任意二维矩阵空间。

写M(o)=(β,Q;−α,−β)，则由Cayley–Hamilton
\[
M(o)^2=(\beta^2-\alpha Q)I=p f I.
\]
pf被p整除由(3.3)立即得出，且
\[
\boxed{f(o+b_1)-f(o)=\alpha n.}
\tag{3.7}
\]
这解释九偏移及载体更新文稿中的相邻返回倍率为何总有等差结构。不是为每个参数猜一个周期；先求关系格，迹零使它成为反射，唯一有效计数方向控制平方标量。

安全性也统一。由来源总数得β=nj+pα−p²；由输出总数与迹零条件得
\[
Q=-p^3+p\beta+n(py+jv).
\]
令C=(0,1;1,p)把(a,z)改为(z,y_*)=(z,a+pz)，直接相乘得到
\[
CMC^{-1}=\begin{pmatrix}
p^2-nj&-\alpha\\
n[p(y-j)+jv]&-p^2+nj
\end{pmatrix}.
\]
因此
\[
\boxed{\beta^2-\alpha Q\equiv p^4\pmod n,\qquad
p^{-2}CMC^{-1}\equiv
\begin{pmatrix}1&-\alpha/p^2\\0&-1\end{pmatrix}\pmod n.}
\tag{3.8}
\]
由于gcd(p,n)=1，平方标量非零且在所有ℓ|n处是单位；真实返回将见证y_*变为−y_*模n，故保留合法性。重复返回取得共同非零标量，提供真逆。此结论针对容量确实成立的表，不证明任何给定来源有可行输出。

### 3.2 容量截面是至多两个整数区间

取v₀为α⁻¹β modp在[0,p−1]的代表，令d₀=(β−αv₀)/p，选一个整数特解
\[
o_0=(d_0,0,p-v_0-d_0,v_0).
\]
所有整数输出为o=o₀+h₀b₂+eb₁。因0≤v≤2p−r<2p，只可能h₀=0、1；r>p时至多h₀=0。

固定h₀，记a=o₀+h₀b₂，则可行整数e恰满足
\[
\max\{a_1-h_1,a_2-h_2,\lceil-a_3/2\rceil\}
\le e\le
\min\{a_1,a_2,\lfloor(h_3-a_3)/2\rfloor\},
\tag{3.9}
\]
并检查0≤a₄≤h₄。因此固定来源不需要枚举四维输出计数：精确消元后至多两个区间。这里不声称两区间投影一定相接，也不声称区间长度总够供应根或横向作用。

## 4. 与主流整数规划的精确连接及边界

固定来源后，可行反射输出就是标准的有界整数纤维
\[
\mathcal F=\{o\in\mathbb Z^4:To=(p,\beta)^T,\ 0\le o\le h\}.
\]
Graver基由整数核中同号偏序下极小的非零向量构成。若o,o'同属F，差o'−o能分解为同号Graver向量之和。任意部分和都逐坐标夹在o和o'之间，故全部仍满足库存上下界和同一线性约束。这个论证证明有界纤维的连接，不依赖本项目特殊参数。

本次实际阅读Chen–Koutecký–Xu–Shi的ESA 2020论文第33:6页定义8和同号分解性质；[原文](https://doi.org/10.4230/LIPIcs.ESA.2020.33)。所需分解也可直接归纳证明：若非零核向量不是同号极小，就减去一个更小同号核向量，整数l₁范数下降，有限步完成。有限性来自Dickson引理在各正交象限的应用。

但(3.4)的一组格基不必就是Graver基。任意格基的正负移动可能暂时越过库存边界；不能把“张满整数核”直接等同于“在非负计数内连通”。标准Markov基首先对应固定线性统计量的非负纤维；有上界时须保留补计数，或使用上述同号分解。

更重要的是：这里的连通性连接的是**两张备选操作表**。它不是从W(o)X直接对数值执行计数移动。若一张表已有真实射影逆，才可用W(o')W(o)⁻¹把比较转成实际作用。没有逆时，不能把Graver边视为免费物理步骤。

因此可借用的成熟理论是准确的，却只处理“纤维非空以后如何系统比较”。它不证明纤维非空、有效方向非零、两个横向来源存在或根理想足够。这些必须另证。

### 4.1 一个整族单点纤维，说明连通性本身不够

取所有奇素数p≥5、r=2p−1、来源c=(1,0,p−1)。库存为(p−2,p,1,1)，且α=1、β=−p(p−1)。迹零模p迫使v=0，再由x−y=−(p−1)与输出总数得唯一解
\[
\boxed{o=(0,p-1,1,0).}
\]
这个唯一反射满足
\[
M^2=p(p^3-4p^2+5p-1)I\ne0.
\]
所以有可逆返回，但计数纤维中无第二张表；任何连通定理均无法在此凭空产生相邻倍率。它只排除这个来源，不能排除其他来源或多阶段重建。上一轮在n=(7p+1)/2处的守恒模板障碍则进一步说明：某些参数确实需要放开构造类型。

## 5. 算术群、局部几何和模形式各自处在什么位置

已有[整格拼接](../sources/outputs/prime_arity/structure/integral_gluing_and_positive_transport.md)给出本原重数w下的典范数据
\[
H_w=\ker(w^T:\mathbb Z^3\to\mathbb Z),\quad
N=\sum w_i,\quad
\mathbb Z^3/(H_w+\mathbb Z\mathbf1)\simeq\mathbb Z/N\mathbb Z.
\]
指定常值方向造成的有限标记，解释Γ₀／Γ₁型稳定子、单位尺度以及深同余纤维。对(p,p,r)、r≠p，N=n；对(p,p,p)，先本原化w=(1,1,1)，所以N=3。这是真正跨越各段的整格结构。N是这个指定常值方向的拼接指数，不应不加证明就称为任意能量格的完整判别群。

在已取得可逆返回后，ℓ进群及Bruhat–Tits几何能解释局部整格移动；根是unipotent作用，有限列修正是其线性化。已证的二进列提升实际利用了这一层。原子平均却是奇异投影，不能一开始便全看作建筑上的可逆边。

模曲线／模形式确实自然附着于这些同余子群，但它们研究的轨道商、函数或Hecke对应通常不包含(3.1)的位置库存，也不记录一个有理矩阵是否来自有限正向词。仅把群识别成Γ₀，不会替代第3、4节的非负整数存在性。本次没有找到可以直接取消这一步的模形式定理。

比强求完整群包含更值得复用的另一结构，是2p+2证明的两次CRT准备：它在有限模数处把当前本原列直接送到目标尺度，不要求所有安全数字都先成为可逆生成元。其主流对应是PID上的本原列补全、半局部环的单位准备与CRT。跨段推广应问哪些真实数字返回能做到这种列准备，而不是预先要求每段都生成最大的同余群。

## 6. 对下一步的具体影响

本次确实消除了一项入口形状的差异；没有消除全部终止分支。下一步可在共同(p,p,r)上比较两类完整接口：

1. 具有两个可行有效输出的来源：用(3.4)—(3.9)直接计算相邻倍率与根，不再猜输出模板；证明何时这些来源提供足够横向参数。
2. 有效纤维不足的来源或边界：使用旧成功证明中的重叠、来源改变或状态相关数字准备，证明它们实际跨过缺失方向；不能用同一纤维的连通性掩盖空集／单点问题。

一个足以称为整体推进的后续结果，仍须接成对整个r范围统一量化的核内终端定理，并与第2节共同入口相接。Graver基、反射直线和均值格已经给出三个可精确比较的对象，但不是三个尚待证明公理的新名称。

## 7. 阅读、文献与核验

本次回读：端点同余闭合第2—6节；奇余量核心第2—6节；偶余量完成第2—7节；2p+2第2—7节；3p−1第2—9节；3p运输第2—4节；上半带三值入口第1—3节、四返回第2—4节、完整收尾的辅助因子与单位部分、重叠返回第2节、九偏移第2—5节及计数区间改进；同时对照本目录全偶载体闭路、正常形、守恒交换与整族模板障碍。没有重新审定所有附录或每条程序记录。

文献访问及实际阅读范围见[文献记录](../sources/research/prime_arity_padic/literature_integer_moves/README.md)。Diaconis–Sturmfels 1998的题录与DOI已核对，但全文访问受阻；Onn专著只核对题录。ESA 2020正文已取得并阅读相关基础段落。本次不声称穷尽所有最新文献。

[核验器](../sources/research/prime_arity_padic/verify_common_shape_and_relation_lattice.py)对显式形状转换作21,438组公式检查及1,584次原子重放；对992个小来源纤维，将格参数化和直接有界计数逐项比较，共866个可行输出、449次相邻平方差核对；另检查93个单点边界实例。它没有搜索平均词；小纤维枚举只核对手写参数化，不承担无限量词。结果见[记录](../sources/research/prime_arity_padic/common_shape_relation_lattice_verification.json)。原256份冻结文件保持不变。

<!-- END SOURCE doc-911de441bfd4 -->

---

<a id="doc-583d4cabdc53"></a>

## 原文导签：全部 2p+2：可逆缩放、三步反射与两次 CRT 返回

来源：`outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md` · [逐字节原样副本](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md)

**PRIME-2P2 · 原证明已完成（沿用登记，非本次重审）**

全部素数p≥5、n=2p+2的完整G=1判据；无需omega(p+1)限制。

**边界：** 原文的“上方九偏移仍未解”是历史状态；本边界已完整，但不等于内部偶数启动已经同构。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-2P2`）

旧核验ID：`two-p-plus-two-uniform`
<!-- BEGIN SOURCE doc-583d4cabdc53 -->
# 全部 2p+2：可逆缩放、三步反射与两次 CRT 返回

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../sources/outputs/prime_arity/README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

日期：2026-09-15。p 表示平均元数，n 表示原位置数。

## 1. 完整定理

**定理。** 对每个素数 p>=5，n=2p+2 的任意非全等有理输入，经有限次原位置 p 平均可达全等，当且仅当本原中心化差分 gcd 为 G=1。

没有 omega(p+1)<=2 或其他素因子条件。结合[全部3p-1](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md)、全部奇余量和内部偶余量，得到
\[
\boxed{
p\ge5\text{ 为素数},\quad2p<n\le3p
\ \Longrightarrow\ \text{完整可达性判据成立}.
}
\]
n<3p时判据为G=1；n=3p沿用其G为p幂的完整判据。特别不能在n=3p错误地要求G只能为1。

当前任意素数最优阈值仍未证明。3p以上的九种偏移3p+1至3p+9仍未统一完成，故一般最终上界仍为N(p)<=3p+10。

本文使用 Morris 2007 定理6.1(2)、Serre 强同余子群性质及既有深同余引理。外部来源和原文访问边界沿用[深同余证明](../sources/outputs/prime_arity/history/prime_arity_even_middle_congruence_and_eighteen.md)。一般量词由下述原位置恒等式和CRT证明承担，不由有限输入测试外推。

## 2. 已有入口、平移和数字返回

置m=p+1。无条件下半带入口给出
\[
D(u,v)=((u+v)^p,(u-v)^p,(-pu)^2),
\quad \gcd(u,v)=\gcd(v,m)=1.
\tag{2.1}
\]
因此v为奇数。共同本原化仅用于分析，不是额外数值操作。

以下两种真实两原子返回见[统一文稿第11节](../sources/outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)。

首先，每个整数k的上平移
\[
U(k):(u,v)\longmapsto(u+kv,v)
\tag{2.2}
\]
均可正向执行，且逆也如此。基本U(1)的实际尺度为-1/p；交换两个p块的角色给U(-1)。

其次，对每个2<=q<=p，平均两个不交组
\[
(A^{q-2},B^{p-q},C^2),\qquad
(A^{p-q},B^q),
\]
留下两份旧A作载体，给出实际矩阵p^-1乘
\[
M_q=\begin{pmatrix}-1&-1\\-m&2q-m\end{pmatrix}.
\tag{2.3}
\]
M_q并非在所有本原状态上都合法。下面每次使用时都先选择U平移，并严格证明输出本原及合法；不把它当作免费可逆群元。

## 3. 四次平均给保载体缩放的正向逆

两个p块作互补配比，各取(p+1)/2份一种值、(p-1)/2份另一种值，载体不动，得到
\[
F:(u,v)\longmapsto(u,v/p).
\tag{3.1}
\]

其逆有一个全局原位置构造。先分别平均
\[
(A^{(p-1)/2},B^{(p-1)/2},C),
\]
使用两个不同的C位置和互不相交的旧块位置，产生2p份同值
\[
D=-u/p.
\]
旧A、B各剩一份。从新D保留两份作最终载体，再分别平均一份旧A或旧B与p-1份D，得到
\[
(u,v)\longmapsto(u/p^2,v/p)
=\frac1{p^2}F^{-1}(u,v).
\tag{3.2}
\]
这四次平均覆盖原位置，并共同缩放载体；没有留下未跟随的外部坐标。

因此F与F^{-1}均正向可执行。通过它们对(2.2)的共轭，已有
\[
\boxed{U(\mathbb Z[1/p]).}
\tag{3.3}
\]

## 4. 一个统一的三步反射

令t=(p-3)/2。先平均
\[
(A^{(p+1)/2},B^t,C),
\]
产生p份
\[
D=(-u+2v)/p.
\]
保留其中两份作最终载体，余下旧A、B、C、新D的数量分别为
\[
(p-1)/2,\quad(p+3)/2,\quad1,\quad p-2.
\]

令w=(p-1)/2，并定义
\[
b=\begin{cases}1,&p=1\pmod4,\\0,&p=3\pmod4,\end{cases}
\quad
x=(p-b-w)/2,\quad y=x+1,\quad z=w-1.
\]
平均一个p元组(A^x,B^y,C^b,D^z)，再平均剩余的p份。这里是**一个输出组及其补组**，不能误写成两个重复组再加第三组。

计数对全部p>=5成立：若p=4k+1，(x,y,b,z)=(k,k+1,1,2k-1)；若p=4k+3，(x,y,b,z)=(k+1,k+2,0,2k)。均在上述实际重数内。

所得实际矩阵为p^-2乘
\[
J=\begin{pmatrix}1&-2\\c&-1\end{pmatrix},
\quad
c=\begin{cases}
-(p^2-1)/2,&p=1\pmod4,\\
(p+1)^2/2,&p=3\pmod4.
\end{cases}
\tag{4.1}
\]
于是
\[
J^2=(1-2c)I,\qquad
1-2c=
\begin{cases}p^2,&p=1\pmod4,\\-p(p+2),&p=3\pmod4.\end{cases}
\]
平方标量非零，故J的逆也正向可执行。c被m整除，且平方标量与m互素，所以整个返回保持合法性。

自由角色交换为S=diag(1,-1)。令H=J U(2)，则
\[
H=\begin{pmatrix}1&0\\c&2c-1\end{pmatrix},
\qquad
\boxed{[S,H]=L(-2c).}
\tag{4.2}
\]
由F的正逆共轭，得到L(2c Z[1/p])。置
\[
h=|2c|=
\begin{cases}p^2-1,&p=1\pmod4,\\m^2,&p=3\pmod4,\end{cases}
\quad R=\mathbb Z[1/p],\quad Q=h^2.
\tag{4.3}
\]
已有U(hR)、L(hR)，故深同余引理给
\[
\boxed{\Gamma(Q,R)\text{ 正向可执行}.}
\tag{4.4}
\]
m整除h、gcd(p,h)=1。第一种情况的Q可以包含p-1的额外素因子；下面直接处理它们，不再逐个局部化消除。

## 5. 一次 M_p 把v变成整个控制层的单位

从本原(u,v)出发，先以U平移选择某个整数a，使
\[
2a=u\pmod v.
\tag{5.1}
\]
这等价于把u调整为u_*=2a-v。因为v奇，u_*也奇。随后(2.3)的q=p返回给
\[
\frac1pM_p(u_*,v)^T
=\frac2p(-a,\ pv-ma)^T.
\tag{5.2}
\]
我们可以选a，使这个整数分析列本原，且第二坐标在模Q下可逆。

具体地，(5.1)保证gcd(a,v)=1。对每个ell|Q：

- 若ell|m，原v为单位，而pv-ma=pv mod ell，始终非零。
- 若ell|v，由原条件知ell不整除m；(5.1)使a非零，所以pv-ma=-ma非零。
- 其余ell处，m、v都可逆，可指定a=(pv-1)/m mod ell，使新第二坐标等于1。

这些额外同余的素数都不除v，故与(5.1)由CRT同时满足。此外若p不整除v，另指定a=1 modp；若p|v，则(5.1)已保证p不整除a。因为p不整除Q，该条件也相容。

于是令
\[
(u_1,v_1)=(-a,pv-ma),
\]
有
\[
\boxed{\gcd(u_1,v_1)=1,\quad\gcd(v_1,Q)=1.}
\tag{5.3}
\]
本原性来自gcd(a,pv-ma)=gcd(a,p)=1。因m|Q，输出仍合法。完整返回的输出合法，也保证各原子不会在途中进入不可消除的非零共同余类。

这一阶段没有使某个能量必然下降，也不需要；它直接完成局部单位准备。

## 6. 第二次 M_q 同时设定全部终端尺度

取v_1在模m下的逆元q_0，1<=q_0<=p。它为奇数。若q_0>=2，令(q,epsilon)=(q_0,1)；若q_0=1，则令(q,epsilon)=(p,-1)。因p=-1模m，总有
\[
2\le q\le p,\quad q\text{ 奇},\quad
qv_1=\epsilon\pmod m,\quad\epsilon\in\{1,-1\}.
\tag{6.1}
\]
这明确避开不可实现的数字q=1。

置K=Q/m。因v_1与Q互素，CRT可以选择整数b，使
\[
2b=u_1\pmod{v_1},\qquad
b=\frac{qv_1-\epsilon}{m}\pmod K.
\tag{6.2}
\]
右侧为整数，两个模数互素。还可使gcd(b,q)=1：

若ell|q同时整除v_1，第一条同余已经迫使b非零；若ell|q同时整除K，因q与m互素，第二条同余给mb=-epsilon mod ell，也迫使b非零。其余ell|q不除两个模数，可再用CRT令b=1 mod ell。

先以U平移使第一坐标为2b-v_1，再执行M_q。输出的本原整数分析列恰为
\[
(u_2,v_2)=(-b,qv_1-mb),
\quad
\boxed{v_2=\epsilon\pmod Q.}
\tag{6.3}
\]
因为gcd(b,v_1)=gcd(b,q)=1，坐标gcd严格为1，不会在本原化中破坏已经安排好的尺度。

这一步不要求R单位模Q满射，也不要求q在R中预先可逆。它是根据输入选取的真实正向返回，直接把尺度设为R单位epsilon=±1。

## 7. 精确终端与全输入

用U(k)使u_3=u_2+kv_2=0 modQ。仍有gcd(u_3,v_2)=1。取alpha u_3+beta v_2=1，并调整(alpha,beta)使alpha=0 modQ。则
\[
P=\begin{pmatrix}
v_2/\epsilon&-u_3/\epsilon\\
\epsilon\alpha&\epsilon\beta
\end{pmatrix}\in\Gamma(Q,\mathbb Z),
\qquad P(u_3,v_2)^T=(0,\epsilon)^T.
\]
由(4.4)，P有原位置正向实现。最终状态是非零共同尺度乘
\[
(\epsilon^p,(-\epsilon)^p,0^2),
\]
三次相反值消去即可全零。

无条件入口已给全部合法原输入；必要性为原G不变量。因此定理完整成立，没有剩下“原位置分解”或“有限尺度类”的额外假设。

## 8. 与旧下降证明的关系及核验

旧证明在omega(p+1)<=2时，以最近奇数和一次除二修复保证整数高度逐轮下降。一般多奇素因子可能交替阻断那个规则。本文保留真实数字返回M_q，却改变了用途：利用已经建立的深主同余层，用两次CRT准备直接指定最终同余类，不再要求每轮变小。

此前失败的三步返回草稿混用了上半带的两个重复行和下半带的一个输出行，已删除。本文第4节及核验只使用正确的(p,p,2)位置账本。旧低维或短词菜单的失败也不构成本定理的反例。

[核验程序](../sources/work/verify_two_p_plus_two_uniform.py)检查：

- p<1000的166组反射与根恒等式；
- 80条原位置三步反射及保载体缩放的全局逆闭路；
- 1992组M_p/M_q的CRT准备和精确整数主同余终端矩阵；
- p<=31的两个状态相关返回均逐原位置重放；另显式包含旧p=29、(u,v)=(4,7)的一轮下降障碍。

该程序不搜索平均词，不枚举有限群，不由有限高度样本推断一般定理。主同余群的一般词提取和多项式长度仍未给出。

核验入口：python work/run_verifications.py --id two-p-plus-two-uniform。


<!-- END SOURCE doc-583d4cabdc53 -->

---

<a id="doc-3e4834660712"></a>

## 原文导签：全部内部偶余量的完整证明：有限逆提升、局部循环与尺度

来源：`outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md` · [逐字节原样副本](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md)

**PRIME-EVEN-INTERIOR · 原证明已完成（沿用登记，非本次重审）**

全部p≥7、偶数4≤r≤p−3，n=2p+r全输入G=1充要。

**边界：** 不承担r=2及r=p−1；这两条边界有独立完整卡。旧二进表可由PRIME-DYADIC替代，不等于启动全部统一。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-EVEN-INTERIOR`）

旧核验ID：`even-interior-completion`
<!-- BEGIN SOURCE doc-3e4834660712 -->
# 全部内部偶余量的完整证明：有限逆提升、局部循环与尺度

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../sources/outputs/prime_arity/README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

日期：2026-09-15。

## 1. 定理与剩余边界

**定理。** 设 \(p\ge7\) 为奇素数，\(r\) 为偶数，且
\[
\boxed{4\le r\le p-3,\qquad n=2p+r.}\tag{1}
\]
任意非全等有理 \(n\) 元输入，经中心化、清分母和本原化得到 \(X\)。则在原 \(n\) 个位置上有限 \(p\) 平均可达，当且仅当 \(G(X)=1\)。

因此，接已有端点、全部奇余量和 \(3p\) 定理，区间 \(2p<n\le3p\) 对任意素数 \(p\) 只剩两个可能未完成的维数：
\[
\boxed{n=2p+2,\qquad n=3p-1.}\tag{2}
\]
其中前者在 \(\omega(p+1)\le2\) 时已经完成；小素数还有已证特例。本文没有完成这两个边界的一般情形，也不推出最终阈值 \(N(p)\le3p\)，因为上半带仍有任务。

新证明使用[无条件入口](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)；核心内以已有深主同余子群为基础，把有限模上的逆提升为真实射影逆。再分别控制方向和单位尺度，最后用主同余纤维定理精确到达终端。

外部依赖仍为已在[深同余引理](../sources/outputs/prime_arity/history/prime_arity_even_middle_congruence_and_eighteen.md)列明的 Morris 2007 定理6.1(2)及 Serre 的有理 \(S\) 整数强同余子群性质。Serre原文全文尚未取得；本文不声称这些外部结论由程序验证。

## 2. 坐标、真实返回与已有深同余控制

写 \(r=2t\)、\(m=p+t\)、\(n=2m\)。核心采用整数幺模坐标
\[
\mathcal D_{p,t}(u,v)=((tu+v)^p,(tu-v)^p,(-pu)^{2t}),
\quad a=tu+v,\ z=u.
\]
本原性为 \(\gcd(u,v)=1\)，差分 gcd 为
\[
G=\gcd(2v,mu+v).
\]
因此合法性恰为
\[
\begin{cases}
\gcd(v,m)=1,&t\text{ 奇，此时 }m\text{ 偶},\\
\gcd(v,m)=1,\quad u+v\text{ 奇},&t\text{ 偶，此时 }m\text{ 奇}.
\end{cases}\tag{3}
\]

对每个可行奇数 \(s\)，已有两次原位置平均的对合。其参数范围及矩阵为
\[
\max(1,4t-p)\le s\le2t,\qquad
J_s=\begin{pmatrix}-t&-1\\m(t-s)&t\end{pmatrix},
\]
\[
d_s=pt-ms,\qquad J_s^2=-d_sI,\qquad \gcd(d_s,n)=1.
\tag{4}
\]
实际矩阵是 \(J_s/p\)。分组为
\[
(A^i,B^i,C^s),\quad(A^{p-r-i},B^{p-i},C^{r-s}),\quad
i=(p-s)/2,
\]
并留下 \(r\) 份旧 \(A\) 作新载体。换块在 \((u,v)\) 中是 \(S=\operatorname{diag}(1,-1)\)，在 \((a,z)\) 中是
\(\Sigma=(-1,r;0,1)\)。

内部范围总有 \(s_0=r-1,s_1=r-3\)。设 \(d=d_{s_0}\)、\(e=d+n\)，则 \(d,e\) 互素、奇数且与 \(n\) 互素。原来的对角倍率与根公式，在
\[
R_0=\mathbb Z[1/|de|],\qquad h=rn
\]
上给出 \(U(hR_0),L(hR_0)\)，并由深同余引理得到
\[
\Gamma(h^2,R_0).\tag{5}
\]
这里根公式首先在 \((a,z)\) 坐标成立；主同余子群在整数幺模换元下保持同一个 level。

若还有第三个返回 \(s_2=r-5\)，则可以把 \(R_0\) 扩为
\(\mathbb Z[1/|d(d+n)(d+2n)|]\)。两个对角倍率的正负幂和根参数相加给出同一根公式；三个奇数两两互素。

## 3. 从有限逆提升到真实逆

**有限逆提升引理。** 假设在全系统核心上已正向实现 \(\Gamma(Q,R)\)，且一个正向返回的射影矩阵 \(Z\) 属于 \(\mathrm{SL}_2(R)\)。则 \(Z^{-1}\) 也可正向实现。

证明：\(R/QR\) 有限，故某个 \(k>0\) 使 \(Z^k\in\Gamma(Q,R)\)。于是
\[
Z^{-1}=Z^{k-1}(Z^k)^{-1}.
\]
右端全部已正向可执行。这里主同余子群提供真正的有理逆，不能省去这个前提。

### 3.1 保载体倍率

两次互补平均保留全部载体，给
\[
F_c:(u,v)\mapsto(u,cv/p),\qquad c\text{ 奇},\quad |c|\le p.
\]
\(F_1\) 始终合法，其整数射影矩阵为 \(\operatorname{diag}(p,1)\)。因为 \(p\) 与 (5) 的 level 互素，已有矩阵夹乘引理给 \(F_1^{-1}\) 的正向实现。故
\[
C_c=F_cF_1^{-1}=\operatorname{diag}(1,c)\tag{6}
\]
正向可执行。若 \(c\) 为奇数且与 \(n\) 互素，它保持 (3)。

一个直接的夹乘证明如下：若 \(D=\operatorname{diag}(1,c)\)、\(\gcd(c,Q)=1\)，选择 \(g\in\Gamma(Q,\mathbb Z)\)，使 \(g_{11}\equiv0\pmod c\)。可由模 \(c\) 的旋转矩阵和模 \(Q\) 的恒等矩阵，用CRT及整数初等矩阵提升得到。则 \(H=DgD/c\) 是正向可实现的整数 \(\mathrm{SL}_2\) 矩阵。有限逆提升给 \(H^{-1}\)，而 \(gDH^{-1}=cD^{-1}\) 给所需射影逆。

### 3.2 反演 \(t\) 的全部奇因子

设奇数 \(c\mid t\)。它可能整除原 level，不能直接套用上一段的互素条件。但取 (4) 中的 \(J=J_{s_0}\)，有
\[
H=\frac1c C_cJC_c
=\begin{pmatrix}-t/c&-1\\m(t-s_0)&tc\end{pmatrix}.
\]
\(\det H=\det J=d\) 是 \(R_0\) 单位。因此 \(Z=HJ^{-1}\in\mathrm{SL}_2(R_0)\)，且其射影作用正向可实现。有限逆提升先给 \(Z^{-1}\)，再给 \(H^{-1}\)。恒等式
\[
JC_cH^{-1}=cC_c^{-1}\tag{7}
\]
于是给出 \(C_c^{-1}\)。

这没有在物理上除以 \(c\)：\(H\) 只是完整返回的非零共同尺度规范化。所有 \(n\) 个位置都在同一个核心内。

记 \(t=2^a t_0\)，\(t_0\) 奇。现在可反演倍率 \(p,t_0\)。在 \((a,z)\) 坐标中 \(C_c\) 是上三角矩阵
\[
\begin{pmatrix}c&t(1-c)\\0&1\end{pmatrix};
\]
共轭原上根使参数乘 \(c\)，再用 \(J\) 把上根转成下根。因此，令
\[
R=R_0[1/(pt_0)],\qquad Q=(2^{a+2}m)^2,
\]
可重新应用深同余引理，得到
\[
\boxed{\Gamma(Q,R)\text{ 正向可执行}.}\tag{8}
\]
原 \(r\) 中的奇素数都已局部化；\(Q\) 只含 \(n\) 的素因子。后续任何 \(|c|\le p\) 的奇数、\(\gcd(c,n)=1\)，均可通过 (6) 及互素夹乘反演并加入 \(R\)。同样的根共轭保持 (8) 的 level。

## 4. 射影循环与精确纤维提升

取一个可行 \(s\)，令
\[
G_s=-SJ_s=\begin{pmatrix}t&1\\m(t-s)&t\end{pmatrix},
\quad c_s=\frac{m(t-s)}{t^2}.
\]
其射影作用正向可执行。对奇素数 \(\ell\mid m\)，在 \(x=u/v\) 坐标中，它模 \(\ell\) 是
\[
x\mapsto x+1/t.
\]
若 \(3\mid m\)，选择 \(s\) 避免 \(c_s\equiv-3\pmod9\)。两个相邻的可行奇数 \(s,s-2\) 保证至少一个可用：当 \(v_3(m)=1\) 时，两者的 \(c_s/3\) 模3不同；更深时均不退化。

**局部循环引理。** 对这样的 \(s\)，该射影作用在每个 \(\mathbb Z/\ell^b\mathbb Z\) 上形成一个完整循环。若 \(t\) 奇，则在所有 \(2^b\) 上也成立。

证明：在对应局部环中写
\[
G_s/t=I+N,\qquad N^2=c_s I.
\]
\(\ell\ge5\) 时，二项式展开给 \((I+N)^\ell=A I+B N\)，其中 \(A\) 为单位、\(v_\ell(B)=1\)。\(\ell=3\) 时 \(B=3+c_s\)，所选条件正保证其赋值为1。若 \(t\) 奇，则 \(m\) 偶且 \(c_s\) 偶；在2处 \((I+N)^2=(1+c_s)I+2N\)，也有单位对角项和精确的一阶非对角项。

重复取 \(\ell\) 次幂得到 \(G_s^{\ell^j}\) 的射影非对角系数赋值恰为 \(j\)。对任意 \(x\)，其位移还乘一个单位 \(1-t^2c_sx^2\)。因此 \(G_s^k\) 固定 \(x\bmod\ell^b\) 当且仅当 \(\ell^b\mid k\)，轨道长度正好 \(\ell^b\)。证毕。

不同奇素数的循环长度互素，CRT能同时选择同一个正向幂。指数可逐素数幂提升求出，不搜索平均词。

**精确纤维引理。** 若 \(x,y\) 是 \(R^2\) 中本原列，且 \(x\equiv y\pmod{QR^2}\)，则存在 \(H\in\Gamma(Q,R)\) 使 \(Hx=y\)。证明是把两列补成行列式一矩阵，并调整第二列使两个矩阵模 \(Q\) 相同。对 \(x\equiv\epsilon y\)、\(\epsilon\in R^\times\) 同样适用。

下面每一分支均同时证明方向相等和尺度属于真实 \(R\) 单位，最后才调用这个引理。仅有普通射影方向相同是不够的。

## 5. \(t\) 奇：全部 \(r\equiv2\pmod4\) 的内部核心

此时 \(t\ge3\)、\(m\) 偶，\(t\) 已由第3节完全局部化。取 \(Q=(4m)^2\)。合法性使 \(v\) 为模 \(Q\) 单位。第4节的循环同时覆盖全部素数幂，因此某个 \(G_s^k\) 把 \(u/v\) 送到0模 \(Q\)。

其矩阵属于 \(\mathrm{GL}_2(R)\)，行列式为已反演的 \(-d_s\)，故输出仍为 \(R\) 本原列。取整数本原代表 \((u_1,v_1)\)，有 \(u_1\equiv0\pmod Q\)、\(v_1\) 为模 \(Q\) 单位。

选 \(v_1^{-1}\pmod m\) 的平衡代表 \(c\)。因 \(m\) 偶，\(c\) 奇，且
\[
0<|c|\le m/2<p.
\]
先用已实现的 \(U(Qk)\) 使 \(u_1+Qkv_1\) 与 \(c\) 互素。这可按 \(c\) 的素因子用CRT选择；\(\gcd(c,Q)=1\)，原列本原保证每处可选。随后执行 \(C_c\)。输出 \((u_2,v_2)\) 仍本原，且 \(u_2=0\pmod Q,\ v_2=1\pmod m\)。

模 \(Q\) 到模 \(m\) 的单位核，全部由两个已经存在的 \(R\) 单位生成：
\[
\eta_1=-p/t=1-m/t,\qquad \eta_2=e/d=1+2m/d.\tag{9}
\]
若 \(4\mid m\)，LTE给 \(\eta_1\) 在每个局部单位核上的最大阶，各阶互素，所以它单独生成整个核。若 \(m=2\pmod4\)，\(\eta_2\) 生成模 \(2m\) 的单位核，\(\eta_1=3\pmod4\) 补齐另一陪集。这些断言包括 \(m\) 的任意素数幂。

于是存在实际 \(R\) 单位 \(\epsilon\equiv v_2\pmod Q\)。精确纤维引理把 \((u_2,v_2)\) 送到 \((0,\epsilon)\)，对应
\[
(\epsilon^p,(-\epsilon)^p,0^{2t}),
\]
已有三次相反值平均完成归零。该分支不要求 \(3t\le p\)。

当 \(3t\le p\) 时还可直接取 \(s=t\)，得到
\[
SJ_t=-t\,U(1/t).
\]
这是同一机制的较短特例，不是一般定理的容量前提。

## 6. \(t\) 偶且有三个返回：\(8\le r\le p-5\)

此时 \(m\) 奇。取 \(s_0=r-1,s_1=r-3,s_2=r-5\)，对应 \(d,d+n,d+2n\)。按第3节反演 \(t_0,p\)，并加入
\[
c_*=(m+\sigma)/2\text{ 为奇数},\quad \sigma\in\{1,-1\},\qquad
\epsilon_2=\sigma/c_*.
\]
有 \(c_*\le p,\ \gcd(c_*,n)=1\)，故它及其逆正向可用，且
\[
\epsilon_2\equiv2\pmod m.
\]
这只是2的剩余类由一个奇数 \(R\) 单位表示，没有反演有理数2。

先用[已有二进深度下降](../sources/outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)达到 \(v_2(az)=1\)。必要时用 \(J_s\) 交换角色，得到 \(a\) 奇、\(z=u\) 的赋值为1，因而 \(v=a-tu\) 奇。

选 \(v^{-1}\pmod m\) 的平衡代表 \(w=2^h c\)、\(c\) 奇。仍有 \(|c|<p\)。先用 \(U(Qk)\) 保证施加 \(C_c\) 后本原，再施加 \(C_c\)，使 \(v\bmod m\) 属于 \(R\) 单位像，具体可由 \(\epsilon_2^{-h}\) 表示。这些操作保持二进深度一。

### 二进方向

两个比值
\[
\frac{d+n}{d},\qquad\frac{d+2n}{d+n}
\]
模8分别为3和7，因为 \(n=2m\)、\(m\) 奇。选 \(\kappa=3\pmod8\) 的那个。对应实际对角返回在 \((a,z)\) 中使 \(x=z/a\) 乘 \(\kappa\)。而换块使
\[
x\mapsto\frac{x}{-1+rx}\equiv-x\pmod{16}
\quad(v_2(x)=1,\ 4\mid r).
\]
由一次换块及零次或一次 \(\kappa\) 倍率，可覆盖赋值一的全部模16方向。又
\[
v_2(\kappa^2-1)=3,
\]
所以 \(\kappa^2\) 的幂覆盖固定模16方向的全部高阶提升。

取终端
\[
u_T=2,\quad a_T=p-r(p-3)/2,\quad v_T=a_T-2t.
\tag{10}
\]
它本原、合法，且 \(v_2(a_Tu_T)=1\)。上面的动作可使 \(z/a\) 在 \(Q\) 的2部分上与该终端相同。

### 奇素数方向

选择第4节的非退化 \(G_s\)。它模2是交换矩阵，因此其在任何 \(2^b\) 上的矩阵阶都是2的幂。用CRT把奇素数处所需的射影循环指数，和“在2部分矩阵为恒等”的指数条件合并，即可在保持二进方向的同时，使 \(u/v\) 在 \(m^2\) 上命中 (10)。

### 单位尺度

到此输出与 (10) 模 \(Q\) 只差一个单位 \(\lambda\)。所有方向调整把 \(v\bmod m\) 乘以 \(R\) 单位的剩余类：\(J_s\) 的倍率 \(t\) 可由
\[
\tau=\epsilon_2^{v_2(t)}t_0\in R^\times
\]
表示，换块用 \(-1\)，对角比值模 \(m\) 为1。而 \(v_T=t^2\pmod m\)。因此 \(\lambda\bmod m\) 也来自 \(R^\times\)。

剩余单位核由
\[
\kappa_0=(d+n)/d=1+2m/d,\qquad
\eta=(d+2n)/d=1+4m/d
\]
生成。\(\eta\) 通过LTE生成模 \(4m\) 的全部单位核；\(\kappa_0=3\pmod4\) 补另一陪集。故存在 \(\epsilon\in R^\times\) 使输出等于 \(\epsilon(u_T,v_T)\pmod Q\)。

精确纤维引理将其真正送到该终端。选取 \((p+1)/2\) 份 \(A\)、\((p-3)/2\) 份 \(B\) 和一份 \(C\)，和为零。一次平均造出 \(p\) 个零，再用[零触发定理](../sources/outputs/prime_arity/tools/prime_arity_interpolation_and_lattice_structure.md)完整收尾。

## 7. 两种只需固定二进证书的内部边界

还剩 \(r=4\)，以及 \(r=p-3\) 且 \(p=3\pmod4\)。它们的 \(t\) 偶但只有两个标准对合。下面增加一个有实际计数的迹为 \(\pm2\) 的返回。

保留 \(r\) 份旧 \(A\)，第一组取 \(i=p-j-s\) 份 \(A\)、\(j\) 份 \(B\)、\(s\) 份 \(C\)，第二组取全部剩余位置。矩阵在 \((a,z)\) 中为
\[
M=\begin{pmatrix}a_0&D\\-1&0\end{pmatrix},\quad
a_0=p-2j-s,\quad D=rj-ps.
\tag{11}
\]

| 范围 | \(s\) | \(j\) | \(a_0\) | \(D\) |
|---|---:|---:|---:|---:|
| \(r=4,\ p\ge11\) | 1 | \((p-3)/2\) | 2 | \(p-6\) |
| \(r=p-3,\ p=1\pmod3\) | \(p-4\) | 1 | 2 | \(-p^2+5p-3\) |
| \(r=p-3,\ p=2\pmod3\) | \(p-6\) | 4 | -2 | \(-p^2+10p-12\) |

各行容量非负且 \(\gcd(D,rn)=1\)。第二、三行分别避开 \(p-2\)、\(p+2\) 与 \(3(p-1)\) 的共同因子3。\(p=7,r=4\) 使用第二行。

### 新返回的真逆和统一 level

设已有主同余 level 为 \(Q_0\)。取整数 \(k=0\pmod{Q_0}\)、\(k=a_0\pmod D\)，则
\[
H=M U(k) M/D\in\mathrm{SL}_2(\mathbb Z).
\]
它是正向可实现的完整返回。有限逆提升给 \(H^{-1}\)，再由 \(U(k)MH^{-1}=DM^{-1}\) 得 \(M^{-1}\)。

\(MJ_s^{-1}\) 是上三角矩阵，比值为 \(D/d_s\)。其正负共轭使根参数局部化到 \(D\)。与 \(\Sigma\) 作交换子给真正的上根
\[
U\!\left(2a_0+r(1-D/d_s)\right).\tag{12}
\]
括号是 \(nR\) 中的元素，二进赋值恰为2。反演 \(t_0\) 后，原根理想是 \(2^{v_2(t)+1}nR\)，与 (12) 合并得到 \(2nR\)：清除一个奇数 \(R\) 单位分母后，用奇数与2幂的贝祖关系先取得 \(U(2n)\)，再利用 \(R/2^kR\) 的整数代表扩展到全部参数。下根由 \(J_s\) 共轭取得。故可使用
\[
\Gamma((2n)^2,R).
\]
\(m\) 奇，所以2部分只需模16；对 \(r=4\) 下面方便起见使用其子群 \(\Gamma(64m^2,R)\)，多保留两位精度。

### 归一化二进证书保留尺度

令 \(\epsilon_2=\sigma/c_*\) 如第6节，\(\tau\in R^\times\) 表示 \(t\bmod m\)。在 \(r=4\) 时取 \(\tau=\epsilon_2\)；在另一边界取 \(\tau=\epsilon_2^{v_2(t)}t_0\)。

对每个实际矩阵，除以一个明确 \(R\) 单位，使其在模 \(m\) 上保持 \(v\) 不变。这是本原列的分析规范化，不是额外的物理除法。证书使用：
\[
-S,\qquad J_{s_0}/\tau,\quad J_{s_1}/\tau,\qquad
M_{uv}/\alpha,\qquad \operatorname{diag}(c^{-1},1).
\tag{13}
\]
其中 \(M_{uv}=(-t,-1;m(t-s),t+a_0)\)，\(r=4\) 时 \(\alpha=\epsilon_2^2\)，另一边界取 \(\alpha=-D/\tau\)。这些都是 \(R\) 单位，且分别表示 \(M\) 的模 \(m\) 倍率。最后一类来自已取得正向逆的 \(C_c\)：

* \(r=4\)：使用 \(c=p,p-2,p-6,c_*\)，均为允许的小奇数且与 \(n\) 互素。
* \(r=p-3\)：使用 \(c=p,\tau,c_*\)；\(C_\tau\) 是 \(C_{t_0}\)、\(C_{c_*}\) 与换块的乘积。

如下有限证书穷尽所有参数，不是固定几个 \(p\) 的试验：

| 分支 | 参数分类 | 状态空间 | 完整覆盖 |
|---|---|---|---|
| \(r=4\) | 所有奇 \(p\bmod128\)，64类 | \((u,v)\bmod64,\ u+v\) 奇 | 每类2048个状态 |
| \(r=p-3,\ p=3\pmod4\) | \(p\bmod192,\ p\ne0\pmod3\)，及全部奇 \(\tau\bmod16\)，共256类 | \((u,v)\bmod16,\ u+v\) 奇 | 每类128个状态 |

每类中 (13) 的轨道均包含全部状态，终端为 \((0,1)\)。所有生成元的真逆已经证明，故从该终端计算的覆盖树可反向执行。参数分类包含全部实际 \(p\)，因为矩阵剩余类只依赖表中数据；将 \(\tau\bmod16\) 全部列入避免假设某种单位分布。

### 从固定二进证书到完整有理终端

先选 \(v^{-1}\pmod m\) 的平衡代表 \(2^h c\)，用 \(U(Qk)\) 保证本原后执行 \(C_c\)，再以 \(R\) 单位 \(\epsilon_2^h\) 规范化，使 \(v=1\pmod m\)。

用 (13) 把二进列精确送到 \((0,1)\)。选择第4节的非退化 \(G_s\)，并将它规范化为 \(G_s/\tau\)，其模 \(m\) 的 \(v\) 倍率为1。它在二进有限环上的阶为2幂，故可选择一个保持二进列的正向幂，同时在全部奇素数幂上把 \(u/v\) 送到0。

最终 \(u=0\pmod Q\)，而 \(v=1\) 同时成立于 \(m\) 和二进模数。令 \(\kappa=e/d=1+2m/d\)，取其在二进模数上的阶 \(T\)，则 \(T\) 是2幂。\(\kappa^T\) 在奇数模数 \(m^2\) 上生成模 \(m\) 的整个单位核，且在二进部分为1。因此 \(v\bmod Q\) 由一个实际 \(R\) 单位 \(\epsilon\) 表示。

精确纤维引理现在把输出送到 \((0,\epsilon)\)，三次相反值平均归零。两种内部边界完成。

## 8. 全输入结论

第5节覆盖全部奇 \(t\)；第6节覆盖有三个返回的偶 \(t\)；第7节补齐只有两个返回的 \(r=4\) 和 \(r=p-3\) 偶 \(t\)。因此所有 (1) 的合法核心均已完整归零。

[无条件入口](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)已把所有合法原输入送到这些核心。必要性仍是非 \(p\) 共同非零余数不变量。定理得证。

这不是有限方向覆盖之后再次留下“有理实现”缺口：原位置基本返回、真逆、主同余包含、完整单位尺度和最终精确纤维提升都已分别落实。全长平均词可能很长，没有给出统一高效或最短构造。

## 9. 核验范围

[奇 \(t\) 核验](../sources/work/verify_even_odd_half_core.py)检查110组一般内部参数、880次素数幂循环和880次单位提升；包含模9退化的负对照与相邻返回修复，以及 \(p=13,t=5\)、\(p=17,t=7\) 两条超出原 \(3t\le p\) 容量的精确终端矩阵。较短平衡分支另有65组恒等式、9200个单位类、520个终端输送、30条原位置根和5条七原子完整归零路径。

[偶 \(t\) 与边界核验](../sources/work/verify_even_interior_completion.py)穷尽上述64类及256类二进证书，重放30个一般原位置返回和7组迹为 \(\pm2\) 的真实返回，并核对255条三返回分支的完整方向—尺度输送及48条内部边界输送。

它们没有搜索平均词，也没有用有限 \(p\) 样本外推一般定理。无限部分由本页局部循环、LTE、有限逆提升及明确外部依赖承担；固定二进参数空间则由完整有限证书承担。

数据：[奇 \(t\) 记录](../sources/work/even_odd_half_core_records.json)、[偶 \(t\) 与边界记录](../sources/work/even_interior_completion_records.json)。验证ID：even-interior-completion。

当前仍须攻的是 \(r=2\) 与 \(r=p-1\) 两个单对合边界。它们没有本页起点 (5) 的双返回深主同余控制，不能直接套用有限逆提升。

<!-- END SOURCE doc-3e4834660712 -->

---

<a id="doc-2403827e76f3"></a>

## 原文导签：全部 3p-1 的统一完成与五平均最优阈值

来源：`outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md` · [逐字节原样副本](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md)

**PRIME-3PM1 · 原证明已完成（沿用登记，非本次重审）**

全部素数p≥5、n=3p−1的完整G=1判据；p≥7通式，p=5有显式夹乘。

**边界：** 两条偶数边界均已完成；本卡并未宣称与r=2及内部是同一资源公式。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-3PM1`）

旧核验ID：`three-p-minus-one-completion`
<!-- BEGIN SOURCE doc-2403827e76f3 -->
# 全部 3p-1 的统一完成与五平均最优阈值

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../sources/outputs/prime_arity/README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

日期：2026-09-15。p 表示每次平均的元数，n 表示原位置数。

## 1. 定理与剩余范围

**定理。** 对每个素数 p>=5，n=3p-1 的任意非全等有理输入，经有限次原位置 p 平均可达全等，当且仅当本原中心化差分 gcd 为 G=1。

特别地，五平均14元完整解决。接已有11、12、13元及全部n>=15的定理，并结合10元反例，得到
\[
\boxed{N(5)=11.}
\]

一般证明适用于全部 p>=7，无参数表、平均词搜索或有限方向图。p=5使用同一类重叠返回，加一个显式夹乘恒等式；方向与单位尺度仍由解析公式完成，也不枚举模群。

证明沿用 Morris 2007 定理6.1(2)、Serre 强同余子群性质及项目既有深同余、正向取逆引理。原文访问与外部依赖边界见[深同余引理](../sources/outputs/prime_arity/history/prime_arity_even_middle_congruence_and_eighteen.md)。本文没有用程序证明这些外部无限群定理。

此后任意素数的临界全解仍剩：一般2p+2，以及3p+1至3p+9中尚未完成的偏移族。不是声称这些剩余维数均已证明。p=2、3、5、7现在各自已具有最优阈值。

## 2. 核心、标准对合及自由角色交换

置
\[
r=p-1,\quad n=3p-1,\quad d=p^2-3p+1.
\]
无条件下半带入口把任意合法输入送到
\[
K(a,z)=(a^p,(rz-a)^p,(-pz)^r),
\quad \gcd(a,z)=\gcd(a+pz,n)=1.
\tag{2.1}
\]
标准两步对合及等大块角色交换为
\[
A=\begin{pmatrix}0&-d\\-1&0\end{pmatrix},
\quad A^2=dI,\qquad
S=\begin{pmatrix}-1&r\\0&1\end{pmatrix}.
\tag{2.2}
\]
A 的实际尺度为1/p，S只更新两个p块的角色标签。d与pn互素。

以下全部矩阵表示整体非零标量意义下的真实核心返回。所有位置共同缩放只用于分析，不作为额外物理操作。

## 3. 三步重叠对合

给定 sigma和h，先平均
\[
(A^{p-\sigma},C^\sigma),
\]
得到p份新值
\[
D=\frac{p-\sigma}{p}a-\sigma z.
\]
保留其中r=p-1份作最终载体。其余位置为 sigma份旧A、p份旧B、r-sigma份旧C以及一份D。

平均
\[
(A^{h-\sigma},B^h,C^{p+\sigma-2h}),
\]
再平均其余p份，总计三次原子平均。只需
\[
0\le h-\sigma\le\sigma,\quad h\le p,\quad
0\le p+\sigma-2h\le p-1-\sigma.
\tag{3.1}
\]
实际返回矩阵为p^-2乘
\[
J_{\sigma,h}=
\begin{pmatrix}
-p\sigma&p[nh-p(p+\sigma)]\\
-(p-\sigma)&p\sigma
\end{pmatrix}.
\]
其平方为
\[
\boxed{J_{\sigma,h}^2=p f_{\sigma,h}I,\qquad
f_{\sigma,h}=p^3-n(p-\sigma)h.}
\tag{3.2}
\]
f模n为p³，故非零且与n互素。重复三步返回提供真实正向射影逆。

对所有p>=7，以下四个参数同时满足(3.1)：
\[
(\sigma,h)=(2,3),(2,4),(3,4),(3,5).
\tag{3.3}
\]
最紧的计数是p+2-2*4=p-6和p+3-2*5=p-7，均非负。这是整个一般证明唯一的p>=7容量门槛。

## 4. 自由角色交换把根理想降到2n

固定sigma=2或3，取h=sigma+1，记
\[
f_\sigma=f_{\sigma,h},\quad
g_\sigma=f_{\sigma,h+1}=f_\sigma-n(p-\sigma).
\]
由于p不整除sigma，且f_sigma与n互素，
\[
\gcd(f_\sigma,g_\sigma)
=\gcd(p^3,n(p-\sigma))=1.
\]
相邻对合的商为
\[
T_\sigma=J_{\sigma,h}^{-1}J_{\sigma,h+1}
=\begin{pmatrix}1&-p\sigma n/f_\sigma\\0&g_\sigma/f_\sigma\end{pmatrix}.
\]
它与角色交换S的交换子恰为
\[
\boxed{[S,T_\sigma]=
U\left(\frac{n[n\sigma-pr]}{g_\sigma}\right).}
\tag{4.1}
\]
两个整数系数相差n，并且
\[
\gcd(2n-pr,3n-pr)=\gcd(n,pr)=2.
\tag{4.2}
\]
令
\[
R_0=\mathbb Z[1/|f_2g_2f_3g_3|].
\]
两个倍率及其逆生成R_0，因而上根参数在R_0上封闭。式(4.1)、(4.2)与Bezout给出U(2nR_0)。

不需要先假定d可逆：对任意x属于2nR_0，已可执行U(dx)，而
\[
A\,U(dx)\,A^{-1}=L(x).
\]
因此也有L(2nR_0)。深同余引理给出
\[
\boxed{\Gamma(4n^2,R_0)\text{ 正向可执行}.}
\tag{4.3}
\]
2已整除n，故控制层没有任何额外素数。这比先产生含r或p的深根再逐项消除更直接。

## 5. 单位像满时，可以在方向调整后重新本原化

以下小引理避免一个不必要的行列式局部化要求。

**局部本原化引理。** 设R的反演素数均不除正整数M，Gamma(M,R)已可执行，且R单位模M满射。给定本原整数列v，若一条实际正向路径的矩阵属于GL2(Z_(M))，其中Z_(M)表示分母与M互素的有理数环，并使其方向满足z/y=0模M、y为局部单位，则可以正向精确送到(0,epsilon)，epsilon为某个R单位。

证明：将路径后的矩阵列清去与M互素的分母，得到整数列(z_0,y_0)。因矩阵在每个ell|M处可逆，该列仍局部本原，故其整数坐标gcd与M互素。除这个gcd后得到本原整数列(z,y)，仍有z=0模M、y为单位。单位像满射给epsilon=y模M。

取alpha z+beta y=1，调整(alpha,beta)为(alpha+ty,beta-tz)，使alpha=0模M。则
\[
P=\begin{pmatrix}
y/\epsilon&-z/\epsilon\\
\epsilon\alpha&\epsilon\beta
\end{pmatrix}
\in\Gamma(M,R),\qquad
P(z,y)^T=(0,\epsilon)^T.
\tag{5.1}
\]
Gamma(M,R)提供真实正向实现。实际状态和分析列之间仅差共同非零尺度，因此同样产生零终端。证毕。

引理不允许忽略本原化；它明确追踪被除因子在模M下是单位。只有在R单位像满时，才可不将路径中每个行列式因子预先反演。若单位像只是一个真子群，原来保留R本原性的要求仍然重要。

## 6. 奇数数字与乘3折返给全部模n单位

保留旧C的两块混合为
\[
F_t=\frac1p
\begin{pmatrix}
t&r(p-t)/2\\0&p
\end{pmatrix},
\qquad t\text{ 奇},\quad -p\le t\le p.
\tag{6.1}
\]
它的原位置两组分别取(p-j,j)和(j,p-j)份A、B，其中j=(p-t)/2。

F_1的整数代表行列式为p，与4n²互素，故既有安全整数返回取逆引理适用。其上三角倍率反演p，先将p加入R。随后
\[
C_b=F_bF_1^{-1}
=\begin{pmatrix}b&r(1-b)/2\\0&1\end{pmatrix}
\]
对每个奇数1<=b<=p、gcd(b,n)=1都实际存在。行列式b与控制层互素，故C_b的逆可执行。上下根随倍率共轭扩张到这些b全部反演后的有限局部化环R，且Gamma(4n²,R)继续成立。

因为n=3p-1不被3整除，3属于这些安全数字。对任意模n单位u，取正平衡绝对代表b<n/2；n偶使b必奇。若b>n/4，以
\[
b\longmapsto |n-3b|
\tag{6.2}
\]
替代。结果仍是正奇数、与n互素，并严格减小；它只改变u所乘的符号和3的幂。最终
\[
1\le b\le n/4<p.
\]
这个b已是R单位。倒推(6.2)，得到u的R单位提升。因此
\[
R^\times\longrightarrow(\mathbb Z/n\mathbb Z)^\times
\quad\text{满射}.
\tag{6.3}
\]
没有要求3是模n的原根，也没有单位代表表。

## 7. 同一条方向循环适用于全部p>=7

取
\[
V=J_{3,4}A/p^3,
\]
在整幺模(z,y)=(z,a+pz)坐标中有
\[
V=\begin{pmatrix}1&-3/p^2\\0&1\end{pmatrix}\pmod n,
\]
\[
\operatorname{tr}V=2-\frac{n(5p-3)}{p^3}=2\pmod4.
\tag{7.1}
\]
平移系数在所有ell|n处均为单位，因为3不整除n。迹的模4条件适用于全部p，不必选择奇偶分支。

已有局部射影循环引理因此适用于所有2幂和所有奇素数幂ell|n。指数CRT用V的一次非负幂将任意合法方向送到
\[
z/y=0\pmod{4n^2}.
\tag{7.2}
\]
A的行列式可能未在R中反演，但它与n互素；第5节正好允许在方向调整后处理这个共同内容。

## 8. 从n到4n²的全部单位尺度

已有R单位
\[
\kappa_2=g_2/f_2=1-\frac{n(p-2)}{f_2},\quad
\kappa_3=g_3/f_3=1-\frac{n(p-3)}{f_3}.
\]
对任意奇素数ell|n，有gcd(p-3,n)只含2，因此
\[
v_\ell(\kappa_3-1)=v_\ell(n).
\]
kappa_3的幂生成全部奇素数处的主单位核。

二进处，p-2为奇数，故
\[
v_2(\kappa_2-1)=v_2(n).
\]
若4|n，先用kappa_2调好全部二进位；随后用kappa_3的完整二进阶次幂修复奇素数处。该阶是2幂，不改变任何奇素数处的LTE起始深度。

若n=2模4，则p=1模4，v_2(p-3)=1。kappa_2=3模4补两类中的一类，kappa_3从1模4开始生成余下全部二进主单位。再同样用完整二进阶次幂修复奇素数处。于是主单位核全部生成。

接(6.3)，R单位模4n²满射。第5节把(7.2)精确送到(0,epsilon)。核心成为
\[
(\epsilon^p,(-\epsilon)^p,0^{p-1}).
\]
以(p-1)/2份epsilon、同样多份-epsilon和一个零组成零和p元组，即可触发统一零收尾。这完成全部p>=7。

## 9. 五平均14元：一个显式夹乘补齐最小容量

这里p=5、r=4、n=14。只需以下三个已实现变换：
\[
A=\begin{pmatrix}0&-11\\-1&0\end{pmatrix},\quad
S=\begin{pmatrix}-1&4\\0&1\end{pmatrix},\quad
J=J_{1,2}=\begin{pmatrix}-5&-10\\-4&5\end{pmatrix}.
\]
A²=11I、J²=65I，J仍是第3节的三原子返回。

令
\[
W=ASASJ=
\begin{pmatrix}-121&330\\0&65\end{pmatrix}.
\]
直接得到
\[
[S,W]=U(84/65).
\tag{9.1}
\]
这个上三角词也可以由有理方向确定：J送无穷远到5/4，S送到11/4，A送到4，S送到0，再由A送回无穷远。不是平均词搜索的输出。

由于121与65互素，W的倍率及其逆生成
\[
R_0=\mathbb Z[1/(5\cdot11\cdot13)].
\]
所以U(84R_0)、L(84R_0)及Gamma(7056,R_0)已可执行。

F_1的整数行列式5与7056互素，故可激活其逆，得到
\[
C_3=F_3F_1^{-1}=\begin{pmatrix}3&-4\\0&1\end{pmatrix}.
\]
虽然3整除旧控制层，下面的夹乘直接提供其逆：
\[
H=\frac13C_3JC_3
\ =\begin{pmatrix}1&-18\\-4&7\end{pmatrix},
\quad \det H=-65=\det J.
\tag{9.2}
\]
HJ^{-1}属于SL2(R_0)，且正向可执行。有限逆提升引理因而给出H^{-1}，再用
\[
JC_3H^{-1}=3C_3^{-1}
\]
取得C_3的真正正向射影逆。

共轭上根反演3。令R=Z[1/(3*5*11*13)]，则84R=28R，再次用深同余引理得到
\[
\boxed{\Gamma(784,R).}
\tag{9.3}
\]

### 9.1 不用有限轨道图的方向与尺度

取V=JA/125。其模14平移为-1/25，迹为2-196/125=2模4。因此一个V的CRT指数覆盖模16和模49的全部合法仿射方向。

以下三个实际R单位的余数为
\[
\begin{array}{c|cc}
&\bmod16&\bmod7\\ \hline
15&-1&1\\
10725&5&1\\
2145&1&3
\end{array}
\]
因为-1和5生成模16单位群，3生成模7单位群，这三者已覆盖模112的所有单位。它们分别为3*5、3*5²*11*13、3*5*11*13。

再令lambda=-121/65，有
\[
\lambda^2-1=\frac{10416}{4225},
\quad v_2(10416)=4,\quad v_7(10416)=1.
\]
故lambda²模16为1，并生成模49到模7的七阶单位核。于是R单位模784满射。

由(9.3)、第5节和同一个相反值终端，全部合法14元核心及全输入均归零。

## 10. 五平均最优阈值及验证边界

已有[十一元](../sources/outputs/prime_arity/examples/five_average_eleven_complete.md)、[十二元直接下降](../sources/outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)第11节、[十三元](../sources/outputs/prime_arity/examples/five_average_thirteen_congruence_complete.md)和[全部n>=15](../sources/outputs/prime_arity/examples/five_average_three_p_threshold.md)的完整判据。本文补齐14元，故N(5)<=11；10元的既有G=1不可达例排除更低阈值，得到N(5)=11。

[核验程序](../sources/work/verify_three_p_minus_one_completion.py)只用精确矩阵、闭式计数和逐位模幂：

- p<250的50组一般参数及7874个完整模n单位代表；
- 200组局部方向、主单位和精确纤维接口；
- 78条原位置返回及重复闭路；
- 五平均夹乘、336个模784单位的显式指数，以及12组完整终端接口。

这些有限核验用于发现公式与实现错误；全部输入与全部p的量词由正文证明承担，没有搜索平均词或有限方向轨道。记录文件仅保存单位指数与核验统计，不是一般群词提取器。

核验入口：python work/run_verifications.py --id three-p-minus-one-completion。

<!-- END SOURCE doc-2403827e76f3 -->

---

<a id="doc-90dc128dc488"></a>

## 原文导签：2p 与 4p 之间：三块运输解掉 3p，并缩小双重值障碍

来源：`outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md` · [逐字节原样副本](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md)

**PRIME-3P · 原证明已完成（沿用登记，非本次重审）**

n=3p的完整判据允许G为p幂；等大三块具有独立的真实运输／终端机制。

**边界：** 此处不可简写G=1；本原重数改变，未由r≠p的共同控制器替代。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-3P`）

旧核验ID：`prime-arity-middle-band`
<!-- BEGIN SOURCE doc-90dc128dc488 -->
# 2p 与 4p 之间：三块运输解掉 3p，并缩小双重值障碍

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../sources/outputs/prime_arity/README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

日期：2026-09-12。p 是一次平均的位置数，主要讨论奇素数 p。

最新五平均阈值：[最小见证与总和证书](../sources/outputs/prime_arity/examples/five_average_three_p_threshold.md)已解决五平均16、17、18元，接本页15元与已有>=19，得到N(5)<=15，尚待覆盖12、13、14。一般p的3p级统一界仍未证明。

最新：[逆EGZ与共同预留](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_inverse_egz_threshold.md)已把统一条件降至n>=4p-2+d，新增五平均十九元与七平均二十七元。三重值的非等重数分支在n>=3p+2也已闭合；本页第8节的对应旧缺口现由该引理解决。五平均尚待覆盖12、13、14、16、17、18，N(5)<=19。

同日后续：[支持数传播与统一造零收尾](../sources/outputs/prime_arity/tools/prime_arity_interpolation_and_lattice_structure.md)利用本页3p定理及已有4p、大维数结果，证明所有n>=2p+1中，一旦真实p平均产生p个零即可完整归零；低维段只需已有的2p+1含零尾部，不必假设完整端点。尚未证明每个合法输入都能先造零，因此本页未解维数列表不变。

## 1. 本次解决了什么，尚未解决什么

此前的通用充分条件仍是

\[
n\ge4p-1+d_p(n),\qquad
d_p(n)=\#\{q:q\mid n,\ q\ne p\text{ 为素数}\}.
\]

因此严格上界仍是 N(p)<=4p+ceil(log_2 p)+1，不能简写成已证明所有 n>=4p-1。
[临界端点控制器](../sources/outputs/prime_arity/tools/uniform_endpoint_positive_controller.md)也没有自动填满中间维数。

本页补上两项结构结果：

**定理 A。** 对每个奇素数 p，n=3p 已满足完整判据：非零本原中心化输入可经有限次 p 平均归零，当且仅当 G 为 p 幂。

特别地，五平均十五元、七平均二十一元、十一平均三十三元等全部解决。
证明只使用一个九项非负整数运输表及固定的 Gamma_0(3) 结构，没有随 p 搜索种子或轨道。

**引理 B。** 在 n>=3p+d_p(n) 时，若合法整数零和状态恰有两个不同 p 重值，并且它们模 p 同余，则存在安全非恒等整数 p 平均，继续保留两个不同 p 重值。

这些结果不证明整个 2p+1 至 4p-1 区间，也没有降低当前 N(p) 的通用上界。
它们确实解决一个完整中间维数，并把 3p 以上的旧双重值困难进一步集中到模 p 不同余的情形。

五平均当前已证 n=11、15 和全部 n>=20；本次整理中仍待覆盖 n=12、13、14、16、17、18、19。

## 2. n=3p 的资源与端点不同

三个 p 重块写成

\[
\mathcal C_p(a,b,c)=(a^p,b^p,c^p),\qquad a+b+c=0.
\]

每个输入值恰有 p 个实际副本。
任意 3x3 非负整数矩阵 K，只要每行、每列之和均为 p，就可以按以下方式实现 K/p：

- 第 i 个新块从第 j 个旧块取 K_ij 个尚未使用的位置；
- 每列和为 p 保证恰好用完每个旧块；
- 每行和为 p 保证每个新块可用一次真实 p 平均产生。

三个新块互不相交，共用原来的全部 3p 个位置，恰执行三次 p 平均。
这是一层真实的分组操作，不是允许任意双随机矩阵。
我们下面只使用两个明确的 K，逐项证明其非负性。

## 3. 一对统一的正向剪切运输表

以下先设 p>=5。取 epsilon 属于 {1,-1}，使

\[
p=3m+\epsilon.
\]

因为 p 是不等于 3 的奇素数，m>=2。
令 J_3 是 3x3 全一矩阵，置

\[
D=\begin{pmatrix}
1&-1&0\\
1&-1&0\\
-2&2&0
\end{pmatrix}
=\begin{pmatrix}1\\1\\-2\end{pmatrix}(1,-1,0).
\]

有

\[
D\mathbf1=0,\qquad\mathbf1^TD=0,\qquad D^2=0.
\]

定义两个整数运输表

\[
\boxed{K_\pm=mJ_3+\epsilon(I\pm D).}
\tag{1}
\]

I+D 和 I-D 的每个元素都位于 [-2,2]。
因此 K_+、K_- 的每个元素至少为 m-2>=0。
两者每行、每列之和都是 3m+epsilon=p，所以第 2 节给出真实实现。

对零和三参数 v=(a,b,c)^T，J_3v=0，故

\[
\frac1pK_\pm v=\frac\epsilon p(I\pm D)v.
\tag{2}
\]

改用整数幺模参数坐标

\[
x=a,\qquad y=a-b,
\]

I+D 的作用是

\[
(a,b,c)\mapsto(a+(a-b),\ b+(a-b),\ c-2(a-b)),
\]

所以在 (x,y) 上恰为 U(1)；I-D 恰为 U(-1)。
因此一次三平均层分别实现

\[
\boxed{\frac\epsilon pU(1),\qquad\frac\epsilon pU(-1).}
\tag{3}
\]

两层复合在零和参数空间上是 p^(-2)I。
这是明确的正向逆关系，不需要额外的周期存在性假设。

### 五平均的两个实际表

p=5 时，m=2、epsilon=-1，两个表为

\[
K_+=\begin{pmatrix}0&3&2\\1&2&2\\4&0&1\end{pmatrix},
\qquad
K_-=\begin{pmatrix}2&1&2\\3&0&2\\0&4&1\end{pmatrix}.
\]

例如 K_+ 的第一行就是从 b 块取三个位置、从 c 块取两个位置进行五平均。
每张表只需三次五平均。

这说明 3p 的正向实现来自足够的副本和非负运输余量，不依赖精细的 p 参数周期。

## 4. 同一个 Gamma_0(3) 覆盖所有 p 的合法三块

交换 a、b 两个块的名称，参数作用为

\[
\Sigma=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
\]

交换 a、c 两个块的名称，参数作用为

\[
P=\begin{pmatrix}-2&1\\-3&2\end{pmatrix}.
\]

这些交换都只是更新完整 p 元块的原位置账本。
直接计算

\[
P\Sigma=U(1)L(-3),\qquad
\boxed{L(-3)=U(-1)P\Sigma.}
\tag{4}
\]

所以 U(1)、L(3) 及其逆都有正向实现。

完整 Gamma_0(3) 包含可以用固定的四个右陪集证明：

\[
I,\qquad \mathsf S\mathsf T^{-1},\quad\mathsf S,
\quad\mathsf S\mathsf T,
\qquad
\mathsf S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad\mathsf T=U(1).
\]

非平凡 Schreier 回路只有 U(1)、L(-3) 及其逆。
因此上述正向操作包含整个 Gamma_0(3)，而不是仅在模 3 上有足够的像。

对本原整数三参数，a+b+c=0，

\[
G(a,b,c)=\gcd(a-b,3).
\]

证明：在 y=a-b 下，另一差 b-c=3a-2y；因 gcd(a,y)=1，两个差的 gcd 等于 gcd(y,3)。
复制 p 次不改变坐标 gcd 或差分 gcd。
于是合法三块恰对应本原 (x,y) 且 3 不整除 y。

取 alpha*x+beta*y=1，并沿 Bezout 通解调整使 3 整除 alpha。则

\[
H=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}\in\Gamma_0(3),
\qquad H(x,y)^T=(0,1)^T.
\]

由群包含与正向逆，将 H 编译成有限个真实运输层，得到

\[
(0^p,s^p,(-s)^p).
\]

令 h=(p-1)/2。依次平均

\[
(s^h,(-s)^h,0),\quad
(s^h,(-s)^h,0),\quad
(s,-s,0^{p-2}),
\]

三次实际 p 平均后全部归零。

标准模群矩阵 S 只参与代数分解，不被当成自由物理操作。
整数 Euclid 分解和四陪集重写保证每个输入都有有限操作词；不需逐输入搜索路径。

## 5. 任意 3p 元合法输入的三步入口

设 X 是非零本原整数零和输入，G(X) 为 p 幂，p>=5。
因为 3|3p 而 3!=p，原输入模 3 不全同余。

任意将位置分成 A、B、C 三组，每组 p 个，记各组和为 S_A、S_B、S_C。
如果三个组和模 3 不全同余，直接分别平均即可。

否则三个组和同余于 r。由于原输入模 3 不全同余，必有不同组中的两个值 x、y 模 3 不同。
交换它们在分组中的归属，令 delta=y-x!=0 mod 3，则新的组和余数是

\[
r+\delta,\qquad r-\delta,\qquad r,
\]

它们两两不同。
按修复后的分组执行三次 p 平均，进入合法三块状态。
这一步使用 p 在模 3 下可逆；没有调用更小维数的 p 平均定理。

必要性仍是非 p 共同非零模余数障碍。
p=3 时 n=9，用两层三元蝶形网络即可把所有输入平均。
至此定理 A 对每个奇素数 p 都已证明。

## 6. 旧的 3p 闭包反例被整个解决

此前用来否定“一步保持两个 p 重值”的族为

\[
E_p=\bigl((-(\kappa p+1))^p,1^p,(\kappa p)^p\bigr),
\]

其中 p=2 mod 3 时 kappa=1，p=1 mod 3 时 kappa=2。
它们合法，但每次非恒等整数平均都破坏双 p 重值，且不能一步造零。

现在 E_p 已被定理 A 统一解决。
新方法允许一个运输层的内部步骤暂时破坏旧重数；完整三次操作后恢复三个 p 重块。
必要时使用更深的 p 进分母，所以不再强求每个原子都是整数平均。

因此这里的进展是一个完整的多步原位置机制，不是把旧闭包障碍忽略掉。

## 7. 3p 以上的同余双重值不再是缺口

证明引理 B。设恰有两个不同 p 重值 a、b，且 a=b mod p，重数为 A、B。

若 B>=p+1，平均 (a^(p-1),b)。它是非恒等整数平均，均值严格介于 a、b 之间，而 b 仍有至少 p 份。
a 和 b 都有未选副本，所以操作安全，并继续有两个不同 p 重值。
A>=p+1 的情况对称。

只剩 A=B=p。低重数位置池 L 有

\[
|L|=n-2p\ge p+d_p(n).
\]

对每个危险素数，若其例外支持全部落在 L 中，就保留其中一个位置不选。
至多保护 d_p(n) 个位置，仍能取出 p 个低重数位置 x_1,...,x_p。
若危险支持包含整个 a 或 b 重值，它至少占 p 个位置，下面每次只选至多 p-1 份锚点，故也不会完整选中它。

对模 p 的 p 个差值 x_i-a，使用部分和

\[
0,\quad x_1-a,\quad (x_1-a)+(x_2-a),\quad\ldots
\]

必有两项相等。两项之间给出非空片段 T，长度 s<=p，且

\[
\sum_{x\in T}(x-a)=0\pmod p.
\]

可以用 a 或 b 把 T 补足 p 个位置。两种均值为

\[
c_a=\frac{\sum T+(p-s)a}{p},\qquad
c_b=\frac{\sum T+(p-s)b}{p}.
\]

它们都是整数，且

\[
c_a-c_b=\frac{p-s}{p}(a-b).
\]

不可能同时 c_a=b、c_b=a，否则因 a!=b 会推出 s=2p，与 s<=p 矛盾。
所以至少一种补法产生不同于完整保留重值的新 p 重值。
所选片段都是不同于 a、b 的低重数值，保证非恒等；若 s=p，则低重数限制同样排除恒等。
危险见证全部保留，所以操作安全。引理 B 得证。

这里需要的低重数池长度是 p+d，不再是 EGZ 的 2p-1+d。
构造使用一次线性扫描的模 p 部分和碰撞，无位置子集枚举。

## 8. 中间区间现在具体卡在哪里

对旧的双 p 重值整数不变量，保留以下已经完整证明的分支：

- 有至少四个重值：原顺序引理处理。
- 恰有三个重值，存在低重数值，或某个极端重值多于 p 份，或两个重值模 p 同余：原顺序引理处理。
- 存在 2p-1 重的背景值：原背景值引理处理。
- 恰有两个模 p 同余的重值：n>=3p+d 时由本页引理 B 处理。

这样，在 3p+d 附近尚未闭合的旧分类主要集中到：

1. 恰有两个重值，模 p 不同余，且没有 2p-1 重背景。不能继续把两组各 p 份全部冻结后再调用一般 EGZ。
2. 只有三个实际值 a<b<c，两个极端恰为 p 份，中间有 n-2p 份；三个值模 p 各不相同。n=3p 现已解决，但 3p<n<4p-1 时各块重数不再相等。

在更低的 2p<n<3p 区间，只有两个完整 p 重块，第三组副本资源尚不存在。
此外，旧的“两次整数平均初始化”只在 n>=3p+d 有通用证明，不能默默延伸到更低维数。

因此应区分两个任务：先处理 3p 以上的非等重数耦合，再处理 2p 至 3p 之间缺第三块的位置资源。
这比把整段统称为“再找一个种子”更准确。

## 9. 为什么 3p 定理不能直接嵌入更大维数

本页两张表的复合在全部三参数空间上为

\[
\frac1{p^2}K_+K_-
=\Pi+\frac1{p^2}(I-\Pi),\qquad \Pi=J_3/3.
\]

在整个 n=3p 的零和系统中，Pi 项消失，所以它是可用的正向射影逆。
若这 3p 个位置只是更大系统的一部分，它们的局部均值一般不为零，Pi 项必须保留。
于是得到的是围绕局部均值的收缩，不能当成全系统的射影逆。

另外，任意选出的 3p 元子块也未必满足自身的 p 平均可达判据。
因此“3p 已解，冻结额外位置重复调用”不是现成的维数扩张定理。

后续需要明确处理不同块总和之间的转移，或者找到允许临时破坏重数的全局下降量。
本页已经展示了后一类多步机制在等重数中心 n=3p 处如何实际成立，但尚未证明其覆盖整段区间。

## 10. 核验与范围

`work/verify_prime_arity_middle_band.py` 独立构造九项运输表，验证非负性及每行每列容量，
在两个独立零和输入上逐次执行真实 p 平均。
固定四陪集重写处理全部生成元边；Euclid 的平移幂按商一次性重写，不逐个扫描同余余数。
全部输入路径使用实际 Fraction 值，未用本原化伪装数值操作。

它还检查引理 B 的部分和构造、危险见证和双重值保持。
没有调用端点控制器，也不运行平均词搜索。

一般 p 定理、任意输入覆盖和引理 B 的维数界由正文证明；有限核验只防止公式与账本错误。
不声称最短路径、统一位长多项式原子长度或一位额外 p 进精度。

本次核验通过：40 组双基输入上的真实运输层，固定四陪集的全部 12 条生成元边，
7 个 p 上的旧闭包反例族，7 个 G=p 的合法输入，56 个其他原题输入的完整 Fraction 路径，
最长样本 105 次原子平均；另核对 996 个同余双重值闭包实例。

项目入口：`python work/run_verifications.py --id prime-arity-middle-band`。

<!-- END SOURCE doc-90dc128dc488 -->

---

<a id="doc-ce510dd1fb98"></a>

## 原文导签：小参数怎样自然闭合：格指数、退化纤维和真正尚缺的定理

来源：`research/prime_arity_padic/small_parameters_lattice_defects_and_closure_target.md` · [逐字节原样副本](../sources/research/prime_arity_padic/small_parameters_lattice_defects_and_closure_target.md)

**PRIME-NATURAL-UNIFICATION · 开放问题**

原阈值已证。目标是统一2p<n<4p的初始物理资源供应；纤维比较、改变来源、状态相关准备是并列候选策略。奇数下半带已有共同反射。

**边界：** 退化出口不是唯一必经关卡；先有独立真实资源才可使用深核。共同收尾、共同形状与同一选参公式是不同强度。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-NATURAL-UNIFICATION`）
<!-- BEGIN SOURCE doc-ce510dd1fb98 -->
# 小参数怎样自然闭合：格指数、退化纤维和真正尚缺的定理

2026-09-16。回答“新视角怎样处理小p以及全部1≤r≤2p−1”。本页给两个全参数结构计算及一个明确标注的有限诊断；不宣布新的全参数无证书证明。原可达性结果已覆盖全部范围，当前任务是替代其分散的充分性构造。

## 1. 先把格写正确：端点CRT推广的障碍不是有理数m本身

设p为奇素数、1≤r<p，n=2p+r。共同整参数为
\[
(A,B,C)=(a,rz-a,-pz),\qquad (a,z)\in\mathbb Z^2.
\]
若r奇，取u=A+B=rz、v=A−B=2a−rz，则像格为
\[
L_r=\{(u,v)\in\mathbb Z^2:r\mid u,\ u\equiv v\pmod2\},
\quad [\mathbb Z^2:L_r]=2r.
\tag{1.1}
\]
若r=2t偶，取半块和／差u=tz、v=a−tz，则
\[
L_r=t\mathbb Z\times\mathbb Z,
\quad[\mathbb Z^2:L_r]=t=r/2.
\tag{1.2}
\]
两式由坐标换元矩阵(0,r;2,−r)和(0,t;1,−t)的整数像直接得到。

因此U(k):(u,v)↦(u+kv,v)保持整张L_r，当且仅当
\[
\boxed{2r\mid k\ (r\text{奇}),\qquad (r/2)\mid k\ (r\text{偶}).}
\tag{1.3}
\]
这是格保持条件，不是这些剪切已能物理执行。换回(a,z)时，奇r的左下系数为2k/r、右上为−kr/2；偶r的左下为k/t，给出同样充要条件。

r=1时指数2，端点控制器已能反演2；r=2时指数1，因此[共同两次CRT](../sources/research/prime_arity_padic/adelic_primitive_lines_and_common_endpoint_preparation.md)可以使用完整整数上平移。一般r不能仅从共同矩阵形式就假设U(Z)可用；这正是推广时遗漏的前提。

与此同时，格指数与n的共同素因子至多为2。奇r时gcd(2r,n)=1；偶r时gcd(t,n)=gcd(t,2)。所以一般r的所有**奇格缺陷**均不在危险素数上。可以争取用局部化、夹乘取逆或按当前列的本原化处理；共同危险的整性集中在2。这一事实贯穿旧证明的“反演载体奇因子＋二进修补”，不是每个r都发生一套新的算术现象。

自然的带权CRT必须先指定作用于L_r的允许剪切步长及内容变化，再做局部准备。可以局部化某个奇因子不表示其逆已经物理实现，也不能反演危险2。第(1.3)式正好使这些前提可检查。

## 2. 小容量的真实退化：r=1、2、4不能硬套相邻反射

考虑最近新载体模板：q=1或2组相同来源(i,j,k)，i+j+k=p，来源差α=i−j非零。交换A、B标签可设0<α<p。输出(x,y,u,v)及其相邻表
\[
(x-1,y-1,u+2,v)
\]
都要合法，并满足迹零p(x−y)+αv=β=rj−pk。两张表需要至少两份剩余旧C，即
\[
qk\le r-2.
\tag{2.1}
\]

**r=1：**(2.1)不可能。

**r=2：**只可能k=0。q=2会要求i,j≤(p−1)/2而i+j=p，不可能；q=1时α=p−2j，迹零模p给v≡−1 modp，但0≤v≤p−2，不可能。

**r=4：**q=2时k≤1；k=0不可能，k=1强迫i=j=(p−1)/2，违反α≠0。故q=1，k∈{0,1,2}。k=0时迹零模p给v≡−2，而v≤p−4，仍不可能。k=2时剩余C仅两份，所以基输出u=0；α与p−k同为奇，β=4j−pk为偶，迹零模2给x+y+v偶，却与输出总数p及u=0矛盾。只剩
\[
\boxed{k=1,\quad\alpha\text{ 偶},\quad
H=n(i+j)-2p^2=2(p-2).}
\tag{2.2}
\]
这里H正是相邻反射与换块交换子中的根系数。无论增加多少这个模板的表，来源差始终偶，整数H始终同一个2(p−2)。这说明它们不能自动满足新共同接口要求的gcd α=1、gcd H=2。

这不排除从这些表的其他倍率反演p−2，或用另一种共轭获得更强控制；也不排除α=0、多来源、长词。它严格排除的是“只要更仔细挑选本模板的相邻反射，就会覆盖端点和r=4”的想法。

旧r=1、2分别以互补倍率递推／按状态的CRT处理；r=4的旧载体迹2返回正好离开上述纤维。这三类不应被当成无关的程序例外，它们反映同一个所选计数纤维失去有效方向。

## 3. 对全部小p的有限诊断：83远非实际资源分界

为判断是缺表还是缺一般证明，进行了一个完整但有限的诊断，范围为5≤p<83的所有素数及1≤r<2p、r≠p，共1532个参数。

没有搜索平均词。对每个q∈{1,2}及来源i,j,k，先用模p方程确定v，再把输出约束消为一个整数区间。只保留能够供应两张相邻迹零表、平方系数f,g互素的来源，计算全部可用来源的gcd α和gcd H。检验的是一个已知**充分资源条件**，不是原问题的必要条件。

结果：1462个参数通过；70个不满足。对13≤p<83，失败的r恰为1、2、4；全部上半带都通过。11平均另有r=14，即旧(11,3)辅助13类型；5、7平均另有少量小容量失败。

上半带不满足本充分测试的完整列表为
\[
(p,r)=(5,6),(5,8),(5,9),(7,8),(7,9),(7,10),(7,11),(11,14).
\]
所有这些维数的原可达性早已证明。这个列表只说明当前短模板资源不足，不能解释成原问题反例。

诊断显示：很多原有限证书不是“特殊操作才存在”，而是旧公式只选了完整可行计数集合中的一条窄截面。但是“这些小例都通过”仍不是自然的全参数存在定理。本页不把1532次核验登记成一个新的统一证明，也不另保存一张逐参数根证书来替换旧表。

## 4. 最有依据的闭合路线，需要证明什么

真正缺少的是**完整可行计数集合的结构定理**，而不是继续证明固定选参截面非空。它应有三个可分开检验的部分。

### 4.1 固定纤维内先用整数移动，研究它产生的实际参数理想

对已给的真实来源、块形状与逆资源，研究全部合法输出变化；把不改变矩阵的来源替换方向商掉，再计算有效移动产生的根理想。需要证明这个理想的剩余因子只来自可说明的格指数或实际终端分类；不必先要求gcd H恰为1或2。

Smith标准形给整除障碍，Graver同号分解给同一非空有界整数纤维内的连接。这两项是可调用的成熟事实，却都不创造第二个整数点。因此必须同时检测空纤维、单点纤维，以及像理想非本原的情形。第2节是三个可直接证明的退化例子。

### 4.2 退化时允许跨格、改变来源；不用强迫同一群继续饱和

利用旧载体、新载体和带权数字M_q作为实际备选操作，保留每个候选对当前列的内容余循环及安全域。目标是把当前列送进已有深同余控制的纤维，或者直接命中零和终端。r=1、2的共同CRT已经是这一策略的完整实例。

要把它变成一般定理，须证明允许的数字能同时满足局部条件，且所需上平移步长与(1.3)的格指数相容。不能以“阿代尔各处都可选”省略同一个实际计数的全局容量，也不能假设所有数字均在整个域安全。

### 4.3 给跨纤维过程一个真正的终止保证

若必须反复改格或改来源，应有一个严格下降的良序量，或有限状态上的无坏闭类证明。可考察的是已明确的坏素数支持、局部内容深度及可行移动理想，但**它们的某个组合必下降目前未证**。不能把“可做下一步”当成“必到终端”。原始实能量虽下降，分母会变化，它单独不保证有限终止。

现有深同余精确纤维可以在达到指定有限数据时直接结束，因此不必全过程下降。最有希望的是少数可证明的准备阶段接一次精确纤维，而不是重新设计一个对所有原子单调的势。

上述三项若闭合，才能把“小p例外”改为“同一规则识别容量退化并转入另一种已证明的准备”，使数值83退出最终陈述。它们目前是明确的待证任务；本页没有声称这条路必然成功。

## 5. 阿代尔和模形式能否替代这些任务

阿代尔／局部格语言准确解释(1.1)—(1.3)、内容变化、CRT和原深同余层；它应当用来设计并验证跨格准备。经典强逼近没有原位置非负容量结论，所以不能直接证明第4.2节。

模形式已有端点theta和同余level的严格联系。但本次没有一个新的模形式定理能够保证退化计数纤维有合法出口。把路径放进Hecke对应再取分支之和，会遗忘我们要选的实际分支。若未来要借模形式，必须先建立保留这种方向和容量信息的具体对应，不能把它作为现成的闭合工具。

因此当前判断不是“所有新视角都没用”，也不是“已经找到最后一条定理”。最直接的组合是：整数纤维解释容量，局部格解释整性与本原化，按状态的CRT准备连接已有精确终端。对所有小p和全部r，**对象已经共同，资源供应和准备的全称闭合尚未共同证明**。

## 6. 核验与原文边界

[诊断脚本](../sources/research/prime_arity_padic/verify_small_parameter_resource_scope.py)将输出变量解析消元后检查有限来源；[结果](../sources/research/prime_arity_padic/small_parameter_resource_scope.json)保存失败参数及范围，不保存新路径证书。另核对3830项格剪切整性条件。一般退化结论由第1—2节手写证明承担，1532例只用于判断下一项定理该针对什么。

本次回读共同CRT、完整控制器、旧辅助13修补、统一带权核心与退化容量记录。没有开展新的外部文献检索，也不声称审定全部小基例。所有成果仅在独立研究目录，原256份冻结文档不变。

<!-- END SOURCE doc-ce510dd1fb98 -->

---

<a id="doc-aa555515ca84"></a>

## 原文导签：分散证明怎样统一：本轮框架审计与实际取得的分支合并

来源：`research/prime_arity_padic/unified_stable_range_saturation_candidate_20260916.md` · [逐字节原样副本](../sources/research/prime_arity_padic/unified_stable_range_saturation_candidate_20260916.md)

**PRIME-NATURAL-UNIFICATION · 开放问题**

原阈值已证。目标是统一2p<n<4p的初始物理资源供应；纤维比较、改变来源、状态相关准备是并列候选策略。奇数下半带已有共同反射。

**边界：** 退化出口不是唯一必经关卡；先有独立真实资源才可使用深核。共同收尾、共同形状与同一选参公式是不同强度。

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-NATURAL-UNIFICATION`）
<!-- BEGIN SOURCE doc-aa555515ca84 -->
# 分散证明怎样统一：本轮框架审计与实际取得的分支合并

2026-09-16。本页替换本轮较早、未经充分审计的框架草稿。原完成证明、历史注册及原证书均未改动。最新实质结果见[奇数下半区的共同反射铅笔](../sources/research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md)。

## 1. 必须先修正的四个判断

1. **不是只差一句“纤维出口引理”。** 已有基表真逆、有效根、无限倍率及深核是不同的前提；固定纤维的根格分类不会自动供应全部前提。
2. **固定维数不能免费改成端点。** 对固定 \(p,n\)，写 \(r=n-2p\) 后，\(r\) 已固定。要把一般 \(r\) 的状态送到类似端点的形状，必须另给实际位置转换及剩余位置处理。此前“送到 \(r=1,2,p\)”没有这样的证明，撤回。
3. **参数特殊点不等于内在奇异层。** \(r=p\) 的本原重数确实变化；\(r=1,2\) 是若干模板的边界。\(p<83\) 来自旧容量估计，不能直接称为几何奇异层。一张来源纤维退化，也不说明该维数退化。
4. **正运输是等价解释，不是现有动态证明已经执行的中间步骤。** 存在允许分母的严格正双随机运输，等价于复制足够多份后的可达。它不证明给定运输矩阵可在原位置分解。新证明只需构造某个同样归零的平均词。

这些修正使候选路线的量词更弱，也避免再用新名称包住整个旧缺口。

## 2. 已经成立的共同框架

设 \(p\) 为奇素数，\(R_p=\mathbb Z[1/p]\)，非零零和输入 \(X\) 的障碍模为
\[
\mathcal O_p(X)=
\frac{\sum_iR_pX_i}{\sum_{i,j}R_p(X_i-X_j)}.
\]
有
\[
\mathcal O_p(X)=0
\iff G(X)\text{ 为 }p\text{ 幂}
\iff \exists P>0,\ P\in M_n(R_p),\
P\mathbf1=\mathbf1,\ \mathbf1^TP=\mathbf1^T,\ PX=0.
\]
后一条件还等价于：对某个依赖输入的 \(p\) 幂复制数，每个输入坐标复制该数份后可由真实 \(p\) 平均归零。不是声称一次复制 \(p\) 份总由静态运输证明保证。

对 \(2p<n<4p\)，已有共同入口给 \((p,p,r)\) 核心。核内可用的资源有至少三种来源：

| 实际资源 | 已证明的结构 | 尚不能自动推出 |
|---|---|---|
| 固定来源、固定行列式的计数纤维 | 有效像 \((n/g)\mathbb Z\)；二维整数凸包给本原根 | 可逆基表和横向倍率对所有参数都存在 |
| 改变来源的反射族 | 本轮同一反射铅笔给奇数下半区 \(U(R)\)、\(L(nR)\) | 偶数或上半区仍有相同来源库存 |
| 有初始深核后的状态相关返回 | 互素行列式给完整有限内容分支及共同终端 | 在取得深核之前可用同样准备激活它自身 |

因此自然统一应允许改变来源。固定来源的所有纤维先分类完毕，并非必须经过的路线。

## 3. 本轮实际证明了什么

新[共同启动定理](../sources/research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md)覆盖
\[
p\ge3\text{ 为奇素数},\qquad 1\le r<p,\quad r\text{ 奇}.
\]
在 \((u,v)=(z,a-rz/2)\) 中，令
\[
\epsilon=\left((p-r)/2\bmod2\right),\quad
\alpha_0=-r,\quad \alpha_1=4-r.
\]
两张全参数位置表实现
\[
\mathcal J_\alpha=
\begin{pmatrix}
-rp/2&-\alpha\\
pn(r-2\epsilon)/4&rp/2
\end{pmatrix},
\qquad
\mathcal J_{\alpha_1}-\mathcal J_{\alpha_0}=-4E_{12}.
\]
它们各有平方为非零标量的真实周期；平方系数去掉明确共有因子后互素、奇偶相反。由两反射之商及换块，取得完整 \(U(R)\)，其中2和 \(r\) 都在倍率环中可逆。再用一个保留旧块的两步反射取得 \(L(n)\)，经已知深同余工具补成 \(L(nR)\)、\(\Gamma(n^2,R)\)，接共同终端。

这是完整证明衔接，不是只给两个矩阵：容量、真实逆、倍率环、换基损失、有限标量2、终端和入口依赖均在新文稿逐项核对。它统一 \(r=1\) 端点与全部奇数下半区，不再保留端点倍率递推，也没有83界或小参数记录。

## 4. 本轮没有证明什么

- 没有新的全部 \(2p<n<4p\) 无分支证明。
- 没有证明“所有退化来源均存在安全出口”，也没有证明该命题是必要研究目标。
- 没有减少上半区仍保留的114组资源记录。
- 没有把平均半群识别成整个算术群。
- 没有重新审核外部 Morris／Serre 定理或给高效群元素词展开。

新结果只替换奇数下半区的启动及其单独收尾。原定理覆盖范围没有扩大，改变的是证明结构。

## 5. 更具体的下一步

本轮的成功条件不是“纤维宽”，而是同时有：

1. 容量中的两张真实反射，共享一行且另一行之差为平方零方向；
2. 约去可解释共有因子后，平方系数生成可用倍率环；
3. 一个互补真实反射供应横向根；
4. 深核之后使用现成的有限对应终端。

偶数下半区首先要改变本文的非纯 \(A,B\) 来源。其三步模板的迹零同余强迫新均值用量 \(p-r/2>p-r\)，严格超过库存；因此继续在同一模板里搜索没有意义。纯来源 \(\alpha=\pm p\) 属于仍可用的旧载体返回，不被该障碍排除。可以从原全偶载体逆、\(r=2\) 的四步反演、\(r=p-1\) 的重叠构造中，寻找另一对共享行的反射，而不强求复制奇数公式。

上半区 \(r>p\) 则必须至少两次制造新值；两个相同的纯 \(A,B\) 来源因 \(p\) 奇无法并存。旧 \(C\) 参与来源后，原共同控制器中的来源参数、输出参数和格整性会同时变化。所需新命题应明确给出有界位置表的存在与共享行条件，不能只说“仍然同一反射铅笔”。

这两项是有明确失败判据的构造问题。若能统一完成，再共用已经成立的算术后半程，才可能进一步压缩整段证明。

## 6. 阅读与记录

本轮回读共同形状、共同控制器、旧载体、同行列式纤维、有界纤维几何、共同端点CRT、原端点、奇余量、偶余量、2p+2、通用算术工具和有限对应终端。没有重新列出所有旧程序样本作为新证据。

新公式、证明和核验均在[反射铅笔文稿](../sources/research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md)及其链接的独立脚本／记录中。原草稿所许诺但未实际开展的新纤维全枚举没有执行；本轮使用解析推导，再核对闭式公式和原位置平均。

<!-- END SOURCE doc-aa555515ca84 -->

---

<a id="doc-3ccbd6997b58"></a>

## 原文导签：一对边界反射统一整个奇数下半区：端点不再另作启动

来源：`research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md` · [逐字节原样副本](../sources/research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md)

**PRIME-ODD-PENCIL · 本地已给证明，未独立重审**

所有奇素数p≥3、全部奇数1≤r<p，用同一两组三步反射及两步反射取得根、深核与终端。包含r=1，无83界。

**边界：** 偶数余量、3p及上半带没有因此统一；Morris/Serre等原依赖仍保留。

**具体替代范围：** PRIME-RETAINED-BRIDGE：奇数下半带包括端点改为统一启动，不再依赖83；PRIME-ADELIC：端点与奇数内部的资源启动差异已由共同反射替代

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-ODD-PENCIL`）
<!-- BEGIN SOURCE doc-3ccbd6997b58 -->
# 一对边界反射统一整个奇数下半区：端点不再另作启动

2026-09-16。本地独立改进，不改原完成证明、冻结注册或原证书。本文从分散证明的实际位置表出发，给出一个新的共同启动构造，覆盖所有奇素数 \(p\ge3\) 及全部奇数 \(1\le r<p\)。不是新的可达范围，而是替换原来分开的端点启动与内部奇余量启动；不含 \(p\ge83\) 界或小参数表。

## 1. 定理及明确依赖

**共同启动定理。** 设 \(p\ge3\) 为奇素数、\(1\le r<p\) 为奇数，\(n=2p+r\)。在原位置核心
\[
K(a,z)=(a^p,(rz-a)^p,(-pz)^r)
\tag{1.1}
\]
上，存在显式有限局部化环 \(R\subset\mathbb Q\)，所有分母均与 \(n\) 互素，且 \(2,r\in R^\times\)，使下述作用全部有真实正向射影实现：
\[
 U(R),\qquad L(nR),\qquad \Gamma(n^2,R),
\tag{1.2}
\]
这里使用坐标
\[
u=z,\qquad v=a-\frac r2z,\qquad
A=\frac r2u+v,\quad B=\frac r2u-v,\quad C=-pu.
\tag{1.3}
\]
两张统一三步反射表和一张两步反射表提供全部初始资源。其后调用既有深同余引理、有限对应共同终端，即得全部合法核心的有限归零。接既有安全入口得到所有奇数 \(2p<n<3p\) 的完整 \(G=1\) 判据，包括 \(n=2p+1\)。

**依赖边界。** 深同余步骤引用[通用算术引理 §4](../sources/outputs/prime_arity/arithmetic_toolkit.md)中已审核的 Morris／Serre 特例；入口引用[无条件下半带入口](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)。零目标收尾调用[不扩环的有限对应终端](../sources/research/prime_arity_padic/finite_orbit_completion_without_ring_extension.md)及其独立零触发尾部。本文不以总可达性定理反推新菜单的覆盖，不重证外部群论定理，不给主同余元素的高效原子词展开。

## 2. 为什么改变来源，而不是在一张输出纤维里找第二点

旧内部奇余量证明用两个旧载体反射，其参数为 \(r,r-2\)；在 \(r=1\) 时第二个参数失效。新构造从两个等大块中先制造新载体，再只从旧载体取零份或一份参加输出。

置
\[
\epsilon=\left(\frac{p-r}{2}\bmod2\right)\in\{0,1\},\qquad
d=r-2\epsilon,\qquad
\alpha_0=-r,\quad \alpha_1=4-r.
\tag{2.1}
\]
两张表共用下面的公式。对 \(\alpha=\alpha_0,\alpha_1\)，先平均来源
\[
c_\alpha=(i,j,0),\qquad
i=\frac{p+\alpha}{2},\quad j=\frac{p-\alpha}{2}.
\tag{2.2}
\]
它从 \(A,B\) 各取 \(i,j\) 份，不使用旧 \(C\)。新均值记为 \(D\)，其中保留 \(r\) 份作为最终载体。剩余库存为
\[
\left(\frac{p-\alpha}{2},\frac{p+\alpha}{2},r,p-r\right).
\tag{2.3}
\]
取输出计数
\[
o_\alpha=(x,y,c,v_D)=
\left(
\frac{p+2r-\alpha-2\epsilon}{4},
\frac{p+\alpha-2\epsilon}{4},
\epsilon,
\frac{p-r}{2}
\right).
\tag{2.4}
\]
平均该 \(p\) 元组，再平均其余的 \(p\) 个位置，共三次平均返回同一 \((p,p,r)\) 形状。

### 2.1 对所有参数的容量证明

令
\[
s=p-r=4h+2\epsilon,\qquad h\ge0.
\]
由于 \(s\) 是正偶数，\(\epsilon=0\) 时 \(h\ge1\)。两组来源、输出及库存分别化为：

| 项 | \(\alpha_0=-r\) | \(\alpha_1=4-r\) |
|---|---|---|
| 来源 \((i,j,0)\) | \((2h+\epsilon,r+2h+\epsilon,0)\) | \((2h+\epsilon+2,r+2h+\epsilon-2,0)\) |
| 剩余库存 | \((r+2h+\epsilon,2h+\epsilon,r,4h+2\epsilon)\) | \((r+2h+\epsilon-2,2h+\epsilon+2,r,4h+2\epsilon)\) |
| 输出 | \((r+h,h,\epsilon,2h+\epsilon)\) | \((r+h-1,h+1,\epsilon,2h+\epsilon)\) |

总数都等于 \(p=r+4h+2\epsilon\)。唯一紧的比较是第二张表的第一库存：
\[
r+h-1\le r+2h+\epsilon-2
\quad\Longleftrightarrow\quad h+\epsilon\ge1,
\]
这正由 \(s>0\) 保证。第二来源的 \(j\) 非负也成立：\(\epsilon=0\) 时 \(h\ge1\)；\(\epsilon=1,h=0\) 时 \(j=r-1\ge0\)。所有其他比较直接成立。

因此这两张表在整个范围有效，连 \((p,r)=(3,1)\) 和 \(r=p-2\) 都无需额外处理。这里的 \(\epsilon\) 只是由整性决定的一位计数，不对应两套算术证明。

## 3. 两张矩阵来自同一反射铅笔

在 \((a,z)\) 基中记 \(\beta=rj\)，实际返回为 \(J_\alpha/p^2\)，其中
\[
J_\alpha=
\begin{pmatrix}
\beta&pry-p^2\epsilon+\beta v_D\\
-\alpha&-\beta
\end{pmatrix}.
\tag{3.1}
\]
迹零等式是 \(p(x-y)+\alpha v_D=\beta\)。换到 (1.3) 后，同一矩阵为
\[
\boxed{
\mathcal J_\alpha=
\begin{pmatrix}
-rp/2&-\alpha\\
pn(r-2\epsilon)/4&rp/2
\end{pmatrix}.}
\tag{3.2}
\]
它的对角和左下项均不随 \(\alpha\) 改变，且
\[
\mathcal J_{\alpha+4}-\mathcal J_\alpha=-4E_{12}.
\tag{3.3}
\]
这是一个沿平方零方向变化的反射族。它来自改变来源和输出的匹配，而非固定来源的同行列式纤维。

置
\[
F_\alpha=\frac{pr^2-n(r-2\epsilon)\alpha}{4}.
\]
有
\[
\mathcal J_\alpha^2=pF_\alpha I,\qquad
pF_\alpha\equiv p^4\pmod n.
\tag{3.4}
\]
后一式用 \(r\equiv-2p\pmod n\) 即得。因 \(p\nmid n\)，平方标量非零，且在每个危险素数处为单位。故重复每个三步返回给出其正向射影逆。

在 \((z,y_*)=(z,a+pz)\) 基中，
\[
J_\alpha\equiv
\begin{pmatrix}p^2&-\alpha\\0&-p^2\end{pmatrix}\pmod n.
\tag{3.5}
\]
因此真实返回保持合法性 \(\gcd(y_*,n)=1\)。原子中途也不可能制造不可消除的障碍，否则最终合法性不可能恢复。

## 4. 同一倍率环直接给完整上根

设
\[
c_\epsilon=\begin{cases}r,&\epsilon=0,\\1,&\epsilon=1,\end{cases}
\qquad f_i=F_{\alpha_i}/c_\epsilon,\quad i=0,1.
\tag{4.1}
\]
则 \(f_i\) 是非零整数，且
\[
\gcd(f_0,f_1)=1,\qquad
\gcd(f_0f_1,n)=1,\qquad
r\mid f_0,\qquad f_0-f_1\text{ 为奇数}.
\tag{4.2}
\]

**证明。** 若 \(\epsilon=0\)，
\[
f_0=\frac{r(3p+r)}4,\qquad f_1=f_0-n.
\]
由 \(r,p\) 与 \(n\) 互素，得到 \(\gcd(f_0,n)=1\)，故两数互素。

若 \(\epsilon=1\)，令 \(d=r-2\ne0\)，则
\[
f_0=\frac{r[pr+n(r-2)]}{4},\qquad f_1=f_0-nd.
\]
中括号被4整除，因为 \(p-r\equiv2\pmod4\)。又
\[
4f_0\equiv pr^2\pmod n,\qquad
4f_0\equiv pr^2\pmod d.
\]
这里 \(n,d\) 均奇，\(\gcd(r,d)=1\)，且 \(0<|d|<p\)，所以 \(f_0\) 与 \(nd\) 互素。奇偶性由两种情况下的差均为奇数得到。证毕。

令
\[
R=\mathbb Z[1/|f_0f_1|].
\tag{4.3}
\]
由 (4.2)，\(2,r\) 都是 \(R\) 单位；没有反演任何危险素数。

记 \(S=\operatorname{diag}(1,-1)\) 为两个等大块的角色交换。两条已有真逆的返回给出
\[
T=\mathcal J_{\alpha_1}\mathcal J_{\alpha_0}^{-1}
=\begin{pmatrix}
f_1/f_0&-2r/(c_\epsilon f_0)\\0&1
\end{pmatrix},
\]
\[
\boxed{STS^{-1}T^{-1}=U\!\left(\frac{4r}{c_\epsilon f_0}\right).}
\tag{4.4}
\]
上式根参数是 \(R\) 单位。互素性给
\[
\mathbb Z[f_1/f_0,f_0/f_1]=R.
\]
通过 \(T\) 的正反共轭及上根相加，得到全部 \(U(R)\)，包括全部负参数。这里每条形式逆都有先行标量周期，未借助尚未建立的深核。

**与旧启动的区别。** 两条相邻输出通常先给 \(U(nR)\) 或 \(U(2nR)\)；这里改变来源，直接给完整 \(U(R)\)，同时自动取得2和载体奇因子的所需倍率环。尤其 \(r=1\) 不再需要原端点取得倍率2的单独递推。

## 5. 一个两步返回给下根，深核没有循环依赖

保留 \(r\) 份旧 \(B\)，对其余位置平均两组
\[
\left(A^{(p+r)/2},B^{(p-r)/2}\right),\qquad
\left(A^{(p-r)/2},B^{(p-r)/2},C^r\right).
\tag{5.1}
\]
两个组均长 \(p\)，与保留载体不交。它们给实际矩阵 \(\mathcal K/p\)，其中
\[
\mathcal K=
\begin{pmatrix}-r/2&1\\rn/4&r/2\end{pmatrix},
\qquad
\mathcal K^2=\frac{r(p+r)}2 I.
\tag{5.2}
\]
标量非零且与 \(n\) 互素，故 \(\mathcal K^{-1}\) 正向可执行。由于 \(r,2\in R^\times\)，已有 \(U(2/r)\)，并且
\[
H=\mathcal K U(2/r)
=\begin{pmatrix}-r/2&0\\rn/4&p+r\end{pmatrix},
\qquad
\boxed{SHS^{-1}H^{-1}=L(n).}
\tag{5.3}
\]
这一步没有假设 \(p+r\) 已在 \(R\) 中可逆：\(H^{-1}\) 来自 \(\mathcal K^{-1}\) 和上根逆。

要把整数下根扩为 \(L(nR)\)，必须再给一个真实深核，不能把环系数免费加入。设
\[
P=\begin{pmatrix}1&-2\\0&n\end{pmatrix}.
\]
直接计算得，对每个 \(t\in R\)，
\[
P^{-1}U(t)P=U(nt),
\]
\[
P^{-1}\mathcal K
U\!\left(\frac{8(p+r)}r t\right)
\mathcal K^{-1}P=L(nt).
\tag{5.4}
\]
中间上根参数属于 \(R\)，不需要反演 \(p+r\)。故在 \(P\) 基里两条完整 \(nR\) 根已经实际存在。调用既有深同余引理，得到实际群包含
\[
P\Gamma(n^2,R)P^{-1}\supseteq\Gamma(n^3,R).
\tag{5.5}
\]
最后的包含由 \(P\) 和 \(nP^{-1}\) 在 \(R\) 上整直接验证。换基只是分析，没有执行 \(P\)。

现在对任意 \(t\in R\)，因全部分母与 \(n\) 互素，可取整数 \(k\) 使
\[
t-k\in n^2R.
\]
于是
\[
L(nt)=L(nk)\,L(n(t-k)).
\]
第一项由 (5.3) 的整数幂实现；第二项属于已经实际取得的 \(\Gamma(n^3,R)\)。故完整 \(L(nR)\) 成立。再次应用通用深同余引理，取得 \(\Gamma(n^2,R)\)，证明 (1.2)。

依赖顺序是：两张反射表 → \(U(R)\) → \(\mathcal K\) 和 \(L(n)\) → 换基后的深核 → \(L(nR)\) → 共同深核。没有用深核反过来制造最初的反射或倍率。

## 6. 接到共同终端，完整覆盖奇数下半区

换到
\[
(z,y_*)^T=C(u,v)^T,\qquad
C=\begin{pmatrix}1&0\\n/2&1\end{pmatrix}\in\operatorname{SL}_2(R).
\]
\(L(nR)\) 与 \(C\) 交换，\(\Gamma(n^2,R)\) 在该换基下保持。特别已有整数 \(L(n\mathbb Z)\) 和 \(\Gamma(n^2,\mathbb Z)\)。

选整数 \(k\) 满足
\[
4\mid k,\qquad k\equiv-p^{-2}\pmod n.
\]
已有上根给真实返回
\[
V=CU(k)C^{-1}
=\begin{pmatrix}
1-kn/2&k\\-kn^2/4&1+kn/2
\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z),
\]
\[
V\equiv U(-p^{-2})\pmod n.
\tag{6.1}
\]
它满足共同终端的方向条件。

共同终端还要求有限内容对应能够提供标量2。由 \(f_0,f_1\) 奇偶相反，至少一张 (3.1) 的整数矩阵有偶行列式；其条目共同 gcd 为奇数，因为左下项 \(-\alpha_i\) 为奇数。除掉条目 gcd 后，行列式仍为偶数且与 \(n\) 互素。已有 \(\Gamma(n^2,\mathbb Z)\) 因而允许调用有限内容分支定理，取得所需模 \(n^2\) 的标量2作用。

至此[有限对应共同终端 §3—5](../sources/research/prime_arity_padic/finite_orbit_completion_without_ring_extension.md)的全部前提均已落实。其全区间小单位引理对p≥5直接适用；p=3时这里只有n=7，模7单位由−1和2生成，所需补充直接成立。正向互补数字返回供应其余有限尺度，两根列修正与整数主同余纤维完成归零。可固定选终端
\[
t=\left(1,p^2-\frac{n(p-1)}2\right).
\]
在原块值中，它有
\[
A=-\frac{r(p-1)}2,\quad B=\frac{r(p+1)}2,\quad C=-p.
\]
\((p+1)/2\) 份 \(A\) 加 \((p-1)/2\) 份 \(B\) 恰为零和 \(p\) 元组。

全过程使用原位置与共同尺度；终端有限对应不要求后来数字的有理全局逆。入口和零触发尾部的依赖沿用既有独立证明，故没有把“核心有根”冒充“全输入定理”。

## 7. 对整体统一的实质影响及仍有的边界

本定理把下列范围共用同一个启动：

- \(r=1\) 的临界端点；
- 全部奇数 \(3\le r\le p-2\)；
- 包括 \(p=3,5,7,11\) 在内的全部奇素数。

不需要原端点倍率递推、原内部奇余量对合对或该范围的有限参数表。使用的环不同于旧端点的全小素数环；有限对应收尾不要求预先把所有小数字反演。

这也修正了“自然证明必须先证明退化纤维有出口”的判断。本文的两张表改变来源，根来自平方零方向的反射铅笔，并不通过固定来源同行列式纤维的二维性。所有纤维退化都先被分类，并非统一证明的必要前提。

**偶数余量的精确模板障碍。** 若 \(r\) 偶，仍坚持一组纯 \(A,B\) 来源、\(0<|\alpha|<p\) 和迹零返回，则
\[
\beta=r(p-\alpha)/2,\qquad
\alpha v_D\equiv\beta\pmod p
\quad\Longrightarrow\quad
v_D\equiv-r/2\pmod p.
\]
最小非负代表为 \(p-r/2\)，却严格大于实际库存 \(p-r\)。因此本文这个非纯来源三步模板在偶数 \(r\) 上没有所需迹零表。纯来源 \(\alpha=\pm p\) 不受上述可逆模 \(p\) 的推导约束：它们退回旧载体返回，确实可能存在迹零表；不能把此处障碍扩大成所有纯 \(A,B\) 来源或所有返回的障碍。

**上半区的容量边界。** \(r>p\) 时，一次平均仅制造 \(p\) 份新值，不能保留 \(r\) 份作新载体。两组同组成的纯 \(A,B\) 来源也不可能：需要 \(2i,2j\le p\) 且 \(i+j=p\)，与 \(p\) 奇矛盾。必须允许旧 \(C\) 参与来源，或采用另一种多阶段返回。

因此本页没有统一偶数下半区、\(n=3p\) 或整个上半区，也未消除上半区剩余的114组资源记录。它提供的是一个全参数、无小例外的完整分支合并，不是全部 \(2p<n<4p\) 的新短证明。

## 8. 阅读与核验

本轮直接对照：障碍群文稿、共同形状与整数关系、共同控制器、旧载体桥接、同行列式纤维、有界纤维几何、共同端点CRT、原2p+2完整证明、原偶余量证明、原奇余量证明、原端点控制器、通用算术引理及不扩环终端。没有在本轮开展新的外部文献检索；外部群论依赖仍引用项目原审核范围。

[核验程序](../sources/research/prime_arity_padic/verify_boundary_reflection_pencil.py)先对来源和输出作解析消元，只核对闭式公式。小范围逐位置重放完整返回，两组独立基输入同时核对全部原位置。未搜索词、未枚举群轨道，未用样本代替全称容量证明。

[结果](../sources/research/prime_arity_padic/boundary_reflection_pencil_verification.json)：138373组整数公式／容量检查，4433项精确矩阵等式，1332次原位置平均，32组大整数边界（最大 \(p=2^{61}-1\)），以及以本页新方向菜单接既有收尾的4944次有限列输送。新文稿链接均有效，原256份冻结文件未变。深同余与共同终端依赖由上文证明衔接，这些有限核验不代替 Morris／Serre 或原入口定理。

<!-- END SOURCE doc-3ccbd6997b58 -->

---

<a id="doc-28bfaf55d663"></a>

## 原文导签：深核只建一次：有限对应自动群化与不扩环的共同终端

来源：`research/prime_arity_padic/finite_orbit_completion_without_ring_extension.md` · [逐字节原样副本](../sources/research/prime_arity_padic/finite_orbit_completion_without_ring_extension.md)

**PRIME-FINITE-TERMINAL · 本地已给证明，未独立重审**

已有真实深核，行列式与控制模数互素时，有限正向对应轨道等于明确有限群轨道；终端无需反复扩环。

**边界：** 不供应初始根与深核；共享坏因子的行列式不自动覆盖。

**具体替代范围：** PRIME-RETAINED-BRIDGE：统一已有深核后的终端接口，取消逐数字取逆／扩环要求

[完整前提与核验](../EVIDENCE.md)（搜索 `PRIME-FINITE-TERMINAL`）
<!-- BEGIN SOURCE doc-28bfaf55d663 -->
# 深核只建一次：有限对应自动群化与不扩环的共同终端

2026-09-16。本地独立简化。接[有界纤维几何与内容对偶](../sources/research/prime_arity_padic/global_structure_and_bounded_fiber_geometry_20260916.md)第7.3—7.4节。本页不重新寻找原位置根表，而将该内容分支结论接成一个完整终端定理，取消已有深核之后的普遍有理逆激活和反复扩环。

**结果。** 对与控制模数互素的行列式，有限正向对应的轨道恰等于一个明确有限群的轨道。有限逆和所需尺度均由内容准备实现。应用于共同(p,p,r)核心后，只须保留最初的整数下根与深同余核，以及粗略方向；所有后续安全数字只使用正向物理返回。最终直接到整数本原终端，不要求扩大R或证明R单位在更深模数上满射。

**没有证明：**所有小p、所有r都能按一套无需有限证书的规则取得初始根和深核。若控制模数仍含额外因子，与它不互素的行列式也未被本页自动解决。83不是本页终端算法的限制，但不能因此从物理供应定理中删掉83。

## 1. 正向有限对应的准确群化

设Q≥2，X是Um₂(Z/Q)模共同正负号中的一个有限状态集，且在所有单位标量下不变。其元素记录某个固定原位置核心的合法整数本原列。假设：

- Γ(Q,Z)已有独立证明的真实正向射影实现；
- A₁,…,A_s是有真实原位置词的整数满秩返回，先除掉条目共同gcd；
- d_i=|det A_i|与Q互素，且A_i模Q保持X。

已有内容分支定理给每个x的完整对应
\[
\mathcal R_i(x)=\{g^{-1}A_ix\pmod Q:g\mid d_i,\ g>0\}.
\tag{1.1}
\]
每个分支都能由“先在Γ(Q,Z)纤维内准备，再执行原A_i”真实提升。单位标量、形式逆均尚未假设有物理实现。

**有限轨道群化定理。** 定义
\[
H_Q=\left\langle A_i\bmod Q,\ \ell I\bmod Q:
\ell\text{素且 }\ell\mid\prod_i d_i\right\rangle
\subseteq\operatorname{GL}_2(\mathbb Z/Q).
\tag{1.2}
\]
由这些实际正向对应从x可达的集合，恰为H_Qx。特别地，同一轨道内的有限反向移动总可正向完成；这个结论只在有限本原标记上成立，不宣称A_i在有理核心上有一条固定的正向逆词。

**证明。** (1.1)中的每条分支为g⁻¹A_i，是X上的置换且属于H_Q。反向包含分两步：内容1分支给A_i；有限置换的逆是其正幂，所以A_i⁻¹也在正向对应半群中。若m_i是A_i模Q的一个阶，则一次g分支后再做m_i−1次内容1分支，模Q作用恰为g⁻¹I。取g=ℓ给ℓ⁻¹I，再取其有限阶的正幂给ℓI。因此H_Q的全部生成元及逆均有有限正向对应词。证毕。

可以取m_i=|GL₂(Z/Q)|作统一有限上界，用快速幂计算模矩阵；这不保证展开后的平均词短。每次分支都在当前模Q纤维内重新准备，不要求原来那个整数提升被保持。

这是第7.4节有限尺度公式的整体轨道版本。在与Q互素的行列式部分，有向性已经转化为明确有限群作用，无需再对这部分证明额外的“没有非终端闭分量”定理。仍须证明这些群轨道命中终端。

## 2. 为什么可以始终只用原整数深核

对于满秩整数A和本原列v，gcd(Av)整除|det A|。因而输出本原列modQ由v modQ|det A|决定。给定某个分支所需的本原剩余类z modQ|det A|，取它的本原整数提升w。若当前v≡w modQ，精确纤维引理给
\[
\gamma\in\Gamma(Q,\mathbb Z),\qquad\gamma v=w.
\]
随后执行A并分析其整数本原代表。全过程共同尺度可能改变，但原输入的全部位置共同参与所用核心，不涉及外部位置的免费缩放。

最初若已有Γ(Q,R₀)，当然已有其子群Γ(Q,Z)。之后不需要把新增det A的素因子加入R₀，也不需要在每次扩环后重做横向根与深核包含。有限内容分支承担的是有限剩余尺度；其物理词按当前状态准备，不是统一线性放大。

模Q合法性必须能由本原列判断，A_i还必须保持所讨论的合法域。这些条件在下面的共同核心中逐项验证。对不保持整个域的矩阵，或者gcd(d_i,Q)>1的矩阵，不能套用第1节的群化结论。

## 3. 共同核心的前提可以进一步减弱

设p≥3为奇素数，n=2p+r、1≤r<2p、r≠p，采用
\[
K(a,z)=(a^p,(rz-a)^p,(-pz)^r),\qquad y=a+pz,
\]
合法本原列为(z,y)，gcd(y,n)=1。令δ=gcd(n,2)、h=δn、Q=h²。

本页终端定理只要求先独立取得：

1. 在(z,y)基中全部L(hk)、k∈Z，以及Γ(Q,Z)，均真实正向可执行；
2. 一组条目本原的满秩整数返回，各行列式与Q互素且模Q保持合法状态集，使第1节有限轨道群（连同本页第4节明确给出的数字返回）中包含某个V满足
   \[
   V\equiv\begin{pmatrix}1&-p^{-2}\\0&1\end{pmatrix}\pmod n;
   \tag{3.1}
   \]
3. n奇时，该有限群还包含标量2I。这可由任意一张条目本原、行列式为偶数且与n互素的真实返回供应；n偶不需要2。

这里V只需是一项可执行的有限标记动作，不要求它在Q上提升成同一有理V的全域真逆。初始资源仍须由已证根、深群定理或独立周期落实，不能使用本页结论反过来证明前提1。

现有共同反射资源已经满足这些条件：若规范反射J/p²模n的步长为−α/p²，用换块和整数Bezout在模n合成(3.1)。只为有限方向，需要的是gcd(n,α₁,…,α_s)=1；取得深核所需的横向条件仍另行核对。J的公因子若非1，它至多为|α|<p且与n互素，所需有限规范尺度可由下一节的小数字提供。旧载体对合用J/p，分母同样只需p。

当n奇，现有相邻反射中选择奇α，平方系数f、g的奇偶相反。对互素平方系数族，奇α还使偶行列式那张表的条目共同gcd为奇数；去掉它后仍有偶行列式，故条件3不增加新的计数要求。其他启动族需明确指出条件3的来源，而不能默认2可用。

## 4. 安全小数字现在只需要正向实现

对任意奇q、1≤q≤p，保留C，平均两个互补p组，给实际返回P_q/p，其中
\[
P_q=\begin{pmatrix}q&r(p-q)/2\\0&p\end{pmatrix}
\quad\text{在}(a,z)\text{基中}.
\tag{4.1}
\]
gcd(q,n)=1时，det P_q=pq与Q互素，并且y'≡qy modn。故整数代表保持合法域。q<p时P_q条目本原，内容分支供应p以及q全部素因子的有限尺度；q=p时返回恒等，但有限尺度p已由P₁的行列式提供。

于是所有安全奇数字q≤p及p的有限标量作用均可用。n奇时再用前提3取得2，便覆盖全部安全整数q≤p。由已证的全区间小单位引理，所生成有限标量群在模n单位群上的像满射。这里只要求modn满射，不要求其在modQ满射，也不宣称这些数已成为原R₀单位。

在有限矩阵群中，P_qP₁⁻¹及标量q⁻¹给
\[
D_q=\begin{pmatrix}q^{-1}&0\\
\frac n2(q^{-1}-1)&1\end{pmatrix}\quad\text{在}(z,y)\text{基中}.
\tag{4.2}
\]
当n偶、q奇，n/2为整数且q⁻¹−1可写为偶整数除以q，故D_q保持y modn、将z乘q⁻¹。式(4.2)只在有限群中合成；没有调用P₁或P_q的有理正向逆。

n偶时总有安全奇q≤p且q≡3或5 mod8。p≥11由[已证数字引理](../sources/research/prime_arity_padic/split_torus_completes_all_directions.md)第2节；p=5、7时若3、5都不安全，偶n须被30整除，与n<4p≤28矛盾；p=3只需n=8、10，q=3即可。−1和q生成全部有限二进单位，因此终端算术本身对p=3、5、7也没有缺口。它不提供这些小p所需的初始深核。

## 5. 不扩环的完整终端过程

所有步骤在有限本原列modQ上执行，每个群动作由第1—2节提升为真实正向路径。始终按当前实际输出选择整数本原代表，不要求保持某个R₀本原代表。

### 5.1 模n准备

给定合法(z,y)，取
\[
k\equiv p^2zy^{-1}-1\pmod n.
\]
作用V^k，使z≡y/p² modn。由第4节，选一个可用有限标量s，其模n为z⁻¹；作用后有
\[
(z,y)\equiv(1,p^2)\pmod n.
\tag{5.1}
\]
s在modQ的具体值由小数字乘积决定，不随意假设任意模Q单位都可用。

### 5.2 偶数地方先匹配首坐标

写n=2ᵃm、m奇。令b=h/m=2^(a+1)、M=b²。选择−1与第4节q的幂，使其乘积模M等于当前z；执行相应D_q及−S，将z变为1 modM。y仍为p² modn。

V模2为非平凡上幂零，所以V^M≡I modM；不需要tr V≡2 mod4。使用V的M倍次数在模m处调整z为1，保持完整二进精度。于是z≡1 modh，y≡p² modn。

n奇时h=n，(5.1)已足够，跳过此步。

### 5.3 选终端代表并修正两项误差

真实终端列仍是
\[
t_j=(1,p^2-nj),\qquad
\max(0,\lceil(p-1-r)/2\rceil)\le j\le(p-1)/2.
\tag{5.2}
\]
对应j+1份A、j份B及p−1−2j份C的零和p元组。n奇只需一个j；n偶时r为正偶数、r≥2，区间包含两个连续j，足以选中任意j mod2。选择j使当前列与t_j模h相同。

在有限环中令E=E₂₁、X=VEV⁻¹。模n时
\[
Et_j=(0,1)^T,\qquad Xt_j=(-2/p^2,2)^T.
\]
故两列的行列式为2/p²，是n奇数部分的单位。只用已有整数根L(hk)及其**有限**V共轭，就能解一次二维线性同余，将当前列修正到t_j模m²。参数通过CRT取成在完整二进模M下恒等。

n偶时首坐标已为1 modM，再用一次L(hk)匹配第二坐标模M，且令k≡0 modm保留m²部分。最终
\[
v_{\mathrm{out}}\equiv t_j\pmod Q.
\]
当前真实列取整数本原代表后仍满足此式，t_j也整数本原。只用最初已经真实取得的Γ(Q,Z)，精确送到t_j；再平均对应零和组并接独立已证尾部，完成归零。

这里不需要选择一个R₀单位ε，更不需要证明ε在所有高阶模数上存在。有限标量的状态相关路径已经完成所需modn尺度准备，精确终点则选固定整数本原列t_j。

## 6. 这实际删除了哪些依赖

对满足第3节资源前提的分支，可以将原终端阶段替换为本文，删除下列步骤的使用：

- 在得到初始深核后，为每个安全F_q证明有理正向逆的Smith—CRT夹乘；
- 将p、小数字及方向返回的新增行列式素数逐一加入根参数环；
- 每次扩环后重新取得同一level的深同余群；
- 为后续返回始终维持同一个GL₂(R)本原列模型。

最初用于造根、造无穷单位及建立Γ(Q,Z)的真实周期、倍率和Morris／Serre步骤仍保留。本文只删去**深核已取得之后**的扩环，不宣称所有扩环都多余。格对应所用Γ(Q,Z)的词可能很长，本页不保证算法比原方法更快；简化的是证明依赖与前提。

这将“整数格自同构”与“单向格对应”接在同一有限终端过程中。它也解释了为何r=2的状态相关CRT是自然的：本原内容可以承担有限尺度准备，不必要求所有后继都属于一个固定可逆环上的群。

### 6.1 接上本轮几何文稿的具体实例

在p=43、r=65、n=151的二维同行列式纤维中，原几何文稿已用两条比较得到U(151/15)，相邻倍率给R₀=Z[1/(2·3·5·11)]。α=15在R₀可逆，故原横向根论证提供Γ(151²,R₀)，从而有Γ(151²,Z)和整数所需根。

这里J的规范矩阵还含p=43分母；传统收尾要先激活43以及全部小数字，再保持GL₂(R)。本文只把J和其他实际数字看作安全有限对应。J的条目gcd为5，相邻反射的条目gcd为3，均为已可由安全数字供应的有限尺度；其本原行列式都与151互素，而且相邻本原反射有偶行列式，提供2。

一个反射乘换块的模151平移步长为−15/p²，取15的模151逆次幂即可得到(3.1)。然后直接执行第5节。故这个几何实例接成终端时，不需要再扩R₀，也不需要取得所有新增数字的有理逆。没有把重新解决该固定维数当成全部参数定理，它用于核对几何资源与新弱接口确实衔接。

## 7. 仍然不能删掉什么

若初始根理想有额外因子，深核模数Q包含不除n的素数，则某些P_q行列式可能与Q不互素；这时内容分支可能改变方向，不能照搬第1节的置换群化。本页没有证明这些坏地方都能安全退出。

同样，第3节的根、深核及粗略方向还须由实际有限库存提供。二维整数凸包定理让本原根更容易取得，但旧很多选定纤维仍是单点；本页不证明每个p,r总有另一个丰富纤维。

因此新的准确局面是：**在已经取得同余深核且后续行列式与它互素的部分，终端理论可以整体删除后期扩环与真逆激活。** 剩余统一任务更集中在初始资源和与Q共享因子的退化对应，而不是重新证明安全单位数字的全部有理可逆性。

## 8. 验证与文件边界

[核验器](../sources/research/prime_arity_padic/verify_finite_orbit_completion_without_ring_extension.py)执行3750项基础有限输送及几何实例的12项输送，共3762项；构造3494项安全小数字标量词；60次非单位内容的精确准备均给出整数Γ(Q,Z)矩阵证据，再实际重放120次互补平均；另核对846项有限数字乘法身份。

有限终端包括p=3、5、7的算术条件检查，但其中使用的抽象V只是检验条件定理，不作为这些参数的物理启动证书。另有来自当前共同构造的实际V和p=43几何实例，明确接已有资源。没有搜索平均词、枚举大模群或从有限检查推断无限群包含。

[结果](../sources/research/prime_arity_padic/finite_orbit_completion_without_ring_extension_verification.json)全部通过。原256份完成文稿、索引和注册保持不变；本页不改写其他AI的几何调查，新增成果仅在独立目录。

<!-- END SOURCE doc-28bfaf55d663 -->

---

<a id="doc-f496eaf9576b"></a>

## 原文导签：为什么三平均的精确阈值是七：资源边界、有限周期与合法单轨道

来源：`outputs/prime_arity/examples/seven_exact_threshold_structure.md` · [逐字节原样副本](../sources/outputs/prime_arity/examples/seven_exact_threshold_structure.md)

**SEVEN-STRUCTURE · 原证明已完成（沿用登记，非本次重审）**

两步安全入口、三种实际返回的标量周期、根群与八陪集改写、合法单尖点轨道和四步尾部。

**边界：** 七元作为全系统才共享目标均值；嵌入较大系统不可免费当作全局射影逆。

[完整前提与核验](../EVIDENCE.md)（搜索 `SEVEN-STRUCTURE`）

旧核验ID：`seven-endpoint-structure`
<!-- BEGIN SOURCE doc-f496eaf9576b -->
# 为什么三平均的精确阈值是七：资源边界、有限周期与合法单轨道

日期：2026-09-12。

同日后续：[统一正向控制器](../sources/outputs/prime_arity/tools/uniform_endpoint_positive_controller.md)已通过第二种“保留单点”返回、仿射配对、必碰偶数的整数链及欧拉周期，证明每个奇数平均元数的安全返回都有正向逆，并取得完整局部化上下根。第6节在q=2p+1为素数时的充分条件现已无条件实现；合数q的全输入入口与轨道仍需另证。本页保留七元的独立短周期证明和特定扫掠的谱分界。

本页区分两件事：为什么六元尚有反例，以及为什么七元已经能够处理全部合法输入。
前者由位置资源与三进障碍解释；后者需要真实操作的精确代数关系。
它们不是同一个论断，不能只凭“多了一个缓冲位置”就宣称充分性。

## 1. 六到七的边界是实际的资源变化

六元输入

\[
(-3,0,0,1,1,1)
\]

零和、本原，G=1，却不可达。
唯一非恒等整数三平均得到 (-1^3,1^3)，产生模 2 的非零共同余数障碍。
而对至多六个位置，成功路径不能引入新三进分母：首次产生的最低三进层恰为三个相等位置；后续部分相交会使这一非零最低层继续下降，完全不相交则在六元处形成两个相反常值块，仍受模 2 障碍限制。

加入第七个零后，形成两个相反三重块加一个单点零，三个 (-1,1,0) 就可以逐对消去。
因此 6 和 7 的区别确实存在于原位置的操作能力中。

但这仅给出阈值下界和一个收尾机制。要解释七元全部输入的充分性，还需下面的两层结构。

## 2. 七元恰好容纳一个完整的双块载体系统

考虑

\[
(u^3,v^3,w),\qquad3u+3v+w=0.
\]

令 d_1=u-w、d_2=v-w。
平均载体 w 和某个三重块中的两个位置，旧块剩余的那个位置成为新载体。
两个真实操作对差值的作用为

\[
E_1=\begin{pmatrix}-1/3&0\\-1&1\end{pmatrix},\qquad
E_2=\begin{pmatrix}1&-1\\0&-1/3\end{pmatrix}.
\]

依次交换两块，得到

\[
E_2E_1=\frac13 V_3,\qquad
V_3=\begin{pmatrix}2&-3\\1&-1\end{pmatrix}.
\]

这个矩阵满足

\[
\chi_{V_3}(t)=t^2-t+1,\qquad V_3^3=-I.
\]

故六次正向原子平均构成精确关系

\[
\boxed{(E_2E_1)^3=-\frac1{27}I.}
\tag{1}
\]

循环旋转这个正词并删去首字母，可以正向实现每个 E_i 的射影逆。
这里不是倒放平均或拆分坐标；逆是由另外五次正向三平均组成的。

还有一个关键点：这七个位置就是整个系统，其均值正是目标零。
因此差值整体缩放会使整个状态整体缩放。
如果把同样七个位置当作更大系统中的一个窗口，通常只能得到围绕该窗口自身均值的收缩，不能直接当成整个系统的射影逆。
这解释了七元局部机制为何精确有效，也解释了它不能未经处理地拼接到所有更大维数。

## 3. 同一载体机制在一般 p 上有明确的谱分界

对一般素数平均元数 p，两个 p 重块加一个单点仍产生

\[
E_1=\begin{pmatrix}-1/p&0\\-1&1\end{pmatrix},\qquad
E_2=\begin{pmatrix}1&-1\\0&-1/p\end{pmatrix},
\]

所以

\[
pE_2E_1=V_p=\begin{pmatrix}p-1&-p\\1&-1\end{pmatrix},
\quad\det V_p=1,\quad\operatorname{tr}V_p=p-2.
\]

其特征多项式与判别式为

\[
t^2-(p-2)t+1,\qquad p(p-4).
\]

- p=2：特征值为四次单位根，V_2²=-I。
- p=3：特征值为六次单位根，V_3³=-I。
- p>=5：特征值为互为倒数的不同正实数，V_p 没有有限射影阶。

因此三平均七元的六步关系来自一个准确的有限周期，确实带有小素数特性。
它不是“所有 p 都会有相同周期”的迹象。

反过来，这也不是 p>=5 的不可达障碍：五平均十一元已经通过额外跨块返回获得另一组正向周期并解决全部合法输入。
有限周期的具体来源可以改变，但必须实际构造。

## 4. 给七元补上一份不依赖十八词覆盖的结构证明

先说明全输入入口。任意七元合法整数零和输入，保留一个单点 c，将其余六个位置分成两个三元块。
若其中一块和为 S，平均后的块值差为 (2S+c)/3。
若它模 7 为零，交换两块中一对模 7 不同的值，就把这个差变成模 7 非零。
这样的跨块差异必存在，否则原七个值模 7 全同余。
因此两次三平均就能进入合法

\[
K_3(a,b)=(a^3,b^3,-3(a+b)).
\]

### 4.1 三个有原位置账本的返回

对 j=1,2,3，依次平均

\[
(a^{j-1},b^{3-j},-3(a+b)),\qquad
(a^{3-j},b^j).
\]

输出为 K_3(c,d)，其中

\[
c=-\frac{(4-j)a+jb}{3},\qquad
d=\frac{(3-j)a+jb}{3}.
\]

令 x=a、y=a-b，射影矩阵与块重标记为

\[
T_j=\begin{pmatrix}-4&j\\-7&2j\end{pmatrix},\qquad
\Sigma=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
\]

真实 T_j 带共同因子 1/3；Σ 只是将两个块的名称互换，后续原下标账本随之更新。
合法性为 7 不整除 y，全部 T_j 和 Σ 都保持它。

七本身为素数也在这里发挥了作用：1<=j<=3 的全部行列式 -j 都在模 7 下可逆，所有这些跨块返回都能用于整个合法域。

### 4.2 三个精确正向周期

直接矩阵恒等式给出

\[
\boxed{T_2^2=2I,\qquad(\Sigma T_1)^3=-I,\qquad
(\Sigma T_3)^6=-27I.}
\tag{2}
\]

每个字母都处于一个正向标量周期中，所以全部 T_j 的射影逆均有正向平均词。
这一步提供的是确实可执行的群，不是假定平均可逆。

### 4.3 生成完整局部化根与同余群

记 Δ(t)=diag(1,t)，U(t)=E12(t)，L(t)=E21(t)。
有

\[
T_1^{-1}T_j=\Delta(j),\qquad
\Sigma\Delta(2)\Sigma\Delta(2)^{-1}=U(1/2),
\]

\[
\Sigma U(1)=\Delta(-1),\qquad
T_1U(1/4)\Delta(-16)=-4L(7/4).
\tag{3}
\]

由整数幂与对角共轭，得到 R=Z[1/6] 上的全部

\[
U(R),\qquad L(7R),\qquad\Delta(R^\times).
\]

这些都是由 (2)--(3) 编译的正向三平均词。
R 中出现二分母，是射影作用带共同缩放的结果，不是在实际操作中加入二平均；实际坐标仍只有三进分母。

对 Γ₀(7)，有符号右陪集代表为

\[
I,\qquad\mathsf S\mathsf T^j\quad(-3\le j\le3),
\]

其中 𝕊=[[0,-1],[1,0]]、𝕋=U(1) 仅用作模群的代数生成元。
全部非平凡 Schreier 回路为 U(1)、L(-7)，以及

\[
g_j=\begin{pmatrix}-k&-1\\jk+1&j\end{pmatrix},
\quad k\equiv-j^{-1}\pmod7,\quad0<|k|\le3.
\]

每个 g_j 都有分解

\[
g_j=L\!\left(-\frac{jk+1}{k}\right)
\operatorname{diag}(-k,-1/k)U(1/k).
\]

所有主元 k 在 R 中可逆。因而可执行群包含完整 Γ₀(7)，不需十八个下降词的实区间覆盖证书。

### 4.4 合法单轨道与归零

对本原整数列 (x,y)，7 不整除 y。取 αx+βy=1，再将 α、β 调整为 α+ky、β-kx，使 7 整除 α。
于是

\[
h=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}\in\Gamma_0(7),
\qquad h(x,y)^T=(0,1)^T.
\]

所以所有合法方向都可经正向平均到某个非零缩放的 K_3(0,-1)。
先平均 (3s,0,0)，再三次平均 (s,-s,0)，四步归零。
结合全输入入口，这是一份完整的七元充分性证明。

这里明确使用了正向逆、完整根群、全部陪集回路和终端，不能只把其中的有限周期单独称作充分性证明。

## 5. “七是阈值”的三层含义

七元可以解释为三层机制恰好同时具备：

1. 位置层：两个三重块外第一次可以保留一个独立位置，六元的非零相反块陷阱因此可以被打破。
2. 动力层：这个全系统载体窗口具有精确正向周期，实际返回可形成可逆的射影控制。
3. 算术层：加入明确跨块返回后，真实群足以覆盖唯一合法有理轨道，并且该轨道有原位置终端。

必要边界由第一层解释；充分性需要第二、三层。
仅有一个零或缓冲位置，不自动保证任意输入都能造零；仅有周期，也不自动保证全部合法轨道相通。

此外，“七元全部可解”并不独自证明 N(3)=7。
完整阈值还要结合已证八、九、十元，以及 n>=11 的统一不变量定理。
六元反例与这些充分性结果共同给出最优统一阈值 N(3)=7。

## 6. 一条可检验的精确端点充分条件

对任意奇素数 p，若 q=2p+1 也是素数，同一族两步返回在 (a,a-b) 坐标中为

\[
T_j(p)=\begin{pmatrix}-(p+1)&j\\-q&2j\end{pmatrix},
\qquad1\le j\le p.
\]

这些返回无条件存在于原 q 个位置上，实际带因子 1/p。
如果能够为它们构造正向射影逆，则

\[
T_1^{-1}T_j=\Delta(j),
\]

以及与 (3) 同型的公式给出 R=Z[1/p!] 上的 U(R)、L(qR) 和对角单位。
其中下根来自

\[
T_1U\!\left(\frac1{p+1}\right)\Delta(-(p+1)^2)
=-(p+1)L\!\left(\frac q{p+1}\right).
\]

p+1 的素因子不超过 p，所以所有系数都在 R 中。
Γ₀(q) 的有符号 Schreier 主元绝对值至多 p，因而同一完整生成与轨道证明直接适用。
单素数维数的两步入口及含零终端随后解决该端点。

这是一条准确的充分路线：p=3 和 p=5 的正向逆已经分别由不同的明确周期构造出来。
它不是所有 p 的已证定理，也不声称这些逆是可达性的必要条件。
q 为合数时还存在多素数入口问题，不能略去该前提。

还有一个更直接的合数边界：若素数 r 整除 q=2p+1，并且 r 整除 j，则 T_j 的输出满足 y'=0 mod r。
当输入 x 是模 r 单位时，x'=-(p+1)x+j y 仍为单位，因为 gcd(p+1,2p+1)=1。
输出因此在原位置上全部成为同一个非零模 r 余数，不能归零。
所以 q 为合数时，不能无条件采用全部 j=1,...,p 的返回。
7=2*3+1 与 11=2*5+1 都是素数，使它们在这方面共有同一个简洁合法域；15=2*7+1 已不同。

这说明精确端点不必通过不断压低 4p 的常数才能到达；它可以由单独的结构定理直接闭合。
但当前仍缺对全部素数平均元数统一成立的端点机制，以及从端点到临界维数带全部维数的覆盖。

## 7. 核验职责

程序独立重放三个七元返回、三条周期、正向逆和根公式，核对 Γ₀(7) 的完整八陪集及六个有符号回路。
一般公式通过精确矩阵恒等式检查；有限参数实例仅用于防止账本和符号错误。
此证明不导入或运行旧十八词实覆盖程序，也不使用有限深度搜索来声称无限轨道覆盖。

本轮核验：六个平均元数下的双块扫掠与谱公式；三个七元返回及三条精确周期；十三组根与对角种子恒等式；八个陪集、六个有符号回路和全部 24 条标准生成元转移；十条直接 Fraction 原位置归零路径，最长 338 次原子操作。

项目入口：`python work/run_verifications.py --id seven-endpoint-structure`。

<!-- END SOURCE doc-f496eaf9576b -->
