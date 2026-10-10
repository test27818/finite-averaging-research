

# C25.2 上半带的整数坐标与真实对合

设 p>=5 为素数、1<=r<p、n=3p+r。由[上半带全输入归约](prime_arity_upper_band_three_value_reduction.md)，只需处理
\[
\mathcal K(a,z)=\bigl(a^{2p},(-2a+rz)^p,(-pz)^r\bigr),
\qquad \gcd(a,z)=\gcd(a+pz,n)=1.
\tag{1}
\]
这是旧坐标 y=a+pz 的整幺模变换。记三种实际值为 A、B、C。

使用[两种载体对合](../../history/prime_arity_three_p_remaining_gap.md)的原位置构造：平均两个组成相同的 p 组，再平均其余 p 组，保留 r 份旧 A 或旧 B 作新载体。每个返回恰有三个原子平均。

保留 A 时取 s=p-3j，两个相同组各取 (A^(2j),B^j,C^s)。在 (a,z) 上的整数矩阵及实际尺度为
\[
\frac1p A_j,\qquad
A_j=\begin{pmatrix}0&-d_j\\-1&0\end{pmatrix},
\quad d_j=p^2-nj.
\tag{2}
\]
允许 j 的连续整数区间是
\[
I_A=\left[
\left\lceil\frac{2p-r}{6}\right\rceil,
\min\left(\left\lfloor\frac{2p-r}{4}\right\rfloor,
\left\lfloor\frac p3\right\rfloor\right)\right]\cap\mathbb Z.
\tag{3}
\]

保留 B 时取 s=p-r-3k，两个相同组各取 (A^(2k+r),B^k,C^s)。对应
\[
\frac1p B_k,\qquad
B_k=\begin{pmatrix}r&b_k\\2&-r\end{pmatrix},
\quad b_k=nk-p^2+rp,
\tag{4}
\]
\[
I_B=\left[
\max\left(0,\left\lceil\frac{2p-3r}{6}\right\rceil\right),
\left\lfloor\frac{p-r}{3}\right\rfloor\right]\cap\mathbb Z.
\tag{5}
\]
直接有
\[
A_j^2=d_j I,\qquad B_k^2=\mu_k I,
\quad \mu_k=r^2+2b_k.
\]
d_j、mu_k 模 n 都等于 p²，故非零且与 n 互素。这些返回和射影逆都有真实正向实现，重复一次就是六原子的全局非零标量词。返回在所有 ell|n 处保持合法性。

# C25.3 两个对角方向之间的显式交换子

假设 I_A、I_B 各含两个相邻整数 j,j+1 和 k,k+1。记
\[
d=d_j,\quad e=d-n,\qquad
\mu=\mu_k,\quad\nu=\mu+2n,
\quad R=\mathbb Z[1/|de\mu\nu|].
\]
四个对合已经提供两个正向可逆的上三角变换：
\[
D=A_j^{-1}A_{j+1}
=\begin{pmatrix}1&0\\0&e/d\end{pmatrix},
\quad
T=B_k^{-1}B_{k+1}
=\begin{pmatrix}1&rn/\mu\\0&\nu/\mu\end{pmatrix}.
\tag{6}
\]
它们的交换子为
\[
\boxed{DTD^{-1}T^{-1}=U\left(\frac{rn^2}{e\nu}\right).}
\tag{7}
\]
这是一条对所有满足容量条件的 p,r 恒成立的公式，不是逐参数的周期搜索。

下面核对共同局部化环，避免将任意分母视为免费操作。有 gcd(d,e)=1；又
\[
\gcd(\mu,\nu)=
\begin{cases}1,&r\text{ 奇},\\2,&r\text{ 偶}.\end{cases}
\]
这是因为 gcd(mu,n)=1 且 mu 的奇偶性与 r 相同。r 偶时 n 奇，d、e 奇偶相反，所以 Z[e/d,d/e] 已含 1/2。r 奇时 mu、nu 已互素。两种情形都得到
\[
\mathbb Z[e/d,d/e,\nu/\mu,\mu/\nu]=R.
\tag{8}
\]

对任意 x，D 共轭 U(x) 将其参数乘 d/e；T 共轭 U(x) 将参数乘 mu/nu，T 的上平移部分在此消去。结合逆共轭、根参数的加法和取负，(7)、(8) 给出完整 U(rn²R)。由
\[
A_jU(x)A_j^{-1}=L(x/d)
\]
再得到完整 L(rn²R)。所有操作和逆均已有原位置实现。

因此令 h=rn²，调用[偶数深同余引理](../../history/prime_arity_even_middle_congruence_and_eighteen.md)，即有
\[
\boxed{\Gamma(h^2,R)=\Gamma(r^2n^4,R)
\text{ 的作用正向可执行}.}
\tag{9}
\]
R 有无限多个单位：相邻 d、e 互素且相差 n>2，不可能同时绝对值为1。(9) 使用 Morris 2007 定理6.1(2)、Serre 对有理数域 S 整数 SL2 的强同余子群性质以及已证任意有限环消元。外部来源与原文访问边界沿用所引深同余文档，不由有限样本证明这两项外部定理。

与下半带相比，这里没有交换 2p 块与 p 块的免费角色对称。两组载体返回分别给出 (6)，通过它们的交换子获得根，所以自然多出一个 n 因子。不能将下半带的换块矩阵直接搬来。

# C25.4 一个所有 p 都适用的内部区间

**容量定理。** 对所有素数 p>=13，若
\[
10\le r\le p-3,
\quad\text{即}\quad
\boxed{3p+10\le n\le4p-3,}
\tag{10}
\]
则 I_A、I_B 均至少含两个整数，故第 3 节全部结论成立。

证明 I_B：允许 s 的区间是 [0,min(floor(r/2),p-r)]，且 s=p-r 模3。r>=10 使 floor(r/2)>=5。若 p-r>=5，则 0,...,5 至少给每个模3类两个代表；若 p-r=3，则选 s=0,3；若 p-r=4，则选 s=1,4。

证明 I_A，先设 p>=23。若 r<=2p/3，则 (3) 的上界为 floor(p/3)，选 0,...,5 中与 p 同余模3的两个 s 即可，其他容量由 r<=2p/3 保证。若 r>2p/3，则 j 的实区间为 [(2p-r)/6,(2p-r)/4]，长度
\[
\frac{2p-r}{12}\ge\frac{p+3}{12}>2,
\]
所以至少有两个整数。p=13 只需 r=10，此时 I_A={3,4}；p=17 的 r=10,...,14 均有 I_A={4,5}；p=19 的 r=10,...,13 有 {5,6}，r=14 有 {4,5,6}，r=15,16 有 {4,5}。证毕。

(3)、(5) 是更精确的适用条件，个别 r<10 也可覆盖，例如 p=13,r=9。式 (C25.10) 取一个无需逐 p 分类的统一范围。
