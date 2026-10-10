本节设 $p\ge13$ 为奇素数、$n=3p+r$、$10\le r\le p-3$，并使用加权上半带四返回的容量及根。

# C26.2 共同核心与已有资源

置 r=n-3p，故 10<=r<=p-3。已有原位置入口将任意合法输入送到
\[
K(a,z)=(a^{2p},(-2a+rz)^p,(-pz)^r),\qquad
\gcd(a,z)=\gcd(a+pz,n)=1.
\]
令 y=a+pz，使用整幺模坐标 (z,y)。合法性恰为 y 在模 n 下可逆。

四返回文档给出相邻参数 j_0,j_0+1 和 k_0,k_0+1，以及
\[
A=\begin{pmatrix}0&-d\\-1&0\end{pmatrix},\quad
B=\begin{pmatrix}r&b\\2&-r\end{pmatrix},
\]
\[
d=p^2-nj_0,\quad e=d-n,\quad
b=nk_0-p^2+rp,\quad \mu=r^2+2b,\quad\nu=\mu+2n.
\]
相邻 A、B 分别记为 A',B'。每个矩阵实际乘以 1/p，恰由三个原位置平均实现；平方分别为 dI,eI,mu I,nu I，故射影逆也正向可执行。

令 R_* = Z[1/|de mu nu|]。已有
\[
U(rn^2R_*),\quad L(rn^2R_*),\quad
\Gamma(r^2n^4,R_*).
\tag{2.1}
\]
反演素数均不除 n；n 奇时 2 已在 R_* 中可逆。还可执行
\[
D_0=A^{-1}A'=\operatorname{diag}(1,e/d),\quad
T=B^{-1}B'=
\begin{pmatrix}1&rn/\mu\\0&\nu/\mu\end{pmatrix}.
\]
两者的共轭倍率及逆倍率生成整个 R_*。在本文每次扩张 R 后，同一组倍率继续使根参数构成相应的 R 模。

以下“可执行矩阵”均指：一个有限原位置平均词在整个核心上实现该矩阵的某个非零共同标量倍。共同标量不改变归零目标；不得用于单独缩放外部位置。

# C26.3 两个取逆引理

**有限逆提升。** 若 Gamma(Q,R) 已可执行，Z 属于 SL2(R) 且 Z 正向可执行，则 Z 的射影逆也正向可执行。

因为 R/QR 有限，存在 k>=1 使 Z^k 属于 Gamma(Q,R)，而
\[
Z^{-1}=Z^{k-1}(Z^k)^{-1}.
\tag{3.1}
\]
这里最后一因子是已知主同余群中的真正逆，故不只是模 Q 的逆。

**安全整数返回取逆。** 若 Gamma(Q,R) 已可执行，整数非奇异返回 M 真实存在，且 gcd(det M,Q)=1，则 M 的射影逆也可执行。

证明使用[旧证明第5节](prime_arity_upper_band_coprime_six_complete.md)的 Smith--CRT 夹乘，那里 n 可逐字替换为 Q：取正偶次 P=M^k=I mod Q，令 Delta=det P。以整数行列式一的行列变换对角化 P，构造 g_* 使 Pg_*P 被 Delta 整除，再用 CRT 取 g=g_* mod Delta、g=I mod Q。于是
\[
h=\Delta^{-1}PgP\in\Gamma(Q,\mathbb Z),\qquad
gPh^{-1}=\Delta P^{-1}.
\]
g、h 的逆由主同余控制提供。证毕。

对本文常用的伴随形矩阵，还有无需展开巨大 M^k 的恒等式。若
\[
M=\begin{pmatrix}\alpha&D\\-1&0\end{pmatrix},
\quad \gcd(D,Q)=1,
\]
取整数 t 满足 t=alpha mod D、t=0 mod Q，则
\[
H=D^{-1}MU(t)M\in SL_2(\mathbb Z),\qquad
U(t)MH^{-1}=DM^{-1}.
\tag{3.2}
\]
H 本身正向可执行，故 (3.1) 提供 H^{-1}。当 |D|=1 时模 D 条件为空。

所有应用均先指出真实返回，再激活其逆；两个引理不将任意形式矩阵变为平均操作。

# C26.4 消除来自 r 的额外素因子

目标是在某个有限局部化环 R 中获得
\[
U(3^a n^2R),\quad L(3^a n^2R),\quad
\Gamma(M,R),\qquad
a=v_3(r),\quad M=3^{2a}n^4.
\tag{4.1}
\]
R 的反演素数全部不除 n；因此 M 的素数支持恰为 n 的素数支持。

### 4.1 先激活 p 和小素因子

保留 r 份原载体 C，将三个 p 组分别平均，给出
\[
F_t=\begin{pmatrix}t/p&r(p-t)/(3p)\\0&1\end{pmatrix},
\quad t=p-3j,\quad0\le j\le(p-1)/2.
\tag{4.2}
\]
两个重复组各取 p-j 份 A、j 份 B。它们的互补组恰有 p 份，故容量成立。

取 epsilon=1 或 -1，使 p=epsilon mod3。F_epsilon 的整数代表行列式为 epsilon p，与 r^2n^4 互素；由第3节取得逆。其上三角倍率为 epsilon/p，通过根的正逆共轭，先将 p 加入 R 的反演集合。

对 q=1 mod3，只要 epsilon q 是 (4.2) 的允许数字，便有
\[
C_q=F_{\epsilon q}F_\epsilon^{-1}
=\begin{pmatrix}q&r(1-q)/3\\0&1\end{pmatrix}.
\tag{4.3}
\]
设素数 ell|r、ell!=3、ell<=(p-1)/2，选 q=ell 或 -ell 使 q=1 mod3。若 ell<=(p-3)/2，数字容量立即成立。若 ell=(p-1)/2，则 p=2ell+1>7 为素数迫使 ell=p=2 mod3，取 q=-ell、epsilon=-1，所需数字为正 ell，容量仍成立。

(4.3) 的右上项被 q 整除，故
\[
H=q^{-1}C_qAC_q
\]
为整数矩阵，det H=det A=-d。于是 HA^{-1} 属于 SL2(R)，且正向可执行。由 (3.1) 得 H^{-1}，从
\[
AC_qH^{-1}=qC_q^{-1}
\tag{4.4}
\]
得到 C_q 的真正射影逆。共轭上根将 ell 局部化，再以 A 交换上下根。

这里允许 ell 整除旧主同余层：式 (C26.4.4) 正是绕过“行列式与旧层互素”限制的必要步骤。

### 4.2 唯一可能的大素因子

若 r 有一个大于 p/2 的素因子，则 r 本身就是该素数。此时 r 奇、n 偶，且 3 不整除 n。

若 p=r mod3，保留 B 的迹零返回 k_*=(p-r)/3、s=0 可执行，其平方标量
\[
\mu_*=\frac{r(2p+r)}3
\]
被 r 整除且与 n 互素。它与原 B 的商提供上三角倍率，直接将 r 局部化。

余下假设 p!=r mod3。选择一个奇数 q 满足
\[
r<q<p,\qquad2q\le3r,\qquad\gcd(q,n)=1.
\tag{4.5}
\]
以下闭式选择证明其存在，不需逐素数搜索。

- 若 5r>=3p，取严格小于 n/4 的最大奇数。此时 n-4q 属于 {2,4,6,8}。因 q 奇且 3 不整除 n，q 与 n 互素。p-r>=4 保证 q>r，其余容量由 3p<=5r 得到。
- 若 p/2<r<3p/5，取离 n/5 最近的奇数。距离至多1；n-5q 为 ±1、±3 或 ±5。只有 5|n 时须在 n/5±1 中选不被5整除的一项。n/5 是偶数，至少一项可用。由 r>p/2、r<3p/5 和 r>=(p+1)/2，可直接得 r<q<p 及 q<=3r/2。

置 s=q-r，为正偶数，且 2s<=r。保留 B、两个重复行各取 p-s 份 A 和 s 份 C，给
\[
N_s=\begin{pmatrix}p-s&-ps\\2&-r\end{pmatrix}.
\]
其行列式 Delta=s(2p+r)-pr 模 n 为 -pq，模 r 为 2ps，故与 rn 互素。第3节已可给出 N_s^{-1}。

令 H=N_sB^{-1}=(rho,beta;0,1)。其右上项满足
\[
\beta=(p-s)/2\pmod r,
\]
非零：s=q-r<p-r，故 r<p-s<p<2r。于是
\[
[D_0,H]=U(x),\qquad x=\beta n/e,
\tag{4.6}
\]
且 x 是模 r 单位。选整数 t 使 tx=1 mod r，则 n^2(1-tx) 属于 rn^2R。根参数相加给出 U(n^2)。再将任意 R 元素取整数模 r 代表，可得 U(n^2R)，A 共轭给下根。由深同余引理得到 Gamma(n^4,R)。

最后 N_0=(p,0;2,-r) 行列式 -pr 已与新层互素，故 N_0^{-1} 可执行。N_0B^{-1} 的倍率将 r 局部化。若中途为扩大根参数环加入 det N_s，仍只反演不除 rn 的素数。

上述操作消掉 r 的全部非3素因子。若 3|r，则它的所有非3素因子均小于 p/2，已属于第4.1节。因此 (4.1) 在全部参数下成立。

# C26.5 可执行数字与模 n 的全部单位

保留 A 的一般返回为
\[
M_A(j,s)=
\begin{pmatrix}p-3j-s&rj-ps\\-1&0\end{pmatrix}.
\tag{5.1}
\]
两个重复 p 组各取 p-j-s 份 A、j 份 B、s 份 C，留下 r 份旧 A，再平均其余 p 份。其容量恰为
\[
0\le j\le\lfloor p/2\rfloor,\quad
0\le s\le\lfloor r/2\rfloor,\quad
j+s\ge\lceil r/2\rceil.
\tag{5.2}
\]
置 q=3j+s、alpha=p-q、D=rj-ps=nj-pq。若 gcd(q,n)=1，则 D 与 M 互素，(3.2) 激活正向逆。且
\[
M_AA^{-1}=\begin{pmatrix}-D/d&-\alpha\\0&1\end{pmatrix}.
\]
通过共轭将 D 局部化。由于 D=-pq mod n、p 已可逆，R 单位的模 n 像便包含 q。

可以一次将全部满足 (5.2)、gcd(q,n)=1 的有限多返回的 D 加入 R。每次扩大 R 后，根和 (4.1) 继续成立。所有反演素数仍不除 n。

**容量区间。** 令 h=floor(r/2)、J=floor(p/2)，则每个整数
\[
L\le q\le U,\qquad
U=3J+h,\quad
L=\begin{cases}h+2,&r\text{ 偶},\\h+5,&r\text{ 奇},\end{cases}
\tag{5.3}
\]
均可实现。可取
\[
\max(0,\lceil(q-h)/3\rceil)\le j\le
\min(J,\lfloor q/3\rfloor,\lfloor(q-\lceil r/2\rceil)/2\rfloor),
\quad s=q-3j.
\tag{5.4}
\]
证明也可看每个固定 j 的数字区间：
\[
[3j+\max(0,\lceil r/2\rceil-j),\,3j+h].
\]
偶 r 从 j=1 开始，奇 r 从 j=2 开始；r>=10 保证这些整数区间相邻或交叠，起点和终点正是 (5.3)。

**单位覆盖命题。** 最终有限局部化环 R 满足
\[
R^\times\longrightarrow(\mathbb Z/n\mathbb Z)^\times
\quad\text{满射}.
\tag{5.5}
\]

若 3 不整除 n，第4节已使 r 成为实际 R 单位，因此 -r/p 是模 n 的单位3的一个 R 单位提升。对任意模 n 单位 u，先取正平衡绝对代表 b<=n/2。若 b>n/4，以 |n-3b| 代替 b。这是非零正整数严格下降，且只改变符号和3的乘法幂。重复至 b<=n/4。若 b<L，逐次乘3至首次达到 L，所得 q<=3L-3<=U。原 b 若已>=L，则 b<=n/4<=U。最后 q 是 (5.3) 的安全数字，所以 q 属于 R 单位像；倒推得到 u 也属于该像。r 奇时 r<=p-4、p>=17；这正保证上述 3L-3<=U，偶 r 情形更直接。

若 3|n，置 k=n/3。k±1 都在 (5.3) 中。模 n 到模 k 的单位群核由以下安全数字提供：

- 3|k 时，1+k 生成阶3的核；
- k=1 mod3 时，1+k 是阶2核的非平凡元；
- k=2 mod3 时，1-k 是阶2核的非平凡元。

这里取负是 R 单位 -1，不要求负数数字本身满足 (5.3)。

对任意单位 u，取它模 k 的正平衡绝对代表 1<=b<=k/2。考虑 k-b、k+b、b；三者模 k 都等于 ±u。若 k-b 不被3整除，取 q=k-b；否则 k 不被3整除，而 k+b 和 b 均不被3整除，取落在 [L,U] 的一个。

容量说明如下。总有 k/2>=L；k-b 从而位于 [L,U]。若 k+b>U，则
\[
b>U-k\ge k/2-2.
\]
除 (p,r)=(19,15) 外，所有 3|r 的允许参数均有 k/2-2>=L：偶 r 由 3p-2r>=24，奇 r 由 3p-2r>=39；p>=31 立即成立，较小 p 的允许 3|r 项直接满足这两不等式，唯一例外正是 (19,15)。在这个例外中 k=24 被3整除，所以第一选择 k-b 始终可用，不会进入溢出分支。于是总有一个安全 q 可用。q/u 在模 k 下等于 ±1，前述核元素和 -1 将其提升；因 q 已由 (5.1) 激活，得到 u 的 R 单位提升。证毕。

# C26.6 一条局部射影循环引理

**引理。** 设 ell 为素数，T 属于 GL2(Z_ell)，其模 ell 作用为
\[
T\sim\begin{pmatrix}1&b\\0&1\end{pmatrix},\qquad b\ne0.
\]
作用在仿射坐标 x=z/y、y 为单位的图上。

1. ell>=5 时，T 在每个 Z/ell^eZ 上都是单个长度 ell^e 的循环。
2. ell=3 时，令 T 的迹半数归一化后为 I+N、N^2=cI；若 c=0 mod3 且 c!=6 mod9，同样成立。
3. ell=2 时，若 tr T=2 mod4，也同样成立。

证明：奇 ell 可将 T 除以迹半数，得到 I+N。模 ell 的 N 非零幂零，故 c=0 mod ell。写
\[
(I+N)^\ell=A_\ell I+B_\ell N,\qquad
B_\ell=\sum_{j\ge0}\binom{\ell}{2j+1}c^j.
\]
ell>=5 时 v_ell(B_ell)=1、A_ell 为单位；ell=3 时 B_3=3+c，条件恰保证同样的赋值。此后重复 ell 次幂，非标量系数的赋值每次恰增加1。因为 N 在模 ell 下为非零上根，T^{ell^h} 在 x 上的首个非零位移总具有精确赋值 h。因此一个循环每提升一级都分裂为长度增加 ell 倍的单循环。

ell=2 时 Cayley--Hamilton 给 T^2=(tr T)T-(det T)I。非标量系数恰有赋值1，而 T 模2的上平移系数为单位。并且
\[
\operatorname{tr}(T^2)=(\operatorname{tr}T)^2-2\det T=2\pmod4.
\]
继续平方得到逐层精确位移，证明同上。标量归一化不改变射影作用。

引理不仅说某个方向能动，而且提供逐位计算到指定方向的指数；无需枚举 ell^e 个方向。

# C26.7 同时消除全部素数处的方向

在 (z,y) 坐标中取 V=BA/p^2，直接有
\[
V=\begin{pmatrix}1&-3/p\\0&1\end{pmatrix}\pmod n.
\tag{7.1}
\]
因此每个 ell>=5、ell|n 处均可用第6节。

若 n 偶，整数 BA 的迹为
\[
\operatorname{tr}(BA)=n(2j_0-k_0)-p(p+r).
\tag{7.2}
\]
n=0 mod4 时此迹自动为2 mod4；n=2 mod4 时把 k_0 换成 k_0+1 恰改变迹 n，所以相邻两个 B 中总有一个使迹为2 mod4。除以 p^2 不改变模4的迹，故这个 V 也在全部二进层形成完整循环。

若 3|n，(7.1) 在模3下是单位矩阵，须先用另一条真实 A 返回处理3方向。置 k=n/3，从 delta 属于 {-1,1,3} 中选
\[
q=k+\delta=-p\pmod3.
\]
具体地，-p-k 模3分别为1、2、0时取 delta=1、-1、3。总有 gcd(q,n)=1。可行 j 区间 (5.4) 含两个相邻整数。为说明这不是经验容量：q 位于 [p+r/3-1,p+r/3+3]，将 (5.4) 的三个实上界减去 (q-h)/3，每个差均至少2；p>=19 的条件直接给出，唯一更小的允许 3|r 参数 (17,12) 也成立。

若 v_3(n)=1，选其中一个 j 使 kj!=1 mod3；若 v_3(n)>=2，任取。实际 (z,y) 矩阵为
\[
W=\frac1p\begin{pmatrix}p&-1\\nj&-q\end{pmatrix}.
\]
它模3是非平凡上平移，且迹半数归一化后的参数为
\[
c=\frac{(p+q)^2-4nj}{(p-q)^2}.
\tag{7.3}
\]
若 9|n，则 c=0 mod9。若 v_3(n)=1，则 c/3=-kj mod3，所选 j 保证 c!=6 mod9。因此第6节提供每个三进层的完整方向循环。

现在给定任意合法 R 本原列 (z,y)。先用 W 的某个非负次幂使 z/y=0 mod 3^{v_3(M)}。V 在模3下为 I，其模任意3幂的**完整矩阵阶**是3的幂；令后续 V 的指数被该阶整除，就保留刚调好的3数据。其他 ell|n 的方向循环长度分别是 ell^{v_ell(M)}，彼此及上述3幂互素。指数 CRT 同时完成所有方向。因此得到
\[
z=0\pmod M,\qquad y\in(R/MR)^\times.
\tag{7.4}
\]
若 3 不整除 n，省去 W 即可。

这里明确使用 V 的完整3进矩阵阶来保护已完成数据；不能拿局部射影逆在不同素数处随意拼接。

# C26.8 单位尺度从 n 提升到 M

第5节已给模 n 的全部单位像。还需证明这个像覆盖模 M 的主单位核，不能只证明射影方向。

已有实际 R 单位
\[
\kappa_A=e/d=1-n/d,\qquad
\kappa_B=\nu/\mu=1+2n/\mu.
\tag{8.1}
\]
对任意奇素数 ell|n，
\[
v_\ell(\kappa_A-1)=v_\ell(n).
\]
LTE 表明 kappa_A 在模 ell^{v_ell(M)} 下生成所有等于1模 ell^{v_ell(n)} 的单位。不同素数处这些循环的阶为互素素数幂，故一条 kappa_A 的幂已通过 CRT 覆盖其乘积。

若 4|n，二进 LTE 同样适用于 kappa_A。若 n=2 mod4，则 kappa_A=3 mod4，而
\[
v_2(\kappa_B-1)=2.
\]
kappa_B 在奇素数处仍恰从 v_ell(n) 层开始，所以其幂覆盖“等于1模 2n”的全部主单位；再用 kappa_A 补另一个模4类。故无论 n 的局部类型如何，
\[
\boxed{R^\times\longrightarrow(R/MR)^\times
\text{ 满射}.}
\tag{8.2}
\]

注意本文并未要求实际反演2或3；它们若整除 n，就始终不在反演集合。利用的是不除 n 的真实单位在有限商中的像。

# C26.9 从有限同余精确到终端

全部使用的规范返回均属于 GL2(R)：p、四对合标量、所用安全返回的行列式已经逐步局部化。因此它们保持 **R 本原性**。即使整数代表后来出现共同因子，该因子只能是 R 单位；不能忽略这一点而直接对模方向作结论。

由 (7.4)、(8.2)，选 epsilon 属于 R^times，使 epsilon=y mod M。R 为 Z 的有限局部化，故是 PID；(z,y) 与 (0,epsilon) 都是 R 本原列且模 M 相同。以下显式主同余输送补上精确性。

取 alpha,beta 属于 R，使 alpha z+beta y=1。通过
\[
(\alpha,\beta)\mapsto(\alpha+ty,\beta-tz)
\]
选取 t，使 alpha=0 mod M；因为 y 模 M 为单位，总能做到。此时 beta=epsilon^{-1} mod M。于是
\[
P=\begin{pmatrix}
y/\epsilon&-z/\epsilon\\
\epsilon\alpha&\epsilon\beta
\end{pmatrix}
\in\Gamma(M,R),
\quad
P\binom zy=\binom0\epsilon.
\tag{9.1}
\]
(4.1) 保证 P 有真实正向实现。因此有限同余终端提升为精确核心
\[
(\epsilon^{2p},(-2\epsilon)^p,0^r).
\]
实际平均词可能带另一个非零共同尺度，它仍保持同一个零和 p 组。

令 j=floor(p/3)，取 2j 份 epsilon、j 份 -2epsilon 和 p-3j 份零；数目恰为 p，和为零，且 p-3j 属于 {1,2}<=r。执行一次平均产生 p 个零。调用[统一零触发收尾](../../tools/prime_arity_interpolation_and_lattice_structure.md)完成全系统。必要性仍由既有 G 不变量给出，定理得证。
