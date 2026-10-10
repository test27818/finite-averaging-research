

# C7.2 只要求在有限环上取逆

先证明一个稍一般的入口引理。设整数 \(p\ge2\)，
\[
n=2p+r,\qquad1\le r<p,\qquad\gcd(p,n)=1.
\]
记 \(\mathcal P\) 为 \(n\) 的不同素因子集合，\(d=|\mathcal P|\)，以及
\[
M=\operatorname{rad}(n)=\prod_{\ell\mid n}\ell,\qquad R=\mathbb Z[1/p].
\]
计算始终允许真实 \(p\) 平均产生的 \(R\) 分母。称状态有完整见证，如果它在每个 \(\ell\mid n\) 下不全同余。合法本原整数输入具有此性质。

对已具有一个等值 \(p\) 块的状态，写成
\[
(a^p,c_1,\ldots,c_m),\qquad m=n-p=p+r.
\]
选单点角色 \(i\)，平均该单点与块中的 \(p-1\) 个位置，留下最后一份旧块值作为新的第 \(i\) 单点。真实变化是
\[
(a,c_i)\longmapsto\left(\frac{(p-1)a+c_i}{p},a\right).\tag{2}
\]
所有其他单点位置不变。被留下的旧块位置接替单点角色，故每一步都有原位置账本，不需要搬动数值或增加副本。

式 (C7.2) 的矩阵及形式逆为
\[
E=\begin{pmatrix}(p-1)/p&1/p\\1&0\end{pmatrix},
\qquad E^{-1}=\begin{pmatrix}0&1\\p&-(p-1)\end{pmatrix}.
\]
二者在每个 \(\ell\mid n\) 下可逆并固定常值向量。因此每个真实交换自动保持完整见证。形式逆在这里首先只用于证明安全性。

令 \(\lambda=-1/p\)。对每个 \(\ell\mid n\)，该交换模 \(\ell\) 的阶可取
\[
o_\ell=
\begin{cases}
\operatorname{ord}_\ell(\lambda),&p\not\equiv-1\pmod\ell,\\
\ell,&p\equiv-1\pmod\ell.
\end{cases}
\]
第一种情况有两个不同特征值 \(1,\lambda\)。第二种情况 \(E=I+N\)、\(N^2=0\)，故 \(E^\ell=I\)。这包括 \(\ell=2\) 的幺幂情况。

取
\[
L=\operatorname{lcm}_{\ell\mid n}o_\ell.
\]
则同一角色连续交换 \(L\) 次在模 \(M\) 上是恒等，交换 \(L-1\) 次在模 \(M\) 上是逆。全部都是正向真实平均。

这不是有理数值上的逆。例如 \(p=3\)、\(M=7\)，两次交换将 \((a,c)=(0,1)\) 变成 \((2/9,1/3)\)，而形式逆给 \((1,-2)\)。两者模7相同，实际数值不同。入口只要求最终同余见证正确，因此这种逆恰好足够。

# C7.3 三个单点给出显式见证转移

令
\[
\delta_i=c_i-a,\qquad \delta=(\delta_1,\ldots,\delta_m)^T.
\]
在 \(R^m\) 上，式 (C7.2) 的实际差分矩阵为
\[
A_i=I+v_i e_i^T,\qquad v_i=\lambda\mathbf1-e_i.
\tag{3}
\]
其第 \(i\) 差分乘 \(\lambda\)，其他差分加 \(\lambda\delta_i\)。有
\[
e_i^Tv_i=\lambda-1,\qquad
A_i^{-1}=I-\lambda^{-1}v_ie_i^T.
\]

取三个互异角色 \(i,j,k\)。由于 \(m=p+r\ge3\)，这些角色始终存在。令
\[
T=A_k^{-1}A_jA_k,\quad w=e_k-e_j,\quad h=e_j^T+\lambda e_k^T.
\]
直接计算：
\[
A_k^{-1}v_j=v_j-v_k=w,\qquad e_j^TA_k=h,\qquad T=I+wh.
\]
又 \(e_i^Tw=0\)、\(hv_i=\lambda(1+\lambda)\)。因此
\[
\boxed{[T,A_i]:=TA_iT^{-1}A_i^{-1}
=I+(1+\lambda)(e_k-e_j)e_i^T.}\tag{4}
\]
其中 \(1+\lambda=(p-1)/p\)。证明可在整个 \(R^m\) 上完成：共轭将 \(v_i\) 改成 \(v_i+\lambda(1+\lambda)w\)，再右乘 \(A_i^{-1}\)，系数恰除去 \(\lambda\)。

把 (4) 中每个形式逆换成第2节的正向 \(L-1\) 次幂，得到实际词 \(W_{ijk}\)。按时间顺序执行的八段为
\[
A_i^{L-1},\ A_k,\ A_j^{L-1},\ A_k^{L-1},
\ A_i,\ A_k,\ A_j,\ A_k^{L-1}.\tag{5}
\]
总计 \(4L\) 个原子交换。这个词满足模 \(M\) 的精确恒等式
\[
W_{ijk}\equiv I+c(e_k-e_j)e_i^T,\qquad c=(p-1)/p.
\tag{6}
\]
没有宣称 (5) 在有理数上等于 (4)。

因 \(((e_k-e_j)e_i^T)^2=0\)，重复该真实词 \(t\) 次给出
\[
\delta_j\mapsto\delta_j-ct\delta_i,\qquad
\delta_k\mapsto\delta_k+ct\delta_i,\qquad
\delta_h\mapsto\delta_h\ (h\ne j,k)
\pmod M.\tag{7}
\]
这是正向路径的单个分支，不是矩阵线性组合或分支求和。

# C7.4 失效素数恰好能由保留位置承接

定义
\[
\mathcal B=\{\ell\mid n:\ell\mid p-1\},\qquad b=|\mathcal B|.
\]
对 \(\ell\notin\mathcal B\)，\(c\) 为模 \(\ell\) 单位，式 (C7.7) 可以转移一个非零见证。对 \(\ell\in\mathcal B\)，式 (C7.7) 在全部差分上为恒等。

由于
\[
\gcd(p-1,n)=\gcd(p-1,r+2),
\]
所有失效素数都整除 \(r+2\)。特别地
\[
\boxed{b\le r.}\tag{8}
\]
否则 \(r+2\ge\prod_{\ell\in\mathcal B}\ell\ge2^{r+1}>r+2\)，矛盾。

这正是容量与算术的配合：可以为每个失效素数保留一个单点见证，其总数不超过实际剩余位置 \(r\)。其他素数由 (7) 在这些保护不变的前提下逐一处理。

在端点 \(r=1\)，失效素数至多只有3，因为
\[
\gcd(p-1,2p+1)=\gcd(p-1,3).
\]
这解释了为什么一个保留位置就足够；不涉及 \(2p+1\) 有多少个其他素因子。

更具体地，端点模 \(M\) 有 \(\lambda=2\)，所以交换子的系数恰为3，式 (C7.7) 是在两个目标单点之间转移 \(3t\delta_i\)。原来依赖 \(2^k\) 的同步避让由一个明确的加法剪切取代。

这也解释该入口机制在 \(2p\) 与 \(2p+1\) 的区别。对奇素数 \(p\)，若形式上取 \(r=0,n=2p\)，则失效素数为2，而保留位置为零，式 (C7.8) 不再成立；非零相反双块 \((a^p,(-a)^p)\) 正有不可消除的模2障碍。增加到 \(r=1\) 后，失效素数至多为3且已有一个位置承接。这个说明与已证的 \(2p\) 下界相容，不是说所有 \(2p\) 元输入都不可达。

# C7.5 无条件建立两个合法 \(p\) 块

**两块入口引理。** 在第2节的假设下，每个合法输入都能有限步变成具有完整见证的
\[
(a^p,b^p,c_1,\ldots,c_r).
\tag{9}
\]

先固定原位置0。对每个 \(\ell\mid n\)，保护位置0及另一个与它不同余的位置，总计至多 \(d+1\) 个位置。保护集外足够选出 \(p\) 个位置：若 \(d\ge p+r\)，则
\[
n\ge2^d\ge2^{p+r}>2(p+r)\ge2p+r=n,
\]
矛盾。所以 \(d+1\le p+r=n-p\)。在保护集外平均 \(p\) 个位置，得到一个 \(p\) 块与 \(m=p+r\) 个单点，完整见证由未选位置保留。

对每个 \(\ell\in\mathcal B\)，选一个 \(\delta_i\ne0\pmod\ell\) 的单点角色，并把它列入保留集合 \(J\)。完整见证保证这样的单点存在。由 (8)，可补足至恰好 \(|J|=r\)。从 \(J\) 中固定一个目标角色 \(j\)。

假设目标在某个 \(\ell\notin\mathcal B\) 处缺失见证。选择 \(\delta_i\ne0\pmod\ell\) 的角色 \(i\ne j\)，并选任意 \(k\notin\{i,j\}\)。令 \(Q=\prod_{q\in\mathcal P\setminus\mathcal B}q\)。CRT 给出正整数 \(t<Q\)，使
\[
t\equiv1\pmod\ell,\qquad
t\equiv0\pmod q\quad(q\in\mathcal P\setminus(\mathcal B\cup\{\ell\})).
\]
执行 (5) 共 \(t\) 次。式 (C7.7) 给目标新增非零差分 \(-c\delta_i\pmod\ell\)，其他非失效素数处的目标差分不变；所有失效素数处的全部差分都不变。此前保留在 \(J\) 中的见证因而仍在。

至多 \(d-b\) 个阶段后，目标 \(j\) 在全部非失效素数处都非零，而 \(J\) 在每个失效素数处仍有见证。

最后保留 \(J\) 的 \(r\) 个单点，平均其他恰好 \(p\) 个单点。未选的旧 \(p\) 块和 \(J\) 在每个 \(\ell\mid n\) 下都不全同余，所以最后一步安全，得到 (9)。全过程在原位置执行，至此引理得证。

每个中间交换都自动安全；保留的是单点角色，原位置随 (2) 更新。不能把角色 \(J\) 误解为始终冻结同一批物理位置。

### 算法可以比逐素数CRT幂短得多

CRT只用于给最直接的存在证明。实际选择 \(t\) 时，可令
\[
\delta_j-ct\delta_i\ne0\pmod q
\]
同时覆盖 \(i,j\) 在所有非失效素数处的支持并集。每个相关素数只禁止一个 \(t\) 类，因此可调用[已有短区间筛选](../upper_band/prime_arity_upper_band_three_value_reduction.md)。

对素数 \(p\ge5\)、\(n<3p\)，筛选在 \(1\le t\le p-1\) 内完成。每阶段严格增加目标支持，得到两块入口的显式上界
\[
2+4L(p-1)(d-b).\tag{10}
\]
这只是有限性与实际算法改进，不是位长多项式或最短路径保证。程序对大参数只指数化固定四角色矩阵或保存重复词，不展开巨大重复数组。
