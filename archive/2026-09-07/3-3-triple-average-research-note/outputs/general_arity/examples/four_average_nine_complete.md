# 四平均九元完整判据：一个四步周期与模9控制器

日期：2026-09-12。本文证明：对九个有理数，四平均有限步可达，当且仅当中心化、本原化后 \(G=1\)；全等输入单独允许空词。

九元的 \(G\mid9\)，所以这正是原来的“\(G\) 只能含2因子”条件。证明使用明确的原位置宏、一个显式周期、模9全部陪集回路与 Bezout 输送。没有搜索种子、平均词或未验证的矩阵分解前提。

## 1. 两步进入双四重块

写零和本原输入为 \(X\)。保留任意一个原位置 \(w\)，将其余八个位置分成两个四元块 \(A,B\)。

如果两块和模3不同，直接分别四平均，得到
\[
K(a,b)=(a^4,b^4,-4(a+b)).
\tag{1}
\]
如果块和模3相同，交换计划中跨块的一对模3不同的输入，使块和差改变 \(2(y-x)\)，变成模3非零。

为什么这种跨块对一定存在：若没有，则八个位置全模3同余为 \(r\)，全局零和迫使第九项为 \(-8r=r\pmod3\)，与 \(G=1\) 和本原性矛盾。交换只改变要平均哪些原位置的计划，不是额外物理操作。

令参数
\[
x=a,\qquad y=a-b.
\]
对本原整数参数，(1) 有
\[
G(K)=\gcd(y,9).
\tag{2}
\]
对有理参数先清分母、除共同因子。入口的模3不同余正好保证合法参数条件 \(3\nmid y\)。

## 2. 宏矩阵及原位置实现

对 \(j=1,2,4\)，依次平均两个不交四元组
\[
(a^{j-1},b^{4-j},-4(a+b)),
\qquad
(a^{4-j},b^j),
\tag{3}
\]
留下另一份 \(a\) 当作新单点。参数实际矩阵为 \(T_j/4\)，其中
\[
T_j=\begin{pmatrix}-5&j\\-9&2j\end{pmatrix}.
\tag{4}
\]

交换两个常值块的账本名称给
\[
\Sigma=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
\tag{5}
\]
它不移动数值，只改变后续如何引用两组标签。

另保留单点，平均 \((a^3,b)\) 和 \((a,b^3)\)，得到
\[
F_2=\begin{pmatrix}1&-1/4\\0&1/2\end{pmatrix}.
\tag{6}
\]
这些矩阵都是对整个二维输入族有效的真实宏。每个矩阵的行列式及 \(y\) 的模3倍率都是单位，因此保持合法域。

## 3. 偶数元数的新周期：无需原来的奇数种子

直接计算：
\[
T_2\Sigma=\begin{pmatrix}-5&3\\-9&5\end{pmatrix},
\qquad
\boxed{(T_2\Sigma)^2=-2I.}
\tag{7}
\]
恢复每个 \(T_2\) 的真实尺度 \(1/4\)，四次原子平均在核心上的矩阵是 \(-I/8\)，所以 \(T_2\) 有正向射影逆 \(\Sigma T_2\Sigma\)。

进一步，
\[
D=T_2^{-1}T_4=\Delta(2),
\qquad
DF_2=U(-1/4),
\tag{8}
\]
其中 \(\Delta(t)=\operatorname{diag}(1,t)\)、\(U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix}\)。

只知道 \(D\) 正向存在时，不能直接使用 \(D^{-1}\)。这里的逆由明确机制补齐：
\[
\Sigma U(t)\Sigma=U(-t).
\]
因此 \(P=DF_2\) 已有正向逆 \(\Sigma P\Sigma\)，从而
\[
D^{-1}=F_2(\Sigma P\Sigma),\qquad
F_2^{-1}=(\Sigma P\Sigma)D
\tag{9}
\]
都正向可执行。

于是 \(U(\pm1/4)\)、\(\Delta(2)^{\pm1}\) 都已实现，通过整数次幂与共轭得到
\[
U(\mathbb Z[1/2]).
\tag{10}
\]
\(\Delta(-1)=\Sigma U(1)\) 也已实现。

下根来自一个明确恒等式：
\[
U(-1/2)\,T_1\,\Delta(-1/4)\sim L(18),
\qquad
\Delta(1/2)L(18)\Delta(2)=L(9),
\tag{11}
\]
其中 \(\sim\) 表示相差一个非零共同标量。用 \(\Delta(-1)\) 共轭给下根逆，再按2的幂共轭。

所以真实正向宏半群已经包含
\[
\boxed{
U(R),\quad L(9R),\quad \Delta(R^\times),
\qquad R=\mathbb Z[1/2].
}
\tag{12}
\]
每个形式逆都已给出正向词；所有底层操作仍只是四平均。

## 4. 为什么模9全部轨道都能覆盖

复用[素数幂端点的两张坐标图](../../prime_arity/tools/prime_power_endpoint_and_critical_geometry.md)的纯整数部分；此处重新证明所需主元均为2的幂，不套用其“平均元数为奇数”的控制器。

\(\mathbf P^1(\mathbb Z/9\mathbb Z)\) 有12个点，对应
\[
A_j=ST^j=\begin{pmatrix}0&-1\\1&j\end{pmatrix},
\quad -4\le j\le4;
\qquad
B_t=L(t),\quad t\in\{-3,0,3\}.
\tag{13}
\]
这里 \(S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\)、\(T=U(1)\) 只是整数群证明的字母。代表本身不被当成可执行物理操作。

右乘 \(T^{\pm1}\) 时，第一张图的回路是 \(L(0)\) 或 \(L(\pm9)\)。右乘 \(S\) 时：

- \(3\mid j\)：回路为 \(-I\)；
- \(3\nmid j\)：取居中代表 \(k=-j^{-1}\pmod9\)，回路为
  \[
  \begin{pmatrix}-k&-1\\jk+1&j\end{pmatrix}.
  \tag{14}
  \]
  因 \(k\in\{\pm1,\pm2,\pm4\}\)，左上主元是 \(R\) 单位。

第二张图右乘 \(S\) 的回路为 \(I\)。右乘 \(T^\epsilon\)，由于 \(9\mid t^2\)，下一代表仍为 \(B_t\)，回路是
\[
B_tT^\epsilon B_t^{-1}
=\begin{pmatrix}
1-\epsilon t&\epsilon\\
-\epsilon t^2&1+\epsilon t
\end{pmatrix}.
\tag{15}
\]
其非平凡主元只有 \(-2,4\)，仍为 \(R\) 单位。这是模9特别简洁的地方。

任何行列式为1、左下项被9整除且左上项 \(u\) 为 \(R\) 单位的矩阵都有
\[
\begin{pmatrix}u&v\\w&z\end{pmatrix}
=L(w/u)\operatorname{diag}(u,u^{-1})U(v/u).
\tag{16}
\]
中间因子射影等于 \(\Delta(u^{-2})\)。因此所有12个代表在 \(S,T,T^{-1}\) 下的36条回路都由 (12) 正向实现。

完整 Schreier 生成定理遂给出
\[
\boxed{\Gamma_0(9)\ \text{的射影作用全部可由真实正向四平均实现。}}
\tag{17}
\]
这不是只验证模9的群像，也不声称宏群等于 \(\Gamma_0(9)\)：它实际含有二进局部化的额外元素。充分性只需上述包含。

## 5. 任意合法方向输送到零

把参数写为本原整数 \((x,y)\)，有 \(\gcd(y,9)=1\)。取 \(ux+vy=1\)，再做
\[
(u,v)\mapsto(u+ky,v-kx)
\]
令 \(9\mid u\)。于是
\[
H=\begin{pmatrix}y&-x\\u&v\end{pmatrix}\in\Gamma_0(9),
\qquad H(x,y)^T=(0,1)^T.
\tag{18}
\]
通过整数 Euclid 将 \(H\) 分解为 \(S,T^{\pm1}\) 词，再沿 (13) 的有限陪集表编译为正向宏。因此任意合法核心有限步达到 \(K(0,b)\)。

最后三步：

1. 平均单点 \(-4b\) 和三个零，得到四份 \(-b\)，留一个零；
2. 取两份 \(b\) 与两份 \(-b\)，得到四个零；
3. 对剩下两份 \(b\) 和两份 \(-b\) 再平均。

全部归零。若核心已经全零，直接结束。

结合两步入口，九元的 \(G=1\) 充分性得证；必要性是旧模3障碍。

## 6. 这个结果在整体路线中的位置

这里采用单维数有限陪集证明，是因为全部36条回路都有公式、所有主元自动是2的幂；没有为九元另做宏搜索。它证明旧工具可以迁移到合数元数，但迁移需要新的正向种子 (7)，不能只把旧代码的平均元数换成4。

更一般地，对偶数平均元数 \(p\)，旧双块矩阵
\[
T_j=\begin{pmatrix}-(p+1)&j\\-(2p+1)&2j\end{pmatrix}
\]
均满足
\[
\boxed{(T_{p/2}\Sigma)^2=-(p/2)I.}
\tag{19}
\]
这是一个对所有偶数元数成立的种子公式。但取得这个逆不自动提供全部根和终端覆盖。四平均里 \(p/2=2\)，恰好使 \(D=\Delta(2)\) 与 \(F_2\) 的倍率互为倒数，完成 (8)–(9)；一般偶数 \(p\) 仍需另查。

本轮[任意元数线性阈值](../arbitrary_arity_linear_threshold.md)已经解决所有充分大维数，因此不必无止境地逐 \(n\) 建群。九元属于剩余有限临界带的补齐。四平均仍待证明 \(7,11,13,15\) 的 \(G\) 充分性。

该控制器保证有限步，不保证最短解，也未给出展开后路径的统一位长多项式界；一位额外二进精度并非本算术证明的结论。

## 7. 精确核验

入口：

~~~text
python work/run_verifications.py --id four-average-nine-complete
~~~

脚本 [verify_four_average_nine_complete.py](../../../work/verify_four_average_nine_complete.py)：

- 独立核对全部72个本原模9行、12个陪集和36条回路；
- 对宏叶子的两个基输入做真实原位置重放；
- 检查全部合法模3重数类型及每个单点选择，共144个入口；
- 50个大整数入口与 Bezout 输送；
- 6个随机筛选的原始输入经完整宏词归零，并另用 Fraction 仅按索引独立重放。

实际输出：

~~~text
four-average n9 positive seeds and complete Schreier cover: PASS 36 72 8
four-average n9 universal-entry finite audits: PASS 144 50
four-average n9 literal full consensus paths: PASS 6 621
four-average nine-position complete criterion: PASS
~~~

[完整序列记录](../../../work/four_average_nine_witnesses.json)采用1基索引。最长样本621步，只是当前直接编译器的输出；不代表九元最短步数或本构造的最坏长度。

原子词以有向无环表达式保存，共同尺度从来不作为额外物理操作执行。全部成功序列最终都从原始数值重放，排除了只在规范化参数上归零的误判。
