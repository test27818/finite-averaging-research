# 上半带与 6 互素维数的完整证明

**2026-09-15后续：** [无条件上半带完整证明](prime_arity_upper_band_unrestricted_completion.md)已删除本页gcd(n,6)=1限制，证明整个3p+10<=n<=4p-3。本文的安全整数返回取逆引理继续作为依赖；本文以下范围说明保留原阶段。

日期：2026-09-14。本文接续[四返回深同余控制](prime_arity_upper_band_four_return_congruence.md)。p 是每次平均的元数，n 是原位置数。所有路径均在原 n 个位置上执行。

## 1. 完整定理

**定理。** 对每个素数 p>=13，若
\[
\boxed{3p+10\le n\le4p-3,\qquad\gcd(n,6)=1,}
\tag{1}
\]
则非全等有理 n 元输入可以经过有限次 p 平均变成全等，当且仅当中心化、清分母和本原化后的差分 gcd 满足 G=1。

等价地，写 n=3p+r，条件为
\[
10\le r\le p-3,\qquad\gcd(r,6)=2.
\]
这里 n 可以是素数、素数幂或具有任意多个素因子的合数；没有额外入口密度或素因子个数条件。

例如覆盖 (p,n)=(13,49)、(17,61)、(17,65)、(19,67)、(19,71)、(19,73)、(23,85)、(31,115)、(31,119)、(31,121)。这些例子只说明范围，定理不是逐例核验外推。

本证明引用 Morris 2007 定理6.1(2)及 Serre 对有理数域 S 整数 SL2 的强同余子群性质。其用法与[偶数深同余引理](prime_arity_even_middle_congruence_and_eighteen.md)一致。外部定理不由程序证明；Serre 原文全文仍未取得，作为明确列出的已发表外部依赖引用。

## 2. 已有真实入口和四返回

由[上半带归约](prime_arity_upper_band_three_value_reduction.md)，每个合法原输入可有限步进入
\[
\mathcal K(a,z)=\bigl(a^{2p},(-2a+rz)^p,(-pz)^r\bigr),
\quad\gcd(a,z)=\gcd(a+pz,n)=1.
\tag{2}
\]
入口适用于整个 3p<n<4p，不限制 n 的不同素因子数。

沿用四返回文档的参数区间
\[
I_A=\left[\left\lceil\frac{2p-r}{6}\right\rceil,
\min\left(\left\lfloor\frac{2p-r}{4}\right\rfloor,
\left\lfloor\frac p3\right\rfloor\right)\right]\cap\mathbb Z,
\]
\[
I_B=\left[\max\left(0,\left\lceil\frac{2p-3r}{6}\right\rceil\right),
\left\lfloor\frac{p-r}{3}\right\rfloor\right]\cap\mathbb Z.
\]
条件 (1) 保证各区间至少含两个相邻整数。取 j,j+1 属于 I_A，k,k+1 属于 I_B，记
\[
d=p^2-nj,\quad e=d-n,
\quad b=nk-p^2+rp,
\quad\mu=r^2+2b,\quad\nu=\mu+2n.
\]
整数矩阵
\[
A_j=\begin{pmatrix}0&-d\\-1&0\end{pmatrix},\quad
A_{j+1}=\begin{pmatrix}0&-e\\-1&0\end{pmatrix},
\quad B_k=\begin{pmatrix}r&b\\2&-r\end{pmatrix},\quad
B_{k+1}=\begin{pmatrix}r&b+n\\2&-r\end{pmatrix}
\tag{3}
\]
分别乘 1/p 是三个真实原子平均组成的返回。它们的平方依次为 dI、eI、mu I、nu I，故射影逆也正向可执行。

四返回已经证明：在
\[
R_* =\mathbb Z[1/|de\mu\nu|]
\]
上，可以正向执行 U(rn²R_*) 和 L(rn²R_*)。因为 r 偶、n 奇，互素的 d、e 奇偶相反，故 2 是 R_* 单位。

## 3. 一个额外对合统一反演 r

写 r=2t。条件 gcd(r,6)=2 保证 t 不被3整除。

若 t=p 模3，取 A 载体返回的 s=t、j_*=(p-t)/3。两份相同组各含 2j_* 份 A、j_* 份 B、t 份 C。因为 t<p/2，有
\[
2t=r,\quad 2j_*\le p,\quad4j_*\le2p-2t.
\]
所以该返回有原位置容量，其平方标量为
\[
d_* = p^2-nj_* = \frac{t(p+2t)}3.
\tag{4}
\]
t 整除 d_*。

若 t!=p 模3，则 p=-t=2t=r 模3。取 B 载体返回的 s=0、k_*=(p-r)/3，其平方标量为
\[
\mu_* =\frac{r(2p+r)}3=\frac{4t(p+t)}3.
\tag{5}
\]
k_*>=0，重复行对 B 的使用量满足 2k_*<=p-r，对 A 的使用量满足 2(2k_*+r)<=2p。故该返回同样真实，且 t 整除 mu_*。

将相应标量 f=d_* 或 mu_* 的素因子加入反演集合，令
\[
R_0=\mathbb Z[1/|de\mu\nu f|].
\]
新增 A 返回与 A_j 的商是对角矩阵；新增 B 返回与 B_k 的商是上三角矩阵。它们及逆均已有正向实现。其对 U(x) 的共轭把参数乘以相应标量比及倒数，因此既有根参数环扩张到 R_0。由于 2、t 都是 R_0 单位，r 也是单位，于是得到
\[
\boxed{U(n^2R_0),\quad L(n^2R_0).}
\tag{6}
\]
全部反演素数都不除 n，因为每个对合标量模 n 均为 p²。这里先取得 r 的反演，再使用 (6)，不存在循环前提。

## 4. 从深层加强到整个 Gamma(n)

由 (6) 和此前深同余引理，Gamma(n⁴,R_0) 可执行。下面补齐 n 到 n⁴ 的层，不以有限模样本代替证明。

令
\[
D=A_j^{-1}A_{j+1}=\operatorname{diag}(1,\lambda),\quad\lambda=e/d,
\]
\[
T=B_k^{-1}B_{k+1}=\begin{pmatrix}1&rn/\mu\\0&\delta\end{pmatrix},
\quad\delta=\nu/\mu.
\]
三个行列式一的规范代表为
\[
H_1=\lambda^{-1}D^2,\quad
H_2=\delta^{-1}T^2,\quad
H_3=A_jH_2A_j^{-1}.
\]
它们均属于 SL2(R_0)，射影上均正向可逆，并且模 n 为 I。模 n² 的精确一阶项是
\[
H_i=I+nX_i\pmod {n^2R_0},
\]
\[
X_1=\frac1d\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
X_2=\frac2\mu\begin{pmatrix}-1&r\\0&1\end{pmatrix},\quad
X_3=\frac2\mu\begin{pmatrix}1&0\\r/d&-1\end{pmatrix}.
\tag{7}
\]
对任意 ell|n，ell 为奇数，且 2、r、d、mu 均为模 ell 单位。因此这三个方向在 sl2(F_ell) 中线性无关。

若 e_ell=v_ell(n)，标准二项式展开给出
\[
H_i^{\ell^k}=I+n\ell^kX_i
\pmod {\ell^{e_\ell+k+1}},\qquad k\ge0.
\tag{8}
\]
这里 ell 奇且 e_ell>=1，故从 k 到 k+1 的所有高次项至少多含一阶 ell。式 (8) 逐层生成从 e_ell 开始的全部主同余层，特别覆盖到 4e_ell。不同 ell 处的主同余有限群均为各自的 ell 群，用指数 CRT 可以隔离各处作用；然后逐层相乘消去目标的一阶误差。

所以这些矩阵模 n⁴ 的像覆盖 Gamma(n,R_0)/Gamma(n⁴,R_0)，接上已包含的深层得到
\[
\boxed{\Gamma(n,R_0)\text{ 正向可执行}.}
\tag{9}
\]
规范代表中的 lambda^-1、delta^-1 只调整射影共同尺度，不额外执行缩放；矩阵条目确属 R_0。实际平均词仍由 D、T、A_j 及其正向逆组成。

## 5. 主同余控制激活任意安全整数返回的逆

**取逆引理。** 假设 Gamma(n,R) 及其逆已经正向可执行。设一个合法的核心自返回在射影上由非奇异整数矩阵 M 表示，且 gcd(det M,n)=1。则 M 的射影逆也正向可执行。

证明：取正偶数 k，使 P=M^k=I 模 n。令 Delta=det P>0。对 P 作整数行列式一的行列变换，写
\[
L P R'=\operatorname{diag}(a,b),\qquad L,R'\in\mathrm{SL}_2(\mathbb Z),\quad ab=\Delta.
\]
这里只需对角化，不要求 a 整除 b；整数 Euclid 行列变换即可。取
\[
S=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad g_*=R'SL.
\]
因为 diag(a,b) S diag(a,b)=Delta S，有 Pg_*P 的每项都被 Delta 整除。

由 gcd(Delta,n)=1、CRT 以及 SL2(Z) 到有限商的满射，可取整数行列式一矩阵 g，使
\[
g=g_*\pmod\Delta,\qquad g=I\pmod n.
\]
于是
\[
h=\Delta^{-1}PgP\in\mathrm{SL}_2(\mathbb Z),\qquad h=I\pmod n,
\]
因为 P=I 和 Delta=1 模 n。g、h、h^-1 均已可执行，而
\[
\boxed{gPh^{-1}=\Delta P^{-1}.}
\tag{10}
\]
再复合 M^(k-1)，得到 M^-1 的正向射影实现。证毕。

引理只用于已经真实存在且全局合法的核心返回，不把任意整数矩阵变成免费物理操作。它也不要求 det M 在 R 中预先可逆。

## 6. 半载体返回提供 3 的反演

仍取 t=r/2。留 r 份原 A；两个相同的 p 组分别取
\[
i=p-j-t\text{ 份 A},\quad j=(p-3)/2\text{ 份 B},\quad t\text{ 份 C},
\]
再平均其余 p 个位置。因为
\[
2j=p-3\le p,\quad2t=r,\quad2i=p+3-2t\le2p-r,
\]
且 i=(p+3)/2-t>0，原位置容量成立。这一返回的整数矩阵是
\[
M_3=\begin{pmatrix}(9-p-r)/2&-3t\\-1&0\end{pmatrix},
\qquad\det M_3=-3t.
\tag{11}
\]
实际尺度为 1/p。n 与 3t 互素，故 M_3 在模 n 下可逆。对未除p的整数输出，直接有 y'=(9/2)y 模 n，其中 y=a+pz，故保存合法域。由第 5 节，它已有正向逆。

与 A_j^-1 复合得到上三角变换
\[
M_3A_j^{-1}
=\begin{pmatrix}3t/d&-(9-p-r)/2\\0&1\end{pmatrix}.
\]
其对上根的共轭及逆共轭把参数乘以 3t/d 及倒数。t、d 已是 R_0 单位，所以根参数环扩张到
\[
R=R_0[1/3],\qquad \mathbb Z[1/6]\subseteq R.
\]
再用 A_j 交换上下根，并重复第 4 节的层级证明，得到 Gamma(n,R) 正向可执行。

顺序明确为：四对合 -> 一个额外对合反演 r -> Gamma(n,R_0) -> M_3 取逆 -> 反演 3 -> Gamma(n,R)。没有用 3 的反演反过来证明 M_3 取逆。

## 7. 二三单位小代表：一个整数下降引理

**引理。** 若 n>7、gcd(n,6)=1，对每个模 n 单位 u，存在整数 b 和 s 属于 Z[1/6] 的单位，使
\[
\boxed{1\le b\le n/11,\quad\gcd(b,6n)=1,\quad b=su\pmod n.}
\tag{12}
\]

证明：先取 u 的正平衡绝对代表 b<=n/2，符号计入 s。若 b 被2或3整除，除去该因子，并相应调整 s。设现在 b 与6互素，且 b>n/11。n、b 都奇。

若 b>n/5，取 c=|n-3b|/2，则 c 为正整数且 c<b。

若 n/7<b<=n/5，按模3选择
\[
c=\begin{cases}
|n-4b|/3,&n=b\pmod3,\\
|n-8b|/3,&n=-b\pmod3.
\end{cases}
\]
相应分子被3整除。在第一种情况，由 n<7b 得 c<b；第二种情况由 n>=5b 得 c<=b，等号只在 n=5b。因 gcd(b,n)=1，等号迫使 n=5，与 n>7 矛盾。

若 n/11<b<=n/7，取 c=|n-9b|/2，则 c<=b；等号只在 n=7b，结合互素性将迫使 n=7，亦排除。

这些分子不能为零：否则 n/b 属于3、4、8、9，与 gcd(b,n)=1、n>7、gcd(n,6)=1矛盾。每次 c 模 n 都是 b 乘一个 +-2^alpha3^beta，仍为单位，并且正整数严格下降。重复操作后必有 b<=n/11，最后除尽2、3因子，得到 (12)。证毕。

本引理不要求2、3生成全部模 n 单位群；每个单位的自身乘法轨道都有足够小的代表即可。除法和取负是用于选择参数的整数运算，不是直接对物理状态施加任意缩放。

## 8. 任意合法核心的精确终端输送

### 8.1 先使 z=0 模 n

取 V=B_k A_j，改到 (z,y)=(z,a+pz) 坐标。直接有
\[
V=p^2\begin{pmatrix}1&-3/p\\0&1\end{pmatrix}\pmod n.
\tag{13}
\]
因为3、p、y都是模 n 单位，选择 V 的一个0至n-1次幂就能使 z=0 模 n。其原位置路径和正向逆由已有对合组成。

输出取本原整数代表 (a,z)，仍有 gcd(a,n)=1、z=0 模 n。所有规范矩阵行列式在 n 的素因子处是单位，所以清分母和本原化不改变这些局部结论。

### 8.2 激活载体保持变换

保留 C 块，两个重复 p 组各取 p-j 份 A 和 j 份 B，再平均剩余 p 组。令 t=p-3j，0<=j<=floor(p/2)，其实际作用为
\[
F_t=\begin{pmatrix}t/p&r(p-t)/(3p)\\0&1\end{pmatrix}.
\]
当 gcd(t,n)=1 时它保持合法域。令 epsilon 属于{1,-1}、p=epsilon 模3，则 F_epsilon 始终安全。pF_epsilon 是行列式为 epsilon*p 的整数矩阵，第 5 节提供其正向逆。因此可执行
\[
C_q=F_tF_\epsilon^{-1}
=\begin{pmatrix}q&r(1-q)/3\\0&1\end{pmatrix},\qquad q=t/\epsilon=1\pmod3.
\tag{14}
\]
只需要一次 C_q 的正向作用，不要求先取得任意 q 的逆。

### 8.3 小代表选择和本原性预处理

将第 7 节用于 u=a^-1 模 n，得 b<=n/11、b与6互素、b=s_0 a^-1 模 n。选 t=b 或 -b，使 t=p 模3。因 n<4p、p>=13，有
\[
|t|\le n/11<4p/11\le(p-3)/2,
\]
所以相应 j=(p-t)/3 处于真实容量范围。置 q=t/epsilon，得到 qa=s 模 n，其中 s=+-s_0 是 R 单位。

先用 L(nh) 使 z 与 q 互素。对每个素数 ell|q，若 z=0 模 ell 则选 h=1 模 ell，否则选 h=0 模 ell，再用 CRT 合并；gcd(a,z)=gcd(q,n)=1 保证有效。这一步属于已实现的 Gamma(n,R)，保留 a 和 z 模 n。

随后执行 (14)。新参数
\[
a'=qa+\frac{r(1-q)}3z,\qquad z'=z
\]
仍为本原整数对，因为 gcd(q,z)=1。并且 a'=s、z'=0 模 n。

### 8.4 用主同余矩阵到达真正终端

选择 alpha、beta 属于 Z[1/6]，使 alpha*a'+beta*z'=s。沿 Bezout 通解调整到 beta=0 模 n，随即 alpha=1 模 n。因此
\[
H=\begin{pmatrix}\alpha&\beta\\-z'/s&a'/s\end{pmatrix}
\in\Gamma(n,R),\qquad H(a',z')^T=(s,0)^T.
\tag{15}
\]
H 已有正向原位置实现，实际输出允许带额外共同非零尺度。此时核心形如
\[
(s^{2p},(-2s)^p,0^r).
\]
取 j=floor(p/3)，再取 p-3j 个零，与2j份 s、j份 -2s 合成零和 p 元组。平均后产生 p 个零，由[统一零触发收尾](prime_arity_interpolation_and_lattice_structure.md)完成全部位置。

第 2 节的全输入入口接上本节，证明定理充分性。必要性由标准共同非零模余数障碍得到，因为 gcd(p,n)=1。定理得证。

## 9. 推进程度及剩余问题

这是整个算术族的全输入证明。新增步骤包括：用一个载体对合同时提供 r 的全部分母；用显式一阶方向补齐 Gamma(n)；用一般整数矩阵的 Smith--CRT 夹乘激活逆；用二三单位小代表绕过“模 n 单位必须本来就可实现”的障碍。

条件 gcd(n,6)=1 有明确作用：n 奇使主同余第一层的系数2可逆；3与n互素使 (13) 的平移可覆盖全部合法方向，也允许合法反演3。不能直接删除该条件。

任意 p 的完整最终阈值仍未证明。剩余包括：上半带偶数 n、被3整除的 n；3p 后最初几个维数及靠近4p的短边界；4p上方旧不等式遗漏的接续点。五平均12、14和七平均20、22不由本定理解决。下半带的一般偶数核心也不能因为本页证明而自动升级。

同样，主同余包含依赖外部存在性定理。本页没有承诺短平均词、统一精度、位长多项式算法，也没有展开任意输入中 H 的完整平均词。

## 10. 核验与文件

[核验程序](../work/verify_upper_band_six_unit_completion.py)只用标准库整数和 Fraction，复用原位置账本。核对24168个二三单位代表，全部六种下降分支；274组参数的2r分母、主同余一阶项及3465个高阶层等式；230个双基原位置对合往返和额外半载体、保载体返回；822条精确终端矩阵构造；23条既有全输入入口；4组保载体逆和2组一般Smith逆的整数夹乘；4条真实零触发收尾。

一般定理由正文的容量、环、层级、整数下降及终端输送证明承担。上述有限检查防止公式与账本错误，不是对无限输入采样得出结论。完整核验约三秒，没有原子词或种子发现搜索。

[核验记录](../work/upper_band_six_unit_completion_records.json)。项目入口：`python work/run_verifications.py --id upper-band-coprime-six-complete`。
