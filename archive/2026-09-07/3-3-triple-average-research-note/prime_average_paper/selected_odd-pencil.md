本节设 $p\ge3$ 为奇素数、$1\le r<p$ 为奇数、$n=2p+r$。采用全系统核心 $K_{p,r}(a,z)$，并令 $u=z$、$v=a-rz/2$，故 $A=ru/2+v$、$B=ru/2-v$、$C=-pu$。

# C11.2 为什么改变来源，而不是在一张输出纤维里找第二点

旧内部奇余量证明用两个旧载体反射，其参数为 \(r,r-2\)；在 \(r=1\) 时第二个参数失效。新构造从两个等大块中先制造新载体，再只从旧载体取零份或一份参加输出。

置
\[
\epsilon=\left(\frac{p-r}{2}\bmod2\right)\in\{0,1\},\qquad
d=r-2\epsilon,\qquad
\alpha_0=-r,\quad \alpha_1=4-r.
\tag{2.1}
\]
两张表共用下面的公式。对 \(\alpha=\alpha_0,\alpha_1\)，先平均来源
\[
c_\alpha=(i,j,0),\qquad
i=\frac{p+\alpha}{2},\quad j=\frac{p-\alpha}{2}.
\tag{2.2}
\]
它从 \(A,B\) 各取 \(i,j\) 份，不使用旧 \(C\)。新均值记为 \(D\)，其中保留 \(r\) 份作为最终载体。剩余库存为
\[
\left(\frac{p-\alpha}{2},\frac{p+\alpha}{2},r,p-r\right).
\tag{2.3}
\]
取输出计数
\[
o_\alpha=(x,y,c,v_D)=
\left(
\frac{p+2r-\alpha-2\epsilon}{4},
\frac{p+\alpha-2\epsilon}{4},
\epsilon,
\frac{p-r}{2}
\right).
\tag{2.4}
\]
平均该 \(p\) 元组，再平均其余的 \(p\) 个位置，共三次平均返回同一 \((p,p,r)\) 形状。

### 2.1 对所有参数的容量证明

令
\[
s=p-r=4h+2\epsilon,\qquad h\ge0.
\]
由于 \(s\) 是正偶数，\(\epsilon=0\) 时 \(h\ge1\)。两组来源、输出及库存分别化为：

| 项 | \(\alpha_0=-r\) | \(\alpha_1=4-r\) |
|---|---|---|
| 来源 \((i,j,0)\) | \((2h+\epsilon,r+2h+\epsilon,0)\) | \((2h+\epsilon+2,r+2h+\epsilon-2,0)\) |
| 剩余库存 | \((r+2h+\epsilon,2h+\epsilon,r,4h+2\epsilon)\) | \((r+2h+\epsilon-2,2h+\epsilon+2,r,4h+2\epsilon)\) |
| 输出 | \((r+h,h,\epsilon,2h+\epsilon)\) | \((r+h-1,h+1,\epsilon,2h+\epsilon)\) |

总数都等于 \(p=r+4h+2\epsilon\)。唯一紧的比较是第二张表的第一库存：
\[
r+h-1\le r+2h+\epsilon-2
\quad\Longleftrightarrow\quad h+\epsilon\ge1,
\]
这正由 \(s>0\) 保证。第二来源的 \(j\) 非负也成立：\(\epsilon=0\) 时 \(h\ge1\)；\(\epsilon=1,h=0\) 时 \(j=r-1\ge0\)。所有其他比较直接成立。

因此这两张表在整个范围有效，连 \((p,r)=(3,1)\) 和 \(r=p-2\) 都无需额外处理。这里的 \(\epsilon\) 只是由整性决定的一位计数，不对应两套算术证明。

# C11.3 两张矩阵来自同一反射铅笔

在 \((a,z)\) 基中记 \(\beta=rj\)，实际返回为 \(J_\alpha/p^2\)，其中
\[
J_\alpha=
\begin{pmatrix}
\beta&pry-p^2\epsilon+\beta v_D\\
-\alpha&-\beta
\end{pmatrix}.
\tag{3.1}
\]
迹零等式是 \(p(x-y)+\alpha v_D=\beta\)。换到 (1.3) 后，同一矩阵为
\[
\boxed{
\mathcal J_\alpha=
\begin{pmatrix}
-rp/2&-\alpha\\
pn(r-2\epsilon)/4&rp/2
\end{pmatrix}.}
\tag{3.2}
\]
它的对角和左下项均不随 \(\alpha\) 改变，且
\[
\mathcal J_{\alpha+4}-\mathcal J_\alpha=-4E_{12}.
\tag{3.3}
\]
这是一个沿平方零方向变化的反射族。它来自改变来源和输出的匹配，而非固定来源的同行列式纤维。

置
\[
F_\alpha=\frac{pr^2-n(r-2\epsilon)\alpha}{4}.
\]
有
\[
\mathcal J_\alpha^2=pF_\alpha I,\qquad
pF_\alpha\equiv p^4\pmod n.
\tag{3.4}
\]
后一式用 \(r\equiv-2p\pmod n\) 即得。因 \(p\nmid n\)，平方标量非零，且在每个危险素数处为单位。故重复每个三步返回给出其正向射影逆。

在 \((z,y_*)=(z,a+pz)\) 基中，
\[
J_\alpha\equiv
\begin{pmatrix}p^2&-\alpha\\0&-p^2\end{pmatrix}\pmod n.
\tag{3.5}
\]
因此真实返回保持合法性 \(\gcd(y_*,n)=1\)。原子中途也不可能制造不可消除的障碍，否则最终合法性不可能恢复。

# C11.4 同一倍率环直接给完整上根

设
\[
c_\epsilon=\begin{cases}r,&\epsilon=0,\\1,&\epsilon=1,\end{cases}
\qquad f_i=F_{\alpha_i}/c_\epsilon,\quad i=0,1.
\tag{4.1}
\]
则 \(f_i\) 是非零整数，且
\[
\gcd(f_0,f_1)=1,\qquad
\gcd(f_0f_1,n)=1,\qquad
r\mid f_0,\qquad f_0-f_1\text{ 为奇数}.
\tag{4.2}
\]

**证明。** 若 \(\epsilon=0\)，
\[
f_0=\frac{r(3p+r)}4,\qquad f_1=f_0-n.
\]
由 \(r,p\) 与 \(n\) 互素，得到 \(\gcd(f_0,n)=1\)，故两数互素。

若 \(\epsilon=1\)，令 \(d=r-2\ne0\)，则
\[
f_0=\frac{r[pr+n(r-2)]}{4},\qquad f_1=f_0-nd.
\]
中括号被4整除，因为 \(p-r\equiv2\pmod4\)。又
\[
4f_0\equiv pr^2\pmod n,\qquad
4f_0\equiv pr^2\pmod d.
\]
这里 \(n,d\) 均奇，\(\gcd(r,d)=1\)，且 \(0<|d|<p\)，所以 \(f_0\) 与 \(nd\) 互素。奇偶性由两种情况下的差均为奇数得到。证毕。

令
\[
R=\mathbb Z[1/|f_0f_1|].
\tag{4.3}
\]
由 (4.2)，\(2,r\) 都是 \(R\) 单位；没有反演任何危险素数。

记 \(S=\operatorname{diag}(1,-1)\) 为两个等大块的角色交换。两条已有真逆的返回给出
\[
T=\mathcal J_{\alpha_1}\mathcal J_{\alpha_0}^{-1}
=\begin{pmatrix}
f_1/f_0&-2r/(c_\epsilon f_0)\\0&1
\end{pmatrix},
\]
\[
\boxed{STS^{-1}T^{-1}=U\!\left(\frac{4r}{c_\epsilon f_0}\right).}
\tag{4.4}
\]
上式根参数是 \(R\) 单位。互素性给
\[
\mathbb Z[f_1/f_0,f_0/f_1]=R.
\]
通过 \(T\) 的正反共轭及上根相加，得到全部 \(U(R)\)，包括全部负参数。这里每条形式逆都有先行标量周期，未借助尚未建立的深核。

# C11.5 一个两步返回给下根，深核没有循环依赖

保留 \(r\) 份旧 \(B\)，对其余位置平均两组
\[
\left(A^{(p+r)/2},B^{(p-r)/2}\right),\qquad
\left(A^{(p-r)/2},B^{(p-r)/2},C^r\right).
\tag{5.1}
\]
两个组均长 \(p\)，与保留载体不交。它们给实际矩阵 \(\mathcal K/p\)，其中
\[
\mathcal K=
\begin{pmatrix}-r/2&1\\rn/4&r/2\end{pmatrix},
\qquad
\mathcal K^2=\frac{r(p+r)}2 I.
\tag{5.2}
\]
标量非零且与 \(n\) 互素，故 \(\mathcal K^{-1}\) 正向可执行。由于 \(r,2\in R^\times\)，已有 \(U(2/r)\)，并且
\[
H=\mathcal K U(2/r)
=\begin{pmatrix}-r/2&0\\rn/4&p+r\end{pmatrix},
\qquad
\boxed{SHS^{-1}H^{-1}=L(n).}
\tag{5.3}
\]
这一步没有假设 \(p+r\) 已在 \(R\) 中可逆：\(H^{-1}\) 来自 \(\mathcal K^{-1}\) 和上根逆。

要把整数下根扩为 \(L(nR)\)，必须再给一个真实深核，不能把环系数免费加入。设
\[
P=\begin{pmatrix}1&-2\\0&n\end{pmatrix}.
\]
直接计算得，对每个 \(t\in R\)，
\[
P^{-1}U(t)P=U(nt),
\]
\[
P^{-1}\mathcal K
U\!\left(\frac{8(p+r)}r t\right)
\mathcal K^{-1}P=L(nt).
\tag{5.4}
\]
中间上根参数属于 \(R\)，不需要反演 \(p+r\)。故在 \(P\) 基里两条完整 \(nR\) 根已经实际存在。调用既有深同余引理，得到实际群包含
\[
P\Gamma(n^2,R)P^{-1}\supseteq\Gamma(n^3,R).
\tag{5.5}
\]
最后的包含由 \(P\) 和 \(nP^{-1}\) 在 \(R\) 上整直接验证。换基只是分析，没有执行 \(P\)。

现在对任意 \(t\in R\)，因全部分母与 \(n\) 互素，可取整数 \(k\) 使
\[
t-k\in n^2R.
\]
于是
\[
L(nt)=L(nk)\,L(n(t-k)).
\]
第一项由 (5.3) 的整数幂实现；第二项属于已经实际取得的 \(\Gamma(n^3,R)\)。故完整 \(L(nR)\) 成立。再次应用通用深同余引理，取得 \(\Gamma(n^2,R)\)，证明 (1.2)。

依赖顺序是：两张反射表 → \(U(R)\) → \(\mathcal K\) 和 \(L(n)\) → 换基后的深核 → \(L(nR)\) → 共同深核。没有用深核反过来制造最初的反射或倍率。

# C11.6 接到共同终端，完整覆盖奇数下半区

换到
\[
(z,y_*)^T=C(u,v)^T,\qquad
C=\begin{pmatrix}1&0\\n/2&1\end{pmatrix}\in\operatorname{SL}_2(R).
\]
\(L(nR)\) 与 \(C\) 交换，\(\Gamma(n^2,R)\) 在该换基下保持。特别已有整数 \(L(n\mathbb Z)\) 和 \(\Gamma(n^2,\mathbb Z)\)。

选整数 \(k\) 满足
\[
4\mid k,\qquad k\equiv-p^{-2}\pmod n.
\]
已有上根给真实返回
\[
V=CU(k)C^{-1}
=\begin{pmatrix}
1-kn/2&k\\-kn^2/4&1+kn/2
\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z),
\]
\[
V\equiv U(-p^{-2})\pmod n.
\tag{6.1}
\]
它满足共同终端的方向条件。

共同终端还要求有限内容对应能够提供标量2。由 \(f_0,f_1\) 奇偶相反，至少一张 (3.1) 的整数矩阵有偶行列式；其条目共同 gcd 为奇数，因为左下项 \(-\alpha_i\) 为奇数。除掉条目 gcd 后，行列式仍为偶数且与 \(n\) 互素。已有 \(\Gamma(n^2,\mathbb Z)\) 因而允许调用有限内容分支定理，取得所需模 \(n^2\) 的标量2作用。

至此[有限对应共同终端 §3—5](finite_orbit_completion_without_ring_extension.md)的全部前提均已落实。其全区间小单位引理对p≥5直接适用；p=3时这里只有n=7，模7单位由−1和2生成，所需补充直接成立。正向互补数字返回供应其余有限尺度，两根列修正与整数主同余纤维完成归零。可固定选终端
\[
t=\left(1,p^2-\frac{n(p-1)}2\right).
\]
在原块值中，它有
\[
A=-\frac{r(p-1)}2,\quad B=\frac{r(p+1)}2,\quad C=-p.
\]
\((p+1)/2\) 份 \(A\) 加 \((p-1)/2\) 份 \(B\) 恰为零和 \(p\) 元组。

全过程使用原位置与共同尺度；终端有限对应不要求后来数字的有理全局逆。入口和零触发尾部的依赖沿用既有独立证明，故没有把“核心有根”冒充“全输入定理”。
