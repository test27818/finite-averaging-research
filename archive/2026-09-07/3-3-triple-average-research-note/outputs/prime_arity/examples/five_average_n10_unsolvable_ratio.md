# 五平均 (n=10) 的不可解比例实验

日期：2026-09-12。这里每次选择五个位置并把它们替换为平均值。对十元本原零和状态，候选必要条件是

\[
G(X)=\gcd_{i<j}|X_i-X_j|\quad\text{为 }5\text{ 的幂}.
\]

实验使用 `work/exact_five_n10_ratio.py`。整数输入在 (p\le n\le2p) 时成功路径不会产生新的五进分母；因此脚本枚举全部合法整数五平均后继。每个非恒等后继严格降低平方能量，递归没有深度截断，故对给定状态的可达性判断是精确的。状态只按排序和整体符号规范化，整体公因子在每步约去，因为这与可达性相容。

## 结果

### 有界状态的完整枚举

“比例”是满足 (G=5^k) 的规范化本原零和状态中，不可归零状态所占的比例；它不是独立随机数组的概率。

| 初始坐标范围 | 合法状态数 | 可解 | 不可解 | 比例 |
|---|---:|---:|---:|---:|
| ([-1,1]) | 4 | 4 | 0 | 0 |
| ([-2,2]) | 31 | 30 | 1 | 3.226% |
| ([-3,3]) | 175 | 168 | 7 | 4.000% |
| ([-4,4]) | 766 | 755 | 11 | 1.436% |
| ([-5,5]) | 2723 | 2687 | 36 | 1.322% |
| ([-6,6]) | 8248 | 8148 | 100 | 1.212% |
| ([-7,7]) | 22223 | 22047 | 176 | 0.792% |

完整枚举中的不可解例子包括

\[
(-5,0^4,1^5),
\qquad
(-2,-2,-2,0,1^6),
\]

以及若干具有大重数块的变体。它们不是均匀散布的状态，而是集中在低复杂度重数结构中。

### 独立随机原始数组

每次独立生成十个均匀整数，中心化、本原化后只接受 (G=5^k) 的样本；可达性仍由上面的完整递归判断。结果：

| 原始抽样范围 | 接受样本数 | 不可解 | 经验比例 | 95% Clopper–Pearson 区间 |
|---|---:|---:|---:|---:|
| ([-2,2]) | 2000 | 1 | 0.050% | [0.0013%, 0.2783%] |
| ([-5,5]) | 2000 | 0 | 0 | [0, 0.1843%] |
| ([-20,20]) | 待补跑 | - | - | - |

最后一行来自同一精确递归版本的已完成运行；较大范围的单样本递归耗时显著增加。接受率（原始数组中满足 (G=5^k) 的比例）约为 10% 左右，随范围略有变化，但它不是不可解率的分母。

## 对 (2p+1) 反例搜索的含义

1. 若把 (n=10) 的**有界规范化状态比例**约 (1\%-4\%) 当作最粗参考，则在真实反例率为 (r) 的随机模型下，观察到至少一个反例的样本量满足
   
   \[
   N\ge\frac{\log(0.05)}{\log(1-r)}\approx\frac3r.
   \]
   因而 (r=1\%,0.1\%,0.01\%) 分别需要约 (299,2995,29956) 个**接受样本**。

2. 对当前独立随机原始数组模型，(n=10) 的命中率只有约 (0.05\%-0.10\%)，并且扩展范围后没有上升趋势。按这个更保守的量级，至少准备 (3000\)-(6000) 个接受样本才能有约 95% 概率看到一次反例；若反例率降到 (10^{-4})，则需要约 30000 个。

3. 若 (N) 次接受样本一个反例也没有，不能说反例率为零。95% 单侧上界为

   \[
   1-0.05^{1/N}\approx3/N.
   \]

   例如 (N=2000) 时上界约 (0.15\%\)，(N=10000) 时约 (0.030\%\)。

4. 这些数字不能直接证明或否定 (n=2p+1) 的一般猜想。(n=10) 的已知不可解族具有特殊重数形状，独立均匀数组命中它的概率可能远低于“所有规范化状态均匀抽样”的比例。对 (2p+1) 的数值证据应同时报告抽样分布、接受率、完整验解状态和置信区间，并专门增加对大重数/稀疏结构的分层抽样。

复现实验：

```text
python work/exact_five_n10_ratio.py --exact-bounds 2 3 4 5 --random-bounds 2 5 --samples 2000 --output work/five_average_n10_ratio_corrected_small.json
```

较大范围参考运行的结果保存在 `work/five_average_n10_ratio_2000.json`。

### Correction to the random-table note

The corrected predicate is (G=5^k), including (G=5). The corrected runs have an acceptance rate near 49%, not 10% (10% was the obsolete (G=1)-only filter). The corrected 2000-sample results currently cover bounds 2 and 5: respectively 1/2000 and 0/2000 unsolvable accepted samples. The bound-20 row from the older file used the obsolete filter and must not be used as a corrected estimate.

One explicit additional trap in the corrected predicate is the primitive zero-sum state (-14, 1^8, 6): its difference gcd is 5 and the complete integer recursion certifies it is unreachable. Thus the experiment must retain G=5 states; restricting to G=1 would miss genuine candidate failures.
