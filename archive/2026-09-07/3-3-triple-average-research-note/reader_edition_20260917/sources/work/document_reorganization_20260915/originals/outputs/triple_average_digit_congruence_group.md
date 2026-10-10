# 数字算子的完整同余群：平衡生成、循环扩张与有理轨道分类

日期：2026-09-10。本文将[一次三份复制定理](triple_average_one_tripling_stabilization.md)中的向量轨道结论加强为完整的算术群等式。一般 n 的原维数充分性仍开放；这里的正向实现发生在副本空间。

## 1. 总定理

设 \(n\ge5\)，\(A=\{x\in\mathbb Z^n:\sum_i x_i=0\}\)。在 \(A\) 上使用基
\[
f_i=e_i-e_n,\quad 1\le i<n,
\]
并令 \(\eta=(1,\ldots,1)^T\in\mathbb Z^{n-1}\)。

**平衡生成定理。** 坐标置换与四个互异下标的平衡剪切
\[
E_{ij;k\ell}(a)=I+a(e_i-e_j)(e_k^T-e_\ell^T),\quad a\in\mathbb Z,
\tag{1}
\]
生成整个群
\[
\mathcal H_n=\{M\in GL_n(\mathbb Z):M\mathbf1=\mathbf1,
\ \mathbf1^TM=\mathbf1^T\}.
\tag{2}
\]
限制到 A 后，得到准确的同余群
\[
H_n=\{B\in GL_{n-1}(\mathbb Z):B\eta\equiv\eta\pmod n\}.
\tag{3}
\]

进一步设 \(2\le q\le n-2\)、\(\gcd(q,n)=1\)，令
\[
(K_qx)_i=\sum_{a=0}^{q-1}x_{qi+a},\quad i\in\mathbb Z/n\mathbb Z,
\qquad L=\operatorname{ord}_n(q).
\]
记 \(B_q=K_q|_A\)。

**数字同余群定理。** 在 A 上，数字算子和全部坐标置换恰生成
\[
\boxed{\Gamma_n(q)=
\{B\in GL_{n-1}(\mathbb Z):
B\eta\equiv q^j\eta\pmod n\text{，某个 }j\in\mathbb Z\}.}
\tag{4}
\]
而且这是分裂循环扩张
\[
\Gamma_n(q)=H_n\rtimes\langle B_q\rangle,
\qquad B_q^L=I,\quad |\langle B_q\rangle|=L.
\tag{5}
\]
每个 \(\Gamma_n(q)\) 元素的射影作用，都由 q 份复制上的正向 q 平均及位置重新标号实现。

这给出一般维数的真实同余群等式，不是有限模像或 Zariski 稠密的外推。对 q=3，它覆盖每个 \(n\ge5,3\nmid n\)。

## 2. 为什么 level 恰为 n

以 \((f_1,\ldots,f_{n-1},e_n)\) 为 \(\mathbb Z^n\) 的整基。保和矩阵必写成
\[
M=\begin{pmatrix}B&b\\0&1\end{pmatrix}.
\]
常值向量在此基中的坐标为 \((\eta,n)\)，因此固定常值等价于
\[
B\eta+nb=\eta.
\tag{6}
\]
给定 \(B\in GL_{n-1}(\mathbb Z)\)，它能整系数提升为 (2)，当且仅当 (3) 成立；此时 \(b=(\eta-B\eta)/n\) 唯一。

所以 n 记录的是零和格与常值方向之间的积分拼接。它不只是某个二次型的判别式，也不是合法参数集合单独给出的模数。这个解释同时适用于合数与素数幂，不需要按素数逐个猜同余群。

## 3. 第一步：将一列化为标准单位向量

显然 (1) 及置换属于 \(\mathcal H_n\)。反向取任意 \(M\in\mathcal H_n\)，令 \(x=Me_n\) 为其末列。

它的总和为 1，且差分 gcd 为 1。否则若所有 \(x_i\equiv c\pmod d\)，对整系数、固定常值的 \(M^{-1}\) 应用同余，得到 \(e_n\equiv c\mathbf1\pmod d\)，迫使 d=1。

[平衡欧几里得正规形](triple_average_one_tripling_stabilization.md)第5节证明：至少五个整数坐标，总和 s、差分 gcd 为1时，可由 (1) 和置换化为 \((0^{n-2},1,s-1)\)。其证明每轮至多两次剪切，将最小正差至少减半，随后利用两个零位置完成清除。

取 s=1，便可左乘一个已生成元素，使 M 的末列等于 \(e_n\)。剩下只需生成该列的稳定子。

## 4. 第二步：完整生成列稳定子

置 \(m=n-1\)。固定末列 \(e_n\) 的矩阵唯一写成
\[
\Psi(C)=
\begin{pmatrix}
C&0\\ \mathbf1^T-\mathbf1^TC&1
\end{pmatrix},
\qquad C\in GL_m(\mathbb Z),\quad C\mathbf1=\mathbf1.
\tag{7}
\]
\(\Psi\) 是群同态。对 m 个坐标上的三个互异下标，
\[
S_{i;k\ell}(a)=I+a e_i(e_k^T-e_\ell^T)
\]
的提升恰为 \(E_{i,n;k\ell}(a)\)，所以全部可用。

下面证明这些三下标剪切与置换生成所有固定常值的 \(GL_m(\mathbb Z)\)。改用整基
\[
(e_1,\ldots,e_{m-1},\mathbf1_m),\quad d=m-1.
\]
目标群在该基中恰为
\[
\left\{\begin{pmatrix}U&0\\r&1\end{pmatrix}:
U\in GL_d(\mathbb Z),\ r\in\mathbb Z^{1\times d}\right\}.
\tag{8}
\]

首先，对 \(i\ne k<m\)，\(S_{i;k,m}(a)\) 变成 \(\operatorname{diag}(I+a e_i e_k^T,1)\)。配合前 d 个坐标的置换，经典整数欧几里得消元生成所有 \(\operatorname{diag}(U,1)\)。

其次，取 \(k\ne\ell<m\)，记 \(r=e_k^T-e_\ell^T\)。\(S_{m;k\ell}(1)\) 在新基中为
\[
\begin{pmatrix}I-\mathbf1_d r&0\\r&1\end{pmatrix}.
\]
因 \(r\mathbf1_d=0\)，其左上块是整系数幺幂矩阵，逆为 \(I+\mathbf1_d r\)。用已经生成的对角块将它消去，便得到纯平移
\[
N_r=\begin{pmatrix}I&0\\r&1\end{pmatrix}.
\]
再令 \(U=I+e_\ell e_k^T\)。有 \(rU=-e_\ell^T\)，故
\[
\operatorname{diag}(U^{-1},1)N_r\operatorname{diag}(U,1)=N_{-e_\ell^T}.
\]
取逆、置换及整数次幂，生成任意平移行 r。因此 (8) 完整生成，(7) 的列稳定子也完整生成。

结合第3节的列归约，证明 \(\mathcal H_n\) 等于平衡剪切与置换生成的群。使用 n>=5 的地方是前面的向量正规形；列稳定子的证明本身只需 d>=2。

## 5. 数字算子给出精确循环扩张

由离散梯度恒等式
\[
K_qD=DF_q,\quad D=I-S,\quad(F_qx)_i=x_{qi},
\]
可知 \(B_q\) 在 \(A_\mathbb Q\) 上共轭于有限置换，行列式为 \(\pm1\)。它本身整系数，所以 \(B_q\in GL_{n-1}(\mathbb Z)\)。三进数字证明的同一推广还给出
\[
K_q^L=I+\frac{q^L-1}{n}J,
\]
因此 \(B_q^L=I\)。

全空间上 \(K_q\mathbf1=q\mathbf1\)，在第2节的基中得到
\[
B_q\eta\equiv q\eta\pmod n.
\tag{9}
\]
因 q 模 n 的阶为 L，\(B_q\) 的阶也恰为 L。

所有坐标置换均属于 \(H_n\)。另一方面，[循环区间剪切公式](triple_average_one_tripling_stabilization.md)第10节表明：\(K_q\) 与置换及其逆生成每个平衡剪切。第4节遂保证它们已经包含整个 \(H_n\)。

现在若整数矩阵 B 满足 \(B\eta\equiv q^j\eta\pmod n\)，则 \(B_q^{-j}B\in H_n\)，从而 B 属于实际生成群。反向由 (9) 与乘法立即成立，证明 (4)。模 n 的倍率映射以 \(H_n\) 为核，以 \(\langle q\rangle\) 为像，并由 \(B_q\) 提供截面，故扩张 (5) 分裂。

## 6. 有限指数与正向实现

\(GL_{n-1}(\mathbb Z)\) 在模 n 的本原向量上可迁；这由整数初等消元或 Smith 正规形给出。模 n 的本原向量总数为
\[
n^{n-1}\prod_{p\mid n}(1-p^{-(n-1)}).
\]
所以
\[
[GL_{n-1}(\mathbb Z):H_n]
=n^{n-1}\prod_{p\mid n}(1-p^{-(n-1)}),
\]
\[
[GL_{n-1}(\mathbb Z):\Gamma_n(q)]
=\frac{n^{n-1}}{L}\prod_{p\mid n}(1-p^{-(n-1)}).
\tag{10}
\]
它们都是含主同余子群的有限指数算术群。

在 q 份复制上，\(P_q=K_q/q\) 是一层真实 q 平均。在零和空间
\[
P_q^L=q^{-L}I,
\]
所以 \(P_q^{-1}\) 的射影作用由 \(P_q^{L-1}\) 正向实现。置换只改变位置账本。因此 \(\Gamma_n(q)\) 的全部射影群作用都由这一固定字母表的正向词实现。整数平衡生成证明无需把形式逆非法地当作原子平均。

这里的算术群定义在整数根格上；局部化分母进入的是实际收缩尺度。不能将它误写为已经生成整个 \(GL_{n-1}(\mathbb Z[1/q])\) 的射影群。

## 7. 全部有理射影轨道的显式分类

取非零本原 \(x\in A\)，令
\[
d=G(x)=\gcd_{i,j}(x_i-x_j),\qquad c=x_1\pmod d.
\]
有 \(\gcd(c,d)=1\) 且 \(d\mid n\)：本原性给出第一式，零和给出 \(nc\equiv0\pmod d\)，再得第二式。

平衡轨道定理证明，\(H_n\) 在本原向量上的轨道恰由 \((d,c)\) 分类。\(B_q\) 保持本原性和 d，并将 c 变成 qc：模任意 \(d\mid n\)，\(K_q\) 把常值 c 送到 qc，且 \(K_q^{-1}\) 的分母只含 q，故反向同余也成立。

有理射线的本原代表还可差一个负号。因此完整分类为
\[
\boxed{\Gamma_n(q)\backslash\mathbb P(A_\mathbb Q)
\ \cong\ \coprod_{d\mid n}
(\mathbb Z/d\mathbb Z)^\times/\langle-1,q\rangle.}
\tag{11}
\]
d=1 的一项按单点处理。每个标签有显式代表
\[
(c^{n-2},c+d,-(n-1)c-d).
\tag{12}
\]
这不是仅给出轨道数的上界：必要性、标签可实现性及同标签之间的真实群输送都已证明。

特别地，合法的 d=1 方向始终只有一个轨道，代表是 \((0^{n-2},1,-1)\)。一般 q 与 n 互素时，局部必要条件恰要求 d=1，所以轨道分类直接解释 q 份复制后的充分性。

对素数 p，射影轨道数为
\[
1+\frac{p-1}{|\langle-1,q\rangle\subset\mathbb F_p^\times|}.
\tag{13}
\]
q=3 时，p=7、11、17、23、29 都有两个轨道；p=13 有三个。但所有情形都只有一个合法轨道。这里分类的是高秩群的有理直线轨道，不是宣称已经分类全部旗标抛物边界，也不是原二维宏群的 cusp 数。

## 8. 对原问题究竟推进了什么

此前的高秩交换定理只识别 Zariski 闭包；本文对一个明确的副本宏库，进一步识别了完整整数算术群、同余 level、分裂扩张及全部有理直线轨道。群、正向词和终端代表在稳定化端已经一致。

其自然结构是：常值方向与零和格的积分拼接给出模 n 向量；平衡初等变换生成其稳定子；分圆 Hilbert90 数字周期添加倍率 q 的循环作用；整数欧几里得正规形将合法点送到一条根。

这也说明没有必要要求每个宏始终回到某个二维 B 核：在完整根格中，全部合法方向本来属于一个高秩算术轨道。限制到固定二维平面的稳定子可能产生更多轨道，不能将限制后的困难当成整个算术群的困难。

但正向实现仍使用 nq 个位置。原 n 维任何非空三平均词都不能在整个零和空间上可逆；因此不能把此群等式直接下降为原 n 维生成定理。值得继续检验的原维数接口，是[平坦三重块与载体](triple_average_structural_picture_audit.md)第9、10节：其参数秩已经足以容纳高秩算术作用，局部逆也已存在，尚缺整体正向实现与终端覆盖。

## 9. 核验契约

脚本：[verify_balanced_congruence_group.py](../work/verify_balanced_congruence_group.py)，统一ID为 `balanced-digit-congruence-group`。

- 380 个列稳定子基变换、初等块、平移生成公式。
- 160 个直接从主同余矩阵构造的独立输入，核对整系数提升、平衡列消元及列稳定子接口。
- 118 个 q、n 参数对，核对数字根格矩阵、倍率 level 和完整周期。
- 492 个显式射影代表的平衡／数字迭代，核对全部轨道不变量。

无限量词由第2至7节的生成和正规形证明承担。有限核验不替代整数初等生成定理，也不证明原维数复制消去。
