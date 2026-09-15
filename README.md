# 完美可混合性与有限步平均 · Perfect Mixability and Finite Averaging

**中文 · [English](README.en.md) · [证明路线](docs/PROOF_GUIDE.md) · [核验指南](docs/VERIFICATION.md) · [中英术语](docs/TERMINOLOGY.md)**

**什么时候，一组有理数能在固定位置上通过有限次平均变得精确全等？** 每次选恰好 $`k`$ 个不同位置，把这些位置的值全部替换为其算术平均；不增加副本、不丢弃输出。我们研究完美可混合性／完全可混合性（**perfect mixability**）、混合图（**mixing graphs**）以及二平均、三平均、素数 $`p`$ 平均与一般 $`k`$ 平均。

> **项目重点：三平均已有独立直接证明；全部素数平均的最优最终阈值已完成；一般 $`k`$ 平均已有统一下界、明确的精细阈值猜想和多族已证结果。当前继续追求更自然、易读且结构统一的证明，并推进合数元数的剩余问题。**

这些新研究成果主要基于 **GPT-6 Astra（gpt6-astra）** 与用户的持续协作。已完成证明经过多轮内部审核、交叉复核与针对性精确核验；修改、撤回、引用前提和已知问题均保留。原二平均定理归其文献作者，见[研究来源](PROVENANCE.md)。

**English overview:** exact finite averaging and perfect mixability on fixed positions; direct ternary proofs, optimal prime-arity thresholds, composite-arity conjectures, positive realizations, exact verifiers and algorithms. [Read in English](README.en.md).

## 已取得的主要成果

对非全等有理输入，先中心化、清分母、本原化为整数零和向量 $`X`$，记

```math
G(X)=\gcd_{i\lt j}|X_i-X_j|.
```

$`\mathrm{rad}(m)`$ 表示 $`m`$ 的不同素因子之积。一般 $`k`$ 平均的必要条件是 $`\mathrm{rad}(G)\mid k`$；下表明确列出它已被证明充分的范围。全等输入始终零步完成。

| 成果 | 精确范围与意义 | 证明入口 |
|---|---|---|
| **二平均完整分类：文献基础** | **四元任意输入无条件可平均，固定四步足够**；所有二幂维数同样无条件。其余 $`n\ge5`$ 用“$`G`$是2的幂”判定；$`n=3`$恰为等差数列 | [完整分类与四步证明](docs/BINARY_CLASSIFICATION.md) |
| **三平均的独立直接证明** | 全部 $`n\ge7`$，可平均当且仅当 $`G`$ 是3的幂；双三重值不变量直接覆盖 $`n\ge11`$，接7、8、9、10元基例，不需一般素数／合数维数归约 | [直接证明](archive/2026-09-07/3-3-triple-average-research-note/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md) |
| **全部奇素数的最优最终阈值** | 对每个奇素数 $`p`$，$`\boxed{N(p)=2p+1}`$；全部 $`n\ge2p+1`$ 的判据为 $`G=p^e`$，$`e`$为非负整数，并有 $`2p`$ 处合法不可达反例证明最优性 | [总证明及全部区间覆盖](archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/proof.md) |
| **任意元数的共同端点与宽尾部** | 所有 $`k\ge2`$ 的 $`n=2k+1`$ 均有完整 $`G=1`$ 判据；任意 $`k\ge3`$ 有 $`N(k)\le4k+\lceil\log_2k\rceil+1\le5k`$ | [端点及当前交接](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_three_tasks_progress_20260915.md) · [线性尾部](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/arbitrary_arity_linear_threshold.md) |
| **一般元数的整族区间与转译** | 任意 $`k\ge2`$ 的全部 $`n=jk`$、$`j\ge3`$；奇素数幂 $`k=p^a`$ 的全部奇数 $`2k\lt n\lt 3k`$；均取得完整算术判据 | [块均值转译](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/averaging_proof_strategy_and_composite_frontier_20260915.md) · [奇数中间带](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/odd_composite_coprime_middle_band_completion.md) |
| **无条件固定网络族** | 整数$`m\ge2`$时，$`k=m(m-1)`$、$`n=m^2`$ 有固定四步网络；整数$`b\ge1`$时，$`k=2(4^b-1)/3`$、$`n=4^b`$ 有固定 $`2b+2`$ 步网络，特别十平均十六元固定六步 | [四步网络](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/composite_critical_scale_and_conjecture.md) · [十平均及递推族](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/ten_average_sixteen_and_dyadic_network_family.md) |
| **GRH下的平方族与部分素数幂临界点** | 所有 $`k=t^2`$、整数$`t\ge2`$在 $`n=t^2+t+1`$ 上有完整判据；素数偶次幂及2、3的全部幂达到各自最早临界下界。**这不是全部后续维数的最终阈值结论** | [平方族](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md) · [2、3奇次幂](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/two_three_odd_power_critical_grh_completion.md) |
| **证明简化：统一二进列提升** | 三个已有真实返回的平方、交换子与逐层提升，统一替代内部偶余量64／256类轨道表，完整保留方向与尺度 | [2026-09-16独立改进](archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/structural_reassessment_and_uniform_dyadic_orbits.md) |

**算法成果：** 二平均提供Python、JavaScript网页和Prolog工具，以及1636个基准实例、538条已验解路径；三／$`p`$平均另有困难实例、精确原位置验解器、论文PDF／LaTeX和构造脚本。可达性判定、构造路径与认证最短路径分别记录，不能把搜索预算耗尽当成不可达。

## 我们使用的方法：为什么证明能推进

**1. 重复值保护算术见证，离散能量保证终止。** 二平均原文保持两个不同的重复值；三平均直接证明保持两个不同的三重值。重复位置留下模危险素数的见证，避免平均过程中丢失合法性。先预留一位额外精度，再在整数格上选安全非恒等平均，使 $`\sum_i X_i^2`$ 严格下降，直到明确终端。这是三平均绕开旧种子搜索的关键。二平均四元及其他二幂维数直接用固定网络，不需要这套一般不变量。

**2. 临界区间先压缩到可操纵核心，再制造真实逆。** 原位置的安全分组把输入送入少量等值块；显式计数给出返回 $`J`$，若在完整核心上 $`J^2=cI`$、$`c\ne0`$，就有可正向执行的射影逆。相邻计数返回的商与交换子产生剪切根；这些根的参数理想和真实倍率决定哪些分母可局部化。每一步都要有足够的实际位置，不能把抽象矩阵逆当成平均操作。

**3. 均值格解释同余结构，精确纤维完成有理终端。** 常值方向与整数零和格的拼接给出自然的同余标记。真实根接Morris／Serre的算术群工具，取得深主同余控制；再调整有限模数中的**方向和许可单位尺度**，由精确纤维送到真正的零和终端。新的二进列提升把部分轨道枚举改写为同一个线性误差修正规则。

**4. 合数元数结合块均值转译、固定网络与局部赋值。** 商系统的操作由原位置上的块并集平均实现；未选块无需事先平均。允许素数处的赋值陷阱给出临界下界；平方核心和混合元数网络提供正向构造。GRH只在相关条件性证明的“小单位生成”环节使用，不能代替位置容量、真实逆或终止论证。

[完整证明路线与依赖图](docs/PROOF_GUIDE.md) · [通用算术引理](archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/arithmetic_toolkit.md) · [自然结构与独立改进](archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/README.md)

## 一般 k 平均：精细阈值猜想

令 $`\mathcal P(k,n)`$ 表示：该维数的每个有理输入都满足完整判据“可平均当且仅当 $`\mathrm{rad}(G)\mid k`$”，全等输入单列。必须区分：

| 量 | 定义 | 例子 |
|---|---|---|
| $`M(k)`$ | 排除平凡的$`n=k`$后，最早一个满足$`\mathcal P(k,n)`$的维数 | $`M(6)=9`$，来自无条件固定网络 |
| $`H(k)`$ | 最早满足$`\mathcal P(k,n)`$且$`\mathrm{rad}(n)\nmid k`$的维数；此时$`G`$条件真正筛选输入 | $`H(6)=10`$；二平均$`M(2)=4`$而$`H(2)=5`$ |
| $`N(k)`$ | 从此以后**每个**维数都满足$`\mathcal P(k,n)`$的最小起点 | $`N(3)=7`$；一般合数的$`N`$仍有未解范围 |

写 $`k=\prod_p p^{a_p}`$，定义局部临界尺度

```math
S(k)=\max_{p\mid k}p^{\lceil a_p/2\rceil},
```

以及

```math
B(k)=k+S(k)+
\begin{cases}
0,&\mathrm{rad}(k+S(k))\mid k,\\
1,&\mathrm{rad}(k+S(k))\nmid k.
\end{cases}
```

**已证下界：$`M(k)\ge B(k)`$、$`N(k)\ge B(k)`$。核心猜想分成两步：**

```math
\boxed{M(k)=B(k)}
\qquad\text{及}\qquad
\boxed{N(k)=M(k)}.
```

合起来预测 $`\boxed{N(k)=B(k)}`$。第一步要证明下界处确实可达；第二步要证明成功以后不再出现缺口，**二者都不能由有限成功样本推出**。非自动算术边缘的对应猜想是

```math
H(k)=C(k),\qquad
C(k)=\min\{n\gt k+S(k):\mathrm{rad}(n)\nmid k\}.
```

**公式背后的结构：** 对每个 $`p^a\parallel k`$，若余下位置不足 $`p^{\lceil a/2\rceil}`$，一个最低$`p`$进赋值的$`k`$重块会在每次非恒等平均后重新出现，阻止归零；取最坏局部尺度得到$`S(k)`$。边界退出可能形成新的非法共同余数，因此出现$`B(k)`$中的加1修正。它统一解释奇素数的$`2p+1`$、四平均的7、八平均的13等临界数。

| 元数$`k`$ | 猜想临界$`B(k)`$ | 已证最早结果 | 最终$`N(k)`$ |
|---|---:|---|---|
| 2 | 4 | $`M=4,\ H=5`$；四元无条件 | **已证4** |
| 奇素数$`p`$ | $`2p+1`$ | $`M=H=2p+1`$ | **全部已证$`2p+1`$** |
| 4、8、9 | 7、13、13 | 对应$`M=H=7,13,13`$，均无条件证明 | 尚未确定 |
| 6 | 9 | $`M=9,\ H=10`$ | 尚未确定 |
| 10、12 | 16、16 | 均有$`M=16,\ H=17`$，无条件证明 | 尚未确定 |
| $`p^{2a}`$，$`a\ge1`$ | $`p^{2a}+p^a+1`$ | GRH下全部达到$`M=H=B`$；部分小值已有无条件证明 | 一般尚未确定 |
| $`p^{2a+1}`$，$`a\ge1`$，$`p=2,3`$ | $`p^{2a+1}+p^{a+1}+1`$ | GRH下全部达到$`M=H=B`$ | 一般尚未确定 |
| 14、15、18 | 22、21、22 | 下界已证，临界充分性仍未证明 | 尚未确定 |

对混合平方元数，平方族的已证维数未必达到$`B(k)`$：例如$`k=36`$时，GRH平方族给$`n=43`$，而猜想临界为$`B(36)=40`$。另外，$`\mathrm{rad}(n)\mid k`$只说明$`G`$条件自动满足，**不自动提供平均网络**；$`k=24,n=27`$已有合法不可达反例。

[原始临界下界与猜想全文](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/composite_critical_scale_and_conjecture.md) · [最新已证范围与剩余任务](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_three_tasks_progress_20260915.md)

## 当前主攻方向与证明边界

- **证明统一化：** 已有素数最优阈值基础上，提取共同的位置计数、根理想和列提升机制，减少孤立构造。九偏移的162组物理／根理想证书及其他有限证据仍保留，未宣称整个证明已经无计算依赖。
- **合数临界点：** 继续处理$`p\ge5`$的高奇次幂，以及14、15、18等混合元数；不同允许素数的局部进位必须在同一条真实路径上协调。
- **区间接续：** 从$`M(k)`$或$`2k+1`$端点推进到所有后续维数；已有奇数区间、整除转译和宽尾部尚不足以推出一般$`N(k)=B(k)`$。
- **构造效率：** 将存在性证明转为更短、可实际提取的平均序列；尚无覆盖全部可变$`k,n`$的统一多项式操作长度或最短路径算法。

素数证明无条件，但引用已注明的Morris／Serre定理；一般元数的GRH结果明确标注。多轮内部审核不等于外部同行评审或形式化认证。每项程序PASS的含义由其证据范围限定；失败探索、历史状态和已知软件问题均留档。

## 阅读与文件结构

| 需要 | 入口 |
|---|---|
| 二平均定义、无条件小维数、求解器 | [二平均主题](topics/binary/README.md) |
| 三平均直接证明、基例、论文PDF／LaTeX | [三平均主题](topics/ternary/README.md) |
| 素数全部区间及依赖 | [素数主题](topics/prime/README.md) |
| 一般元数、GRH与未解范围 | [一般元数主题](topics/general/README.md) |
| 从一条命题定位正文和代码 | [185项命题—核验索引](catalog/CHECKS.md) |
| 研究历史与文件全文 | [完整文件目录](catalog/FILES.md) · [历史路线账本](archive/2026-09-07/3-3-triple-average-research-note/outputs/history/research_routes_history_20260915.md) |
| 算法能力测试 | [二平均1636题](archive/2026-09-07/new-chat-3/averaging_benchmark/README.md) · [三／p平均困难实例](archive/2026-09-10/new-chat/outputs/averaging_algorithm_benchmark/README.md) |

~~~text
topics/              二、三、p、k平均专题入口
docs/                双语定义、证明路线、核验指南、已知问题
catalog/             全文件索引、185项核验索引、哈希与运行记录
scripts/             归档检查与临时副本复现工具
archive/
  2026-09-07/
    3-3-triple-average-research-note/
      outputs/       按主题分类的证明、文献与研究历史
      research/      独立结构改进
      work/          原核验器、证书、探索脚本和来源材料
    new-chat-3/      二平均求解器与基准库
  2026-09-09/cha/    历史文稿审阅
  2026-09-10/new-chat/ 论文、算法测试集和补充研究
~~~

**公开快照：2026-09-16。** 保留1905个原文件，包括590篇Markdown、479个Python脚本、42份PDF及22份LaTeX源码。日期层级保留原导入和跨目录引用，专题导航提供当前阅读顺序。历史原稿有过期“未解”和旧路径，按[来源与移植说明](PROVENANCE.md)定位；原归档不随首页整理被改写。

## 怎样检验

需要Python 3.11+；二平均JavaScript回归另需Node.js。下面的review在临时副本中运行，保留归档原件：

~~~sh
git clone https://github.com/test27818/finite-averaging-research.git
cd finite-averaging-research
python -B scripts/check_archive.py
python -B scripts/build_check_index.py --check
python -B scripts/reproduce.py --suite review
~~~

[复现指南](docs/VERIFICATION.md)说明每项检查的范围、命令和外部依赖；[完整review日志](catalog/reproduction_review.txt)保留实际结果。**最近一次完整review的数学检查通过，二平均Python有1项零预算计时状态测试失败**，原因及确定性诊断见[已知问题](docs/KNOWN_ISSUES.md)，没有将该次运行标成全绿。

二平均可直接下载并打开[离线网页](archive/2026-09-07/new-chat-3/averaging_benchmark/solver.html)。更多脚本按需使用[可选依赖](requirements.txt)。归档完整性检查、有限证书重放与一般数学证明承担不同任务。

## 原始问题与文献来源

二平均直接来源为 Miguel Coviello Gonzalez、Marek Chrobak 的 *Towards a Theory of Mixing Graphs: A Characterization of Perfect Mixability*（[arXiv:1806.08875v4](https://arxiv.org/abs/1806.08875v4)，[DOI](https://doi.org/10.1016/j.tcs.2020.09.007)）；[原文复核](archive/2026-09-07/3-3-triple-average-research-note/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)说明Condition (MC)、重复值方法和推广边界。

**检索用语：** perfect mixability、mixing graphs、finite-step averaging、pairwise/binary averaging、ternary/triple averaging、prime-arity averaging、general k-ary averaging；完美可混合性、混合图、有限步平均、两数平均、三数平均、素数平均、合数平均。有限时间共识（finite-time consensus）、clique gossiping是相关问题，但固定网络与依赖输入的可达性量词不同，见[双语术语表](docs/TERMINOLOGY.md)。

第三方文献和源码保留原作者与权利，见[资料来源说明](THIRD_PARTY.md)。[研究来源及审核记录](PROVENANCE.md) · [原始文件哈希](catalog/SHA256SUMS.txt)
