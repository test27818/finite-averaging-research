# 统一补齐 4p 上方的 d_p 尾部：N(p)<=3p+10

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../../README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

**同日后续：** [全部素数统一阈值](../upper_band/prime_arity_all_prime_three_p_plus_ten.md)以相同接口补齐较小p的上端，删除本页定理B的p>=37条件。现在N(p)<=3p+10对所有素数p>=5成立；本页尾部证明继续完整使用，不另增加d_p条件。

日期：2026-09-15。p 为平均元数，n 为原位置数。本文所有平均均在原 n 个位置执行。

## 1. 完整结论

**定理 A。** 对每个素数 p>=5、每个 n>=4p，非全等有理输入有限步 p 平均可达全等，当且仅当本原中心化差分 gcd 的素因子只有 p。

**定理 B。** 结合[重叠返回的上端完成](../upper_band/prime_arity_upper_band_overlap_completion.md)，对每个素数 p>=37，
\[
\boxed{N(p)\le3p+10.}
\]
这里 N(p) 要求全部后续维数均满足完整判据。它已经不是只有一段内部区间成立；4p 上方旧 d_p 条件漏掉的维数全部由本文补齐。

本文沿用既有 Morris 2007 定理6.1(2)、Serre 强同余子群性质及由此建立的深同余引理、正向取逆引理。外部依赖与[上半带完整证明](../upper_band/prime_arity_upper_band_unrestricted_completion.md)一致，Serre 原文全文的访问边界仍保留。程序不证明外部无限群定理。

**没有证明 N(p)<=3p。** 对 p>=37，若进一步完成 3p+1 至3p+9 的一般偏移族，就可达到这个目标。2p 附近的最优阈值仍是另一问题。

## 2. 为什么旧缺口反而提供足够资源

已有定理覆盖
\[
n\ge4p-2+d_p(n),\qquad N(p)\le4p+\lceil\log_2p\rceil.
\]
因此只须考虑
\[
n=4p+s,\quad1\le s<\lceil\log_2p\rceil<p.
\]
此时 p 不整除 n，令 d=omega(n)。旧不等式失效恰为
\[
\boxed{d\ge s+3.}
\tag{2.1}
\]
n=4p 本身满足旧条件，已经完成。

若 n 奇，s 奇且 d>=4；n 至少含 d 个不同奇素数。若 n 偶，s 为正偶数，故 d>=5。由最小素数乘积，得到两个统一估计：
\[
\boxed{p\ge16s+21,\qquad
\varphi(n)>8\cdot2^d+7s+36.}
\tag{2.2}
\]

证明如下。奇数情形的基点 d=4 给
\[
n\ge3\cdot5\cdot7\cdot11=1155,\quad\varphi(n)\ge480;
\]
偶数情形的基点 d=5 给
\[
n\ge2\cdot3\cdot5\cdot7\cdot11=2310,\quad\varphi(n)\ge480.
\]
增加一个不同素因子时，最小乘积至少乘13，最小 phi 至少乘12。因此归纳得到
\[
n\ge65d-111,\qquad\varphi(n)>8\cdot2^d+7d+15.
\]
基点分别比较1155与149、2310与214，以及480与171、480与306；后续乘积增长超过右侧的增长。重复素因子只会增大这两个下界。

将 s<=d-3 代入，便得 n>=65s+84，即 p=(n-s)/4>=16s+21，以及 (2.2) 的 phi 估计。

所以不能仅把旧缺口视为“任意大小的余量 s”。它强制 p 相对 s 很大，并提供很强的单位密度；这两项正用于下面的容量和尺度证明。

## 3. 短参数筛选仍然成立

记 rho=phi(n)/n。每个 ell|n 给定至多一个禁止余数类，CRT 将它们合成一个平移。长度 L 的整数区间中，避开这些类的个数大于
\[
L\rho-(2^d-1).
\]
取 L=p-1，由 (2.2)，
\[
(p-1)\rho
=\frac{n-s-4}{4}\rho
\ge\frac{\varphi(n)-s-4}{4}>2^d-1.
\tag{3.1}
\]
因此 [1,p-1] 内总有同时避开所有禁止类的参数。

这重新证明了尾部所需的短配比引理，而不是将旧 n<4p 的引理直接用于 n>4p。具体算法只须对各素数标记一个等差数列；没有平均词搜索。

## 4. 全输入进入大载体核心

我们保持同一个 m=2 核心，允许载体大于 p：
\[
\boxed{
K(a,z)=(a^{2p},(-2a+rz)^p,(-pz)^r),\quad
r=p+s,\quad n=3p+r.}
\tag{4.1}
\]
因为 gcd(p,r)=1，本原整数核心仍满足
\[
\gcd(a,z)=1,\qquad G=\gcd(a+pz,n).
\]
以下证明任意合法输入都能进入 (4.1)。

### 4.1 四个 p 块与 s 个单点

固定一个单点 w，保护它和每个 ell|n 处的一个不同余见证，在其余位置平均出两个 p 块。容量足够：d<p 由 2^d<=n<5p、p>=37 得到，而 n-(d+1)>=2p。

用既有块--单点交换和第3节配比筛选，至多3d步使第一块 a 与 w 在全部 ell|n 处不同余。避开 w，再平均出第三、第四个 p 块，得到
\[
(a^p,b^p,c^p,d_0^p,x_1,\ldots,x_s).
\]
沿用三个主块的见证修复：先混合 b,c，使 c-a 在原已好素数处非零，再交换 b 块与 w。原坏素数处 a=b=c、w!=a，因此这一次交换修复全部原坏素数。现在前三块在每个 ell|n 处不全相同。

这些论证只使用第3节的短配比，以及每个交换真实存在，不需要 s>=d。

### 4.2 第一次三行折叠

令 p=3m+epsilon，epsilon 属于 {1,-1}。先混合 b,c，使 b-a 在所有前三块非全同余的素数处非零；再混合 a,b。

第二次混合保持 S=a+b+c 不变，而
\[
mS+\epsilon a-pd_0
\]
对混合参数的斜率在所需素数处非零。因此第3节可使
\[
\frac{mS+\epsilon a}{p}-d_0
\]
在全部 ell|n 处非零。随后平均两个组成均为 (m+epsilon,m,m) 的 p 组，再平均余下 p 份，得到
\[
(A^{2p},B^p,d_0^p,x_1,\ldots,x_s),
\qquad A-d_0\text{ 在模 }n\text{ 下为单位}.
\]

### 4.3 增大载体，再折叠一次

平均 p-s 份 A 和全部 s 个单点，留下 p+s 份旧 A 作载体。其余是三个 p 块；其中原 d_0 块与载体有完整见证，故操作安全。

相对载体 A，三个 p 块的差之和在每个 ell|n 处为零，这是全局零和与 n=0 mod ell 的直接结果。因此它们任意两个差不可能同时为零。先混合两个块取得完整差见证，再用上一段的 (m+epsilon,m,m) 三行折叠，得到 (4.1)。

全过程至多20+3d次平均。载体在最后折叠中保持不动，其大小可以超过 p；没有调用一个 p+s 维平均求解器。

## 5. 两次制造新载体的五步对合

置 epsilon=1 或 -1，使 p=epsilon mod4，并令
\[
t_0=\frac{p-\epsilon}{4},\qquad
t_1=t_0+s.
\]
以下分别取 t=t_0,t_1，定义
\[
b=p-s-3t,\qquad
\beta=rt-pb=nt-p^2+ps.
\tag{5.1}
\]

先平均两个互不相交、组成相同的 p 组
\[
(A^{p-b-t},B^t,C^b).
\]
它们产生 2p 份
\[
D=\frac{s a+\beta z}{p}.
\tag{5.2}
\]
这里使用 p-b-3t=s。原 A、B、C 的剩余数量分别为 2(b+t)、p-2t、r-2b。

从新 D 中保留 r=p+s 份作最终载体。对整数 h，再平均两个组成相同的 p 组
\[
(A^x,B^h,C^u,D^t),\qquad
x=2h+t-b,\quad u=p-2t+b-3h.
\tag{5.3}
\]
最后平均其余 p 份。总计五次原子平均。

可取全部整数
\[
\boxed{
\max\left(0,\left\lceil\frac{5p-5s-16t}{6}\right\rceil\right)
\le h\le b.}
\tag{5.4}
\]
第2节的 p>=16s+21 保证此区间至少含两个相邻整数。

具体容量核对：两个初始重复组需要 2t<=p、2b<=r、p-b-t>=0。最后重复组要求
\[
0\le x\le b+t,\quad
0\le2h\le p-2t,\quad
0\le2u\le r-2b,\quad
2t\le p-s.
\]
将 t=t_0+delta、delta=0或s 代入，有 b-t=epsilon-s-4delta<=0，且 b<=(p-2t)/2，所以 (5.4) 保证以上全部条件。其未截断实端点差为
\[
\frac{p+\epsilon-2s-4\delta}{12}>2,
\]
而 b>=4，截断下界为0不会破坏两个相邻整数的存在。

所得返回为 p^-2 J_{t,h}，其中
\[
J_{t,h}=
\begin{pmatrix}\beta&Q\\-s&-\beta\end{pmatrix},
\quad
Q=prh-p^2u+t\beta.
\]
直接得到
\[
\boxed{
J_{t,h}^2=p f_{t,h}I,\qquad
f_{t,h}=p^3+n[4t^2+(s-2p)t-sh].}
\tag{5.5}
\]
f=p^3 mod n，所以非零且与 n 互素。每个五步返回的射影逆都可通过重复它正向实现。

在 (z,y)=(z,a+pz) 基下，整数矩阵为
\[
\begin{pmatrix}
p^2-nt&-s\\
n[ph-t(p-t)]&-p^2+nt
\end{pmatrix}.
\tag{5.6}
\]
故其实际模 n 作用为 (1,-s/p^2;0,-1)，保持合法域。

## 6. 四个五步返回统一产生深主同余控制

旧 A 对合仍适用于 r=p+s：
\[
A_j=\begin{pmatrix}0&-d_j\\-1&0\end{pmatrix},
\quad d_j=p^2-nj,
\quad
\left\lceil\frac{p-s}{6}\right\rceil\le j\le
\left\lfloor\frac{p-s}{4}\right\rfloor.
\]
因为 p-s>=36，区间至少有三个相邻整数 j,j+1,j+2。分别记其标量为 d_0,d_1,d_2。

固定 t，取 (5.4) 的两个相邻 h,h+1，记 f=f_{t,h}、g_t=f_{t,h+1}。有
\[
g_t=f-sn,\qquad \gcd(f,g_t)=1.
\tag{6.1}
\]
因为 gcd(f,n)=1，且
\[
f=p(p-4t)^2\pmod s;
\]
t=t_0 或 t_0+s 时 p-4t 分别为 epsilon、epsilon-4s，与 s 互素，而 gcd(p,s)=1。

相邻商为
\[
T_t=J_{t,h}^{-1}J_{t,h+1}
=\begin{pmatrix}1&\beta_t n/f\\0&g_t/f\end{pmatrix}.
\]
与 A_j^{-1}A_{j+1}=diag(1,d_1/d_0) 取交换子，得到
\[
U\left(\frac{\beta_t n^2}{d_1g_t}\right).
\tag{6.2}
\]
两个 t 提供的 beta 满足
\[
\beta_{t_1}-\beta_{t_0}=ns,\quad
\gcd(\beta_{t_0},s)=1,\quad
\boxed{\gcd(\beta_{t_0},\beta_{t_1})=\gcd(n,5)=:g.}
\tag{6.3}
\]
最后一步用 beta_t= p(s-p) mod n、gcd(p,n)=1。

令 R_0 局部化所有 d_0,d_1 及两对 f,g_t。相邻商的倍率和逆倍率生成这个环，所有反演素数均不除 n。由 (6.2)、整数 Bezout 和共轭，获得
\[
U(gn^2R_0),\qquad L(gn^2R_0).
\]
于是既有深同余引理给
\[
\boxed{\Gamma(M,R_0),\qquad M=g^2n^4.}
\tag{6.4}
\]
g 为1或5且整除 n，所以控制层没有任何 n 以外的辅助素数。

再取 eta 属于 {1,-1}、eta=p mod3，由安全返回取逆引理激活保载体 F_eta，局部化 p；由第三个 A 的相邻商局部化 d_2。这里 eta 与第5节按模4选择的 epsilon 分别定义。下面每次加入安全返回行列式，都通过真实上三角倍率扩张根参数环，再由深同余引理取得 Gamma(M,R)。不存在先假定任意返回可逆的循环。

## 7. 单位尺度用一次计数统一覆盖

一般保留 A 的真实返回仍是
\[
M_{q,j}=
\begin{pmatrix}p-q&nj-pq\\-1&0\end{pmatrix},\quad q=3j+k.
\]
现在须显式保留 j+k<=p，因为 r>p。完整容量为
\[
0\le j\le\lfloor p/2\rfloor,\quad
0\le k\le\lfloor r/2\rfloor,\quad
\lceil r/2\rceil\le j+k\le p.
\]

下列整个整数区间都可实现：
\[
I=[L,2p-1],\qquad
L=\begin{cases}
r/2+2,&r\text{ 偶},\\
(r+9)/2,&r\text{ 奇}.
\end{cases}
\tag{7.1}
\]
证明：固定 j 时，可实现的 q 区间为
\[
[2j+\lceil r/2\rceil,\ \min(3j+\lfloor r/2\rfloor,2j+p)].
\]
r 偶从 j=1 开始，r 奇从 j=2 开始，连续区间相邻或交叠，最终上界为2p-1。

每个 gcd(q,n)=1 的返回行列式 D=nj-pq 都与 M 互素，故正向逆已可执行。其与旧 A 的商将 D 局部化，而 -D/p 是 q mod n 的实际 R 单位提升。只须加入有限多个 q 属于 I。

记 C 为 I 中模 n 单位的个数。由容斥，
\[
C>|I|\rho-(2^d-1),\quad
|I|\ge\frac{3n-7s-36}{8}.
\]
利用 (2.2)，得到
\[
\boxed{C>\frac{\varphi(n)}4.}
\tag{7.2}
\]
又 I 完全位于 (0,n/2)，所以 I 中单位及其负数组成集合 S，大小大于 phi(n)/2。对任意模 n 单位 u，S 与 uS 必相交，因而 u 是 S 中两个元素之比。所有这些元素均已有 R 单位提升，故
\[
\boxed{R^\times\longrightarrow(\mathbb Z/n\mathbb Z)^\times
\text{ 满射}.}
\tag{7.3}
\]

这避免了寻找模 n 原根，也不需要逐类反演 r 或构造二三单位的小代表。尾部本身的多素因子条件使容斥误差小于主项所留余量。

## 8. 所有局部方向，包括模5

取某个 J_{t,h} 与 A_j 的积 V=J_{t,h}A_j/p^3。在 (z,y) 基下，
\[
V=\begin{pmatrix}1&-5/p\\0&1\end{pmatrix}\pmod n.
\tag{8.1}
\]
这在全部 ell|n、ell!=5 处是非平凡上平移。

其迹为
\[
\operatorname{tr}V=
2-\frac n{p^3}[pt+t^2+ph+sj].
\tag{8.2}
\]
n=0 mod4 时迹自动为2 mod4；n=2 mod4 时 s 偶，pt+t^2 与 sj 均偶，选相邻 h 中的偶数即可。因此二进完整循环成立。

若 3|n，将 V 除以迹半数后写为 I+N、N^2=cI。9|n 时 c=0 mod9；v_3(n)=1 时
\[
\frac c3=
\frac{n/3}{p^3}
\bigl[(p-s)(j+t-h)-5t^2\bigr]\pmod3.
\tag{8.3}
\]
因为 p-s=2p mod3 为单位，从相邻 j,j+1 中选一个便可避开 c=6 mod9。这不改变二进条件。所有 ell>=7 直接适用已证局部射影循环引理。

若 5|n，先选一个 q 属于 I，使
\[
q=-p\pmod5,\qquad\gcd(q,n)=1.
\tag{8.4}
\]
这样的 q 确实存在：固定非零模5类后，容斥主项为 |I|rho/4，误差小于2^{d-1}；(2.2) 还给 |I|rho>2^{d+1}，所以剩余数严格为正。

该安全 A 返回在模5下为 (1,-1/p;0,1)，在每个5幂上具有完整射影循环。先用其非负次幂使 z/y=0 mod 5^{v_5(M)}。V 模5为 I，其在模5幂下的完整矩阵阶为5幂。随后令 V 的指数被该阶整除，再用 CRT 同时满足所有其他素数处的完整循环指数。

于是任意合法 R 本原列均能到达
\[
z=0\pmod M,\qquad y\in(R/MR)^\times.
\tag{8.5}
\]
这一步保留完整5进矩阵阶，不以局部形式逆代替真实路径。

## 9. 从同余目标到精确零终端

两个已知实际 R 单位
\[
\kappa_1=d_1/d_0=1-n/d_0,\qquad
\kappa_2=d_2/d_0=1-2n/d_0
\]
通过 LTE 和 CRT 生成模 M 到模 n 的全部主单位核。n=2 mod4 时，用 kappa_2 生成等于1模2n的部分，再以 kappa_1=3 mod4 补另一个类；其余情形 kappa_1 即可。

结合 (7.3)，R 单位模 M 满射。全部所用规范返回的行列式在最终 R 中已可逆，所以它们保持 R 本原性。选 epsilon 属于 R^times 匹配 (8.5) 的 y，由已证主同余纤维引理，将状态**精确**送到 (z,y)=(0,epsilon)。

最终核心为
\[
(\epsilon^{2p},(-2\epsilon)^p,0^{p+s}).
\]
选取全部3p个非零位置和p个零，调用旧不等式已经独立证明的4p维判据；剩余s个零不动。这个子块自身零和且含零，G=1，因此调用合法。这也说明收尾没有循环使用本文的上方区间定理。结论承接第4节任意原输入入口，因此不是仅有核心群或有限模像。

必要性沿用 G 不变量。旧定理覆盖的 n 与本文补齐的 n 合并，即得定理 A；再接 3p+10 至4p-1 的已有完整区间，得定理 B。

## 10. 范围与核验

此前反复列出的两个类型现在均已包含：

- p=761，n=3045=3*5*7*29，s=1、d=4；
- p=577，n=2310=2*3*5*7*11，s=2、d=5。

为了检查更高偏移及5进层，还核对了
\[
p=10103843,\quad n=40415375=5^3\cdot7\cdot11\cdot13\cdot17\cdot19,
\quad s=3,\quad d=6.
\]
大例只作固定2x2矩阵及逐位模运算，没有生成四千多万个位置的状态或枚举模群。

[核验程序](../../../../work/verify_four_p_tail_completion.py)使用最小素因子筛列出 p<=20000 的365个旧条件遗漏参数，再加入上述高偏移例。核验内容为：

- 366组多素因子容量、单位密度、五步对合与根 gcd；
- 39组不依赖有限遗漏清单的额外容量系统；
- 32条五步返回及其重复闭路的逐位置 Fraction 重放；
- 732组方向和单位尺度联合输送；
- 3条一般整数零和输入到大载体核心的原位置路径，样本最长22步。

所有一般量词由正文的乘积估计、计数、容量、群控制和精确终端证明承担。有限核验不证明外部 Morris/Serre 定理，也不宣称生成了完整平均词或给出最短路径算法。

核验入口：python work/run_verifications.py --id four-p-tail-completion。
