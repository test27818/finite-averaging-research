# 形状变化势：已核对的零和文献与实际适用范围

更新：2026-09-12。新的证明与路径见[最优集中界与极端冻结态逃逸](../history/prime_arity_sharp_concentration_and_escape.md)。

## 1. Grynkiewicz 的零和子序列计数

D. J. Grynkiewicz, *On the number of m-term zero-sum subsequences*, Acta Arithmetica 121.3 (2006), 275–298，[DOI](https://doi.org/10.4064/aa121-3-5)。已下载全文，保存在 `work/literature_20260912/impan_0.pdf` 及对应文本。

其定理 1.1 对阶为 $m\ge30$ 的有限交换群、长度 $n$ 序列给出 $m$ 项零和子序列数下界
\[
\min\left\{
\binom{\lceil n/2\rceil}{m}+\binom{\lfloor n/2\rfloor}{m},
\binom{n-m}{\lceil(2m-1)/3\rceil}
\right\}.
\]
旧文第二个二项式抄录错误，现按原 PDF 定理修正。此计数下界不蕴含“两大桶重数和至少 $3p-2$”；该说法已被 $0^{32}1^42^4\subset C_{13}$ 否定。

## 2. 逆 EGZ 与 Graham 条件不能互换

D. J. Grynkiewicz, Ó. Ordaz, M. T. Varela, F. Villarroel, *On Erdős–Ginzburg–Ziv inverse theorems*, Acta Arithmetica 129.4 (2007)，[DOI](https://doi.org/10.4064/aa129-4-1)。全文缓存为 `impan_1.pdf` 及文本。

定理 1.2：群阶为 $m$，最小素因子为 $p_0$ 时，若
\[
|S|\ge m+\max\{h(S),m/p_0-1\},
\]
则 $0\in\Sigma_m(S)$，且 $\Sigma_m(S)$ 具有非平凡周期。对素数阶群，它就是全群。这里的 $h(S)$ 是全部余数的最大重数；不能在高重桶上略去该条件。

D. J. Grynkiewicz, *Note on a conjecture of Graham* (2011)，[DOI](https://doi.org/10.1016/j.ejc.2011.06.004)，已通过 Europe PMC XML 阅读。它控制“长度 $p$ 的序列中，所有非空零和子序列长度相同”，并推出支撑至多两种；这不等于“只禁止混合的长度 $p$ 零和”。

## 3. 本轮实际用上的工具：Balandraud 与勘误

É. Balandraud, *An addition theorem and maximal zero-sum free sets in Z/pZ*, Israel Journal of Mathematics 188 (2012), 405–429，[主文](https://doi.org/10.1007/s11856-011-0171-9)；[勘误](https://doi.org/10.1007/s11856-012-0065-5)，192 (2012), 1009–1010。

对 $A\cap(-A)=\varnothing$，包括空集的子集和集满足
\[
|\Sigma_0(A)|\ge\min\{p,1+|A|(|A|+1)/2\}.
\]
同文给出零和自由集合的三角数大小上界。主文定理表述已从出版社摘要核对；本轮主文 PDF 地址返回 HTML，未声称阅读其完整证明。勘误 PDF 已下载并读完：它修正 Lemma 4 的高次项展开，明确说明其他部分无需改动。

新文通过逐重数分层、Cauchy–Davenport 以及零只有空选择表示，推出零和自由序列满足
\[
|T|-h(T)\le\lfloor(p-1)/3\rfloor.
\]
由此得到无混合 $p$ 项零和序列的最优两桶下界。这里外部定理解决的是精确的余数重数估计，真实三步路径在新文中另行构造。

## 4. 原位置与安全性仍须单独检查

混合余数零和组一定给出非恒等整数平均；同一余数桶中的不同实际值也可能给出非恒等整数平均。不能只检查混合余数。

保护集必须让每个危险素数在未选位置中保留不同余见证，或逐步证明等价安全条件。“留一个位置”本身不保证安全。余数无混合的分类只处理整数冻结，不能覆盖所有“整数平均存在但都不安全”的状态。

文献核对记录改登记为支持材料，不再用打印一句成功消息的命令充当定理证书。一般阈值没有因此降低。
