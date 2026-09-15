# 可混合性、混合图与平均：中英术语和模型 / Mixability, mixing graphs and averaging

[中文首页](../README.zh-CN.md) · [English](../README.md) · [指南目录 / Guides](README.md)

## 同一问题的检索表述 / Search vocabulary

| 中文名称与常见表述 | English terms | 本仓库中的含义 / Meaning here |
|---|---|---|
| 完美可混合性、完全可混合性、可混合性、精确混合 | perfect mixability, perfect mixing, mixability | 指定输入能否有限步精确全等 / Exact finite equalization of a specified input |
| 混合图、无废弃混合网络 | mixing graphs, waste-free mixing networks | 混合器的有向无环图及其顺序执行 / A mixer DAG and its sequential execution |
| 有限步平均、有限次平均、平均化、均值化 | finite averaging, finite-step averaging, exact averaging, averaging to equalize | 每一步替换全部被选位置 / Replace every selected coordinate by their common mean |
| 二平均、两数平均、成对平均、两两平均 | binary averaging, pairwise averaging, 2-averaging | 每步恰选两个位置 / Exactly two positions per operation |
| 三平均、三数平均、三元平均 | ternary averaging, triple averaging, 3-averaging | 每步恰选三个位置 / Exactly three positions per operation |
| p平均、素数平均、素数元平均 | p-averaging, prime-arity averaging | 平均元数是素数 $`p`$ / Prime operation arity |
| k平均、k元平均、一般平均、合数平均 | k-averaging, k-ary averaging, general-arity averaging, composite-arity averaging | 每步选 $`k`$ 个位置 / General operation arity |
| 同余判据、差分最大公因子、原始可混合条件 | congruence obstruction, difference gcd, Condition (MC) | 可达性的算术障碍；MC的精确适用范围见下 / Arithmetic reachability obstruction |
| 有限步共识、有限时间共识、团八卦算法 | finite-time consensus, exact consensus, clique gossiping | 相关文献用语；需核对模型与量词 / Related terminology with potentially different models |
| 精确有理验解、可达性证书 | exact rational verification, reachability certificate | 在原位置上用整数／有理数逐步重放 / Exact replay on original positions |

这些词用于描述数学内容，并不声称所有文献模型等价。“混合”也可能指概率混合时间、图着色、化学反应或有废弃的样品制备，引用前须核对定义。

These terms describe the mathematical subject. They do not make all mixing or consensus models equivalent; probabilistic mixing times and sample preparation with extra droplets are different problems.

## 严格操作 / Exact operation

输入是 $`x=(x_1,\ldots,x_n)\in\mathbb Q^n`$。选恰好 $`k`$ 个不同位置组成 $`S`$，执行

```math
x'_i=
\begin{cases}
\frac1k\sum_{j\in S}x_j,&i\in S,\\
x_i,&i\notin S.
\end{cases}
```

要求有限步后所有位置等于原均值 $`\bar x=\sum_i x_i/n`$；位置总数不变。它不是只替换一项，不允许额外复制，也不允许丢弃输出。

The input is a rational vector on $`n`$ fixed positions. Each operation averages exactly $`k`$ distinct positions and replaces **all** selected entries. The target is the original mean at every position after finitely many steps, without adding copies or discarding outputs.

例如二平均 $`(0,0,2,2)`$ 可依次平均第1与3项、第2与4项，得到 $`(1,1,1,1)`$；三平均 $`(0,3,6)`$ 一步变成 $`(3,3,3)`$。这些例子只说明操作，不证明一般判据。

For example, binary averaging of positions $`(1,3)`$ and then $`(2,4)`$ sends $`(0,0,2,2)`$ to $`(1,1,1,1)`$. One ternary operation sends $`(0,3,6)`$ to $`(3,3,3)`$. These illustrate the operation, not the general theorem.

## Condition (MC) 与 G / Condition (MC) and the gcd formulation

原二平均文献在其整数／二进有理精度约定下，Condition (MC) 要求：对每个奇模数 $`b`$，若所有输入模 $`b`$ 同余，则目标均值也属于同一余数类。请读[原文复核](../archive/2026-09-07/3-3-triple-average-research-note/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)。

In the binary paper's integer/dyadic-precision setting, Condition (MC) requires that whenever the input is congruent modulo an odd modulus $`b`$, adjoining the target mean preserves that congruence. It is a statement about both the input and its mean.

本项目将非全等有理输入中心化、清分母、本原化成整数零和向量 $`X`$，再定义 $`G=\gcd_{i\lt j}|X_i-X_j|`$。素数 $`p`$ 平均的完整阈值范围内，判据是 $`G=p^e`$；一般 $`k`$ 的必要条件是每个整除 $`G`$ 的素数均整除 $`k`$，即 $`\mathrm{rad}(G)\mid k`$，充分性要看具体已证范围。

The project uses primitive centered integer deviations. Above the proved prime-arity thresholds, the criterion is $`G=p^e`$, with $`e`$ a nonnegative integer. For general $`k`$, the necessary condition is $`\mathrm{rad}(G)\mid k`$; its sufficiency must be read with the stated dimension range. Constant input is a separate zero-step case.

**二平均的四元情形无条件成立。** 任意$`(a,b,c,d)`$按$`(1,2),(3,4),(1,3),(2,4)`$四次配对即到总均值，无须检查$`G`$。本原零和向量有$`G\mid n`$，所以$`n=4`$时$`G`$自动为1、2或4。二平均的其他二幂维数同样无条件可平均；其余$`n\ge5`$才需要用$`G`$判据筛选。见[完整分类](BINARY_CLASSIFICATION.md)。

**Four-entry binary averaging is unconditional.** The fixed schedule $`(1,2),(3,4),(1,3),(2,4)`$ works for every input. Since primitive zero-sum vectors satisfy $`G\mid n`$, their $`G`$ at $`n=4`$ is automatically 1, 2 or 4. Other powers-of-two sizes are also unconditional; the gcd test selects eligible inputs at the remaining sizes $`n\ge5`$. See the [complete classification](BINARY_CLASSIFICATION.md).

## 原始 mixing graph 与顺序平均 / Mixing graphs and sequential averaging

原二平均文献中的无废弃二入二出混合器，把两份浓度都替换为均值；混合图按拓扑序执行可解释为固定数量液滴上的二平均。这里沿用这种原位置、无增殖的顺序模型。

The binary literature's waste-free two-input/two-output mixers replace both concentrations by their mean. Executing a mixing DAG in topological order gives the sequential model with a fixed number of droplets.

但以下两个命题不同：

1. 对每个合法的有理输入，存在一条可依赖输入的有限路径。
2. 存在一个固定网络，对全部实输入都实现全平均。

The first is state-dependent reachability; the second is a universal fixed network. A theorem about the second need not classify the first. The same distinction applies when importing results on clique gossiping and finite-time consensus.
