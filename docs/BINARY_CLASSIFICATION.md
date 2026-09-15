# 二平均完整分类：四元无条件成立 / Binary classification: four entries are unconditional

[中文首页](../README.zh-CN.md) · [English](../README.md) · [二平均主题 / Binary topic](../topics/binary/README.md) · [证明指南 / Proof guide](PROOF_GUIDE.md)

**任意四个输入都可二平均，固定四次操作足够，不需要检查 $`G`$。**

**Every four-entry input is mixable by binary averaging. Four fixed operations suffice; no gcd test is needed.**

## 完整分类 / Complete classification

以下输入为有理数。全等输入始终以零步完成；$`G`$仅对非全等输入在中心化、清分母、本原化后定义。

Inputs below are rational. Constant input always takes zero steps; $`G`$ is defined for nonconstant input after centering and primitive integer normalization.

| 位置数 / Number of positions | 结论 / Result |
|---|---|
| $`n=1`$ | 已全等 / Already equal |
| $`n=2`$ | 任意输入，一步平均 / Every input, one averaging operation |
| $`n=3`$ | 当且仅当排序后三数成等差数列，即某一项等于总均值 / Exactly when one entry is the mean, equivalently an arithmetic progression after sorting |
| **$`n=4`$** | **任意输入，无条件可平均；固定四次操作足够 / Every input, unconditionally; four fixed operations suffice** |
| $`n=8,16,32,\ldots`$ | 任意输入，无条件可平均；固定蝶形网络 / Every input, via a fixed butterfly network |
| 其余$`n\ge5`$ / Other $`n\ge5`$ | 当且仅当$`G`$是2的非负整数次幂，即$`G\in\{1,2,4,8,\ldots\}`$ / Exactly when $`G`$ is a nonnegative integer power of 2 |

无条件网络对任意实输入也成立；有理输入的gcd分类不直接移植为任意实数的分类。

The unconditional networks also work for arbitrary real inputs. The rational gcd criterion is not a classification of arbitrary real inputs.

## 四元的直接证明 / Direct proof for four entries

对任意 $`(a,b,c,d)`$，按原位置依次平均

```math
(1,2),\quad(3,4),\quad(1,3),\quad(2,4).
```

令 $`A=(a+b)/2`$、$`B=(c+d)/2`$、$`\mu=(a+b+c+d)/4`$，则

```math
(a,b,c,d)
\longrightarrow (A,A,c,d)
\longrightarrow (A,A,B,B)
\longrightarrow (\mu,A,\mu,B)
\longrightarrow (\mu,\mu,\mu,\mu).
```

Every input follows this same four-operation schedule. “Four suffice” is an upper bound; special inputs can require fewer operations. In particular, **$`n=4`$ does not need the repeated-value invariant or the general sufficiency theorem**.

更一般地，$`n=2^r`$时，先递归平均两个等大半块，再按位置跨半块配对，得到固定蝶形网络。$`N(2)=4`$指从四元起一般可达性判据始终适用，**并不表示所有$`n\ge4`$都无条件可平均**；例如五元$`(0,0,0,0,1)`$的目标$`1/5`$不能由二进系数产生。

For $`n=2^r`$, recursively average the two halves and then pair their positions across the halves. The final threshold $`N(2)=4`$ means the general characterization applies from dimension four onward; it does not make every input mixable for every $`n\ge4`$. For example, $`(0,0,0,0,1)`$ cannot reach the mean $`1/5`$ using dyadic coefficients.

## 为什么历史等价式与无条件成立不冲突 / Why the archived equivalence is consistent

对非零本原整数零和向量 $`X`$，若所有坐标模$`G`$均等于$`c`$，则$`\gcd(c,G)=1`$：否则整除$`c`$与$`G`$的素数会整除每个坐标，与本原性矛盾。总和为零给出$`nc\equiv0\pmod G`$，所以

```math
G\mid n.
```

因此$`n=4`$时$`G`$自动属于$`\{1,2,4\}`$；一般$`n=2^r`$时$`G`$也自动是2的幂。历史文稿“$`n\ge4`$时可平均当且仅当$`G`$是2的幂”在逻辑上成立，但四元情形中右侧自动满足，**不是筛选输入的附加条件**。当前中英文导航把这种无条件情形明确单列。

For a nonzero primitive integer zero-sum vector, all entries share a residue $`c`$ modulo $`G`$ and $`\gcd(c,G)=1`$. Their sum gives $`nc=0`$ modulo $`G`$, hence $`G`$ divides $`n`$. At $`n=4`$, therefore, $`G`$ automatically belongs to $`\{1,2,4\}`$. The archived equivalence for $`n\ge4`$ is logically valid, but its right-hand side is automatic at four entries; it imposes no additional restriction. Current navigation lists the unconditional cases separately.

## 原文与程序 / Sources and code

- [二平均原始文献复核](../archive/2026-09-07/3-3-triple-average-research-note/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)。
- [历史问题说明](../archive/2026-09-07/new-chat-3/averaging_benchmark/problem.md)：已单列$`n=4`$恒可；一般$`n\ge4`$判据应按上文理解。
- [Python判定和固定蝶形网络](../archive/2026-09-07/new-chat-3/averaging_benchmark/src/solver.py)：judge通过gcd也会对每个四元整数输入返回True；power2_tree_sequence提供固定网络。
- [当前核验指南](VERIFICATION.md)与[已知计时问题](KNOWN_ISSUES.md)：预算状态测试不改变上述固定网络证明。

这次修正的是当前说明中遗漏的无条件分类；原始数学等价式和实际四元算法并未因此失效。原文献、冻结证书和历史归档保留原件。

This clarification restores the explicit unconditional classification in the current presentation. It does not invalidate the original equivalence or the four-entry algorithm. Source literature, frozen evidence and historical archives retain their original contents.
