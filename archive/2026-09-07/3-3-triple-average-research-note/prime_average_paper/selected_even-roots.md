

# C13.3 偶数核心的同一整数格

令 r=2t，n=2p+r。整数零和核心可以写成
\[
\mathcal K(a,z)=(a^p,(rz-a)^p,(-pz)^r),\qquad \gcd(a,z)=1.
\tag{4}
\]
因为 gcd(p,r)=1，式 (C13.4) 给出全部整数三块零和状态，其本原性恰为 gcd(a,z)=1。

置 y=a+pz。两种差为
\[
a-(-pz)=y,\qquad a-(rz-a)=2y-nz.
\]
由 gcd(y,z)=1 得精确等式
\[
\boxed{G=\gcd(y,n).}
\tag{5}
\]
这里没有遗漏模 2 条件。旧坐标 a=tz+v 给 y=v+(p+t)z，模 2 恰为 v+(t+1)z；奇素数 ell|n 时 y=v 模 ell。旧两条合法条件实际上是 (5) 的不同局部写法。

沿用[原位置对合](prime_arity_band_period_and_involutions.md)。允许奇数 s 满足 max(1,2r-p)<=s<=r，令 i=(p-s)/2。平均两个不交组
\[
(a^i,b^i,c^s),\qquad
(a^{p-r-i},b^{p-i},c^{r-s}),
\tag{6}
\]
留下 r 份原 a。其 (a,z) 矩阵为
\[
\frac1pJ_s,\qquad
J_s=\begin{pmatrix}0&d_s\\-1&0\end{pmatrix},\quad
d_s=\frac{pr-ns}{2}.
\tag{7}
\]
因为 s、p 奇，d_s 为奇数；对每个 ell|n，d_s=-p^2 模 ell。故 d_s 非零且与 n 互素，J_s^2=-d_s I，返回及射影逆均有真实正向实现。

在 (z,y) 整幺模坐标中，同一返回的矩阵为
\[
\frac1pK_i,\qquad
K_i=\begin{pmatrix}p&-1\\ni&-p\end{pmatrix},\quad
K_i^2=(p^2-ni)I.
\tag{8}
\]
交换两个 p 块的角色分别对应
\[
\Sigma=\begin{pmatrix}-1&r\\0&1\end{pmatrix}
\quad\hbox{和}\quad
S=\begin{pmatrix}1&0\\n&-1\end{pmatrix}.
\]
块角色交换只是更新原位置账本。

# C13.4 任意内部偶余量都有深主同余控制

现设 4<=r<=p-3。s=r-1、r-3 都满足 (6) 的容量。记
\[
d=\frac{pr-n(r-1)}2,\qquad e=d+n,\qquad
R=\mathbb Z[1/|de|],\quad h=rn.
\]
有 gcd(d,e)=1，d、e 均奇且与 n 互素。又 |de|>1，所以 R 有无限多个单位。

令 J=J_{r-1}、Q=J_{r-3}。直接计算
\[
D=J^{-1}Q=\operatorname{diag}(1,e/d),\qquad
\Sigma D\Sigma D^{-1}=U(rn/e).
\tag{9}
\]
由 gcd(d,e)=1，
\[
\mathbb Z[e/d,d/e]=\mathbb Z[1/(de)]=R.
\]
用 D 的共轭、逆共轭及根参数相加、取负，得到 U(hR)。又
\[
JU(x)J^{-1}=L(-x/d)
\]
给 L(hR)。全部因子及其逆均有正向实现。

**深同余引理。** 对 R=Z[1/q]、q>1 和正整数 h，使用下述外部定理时，
\[
\boxed{\Gamma(h^2,R)\subseteq
E_h:=\langle U(hR),L(hR)\rangle.}
\tag{10}
\]

证明：Morris 2007 定理 6.1(2) 应用于有限指数子群 Gamma(h,R)。其中全部初等矩阵恰为两种根，故 E_h 有限指数。Serre 对有理数域的 S 算术 SL2 强同余子群性质给某个 Gamma(M,R) 包含于 E_h；可令 h²R 整除 MR。

在有限环 B=R/MR 中取 g=(a,b;c,d) 属于 Gamma(h²,R) 的像。可用 U(hk) 使 u=a+hkc 在 B 中为单位：在除 h 的素数处 a=1；在不除 h 的素数处，用 CRT 选择 k 避开至多一个坏类。置 v=b+hkd，则
\[
g=U(-hk)L(c/u)\operatorname{diag}(u,u^{-1})U(v/u).
\]
这些非对角参数都属于 hB，而且 u-1 属于 h²B。选择 t 属于 hB 使 ht=u-1（从整数的 h² 倍代表可选），便有
\[
\operatorname{diag}(u,u^{-1})
=U(h)L(t)U(-h/u)L(-tu).
\tag{11}
\]
所有参数都在 hB，可分别提升到 hR。因此 E_h 在模 M 覆盖 Gamma(h²,R) 的像，再用已包含的 Gamma(M,R)，得到 (10)。

这里有限环里的除法仅用于挑选允许根参数的剩余类；没有把任意模 M 单位当作 R 单位。也未使用仅在高秩成立的相对初等生成定理。

结合 (9)、(10)，每个内部偶余量都有真实可执行的
\[
\boxed{\Gamma((rn)^2,\mathbb Z[1/|de|]).}
\tag{12}
\]
它把无限轨道问题降为有限的同余轨道和单位尺度问题，但本身不保证所有有限轨道都有终端。r=2、r=p-1 各只有一个允许的标准对合，本文不将它们包含在 (12) 中。

外部来源与[端点同余闭合](../proofs/lower_band/prime_arity_endpoint_congruence_completion.md)一致：Morris, NYJM 13 (2007), 定理 6.1(2)；Serre, Annals of Mathematics 92 (1970), 489--527, [DOI](https://doi.org/10.2307/1970630)。此处将 Serre 定理用在 R=Z[1/65]，即 S={无穷处,5,13} 的有理数域特例；不是由 Z[1/2] 的特例推演得到。Morris 相关原文已在项目中核对；Serre 原文全文未取得，这里作为已发表外部定理引用，不声称自行证明或数值验证了该定理。
