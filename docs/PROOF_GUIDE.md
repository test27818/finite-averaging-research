# 证明思路与审核路径 / Proof strategy and reviewer map

[中文首页](../README.md) · [English](../README.en.md) · [核验 / Verification](VERIFICATION.md)

本文是证明的导航与结构说明，不替代所链接的一般论证。项目是研究证明与证据档案，不是Lean、Coq或Isabelle形式化，也不能把归档内“独立审核”理解成外部同行评审。

This guide explains the architecture and routes reviewers to the actual arguments. It is not a formalization or a replacement for the proofs; internal audit notes are not external peer review.

## 先核对量词 / First fix the quantifiers

$k$ 为每次平均的位置数，$n$ 为总位置数。非全等输入中心化并取本原整数代表 $X$；$G$ 是坐标差的gcd。全等输入用空操作序列完成。

Here $k$ is the operation arity and $n$ is the number of fixed positions. For nonconstant input, $G$ is computed after centering and primitive integer normalization.

| 结论 / Claim | 范围与状态 / Scope and status | 主要正文 / Primary source |
|---|---|---|
| 二平均 / Binary | $n\ge4$, iff $G=2^e$；$n=3$另分类 / separate classification | [原文复核 / Source review](../archive/2026-09-07/3-3-triple-average-research-note/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md) |
| 三平均 / Ternary | $n\ge7$, iff $G=3^e$；主体$n\ge11$接小基例 / direct proof plus small bases | [双三重值证明 / Repeated-value proof](../archive/2026-09-07/3-3-triple-average-research-note/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md) |
| 奇素数 / Odd prime | $n\ge2p+1$, iff $G=p^e$；最终阈值最优 / optimal final threshold | [总证明 / Consolidated proof](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/proof.md) |
| 任意元数端点 / General endpoint | 全部$k\ge2$的$n=2k+1$；不等于全部后续$n$ / endpoint only | [最新一般元数交接 / General status](../archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_three_tasks_progress_20260915.md) |
| 任意元数宽尾部 / General tail | $k\ge3,\ n\ge4k-1+d_k(n)$，iff $\operatorname{rad}(G)\mid k$ | [线性阈值 / Linear threshold](../archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/arbitrary_arity_linear_threshold.md) |
| 平方与部分素数幂 / Squares and selected prime powers | 指定早期临界维数，部分结果依赖GRH / specified critical dimensions, GRH where stated | [条件性结果 / Conditional results](../archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md) |

其中 $d_k(n)$ 是整除$n$但不整除$k$的不同素数个数。只有$p\nmid n$时，素数判据可简写为$G=1$。当前总状态优先于历史稿的日期性“未解”叙述。

Here $d_k(n)$ counts distinct primes dividing $n$ but not $k$. The shorthand $G=1$ is valid for prime arity only when $p\nmid n$. Current status takes precedence over dated statements in historical notes.

## 两条成功证明机制 / Two successful mechanisms

### 二平均与三平均直接证明 / Direct binary and ternary proofs

共同思路是保存“继续操作所需的资源”：两个不同的重复值、每个危险模数下的非恒定见证，以及整数格。二平均每个值重复至少两次；三平均直接证明要求两个不同值各至少重复三次。

The invariant preserves repeated values, nonconstant residue witnesses at dangerous primes, and integrality. Two distinct repeated pairs suffice in the binary method; the direct ternary method maintains two distinct values of multiplicity at least three.

选择平均时必须证明重数和见证都保留，或直接进入可明确处理的终端。对非恒等整数操作，

$$
\sum_i x_i^2-\sum_i(x'_i)^2
=\sum_{i\in S}(x_i-\bar x_S)^2>0.
$$

离散能量保证有限终止。三平均主体先整体乘3以预留一位精度，再在整数格上操作；其计数余量适用于$n\ge11$，7、8、9、10用独立基例。整数能量下降本身不是输入位长多项式复杂度证明。

Each nontrivial integer averaging step strictly decreases the discrete quadratic energy. The ternary proof first reserves one extra ternary precision digit, then stays on an integer lattice. The uniform invariant uses $n\ge11$; dimensions 7–10 are separate proved bases. Discrete descent alone does not imply a polynomial bit-complexity bound.

### 临界素数范围的算术路线 / Arithmetic route near the prime threshold

~~~mermaid
flowchart TD
    A["合法输入 / Eligible input"] --> B["安全压缩到加权核心 / Safe weighted-core entry"]
    B --> C["原位置返回与正向逆 / Physical returns and positive inverses"]
    C --> D["根参数理想与单位环 / Root ideals and localization"]
    D --> E["深同余纤维 / Deep congruence fibers"]
    E --> F["有限方向与尺度修正 / Finite direction and scale correction"]
    F --> G["精确零和终端 / Exact zero-sum terminal"]
    G --> H["造零及收尾 / Zero creation and completion"]
    X["Morris / Serre external theorems"] --> E
~~~

| 步骤 / Step | 必须核对 / What to verify | 正文入口 / Source |
|---|---|---|
| 安全入口 / Safe entry | 所有危险素数处见证保留；作用于原$n$位置 / preserve witnesses on original positions | [下半带入口](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md) |
| 返回与逆 / Returns and inverses | 完整核心上的$WE_\pi=\lambda E_{\pi'}M$；非负计数与真实逆 / full image, nonnegative counts, executable inverse | [通用引理§2](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/arithmetic_toolkit.md) |
| 根与局部化 / Roots and localization | 参数理想足够；约分后的倍率才提供分母 / actual root ideal and denominator resources | [九偏移§5–6](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md) |
| 深核 / Deep kernel | 外部定理前提及换基level损失 / theorem hypotheses and change-of-basis losses | [外部定理审核](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md) |
| 有限终端 / Finite terminal | 同时保留方向和许可单位尺度 / direction plus allowed unit scale | [浅层提升](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md) |
| 精确收尾 / Exact completion | 有限类相符后由精确纤维到有理终端 / exact fiber lift after finite matching | [通用引理](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/arithmetic_toolkit.md) |
| 维数覆盖与下界 / Coverage and lower bound | 全部区间无遗漏；$2p$不可达例 / all ranges and the $2p$ obstruction | [总证明§4–5](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/proof.md) |

给出一个抽象可逆矩阵不等于有正向平均实现；只到达合法核心也不等于终止。主证明的每个区间都要把这一整条链闭合。更远的整数能量尾部仍可直接下降，不要求每条路线都构造完整同余群。

An abstract inverse does not provide a positive averaging word. Reaching a legal core does not prove termination. Each dimension range must close the entire chain. Large-dimension integer-energy arguments may terminate directly and need not construct an entire congruence group.

## 哪些证书仍在证明里 / Remaining certificate dependence

九偏移$n=3p+s,\ 1\le s\le9$中，$p\ge83$用统一计数公式；$11\le p<83$保留162组物理返回／根理想证书及两个局部修补。这不是整个项目所有有限证据的总数。

For the nine offsets, a uniform formula handles $p\ge83$, while 162 small-prime cases and two local repairs remain. That count is not the total amount of finite evidence in the whole proof.

原内部偶余量还有64／256类二进轨道表。2026-09-16的[统一二进列引理](../archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/structural_reassessment_and_uniform_dyadic_orbits.md)以三个已有返回的平方、交换子和逐层提升替代这两表；它保留尺度，仍依赖旧已证明的真实返回与逆。原文和注册冻结，所以复现原18项profile仍会运行旧表，新引理另作一项检查。

The independent dyadic lemma replaces two orbit tables by identities and induction, including scale. The archived profile remains frozen and still checks the old tables; the new proof has a separate verifier. It does not remove the nine-offset physical certificates.

## 如何提出可核对的异议 / Reporting a checkable concern

请指出文档路径与章节、具体命题及参数条件；若有算法反例，提供有理输入、位置索引序列和首次违反的等式。区分“公式错误”“计数非法”“引用前提不满足”“有限检查遗漏”和“程序预算耗尽”。

Identify the document, section, claim, hypotheses, and the first failed equality or inference. For a computational example, include exact rational inputs and position indices. Distinguish an invalid formula or physical count from a missing theorem hypothesis, incomplete finite coverage, or exhausted search budget. GitHub Issues can preserve such reports alongside the revision discussed.
