# 九个低偏移的共同完成：改用大载体与两个等大块

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](prime_arity/README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

日期：2026-09-15。p 是平均元数，n 是原位置数。

## 1. 定理、证据和依赖

**定理。** 对每个素数 p>=5，以及每个 1<=s<=9，n=3p+s 的非全等有理输入具有完整可达性判据：中心化、清分母、本原化后的差分 gcd 的素因子只能是 p。若 p 不整除 n，这就是 G=1。

结合已经完成的 [2p<n<=3p](prime_arity_two_p_plus_two_uniform.md)、[全部 n>=3p+10](prime_arity_all_prime_three_p_plus_ten.md) 和 [n=2p 的反例](prime_arity_linear_threshold.md)，得到
\[
\boxed{N(p)=2p+1\qquad(p\text{ 为奇素数}).}
\]
p=3 沿用三平均的独立证明，p=2 的最优最终阈值为 N(2)=4。

本证明不再为 s=1,...,9 分别寻找控制器，而是将它们共同放入
\[
\boxed{(A^p,B^p,C^{p+s})}
\]
形状。主体是一套四原子反射、换块交换子及局部循环。p>=307 的全部参数由闭式计数证明；11<=p<307 的全部 522 对 (p,s) 用**同一接口的一份完整有限证书**核对，只需两个写明的局部补充。p=5、7 已有更强的最优阈值。

因此这里仍含有限的计算辅助容量证明，不能描述成完全没有计算的证明。有限证书只核对有限参数的整数计数、根理想及有限单位群；任意输入、任意高素数幂的方向与精确终端由下面的一般论证承担。

无限群步骤沿用已核对的 Morris 2007 定理6.1(2)、Serre 强 CSP 及项目深同余引理，参见 [外部定理审核](prime_arity_lower_band_external_theorems_audit_20260915.md)。不新增自守形式假设，也不以有限矩阵测试代替这些定理。

## 2. 两次平均改变核心形状

只需处理 p>=11，此时 1<=s<p。已有无条件入口给
\[
(a^{2p},(-2a+sz)^p,(-pz)^s),
\qquad \gcd(a,z)=\gcd(a+pz,n)=1.
\]
仍以 A,B,C 标记旧值。选择整数 t,u，使
\[
0\le u\le s,\quad s\le t+u\le p,\quad
q=3t+u\text{ 与 }n\text{ 互素}.
\tag{2.1}
\]
平均 (A^(p-t-u),B^t,C^u)，产生 p 份 D；从剩余旧 A 保留 r=p+s 份，再平均其余 p 个位置。得到两个 p 块和 r 个相同载体。

将新核心写作
\[
\mathcal L(a',z')=((a')^p,(rz'-a')^p,(-pz')^r),
\quad r=p+s,\quad n=2p+r,
\]
实际返回为
\[
\binom{a'}{z'}=\frac1p
\begin{pmatrix}p-3t-u&st-pu\\-1&0\end{pmatrix}
\binom az.
\tag{2.2}
\]
其新差见证满足
\[
a'+pz'=-\frac q p(a+pz)\pmod n.
\]
所以所有危险素数处的见证同时保留；清分母和本原化仍合法。两次平均都在原 n 个位置上，未调用一个 p+s 维求解器。

若 3 不整除 s，直接取 (t,u)=(s,0)，因为 gcd(3s,3p+s)=1。若 3|s，取 u=1，在 s-1<=t<=p-1 内避开每个 ell|n、ell!=3 的唯一禁止类 3t+1=0 mod ell。

p>=307 时这个短筛必有解。区间长度 L=p-s+1>=(n-33)/3，且 L>=299。若禁止素数数目 h<=4，则密度 rho 至少为24/77，容斥误差小于2^h-1，所以 L rho>2^h-1。若 h>=5，令 M 为这些素数之积；因 3M|n，有 L rho>=phi(M)-11，且 phi(M)>=2880，继续增加素因子时增长超过2倍，仍严格大于2^h-1。较小 p 的具体 (t,u) 已列入完整证书。

此后把新坐标重新记为 (a,z)。因 gcd(p,r)=1，这个大载体核心仍有
\[
\gcd(A,B,C)=\gcd(a,z),\qquad
G=\gcd(a+pz,n).
\tag{2.3}
\]
两个 p 块允许自由交换角色：
\[
S=\begin{pmatrix}-1&r\\0&1\end{pmatrix}.
\tag{2.4}
\]
这正是原 (2p,p,s) 核缺少的对称性。

## 3. 四原子大载体反射的一般计数

从 \(\mathcal L\) 先平均两个不交、组成相同的组
\[
(A^i,B^j,C^k),\qquad i+j+k=p.
\]
记
\[
\alpha=i-j>0,\quad \beta=rj-pk=nj-p(p-\alpha).
\]
得到 2p 份 D=(alpha a+beta z)/p。保留 r=p+s 份 D；剩余旧 A,B,C 和新 D 数目为
\[
p-2i,\quad p-2j,\quad r-2k,\quad p-s.
\]
平均一组 (A^x,B^y,C^u,D^v)，再平均其 p 元补组。注意这里只有**一个输出组及其补组**，不是上半带的两条重复输出行。

完整容量是
\[
\begin{gathered}
2i\le p,\quad2j\le p,\quad2k\le r,\qquad x+y+u+v=p,\\
0\le x\le p-2i,\quad0\le y\le p-2j,\quad
0\le u\le r-2k,\quad0\le v\le p-s.
\end{gathered}
\tag{3.1}
\]
当
\[
p(x-y)+\alpha v=\beta
\tag{3.2}
\]
时，总返回恰为 p^-2 乘
\[
J=\begin{pmatrix}\beta&Q\\-\alpha&-\beta\end{pmatrix},
\quad Q=pry-p^2u+v\beta.
\tag{3.3}
\]
定义 pf=beta²-alpha Q，则
\[
J^2=pfI,\qquad pf=p^4\pmod n.
\tag{3.4}
\]
这里 f 是整数：由 beta=alpha v mod p，有 Q=v beta mod p，故 p 整除 beta²-alpha Q。又 gcd(p,n)=1，故 f 非零且与 n 互素。

每个反射因此有真正的正向射影逆：重复同样四次平均。换到始终幺模的 (z,y)=(z,a+pz) 基，实际模 n 作用为
\[
p^{-2}J\equiv
\begin{pmatrix}1&-\alpha/p^2\\0&-1\end{pmatrix}.
\tag{3.5}
\]
这也直接证明它保持合法性。

## 4. 一套覆盖全部大 p 的公式

取 alpha=s 或 s+1。令
\[
h_0=\left\lceil\frac{p-\alpha-s+6}{3\alpha+s}\right\rceil,
\qquad h=h_0,h_0+1,
\]
并对 e=0,1,2,3 定义
\[
\begin{aligned}
j&=\alpha h,&i&=\alpha(h+1),&k&=p-2\alpha h-\alpha,\\
v&=sh,&x&=\alpha h-e,&y&=k-e,\\
u&=(\alpha-s)h+\alpha+2e.
\end{aligned}
\tag{4.1}
\]
这些数满足 (3.2)，且组成数之和均为 p。

容量只需要
\[
\frac{p-\alpha-s+6}{3\alpha+s}\le h
\le\frac{p-2\alpha}{3\alpha}.
\tag{4.2}
\]
右界保证 x<=p-2i；左界保证 u<=r-2k。y<=p-2j 自动成立，2k<=r 由左界推出，v<=p-s 由 s<=alpha 和右界推出。p>=307、alpha<=10 也保证 x,y,k 非负。

实区间长度至少2，充分条件为
\[
sp\ge\alpha(21\alpha+5s+18).
\]
alpha=s 时右侧除以 s 为26s+18；alpha=s+1 时为26s+65+39/s。这两者在1<=s<=9上都小于304。因此 p>=307 时 h0 和 h0+1 全部可用。

固定 alpha,h，把 e 增加1，恰使 Q 减去 pn、f 增加 alpha n。于是这一个公式提供所需的相邻反射、奇偶调节和模3调节。

## 5. 换块交换子、双向根和主同余控制

先给适用于一般计数证书的接口。若同一个 alpha,j,v 有两条反射，后一条取 (x-1,y-1,u+2,v)，记平方系数为 f,g，则
\[
g=f+\alpha n,\qquad
T=J_f^{-1}J_g=
\begin{pmatrix}1&-\beta n/f\\0&g/f\end{pmatrix}.
\tag{5.1}
\]
与角色交换 S 的交换子为
\[
\boxed{[S,T]=U\!\left(\frac{nH}{g}\right),\quad
H=2\beta+r\alpha=n(2j+\alpha)-2p^2.}
\tag{5.2}
\]
这里 U(t)=(1,t;0,1)。所有逆都已由实际反射和角色交换提供。

令 R0 是由各倍率 g/f 及 f/g 生成的整数环。对 (4.1)，gcd(f,g)=1：因为 gcd(p,alpha)=1、j=alpha h，(3.4) 给 f=p³ mod alpha，再用 gcd(f,n)=1。因此 R0 恰为相应 f,g 的素因子局部化。小参数证书独立核对所有 f,g 的素因子确实被这些**约分后**的倍率反演；没有假定约掉的公因子免费可逆。

各 T 共轭 U 将根参数乘 f/g。由共轭、求逆、根参数相加和整数 Bezout，得到
\[
U(\delta nR_0),\qquad\delta=\gcd\{H\}.
\tag{5.3}
\]
大 p 公式中，相邻 h 的 H 相差2alpha n，而两个 alpha 互素。故 delta|2n；又 H=-2p² mod n，delta 没有奇素因子。n 奇时有奇 alpha 给奇 H，所以 delta=1；n 偶时一条偶 alpha 排除额外的4，故 delta=2。

解释横向根时无需把换基自身当成可执行操作。对任一反射 J，设
\[
P=(e_1,Je_1)=\begin{pmatrix}1&\beta\\0&-\alpha\end{pmatrix}.
\]
精确有
\[
P^{-1}U(t)P=U(-\alpha t),\qquad
P^{-1}J U(t)J^{-1}P=L(\alpha t/\det J).
\tag{5.4}
\]
置 h*=delta n，第二式取 t=(det J)h*x，清去分母；于是 P 基下已有 U(alpha h* R0)、L(alpha h* R0)。深同余引理给 Gamma(alpha² h*²,R0)。换回原基，因 alpha P^-1 和 P 都整于 R0，有
\[
\Gamma(\alpha^3h_*^2,R_0)\text{ 正向可执行}.
\tag{5.5}
\]
不同 alpha 的 gcd 为1时，这些群生成包含 Gamma(h*²,R0) 的群。理由是先模各 level 的公倍数：各素数幂下的主同余条件是嵌套的，CRT 和 SL2 的有限环满射使它们的乘积给 gcd level，再接已知深层。这一步不要求任何 alpha 是 R0 单位。

故大 p 一律已有 Gamma(n²,R0) 或 Gamma(4n²,R0)。小参数证书除一个补充外给 gcd(alpha)=1、delta 属于{1,2,4}，且 delta 的素数都整除 n，故同样得到仅支持于 n 的控制层。具体补充见第9节。

下文统一使用更深但方便的
\[
\mathfrak M=\begin{cases}n^4,&n\text{ 奇},\\64n^4,&n\text{ 偶}.
\end{cases}
\tag{5.6}
\]
上述控制层均包含 Gamma(mathfrak M,R0)。

## 6. 一般配比提供全部终端单位尺度

保留整个大载体，两个 p 块作互补混合。每个奇数 q、1<=q<=p 给真实返回
\[
F_q=\frac1p\begin{pmatrix}q&r(p-q)/2\\0&p\end{pmatrix}.
\tag{6.1}
\]
若 gcd(q,n)=1，其整数代表行列式 pq 与 mathfrak M 互素。已有 [安全整数返回取逆引理](prime_arity_upper_band_unrestricted_completion.md)提供正向射影逆。

先取 q=1，用其上三角倍率反演 p；随后 Fq F1^-1 的倍率是 q，逐个反演所有不除 n、且不大于 p 的奇素数。若 n 奇，(5.1) 中一条奇 alpha 的 f,g 奇偶相反，已经反演2。所以最终 R 的单位像包含全部
\[
1\le q\le p,\qquad\gcd(q,n)=1.
\tag{6.2}
\]
扩环不丢失群控制：上根通过这些上三角倍率对扩环封闭，再用相同反射、(5.4)、(5.5) 得相同 level 的主同余包含。只有有限多个 q 被加入。全部反演素数均不除 n。

**补充倍率也必须计入最终环（2026-09-15整理补入）。** 上述扩环同时适用于下文主单位核所用的全部 `binary_unit` 反射商，以及大参数隔一反射的比值，不能假定它们已属于“原根对＋小数字”生成的环。若实际可逆返回之商为
\[
T=\begin{pmatrix}1&b\\0&\kappa\end{pmatrix},\qquad\kappa=A/B\ne0,\quad\gcd(A,B)=1,
\]
则
\[
TU(x)T^{-1}=U(x/\kappa),\qquad T^{-1}U(x)T=U(\kappa x).
\]
所以已有的全部 \(U(h_*R)\) 扩张为全部 \(U(h_*R')\)，其中
\[
R'=R[\kappa,\kappa^{-1}]=R[1/(AB)].
\]
最后一个等号由整数 Bezout 得到：\(uA+vB=1\) 给 \(u\kappa+v=1/B\)，互换 A、B 得 \(1/A\)。上三角项 b 在根共轭中消去，不要求其分母预先在旧环内。T 及其逆来自已证标量周期的真实反射词，故此次扩环没有增添可达性假设。

将所有这些有限补充倍率纳入最终 R，再用原来的横向反射、(5.4)、(5.5) 及互素 alpha 的 level 合并，在 R 上重新得到同一个 \(\Gamma(\mathfrak M,R)\)。\((11,3)\) 的特殊补充按第9节先取得 alpha=1 反射后使用同一论证。全部约分后的 A、B 与 n 互素，所以危险素数没有被反演。

这一步确实必要：\((p,s)=(11,1)\) 的二进倍率 \(-39/29\) 另需反演13。[独立审核第1节](prime_arity_optimal_threshold_independent_audit_20260915.md)在522组证书中识别出99组有这种额外局部化；它们均由本段同一引理处理。以下的“最终 R”始终指包含这些补充倍率的环。

**模 n 单位覆盖。** p>=307 时，设 d=omega(n)、rho=phi(n)/n。区间[1,p]内的单位数 C 满足
\[
C>p\rho-(2^d-1)>\varphi(n)/4.
\tag{6.3}
\]
第二个不等式由 (n-36)rho>12(2^d-1) 得到。d<=4 时 n>=922、rho>=8/35 已够；d>=5 时 phi(rad n)>=480，故 (n-36)rho>=phi(rad n)-36>12(2^d-1)，增加素因子后仍保持。

正负 [1,p] 的单位代表互不相交，数量超过 phi(n)/2，因此生成的子群只能是整个单位群；等价地，每个单位都是这组正负代表中两个元素之比。小 p 的同一有限单位群满射由完整证书核对。

**主单位核。** 已有单位
\[
\kappa=g/f=1+\alpha n/f.
\tag{6.4}
\]
gcd(alpha)=1 保证对每个奇 ell|n 至少一个 alpha 不被 ell 整除。LTE 给出模 ell^e 下从 v_ell(n) 开始的全部主单位；不同素数处用指数 CRT 分离。

若4|n，奇 alpha 同样覆盖二进主单位。若n=2 mod4，先用奇 alpha 的 kappa 补模4的另一类，再用一个差为2alpha n、alpha奇的 f_(e+2)/f_e 提供精确二进深度2。大 p 的 e=0,1,2,3 自动提供后者。小参数证书或者提供 alpha=2 mod4 的相邻对，或者提供奇 alpha 的隔一对；唯一 (13,3) 的补充见第9节。

所以最终
\[
\boxed{R^\times\longrightarrow(R/\mathfrak M R)^\times\text{ 满射}.}
\tag{6.5}
\]

## 7. 相邻 alpha 一次覆盖全部局部方向

取 alpha 和 alpha+1 的反射 J0,J1，置 V=J0 J1/p⁴。在 (z,y) 坐标下，(3.5) 给
\[
V=\begin{pmatrix}1&-1/p^2\\0&1\end{pmatrix}\pmod n.
\tag{7.1}
\]
平移系数在**每个** ell|n 处都是单位；不再像旧 (2p,p,s) 核那样在模3丢失方向。

使用 [局部射影单循环引理](prime_arity_upper_band_unrestricted_completion.md)第6节：ell>=5 自动在全部 ell 幂上形成单循环；ell=2 只需 tr V=2 mod4；ell=3 只需迹半数归一化的 c=1-4det V/(tr V)² 不等于6 mod9。

大 p 公式中的 e 可以同时保证这两个条件。将 J0 的 e 增加1，未规范化乘积的迹增加 (alpha+1)pn；将 J1 的 e 增加1，迹增加 alpha pn。n=2 mod4 时，至少一个系数为奇数，故可以按 e 的奇偶选择所需二进迹。n=0 mod4 时条件自动成立。

若9|n，c=0 mod9 自动成立。若v3(n)=1，增加 J0 的 e 使 c/3 模3增加 (n/3)/p³，增加 J1 的 e 则减少同一个非零单位。因此即使先固定了奇偶，e=0,...,3 中剩余的两个相差2的选择也能避开唯一坏类。小参数证书直接给出满足这两个有限同余的相邻 alpha 反射。

所以一个 V 已在每个 ell^{v_ell(mathfrak M)} 的合法仿射图上形成全长循环。各循环长度是互素素数幂，指数 CRT 给出一个非负整数 k，将任意合法列送到
\[
z=0\pmod{\mathfrak M},\qquad y\text{ 为模 }\mathfrak M\text{ 单位}.
\tag{7.2}
\]
V^k 是实际反射的正向路径，不是局部逆的形式拼接。

## 8. 同余目标提升为精确归零

这里不要求第7节每个额外反射的行列式已经是 R 单位。它们在 n 的全部素数处可逆，清分母、本原化后的整数列 (z,y) 仍满足 (7.2)，坐标 gcd 为1。使用 [局部本原化引理](prime_arity_three_p_minus_one_completion.md)第5节及 (6.5)，取 epsilon 属于 R 单位且 epsilon=y mod mathfrak M。

取 Bezout 系数 eta z+theta y=1，并使 eta=0 mod mathfrak M，则
\[
P_{\rm end}=\begin{pmatrix}
y/\epsilon&-z/\epsilon\\
\epsilon\eta&\epsilon\theta
\end{pmatrix}
\in\Gamma(\mathfrak M,R),
\qquad
P_{\rm end}\binom zy=\binom0\epsilon.
\]
主同余包含给出真实原位置实现。最终核心是非零共同尺度乘
\[
(\epsilon^p,(-\epsilon)^p,0^{p+s}).
\]
已经有至少 p 个零，接已有统一零触发尾部，全系统有限步归零。这里全输入入口、原位置逆、合法性、方向、单位尺度和精确终端均已给出。

## 9. 小 p 的同一证书，以及两项局部补充

[完整有限证书](../work/large_symmetric_carrier_small_certificate.json)覆盖全部素数11<=p<307和全部1<=s<=9，共522组，不抽样输入高度。每组只列：第2节入口计数、成对反射计数、相邻 alpha 方向计数、需要时的一对二进单位计数。

[独立核验器](../work/check_large_symmetric_carrier_certificate.py)不调用候选生成器。它从每个七元计数(i,j,k,x,y,u,v)重新核对(3.1)、(3.2)、矩阵、平方、根交换子、约分倍率的真实局部化、gcd、模4/mod9条件；再核对整个有限单位群及一般素数幂提升接口。程序的参数集合与全部522组相等，不能用一份有遗漏的成功表代替这项检查。

所有参数都满足前述接口，只有以下两项需要补充。它们不是两套新的平均算法。

### 9.1 (p,s)=(11,3)：消去一个辅助13

取计数(4,2,5,2,5,1,3)及(4,2,5,1,4,3,3)，给
\[
J_f=(-27,568;-2,27),\quad f=-37,
\quad J_g=(-27,172;-2,27),\quad g=35.
\]
此时 alpha=2、H=-26，已有 U(26n R0) 和 Gamma(32·13² n²,R0)，R0=Z[1/(5·7·37)]，n=36。

先由安全 F1 激活11。记 T=Jf^-1 Jg，D=(g/f)^-1 T²，另取真实反射
\[
J_*=(-52,905;-3,52),\quad J_*^2=-11I,
\]
对应计数(4,1,6,2,7,1,1)。令 E=J* D J*^-1，则 D,E 均属于 SL2(R)，且模13为
\[
D=(6,9;0,11),\qquad E=(11,0;8,6).
\]
W=DE³=(5,7;7,10) 是非平凡幂零矩阵加 I，固定列为(1,5)。D 将该列送到(12,3)，两列行列式为8 mod13。因此 W 与 DWD^-1 的幂给两个横向的完整根群，生成 SL2(F13)，已有局部提升引理给所有13幂。

在2、3部分，D,E位于模 n 的主同余核，故像可解。使用 [完美局部群／可解商分离引理](prime_arity_three_p_plus_one_residue_four.md)第5节，13部分从其余像中分离；接已有深层，得到 Gamma(32n²,R)。由 U(26nR) 与 U(32n²R) 作 Bezout，因 n=36，得到 U(2nR)。

另一个实际 alpha=1 反射是 (-38,267;-1,38)，计数(3,2,6,0,4,1,6)。将其代入(5.4)、(5.5)，得到 Gamma(4n²,R)。此后所有扩环仍维持 U(2nR) 和该主同余层，因此辅助13已真正消除，不在后续安全返回的前提里残留。

本例原相邻对只有偶 alpha，故还须明确第6节的二进主单位。37 已是 R 单位，而且 37=1+n；n=36 被4整除，37 在2、3处都恰从 v_ell(n) 层起步，LTE 和 CRT 一次覆盖全部主单位核。

### 9.2 (p,s)=(13,3)：补一个二进单位

此时 n=42。根对已反演13和113；但原证书的相邻单位尚缺精确二进深度2。先用安全 F5 反演5。

使用同一个首次组成(i,j,k)=(4,2,7)。迹零输出(x,y,u,v)=(2,7,1,3)给
\[
J=(-59,1110;-2,59),\qquad J^2=13\cdot97I.
\]
改用仍合法的补组计数(x,y,u,v)=(1,2,0,10)，得到真实非迹零返回
\[
M=(7,-174;-2,59),\qquad\det M=65.
\]
det M 与 n 互素，故其逆由已有主同余层激活。精确有
\[
MJ^{-1}=\begin{pmatrix}-5/97&-192/97\\0&1\end{pmatrix}.
\]
这个实际上三角倍率及逆将97加入 R。于是
\[
\kappa=97/13=1\pmod{42},\qquad v_2(\kappa-1)=2,
\]
正好补齐第6节的二进接口。这里没有把两个不同首次组成的反射商误认为上三角矩阵。

## 10. 为什么这次能共同完成，以及结论的限制

原来小载体只有 s 份，两个重复输出行争用它，迹零条件自然受到模3取整限制。新形状把 p 份位置并入载体，使载体有 p+s 份；两个新 p 块只需一个输出行和补行，所以能用同一个连续参数留下至少四个取整选择。恢复的换块对称还把根理想从带小载体因子的形式降到 n 或2n。

这是一项改变真实块形状的构造，不能解释为在原小载体核里又找到了更长的种子词。它同时处理所有 s=1,...,9。p>=307 的分界只服务于一份统一容量公式，较小 p 由同一有限接口接续，不是结论的素数下界。

核验结果：完整522组小参数、2206条根反射计数全部通过；小参数的两条方向反射也逐一核对。另以1440条通用公式核验大参数计数和局部提升；p<=23的指定反射在两列基输入上逐原位置重放。一般无限量词由第2、4、5、6、7、8节承担。

本结论是有限步存在性及精确可达性判据。仍未给出对可变 p,n 的多项式词长界、实用最短平均算法，亦未解决任意合数平均元数的最优阈值。它不把 G=1 错用于 p|n 的一般维数。

核验入口：`python work/check_large_symmetric_carrier_certificate.py`。
