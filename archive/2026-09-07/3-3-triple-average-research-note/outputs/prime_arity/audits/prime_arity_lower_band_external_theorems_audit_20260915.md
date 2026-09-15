# 2p 至 3p 区间与外部定理的专项审核

日期：2026-09-15。补充[本轮新进展审核](prime_arity_new_results_audit_20260915.md)，专门回答区间成果是否经过证明审阅，以及 Morris、Serre 的引用是否准确。

结论：本轮再次审阅后，未发现需要撤回全部奇余量及内部偶余量定理的缺口。此前 Serre 一般局部化环特例的文献核对不足，现已取得正式出版综述全文，确认所需的是已证明的平凡同余核结论，且覆盖本项目的所有非平凡有理局部化环。没有取得 Serre 1970 原文全文，不能把本次陈述与适用性核对写成对其原证明的逐页复审。

## 1. 区间结论不是逐个素数的试验

以下 p 为奇素数。严格中间带写成 n=2p+r、1<=r<p；因 gcd(p,n)=1，完整必要条件在这里恰是 G=1。

| 区间部分 | 当前结论 | 审核的证明来源 |
|---|---|---|
| r=1 | 全输入完成；实际上允许任意奇整数平均元数p>=3 | [无条件入口](../proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)与[端点核心](../proofs/lower_band/prime_arity_endpoint_congruence_completion.md) |
| 奇数3<=r<p | 全输入完成，对所有素数p>=5统一成立 | [奇余量核心](../proofs/lower_band/prime_arity_uniform_odd_middle_cores.md)与无条件入口 |
| 偶数4<=r<=p-3 | 全输入完成，对所有素数p>=7统一成立 | [内部偶余量定理](../proofs/lower_band/prime_arity_even_interior_completion.md)与无条件入口 |
| r=2 | omega(p+1)<=2时全输入完成；一般仍开放 | [统一文稿第11节](../tools/prime_arity_unified_weighted_core_theorem.md) |
| r=p-1 | 一般仍开放；有七平均等已完成特例 | 内部定理明确排除该单对合边界 |
| n=3p | 完整p幂G判据已证，此处不能一律写成G=1 | [三块运输与固定模群](../proofs/lower_band/prime_arity_middle_band_structure.md) |

所以对一般p，2p<n<3p只剩2p+2与3p-1两条一般边界；不是还剩许多未检查的内部维数。p=3的小维数用已有三平均判据处理。n=2p不在充分性定理内，该处有合法不可达反例。

例如p=29时，59至86中的全部严格内部维数，除60和86这两条一般边界外，都被统一定理覆盖。这只是说明量词的例子，不是用该例替代一般证明。

## 2. 再次核对的核心连接

### 2.1 全输入到全系统核心

新入口在模rad(n)上实现三单点交换子。逆只在有限环中实现，文稿没有把它当作有理值上的逆；后续入口也只使用有限同余见证。

失效素数整除gcd(p-1,r+2)，其数量不超过r，可由保留单点承接；其余素数的见证通过CRT转移。这一步适用于全部r，并接固定单点支持合并与两轮修复。其输出是覆盖原n个位置的(p,p,r)核心，不是冻结非零外部坐标的局部核心。

### 2.2 奇余量

两个原位置对合给双向根。用Morris、Serre及全部有限商的消元得到主同余包含后，另用夹乘构造保载体返回的正向逆。小代表引理只要求每个二进单位轨道有足够小代表，不假设2是模n原根。

本原性预处理防止施加非单位小整数倍率时发生未经记录的约分。最终精确目标矩阵确属已取得的主同余子群。这些是对任意有理输入的步骤，不依赖有限输入高度。

### 2.3 内部偶余量的三个分支穷尽所有参数

设r=2t、m=p+t。

- t奇：t>=3，用局部射影循环处理方向，用-p/t与e/d处理单位核。证明不再要求旧的3t<=p容量条件。
- t偶且8<=r<=p-5：三个对合参数r-1、r-3、r-5都可行。先做二进深度下降，再用一个模8等于3的倍率与换块控制二进方向；用奇素数循环的CRT幂保留二进结果；最后补单位尺度。
- 剩下t偶的内部情形只有r=4及r=p-3、p=3 mod4。额外迹为正负2的返回先取得真逆并改善根理想，再用固定参数剩余类上的完整二进列证书。

不存在介于上述三分支之间的第四种内部偶参数。r=p-3且p=1 mod4时t奇，已属于第一分支；p=7、r=4使用边界表的第二行。

固定边界证书的参数精度也足够：r=4在模64工作，c_*含一次除二，所以保留p mod128；另一边界的除二、模3分支及模16数据均被p mod192涵盖，tau另穷尽全部奇数模16。程序中的64类及256类因此是全参数覆盖，而不是固定若干实际素数。

局部循环在模3处避开c_s=-3 mod9的退化，两个相邻可行s保证能避开。二进论证从(I+N)^2的精确式开始，没有把奇素数逐层幂公式直接套在浅层模2上。

### 2.4 保留方向之外的尺度

正确有限商是Um_2(R/MR)除以实际R单位的剩余类像。内部偶数文稿在每个分支都另外证明单位核覆盖，然后才用本原列补列引理取得精确有理终端。

因此有限方向覆盖没有直接替代有理可达性。归一化矩阵的共同标量是分析代表选择，实际词始终由原位置平均组成；需要作为R单位使用的标量，另有局部化证明。

## 3. Morris 2007：核对了哪个结论

来源：Dave Witte Morris, *Bounded generation of SL(n,A) (after D. Carter, G. Keller and E. Paige)*, NYJM 13 (2007), 383-421。已读[本地原文](../../../work/research_audit_20260914/morris_muni.pdf)的定理6.1(2)，印刷页416-417；同时核对第2节LU与E的定义，以及第6B节所引用的二维引理与证明结构。

定理6.1(2)的关键原文为：

> For any finite-index subgroup Gamma of SL(n, BS^-1), the set LU(n, BS^-1) intersect Gamma of elementary matrices in Gamma boundedly generates a subgroup of finite index in Gamma.

这里将原文数学排版转写为ASCII；原文在n=2时要求BS^-1有无限多个单位。

在项目中的代入是：

| 外部定理对象 | 本题代入 | 前提检查 |
|---|---|---|
| 数域K及其阶B | Q与Z | Z是Q的整数环，满足阶的要求 |
| BS^-1 | R=Z[1/q]，q>1 | q的不同整数幂给无限多个单位 |
| 矩阵阶数 | 2 | 与原位置数n无关；使用二维无限单位分支 |
| 有限指数子群Gamma | Gamma(h,R)，或端点的Gamma_1(n,R) | 是到有限环矩阵群的约化条件，故有限指数 |
| Gamma中的全部初等矩阵 | U(hR)、L(hR)，或端点U(R)、L(nR) | 由相应同余条件直接读出 |

得到的是这些实际根生成的子群有有限指数。没有把它替换成更大的正规闭包，也没有把仅适用于矩阵阶数至少3的Tits定理直接用于SL2。

该定理不是“任意有限指数子群就是由其初等矩阵生成”；其直接结论仍可能有有限指数差距，下一步需要Serre及有限商消元。

## 4. Serre 强版本：本次新增的正式文献核对

已从Rapinchuk作者主页取得：Gopal Prasad and Andrei S. Rapinchuk, *Developments on the congruence subgroup problem after the work of Bass, Milnor and Serre*, **Collected Papers of John Milnor, Vol. V: Algebra**, AMS, 2010, pp.307-325。

- [作者题录页](https://uva.theopenscholar.com/andrei-rapinchuk/publications/developments-congruence-subgroup-problem-after-work-bass-milnor-and)
- [作者提供的正式重印PDF](https://uva.theopenscholar.com/files/ixqrlw/files/milnor_survey_8.pdf)
- [本地19页全文](../../../work/research_audit_20260914/prasad_rapinchuk_milnor_survey_2010.pdf)
- [提取文本](../../../work/research_audit_20260914/prasad_rapinchuk_milnor_survey_2010.txt)
- [印刷第309页图像](../../../work/research_audit_20260914/prasad_rapinchuk_survey_page309.png)，已实际查看，确认关键数学条件没有被文本提取误读。

### 4.1 原文明确区分“平凡”与“有限”

印刷第308页、第2.1节，把经典CSP定义为每个有限指数子群包含非零level的主同余子群。第309页命题1说明，这恰等价于同余核C^S(G)平凡。

同页第2.3节先写：

> if S contains a noncomplex place ... then C^S(G) is trivial

随后明确写：

> this description of C^S(G) remains valid for G = SL_2 if |S| > 1

并把后一句归于参考文献[49]。该文第324页[49]正是Serre 1970，*Le probleme des groupes de congruence pour SL2*, Annals 92,489-527。

因此这里不只确认同余核有限、中央或阶数至多2，而是确认所需的平凡性。它也不是尚未证明的一般Serre高秩猜想的条件性应用。

### 4.2 所有实际局部化环均符合条件

对R=Z[1/q]、q>1，取数域Q与

\[
S=\{\infty\}\cup\{\ell:\ell\mid q\}.
\]

S包含全部无穷处，且至少两个处。无穷处的完备化是R而非C，故是非复数处。于是

\[
C^S(\mathrm{SL}_2)=1,
\]

每个SL2(R)中的有限指数子群都包含某个Gamma(M,R)。

该核对同时覆盖Z[1/2]、Z[1/65]、Z[1/21]、Z[1/35]及内部偶数证明不断增加安全分母后的环。没有要求分母必须含2，也没有要求q必须是素数。

前提q>1不能删除：q=1对应SL2(Z)，|S|=1，综述同一段明确指出其同余核无限。项目中两个对合的标量互素且相差n>2，不能同时绝对值为1，因此使用外部定理时不是这个例外。

### 4.3 本次审核的准确等级

现在已经核对了正式出版文献中的准确陈述、强弱版本、数域及处的假设、与原文题录的对应，以及在项目各环上的代入。这个等级高于上一轮仅有二进专家答复的交叉支持。

Serre 1970原文全文仍未取得。本次没有重证同余核计算，也不声称逐页核验了其原始证明。对于引用标准已发表定理的研究证明，上述正式综述足以核实本题所引用的特例；若下一步要求原证明级文献审核，仍需另取Serre原文。

## 5. 外部定理怎样接成明确的深主同余包含

令E_h=<U(hR),L(hR)>，R=Z[1/q]、q>1。

1. Morris用于Gamma(h,R)，给E_h在SL2(R)中有限指数。
2. 刚核实的强CSP给某个Gamma(M_0,R)包含于E_h。
3. 把level放大为M=h^2 M_0，可同时确保Gamma(M,R)包含于E_h，且模M能看到Gamma(h^2,R)。
4. 在B=R/MR中，给定g=(a,b;c,d)属于后者的像，选k使u=a+hkc为单位。对除h的素数处a=1；其他处至多一个k类不能选，CRT可同步避开。置v=b+hkd，则

\[
g=U(-hk)L(c/u)\operatorname{diag}(u,u^{-1})U(v/u).
\]

因为u-1属于h^2B，可选t属于hB使ht=u-1，且

\[
\operatorname{diag}(u,u^{-1})
=U(h)L(t)U(-h/u)L(-tu).
\]

所有根参数均在hB，可提升到hR。有限环中的u逆仅用于选择这些参数的剩余类，没有假设u是R中的单位。

5. 对任意g属于Gamma(h^2,R)，上述有限分解给e属于E_h且e=g modM。于是e^-1g属于Gamma(M,R)，也属于E_h。得到

\[
\boxed{\Gamma(h^2,R)\subseteq E_h.}
\]

这一步是对任意有限模数的代数消元，不是程序只测试几个模数。它也说明为何仅有有限模像大还不够：第三步所用的真实主同余核包含不可省略。

## 6. 不属于这条区间证明的外部依赖

Furstenberg拓扑定理只用于一般r=2的有限异常方向归约。它没有参与全部奇余量或内部偶余量的完成，也没有参与omega(p+1)<=2的相邻维数整数下降。因此其原文审核边界不会把这些已完成的分支重新变成依赖Furstenberg的结论。

Furstenberg的准确一维陈述及项目中的闭包推论已作逻辑核对，但其1967原证明仍未全文审核，本次没有提升这一项的文献等级。

CRT、Bezout、局部单位的LTE和本原列补列是本题直接使用的标准初等工具；文稿对需要额外处理的模2及模9情形另有公式。n=3p的固定四陪集证明在射影作用意义下使用Gamma_0(3)，不需要Morris或Serre。

## 7. 核验与修改范围

上一轮12个验证ID全部通过的记录继续有效。本次没有改变数学算法或有限证书，新增的是定向证明复审与正式文献全文核对，没有把下载文献计为一次计算证明，也没有为相同代码重复跑全库。

新增PDF的SHA256为`CA19042C85BDF4E7E3E62F7ED66BD81E6CEC33456F65902715E472E7C9B140A1`，文件571108字节、19页。作者题录、PDF正文页码及参考文献[49]相互吻合。

最终审核意见：区间成果确实达到“除两条一般边界外统一完成”的规模，不能概括成几个固定p的程序证书。证明的主线已经逐项审读，最重要的外部强CSP适用性现有正式全文来源支持；这仍与形式化认证、重证外部深定理、或得到高效完整平均词不同。
