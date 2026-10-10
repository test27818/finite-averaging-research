# H_t文献调查：已有小生成元理论、无条件充分大结论与全范围边界

日期：2026-09-15。调查目标是
\[
n=t^2+t+1,\qquad
H_t=\langle-1,\ d\bmod n:1\le d\le t,\gcd(d,n)=1\rangle,
\qquad H_t\stackrel{?}=(\mathbb Z/n\mathbb Z)^\times.
\]
下文的模数n不是平均元数；对应平均元数是q=t²。

## 1. 调查结论

**这属于已有的“小整数生成剩余类单位群／最小特征非剩余”理论。** 本次未定位到一篇可核查原文，直接以Phi3(t)=t²+t+1为模数并断言所有t>=2的上述精确命题。不能把“本次未找到”写成已知开放问题或原创性结论。

已有文献和初等论证足以取得三项明确结果：

1. **无条件：H_t对所有充分大的t成立。** 直接由Paul Pollack 2017的定理1.1或2.7推出，适用于任意复合模数、任意非主特征，无需无立方因子或本原特征假设。
2. **无条件：若t²+t+1为素数，则该t的H_t成立。** 一页以内的抽屉原理证明，不需要Burgess。
3. **GRH条件下：H_t对所有t>=2成立。** Bach界的正式出版二手陈述给t>=1000；本次精确核验补齐2<=t<1000。该条件性结论不被登记为无条件全解。

因此接[全部平方族入口](general_k_plan_review_and_square_entry_20260915.md)与[完整根和尺度接口](square_arity_uniform_controller_and_nine_thirteen.md)，已经无条件得到：**全部充分大的平方元数q=t²，在n=t²+t+1这个维数上具有完整G=1判据。** 当t为素数幂时，这同时达到旧临界下界，给全部充分大的该类t的M(t²)=H(t²)=t²+t+1。没有得到N(t²)的等式。

无条件剩余可能只在有限个t中，而且这些t的n必须为合数；本次没有取得足够小的明确上界，不能与t<1000的证书强行拼成全称证明。

## 2. 实際检索和阅读范围

本次先直接回读[建议文稿第3至5节](general_k_plan_review_and_square_entry_20260915.md)的H_t定义、终端尺度限制与特征等价式；没有重跑平均词搜索。

外部检索使用OpenAlex题录、Crossref DOI、MathOverflow／Math StackExchange公开接口、作者主页和期刊页，关键词包括small generators、least character nonresidue、proper subgroup、explicit Burgess、composite modulus、imprimitive character及Phi3(t)。OpenAlex缓存汇总有324条去重题录，其中相当部分不相关；它们只算检索线索，不算已读论文。通用网页搜索发生无关结果和连接失败，已弃用这些结果作为证据，转向作者／期刊来源。

**实际取得PDF并阅读相关原文的三篇：**

| 文献 | 本次直接阅读范围 | 对本题的实际作用 |
|---|---|---|
| Paul Pollack, *Bounds for the first several prime character nonresidues*, Proc. AMS 145 (2017), 2815–2826 | 作者PDF第1–4页、第8页第2.3节及定理2.7、参考文献；另查看定理2.7页图像 | 直接给任意模数、任意真子群之外的小素数，证明充分大的H_t |
| Greg Martin、Paul Pollack, *The average least character non-residue and further variations on a theme of Erdős*, JLMS 87 (2013), 22–42 | 正式出版PDF第22–25页，最小非剩余定义、Bach／Norton引用、有限阿贝尔特征引理 | 核对研究对象已有历史，及GRH下3log²n的准确版本；平均值定理本身不能证明全体H_t |
| Hasanalizade、Lin、Martin、Luna Martínez、Treviño, *Explicit Burgess inequalities for cubefree moduli*, arXiv:2511.17778，作者当前预印本 | 第1–3页主定理、适用条件、常数及参考文献；另查看第2页图像 | 核对2025年显式进展及其巨大门槛；不直接完成全部t |

**只核对题录、摘要或被上述论文准确引用，未取得原文的主要资料：**

- Karl K. Norton, *A character-sum estimate and applications*, Acta Arith. 85 (1998), 51–78。期刊题录已确认；PDF下载403。Pollack明确引用其定理1.20及1.30，所以本报告通过实际读到的Pollack定理使用相关结论。
- Glyn Harman, *Integers without large prime factors in short intervals and arithmetic progressions*, Acta Arith. 91 (1999), 279–289。DOI题录已确认；MathOverflow答复指出定理3给小整数生成的Burgess指数界，原PDF403，故不把该定理作为未经原文核对的新主依赖。
- Eric Bach、Lorenz Huelsbergen, *Statistical evidence for small generating sets*, Math. Comp. 61 (1993), 69–82，DOI 10.1090/S0025-5718-1993-1195432-5。直接读题录及摘要，全文403；其更强log n log log n尺度属于启发与数值证据，不能作已证全称界。
- Eric Bach, *Explicit bounds for primality testing and related problems*, Math. Comp. 55 (1990), 355–380，DOI 10.1090/S0025-5718-1990-1023756-8。原PDF403；本报告条件性推论使用Martin–Pollack第22页对其定理3的明确陈述。
- Jain-Sharma、Khale、Liu, *Explicit Burgess bound for composite moduli*, IJNT 17 (2021), 2207–2219，DOI 10.1142/S1793042121500834。题录已确认，原PDF未取得；2025作者预印本第1页Theorem A重述其精确界，已读。

未发送邮件或向外发布问题。所有下载、失败、URL及SHA256保存在[文献缓存](../../work/ht_literature_20260915/source_index.md)。

## 3. 这个对象在文献里叫什么

Bach–Huelsbergen研究最小的g(n)，使不大于g(n)且不整除n的素数生成整个(Z/nZ)^times。本题额外免费加入-1，且所需上界只是
\[
g_{\pm}(t²+t+1)\le t\asymp\sqrt n.
\]
它比猜想中的对数级上界宽松得多，但仍含“每个t”的精确量词。

等价地，若H_t为真子群，有限交换商G/H_t存在非主特征chi。这给
\[
\chi(-1)=1,\qquad
\chi(d)=1\quad(1\le d\le t,\gcd(d,n)=1).
\]
所以必须排除的是**所有非主偶Dirichlet特征**，不只二次特征。一个二次非剩余界不足以排除高阶字符造成的真子群。

MathOverflow的[2014年小生成元问题](https://mathoverflow.net/questions/165809/)及[答复](https://mathoverflow.net/a/165816)也明确将单位群生成、小非剩余、光滑数在等差数列中的分布联系起来。本次阅读了问题与答复全文；论坛用于发现Harman等来源，正式推论以下面的已读论文为依据。

## 4. Pollack定理直接消去全部充分大的参数

[作者PDF](https://www.pollack-math.net/hudson.pdf)，[正式DOI](https://doi.org/10.1090/proc/13432)，[本地全文](../../work/ht_literature_20260915/pollack_hudson.pdf)。作者主页给出的出版信息是2017年，不能因题录的在线日期2016就把卷期写错。

**定理1.1（原文第2页）。** 对每个epsilon>0，存在m0(epsilon)、kappa(epsilon)>0，使每个m>m0以及每个非主Dirichlet特征chi模m都有多于m^kappa个素数ell满足
\[
\ell\le m^{1/(4\sqrt e)+\epsilon},\qquad
\chi(\ell)\notin\{0,1\}.
\]
定义排除了chi(ell)=0，因此这些素数确实与m互素。原文没有假设m为素数，也没有要求chi本原。

**定理2.7（原文第8页）。** 更直接地，任意真子群H<(Z/mZ)^times、指数至少k0，都有许多H之外、不整除m的素数，界为m^(1/(4u_k0)+epsilon)，其中Dickman函数rho(u_k0)=1/k0。取k0=2，u2=sqrt(e)，恢复上述指数。作者给出从字符版推广的说明；本题也可仅用定理1.1加上第3节的商特征，避免依赖这个推广的省略细节。

取固定
\[
\epsilon=\frac14-\frac1{4\sqrt e}>0.
\]
得到对全部m>m0、任意非主特征，都存在安全非剩余素数ell<=m^(1/4)。

现在令m=n=t²+t+1。t>=2时n<t^4，所以
\[
\ell\le n^{1/4}<t.
\]
若H_t真包含于单位群，它的非主商特征在这个ell处必须等于1，与定理矛盾。故
\[
\boxed{\exists T_0\ \forall t\ge T_0:\quad H_t=(\mathbb Z/(t²+t+1)\mathbb Z)^\times.}
\]
这是无条件定理。这里“充分大”对全部特征和子群一致，不是每个t或每个字符各有一个无法统一的例外。

原文没有给本题可直接代入的数值m0。本报告不把它称作已经算出的有效有限检查界，也不因为论文别处使用Siegel就误称定理1.1必然无效：本题只需要承认**这次尚未提取数值界**。

## 5. 素数模数的全范围可以初等完成

**引理。** 若n=t²+t+1为素数，则H_t为整个单位群。

证明：给定a非零模n，考察(t+1)²个数
\[
ai+j\pmod n,\qquad0\le i,j\le t.
\]
因(t+1)²>n，两组不同的(i,j)给同一余数。相减得
\[
a(i_1-i_2)=j_2-j_1\pmod n.
\]
两差都非零：一个为零会迫使另一个也为零，因为绝对值不超过t<n且a可逆。n为素数，分母i1-i2因此也是单位。故
\[
a=uv^{-1}\pmod n,\qquad0<|u|,|v|\le t.
\]
两者都属于H_t，a也属于H_t。证毕。

同一个平方根比值原理见[2023年MathOverflow问题及其所附证明](https://mathoverflow.net/questions/451422/)。本报告给出自足证明，不将论坛当作未核对的无限群定理。

**复合模数不可直接套用。** 小非零分母可能不是单位。更强的“任意奇n的单位群都由-1与不大于sqrt(n)的单位生成”甚至为假：n=105时，小单位只有1、2、4、8，<-1,2>的阶是24，而phi(105)=48。105不是Phi3(t)值，所以该例不反驳H_t；它说明仍需用到特殊模数结构或更强数论工具。

## 6. GRH下全t命题可完整得到

[Martin–Pollack正式出版PDF](https://personal.math.ubc.ca/~gerg/papers/downloads/ALCNFVTE.pdf)第22页明确陈述：在Dirichlet L函数GRH下，对每个模n非主字符，最小满足chi(a)不属于{0,1}的正整数不超过
\[
3(\log n)^2.
\]
该页引用Bach 1990定理3。本次读到的是这份正式出版二手陈述，未取得Bach原PDF。

当t>=1000时，3(log(t²+t+1))²<t。可从t=1000的数值小于573<t起步；函数f(t)=3(log(t²+t+1))²的导数满足
\[
f'(t)<\frac{24\log(t+1)}t<1\quad(t\ge1000),
\]
最后的右侧在此范围递减，故差t-f(t)持续增大。于是所有t>=1000在GRH下成立。

本次用[精确有限阿贝尔商核验](../../work/verify_ht_literature_interfaces.py)处理全部2<=t<1000，共998个参数，其中188个n为素数由第5节覆盖，810个复合n由完整商秩证书覆盖。

算法不枚举整个单位群：先用CRT分解G为奇素数幂单位群的乘积。对每个ell整除|G|，将候选生成元投影到G/G^ell这个F_ell向量空间，验证满秩。若每个ell都满秩，候选子群就不可能包含于任何素数指数的最大子群，因此等于G。各局部离散对数仅在阶ell子群内计算；原根用完整阶因子检查。证书保存实际选中的小素数及其商坐标。

得到
\[
\boxed{\text{GRH}\Longrightarrow\forall t\ge2,\ H_t=(\mathbb Z/(t²+t+1)\mathbb Z)^\times.}
\]
这也条件性完成全部q=t²、n=t²+t+1的全输入判据。若t是素数幂，条件性得到该临界点的M、H等式；仍不是整个后续区间的N等式。

## 7. 最新显式Burgess结果为什么尚未补齐无条件全范围

[2025预印本](https://arxiv.org/abs/2511.17778)，[已取得的作者全文](https://personal.math.ubc.ca/~gerg/papers/downloads/EBICM.pdf)。本次已查看第2页图像，确认下述指数没有被PDF文本提取误读。

其定理1.2适用于本原特征，要求
\[
q\ge\max\{10^{1145},2^{4r-2}\},
\]
且r=2或q无立方因子。定理1.1另有更大的指数门槛，常数因子稍好。其第1页Theorem A重述2021年Jain-Sharma–Khale–Liu的r=2界，模数下界为exp(exp(9.594))。

有三个独立接口仍要补：

1. 这些是特征和界，要与区间内安全整数的数量比较，才得到非剩余；不是现成的H_t全称结论。
2. H_t的商特征可能非本原。按导子降模后，必须处理n额外素数造成的零值／禁用位置，不能直接换个较小模数了事。
3. Phi3(t)不保证无立方因子：Phi3(18)=343=7³；即使t为素数也会出现，例如t=1733时7³整除Phi3(t)。所以不能给全部平方素数幂族免费套上cubefree条件。

即使把上述界有效化完成，10^1145级起点也远远超过可逐t检查的规模。这里不应启动巨大群枚举；应优先寻找更直接的特殊模数结构、较弱但小门槛的有效界，或能解析处理剩余参数的分类。

2025文稿仍是作者列出的预印本；Norton、Pollack的已发表无条件结果才是本报告第4节的主依据。

## 8. 对平均问题的具体推进

已证接口为
\[
\text{全部合法原输入}
\longrightarrow(t²,t,1)\text{核}
\longrightarrow U(R_t),L(nR_t),\Gamma_1(n,R_t)
\xrightarrow{H_t\text{满群}}\text{精确终端}.
\]
结合第4、5、6节，可以正式登记：

- 无条件完成全部n=t²+t+1为素数的平方元数参数。
- 无条件完成所有充分大的t，n可为任意复合数并含任意素数幂。
- 无条件完成全部2<=t<1000的参数；它是有限完整证书，不替代未知T0。
- GRH下完成全部t>=2的这个平方族维数。

例如t=5、q=25、n=31由素数模数引理直接完成；t=7、q=49、n=57和t=9、q=81、n=91由本次有限完整证书及共同入口完成。若需要单独交付某个参数的平均算法，还须提取实际群词；本报告证明的是存在性。

**无条件全t仍未完成。** 不能因为已经证明充分大、又检查了很多小值，就默认两段相接。也不能把“平方族临界点”扩写成“一般合数最优最终阈值”。

## 9. 下一步的优先级

**用户后续已明确允许依赖GRH。** 当前主研究转为[条件性完成后的任务](general_k_grh_stage_and_remaining_tasks_20260915.md)，本节以下关于无条件H_t有效化的建议保留为独立后续，不再阻塞一般k主线。

H_t不再是完全缺少理论支撑的猜想：成熟小非剩余理论已经控制无穷尾部，原问题剩下精确的小界或特殊模数结构。

优先寻找Phi3(t)的初等单位生成论证：n的每个素因子除3外都为1模3，3若出现仅有一次，且t³=1模n。这些约束可能处理一般复合模数平方根命题的非单位分母问题，但本次未给出该修补。

文献方向继续以Norton1998、Harman1999及有效小非剩余为主，重点是获得可证明覆盖所有未检查t的界；若走Burgess显式化，先估算最终门槛，再决定是否值得投入。GRH结论只作结构比较，不作为无条件证明前提。

## 10. 核验与文件

- [外部文献索引与访问记录](../../work/ht_literature_20260915/source_index.md)。
- [t<1000的精确证书](../../work/ht_literature_20260915/ht_through999_certificate.json)。
- [有限核验器](../../work/verify_ht_literature_interfaces.py)，约0.3秒，不搜索平均词或枚举整个模群。
- Pollack外部定理的一般量词由已发表论文承担，程序不“验证”该定理；素数模数引理、指数比较、条件性拼接和对平均问题的接口由本文证明。

核验ID：ht-literature-interfaces。
