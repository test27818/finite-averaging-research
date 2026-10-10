# 合数端点核心的统一闭合：有限指数、同余子群与二进根

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../../README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

**2026-09-15全输入完成：** [三单点交换子的无条件入口](prime_arity_unrestricted_endpoint_and_odd_band.md)已删除本页原全输入推论的六素因子和Theta条件。本文核心定理接新入口后，对任意奇p>=3的全部n=2p+1输入，G=1充要；任意素因子个数与指数均包含。下文入口范围和剩余问题保留为原证明阶段，已由该后续结果取代；核心的Morris/Serre依赖不变。

日期：2026-09-14。本页记录详细复查中找到的一个此前未接入的文献接口。p是平均元数，n=2p+1是位置数，p为奇整数且p>=3；素数平均元数是其中的子情形。

## 1. 新结论及证明性质

**核心定理。** 对任意上述p，全部合法双块核心
\[
K_p(a,b)=(a^p,b^p,-p(a+b))
\]
均可经有限次原位置p平均归零。合法性在本原整数参数上为
\[
\gcd(a-b,n)=1.
\]
n不要求是素数幂，不限制素因子个数。

**全输入推论。** 若另有
\[
\omega(n)\le6
\quad\hbox{或}\quad
\Theta(n)=\sum_{\ell\mid n}\frac1{\operatorname{ord}_\ell(2)}
-\min_{\ell\mid n}\frac1{\operatorname{ord}_\ell(2)}<1,
\]
则任意非全等有理n元输入可达全等，当且仅当中心化、本原化后的G=1。

入口来自[六素因子与指数覆盖](../../history/prime_arity_six_prime_endpoint_entry.md)，本页补的是此前独立开放的核心群包含。因此，所有奇数p>=3且2p+1<4849845的端点得到完整判据；更大而满足上述条件的端点同样覆盖。这不是对这些元数的全部后续维数作出结论。

这是引用已发表群论定理的存在性证明。新增有限核验只校验内部公式，不承担有限指数或同余子群定理，也不产生一个高效的全输入平均词求解器。

## 2. 之前具体遗漏了什么

旧[CRT证书路线](../../../general_arity/composite_endpoint_crt_transfer.md)已为36个指定level完成全部回路，却未证明任意level的回路都能找到允许单位主元。模n单位与可实现局部化环单位之间的区别是真实的。

旧2018年文献阅读集中于整个SL2的有界初等生成。此次核对Morris 2007原文发现：**定理6.1(2)还处理任意有限指数子群中的全部初等矩阵**。对本题选取的子群，这些初等矩阵恰好就是已实现的上下根，不需要把“生成的子群”偷换成正规闭包。

这一有限指数结论再与Serre的同余子群定理、下述所有有限商的显式计算组合，可以省去一般整数主元的逐个分解。仅有有限模像满，仍不足以完成这一步；新增的关键前提是有限指数和强同余子群性质。

## 3. 外部定理及来源核对

本页只需在最小环
\[
A=\mathbb Z[1/2]
\]
上调用两项外部结果。

**外部定理F：有限指数子群的初等生成。** 若B是数域的一个整数阶、S为乘法集，且BS^{-1}有无限多个单位，则对SL2(BS^{-1})的任意有限指数子群Gamma，其中全部初等矩阵生成Gamma的一个有限指数子群。

来源：Dave Witte Morris, *Bounded generation of SL(n,A) (after D. Carter, G. Keller and E. Paige)*, New York Journal of Mathematics 13 (2007), 383–421，**定理6.1(2)，印刷页416–417**。[期刊镜像原文](https://emis.muni.cz/journals/NYJM/j/2007/13-17.pdf)，[本地原文](../../../../work/research_audit_20260914/morris_muni.pdf)。

本次已阅读其定义、定理6.1、5.13及引理6.9、推论6.10：秩二在无限单位条件下明确包含。此处取B=Z、S={2^j:j>=0}，A单位无限。使用的是6.1(2)，没有调用仅适用于矩阵阶数>=3的Tits定理6.8。

**外部定理C：A的强同余子群性质。** SL2(Z[1/2])的每个有限指数子群都包含某个主同余子群
\[
\Gamma(M,A)=\ker(\mathrm{SL}_2(A)\longrightarrow
\mathrm{SL}_2(A/MA)),
\qquad M\text{为正奇数}.
\]

这是Serre对SL2的S算术同余子群定理在有理数域、S={无穷处,2}的特例。需要的是这里的强版本，即包含主同余子群，而不只是同余核有限或中央。可先对有限指数子群取有限指数正规核，再使用相应正规子群结论。

来源：J.-P. Serre, *Le problème des groupes de congruence pour SL2*, Annals of Mathematics (2) 92 (1970), 489–527，[DOI](https://doi.org/10.2307/1970630)。本次未取得Serre原文全文；按上述标准已发表特例引用，并与[针对SL2(Z[1/2])的公开专家答复](https://mathoverflow.net/a/225869)交叉核对。答复只作来源核对，不作为本页自证该深定理的替代品。

访问边界：已下载并阅读Mennicke 2000的相关内容，其主要定理是阶数>=3，故未将其直接用于本题。此前已读Morgan–Rapinchuk–Sury 2018的9因子定理也不是这里新增的有限指数接口。

## 4. 二进上下根恰生成Gamma1

对任意正奇数n，定义
\[
\Gamma_1(n,A)=
\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(A):
a,d\equiv1\pmod{nA},\ c\in nA\right\},
\]
\[
E_n=\langle U(A),L(nA)\rangle.
\]

**引理。**
\[
\boxed{E_n=\Gamma_1(n,A).}
\]

### 4.1 有限指数先由定理得到

E_n包含于Gamma1显然。A/nA有限，所以Gamma1在SL2(A)中有限指数。Gamma1中全部上初等矩阵是U(A)，全部下初等矩阵是L(nA)。外部定理F因此直接给出
\[
[\Gamma_1(n,A):E_n]<\infty.
\]
继而E_n在SL2(A)中有限指数。外部定理C给出Gamma(M,A)包含于E_n。将M替换为lcm(M,n)，可设n整除M。

现在只需证明E_n在模M商中覆盖Gamma1的像。M可以很大，不需要先求出它，也不预设一个与n有关的小阶界。

### 4.2 任意有限商中的显式消元

令B=Z/MZ，给定
\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(B),
\qquad a,d\equiv1\pmod n,\quad c\equiv0\pmod n.
\]
对每个素数ell整除M：若a模ell非零，选k=0模ell；否则det(g)=1保证c模ell非零，选k=1模ell。CRT给出一个整数k，使
\[
u=a+kc\in B^\times,\qquad v=b+kd,\qquad u\equiv1\pmod n.
\]
在这个有限环内可以除以u，得到
\[
g=U(-k)L(c/u)\operatorname{diag}(u,u^{-1})U(v/u).
\]

关键是中间对角矩阵也由允许的根产生：
\[
\boxed{\operatorname{diag}(u,u^{-1})
=U(1)L(u-1)U(-u^{-1})L(-u(u-1)).}
\]
三个下根参数c/u、u-1、-u(u-1)均属于nB。所有上根参数属于B。

由于n整除M，这些有限环参数可以分别提升为整数上根参数和n倍整数下根参数。因此存在e属于E_n，使e=g模M。这里的u^{-1}仅用于选取模M的整数代表，**没有把u^{-1}当成A中的单位或新增物理除法**。

对任意原g属于Gamma1，其剩余e^{-1}g属于Gamma(M,A)，后者已由4.1包含于E_n。因此g属于E_n，引理得证。没有由有限样本外推全部M。

## 5. 用一个小主元补齐Gamma0的整数部分

回到n=2p+1、p奇且>=3，令
\[
R_n=\mathbb Z[1/\ell:\ell\le p\text{为素数},\ \ell\nmid n].
\]
已有[统一正向控制器](../../tools/uniform_endpoint_positive_controller.md)在原n个位置实现
\[
U(R_n),\quad L(nR_n),\quad \Delta(R_n^\times)
\]
及其正向射影逆。因为n奇，A包含于R_n，第4节的全部E_n作用已有物理实现。

给定任意整数矩阵
\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(n).
\]
由det(g)=1、n整除c，有gcd(a,n)=1。取a模n的平衡代表u，使
\[
0<|u|\le p.
\]
u的所有素因子均不超过p且不整除n，故u是R_n单位。取整数v满足uv=1模n，置
\[
b_0=(uv-1)/n,\qquad
g_0=\begin{pmatrix}u&b_0\\n&v\end{pmatrix}\in\Gamma_0(n).
\]
有明确分解
\[
g_0=L(n/u)\operatorname{diag}(u,u^{-1})U(b_0/u).
\]
中间对角矩阵射影等于Delta(u^{-2})，所以g_0及其逆可正向实现。

g_0和g的左上元模n相同、右下元也相同，故
\[
g_0^{-1}g\in\Gamma_1(n,\mathbb Z)
\subseteq\Gamma_1(n,A)=E_n.
\]
因此
\[
\boxed{\Gamma_0(n)\subseteq
\langle U(R_n),L(nR_n),\Delta(R_n^\times)\rangle}
\]
在射影意义下成立，对任意奇p>=3均有效。

本节只选择一次小主元g_0；其余无界整数矩阵由第4节处理。因此不需要证明任意回路都有一个小素数光滑主元，也不需要证明所有Gamma0(R_n)的矩阵都采用同一短分解。

## 6. 接回原位置可达性

设核心本原整数参数为(x,y)=(a,a-b)，gcd(y,n)=1。由Bezout选alpha、beta使alpha*x+beta*y=1，再沿通解调整使n整除alpha。于是
\[
H=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}
\in\Gamma_0(n),\qquad H(x,y)^T=(0,1)^T.
\]
第5节给H一个有限生成词；已有正向控制器把每个因子编译成有限原位置p平均，整体非零尺度不改变零目标。所有因子在合法核心上保持合法性，不能把模M消元中的中间矩阵直接当作这个实际词。

输出为K_p(0,s)。先平均-p*s与p-1个零，得到(s^p,(-s)^p,0)。令h=(p-1)/2，再依次平均
\[
(s^h,(-s)^h,0),\quad
(s^h,(-s)^h,0),\quad
(s,-s,0^{p-2}),
\]
完成归零。总共是到达K_p(0,s)之后的四步尾部。

核心定理得证。接上已有六素因子/Theta入口，得到第1节全输入推论。原435435元的K4直接划分障碍输入，现在由已有重叠入口和本页核心定理得到存在性归零结论；本页没有展开其完整操作序列。

## 7. 对全项目状态的影响

- 任意合数端点的合法核心覆盖不再需要逐level证书。旧36份证书保留为显式、可计算的特殊构造。
- 六素因子范围及Theta(n)<1范围从“入口已证”升级为完整端点判据，素因子指数任意。
- 全部端点的剩余统一问题集中到尚未满足入口充分条件的多素因子输入。六个坏指数类的覆盖障碍仍在；不能凭核心完成就删除这一问题。
- n>2p+1的相对尺度、非等重块核心及一般阈值不由本页解决。没有得到N(p)=2p+1或N(p)<=3p。
- 证明使用非显式的同余子群包含模数，不承诺短平均词、一位精度、位长多项式算法或可直接运行的通用求解器。

## 8. 独立核验

[核验程序](../../../../work/verify_endpoint_congruence_completion.py)采用有限环整数算术、CRT选取和精确分数；不搜索平均词。

已完成34个有限商/level组合，比较由U(1)、L(n)生成的全部有限群与目标子群，共184597个目标元素；对4947个选取的矩阵检查第4节分解。另核对9422个平衡单位及整数陪集归约，并用已有正向编译器检查28个g_0及其逆。

有限群比较是公式的独立诊断；第4节的任意模数论证和两项外部定理才承担一般群等式。编译器检查只覆盖g_0部分，不声称已构造第4节存在性证明中所有Gamma1元素的高效分解。

结果：[endpoint_congruence_completion_records.json](../../../../work/endpoint_congruence_completion_records.json)。文献与访问边界：[本次审查材料](../../../../work/research_audit_20260914/README.md)。
