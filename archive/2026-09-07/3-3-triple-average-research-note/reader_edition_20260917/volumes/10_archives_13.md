# 工作材料、历次快照及旧目录完整附卷 · 第13分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [临界双块的局部几何、素数幂完整证明与 theta 联系](#doc-516c101897ab)
- [合数研究阅读记录](#doc-e41152995bbd)
- [历史路线账本（2026-09-15归档）](#doc-1d066819e7ff)
- [七平均十五元完整G判据：两素数入口与二进 \(\Gamma_0(15)\) 覆盖](#doc-a4ff935be716)
- [七平均 (n=14) 与 (n=15) 对照实验](#doc-c804878969e3)
- [七平均 (n=15) 数值证据](#doc-b26fccfa3c79)
- [七平均的最优最终阈值：二十元、二十二元与 N(7)=15](#doc-cfae2c05db78)
- [七平均达到 3p+2：对称碰撞总和的完整证书](#doc-e64084cd15fa)
- [为什么三平均的精确阈值是七：资源边界、有限周期与合法单轨道](#doc-58f23beef83d)
- [六平均九元：所有输入固定四步完成](#doc-4c0a86ab6d12)
- [六平均十元完整G判据：第一个非自动的算术成功维数](#doc-11fc9beac1cb)
- [平方元数的统一正向控制器与九平均十三元](#doc-342d5ac6c14f)
- [十平均十六元与一族确定性三块网络](#doc-016b9066b0a0)
- [十平均与十二平均17元完整G判据，以及原B公式中的自动维数](#doc-efc595179bd5)

---

<a id="doc-516c101897ab"></a>

## 原文导签：临界双块的局部几何、素数幂完整证明与 theta 联系

来源：`work/document_reorganization_20260915/originals/outputs/prime_power_endpoint_and_critical_geometry.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/prime_power_endpoint_and_critical_geometry.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-516c101897ab -->
# 临界双块的局部几何、素数幂完整证明与 theta 联系

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

2026-09-14后续：[任意合数核心同余闭合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)已补齐一般level的合法核心覆盖。本页素数幂的显式两图证明、theta联系和外部坐标尺度障碍仍独立有效；任意原输入的入口尚需条件，六素因子/Theta入口范围现已完整可达。

日期：2026-09-12。p 表示平均元数，q=2p+1 表示原位置数。

**同日后续：** [七平均十五元](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_fifteen_complete.md)补齐一个非素数幂level：两素数三步入口、CRT的24个标签及二进主元分解证明完整 \(\Gamma_0(15)\) 正向覆盖。该结果独立于本页的素数幂两图证明，也不自动推广到全部多素数level。

**有限合数族已扩展：** [合数端点统一证书](../sources/work/document_reorganization_20260915/originals/outputs/composite_endpoint_crt_transfer.md)覆盖全部 \(n\le219,\ n\equiv3\pmod4\) 的双素因子level。结合本页的素数幂定理，所有奇整数 \(3\le p\le109\) 除97外的 \(2p+1\) 端点已解决；p97的level195只完成核心覆盖，仍缺一般入口。

本页续接《p 平均临界前沿》及统一正向控制器。主要新增结果如下。

**定理。** 对任意奇整数 p>=3，若 q=2p+1 是素数幂，则任意非全等有理 q 元输入，中心化、清分母及本原化后的 G=1 当且仅当它能在原 q 个位置上经有限次 p 平均达到全等。

特别地，十三平均二十七元现在具有完整证明；(p,q)=(1093,2187) 也由同一证明覆盖。这里没有假设每个 3 的幂都会给出素数平均元数，也没有证明 N(13)=27 或全部 n>=2p+1。

本页同时给出两个结构解释：临界能量是一个虚二次整数阶的范数，确实产生权一模形式；全局射影逆嵌入更大系统后不再是逆，这精确解释了相邻维数传播的一处困难。

## 1. 不是仅多了一个可供凑数的位置

两块压缩在 n=2p 时只留下

\[
(a^p,(-a)^p).
\]

非零本原形状的 G=2，对奇数 p 不可达零。其射影参数空间只有一个点。

在 n=2p+1，压缩留下

\[
K_p(a,b)=(a^p,b^p,-p(a+b)),
\quad (x,y)=(a,a-b).
\tag{1}
\]

这里有两个线性参数、一个射影参数。对本原 (a,b)，

\[
G(K_p)=\gcd(a-b,q)=\gcd(y,q).
\tag{2}
\]

所以临界核由“有理射影直线，外加每个 ell|q 处的禁止方向”组成。合法方向满足 gcd(y,q)=1。

更关键的是，整个系统恰好都在这个核内。一个返回若整体乘了非零标量，达到零的目标不变；这个共同尺度可以在控制方向时略去。这个性质在将核嵌入更大系统时会失效，见第 7 节。

## 2. 已有正向资源，使纯算术证明现在可以落到原位置

[统一正向控制器](../sources/work/document_reorganization_20260915/originals/outputs/uniform_endpoint_positive_controller.md)已经证明，在原 q 个位置上可以正向实现

\[
\mathcal H_q=
\left\langle U(R_q),L(qR_q),\Delta(R_q^\times)\right\rangle,
\qquad
R_q=\mathbb Z[1/\ell:\ell\le p\text{ 素数},\ \ell\nmid q],
\tag{3}
\]

其中

\[
U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},\quad
L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix},\quad
\Delta(t)=\operatorname{diag}(1,t).
\]

这里每个生成元及其逆都有明确的有限正向词，等式在非零共同尺度意义下成立。所有叶操作都是原 q 个位置上的两次 p 平均或常值块账本重标记。并没有物理执行其他素数分母的除法。

因此本轮只需证明一个纯代数包含，就能得到真实输送。与历史三平均的条件种子方案不同，(3) 的正向实现前提已经完成，不能再把它当作未知。

## 3. 素数幂的真正优势：局部环只有两张坐标图

设 q=ell^r，ell 为奇素数。模 q 的本原行 (c,d) 至少有一个坐标是单位，因为两坐标若都被 ell 整除就不本原。

因此

\[
\mathbf P^1(\mathbb Z/q\mathbb Z)
=\{[1:j]:j\bmod q\}
\ \sqcup\ \{[t:1]:t\in\ell\mathbb Z/q\mathbb Z\}.
\tag{4}
\]

第二张图仅取第一坐标非单位的部分，故不重复。总数为 q+q/ell。

素数情形第二张图只有 [0:1]，这就是旧 q+1 陪集证明。素数幂并没有要求一种新的种子，只是第二张图扩大了。

把整数代表统一选在 [-p,p]。取

\[
A_j=ST^j=\begin{pmatrix}0&-1\\1&j\end{pmatrix},\quad -p\le j\le p,
\]
\[
B_t=L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix},\quad
-p\le t\le p,\quad \ell\mid t,
\tag{5}
\]

其中 S=[[0,-1],[1,0]]、T=U(1)。底行正好给出 (4)，所以 (5) 是 Gamma_0(q) 在 SL_2(Z) 中的完整右陪集代表；B_0=I。

这里的 S 和代表 B_t 是证明用的矩阵，不是额外物理操作。只有下面的闭合回路需要编译为可执行词。

### 3.1 第一张图的全部转移

右乘 T^epsilon，epsilon=+-1，把 j 送到 j'=center_q(j+epsilon)。回路为

\[
A_jT^\epsilon A_{j'}^{-1}
=L(-(j+\epsilon-j'))\in L(q\mathbb Z).
\tag{6}
\]

右乘 S 时：

- 若 ell 不整除 j，取 k=center_q(-j^{-1})，有
\[
A_jSA_k^{-1}=\begin{pmatrix}-k&-1\\jk+1&j\end{pmatrix}.
\tag{7}
\]
- 若 ell 整除 j，下一代表为 B_{-j}，回路为 -I。

### 3.2 第二张图的全部转移

右乘 S 有 B_tS=A_{-t}，回路为 I。

右乘 T^epsilon 时，1+epsilon t 是模 q 单位。令

\[
t'=\operatorname{center}_q\left(\frac{t}{1+\epsilon t}\right),
\qquad \ell\mid t'.
\]

直接计算得到

\[
\boxed{
B_tT^\epsilon B_{t'}^{-1}
=\begin{pmatrix}
1-\epsilon t'&\epsilon\\
t-(1+\epsilon t)t'&1+\epsilon t
\end{pmatrix}.}
\tag{8}
\]

左下项被 q 整除，左上项 u=1-epsilon t' 是模 ell 单位，而且

\[
0<|u|\le p+1.
\tag{9}
\]

这就是遗漏的回路族。它不需要除以非单位 t，也不需要除以 ell。

### 3.3 为什么这些回路的主元全部已经可逆

若 0<|u|<=p 且 gcd(u,q)=1，则 u 的每个素因子都属于 (3) 已允许的集合，故 u 是 R_q 单位。

唯一额外边界 |u|=p+1 也成立：p 为奇数，p+1 为大于二的偶合数，其每个素因子至多 (p+1)/2<=p；又 gcd(p+1,2p+1)=1。

任何行列式一的矩阵 g=[[u,v],[w,z]]，只要 u 是 R_q 单位且 w 属于 qR_q，就有

\[
g=L(w/u)\operatorname{diag}(u,u^{-1})U(v/u).
\tag{10}
\]

中间因子射影等于 Delta(u^{-2})。所以 (7)、(8) 及 (6) 的全部回路都属于 H_q，而且每一个都有已证的正向实现。

**例：q=27。** B_3T 的下一代表为 B_{-6}，其回路恰为

\[
\begin{pmatrix}7&1\\27&4\end{pmatrix}
=L(27/7)\operatorname{diag}(7,1/7)U(1/7).
\]

7 已是十三平均控制器的安全可逆倍率。这不是搜索出的新宏，而是 (8) 的直接代入。

### 3.4 完整群包含

S,T 生成 SL_2(Z)，并且 -I 的射影作用平凡。完整陪集的全部 S、T、T^{-1} 回路已经属于 H_q。Schreier 生成定理于是给出

\[
\boxed{\Gamma_0(q)\subseteq\mathcal H_q\quad\text{（射影意义下）},
\qquad q=\ell^r.}
\tag{11}
\]

也可以直接理解为沿任意 S,T 词逐边插入代表及其逆：起点和终点同为 B_0 时，整个词望远镜式分解为上述回路。

这证明的是无限整数群的包含，不是只计算了模 q 群像。有限代表是生成定理的工具。

## 4. 从完整群到任意输入：补齐素数幂端点

给定本原整数参数 (x,y)，gcd(y,q)=1。先取 ux+vy=1，再用

\[
(u,v)\longmapsto(u+ky,v-kx)
\]

令 q|u。于是

\[
H=\begin{pmatrix}y&-x\\u&v\end{pmatrix}\in\Gamma_0(q),
\qquad H(x,y)^T=(0,1)^T.
\tag{12}
\]

由 (11)，H 能以真实正向 p 平均实现到非零共同尺度。因此 K_p 到达 K_p(0,s)。先平均 -ps 与 p-1 个零，得到 (s^p,(-s)^p,0)；随后两次各取 (p-1)/2 个 s、同样多 -s 和一个零，最后取 (s,-s,0^(p-2))，四次完成。

对任意 G=1 原输入，[临界前沿第 6 节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_critical_frontier_handoff.md)已证明至多两次 p 平均可进入合法 K_p。简述：保留任意单点 c，剩余两块若块和差被 ell 整除，则交换一对跨块不同余位置，使差改变 2(y-x) 而成为 ell 进单位。全局零和保证这种不同余对必存在。

将入口、(12)、完整回路分解、正向编译及四步尾部连接，证明开头定理。必要性由共同非零模 ell 余数不可消除得到。

有限终止来自 Euclid/Bezout 和有限的群词分解；每个回路编译为有限正向词。这里不依赖“分母不断增长时实能量仍严格下降”这一不足的终止理由。

**范围：** p 本身若为奇素数而 q 是合数素数幂，必有 q=3^r、r 为奇素数，但并非每个 r 都使 p 素。新增包括 (13,27)、(1093,2187)；形式定理也覆盖奇合数平均元数，例如 (121,243)、(171,343)。它不提供统一一位额外精度或多项式原子词长。

## 5. 能量、判别式与虚二次阶：真实的模形式联系

临界能量为

\[
E(K_p)=pQ_p(a,b),\qquad
Q_p=(p+1)(a^2+b^2)+2pab.
\]

令 z=a+b、h=(p+1)/2。整数幺模换元给出

\[
\boxed{\frac{Q_p}{2}=a^2-az+hz^2.}
\tag{13}
\]

因为 p 奇，q=2p+1=3 mod4。令

\[
\omega=\frac{1+\sqrt{-q}}2,
\qquad \mathcal O_q=\mathbb Z[\omega].
\]

这是判别式 -q 的虚二次整数阶（不要求它是极大阶），且

\[
\boxed{E(K_p)=2p\,N_{\mathbb Q(\sqrt{-q})/\mathbb Q}(a-\omega z).}
\tag{14}
\]

因此 q 同时出现在共同余数障碍、能量格判别式及二次阶判别式中，有明确的整格来源。

### 5.1 判别式模与 level

偶格 L=Z^2 的 Gram 矩阵为

\[
B=\begin{pmatrix}2&-1\\-1&p+1\end{pmatrix},\qquad
\det B=q,\qquad
qB^{-1}=\begin{pmatrix}p+1&1\\1&2\end{pmatrix}.
\tag{15}
\]

因为 B 有元素 -1，Smith 不变量为 (1,q)，故 L^*/L 是阶 q 的循环群。qB^{-1} 为偶整矩阵，而 B^{-1} 的非对角项分母恰为 q，所以格的 level 恰为 q。

这些都是精确恒等式，不是从同余子群名称反推的类比。

### 5.2 权一 theta 级数

由正定偶格 theta 级数的标准模性定理，

\[
\Theta_p(\tau)=\sum_{a,z\in\mathbb Z}
\exp\bigl(2\pi i\tau(a^2-az+hz^2)\bigr)
\in M_1(\Gamma_0(q),\chi_{-q}),
\tag{16}
\]

其中 chi_{-q}(d) 是 Kronecker 符号 (-q/d)，允许非本原特征。

具体关联文献：Ernst Kani, *Binary theta series and modular forms with complex multiplication*, DOI [10.1142/S1793042114500134](https://doi.org/10.1142/S1793042114500134)。本轮核对题录与摘要，其中明确将二元 theta 空间解释为具有相应 CM 特征的权一模形式空间；未声称取得其全文。式 (16) 采用标准偶格 theta 模性定理，(13)--(15) 则在本页直接计算。

这条联系可以研究能量值的表示数、不同理想类的 theta 分解、局部密度及 Hecke 在表示数上的作用。q=3^(2m+1) 时，底层数域固定为 Q(sqrt(-3))，改变的是 conductor=3^m 的整数阶；但第 3 节的完整端点证明不依赖该阶的类数。

还应注意，(16) 的模群作用在复变量 tau 上；控制器作用在状态参数 (a,b) 上。这两种作用不能因同样出现 Gamma_0(q) 就视为同一个表示。U(1)、L(q) 也不保持 Q_p 到固定比例；所以不能把所有真实宏直接解释为这个 norm torus 或其 Hecke 对应。

本轮实际核对了 [LMFDB 的 level 27、weight 1 页面](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/27/1/)：M_1(Gamma_1(27)) 的尖点子空间为零，模形式总维数 15 全属 Eisenstein 部分。因而十三平均二十七元的自然 theta 级数并不提供可调用的权一尖点谱。这不否定模形式联系，但提醒我们不能假定这里一定有一个缺失的尖点谱定理在等待使用。

### 5.3 最自然的 Fricke 型对偶恰好跨到禁止方向

在 (s,y)=(a+b,a-b) 坐标中，

\[
Q_p=\frac{q s^2+y^2}{2}.
\]

范数几何自然给出

\[
W_q=\begin{pmatrix}0&1\\-q&0\end{pmatrix},\qquad
W_q^2=-qI,\qquad Q_p(W_qv)=qQ_p(v).
\tag{17}
\]

但若 y 是模 ell 单位、ell|q，则 W_q(s,y)=(y,-qs) 的第二坐标被 ell 整除，第一坐标仍为单位，故本原化后变成不合法方向。

因此这个最自然的对偶不能作为合法核上的正向可逆宏。它解释了为何“有二次型和模形式，便可用伴随／Fricke 直接求逆”仍会失败。已有控制器成功是因为它构造了保持合法侧的其他正向逆。

## 6. 两张图背后的树几何，以及多素数为何不同

在 Q_ell 的 Bruhat--Tits 树上，局部条件 c=0 mod ell^r 是稳定下列两个格类的条件：

\[
\Lambda_0=\mathbb Z_\ell e_1+\mathbb Z_\ell e_2,
\qquad
\Lambda_r=\mathbb Z_\ell e_1+\ell^r\mathbb Z_\ell e_2.
\]

它们距离 r；稳定两个端点也稳定中间整条测地段。r=1 是通常的 Iwahori 边稳定子；r>1 应称段稳定子，不能都误称为同一个边稳定子。

第 3 节是这个局部结构的显式整数坐标版本：保留哪一侧为单位，决定选哪张图；小的平衡代表使回路主元落入已经可逆的范围。真正推动证明的是这最后的主元界，而不只是给群贴上树几何名称。

若 q 有多个素因子，CRT 给

\[
\mathbf P^1(\mathbb Z/q\mathbb Z)
\cong\prod_{\ell^r\Vert q}\mathbf P^1(\mathbb Z/\ell^r\mathbb Z).
\tag{18}
\]

可以在某个素数处第一坐标为单位、另一处第二坐标为单位，从而两个坐标都不是模 q 单位。例如 q=15 的 [3:5]。这类混合位置不属于任何一张全局单位图。

对 q=15，完整空间有 24 点；“c 是单位”与“d 是单位”的两张图合起来只有 22 点，额外两点正是 [3:5] 与 [5:3]。所以七平均十五元确实进入了另一个局部拼接问题；它不是十三平均二十七元的计算规模缩小版。

这给后续一个精确任务：在混合图之间选择整数代表，使全部闭合回路能用安全单位消元，或直接证明合法轨道覆盖。这里仍需同步处理核外入口；已知 K4/CRT 反例否定一般直接 (p,p,1) 划分。完成其中一个任务不等于完成另一个。

## 7. 为何临界控制器不能直接嵌入 2p+2：失去的是共同尺度

研究

\[
(a^p,b^p,c,d),\qquad p(a+b)+c+d=0.
\]

冻结 d，在另外 q 个位置使用局部控制器。局部均值是 mu=-d/q；局部中心化参数为 a-mu、b-mu。

旧控制器的 J=T_h 满足 J^2=hI；实际返回是 J/p，所以连续两个这样的返回把局部中心化状态乘以

\[
\lambda=\frac{h}{p^2},\qquad 0<\lambda<1.
\]

于是实际局部作用为

\[
v\longmapsto\mu\mathbf1+\lambda(v-\mu\mathbf1),
\qquad d\longmapsto d.
\tag{19}
\]

在三个自由参数 (a-mu,b-mu,d) 中，它是 diag(lambda,lambda,1)。若 d 非零，这不是共同标量，所以局部“射影单位词”在全局已不再是单位。

**一般尺度引理。** 设真实平均词 W,V 保持一个线性状态族，并都固定某个在该族上不恒为零的外部坐标。若它们在全族上满足 VW=lambda I、lambda!=0，则 lambda=1，且 W,V 的每个实际平均在该状态族上都只能是恒等作用。

证明：读取固定坐标给 lambda=1。每次平均是欧氏正交投影，故

\[
\|x\|\ge\|Wx\|\ge\|VWx\|=\|x\|.
\]

每次投影都必须取等号；投影取等号只在已位于其像上时成立，因此该平均不改变输入。对所有 x 重复即得结论。若使用块账本重标记，它只是等距识别，不改变这个能量论证。

这个引理不排除状态相关路径、同时动用两个单点，或变换块形状。它排除的是“冻结一个一般非零外部坐标，把旧射影逆当作全局逆”的接口。

d=0 时，局部收缩又是全局收缩，这正与已有零触发收尾相吻合。非零外部坐标是需要控制的真实尺度参照，不能在射影化时丢掉。

## 8. 研究路线现在可以更具体

对于端点本身，已有证据支持的核心对象是：带循环同余障碍的秩二加权零和格，以及其上已实际实现的局部化算术作用。素数幂情形的局部环结构已足以完成证明。

接下来应优先处理两种不同问题。

1. **七平均十五元等多素数端点：** 构造 (18) 中混合图的可编译回路，并处理能够改变见证分布的真实入口。目标是完整轨道和入口，不是再搜种子。
2. **五平均十二元等相邻维数：** 保留 (19) 的实际尺度，交替使用不同单点作局部中心，研究相对尺度与零和超平面的可达性。每个候选必须给出实际矩阵和终止依据；不先假设存在三维可逆群。

模形式在第 5 节具有精确对象，可用于研究范数、理想类和计数规律；本轮完成端点所借到的有效工具是局部射影线与 Schreier 生成。两者可以相互提供结构信息，但目前没有证明 theta 或 Hecke 系数能够选出一条原位置平均路径。

不应声称找不到某种更深理论就“不可能成功”：本轮的素数幂推进只需标准局部代数，却确实填补了一个完整无限量词。应要求每个结构解释能产生新分解、排除假接口或减少未证命题，而不是要求它必须属于某一门强大理论。

## 9. 独立核验与证明效力

`work/verify_prime_power_endpoint_completion.py` 不搜索平均词。它独立重建两张图、所有生成元转移、单位主元界及有理 Gauss 分解，再调用已有正向控制器的编译接口核对实际可用性。

本轮通过：9 个 level（包括 27、243、343、1331、2187）的 15612 条完整转移方程；55512 个本原模行的标签核验；168 条回路的正向无环编译及 48 个叶返回的原位置双基重放；32 个大整数入口与精确 Bezout 输送；2 条十三平均二十七元的完整 Fraction 路径（最长 2466 步）；2754 个能量／范数恒等式和 4 个冻结尺度例子。

这些有限检查核对实现与公式；一般素数幂的完整定理由第 3、4 节的通用回路和已证入口承担。大正向词用无环乘积图表示，未把它们全部展开；其有限性来自已证编译规则，不声称原子长度短。

核验入口：`python work/run_verifications.py --id prime-power-endpoint-completion`。

本页新增完整端点，但不降低一般 N(p) 上界，不证明七平均十五元、五平均十二元，亦不证明整个 2p+1 至 3p 区间。

<!-- END SOURCE doc-516c101897ab -->

---

<a id="doc-e41152995bbd"></a>

## 原文导签：合数研究阅读记录

来源：`work/document_reorganization_20260915/originals/outputs/research_reading_log_20260915.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/research_reading_log_20260915.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-e41152995bbd -->
# 合数研究阅读记录

日期：2026-09-15。本记录区分上一次合数调查实际读过的内容与用户提醒后本次补读的内容；不把间接引用计作读过原文，也不把阅读计作重新验证证明或程序。

## 用户指定的六篇

| 文档 | 上一次调查的实际阅读范围 | 本次补读与保留的要点 |
|---|---|---|
| [全局状态](../sources/work/document_reorganization_20260915/originals/outputs/averaging_global_status_20260912.md) | 直接分段阅读定义、小元数状态和临界猜想，未完整重读后半部 | 补读后半部；M、H、N及自动G维数必须区分，旧开放状态须按最新证明更新 |
| [合数临界尺度与猜想](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md) | 直接阅读S(q)下界、赋值陷阱、B/C猜想、固定网络及八平均核心等主要证明段落 | 补读此前输出中未完整显示的网络及八平均段落；局部尺度的最大值仅是已证必要下界，充分性仍是猜想 |
| [任意元数线性阈值](../sources/work/document_reorganization_20260915/originals/outputs/arbitrary_arity_linear_threshold.md) | 直接读到非单位差分、背景引理及三个重值分类，约第1至6节 | 补读第7至10节：一般EGZ、整数能量终止、阈值推算、四／六平均零触发及证据范围 |
| [四平均九元](../sources/work/document_reorganization_20260915/originals/outputs/four_average_nine_complete.md) | 当时只有结论和相关文档引用，未单独通读正文 | 本次全文阅读；除了36条完整Schreier回路，第6节还已经给出全部偶数元数的种子公式 |
| [四平均七元](../sources/work/document_reorganization_20260915/originals/outputs/four_average_seven_complete.md) | 已直接分段阅读入口、三个宏、周期、二进根、全部回路及终端 | 本次复核末尾范围；它是新平方元数参数恒等式的直接起点，不应将其思想说成全新发现 |
| [六平均九元固定网络](../sources/work/document_reorganization_20260915/originals/outputs/six_average_nine_fixed_network.md) | 已在composite_arity_four_six_transfer.md第6节读过同一四步网络及证明，未单独读这篇全文 | 本次全文阅读，尤其核对固定三步网络不可能的行系数证明；固定全输入最优四步不等于每个输入都需要四步 |

以上六篇本次补读后均已直接参考正文。这只说明阅读范围，不表示本次重新运行了六份旧核验器，亦不表示旧稿中的每个历史状态句都代表当前结论。

## 上一次调查另外直接使用的主要材料

- [四／六平均与原位置副本转译](../sources/work/document_reorganization_20260915/originals/outputs/composite_arity_four_six_transfer.md)：秩障碍、正确副本子空间模拟、同时好划分、半块转译、六平均九元网络和最小赋值陷阱。
- [十／十二平均十七元](../sources/work/document_reorganization_20260915/originals/outputs/ten_twelve_average_seventeen_complete.md)：自动B点、两步合法入口、两步返回模板及共同二进控制机制。
- [端点同余闭合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)：实际根生成Gamma1的精确引理；新九平均十三元证明直接引用。
- [无条件端点与奇数中间带入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unrestricted_endpoint_and_odd_band.md)：有限环正向逆、三单点交换子及真实见证转移。
- [外部定理审核](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_lower_band_external_theorems_audit_20260915.md)：Morris／Serre引用的准确强度及适用局部化环。
- [九偏移共同完成](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)：大载体形状、真实标量反射和方向／单位尺度分工。

## 本次补读对后续路线的具体影响

四平均九元第6节早已证明，对任意偶数元数q，
\[
T_j=\begin{pmatrix}-(q+1)&j\\-(2q+1)&2j\end{pmatrix},
\qquad (T_{q/2}\Sigma)^2=-(q/2)I.
\]
后续若研究偶数元数的2q+1端点，应从这个已有正向种子继续，不能再把“找一个可逆种子”列作未开展任务。该公式本身仍未证明全部根、单位尺度和终端覆盖。

六平均九元的固定四步网络，以及更一般q=m(m-1)、n=m²网络，属于另一条已经明确的原位置构造路线。它们研究自动G维数；平方元数q=t²、n=t²+t+1的三块控制器则研究非自动临界点，二者参数关系不同。

## 后续调查的记录方式

三项主任务执行期间，本轮直接复核平方控制器、旧八平均十三元、统一端点控制器、四平均九元、素数最终独立审核、奇余量核心全文、无条件入口、两轮修复和短筛。新写并运行四项精确核验，分别对应2／3奇次幂、全部偶元数端点、十平均十六元网络、奇合数奇余量区间。没有继续GRH无条件化。结果与剩余见[本轮状态](../sources/work/document_reorganization_20260915/originals/outputs/general_k_three_tasks_progress_20260915.md)。

评估去掉GRH的可能性时，本次复核Pollack作者原文第2.3节／定理2.7、H_t文献报告的无条件与有效界部分、平方核心第5至6节。只做已知定理的范围和路线评估，未开展新的外部检索或扩大数值检查。分析已补入[GRH阶段文稿第7节](../sources/work/document_reorganization_20260915/originals/outputs/general_k_grh_stage_and_remaining_tasks_20260915.md)。

用户决定先依赖GRH后，本次直接回读H_t文献报告第6至9节、Gamma1尺度复核、原规划的素数幂／混合元数／接续部分和旧下界。已将[条件性定理与剩余任务](../sources/work/document_reorganization_20260915/originals/outputs/general_k_grh_stage_and_remaining_tasks_20260915.md)写出；没有开展新的文献检索或重复运行未修改的核验程序。

H_t文献调查本次直接取得并阅读相关段落的外部PDF为：Pollack2017《Bounds for the first several prime character nonresidues》（第1–4、8页及参考文献）、Martin–Pollack2013《The average least character non-residue…》（印刷22–25页）、2025《Explicit Burgess inequalities for cubefree moduli》作者预印本（主定理、条件和参考文献，关键第2页图像）。Norton1998、Harman1999、Bach1990/1993等仅题录或经上述原文明确引用，访问边界另记。详见[调查报告](../sources/work/document_reorganization_20260915/originals/outputs/ht_literature_and_eventual_square_completion_20260915.md)及[来源索引](../sources/work/document_reorganization_20260915/originals/work/ht_literature_20260915/source_index.md)。新增精确计算只验证t<1000的有限阿贝尔商和假设边界；不搜索平均词。

评议建议文稿时，直接阅读了general_k_plan_review_and_square_entry_20260915.md全文及其独立脚本，并对照三单点交换子第2至4节、Gamma1生成第4节和平方控制器的倍率／终端。重跑独立脚本，10条入口、404个原子及199个有限H_t诊断均通过；入口一般量词按正文核对，H_t仍未全称证明。本次未开展新的外部特征和文献检索。结论见[建议复核](../sources/work/document_reorganization_20260915/originals/outputs/general_k_review_response_20260915.md)。

本次一般k证明规划直接复核了平方核心全文、临界尺度第2至5节、策略文稿第4至8节及任意元数上界第1节，并核对本阅读记录中的旧偶数种子。规划时补出了全t平方核心的新交换子，重跑对应精确核验；没有重跑其他旧证明。任务顺序与新推论见[一般k证明计划](../sources/work/document_reorganization_20260915/originals/outputs/general_k_averaging_proof_plan_20260915.md)。

用户要求：调查时主动说明实际读了哪些文档。今后每次报告列出文档名及关键章节，明确标记“直接读正文”“只读摘要／索引”“间接引用”“本次补读”；另行说明是否运行核验。不能用“相关材料都看过”替代具体来源清单。


## 素数证明整理补记（2026-09-15）

本轮回到素数主线，未推进合数GRH任务。直接阅读三份最终／专项审核、九偏移与多个区间附录的相关章节，整理为独立[素数入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/README.md)。具体篇名、章节和间接引用边界见[本轮阅读核验表](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/verification.md)。实际下载并阅读 Milne v1.31 的模曲线、Hecke对应、level结构及权二微分相关段落；Stein和MIT仅导航，Serre及Kani仍保留原有访问等级。

数学修改：将99组二进补充所需的倍率扩环并入九偏移§6；集中证明本原列模可用单位的精确同余轨道分类及共同终端提升定理。这是对已有纤维接口的统一整理，并非新发现此前未有的原则。没有宣布消去有限证书或新的多项式词长。两个旧README同目录归档，24篇关键附录加当前状态提示；本轮重跑范围和运行输出见上述核验表。

<!-- END SOURCE doc-e41152995bbd -->

---

<a id="doc-1d066819e7ff"></a>

## 原文导签：历史路线账本（2026-09-15归档）

来源：`work/document_reorganization_20260915/originals/outputs/research_routes_history_20260915.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/research_routes_history_20260915.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-1d066819e7ff -->
# 历史路线账本（2026-09-15归档）

> 本文保留旧索引和 E／H／I 路线表。当前证明以[素数入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/README.md)为准；旧范围记录用于理解方法边界，不表示当前定理仍有缺口。

---

# 三平均与任意元数：当前状态和路线台账

更新：2026-09-15。**素数元平均的最优最终阈值已完成：每个奇素数 p 都有 N(p)=2p+1；N(2)=4。**

**三项主任务继续推进：** [本轮完成与剩余](../sources/work/document_reorganization_20260915/originals/outputs/general_k_three_tasks_progress_20260915.md)汇总四项完整结果：GRH下全部2、3的幂达到最早临界点；任意k的2k+1端点全部完成；十平均十六元有统一六步网络，M(10)=16；任意奇素数幂k的全部奇数2k<n<3k已完成。p>=5高奇次幂、一般混合临界点及其余维数接续仍开放；三项完成前不再研究去掉GRH。

**当前按用户选择在GRH下推进一般k。** [已完成范围与剩余三项任务](../sources/work/document_reorganization_20260915/originals/outputs/general_k_grh_stage_and_remaining_tasks_20260915.md)：全部t>=2的t²平均在t²+t+1元有完整G=1判据；对t=p^a，得到M(p^(2a))=H(p^(2a))=p^(2a)+p^a+1。H_t在当前条件性主线已关闭。一般素数奇次幂、混合元数临界点及临界后的全区间接续仍需证明，未宣布N(k)=B(k)。以下无条件H_t讨论保留为独立后续。

**H_t文献已给实质推进：** [小生成元调查与平方族充分大完成](../sources/work/document_reorganization_20260915/originals/outputs/ht_literature_and_eventual_square_completion_20260915.md)从Pollack2017定理1.1／2.7严格推出所有充分大的t均有H_t满群；素数模数n=t²+t+1由抽屉原理对全部参数完成。新有限阿贝尔商证书覆盖2<=t<1000，结合已发表Bach界的明确引用还得到GRH下全t成立。无条件全t尚缺数值界或剩余复合模数的统一证明；这些结果只完成相应平方族维数，不证明最终N(t²)。

**一般k平均执行计划：** [证明任务与验收条件](../sources/work/document_reorganization_20260915/originals/outputs/general_k_averaging_proof_plan_20260915.md)已采纳[建议文稿](../sources/work/document_reorganization_20260915/originals/outputs/general_k_plan_review_and_square_entry_20260915.md)：所有t的平方核心完整根和全输入入口均已具备，当前优先证明小整数生成的尺度群H_t满群。[复核记录](../sources/work/document_reorganization_20260915/originals/outputs/general_k_review_response_20260915.md)确认入口和一步终端限制，并补上一般k双块的精确G公式。H_t全称命题、全平方族临界结论及最终阈值仍未证明。

**策略梳理及合数新进展：** [素数证明主线与合数前沿](../sources/work/document_reorganization_20260915/originals/outputs/averaging_proof_strategy_and_composite_frontier_20260915.md)解释八个证明环节、已有S(q)临界猜想及其真正困难，并新增素数因子“块均值模拟”定理，覆盖全部q平均的n=kq、k>=3。[平方元数统一控制器](../sources/work/document_reorganization_20260915/originals/outputs/square_arity_uniform_controller_and_nine_thirteen.md)从四平均七元的宏直接推出参数周期，完整解决九平均十三元，得到M(9)=H(9)=13；未证明N(9)=13或全部合数最优阈值。

对全部 n>=2p+1，非全等有理输入经有限次原位置 p 平均可达全等，当且仅当中心化、清分母、本原化后的差分 gcd 为 p 幂。p 不整除 n 时才可简写为 G=1。n=2p 的一般反例保证奇素数阈值最优。

## 1. 当前证明的阅读顺序

本次合数调查实际读过的文档、章节及补读时间见[阅读记录](../sources/work/document_reorganization_20260915/originals/outputs/research_reading_log_20260915.md)。后续调查须主动列出直接阅读、间接引用和未核验内容。

1. [九偏移的共同完成](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)：最新关键步骤。将 (2p,p,s) 改成 (p,p,p+s)，统一解决全部3p+s、1<=s<=9。大p有闭式计数；小p由同一接口的522组完整有限参数证书和两项局部补充接续。
2. [最后复核记录](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_nine_offsets_completion_audit.md)：原位置、逆、局部化、换基、辅助13、二进单位、精确终端，以及本次草稿纠错的准确边界。
3. [全部2p+2及下半带汇合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_two_p_plus_two_uniform.md)、[全部3p-1](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_minus_one_completion.md)：与无条件入口、奇余量及内部偶余量合并，完成全部2p<n<=3p。
4. [所有素数的3p+10以上](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_all_prime_three_p_plus_ten.md)、[全部4p以上尾部](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_four_p_tail_completion.md)：旧d_p条件遗留的上方间隙已覆盖。
5. [2p反例](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_linear_threshold.md)：提供最优阈值的下界。[外部定理审核](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_lower_band_external_theorems_audit_20260915.md)给Morris/Serre的准确引用及访问边界。

上述是存在性证明，仍不提供对可变p、n的多项式平均词长、最短路径或实用的一般群词提取。一般合数平均元数的最优阈值仍未完成。

## 2. 当前结论与计算证据

| 对象 | 当前完整结论 | 证据与阅读入口 |
|---|---|---|
| 奇素数p | N(p)=2p+1，所有后续维数均有p幂G充要判据 | [新完成证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)及其列明的既有区间 |
| 二平均 | N(2)=4；首个非自动G边缘H(2)=5 | [定义与二平均](../sources/work/document_reorganization_20260915/originals/outputs/averaging_global_status_20260912.md) |
| 三平均 | N(3)=7，另有不依赖一般算术群路线的直接证明 | [任意维数直接证明](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_all_dimensions_double_triple_invariant.md) |
| 九平均 | 十三元完整G=1判据，M(9)=H(9)=13；最终N(9)仍未确定 | [平方元数周期与九平均证明](../sources/work/document_reorganization_20260915/originals/outputs/square_arity_uniform_controller_and_nine_thirteen.md) |
| 2、3的全部幂，GRH下 | 每个元数的最早临界维数已达到；最终N尚未统一确定 | [奇次幂与共同ms²控制器](../sources/work/document_reorganization_20260915/originals/outputs/two_three_odd_power_critical_grh_completion.md) |
| 任意整数k>=2 | 全部2k+1元端点的G=1判据 | [偶元数补齐](../sources/work/document_reorganization_20260915/originals/outputs/even_arity_all_endpoints_completion.md) |
| 奇素数幂k | 全部奇数2k<n<3k的完整判据，包括gcd(k,n)>1 | [奇合数区间与因子转译](../sources/work/document_reorganization_20260915/originals/outputs/odd_composite_coprime_middle_band_completion.md) |
| 十平均 | 十六元固定六步网络，M(10)=16；H(10)=17；N仍未定 | [三块固定网络](../sources/work/document_reorganization_20260915/originals/outputs/ten_average_sixteen_and_dyadic_network_family.md) |
| 全部平方元数，GRH下 | 每个k=t²在n=t²+t+1完整成立；素数偶次幂达到M和H的下界 | [条件性定理及量词](../sources/work/document_reorganization_20260915/originals/outputs/general_k_grh_stage_and_remaining_tasks_20260915.md) |
| 任意q的倍数维数 | 所有n=kq、k>=3具有完整“G的素因子均整除q”判据；另有更一般素数因子转译 | [策略文稿第5、6节](../sources/work/document_reorganization_20260915/originals/outputs/averaging_proof_strategy_and_composite_frontier_20260915.md) |
| 任意整数元数q>=3 | 既有n>=4q-1+d_q(n)时，rad(G)|q为充要条件；一般最优阈值仍开放 | [任意元数上界](../sources/work/document_reorganization_20260915/originals/outputs/arbitrary_arity_linear_threshold.md) |
| 困难输入与算法评测 | 旧有限路径、冻结态及算法测试集仍有用；不可把搜索失败写成不可达 | [算法测试集](../sources/work/document_reorganization_20260915/originals/outputs/averaging_algorithm_benchmark.md) |

新核验ID：`nine-offsets-large-symmetric-carrier`。

- [完整小参数证书](../work/large_symmetric_carrier_small_certificate.json)覆盖全部522组参数，核对2206条根反射计数及相应入口、方向、单位接口。
- [独立核验器](../work/check_large_symmetric_carrier_certificate.py)不导入候选生成器；一般无限量词由正文证明承担。
- [清单](../sources/work/document_reorganization_20260915/originals/work/verification_manifest.json)记录证据等级、外部依赖及不涵盖的算法问题。

**文档优先级：** 本页第1、2节是当前结论；下面第3至5节保留各方法当时做到的范围，用于防止重复研究。历史表内“仍缺”“尚未完成”不再表示素数p的可达性定理仍有缺口；其中限定的直接算法、固定宏或更强结构问题可能独立开放。

**符号注意：** 当前p表示平均元数，n表示位置数。许多旧triple_average_*文件的p表示三平均的位置数，两类问题不可混用。

## 3. 端点及跨维数：哪些已经研究过

编号用于检索和后续更新。“所需增量”指在已有成果和障碍之外，尚需新增的数学内容。

| 编号 / 路线 | 已有成果与失败的准确范围 | 再推进所需增量 | 必读 |
|---|---|---|---|
| E1 正向种子、根、核心轨道 | 统一资源已证；同日新证明用有限指数及强同余性质补齐任意合数核心，绕过短主元菜单 | 核心存在性任务已完成；可另研究可计算分解和长度界，不再重搜种子 | [同余闭合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)、[旧CRT证书](../sources/work/document_reorganization_20260915/originals/outputs/composite_endpoint_crt_transfer.md) |
| E2 直接划分与CRT入口 | 三单点交换子与模意义正向逆已补齐任意多素数入口；K4和单角色覆盖障碍被绕开 | 入口存在性已完成；可优化交换周期和实际词长 | [无条件入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unrestricted_endpoint_and_odd_band.md)、[旧六素因子](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_six_prime_endpoint_entry.md) |
| E3 反向找反例 | 整数冻结已分类为大背景加零和自由例外；若干族已有分数逃逸，七平均十五元已全解 | 真反例须排除分数路径；或在仍开放范围证明新逃逸族 | [反向诊断及纠正](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_counterexample_reverse.md) |
| E4 嵌入更大系统 | 已研究局部均值与相对尺度；射影逆嵌入后只收缩子块，外部不跟随 | 能处理外部总和及相对尺度的真实可重复构造 | [相对尺度](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_middle_band_relative_scale.md)、[局部几何第7节](../sources/work/document_reorganization_20260915/originals/outputs/prime_power_endpoint_and_critical_geometry.md) |
| E5 块—单点交换、改能量 | 交换自动保持非p同余；非整数交换本原平方高度不降；共同单调固定正定二次型唯一性已证 | 状态相关返回或离散高度；只换固定二次权重不够 | [精确增量与唯一性](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_energy_and_dyadic_neighbour.md) |
| E6 等值化、受限Euclid | 全部下半带入口完成，全部奇数维数全输入已解；双载体小分母有统一算法 | 一般偶数核内终止仍开放 | [无条件入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unrestricted_endpoint_and_odd_band.md)、[双载体复查](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_core_gap_reassessment_20260915.md) |
| E6d 双单点完整Euclid | p+1仅含2和至多一个奇素数时，最近奇数加一次除二修复给原位置严格下降；n=2p+2全输入完成 | 多个奇素因子可能相继阻断安全数字；p29仅排除该一轮下降规则，不是不可达反例 | [完整证明，第11节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md) |
| E6b 偶余量深同余与深度下降 | 内部偶余量有深主同余；全部偶数r含2、p-1现可用状态相关返回将v2(az)降到1，跨越旧对合不变量 | 深度一中的全部方向、奇素数和共同尺度的终端覆盖 | [一般深度下降](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)、[旧同余控制](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_middle_congruence_and_eighteen.md) |
| E6c 单对合边界的多宏取逆 | 七平均20、22的短标量闭路提供非迹零宏的正向逆；22元保留两个单位尺度类后联合轨道全覆盖，N(7)=15 | 一般p的相应闭路或其他可执行取逆机制；五平均12、14仍开放 | [七平均完整闭合](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_sharp_threshold_complete.md) |
| E7 相邻维数内插 | 一般内插原则为假；有不可直接调用的2p+1子块族及余维一障碍 | 核对局部仿射格、全局目标和原位置模拟的传播定理 | [维数传播](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_interpolation_and_lattice_structure.md) |
| E8 固定短词覆盖 | 固定长度原子词表不能覆盖全部临界合法方向 | 输入相关长度，加递归/除法规则及终止证明 | [前沿第4.5节](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_critical_frontier_handoff.md) |

**2026-09-14对话的去重说明：** 将外部总和写为S、把端点返回写成带S的仿射式，是E4的坐标表达，不构成新路线。更换单点、围绕局部均值分析收缩属于E4至E6已经尝试的内容。新增进展必须提供上述文档未有的可执行控制或终止论证。

## 4. 三平均历史算术路线

旧文的“最小未解71”“只差种子”是2026-09-11直接证明之前的状态。原三平均问题已通过另一条证明完成；指定宏的更强实现问题可以独立开放。

| 编号 / 路线 | 可保留内容 | 已知边界及入口 |
|---|---|---|
| H1 17至59、非分裂轨道 | 根提取、Schreier、终端；删点Reynolds层及字符公式 | 双载体全空间两层等角障碍有一般证明；其他短词未命中限于有限语法。[结构综合](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_nonsplit_prime_structure_synthesis.md)、[轨道](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_nonsplit_punctured_orbits.md) |
| H2 仿射交换子 | 导群参数是倍率局部化环上的显式理想，可统一计算本原性 | 需要实际可逆仿射元；非零根不等于本原根或全轨道覆盖。[交换子理想](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_affine_commutator_ideal.md) |
| H3 参数周期刚性 | 固定有理函数词的非恒等周期条件只命中有限多个参数 | 不排除符号恒等周期或随参数增长的词长。[周期刚性](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_parametric_cycle_rigidity.md) |
| H4 统一/双/混合迹零 | 混合双返回条件定理已补齐根理想与终端；先前单返回的过强充分性已纠正 | 指定返回原位置分解未证；正运输或副本实现不是原位置实现。[单目标](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_universal_trace_zero_target.md)、[双返回](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_two_trace_zero_returns.md)、[混合返回](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_mixed_singleton_controller.md) |
| H5 伴随、复制消去、数字层 | 全原子倒序可执行；适用域和二维强返回已有审计 | 压缩Gram相等不推出像不变；叶差收缩不带动局部均值。须检查W*WE=lambda E及账本。[原位置分解前沿](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_original_position_factorization_frontier.md) |
| H6 Hecke/Manin/模形式 | 有限Hecke关系、算术格及theta联系有准确内容 | 指定星结构、中心负号、单cusp商、分支之和存在障碍。暂停的是旧直接接入方案。[最终审计](../sources/work/document_reorganization_20260915/originals/outputs/triple_average_final_hecke_audit.md)、[theta联系](../sources/work/document_reorganization_20260915/originals/outputs/prime_power_endpoint_and_critical_geometry.md) |
| H7 合数归约与高斯周期 | 三平均旧合数归约有效；一般p能推广部分范数周期 | 临界小商未必可解，旧剪切恒等式不能直接替换p。[重新评估](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_revisiting_ternary_factor_gaussian_route.md) |

重新借用H6需要明确的数学空间、作用、映射及真实分支提升，不能只改称“覆盖”“饱和”或“gallery”。H2、H3仍是可用代数工具，不应一并归入“群论失败”。

## 5. 上半带与近期不变量改进

| 编号 / 路线 | 目前做到哪里 | 尚未解决或已排除的内容 | 入口 |
|---|---|---|---|
| I1 固定核心返回降能 | 全输入核心入口已证；七平均22元十个不交核心返回已审计 | 该输入没有这种合法降能返回，却有两步重叠造零；只排除该菜单 | [核心陷阱](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_remaining_gap.md) |
| I1b 四返回算术控制 | 两种载体各取相邻参数，显式得到U(rn²R)、L(rn²R)及Gamma(r²n⁴,R)；p>=13的3p+10至4p-3容量统一成立；I1d已补齐完整终止 | 3p+1无本菜单四返回，两端低容量仍须新工具 | [四返回迁移](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_four_return_congruence.md) |
| I1c 主同余升级与二三单位下降 | 旧与6互素完整族及Smith-CRT逆继续有效；gcd(n,6)限制现由I1d删除 | 旧n/11小代表不是一般局部类型所必需 | [旧完整族证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_coprime_six_complete.md) |
| I1d 深层取逆与全局单位像 | 整个3p+10至4p-3全输入完成；去除r辅助素数，真实返回数字生成全部单位像，2、3及其他素数同时完成方向与尺度 | 3p小余量；4p下方两条边界由I1e在p>=37完成，上方由I1f完成 | [无条件上半带](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_unrestricted_completion.md) |
| I1e 一次重叠替换载体 | p>=37的4p-2、4p-1全输入完成；新矩阵对m统一，根无r因子，辅助p由局部SL2消去，单位平移无m+1因子 | 容量仍约要求r>p/m；上方低余量现由I1f的大载体处理，不再重搜上端B载体种子 | [重叠返回与完整证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_overlap_completion.md) |
| I1f 双份新载体与尾部密度 | n=4p+s的旧遗漏强制d>=s+3，保证p>=16s+21和单位计数；全输入进入(2p,p,p+s)，五步对合根gcd仅gcd(n,5)，完整关闭全部尾部 | 不解决一般3p小余量，不给多项式词长；不应再把761/3045列为未解接续 | [尾部及3p+10阈值](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_four_p_tail_completion.md) |
| I1g 容量与仿射行列式接口 | 八组较小p以单位密度替代大p小代表；三个单A边界用两种重叠族及两轮局部提升完成。N(p)<=3p+10现对所有素数成立 | p=11的34至42仍属于一般低余量；有限参数核验不等于有限高度输入验证 | [全部素数统一阈值](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_all_prime_three_p_plus_ten.md) |
| I1h (3p-1) 重叠反射 | 所有p>=7统一得到双向2n根、全部单位尺度和精确终端；p=5以夹乘处理，N(5)=11 | 2p+2已由I1i完成；上方低余量仍须继续 | [统一3p-1证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_minus_one_completion.md) |
| I1i (2p+2) 状态相关CRT终端 | 正确三步重叠反射给 Gamma(h²,Z[1/p])；一次 Mp 和一次 Mq 直接安排 v=+-1 mod h²，所有素因子统一处理 | 上方九个低余量的初始返回资源仍不足 | [统一2p+2证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_two_p_plus_two_uniform.md) |
| I1j 小载体逆与可解商分离 | p=1模3有固定四原子收缩逆；p=4模9的3p+1全输入完成。完美局部群分离统一删除辅助素数 | 其他p的同余分支及s=2至9尚未完成；模双曲线只给可逆返回，不自动给根 | [新完整族](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_plus_one_residue_four.md)、[统一反射接口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_low_offset_unified_frontier.md) |
| I1k 载体打包与三点轨道 | s=mb、m<=3提供标准收缩的真实逆；m=1、2与反向仿射接成nR根，完整解决偏移2、4、8和更一般偶余量区间 | n含2或3时不能直接反演危险素数；剩余s=1,3,5,6,7,9 | [共同控制器](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_low_offsets_common_controller.md) |
| I1l 三进相位与条件数字返回 | U(3R)及一个横向反射给明确深层，至多一次模3相位调整、两个CRT返回送到精确终端，完成偏移3/6的指定p类；短筛选另完成偏移9的p=1模3 | 高三进相反类仍缺无条件起步与闭合；第12节只有条件原位置消去，不是全解 | [三进共同证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_triadic_packed_carrier_completion.md) |
| I2 来源关系 | 指定出口后第二次安全整数续步已证；r>=2保留额外四值关系 | r=1来源式退化为当前零和式；任意安全后继都可继续为假 | [来源与动态阶段](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_provenance_dynamic_and_integer_stages.md) |
| I3 动态保护 | 指定后继危险支持完全重合，至多保护一处，由gcd(3alpha-2,n)确定 | 不是任意多值状态都如此；固定某个极小保护集可能错过有效操作 | [动态阶段](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_provenance_dynamic_and_integer_stages.md)、[保护交换](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_protected_exchange_and_mass.md) |
| I4 单位见证补回 | Hilbert基、容量、Euclid转移、重叠覆盖全部规定单位碰撞入口；旧十个缺口含p983已补齐 | 多值输出未证递归重入；重值对下移不自动降低全局最大值 | [完整补回](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_complete_unit_collision_recovery.md)、[转移](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_euclidean_witness_transfer.md)、[容量](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unit_witness_replenishment.md) |
| I5 弱重数不变量 | S_p>=2p-1+h给一步安全条件；规定维数下停滞态有单背景结构 | (p,p-1)、单独S_p>=2p-1有任意大维数停滞族；相邻双重值不能普适单步保持 | [锐边界](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_sharp_repetition_and_precision_barriers.md)、[单位对障碍](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unit_witness_replenishment.md) |
| I6 非二次势、约分 | 整数阶段能量/两两距离下降；部分分支最大值下降；模q全零后有合法约分实例 | 固定原A,C的分数阶段排除公因子约分，并阻止指定高度下降；未排除一切非二次势 | [势的范围](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_invariant_improvements_and_core_exit.md)、[约分障碍](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_provenance_dynamic_and_integer_stages.md) |
| I7 整数返回、精度 | 奇素数首次离格到返回同格至少五步；一类输入恰需一位额外精度 | 安全、实能量下降、当前一位精度不足以维持下一步同格；坏前缀会冻结 | [精度边界](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_sharp_repetition_and_precision_barriers.md) |
| I8 五步参数消去 | 精确记录显示多值来源可消去并恢复固定形状；p3有参数收缩对照 | p>=5指定规则可使归一化参数增长。尚无正式证明文档及清单登记，不能按脚本标题认定一般非终止定理 | [记录](../work/parameter_erasure_recurrence_records.json)、[程序](../work/verify_parameter_erasure_recurrence.py) |
| I9 逆零和与组合选择 | 尖锐两桶界、极端冻结族逃逸、高重/分散余类及部分碰撞分支 | 中等重数多余类交互未闭合；模零筛选后的选组一般不是拟阵基 | [集中与逃逸](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_sharp_concentration_and_escape.md)、[加法接口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_three_p_additive_interface.md) |
| I10 不同实际值归约 | D>=d+2k-1时有安全整数操作，有限降至D<=d+2k-2 | 是前处理；较大n仍可只有三种值而冻结 | [不同值数](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_distinct_value_integer_reduction.md) |

I8记录范围：209个五原子消去实例、140个来源方向检查、六个素数各20轮递推、8个三平均收缩实例，以及p983补回输出接入。这些检验规定构造，不证明任意合法后继递归归零。本次没有重新运行或扩大实验。

## 6. 后续研究先说明新增了什么

素数元平均的阈值任务已由大载体共同证明完成。下表是可继续研究的直接算法和结构问题，不再是证明N(p)=2p+1所必需的缺口。

| 任务 | 可复用起点 | 应证明的新增内容 |
|---|---|---|
| 停滞态分数逃逸 | E3、I5、I7、I9 | 完整参数族的安全出口及有限返回/零触发；不重复已有极端族 |
| 迁移见证与合法约分 | I3、I6 | 实际操作同时控制非p合法性、公因子、分母，而非仅写净高度条件 |
| 多值后继递归选择 | I2、I4、I8 | 出口仍可处理，每个非终端有允许选择及离散下降；正反例均登记 |
| 端点/中间带控制 | E1核心已闭合，E2入口及E4至E6仍部分开放 | 处理更多素因子入口，或外部质量的原位置构造；再次写出仿射矩阵不够 |

后续优先级为：整理完整论文及其依赖链；优化实际词提取和长度界；研究任意合数平均元数的最优阈值。I8及平方能量支线的限定性障碍仍保留，但不应再次将它们列为素数元平均存在性证明的前置任务。

## 7. 检索、证据与维护

文献入口：[2018至2026综述](../sources/work/document_reorganization_20260915/originals/outputs/averaging_literature_survey_2018_2026.md)、[策略与全文边界](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_strategy_reassessment_20260912.md)、[零和文献核对](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_shape_potential_literature_interface.md)。逆EGZ、零和自由序列、受限和集、群标记组合选择、受限切换与多Lyapunov函数、S整数环初等生成均已有查阅；查阅过不等于已建立本题接口。

新尝试前按数学特征检索，不仅搜索拟起的新标题：

    rg -n "相对尺度|局部均值|单点.*交换|等值化" outputs
    rg -n "冻结|停滞|精度|约分|本原.*高度" outputs
    rg -n "非分裂|交换子|迹零|周期刚性|Hecke|Manin" outputs

新增记录注明：适用元数/维数、原位置操作、对应哪条路线、增加了什么、仍缺什么。反例须说明只针对整数路径、某个宏菜单还是固定不变量；有限阴性诊断记录语法与范围。固定维数成功、合法入口、核内轨道、全部后续维数是四种不同结论。

核验等级以清单为准：theorem-certificate闭合明确的有限证书子问题；symbolic-check核对精确公式；finite-sanity是有限实例；exploratory-search是有限搜索。任何等级都不能超出正文量词。新增计算结论应补专题证明与清单，纯导航维护无需重跑整个研究库。

主研究目录是本文件的上级目录。2026-09-10/new-chat/outputs及聊天根目录存在历史副本，不能凭同名认定同步。本次不移动旧文件；之后更新主目录正文和本索引，避免增加同名内容副本。

## 8. 已过期状态速查

- “九偏移尚未统一／N(p)<=3p+10”：已由大载体共同证明取代，奇素数N(p)=2p+1。
- “下半带偶数或2p+2、3p-1仍开放”：均已全输入完成。
- “4p以上还有d_p缺口”：已由尾部证明完整接续。

- “三平均最小未解71 / 必须补统一种子”：已由任意维数直接证明取代；指定宏问题单独保留。
- “七平均十五元未解”：已由两素数入口和Gamma_0(15)完整覆盖解决。
- “p97 / n195缺入口”：已由四素因子入口补齐；早期28全输入/8核心只是当时证据分工。
- “单位补回还缺十个入口，含p983”：已全覆盖；多值递归仍未闭合。
- “非p保护总要留d处”：只是通用预算；特定交换自动安全，指定核心后继至多一处。
- “统一迹零返回就足以完成根与轨道”：早期表述过强，以混合双返回的条件定理为准。
- “解完3p<n<4p便自动有N(p)<=3p”：还须检查4p以上旧上界遗漏维数，如p761、n3045。
- “任意合数端点核心仍缺群包含”：2026-09-14同余闭合证明已补齐，依赖Morris 2007定理6.1(2)与Serre强同余子群性质；全输入入口仍另计。
- “五平均十三元只完成入口”：同日后续已接两个旧对合与主同余控制，完整G=1判据成立；十二、十四元仍未证。
- “一般奇数r只知道一个对合”：3<=r<p时始终有两个指定对合，现已接成完整核心定理；七平均17、19元完成，剩18、20、22元。

<!-- END SOURCE doc-1d066819e7ff -->

---

<a id="doc-a4ff935be716"></a>

## 原文导签：七平均十五元完整G判据：两素数入口与二进 \(\Gamma_0(15)\) 覆盖

来源：`work/document_reorganization_20260915/originals/outputs/seven_average_fifteen_complete.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_fifteen_complete.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-a4ff935be716 -->
# 七平均十五元完整G判据：两素数入口与二进 \(\Gamma_0(15)\) 覆盖

日期：2026-09-12。按用户要求，研究目标是平均元数继续增大后的首个非自动G维数，停止六平均十一元支线，转而完成七平均十五元。

**同日推广：** [合数端点CRT证书](../sources/work/document_reorganization_20260915/originals/outputs/composite_endpoint_crt_transfer.md)将本页方法统一用于36个列明模数；28个两素数模数得到全输入G=1判据，另外8个只完成合法核心覆盖。下面的入口引理本身对任意两素数指数都有效；新的有限证书没有证明任意合数level的群包含。

## 1. 主定理与严格范围

对十五个有理数，中心化、清分母、本原化为非零整数零和 \(X\)，令
\[
G(X)=\gcd_{i<j}|X_i-X_j|.
\]
则
\[
\boxed{
X\text{ 可有限步七平均归零}
\iff G(X)=1.
}
\tag{1}
\]
全等输入单独允许空词。

本原十五元状态总有 \(G\mid15\)，所以G的可能值为1、3、5、15；其中只有1是7的幂。因此 (1) 正是原来的“G的素因子只能整除平均元数”充要条件，而不是改过的判据。

结合[临界尺度反例](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md)排除全部 \(7<n<15\)，得到
\[
\boxed{H(7)=M(7)=15.}
\tag{2}
\]
H表示G确实筛选输入的最早成功维数；M表示排除平凡 \(n=p\) 后的最早成功维数。这里15的G不是自动合法。

**尚不能宣布 \(N(7)=15\)。** N要求之后所有维数都成立。结合已证十六元、二十一元及全部 \(n\ge23\)，七平均仍待证明G充分性的维数为
\[
17,\ 18,\ 19,\ 20,\ 22.
\]
最终阈值仍为 \(15\le N(7)\le23\)。本页的完备结论只针对十五元和下面明确给出的入口引理。

## 2. 本次补上的两个环节

[统一端点控制器](../sources/work/document_reorganization_20260915/originals/outputs/uniform_endpoint_positive_controller.md)早已在
\[
K_p(a,b)=(a^p,b^p,-p(a+b))
\]
上给出真实正向根和单位。十五元剩下的两个问题是：

1. 任意合法输入是否能同时保住模3、模5见证进入 \(K_7\)；
2. 两种不同素因子产生的额外陪集，是否也能用现有根编译。

本页分别解决它们。没有重新搜索种子或短平均词；已有小高度35714个样本的成功证书不承担本页的无界量词。

## 3. 一般的两素数入口引理

**引理。** 设 \(p\ge3\)，\(n=2p+1\)，且n至多有两个不同素因子。任意本原整数零和 \(G=1\) 输入，至多三次真实p平均便可进入合法
\[
(a^p,b^p,-p(a+b)).
\tag{3}
\]
这里甚至不需要p为奇素数；这里只证明入口，不把核内控制器的奇数适用域一同扩大。

### 第一次平均保留两处不同余见证

对每个素数 \(\ell\mid n\)，选择一对模 \(\ell\) 不同的位置。两对的并集至多有四个位置。因 \(2p+1-4\ge p\)，可以选择一个p元组避开它们，平均得到p份a。余下p+1个单点在每个 \(\ell\) 下仍不全相同，因此这一步安全。

在每个 \(\ell\) 下，至少有一个单点c满足 \(c-a\ne0\pmod\ell\)。

若存在同一个单点w对所有 \(\ell\mid n\) 均满足
\[
w-a\not\equiv0\pmod\ell,
\]
就保留w，把其他p个单点平均为b。全局零和给
\[
a-b=\frac{2pa+w}{p}\equiv\frac{w-a}{p}\pmod\ell,
\tag{4}
\]
其中 \(2p\equiv-1\pmod\ell\)、\(\gcd(p,n)=1\)。故输出两块差同时为各局部单位，进入合法核心。总共两步。

### 没有同时见证时，只需一次块—单点交换

设两素数为 \(\ell_1,\ell_2\)，且没有单点差同时在两处非零。由于每处都有见证，必有两个单点c、d，其相对块值a的差分满足
\[
\begin{array}{c|cc}
 &\ell_1&\ell_2\\ \hline
c-a&0&\ne0\\
d-a&\ne0&0
\end{array}.
\tag{5}
\]
执行一次p平均 \((a^{p-1},c)\)，留下原a的一份作为新单点，新p重值为
\[
a'=a+\frac{c-a}{p}.
\]
未参与的d满足
\[
d-a'=(d-a)-\frac{c-a}{p}.
\tag{6}
\]
在 \(\ell_1\) 下第一项非零、第二项为零；在 \(\ell_2\) 下第一项为零、第二项非零。因此 \(d-a'\) 同时为两处单位。

这次交换自动安全：在块参数 \((a,c)\) 上矩阵为
\[
T=\begin{pmatrix}(p-1)/p&1/p\\1&0\end{pmatrix},
\quad
T^{-1}=\begin{pmatrix}0&1\\p&-(p-1)\end{pmatrix}.
\]
二者均固定常值方向，并在所有 \(\ell\nmid p\) 处整可逆；输出全同余当且仅当输入全同余。形式逆仅用于证明安全性，不执行反向平均。

现在保留d，平均其他p个单点，再由 (4) 完成合法入口。总共三步。

该证明把两个不同局部见证通过一次真实交换合并，不枚举全部联合余数。对于三个或更多危险素数，互补类型 (5) 不再自动存在，本页没有做此推广。

## 4. 十五元入口及合法核心

令p=7，危险素数恰为3、5。第3节给出至多三步入口。用
\[
(x,y)=(a,a-b)
\]
作为核心参数；清分母并本原化后，
\[
G(K_7)=\gcd(y,15).
\tag{7}
\]
因为单点与a的差为 \(-8a-7b=-15a+7y\)，且 \(\gcd(a,b)=1\)。所以合法参数域为
\[
\gcd(x,y)=1,\qquad \gcd(y,15)=1.
\tag{8}
\]

## 5. 已有的正向资源：本页只用二进部分

[统一端点控制器](../sources/work/document_reorganization_20260915/originals/outputs/uniform_endpoint_positive_controller.md)对任意奇数p给出
\[
U(R_n),\quad L(nR_n),\quad \Delta(R_n^\times),
\qquad
R_n=\mathbb Z[1/\ell:\ell\le p\text{ 为素数且 }\ell\nmid n].
\]
这些及其逆都有明确的正向平均词，允许非零全局共同尺度。

对p=7、n=15，\(R_{15}=\mathbb Z[1/14]\)。本页实际只需要更小的资源
\[
\boxed{
U(R),\quad L(15R),\quad\Delta(R^\times),
\qquad R=\mathbb Z[1/2].
}
\tag{9}
\]
无需为倍率7使用欧拉大幂，也不需要制造倍率11、17的逆。

底层宏是已有的两次七平均返回：
\[
T_j/7,\qquad
T_j=\begin{pmatrix}-8&j\\-15&2j\end{pmatrix},
\]
以及保留单点的两组混合
\[
F_r=\begin{pmatrix}1&(r-7)/14\\0&r/7\end{pmatrix}.
\]
p=7的已证种子只用 \(T_1,T_2,T_4,F_{-1},F_1\) 和等大七重块的标签交换。核验器会将每个实际宏在两个基参数上独立重放；绝不把R中的2进除法直接当成物理平均元数。所有真实数值分母仍来自7。

## 6. 模15有24个陪集，不是16个

中国剩余定理给出
\[
\mathbf P^1(\mathbb Z/15\mathbb Z)
\cong\mathbf P^1(\mathbb F_3)\times\mathbf P^1(\mathbb F_5),
\]
所以共有 \(4\cdot6=24\) 个标签。

取整数行列式一代表：
\[
A_j=\begin{pmatrix}0&-1\\1&j\end{pmatrix},
\quad -7\le j\le7;
\]
\[
B_t=\begin{pmatrix}1&0\\t&1\end{pmatrix},
\quad t\in\{-6,-5,-3,0,3,5,6\};
\]
\[
C=\begin{pmatrix}-1&-2\\3&5\end{pmatrix},
\qquad
D=\begin{pmatrix}2&1\\5&3\end{pmatrix}.
\tag{10}
\]
A图覆盖第一坐标在模3、5下均为单位的15个标签；B图覆盖第二坐标为单位、第一坐标至少一处非单位的7个标签。C、D分别补上第一、第二坐标在两处互为非单位的两个剩余标签。

核验器以CRT局部标签独立区分24个陪集，并核对全部192个本原模15行，每个标签对应8个单位倍数。这里C、D只是群论证明用的代表，不是额外物理操作。

## 7. 全部72条回路只需要二进主元

令
\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad T=U(1).
\]
对每个代表Q及 \(g\in\{S,T,T^{-1}\}\)，按底行的CRT标签选择下一代表Q'，回路
\[
H=Qg(Q')^{-1}
\tag{11}
\]
左下项必为15的倍数。

全部72条回路中：

- 62条的左上项已经是 \(\pm1,\pm2,\pm4,\pm8\)，用通常Gauss分解；
- 8条改用右下主元，右下项为 \(\pm2\) 或8；
- 最后2条用一次二进上剪切调整主元。

后二类回路的完整表如下，足以逐项复核新加的分支：

| 起点及生成元 | 回路矩阵 | 处理 |
|---|---|---|
| \(A_{-2}S\) | \(\begin{pmatrix}7&-1\\15&-2\end{pmatrix}\) | 右下主元 \(-2\) |
| \(A_2S\) | \(\begin{pmatrix}-7&-1\\15&2\end{pmatrix}\) | 右下主元2 |
| \(B_{-3}T\) | \(\begin{pmatrix}7&1\\-15&-2\end{pmatrix}\) | 右下主元 \(-2\) |
| \(B_3T^{-1}\) | \(\begin{pmatrix}7&-1\\15&-2\end{pmatrix}\) | 右下主元 \(-2\) |
| \(CS\) | \(\begin{pmatrix}-11&4\\30&-11\end{pmatrix}\) | 左乘 \(U(1/2)\) 后主元4 |
| \(CT\) | \(\begin{pmatrix}17&-3\\-45&8\end{pmatrix}\) | 右下主元8 |
| \(CT^{-1}\) | \(\begin{pmatrix}-7&-1\\15&2\end{pmatrix}\) | 右下主元2 |
| \(DS\) | \(\begin{pmatrix}11&4\\30&11\end{pmatrix}\) | 左乘 \(U(-1/2)\) 后主元 \(-4\) |
| \(DT\) | \(\begin{pmatrix}17&3\\45&8\end{pmatrix}\) | 右下主元8 |
| \(DT^{-1}\) | \(\begin{pmatrix}7&-1\\15&-2\end{pmatrix}\) | 右下主元 \(-2\) |

对 \(\det H=1\)，\(H=\begin{pmatrix}a&b\\c&d\end{pmatrix}\)，两种精确分解是
\[
H=L(c/a)\operatorname{diag}(a,a^{-1})U(b/a)
\quad(a\in R^\times),
\tag{12}
\]
\[
H=U(b/d)\operatorname{diag}(d^{-1},d)L(c/d)
\quad(d\in R^\times).
\tag{13}
\]
若采用上剪切，先分解 \(U(t)H\)，再左乘已实现的 \(U(-t)\)。c仍为15的倍数，所有下根参数仍在 \(15R\) 中。

所有主元处理均为有限精确公式。特别是主元11、17的出现，不意味着必须局部化11、17；它们只是某种消元顺序下的主元。

因此72条回路全部由 (9) 正向编译。标准Schreier生成定理给出
\[
\boxed{
\Gamma_0(15)\text{ 的全部射影作用都由真实正向七平均实现。}
}
\tag{14}
\]
这是无限整数群的包含，不是仅检查模15的群像；也不声称它恰好等于全部真实宏群。

## 8. 从全部合法方向到原位置终端

对本原合法参数 (8)，取
\[
\alpha x+\beta y=1.
\]
通过
\[
(\alpha,\beta)\mapsto(\alpha+ky,\beta-kx),
\qquad
k\equiv-\alpha y^{-1}\pmod {15},
\]
使 \(15\mid\alpha\)。于是
\[
H=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}\in\Gamma_0(15),
\qquad H(x,y)^T=(0,1)^T.
\tag{15}
\]
整数Euclid给出有限S、T、T逆词；第7节把每个回路编译成实际七平均宏。因此到达 \(K_7(0,b)\)。

最后四步：

1. 平均单点 \(-7b\) 与六个零，得到 \((b^7,(-b)^7,0)\)；
2. 取三份b、三份 \(-b\) 和一个零；
3. 再取三份b、三份 \(-b\) 和一个零；
4. 取最后一对相反值与五个零。

全部归零。每步都恰好七个不同原位置。入口、核内词与终端连接，证明(1)充分性。

必要性：若G=3、5或15，选择其中一个素因子 \(\ell\)；本原输入全模 \(\ell\) 同余且非零，七平均保持这一余类，所以不能归零。

## 9. 为什么这次突破不是重新扩大数值搜索

十五元的种子层在旧统一定理中已经完成。真正新增的是：

1. 一次块—单点交换把模3、模5的互补见证合并，完成一般输入入口；
2. CRT给出正确的24个标签，补全过去不能直接使用素数幂两图的地方；
3. 允许换Gauss主元或做一次已实现的剪切，把全部回路降到二进单位。

这说明“多素数端点”至少在两个素数入口上已有统一原位置机制。对于更多素数，见证类型可能无法两两互补；对于其他两素数level，所有回路是否也能用现有局部化单位分解，还需要证明。不能直接把本页换成任意15以外的模数。

已有[反例诊断报告](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_counterexample_reverse.md)里的七个整数冻结输入，必须使用分数才能逃离。本证明允许这种分数路径，并用群词的有限编译保证终止，没有错误地假设实能量下降就自动有限归零。

## 10. 核验入口与原始记录

~~~text
python work/run_verifications.py --id seven-average-fifteen-complete
~~~

[核验器](../work/verify_seven_average_fifteen_complete.py)检查：

- 全部192个本原模15行、24个CRT标签与72条Schreier回路；
- 62个左上、8个右下、2个上剪切主元分解全部编译为正向表达式；
- 已使用的底层宏在两个基参数上的10次真实原位置重放；
- 1800个两素数互补见证与安全交换公式检查；
- 160个96位随机合法输入的入口与Bezout；
- 72个专门构造、强制使用三步入口的输入，逐索引Fraction核对；
- 7条完整原始输入路径，其中包含整数冻结族 \(Z_7=(1^{12},-5,-4,-3)\) 和强制三步入口实例；
- G=3、5、15的三个非法例子。

输出：

~~~text
seven-average n15 complete CRT cosets and positive pivots: PASS 192 72 62 8 2 10
seven-average n15 two-prime entry logic and large inputs: PASS 1800 160 72
seven-average n15 literal full paths and excluded G: PASS 7 7746 3
seven-average fifteen-position full G criterion: PASS
~~~

[完整证书记录](../work/seven_average_fifteen_witnesses.json)保存1基原位置序列、72个特殊入口输入以及三类非法输入。最终验证只相信原输入与索引，不相信中间规范化的宏参数。

最长样本7746步是直接算术编译器的输出，不是最短界或总体复杂度上界。160个大整数输入只核验入口和输送矩阵，没有展开全部长词。本证明不提供一位额外精度界或统一多项式展开长度。

七平均十四元的反例与本页十五元充分性一起确定的是最早成功点H(7)=15；其他更高维数仍独立待证。用户取消的六平均十一元返回表保留为探索记录，本页不继续推进那条支线。

<!-- END SOURCE doc-a4ff935be716 -->

---

<a id="doc-c804878969e3"></a>

## 原文导签：七平均 (n=14) 与 (n=15) 对照实验

来源：`work/document_reorganization_20260915/originals/outputs/seven_average_n14_vs_n15_comparison.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_n14_vs_n15_comparison.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-c804878969e3 -->
# 七平均 (n=14) 与 (n=15) 对照实验

日期：2026-09-12。这里固定平均元数 (p=7)，比较相邻维数

\[
n=14=2p,
\qquad n=15=2p+1.
\]

目的不是只比较搜索速度，而是在相同坐标范围下比较完整整数状态图。对 (n=14\le2p)，已知成功路径不会产生新的七进分母，因此整数后继递归是精确可达性判定。对 (n=15)，本轮采用独立的“零触发”证书搜索；其有限枚举和随机证书结果见 [seven_average_n15_numerical_evidence.md](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_n15_numerical_evidence.md)。

## 完整整数枚举：(n=14)

候选条件为 (G=7^k)。程序保留实际整数尺度，只按排序和整体符号去重；每个非恒等后继严格降低平方能量。

| 坐标范围 | 候选状态 | 可解 | 不可解 | 不可解比例 |
|---|---:|---:|---:|---:|
| ([-1,1]) | 6 | 6 | 0 | 0 |
| ([-2,2]) | 72 | 69 | 3 | 4.167% |
| ([-3,3]) | 647 | 642 | 5 | 0.773% |
| ([-4,4]) | 4314 | 4289 | 25 | 0.580% |
| ([-5,5]) | 22536 | 22477 | 59 | 0.262% |

同样的 ([-4,4]) 范围下，(n=15) 的完整零触发枚举有 6231 个 (G=1) 状态，6231 个全部得到证书；(n=14) 则有 25 个精确不可达状态。这不是搜索深度截断造成的差异。

一个标准不可达族是

\[
(-7,0^6,1^7).
\]

它本原、零和、(G=1)，完整整数递归判定不可达，并且只有一个非恒等整数后继。它正是 (n=2p) 边界的结构性陷阱。(n=14) 的 ([-2,2])、([-3,3])、([-4,4]) 不可解样本也都呈现大重数块结构。

## 随机对照

原始坐标独立均匀取自指定区间，最后一个坐标补成零和，再中心化、本原化并筛选 (G=7^k)。(n=14) 的完整递归结果：

| 范围 | 接受样本 | 可解 | 不可解 | 平均最短步数 |
|---|---:|---:|---:|---:|
| ([-2,2]) | 100 | 100 | 0 | 2.00 |
| ([-5,5]) | 200 | 200 | 0 | 2.02 |
| ([-10,10]) | 200 | 200 | 0 | 2.04 |

随机样本没有命中不可解族，说明这些陷阱很稀疏；这不能推翻完整枚举发现的不可达状态。作为比较，(n=15) 在 ([-20,20])、([-100,100])、([-1000,1000]) 各 500 个样本也全部得到零触发证书，但 (n=15) 的证书路径最长 7 步，而 (n=14) 的随机可达样本通常只需 2--3 步。

## 结论

这组对照排除了“(n=15) 看起来更容易，只是因为数字范围更小或搜索方式不同”的解释：

- 使用同一 (p=7)、同一候选筛选和同一坐标范围，(n=14) 的完整状态图出现稳定的不可解比例；
- (n=15) 的相同范围完整枚举全部有证书；
- (n=14) 的不可解族与 (2p) 边界的重数结构一致，而不是由大整数溢出或浮点误差造成。

因此数值证据支持：(n=15=2p+1) 确实跨过了 (n=14=2p) 的结构性障碍。它仍不等于七平均十五元的无界充分性证明；后续缺口是证明任意 (G=1) 的十五元状态都能进入零触发接口，或建立独立的十五元正向控制器。

复现实验：

```text
python work/exact_seven_average_n14_ratio.py --exact-bounds 3 4 5 --random-bounds 2 --samples 1 --output work/seven_average_n14_exact_b3_b4_b5.json
python work/exact_seven_average_n14_ratio.py --exact-bounds 1 --random-bounds 5 10 --samples 200 --output work/seven_average_n14_random_b5_b10_200.json
python work/exact_seven_average_n15_bounded.py --bounds 1 2 3 4 --output work/exact_seven_average_n15_bounded.json
```

<!-- END SOURCE doc-c804878969e3 -->

---

<a id="doc-b26fccfa3c79"></a>

## 原文导签：七平均 (n=15) 数值证据

来源：`work/document_reorganization_20260915/originals/outputs/seven_average_n15_numerical_evidence.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_n15_numerical_evidence.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-b26fccfa3c79 -->
# 七平均 (n=15) 数值证据

日期：2026-09-12。这里每次选取 7 个位置，以其平均值替换这 7 个位置。由于

\[
n=15=2\cdot7+1
\]

且 (15) 不是素数，已有的“(2p+1) 为素数”统一尖点证明不能直接使用。本实验只验证一条明确的充分路径：先找到一个和为零的 7 元组，再调用 (2p+1) 的显式零触发收尾。搜索失败只表示这条有限深度证书没有找到，不表示不可达。

## 算法和独立验证

程序为 `work/experiment_seven_average_n15.py`。

1. 原始输入独立均匀取自 ([-B,B])，最后一个坐标补成零和，然后取本原代表。
2. 只接受 (G=1) 的候选状态。对 (n=15)，因为 (G\mid15)，候选五进/七进条件在七平均下确实简化为 (G=1)。
3. 先枚举所有和为零的 7 元组。若找到，先执行该七平均。
4. 状态出现零后，另外 14 个位置可分成两个和被 7 整除的 7 元组；平均这两组后进入
   ((a^7,(-a)^7,0)) 型状态，再用三次和为零的七平均归零。总尾长至多五步。
5. 每条报告路径都由 `Fraction` 从原始多重集独立重放，检查每次恰有 7 个位置、平均值、总和以及最终全零。

## 有界完整枚举

枚举排序后的十五元整数零和状态，规范化为本原并按整体符号去重，再筛 (G=1)。`direct` 表示初态已有和为零的 7 元组；`certified` 表示直接或至多一次整数七平均后进入零触发尾部。

| 坐标范围 | 合法状态 | direct | certified | 未覆盖 |
|---|---:|---:|---:|---:|
| ([-1,1]) | 7 | 7 | 7 | 0 |
| ([-2,2]) | 84 | 84 | 84 | 0 |
| ([-3,3]) | 861 | 860 | 861 | 0 |
| ([-4,4]) | 6231 | 6225 | 6231 | 0 |

因此在这四个完整有限状态空间中，没有发现需要两次以上预处理的状态，也没有发现反例。最小的非直接状态出现在 ([-3,3])，但一步整数七平均即可进入零触发尾部。
更细的 ([-4,4]) 分类是：4333 个状态初始含零坐标，1896 个状态初始含零和七元组但不属于前一类，另有 2 个状态需要一次整数七平均；三类合计覆盖全部 6231 个状态。

## 独立随机样本

所有样本均满足 (G=1)，成功率指找到上述完整证书的比例，不把未搜索状态算作失败。

| 独立坐标范围 | 样本数 | 直接零七元组 | 一步预处理 | 完成证书 | 未知 |
|---|---:|---:|---:|---:|---:|
| ([-20,20]) | 500 | 初始零坐标 175；初始零和七元组 322；预处理 3 | 500 | 0 |
| ([-100,100]) | 500 | 初始零坐标 34；初始零和七元组 446；预处理 20 | 500 | 0 |
| ([-1000,1000]) | 500 | 初始零坐标 4；初始零和七元组 362；预处理 134 | 500 | 0 |

共 1500 个独立样本全部得到证书。路径长度分布为：

- ([-20,20])：175 条 5 步、322 条 6 步、3 条 7 步；
- ([-100,100])：34 条 5 步、446 条 6 步、20 条 7 步；
- ([-1000,1000])：1 条 5 步、337 条 6 步、162 条 7 步。

随机样本中真正需要“一步预处理”的比例随数值范围增大而上升：约 (0.6\%)、(4\%)、(26.8\%)。另有一部分样本初始就含零坐标，可以直接进入尾部。大范围下随机 7 元组和恰为零的概率下降，但一次整数七平均后出现零和七元组的现象仍很稳定。

## 结论边界

这些数据为 (p=7,n=15) 的猜想提供了很强的数值支持：在完整小范围状态空间和 1500 个大范围随机样本中，所有 (G=1) 实例都能通过“至多一次整数预处理 + 零触发收尾”解决，最长只需 7 次七平均。

但这还不是 (n=15) 的完整证明。尚未证明任意无界 (G=1) 状态都能在一次整数七平均后产生零和七元组，也未搜索或证明更深的有理路径。因此当前严谨表述是：

\[
\text{“七平均十五元的零触发覆盖”在有限枚举和随机样本中通过，未发现反例。}
\]

复现实验：

```text
python work/experiment_seven_average_n15.py --bounds 20 100 --samples 500 --depth 1 --output work/seven_average_n15_range20_100_500.json
python work/experiment_seven_average_n15.py --bounds 1000 --samples 500 --depth 1 --output work/seven_average_n15_range1000_500.json
```

完整有限枚举：

```text
python work/exact_seven_average_n15_bounded.py --bounds 1 2 3 4 --output work/exact_seven_average_n15_bounded.json
```

<!-- END SOURCE doc-b26fccfa3c79 -->

---

<a id="doc-cfae2c05db78"></a>

## 原文导签：七平均的最优最终阈值：二十元、二十二元与 N(7)=15

来源：`work/document_reorganization_20260915/originals/outputs/seven_average_sharp_threshold_complete.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_sharp_threshold_complete.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-cfae2c05db78 -->
# 七平均的最优最终阈值：二十元、二十二元与 N(7)=15

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity/README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

日期：2026-09-14。本文补齐七平均最后两个临界维数 20、22，接上此前各维数定理，得到完整的最终阈值。

## 1. 定理、依赖与证明范围

**定理。** 对任意 n>=15、任意非全等有理 n 元输入，有限七平均可以使全部坐标相等，当且仅当中心化、清分母、本原化后的差分 gcd 为7的幂。因此
\[
\boxed{N(7)=15=2\cdot7+1.}
\tag{1}
\]

本文新增的是 n=20 和 n=22 的全输入证明；这两个维数与7互素，判据均简化为 G=1。其他维数沿用已完成结果，第 8 节逐项列出依赖。并未证明任意素数 p 的 N(p)=2p+1，也未完成五平均12、14元。

证明使用两类证据。实际宏、周期、根和同余消元有直接矩阵证明及原位置重放；固定有限商用完整的父边证书验证。无限群包含使用此前[深同余引理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_middle_congruence_and_eighteen.md)及其明确的 Morris 2007 定理6.1(2)、Serre 强同余子群性质依赖。Morris 相关原文已在项目核对；Serre 原文全文尚未取得，作为标准已发表外部定理引用，未声称由程序验证。

本次完成的关键不是入口，而是核内的正向取逆和全部终端轨道。二十二元尤其需要[统一有限轨道定理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)中的单位尺度商；普通有限射影线不足以完成它。

## 2. 原位置约定与正向逆的取得

继续使用统一核心
\[
\mathcal K_m(a,z)=
\bigl(a^{7m},(-ma+rz)^7,(-7z)^r\bigr),
\qquad n=7(m+1)+r.
\]
二十元为 m=1,r=6；二十二元为 m=2,r=1。令 y=a+7z，则本原核心合法性均为
\[
\gcd(a,z)=\gcd(y,n)=1.
\tag{2}
\]

记三块值为 A、B、C。宏 A(j,s) 的含义是：保留 r 份旧 A；另做 m 份组成完全相同的七元组，每组取 7-j-s 份 A、j 份 B、s 份 C；最后平均其余七个位置。宏 B(j,s) 同理保留旧 B，宏 C(j,0) 保留旧 C。第3、5节表中每个计数都满足原位置容量。

以下表列整数矩阵，实际宏在 (a,z) 上的作用为矩阵乘 1/7。m=1 时每宏有两个原子平均；m=2 时每宏有三个。角色交换 S 不做数值操作，只交换两个等大的七块标签。

若正向宏组成一个闭路
\[
M_\ell\cdots M_1=cI,\qquad c\ne0,
\tag{3}
\]
则闭路中每个宏都有正向射影逆：把闭路循环移位，使该宏最先执行，再执行剩余宏。循环移位后的乘积仍为 cI；实际尺度则另乘每个宏自身的 1/7。此论证对负标量也成立，不能把负的全局尺度与不可执行的逐坐标取负混淆。

## 3. 二十元：三个返回的新标量闭路

二十元核心为
\[
(a^7,(6z-a)^7,(-7z)^6).
\]
采用以下宏：

| 名称 | 原位置类型 | 整数矩阵 |
|---|---|---|
| P | A(5,1) | \(\begin{pmatrix}-4&23\\-1&0\end{pmatrix}\) |
| Q | A(3,3) | \(\begin{pmatrix}-2&-3\\-1&0\end{pmatrix}\) |
| F | C(2,0) | \(\begin{pmatrix}3&12\\0&7\end{pmatrix}\) |
| S | 交换两个七块 | \(\begin{pmatrix}-1&6\\0&1\end{pmatrix}\) |

例如 P 的第一组为 (A,B^5,C)，第二组为 (B²,C^5)，另留 A^6；Q 的两组为 (A,B³,C³)、(B^4,C³)。F 的两组为 (A^5,B²)、(A²,B^5)，C^6 不动。这些都是原20个位置上的真实分组。

直接计算
\[
PQF=\begin{pmatrix}-45&-96\\6&45\end{pmatrix},
\qquad
\boxed{(PQF)^2=1449I.}
\tag{4}
\]
1449=3²·7·23 非零。因此 P、Q、F 均有正向逆。实际按 F,Q,P,F,Q,P 执行，总计12个七平均，返回尺度为1449/7^6。

每个宏的整数行列式与20互素，且在模2、5下保存合法线。完整循环和根词均在两个独立基输入上逐原子检查了局部合法性。

### 双向根与共同环

用整数幺模坐标
\[
u=z,\qquad v=a-3z,\qquad
(a,z)^T=C(u,v)^T,\quad
C=\begin{pmatrix}3&1\\1&0\end{pmatrix}.
\]
合法性变为 gcd(v,10)=1。在此坐标中，
\[
P=\begin{pmatrix}-3&-1\\20&-1\end{pmatrix},\quad
Q=\begin{pmatrix}-3&-1\\0&1\end{pmatrix},\quad
F=\operatorname{diag}(7,3),\quad
S=\operatorname{diag}(1,-1).
\]
令 H=PQ^-1，则
\[
H=\begin{pmatrix}1&0\\-20/3&-23/3\end{pmatrix},
\]
\[
\boxed{SQSQ^{-1}=U(2),\qquad SHSH^{-1}=L(40/3).}
\tag{5}
\]
F 对上、下根的共轭分别把参数乘7/3、3/7，逆共轭也已正向可执行。由于
\[
\mathbb Z[7/3,3/7]=\mathbb Z[1/21]=:R_{20},
\]
得到 U(2R_20)、L(40R_20)，特别得到 U(40R_20)、L(40R_20)。由深同余引理，
\[
\boxed{\Gamma(1600,R_{20})\text{ 正向可执行}.}
\tag{6}
\]
坐标 C 属于 GL2(Z)，故换回 (a,z) 后仍是同一个主同余子群。

虽然构造根的中间宏 P 的行列式含23，(6) 的最终矩阵全部在 R_20 中；有限轨道部分只使用 S、Q、F 及其逆，它们均在 GL2(R_20) 中。没有把23分母默认为 R_20 分母。

## 4. 二十元：全部有限状态到达真实终端

取 M=1600=2^6·5²。合法性使 y=a+7z 在模 M 下为单位，故射影方向可以写成 x=z/y 模 M。

R_20 的单位 +-3^i7^j 模 M 的像是全部640个单位。证书从1出发反复乘-1、3、7，记录每个余数的父边，独立比较得到的集合与全部模 M 单位。因而此处不剩额外尺度类。

在 (z,y) 坐标中，有限图采用
\[
S=\begin{pmatrix}1&0\\20&-1\end{pmatrix},\quad
Q=\begin{pmatrix}7&-1\\60&-9\end{pmatrix},\quad
F=\begin{pmatrix}7&0\\40&3\end{pmatrix},
\tag{7}
\]
以及 Q、F 的逆。每一步的分母都是模 M 单位。完整有限证书证明1600个方向都在 x=0 的同一个轨道，最大父边深度为9。

终端 x=0 的精确目标取 (a,z)=(1,0)。其状态为
\[
(1^7,(-1)^7,0^6),
\]
选三份1、三份-1和一个零，得到真实零和七元组。

对任意合法本原列，沿有限父边回到 x=0 后取本原整数代表 (a',z')，有 z'=0 模 M、a'为模 M 单位。由于单位像已满，可取 s 属于 R_20 单位，使 s=a' 模 M。于是 (a',z') 与 (s,0) 是模 M 相同的 R_20 本原列。统一有限轨道定理中的 Bezout 补列引理给 H 属于 Gamma(M,R_20)，把前者精确送到后者。由 (6) 实现 H，再接零触发收尾。

至此证明所有合法二十元核心可达。任意原输入的入口由[统一两轮入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_unified_weighted_core_theorem.md)给出：r=6>=omega(20)=2。因此二十元完整 G=1 判据成立。

## 5. 二十二元：原来只有一个对合的边界也能取逆

二十二元核心为
\[
(a^{14},(-2a+z)^7,-7z).
\]
采用三个宏：

| 名称 | 原位置类型 | 整数矩阵 |
|---|---|---|
| A | A(1,0) | \(\begin{pmatrix}4&1\\-1&0\end{pmatrix}\) |
| F | C(2,0) | \(\begin{pmatrix}1&2\\0&7\end{pmatrix}\) |
| J | B(2,0) | \(\begin{pmatrix}1&2\\2&-1\end{pmatrix}\) |

宏 A 保留一份旧 A，两重复组各为 (A^6,B)，最后为 (A,B^5,C)。宏 F 保留 C，两重复组各为 (A^5,B²)，最后为 (A^4,B³)。宏 J 保留一份旧 B，两重复组各为 (A^5,B²)，最后为 (A^4,B²,C)。均恰好使用原22个位置。

直接有
\[
FA^2=\begin{pmatrix}7&2\\-28&-7\end{pmatrix},
\qquad
\boxed{(FA^2)^2=-7I,\qquad J^2=5I.}
\tag{8}
\]
因此 A、F、J 及其逆都能正向执行。实际 A,A,F,A,A,F 共18次七平均，尺度为-7/7^6。

这一步绕过“r=1只存在一个迹零对合”的旧容量限制：A、F 本身不必迹零，联合闭路提供正向逆。

### 根与深主同余

令 H=AFJA^-1，则
\[
H=\begin{pmatrix}-7&-62\\0&5\end{pmatrix},
\qquad
\boxed{FHF^{-1}H^{-1}=U(396/35).}
\tag{9}
\]
F、H 对上根参数的共轭倍率分别为1/7、-7/5；连同逆共轭，生成 R_22=Z[1/35]，故有 U(396R_22)。

取
\[
C=\begin{pmatrix}1&4\\0&-1\end{pmatrix}=C^{-1}.
\]
对任意 t，
\[
CU(t)C=U(-t),\qquad
CAU(t)A^{-1}C=L(t).
\]
所以在这个整数幺模坐标中已有双向396倍根。深同余引理给出
\[
\Gamma(396^2,R_{22})\subseteq\Gamma^+.
\tag{10}
\]
由于 C 整幺模，结论换回原坐标仍成立。

### 删去辅助的三进深层

396²=1936·81。要避免在辅助素数3处无谓扩大有限商，下面严格证明
\[
\boxed{\Gamma(1936,R_{22})\subseteq\Gamma^+.}
\tag{11}
\]

置 X=F²/7，它是 SL2(R_22) 中已有正向实现的规范代表。整数模计算给
\[
A^{440}=X^{440}=I\pmod {1936}.
\]
将这两个矩阵约化模9，所得生成元生成全部 SL2(Z/9Z)，共648个元素。固定证书保存全部父边，独立检查每个矩阵行列式为1；群阶公式
\[
|\mathrm{SL}_2(\mathbb Z/9\mathbb Z)|=3^3|\mathrm{SL}_2(\mathbb F_3)|=648
\]
证明这是完整群，而非一个抽样子集。

从模9满射，可取三个真实词在模9下分别等于 I+3E12、I+3E21、I+3diag(1,-1)。这些词都由 A^440、X^440 组成，因此在模1936下恒为 I。对任意这样的词 W=I+3T，奇素数3的二项式展开给
\[
W^{3^k}=I+3^{k+1}T\pmod {3^{k+2}}.
\]
三方向逐层补齐全部高阶核，所以这个模1936恒等的子群在模81上仍满射到 SL2(Z/81Z)。

给定 g 属于 Gamma(1936,R_22)，选该子群中的 w 使 w=g 模81。两者模1936均为 I，故 w^-1g 属于 Gamma(1936·81,R_22)，已由 (10) 可执行。这证明 (11)，没有从一个小模像直接推断无限群包含。

## 6. 二十二元必须保留共同尺度

现在取 M=1936=2^4·11²。R_22 单位 +-5^i7^j 的模 M 像只有440个，而全部模 M 单位共有880个；这一次单位像不满。

固定证书给
\[
U=\overline{R_{22}^{\times}},\qquad
(\mathbb Z/M\mathbb Z)^\times=U\ \sqcup\ 3U.
\tag{12}
\]
对合法本原列，y=a+7z 是模 M 单位。正确的有限状态因此为
\[
\boxed{(x,\epsilon),\quad x=z/y\pmod M,\quad
\epsilon=
\begin{cases}
0,&y\in U,\\
1,&y\in3U.
\end{cases}}
\tag{13}
\]
共1936·2=3872个。取本原整数代表时可能除去的5、7因子及共同符号属于 R_22 单位，所以 (13) 与代表选择相容。

在 (z,y) 坐标中，三个宏为
\[
A=\begin{pmatrix}7&-1\\22&-3\end{pmatrix},\quad
F=\begin{pmatrix}7&0\\44&1\end{pmatrix},\quad
J=\begin{pmatrix}-15&2\\-110&15\end{pmatrix}.
\tag{14}
\]
若矩阵写成 (\alpha,\beta;\gamma,\delta)，其作用必须同时更新方向和尺度：
\[
x'=(\alpha x+\beta)(\gamma x+\delta)^{-1}\pmod M,
\]
\[
\epsilon'=\epsilon+\chi(\gamma x+\delta)\pmod2,
\tag{15}
\]
其中 chi 是单位群对指数2子群 U 的商映射。所有分母均为模 M 单位。

完整证书用 A、A^-1、F、F^-1、J 的五条边，证明全部3872个状态均在 (0,0) 的单一轨道；最大父边深度为8。证书不只检查投影到 x 的1936个方向，也没有假设不同素数的局部结果自动拼接。单位类和方向在整个模 M 上一起验证。

因此任意合法核心沿父边回到 (0,0) 后，本原代表满足 z'=0 模 M，a'属于 U。由 (12) 可选择 s 属于 R_22 单位，使 s=a' 模 M。用 (11) 和同余本原列的补列引理，精确送到 (s,0)。

精确终端为
\[
(s^{14},(-2s)^7,0).
\]
选四份 s、两份 -2s 和一个零，真实七平均产生七个零，再接已证零触发尾部。

所以全部合法二十二元核心可达。[上半带统一入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_upper_band_three_value_reduction.md)已覆盖其全部原输入，因此二十二元完整 G=1 判据成立。

## 7. 有限证书怎样承担全部输入

两种证明都遵循同一个严格顺序：

1. 原位置计数表给宏；标量闭路给正向逆。
2. 精确交换子给双向根。
3. 外部有限指数、强同余子群定理和任意有限环消元给明确的主同余包含。
4. 在这个已经确定的模数上穷尽方向与可实现单位尺度，得到有限父边树。
5. 对任意无界输入，用父边词回到终端剩余类，再用主同余补列矩阵到精确终端。

第五步仍处理任意大的有理输入，不要求把所有输入值穷举。有限图只承担已证明的有限商命题。程序另外为图中每个状态选取一个整数本原提升，核对其逆词和精确 Bezout 目标矩阵；它没有展开任意主同余元素的完整原子词。

二十元全部单位已可实现；二十二元单位像缺少一半，但宏本身可在两种尺度类之间移动。后者展示了为什么“单位像不满”不意味着不可达：必须检查式 (15) 的联合轨道。

## 8. 合并已有结果，得到最优阈值

| 维数 | 完整判据的来源 |
|---|---|
| 15 | [七平均十五元](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_fifteen_complete.md) |
| 16 | [p+1为2幂的双单点证明](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_energy_and_dyadic_neighbour.md) |
| 17、19 | [奇余量核心与入口](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_uniform_odd_middle_cores.md) |
| 18 | [偶数同余闭合](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_even_middle_congruence_and_eighteen.md) |
| 20、22 | 本文 |
| 21 | [任意p的3p定理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_middle_band_structure.md) |
| 所有 n>=23 | [七平均3p+2最终上界](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_three_p_plus_two_threshold.md) |

因此所有 n>=15 均满足完整七幂 G 判据。另一方面，[一般2p下界](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_linear_threshold.md)给出十四元合法但不可达输入
\[
(-7,0^6,1^7).
\]
其 G=1；不可达性引用该页对允许分数路径也成立的证明，不能由单步整数冻结代替。因此 N(7)>=15，结合上述充分性得到 (1)。

## 9. 核验、来源记录及限制

[独立核验程序](../work/verify_seven_average_sharp_completion.py)固定使用本文计数表和恒等式，不重新搜索种子或平均词。闭路候选来自对原有小计数菜单的有限精确矩阵检查；一般p并未由这种有限检查外推。正式证明完全以表列矩阵和可重放证书为准。

核验包括：38个独立基上的正向循环、逆词和根词；648个完整模9矩阵；二十元640个单位与1600个有限方向；二十二元440个可实现单位及全部3872个方向--尺度状态；5472个精确主同余目标矩阵；96条50位整数原输入的合法入口和两个真实零触发尾部。两个有限图的全部生成元边都被检查。

[证书数据](../work/seven_average_sharp_completion_records.json)保存单位父边、状态父边、辅助模9父边及原位置入口。核验只枚举固定有限商，使用预计算模逆与整数矩阵，约一秒完成。一般群词的长度、分母深度和高效提取仍未控制；不存在“所有输入只需图深度8或9次平均”的结论。

项目入口：python work/run_verifications.py --id seven-average-sharp-completion。

本轮同时复跑了阈值合并依赖的seven-average-fifteen-complete、carrier-energy-dyadic-neighbour、uniform-odd-middle-cores、even-middle-eighteen-congruence、prime-arity-middle-band、seven-average-three-p-plus-two及prime-arity-linear-threshold；各项核验均通过。它们的无限量词仍由对应证明承担，复跑不替代证明审阅或外部定理。

这是一个完整素数平均元数的最优最终阈值结果。任意p的统一最优阈值仍开放；新增可复用内容是多返回闭路激活逆，以及保留单位尺度后完整终端覆盖的实际闭合。

## 10. 对一般 p 的实际帮助与不可外推边界

用户要求的主目标是一般 p。本文虽然完成七平均，但没有因此减少一般 p 尚待证明的核心覆盖条件，也没有降低任意 p 的统一最终阈值。固定小平均元数的完成不能替代这个目标。

两条闭路的自然参数化可以直接审计。对 p=1 模6、p>=7：

- 在 n=3p-1 中，令 P=A(p-2,1)、Q=A((p-1)/2,(p-1)/2)、F=C((p-1)/3,0)，三个计数模板有原位置容量。精确多项式计算给
  \[
  \operatorname{tr}(PQF)=-\frac{(2p+1)(p-7)}6.
  \]
- 在 n=3p+1 中，令 A=A((p-1)/6,0)、F=C((p-1)/3,0)，则
  \[
  \operatorname{tr}(FA^2)=\frac{(p+1)(7-p)}{12}.
  \]

所以本文用于取逆的这两条迹零闭路，在上述自然推广中都只于 p=7 成立。核验程序直接在 Q[p] 的多项式环中比较系数，不从有限 p 样本推断该结论。这不排除不同参数选择、更长词或其他返回存在一般周期；只是明确排除把本文两条公式直接称为参数无关闭路。

可借鉴的经验是：不必要求每个基本宏单独迹零，也不必要求环单位像满群。前者可由联合闭路代替，后者必须检查方向—尺度的联合作用。但这些替代条件本身仍需对一般 p 证明；七平均的有限证书没有承担这个量词。

因此后续主线应继续处理一般 p 的正向取逆、核内联合终端覆盖及少数入口条件，不再以增加另一个固定 p 的证书作为这些一般任务的完成标准。

<!-- END SOURCE doc-cfae2c05db78 -->

---

<a id="doc-e64084cd15fa"></a>

## 原文导签：七平均达到 3p+2：对称碰撞总和的完整证书

来源：`work/document_reorganization_20260915/originals/outputs/seven_average_three_p_plus_two_threshold.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_three_p_plus_two_threshold.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-e64084cd15fa -->
# 七平均达到 3p+2：对称碰撞总和的完整证书

日期：2026-09-12。这里平均元数是 7，与“三平均七元”不是同一个问题。

2026-09-14完整后续：[七平均最优阈值](../sources/work/document_reorganization_20260915/originals/outputs/seven_average_sharp_threshold_complete.md)已补齐20、22，接此前15—19、21以及本页全部n>=23定理，得到N(7)=15。以下N(7)<=23是本页独立证明的历史上界，其n>=23结果继续作为完整阈值的依赖。

## 1. 主定理

**定理。** 所有 n>=23 元有理输入，在非全等时作中心化、清分母及本原化后，有限七平均可达性恰由 G 为 7 幂刻画。

所以

\[
\boxed{15\le N(7)\le23=3\cdot7+2.}
\]

本次新增完整维数 n=23、24、25、26，接此前 n>=27 的定理。
此前 n=21 也已由三块运输证明；n=22 尚未解决，因此不能将 N(7) 宣称为 21。
七平均在猜想端点及中间段尚待覆盖 15、16、17、18、19、20、22。

新增四个维数的整数零和合法输入只需一位额外七进精度。
这是完整有限符号证书辅助的证明；并非只验证有限输入，也没有搜索平均词。

## 2. 一般有效的对称压缩

沿用[五平均总和证书](../sources/work/document_reorganization_20260915/originals/outputs/five_average_three_p_threshold.md)的双重值剩余形状：

\[
f(a)=p+\alpha,\quad f(b)=p+\beta,
\quad\alpha\ge\beta\ge0,\quad\alpha+\beta\le p-3,
\quad p\nmid a-b.
\]

保护集合 T 是危险低重数例外集的包含极小横截集，记 h=|T|。
令 delta=a-b，未保护低重数位置的参数为 t_i=(x_i-b)/delta，余数 z_i=t_i mod p。
假设所有保护后候选都碰撞，就有此前的子集关联方程。

**对称压缩引理。** 将一个余数类的实际参数取算术平均，记其重数 f_r、平均值 y_r。
如果全部个体位置方程相容，那么压缩变量 y_r 满足

\[
\sum_r k_r y_r=p-i
\]

或另一锚点的

\[
\sum_r k_r y_r=\sum_r k_r+j-p,
\]

其中 k_r 是实际可选的位置数，0<=k_r<=f_r，且总选取数及锚点富余数合法。
总和保持为 sum_i t_i=sum_r f_r y_r。

证明：固定每类选取数量 k_r，对该类型的全部位置选择取方程平均。
一个位置出现在 k_r/f_r 比例的选择中，所以它们的贡献恰为 k_r y_r。
这只平均分析方程，不对实际状态新增任何操作。

若某条候选方程在一个余数类中选取 0<k_r<f_r 个位置，则交换一个选中与未选的位置，两个方程相减，迫使这两个位置的实际参数相等。
对所有位置重复交换，该余数类便实际常值。

因此，求总和时可以从一开始压缩到“每个余数一个变量”，不必先假设同余值实际相等。
这个引理对任意 p 成立。

## 3. 七平均剩余模式的完整分类

此前的顺序、同余双重值、单背景和共同预留分支全部沿用。
只剩 p=7、alpha+beta<=4 的不同余双重值情况。

锚点同余修复表明：余数 0 和 1 各至多有一个低重数位置，其实际参数分别为 7、-6。
任一余数若有七个未保护位置，直接平均它们就保留两个旧重值。因此所有余数重数至多六。

令

\[
n-h=21+e,\qquad L=7+e-\alpha-\beta.
\]

对 n=23、24、25、26 及其 h<=d_7(n)，总有 e in {1,2,3,4,5}。
逐项列出全部无序余数多重集，并建立第 2 节的精确压缩方程，共有 57026 个系统。
仅下列 11 个模式相容：

| e | alpha,beta | 余数与重数 | 压缩实际参数 | D=7+alpha+sum f_r y_r |
|---:|---|---|---|---:|
|1|2,0|2^6|2|21|
|1|3,0|2^5|2|20|
|1|3,0|2^4,3|2,3|21|
|1|4,0|2^4|2|19|
|1|4,0|2^3,3|2,3|20|
|1|4,0|2^3,4|2,4|21|
|1|4,0|2^2,3^2|2,3|21|
|2|3,0|2^6|2|22|
|2|4,0|2^5|2|21|
|2|4,0|2^4,3|2,3|22|
|3|4,0|2^6|2|23|

e=4、5 没有相容模式。
每个相容系统都满秩，表中是唯一有理解；每个重数大于一的余数类都出现在至少一条部分选取方程中，因此个体实际参数也都等于表中给出的整数。

这个有限证书给出的关键结果是

\[
\boxed{D\in\mathbb Z,\qquad0<D<21+e.}
\tag{1}
\]

一般原位置参数是任意有理数，不受高度界限制；有限枚举只枚举其模 7 模式。

## 4. 接到最小保护总和矛盾

若 h>0，选择某个保护位置的私人素数 q。
由保护构造，q|(a-b)=delta，其他保护位置在模 q 下都属于主类。
未保护部分相对 b 的总和为 delta D，(1) 保证它模 q 为零。
这使整个状态在模 q 下只剩该保护位置一项非零差，违反 q|n 及全局零和。

若 h=0，全部低重数实际参数都是整数，所以所有实际值都属于 b+delta Z。
合法性于是迫使 gcd(delta,n)=1。
零和关系

\[
nb+\delta D=0
\]

要求 n|D，但 (1) 给 0<D<n，矛盾。

因此全部碰撞不可能发生，必有安全非恒等整数七平均保持双重值。

## 5. 初始化、其他分支和终止

n=23、24、25、26 都满足旧初始化条件 n>=21+d_7(n)。
从 7X 出发，至多两次整数平均进入双重值不变量。
三重值分支适用已证的 n>=3p+2 引理，其余旧分支的前提也都满足。
第 4 节补齐唯一剩余的低总重数不同余双重值分支。

每一步均安全、整数、非恒等，平方能量严格下降；相反值终端可直接消去。
所以有限终止。缩回原输入，所有中间值属于 (1/7)Z。
接已有 n>=27，主定理成立。

## 6. 核验及一般化边界

`work/verify_seven_three_p_threshold.py` 独立重建压缩方程，不导入本轮探索程序。
消元使用整数行运算和 gcd 约分，只在回代时使用精确分数。
完整相容解表固定为上面的 11 行，逐一回代验证；重复余数类的部分选取条件也被检查。

运行时的原子选择使用固定基数与余数的极值动态规划，所有输出都是七个原位置的实际平均。
有限随机路径并非证明依据，只用于独立重放与精度检查。

本轮通过：57026 个完整符号系统及 11 个唯一解、5628 个大整数闭包实例、96 条完整原位置 Fraction 路径，最长276步。
相邻五平均核验也重新运行，确认通用化辅助函数未改变其证书。

本页没有把模 7 分类外推到任意 p。
对任意 p，真正值得推广的是第 2 节的对称总和方法，以及何时碰撞总和必为整数且位于目标区间；该普遍命题仍开放。

项目入口：`python work/run_verifications.py --id seven-average-three-p-plus-two`。

<!-- END SOURCE doc-e64084cd15fa -->

---

<a id="doc-58f23beef83d"></a>

## 原文导签：为什么三平均的精确阈值是七：资源边界、有限周期与合法单轨道

来源：`work/document_reorganization_20260915/originals/outputs/seven_exact_threshold_structure.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/seven_exact_threshold_structure.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-58f23beef83d -->
# 为什么三平均的精确阈值是七：资源边界、有限周期与合法单轨道

日期：2026-09-12。

同日后续：[统一正向控制器](../sources/work/document_reorganization_20260915/originals/outputs/uniform_endpoint_positive_controller.md)已通过第二种“保留单点”返回、仿射配对、必碰偶数的整数链及欧拉周期，证明每个奇数平均元数的安全返回都有正向逆，并取得完整局部化上下根。第6节在q=2p+1为素数时的充分条件现已无条件实现；合数q的全输入入口与轨道仍需另证。本页保留七元的独立短周期证明和特定扫掠的谱分界。

本页区分两件事：为什么六元尚有反例，以及为什么七元已经能够处理全部合法输入。
前者由位置资源与三进障碍解释；后者需要真实操作的精确代数关系。
它们不是同一个论断，不能只凭“多了一个缓冲位置”就宣称充分性。

## 1. 六到七的边界是实际的资源变化

六元输入

\[
(-3,0,0,1,1,1)
\]

零和、本原，G=1，却不可达。
唯一非恒等整数三平均得到 (-1^3,1^3)，产生模 2 的非零共同余数障碍。
而对至多六个位置，成功路径不能引入新三进分母：首次产生的最低三进层恰为三个相等位置；后续部分相交会使这一非零最低层继续下降，完全不相交则在六元处形成两个相反常值块，仍受模 2 障碍限制。

加入第七个零后，形成两个相反三重块加一个单点零，三个 (-1,1,0) 就可以逐对消去。
因此 6 和 7 的区别确实存在于原位置的操作能力中。

但这仅给出阈值下界和一个收尾机制。要解释七元全部输入的充分性，还需下面的两层结构。

## 2. 七元恰好容纳一个完整的双块载体系统

考虑

\[
(u^3,v^3,w),\qquad3u+3v+w=0.
\]

令 d_1=u-w、d_2=v-w。
平均载体 w 和某个三重块中的两个位置，旧块剩余的那个位置成为新载体。
两个真实操作对差值的作用为

\[
E_1=\begin{pmatrix}-1/3&0\\-1&1\end{pmatrix},\qquad
E_2=\begin{pmatrix}1&-1\\0&-1/3\end{pmatrix}.
\]

依次交换两块，得到

\[
E_2E_1=\frac13 V_3,\qquad
V_3=\begin{pmatrix}2&-3\\1&-1\end{pmatrix}.
\]

这个矩阵满足

\[
\chi_{V_3}(t)=t^2-t+1,\qquad V_3^3=-I.
\]

故六次正向原子平均构成精确关系

\[
\boxed{(E_2E_1)^3=-\frac1{27}I.}
\tag{1}
\]

循环旋转这个正词并删去首字母，可以正向实现每个 E_i 的射影逆。
这里不是倒放平均或拆分坐标；逆是由另外五次正向三平均组成的。

还有一个关键点：这七个位置就是整个系统，其均值正是目标零。
因此差值整体缩放会使整个状态整体缩放。
如果把同样七个位置当作更大系统中的一个窗口，通常只能得到围绕该窗口自身均值的收缩，不能直接当成整个系统的射影逆。
这解释了七元局部机制为何精确有效，也解释了它不能未经处理地拼接到所有更大维数。

## 3. 同一载体机制在一般 p 上有明确的谱分界

对一般素数平均元数 p，两个 p 重块加一个单点仍产生

\[
E_1=\begin{pmatrix}-1/p&0\\-1&1\end{pmatrix},\qquad
E_2=\begin{pmatrix}1&-1\\0&-1/p\end{pmatrix},
\]

所以

\[
pE_2E_1=V_p=\begin{pmatrix}p-1&-p\\1&-1\end{pmatrix},
\quad\det V_p=1,\quad\operatorname{tr}V_p=p-2.
\]

其特征多项式与判别式为

\[
t^2-(p-2)t+1,\qquad p(p-4).
\]

- p=2：特征值为四次单位根，V_2²=-I。
- p=3：特征值为六次单位根，V_3³=-I。
- p>=5：特征值为互为倒数的不同正实数，V_p 没有有限射影阶。

因此三平均七元的六步关系来自一个准确的有限周期，确实带有小素数特性。
它不是“所有 p 都会有相同周期”的迹象。

反过来，这也不是 p>=5 的不可达障碍：五平均十一元已经通过额外跨块返回获得另一组正向周期并解决全部合法输入。
有限周期的具体来源可以改变，但必须实际构造。

## 4. 给七元补上一份不依赖十八词覆盖的结构证明

先说明全输入入口。任意七元合法整数零和输入，保留一个单点 c，将其余六个位置分成两个三元块。
若其中一块和为 S，平均后的块值差为 (2S+c)/3。
若它模 7 为零，交换两块中一对模 7 不同的值，就把这个差变成模 7 非零。
这样的跨块差异必存在，否则原七个值模 7 全同余。
因此两次三平均就能进入合法

\[
K_3(a,b)=(a^3,b^3,-3(a+b)).
\]

### 4.1 三个有原位置账本的返回

对 j=1,2,3，依次平均

\[
(a^{j-1},b^{3-j},-3(a+b)),\qquad
(a^{3-j},b^j).
\]

输出为 K_3(c,d)，其中

\[
c=-\frac{(4-j)a+jb}{3},\qquad
d=\frac{(3-j)a+jb}{3}.
\]

令 x=a、y=a-b，射影矩阵与块重标记为

\[
T_j=\begin{pmatrix}-4&j\\-7&2j\end{pmatrix},\qquad
\Sigma=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
\]

真实 T_j 带共同因子 1/3；Σ 只是将两个块的名称互换，后续原下标账本随之更新。
合法性为 7 不整除 y，全部 T_j 和 Σ 都保持它。

七本身为素数也在这里发挥了作用：1<=j<=3 的全部行列式 -j 都在模 7 下可逆，所有这些跨块返回都能用于整个合法域。

### 4.2 三个精确正向周期

直接矩阵恒等式给出

\[
\boxed{T_2^2=2I,\qquad(\Sigma T_1)^3=-I,\qquad
(\Sigma T_3)^6=-27I.}
\tag{2}
\]

每个字母都处于一个正向标量周期中，所以全部 T_j 的射影逆均有正向平均词。
这一步提供的是确实可执行的群，不是假定平均可逆。

### 4.3 生成完整局部化根与同余群

记 Δ(t)=diag(1,t)，U(t)=E12(t)，L(t)=E21(t)。
有

\[
T_1^{-1}T_j=\Delta(j),\qquad
\Sigma\Delta(2)\Sigma\Delta(2)^{-1}=U(1/2),
\]

\[
\Sigma U(1)=\Delta(-1),\qquad
T_1U(1/4)\Delta(-16)=-4L(7/4).
\tag{3}
\]

由整数幂与对角共轭，得到 R=Z[1/6] 上的全部

\[
U(R),\qquad L(7R),\qquad\Delta(R^\times).
\]

这些都是由 (2)--(3) 编译的正向三平均词。
R 中出现二分母，是射影作用带共同缩放的结果，不是在实际操作中加入二平均；实际坐标仍只有三进分母。

对 Γ₀(7)，有符号右陪集代表为

\[
I,\qquad\mathsf S\mathsf T^j\quad(-3\le j\le3),
\]

其中 𝕊=[[0,-1],[1,0]]、𝕋=U(1) 仅用作模群的代数生成元。
全部非平凡 Schreier 回路为 U(1)、L(-7)，以及

\[
g_j=\begin{pmatrix}-k&-1\\jk+1&j\end{pmatrix},
\quad k\equiv-j^{-1}\pmod7,\quad0<|k|\le3.
\]

每个 g_j 都有分解

\[
g_j=L\!\left(-\frac{jk+1}{k}\right)
\operatorname{diag}(-k,-1/k)U(1/k).
\]

所有主元 k 在 R 中可逆。因而可执行群包含完整 Γ₀(7)，不需十八个下降词的实区间覆盖证书。

### 4.4 合法单轨道与归零

对本原整数列 (x,y)，7 不整除 y。取 αx+βy=1，再将 α、β 调整为 α+ky、β-kx，使 7 整除 α。
于是

\[
h=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}\in\Gamma_0(7),
\qquad h(x,y)^T=(0,1)^T.
\]

所以所有合法方向都可经正向平均到某个非零缩放的 K_3(0,-1)。
先平均 (3s,0,0)，再三次平均 (s,-s,0)，四步归零。
结合全输入入口，这是一份完整的七元充分性证明。

这里明确使用了正向逆、完整根群、全部陪集回路和终端，不能只把其中的有限周期单独称作充分性证明。

## 5. “七是阈值”的三层含义

七元可以解释为三层机制恰好同时具备：

1. 位置层：两个三重块外第一次可以保留一个独立位置，六元的非零相反块陷阱因此可以被打破。
2. 动力层：这个全系统载体窗口具有精确正向周期，实际返回可形成可逆的射影控制。
3. 算术层：加入明确跨块返回后，真实群足以覆盖唯一合法有理轨道，并且该轨道有原位置终端。

必要边界由第一层解释；充分性需要第二、三层。
仅有一个零或缓冲位置，不自动保证任意输入都能造零；仅有周期，也不自动保证全部合法轨道相通。

此外，“七元全部可解”并不独自证明 N(3)=7。
完整阈值还要结合已证八、九、十元，以及 n>=11 的统一不变量定理。
六元反例与这些充分性结果共同给出最优统一阈值 N(3)=7。

## 6. 一条可检验的精确端点充分条件

对任意奇素数 p，若 q=2p+1 也是素数，同一族两步返回在 (a,a-b) 坐标中为

\[
T_j(p)=\begin{pmatrix}-(p+1)&j\\-q&2j\end{pmatrix},
\qquad1\le j\le p.
\]

这些返回无条件存在于原 q 个位置上，实际带因子 1/p。
如果能够为它们构造正向射影逆，则

\[
T_1^{-1}T_j=\Delta(j),
\]

以及与 (3) 同型的公式给出 R=Z[1/p!] 上的 U(R)、L(qR) 和对角单位。
其中下根来自

\[
T_1U\!\left(\frac1{p+1}\right)\Delta(-(p+1)^2)
=-(p+1)L\!\left(\frac q{p+1}\right).
\]

p+1 的素因子不超过 p，所以所有系数都在 R 中。
Γ₀(q) 的有符号 Schreier 主元绝对值至多 p，因而同一完整生成与轨道证明直接适用。
单素数维数的两步入口及含零终端随后解决该端点。

这是一条准确的充分路线：p=3 和 p=5 的正向逆已经分别由不同的明确周期构造出来。
它不是所有 p 的已证定理，也不声称这些逆是可达性的必要条件。
q 为合数时还存在多素数入口问题，不能略去该前提。

还有一个更直接的合数边界：若素数 r 整除 q=2p+1，并且 r 整除 j，则 T_j 的输出满足 y'=0 mod r。
当输入 x 是模 r 单位时，x'=-(p+1)x+j y 仍为单位，因为 gcd(p+1,2p+1)=1。
输出因此在原位置上全部成为同一个非零模 r 余数，不能归零。
所以 q 为合数时，不能无条件采用全部 j=1,...,p 的返回。
7=2*3+1 与 11=2*5+1 都是素数，使它们在这方面共有同一个简洁合法域；15=2*7+1 已不同。

这说明精确端点不必通过不断压低 4p 的常数才能到达；它可以由单独的结构定理直接闭合。
但当前仍缺对全部素数平均元数统一成立的端点机制，以及从端点到临界维数带全部维数的覆盖。

## 7. 核验职责

程序独立重放三个七元返回、三条周期、正向逆和根公式，核对 Γ₀(7) 的完整八陪集及六个有符号回路。
一般公式通过精确矩阵恒等式检查；有限参数实例仅用于防止账本和符号错误。
此证明不导入或运行旧十八词实覆盖程序，也不使用有限深度搜索来声称无限轨道覆盖。

本轮核验：六个平均元数下的双块扫掠与谱公式；三个七元返回及三条精确周期；十三组根与对角种子恒等式；八个陪集、六个有符号回路和全部 24 条标准生成元转移；十条直接 Fraction 原位置归零路径，最长 338 次原子操作。

项目入口：`python work/run_verifications.py --id seven-endpoint-structure`。

<!-- END SOURCE doc-58f23beef83d -->

---

<a id="doc-4c0a86ab6d12"></a>

## 原文导签：六平均九元：所有输入固定四步完成

来源：`work/document_reorganization_20260915/originals/outputs/six_average_nine_fixed_network.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/six_average_nine_fixed_network.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-4c0a86ab6d12 -->
# 六平均九元：所有输入固定四步完成

日期：2026-09-12。本页独立整理并重新核验此前的九元网络，回答“六平均在最低候选维数9是否满足 \(G\) 条件”。

## 1. 结论

**任意九个有理数，甚至任意九个实数，都可用同一个四步六平均词变为全局均值。**

对非全等有理输入，本原中心化后的 \(G\mid9\)，所以 \(G\) 只能取1、3或9。这些全部满足六平均要求的“素因子仅来自2、3”。因此九元的候选判据成立，且在这一维数上自动满足。

四步还是**固定全输入网络**的最优长度；某些特定输入可能少于四步，本文不声称每个输入都恰需四步。

## 2. 原位置操作与恒等证明

位置采用1基编号，依次平均：

~~~text
1,2,3,4,5,6
1,2,3,7,8,9
1,2,3,7,4,5
1,2,3,6,8,9
~~~

设初态前六项的均值为 \(a\)，后三项的均值为 \(c\)，全局均值为
\[
A=\frac{2a+c}{3}.
\]
第一步后前六项均为 \(a\)。第二步选三份 \(a\) 与后三项，得到六份
\[
b=\frac{a+c}{2},
\]
其余三项仍为 \(a\)。

第三步恰好选四份 \(b\) 与两份 \(a\)，新值是
\[
\frac{4b+2a}{6}=\frac{2a+c}{3}=A.
\]
留下三项分别为 \(a,b,b\)，其和 \(a+2b=3A\)。第四步取这三项和三份 \(A\)，均值又为 \(A\)。至此九项全等。

这是线性恒等证明，与数值大小、余数模式和随机样本无关。对应的固定矩阵乘积精确等于 \(J_9/9\)。

## 3. 为什么不存在固定三步方案

按位置对称性，固定第一次操作的六元集为 \(S\)，其后六行系数都为 \(r_S=\mathbf1_S/6\)，其他三行为单位行。

考虑任意第二次操作，六元集为 \(T\)，交数 \(k=|S\cap T|\ge3\)。第二次之后的行只有以下三种：

- 未被再次平均的 \(r_S\)，它支撑在六个位置上，不能是全均值行 \(\mathbf1/9\)；
- 未被平均的单位行，同样不是全均值行；
- \(T\) 中的新行
  \[
  r_T=\frac{k}{6}r_S+\frac16\sum_{j\in T\setminus S}e_j^T.
  \]

若 \(T\setminus S\ne\varnothing\)，每个此类位置的系数为 \(1/6\)，不等于目标的 \(1/9\)。若 \(T\setminus S=\varnothing\)，新行仍是 \(r_S\)。因此第二步后**没有任何一行**等于全均值行。

第三次操作只能改变六行，留下三行不动，故不可能使全部九行等于 \(\mathbf1/9\)。不足三步的固定方案也不能更强，可以重复最后一个恒等平均补到三步。

因此任何固定全输入六平均九元网络至少需四步，而第2节达到四步。

## 4. “九元成功”不等于“所有 \(n\ge9\) 成功”

六平均八元存在 \(G=1\) 反例
\[
(-1,-1,-1,-1,-1,-1,0,6).
\]
它的六份 \(-1\) 是三进赋值的唯一最小同值块；每个非恒等六平均都形成新的、更低赋值的六重块，所以永远不能归零。证明见[合数平均报告第8节](../sources/work/document_reorganization_20260915/originals/outputs/composite_arity_four_six_transfer.md)。

所以从8到9，\(G\) 的全称充分性确实从失败变为成功。但这两个事实不能自动推出最终阈值 \(N(6)=9\)。[六平均十元](../sources/work/document_reorganization_20260915/originals/outputs/six_average_ten_complete.md)现已独立完成非自动G判据；后面的11、13、14、16、17、19、20、22、23元仍待解决。已有定理覆盖全部三的倍数及全部 \(n\ge24\)，故
\[
9\le N(6)\le24.
\]
这里 \(N(6)\) 要求其后所有维数都满足完整判据。本文没有给出端点向整个区间传播的引理。

## 5. 独立核验

[核验脚本](../work/verify_six_average_nine_fixed_network.py)只用 Python 标准库，不导入已有网络构造器：

~~~text
python work/run_verifications.py --id six-average-nine-fixed-network
~~~

检查全部九个标准基以确认乘积为 \(J_9/9\)；固定第一次操作后，穷尽84个第二次操作的全部756行，确认任何行都不可能是全均值行；另有160个含大整数及有理分母的输入重放。

~~~text
six-average n9 fixed network exact basis: PASS 9
six-average n9 three-step fixed-network exclusion: PASS 756
six-average n9 original rational samples: PASS 160
six-average nine-position universal four-step network: PASS
~~~

矩阵恒等式与三步下界由正文证明，有限核验负责审计索引和分数运算。原始数值从不规范化，位置数不变。

<!-- END SOURCE doc-4c0a86ab6d12 -->

---

<a id="doc-11fc9beac1cb"></a>

## 原文导签：六平均十元完整G判据：第一个非自动的算术成功维数

来源：`work/document_reorganization_20260915/originals/outputs/six_average_ten_complete.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/six_average_ten_complete.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-11fc9beac1cb -->
# 六平均十元完整G判据：第一个非自动的算术成功维数

日期：2026-09-12。采用用户指定的研究标准：只把G条件确实筛选输入、且恰好等价于有限步可达的维数作为非平凡算术成功点。九元无条件网络保留为独立结构结果，不代替十元的证明。

## 1. 主定理

给定十个有理数，中心化、清分母、本原化为非零整数零和状态 \(X\)，记
\[
G=\gcd_{i<j}|X_i-X_j|.
\]
则
\[
\boxed{
X\text{ 可有限步六平均归零}
\iff G\in\{1,2\}
\iff5\nmid G.
}
\tag{1}
\]
全等输入单独由空词解决。

因为本原零和十元状态总满足 \(G\mid10\)，故可能值仅为 \(1,2,5,10\)。这里G条件确实区分可解与不可解输入，不是自动成立的条件。

按照[临界尺度报告](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md)中排除自动G维数的定义，
\[
H(6)=\min\{n>6:\mathcal P(6,n),\ \operatorname{rad}(n)\nmid6\},
\]
本定理给出
\[
\boxed{H(6)=10.}
\]
七、八元存在G=1反例，九元的G条件自动成立，故它们不能提供更早的非自动算术成功点。

这不是 \(N(6)=9\) 或 \(N(6)=10\) 的证明；六平均十一元等后续维数仍需解决。

## 2. 必要性及真实的两类非法输入

若 \(5\mid G\)，本原性使所有坐标模5等于同一个非零值。六在模5下可逆，每次六平均保持此共同值，故不可能归零。

两类实际例子为
\[
(1^9,-9),\qquad G=10;
\]
\[
(1^6,6^3,-24),\qquad G=5.
\]
它们都本原、零和，且全部坐标模5等于1。

因此只需证明 \(G=1\) 与 \(G=2\) 的充分性。后者不能被误排除：2是六平均允许的分母素数。

## 3. 两步进入合法 \((6,3,1)\) 核

给定合法本原 \(X\)，其坐标模5不全相同。选两个模5不同的位置，再选两个位置，组成四元补集。平均其余六项，记新均值为a，补集四项记为b,c,d,w。

补集不全同余，故可选择其中一项作为w，使
\[
w\not\equiv a\pmod5.
\]
接着取三份a与b,c,d做第二次六平均。输出六份
\[
u=\frac{3a+b+c+d}{6}=\frac{-3a-w}{6},
\]
留下三份 \(v=a\) 与单点w，于是进入
\[
K(u,v)=(u^6,v^3,-6u-3v).
\tag{2}
\]
并且
\[
u-v=\frac{-9a-w}{6}\equiv\frac{a-w}{6}\ne0\pmod5.
\tag{3}
\]
所有分母仅含2、3，因此模5运算合法。

用参数
\[
(x,y)=(u,u-v).
\]
将参数清分母并本原化后有
\[
G(K)=\gcd(y,10).
\tag{4}
\]
因为 \(\gcd(u,v)=1\)，而单点与u的差为
\[
-7u-3v=-10u+3y.
\]
所以合法核心参数正好满足 \(5\nmid y\)，不要求y为奇数。这正是选择 \(\Gamma_0(5)\) 而非强加模10单位条件的原因。

## 4. 四个明确的原位置宏

定义三个一步宏A、B、C，以及一个两步宏R。每个宏完成后重新登记六重块、三重块与单点的位置。

| 宏 | 选取方式 | 新六重值 \(u'\) | 新三重值 \(v'\) | 新单点 |
|---|---|---|---|---|
| A | \(u^3,v^3\) | \((u+v)/2\) | u | 原单点w |
| B | \(u^5,w\) | \((-u-3v)/6\) | v | u |
| C | \(u^3,v^2,w\) | \((-3u-v)/6\) | u | v |

两步宏R：

1. 选择 \(u^4,v,w\)，得到六份 \(t=-(u+v)/3\)，余下两份u、两份v。
2. 选择三份t、一份u、两份v，得到六份 \(v/6\)，余下三份t与一份u。

因此R的输出为
\[
(u',v',w')=\left(v/6,-(u+v)/3,u\right).
\]

在 \((x,y)\) 上的**实际矩阵**为
\[
A=\frac12\begin{pmatrix}2&-1\\0&-1\end{pmatrix},
\quad
B=\frac16\begin{pmatrix}-4&3\\-10&9\end{pmatrix},
\]
\[
C=\frac16\begin{pmatrix}-4&1\\-10&1\end{pmatrix},
\quad
R=\frac16\begin{pmatrix}1&-1\\5&-3\end{pmatrix}.
\tag{5}
\]
不是只在射影意义下定义这些原子矩阵；下文会明确区分实际尺度与射影实现。

所有矩阵模5可逆，并将y乘以模5单位，故保持合法核心。R的第一步还在补集中留两份u和两份v，保留模5不同余；第二步的输出合法性由矩阵R保证。因此中间位置也没有隐藏的同余破坏。

## 5. 三条实际周期给出全部正向逆

直接计算：
\[
\boxed{
R^4=-\frac1{324}I,\quad
(AR)^2=\frac1{36}I,\quad
(RAC)^2=\frac1{216}I.
}
\tag{6}
\]
例如
\[
RAC=\begin{pmatrix}-1/9&1/36\\-5/18&1/9\end{pmatrix}
\]
迹为0、行列式为 \(-1/216\)，其平方即为第三式。

矩阵乘积按右侧先执行。式(6)分别给出以下正向射影逆词：
\[
R^{-1}\sim R^3,\qquad
A^{-1}\sim RAR,\qquad
C^{-1}\sim(RA)C(RA).
\tag{7}
\]
这些词全部由真实原子组成，不反向执行平均。

再计算
\[
\Sigma=C^{-1}B=
\begin{pmatrix}1&-1\\0&-1\end{pmatrix},\qquad \Sigma^2=I.
\tag{8}
\]
所以 \(\Sigma\) 及其逆也有正向实现，\(B=C\Sigma\) 随之可逆。

**六重块和三重块不能免费交换名称。** 此处的 \(\Sigma\) 由C的正向逆词与B实际执行出来，承担了真正的物理操作。共同缩放只用于描述作用，不被当成额外许可操作。

周期的发现经过一个小型返回表：枚举19个合法的一步／两步核心返回，再检查其单个及两两乘积的有限阶。它找出了R与三条显示恒等式；正式证明和核验器不再依赖搜索。

## 6. 从周期到正确的模5根

写
\[
U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},\quad
L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix},\quad
\Delta(t)=\operatorname{diag}(1,t).
\]
有
\[
\Sigma A=\Delta(1/2).
\]
因A和 \(\Sigma\) 都正向可逆，\(D=\Delta(2)\) 及逆可执行。进一步，
\[
\Sigma D\Sigma D^{-1}=U(1/2),
\tag{9}
\]
其平方为U(1)，共轭与整数次幂产生全部二进上根；\(\Sigma U(1)=\Delta(-1)\) 给出符号单位。

现在构造下根，而不把任何尚未实现的除法当操作。令
\[
F=U(-1)C=
\begin{pmatrix}1&0\\-5/3&1/6\end{pmatrix}.
\tag{10}
\]
F及其逆都已正向可执行。其交换子精确为
\[
\boxed{DFD^{-1}F^{-1}=L(-5/3).}
\tag{11}
\]
故把这个已实现下根的逆执行三次，就得到
\[
L(5)=L(-5/3)^{-3}.
\tag{12}
\]
这一步才真正给出模5的根，不需要额外要求模2单位。

事实上，
\[
L(5/3)F=\Delta(1/6)
\]
还能给出 \(\Delta(3)^{\pm1}\)。因此完整的正向资源为
\[
\boxed{
U(\mathbb Z[1/6]),\quad
L(5\mathbb Z[1/6]),\quad
\Delta(\mathbb Z[1/6]^\times).
}
\tag{13}
\]
后面的整数群覆盖只需要其中的二进单位子集。

## 7. 六个陪集、十八条回路完成 \(\Gamma_0(5)\)

取
\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad T=U(1).
\]
\(\mathbf P^1(\mathbb F_5)\) 有六个点，采用代表
\[
Q_j=ST^j,\qquad j\in\{0,\pm1,\pm2\},\qquad Q_\infty=I.
\tag{14}
\]

右乘T或T逆时，有限图的回路为
\[
L(-(j+\epsilon-j')),\qquad j'\equiv j+\epsilon\pmod5,
\]
因此属于 \(L(5\mathbb Z)\)。右乘S且 \(j\ne0\) 时，取代表 \(k\equiv-j^{-1}\pmod5\)，回路为
\[
\begin{pmatrix}-k&-1\\jk+1&j\end{pmatrix}.
\tag{15}
\]
其主元 \(-k\) 只有 \(\pm1,\pm2\)。其余回路为 \(\pm I\) 或 \(U(\pm1)\)。

对左下项被5整除、左上项为二进单位的行列式一矩阵，Gauss分解为
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=L(c/a)\operatorname{diag}(a,a^{-1})U(b/a).
\tag{16}
\]
全部因子均由(13)实现。因此六个陪集的十八条S、T、T逆回路全部是正向可执行宏。

由Schreier生成定理，
\[
\boxed{\Gamma_0(5)\text{ 的全部射影作用均可由真实六平均实现。}}
\tag{17}
\]
陪集代表本身没有被当成许可操作；只编译其闭合回路。这是无限整数群的包含，不只是模5的有限群像计算。

## 8. 覆盖两种合法G类并终止

给定本原合法参数 \((x,y)\)，只知 \(\gcd(x,y)=1,\ 5\nmid y\)，y可以为偶数。取
\[
\alpha x+\beta y=1.
\]
再令
\[
(\alpha,\beta)\mapsto(\alpha+ky,\beta-kx)
\]
使 \(5\mid\alpha\)。于是
\[
H=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}\in\Gamma_0(5),
\qquad H(x,y)^T=(0,1)^T.
\tag{18}
\]
Euclid算法给出有限S、T、T逆词，按第7节编译为正向宏。输出必到达
\[
K(0,v)=(0^6,v^3,-3v).
\]
最后选择三份v、单点 \(-3v\) 与两个零，六平均一次，全部归零。

入口、核心控制和终端连接，完成(1)的充分性。全过程保持原十个位置；不调用九元无条件平均作为未经检查的子问题，也不增加副本。

## 9. 为什么这比“九元无条件成立”提供了更多算术信息

十元真正暴露了危险素数5以及允许的素因子2：

- \(G=1\) 和 \(G=2\) 都必须覆盖；
- \(G=5\) 和 \(G=10\) 必须排除；
- 控制器的自然同余层是 \(\Gamma_0(5)\)，不是直接把总维数10写进 \(\Gamma_0(10)\) 后强迫y为模10单位；
- 一步宏未给出所需周期，两步返回R补齐了正向实现；
- 下根 \(L(-5/3)\) 的真实交换子把允许分母与危险素数明确分开。

因此这一结果符合“G条件真正起筛选作用”的研究标准，也验证了六平均在非自动算术下边缘10的猜想。

剩余的六平均候选临界维数是11、13、14、16、17、19、20、22、23。最终阈值仍只知 \(9\le N(6)\le24\)，不能由九、十元都成功便直接宣称所有 \(n\ge9\) 成功。

## 10. 核验、发现记录及长度边界

正式入口：

~~~text
python work/run_verifications.py --id six-average-ten-complete
~~~

[正式核验器](../work/verify_six_average_ten_complete.py)不导入发现表，只使用显示的四个宏、精确周期和交换子。它检查：

- 四个宏在两个基参数上的原位置实现，共8项；
- 实际尺度的三条周期、下根交换子以及 \(\Delta(3)\)；
- 全部24个本原模5行及18条完整Schreier回路；
- 全部196种非恒定、零和的模5余数多重集入口；
- \(G=1,G=2\) 各60个80位大整数入口与Bezout；
- 两类G各3条随机筛选完整原位置路径，并另从原始输入以Fraction独立重放；
- 两个 \(G=5,10\) 非法例子的非零模5余类。

输出：

~~~text
six-average n10 actual periods and complete Gamma0(5): PASS 8 24 18
six-average n10 complete residue entries and both legal G classes: PASS 196 60 60
six-average n10 literal full paths and excluded classes: PASS 6 1931 2
six-average ten-position full G criterion: PASS
~~~

[完整原始输入与1基操作序列](../work/six_average_ten_witnesses.json)保留全部六个成功实例和两个非法例子。1931步是本次直接编译器的最长样本，不是最短长度或普遍上界；大整数入口检查未展开所有长词。本文只证明有限构造，没有新增统一多项式路径长度或一位额外精度结论。

[两步返回发现程序](../work/explore_six_average_ten_macros.py)及[发现表](../work/six_average_ten_macro_discovery.json)独立保留以便溯源。最初三个一步宏的深度9诊断未发现有限周期，仅说明该有界搜索未命中；它没有被当成无周期或不可达证明。正式结论完全由以上显示恒等式、完整群覆盖和原位置重放承担。

<!-- END SOURCE doc-11fc9beac1cb -->

---

<a id="doc-342d5ac6c14f"></a>

## 原文导签：平方元数的统一正向控制器与九平均十三元

来源：`work/document_reorganization_20260915/originals/outputs/square_arity_uniform_controller_and_nine_thirteen.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/square_arity_uniform_controller_and_nine_thirteen.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-342d5ac6c14f -->
# 平方元数的统一正向控制器与九平均十三元

日期：2026-09-15。本页接已有[四平均七元证明](../sources/work/document_reorganization_20260915/originals/outputs/four_average_seven_complete.md)，将其中的实际周期推广成一个参数恒等式，再利用新近成熟的深同余取逆工具，完成原合数临界猜想中尚未证明的九平均十三元。

**后续入口已补齐：** [规划建议第2节](../sources/work/document_reorganization_20260915/originals/outputs/general_k_plan_review_and_square_entry_20260915.md)对全部t>=2给出从任意合法输入到(t²,t,1)核心的完整原位置入口，经[复核](../sources/work/document_reorganization_20260915/originals/outputs/general_k_review_response_20260915.md)确认。一般平方族现在仍缺的是H_t的尺度覆盖；本页第8节保留九平均的简短入口。

**文献后续：** [H_t调查](../sources/work/document_reorganization_20260915/originals/outputs/ht_literature_and_eventual_square_completion_20260915.md)已无条件完成全部充分大的t、全部n为素数的t以及2<=t<1000。因此本页控制器与共同入口已给这些参数的完整维数判据。GRH下全部t成立；无条件全t尚未证明，N(t²)仍不能由单维数结论推出。

## 1. 结论和范围

**定理A：统一控制器。** 对每个整数 t>=2，令
\[
q=t^2,\qquad n=t^2+t+1.
\]
全系统核心
\[
K_t(u,v)=(u^{t^2},v^t,-t^2u-tv)
\tag{1.1}
\]
有三个真实一步宏，其正向标量周期对所有 t 恒成立。它们提供实际双向上根
\[
U((t-1)\mathbb Z[1/t])
\]
以及可执行主同余群
\[
\Gamma((t-1)^2n^3,\mathbb Z[1/t]).
\tag{1.2}
\]
若 t 为奇数，另有不依赖搜索的原位置除二构造；t偶时用已取得深层的安全取逆引理。因此对**所有整数t>=2**均可取得
\[
U(R),\quad L(nR),\quad R=\mathbb Z[1/(2t)].
\tag{1.3}
\]
这里的所有t推广由第6节补充的一个新交换子完成。此前仅写“t-1是2幂”过于保守：获得除二后，应该重新用Sigma取交换子，而不只是扩张旧根的分母环。

**定理B：九平均十三元。** 对任意十三个有理数，有限次原位置九平均可达全等，当且仅当非全等输入的本原中心化差分 gcd 为 G=1。因此
\[
\boxed{M(9)=H(9)=13.}
\tag{1.4}
\]
下界使用已有[合数临界尺度反例](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md)。本页不证明 N(9)=13，不证明九平均所有 n>=13；也不把定理A的核心群控制称为全部平方元数的临界全输入定理。

群论步骤沿用 Morris 2007 定理6.1(2)、Serre 强同余子群性质、深主同余及安全整数返回取逆引理；准确来源与适用环见[外部审核](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_lower_band_external_theorems_audit_20260915.md)。没有新的无限群假设。

## 2. 三个真实宏与正确尺度

记 w=-t²u-tv，使用坐标
\[
(x,y)=(u,u-v).
\]
取整数本原代表时有
\[
G(K_t)=\gcd(y,n),\qquad\gcd(x,y)=1.
\tag{2.1}
\]
因为 u、v 本身就是实际块值，所以本原性等价；第三个差为 w-u=-nx+ty，故式(2.1)成立。

三个实际一步宏为：

| 宏 | 选取的 q=t² 个位置 | 新 t 重值 | 新单点 |
|---|---|---|---|
| A | u^(q-t), v^t | 旧u | 旧w |
| B | u^(q-1), w | 旧v | 旧u |
| C | u^(q-t), v^(t-1), w | 旧u | 旧v |

每行选后恰留下 t 个同值位置和一个单点；索引只是更新角色，不免费交换不等大小块。实际矩阵是
\[
\mathcal A=\frac1t A,\quad
\mathcal B=\frac1{t^2}B,\quad
\mathcal C=\frac1{t^2}C,
\]
\[
A=\begin{pmatrix}t&-1\\0&-1\end{pmatrix},\quad
B=\begin{pmatrix}-t-1&t\\-n&t^2+t\end{pmatrix},\quad
C=\begin{pmatrix}-t-1&1\\-n&1\end{pmatrix}.
\tag{2.2}
\]
每个矩阵的行列式在 ell|n 处为单位，且下行第一项被 n 整除、第二项为单位，因此保持合法性。

## 3. 平方结构直接给出周期，不是逐参数种子

矩阵 C 的迹为 -t，行列式为 t²，Cayley--Hamilton 给
\[
C^2+tC+t^2I=0,\qquad C^3=t^3I.
\]
另有
\[
\operatorname{tr}(CA)=0,\quad \det(CA)=-t^3,
\qquad C^2B=t^3\Sigma,
\quad \Sigma=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
\]
所以在**实际尺度**上
\[
\boxed{
\mathcal C^3=t^{-3}I,\quad
(\mathcal C\mathcal A)^2=t^{-3}I,\quad
\mathcal C^2\mathcal B=t^{-3}\Sigma.}
\tag{3.1}
\]
C 的逆由 C²提供；CA的周期提供 A的逆；Sigma²=I再提供B的逆。全部都是原位置正向词乘非零全局共同尺度。

这正是四平均七元原证明的三个周期，只需把 t=2 改成任意 t。此前局部研究把这些恒等式用于特定元数；这里利用的是其完整参数结构。

## 4. 统一根和明确深同余层

置 Delta(d)=diag(1,d)。由(2.2)、(3.1)，
\[
\Sigma\mathcal A=\Delta(1/t),\qquad
D:=\Delta(t)
\]
及其逆均可执行。直接有
\[
\Sigma D\Sigma D^{-1}=U((t-1)/t).
\tag{4.1}
\]
D 的双向共轭和根的加法给出 U(hR0)，h=t-1，R0=Z[1/t]。

取仅用于证明的有理换基
\[
P=(e_1,Ce_1)=\begin{pmatrix}1&-t-1\\0&-n\end{pmatrix}.
\]
则
\[
P^{-1}U(a)P=U(-na),\qquad
P^{-1}C U(t^2a)C^{-1}P=L(na).
\tag{4.2}
\]
所以 P 基下已有双向 nhR0 根。深同余引理给 Gamma(n²h²,R0)；回到原基时，nP^-1 和 P 均在 R0 中，故得到
\[
\Gamma(n^3h^2,R_0).
\]
这里 P 自身不必可执行；多乘的一次 n 正是换基清分母的账本。

## 5. 一个统一两步返回提供正向整数倍率

对0<=j<=t-1，先平均
\[
(u^{t^2-j-1},v^j,w),
\]
得到 t² 份新 D。保留其中 t 份作为新 t 块，再保留一份未参与首步的旧u作单点；平均其余 t² 个位置。

第一次外面有 j+1 份旧u，故所需单点总存在。所得实际矩阵为
\[
\mathcal M_j=\frac1{t^3}
\begin{pmatrix}1&j-t\\n&(t+1)(j-t)\end{pmatrix}.
\tag{5.1}
\]
整数代表 M0 的行列式是 t³，和初始控制层 n³(t-1)² 互素。因此已有主同余群先给 M0 的真实正向逆，不能反过来预设所有 Mj 可逆。

精确关系为
\[
M_0^{-1}M_j=\Delta((t-j)/t).
\tag{5.2}
\]
接 D=Delta(t)，得到全部正向 Delta(d)，1<=d<=t。这里暂不宣称这些倍率的逆全部存在。

## 6. t 为奇数时，除二有显式夹乘

取d=2。已由第5节取得 D2=Delta(2) 的正向实现。因为t奇，
\[
H=\frac1{2t}D_2 C D_2
=\begin{pmatrix}
-(t+1)/(2t)&1/t\\-n/t&2/t
\end{pmatrix}
\in\mathrm{SL}_2(R_0).
\tag{6.1}
\]
注意(t+1)/2是整数，所以 H 的条目还未使用1/2。H 是实际正向词的非零共同尺度代表；有限逆提升引理以已有 Gamma(n³h²,R0) 提供 H^-1。

而
\[
\boxed{C D_2 H^{-1}=2t D_2^{-1}.}
\tag{6.2}
\]
这给出真正的原位置除二，尽管初始同余层可能被2整除。不能用“行列式与控制层互素”的取逆引理直接处理 D2；式(6.1)正是绕过该限制的关键。

若t偶，则初始控制层n³(t-1)²为奇数。第5节已有实际D2，故安全整数返回取逆引理直接提供D2^-1。两种奇偶分支由此都取得D2及其正向逆。

现在应重新形成交换子，而不仅仅对原U((t-1)R)扩环：
\[
\boxed{\Sigma D_2\Sigma D_2^{-1}=U(1/2).}
\tag{6.2a}
\]
所以对全部t>=2，整数次幂及Delta(2)、Delta(t)的双向共轭给出U(R)，R=Z[1/(2t)]。这里没有任何剩余的t-1奇因子条件。再用
\[
\boxed{U(-1)\mathcal C\Delta(t^2)=L(-n/t^2)}
\tag{6.3}
\]
取得L(nR)。Sigma U(1)=Delta(-1)也提供符号倍率。

此时旧[Gamma1精确生成引理](../sources/work/document_reorganization_20260915/originals/outputs/prime_arity_endpoint_congruence_completion.md)第4节可以使用：已有的U(Z[1/2])和L(nZ[1/2])至少生成Gamma1(n,Z[1/2])。不必再额外证明一般R版本。

## 7. t=3：完整闭合九平均十三元

此时q=9,n=13,t-1=2。前面已经提供全部双向U(Z[1/6])、L(13Z[1/6])，以及Delta(2)、Delta(3)、Delta(-1)和逆。因此至少有Gamma1(13,Z[1/2])的全部作用。

2的模13阶恰为12：2⁶=-1 mod13，且2⁴=3不等于1、2³=8不等于1。因此每个模13单位都有一个2幂提升。

给定本原合法整数(x,y)，13不整除y。取alpha x+beta y=1，调整使alpha=0 mod13；于是
\[
F=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}
\in\Gamma_0(13,\mathbb Z),\qquad F(x,y)^T=(0,1)^T.
\]
选epsilon=2^k=y mod13。则
\[
\operatorname{diag}(\epsilon^{-1},\epsilon)F
\in\Gamma_1(13,\mathbb Z[1/2]).
\]
对角矩阵射影上是已可执行的Delta(epsilon²)，故F也可执行。这一论证同时处理全部有理合法输入，未枚举高度或平均词。

终端(x,y)=(0,1)对应(0^9,(-1)^3,3)。取三份-1、一份3和五个零作一次九平均，十三个位置全部变零。

## 8. 九平均十三元的全输入入口

中心化、本原化输入为十三元整数零和向量。G=1时存在两个模13不同的位置。取包含它们的四元补集，先平均其余九项，得到九份a。

补集模13不全同，故有一个位置w与a不同余。保留w；平均六份a和补集中另外三项，留下三份旧a。由总和为零，输出(u^9,v^3,w)，其中v=a，并且
\[
u-v=\frac{-12a-w}{9}=\frac{a-w}{9}\pmod{13}\ne0.
\]
所以两次真实平均进入合法(9,3,1)核心，第7节完全归零。G=13时共同非零余类不变量排除可达。结合10至12元的已有反例，定理B得证。

## 9. 结构意义和尚缺的推广

当t为素数幂时，有限射影平面PG(2,t)有t²+t+1个点；点在线上的一个旗标将点集分成t²个线外点、t个线上其余点和一个指定点。它与(1.1)的三块大小相同，且n=Phi3(t)。式C²+tC+t²I=0确实给出了三阶循环结构。

不过本页的实际证明不使用射影平面的存在性，计数公式对任意整数t均成立。因此目前已经建立的是**统一块计数与三阶矩阵恒等式**；尚未证明某个完整射影平面群作用都能由平均实现，不能只凭相同点数就借用整个群的工具。

对t=ell^a，q=t²的旧下界恰是q+t+1；因此这里的形状符合素数偶次幂的真实临界尺度。对一般合数t，S(t²)可能严格小于t，(1.1)不一定在最优边界。

下一层明确障碍为：

1. 一般n=t²+t+1为合数时，全输入合法入口已由上述后续补齐。当前需证明H_t=<-1,d模n:1<=d<=t,gcd(d,n)=1>为完整单位群，或增加能跨越其缺失类的真实返回。
2. 第5节Delta(d)在1<=d<=t时已经正向存在。现有Gamma1包含Gamma(n)，所以gcd(d,n)=1时其逆可直接激活；这提供全部不大于t且不除n的小素数分母。尚不能未经证明就说这些实际单位模n满射。
3. 现有一步零和终端的本原y尺度全部位于H_t，不能单靠多列同形终端补齐H_t外的类。即使临界点完成，也不自动给出之后全部维数，M、H与N必须继续区分。

原先列出的“t-1奇因子仍阻止取得完整根”已由(6.2a)消除，不应再作为后续待证引理。与之不同，允许分母模n的单位像仍是需证明的独立量词。

## 10. 核验

[精确核验](../work/verify_square_arity_controller_and_nine_thirteen.py)不搜索平均词。它检查200个参数的通用周期、深层换基、奇偶除二接口及新交换子的完整根恒等式；72条原位置标量闭路／两步返回；100个九平均十三元入口和152个精确Gamma1及终端接口。一般量词由正文承担，不由参数样本外推。核验没有展开Morris/Serre产生的一般群词。

核验ID：square-arity-controller-nine-thirteen。

<!-- END SOURCE doc-342d5ac6c14f -->

---

<a id="doc-016b9066b0a0"></a>

## 原文导签：十平均十六元与一族确定性三块网络

来源：`work/document_reorganization_20260915/originals/outputs/ten_average_sixteen_and_dyadic_network_family.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/ten_average_sixteen_and_dyadic_network_family.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-016b9066b0a0 -->
# 十平均十六元与一族确定性三块网络

日期：2026-09-15。本页处理混合元数任务中的自动G点，保留一般k主线的GRH假设；本页构造本身是无条件的线性恒等式，不研究GRH的去除。

## 1. 定理

**定理。** 对每个整数b>=1，令
\[
m=2b,\quad n=2^m=4^b,\quad h=(n-1)/3,\quad k=2h.
\]
任意n个实数都有同一个包含m+2=2b+2次原位置k平均的全平均网络。

特别地，k=10、n=16由固定六步网络完全解决。接[旧临界下界](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md)及十七元定理，得到
\[
\boxed{M(10)=16,\qquad H(10)=17.}
\]
N(10)=16仍未证明。这里不声称六步最短。

## 2. 两步进入三个h块加单点

先平均任意k=2h个原位置，得到2h份a；其余h+1个位置保持原值。再平均h-1份a与这h+1个位置，产生2h份b_value，留下h+1份a。

从后者留一份a作单点，其余分成一个h块。新b_value分成两个h块。于是整个系统为
\[
(a^h,b_{\rm value}^h,b_{\rm value}^h,a),
\]
总均值是
\[
\mu=\frac{(h+1)a+2h b_{\rm value}}{3h+1}.
\]
没有额外复制，所有块均由前两次实际平均得到。

## 3. 循环二块平均的精确误差

每次把两个h块合并做一次k平均，恰在三个块的值上执行二平均。依次选块对(0,1)、(1,2)、(2,0)，循环进行。

把a记为系数1、b_value记为系数0。第j次二块平均的新值系数为
\[
c_j=\frac{1-(-1/2)^j}{3},\qquad c_0=0.
\]
每次输出两个h块为c_j，另一个块为c_(j-1)；前一步的配对给递推c_j=(c_(j-1)+c_(j-2))/2，初值c_1=1/2。故上式对所有j成立。

取j=m-1。m偶，所以j奇，
\[
c_{m-1}=\frac{1+2^{1-m}}3
=\frac{h+1}{3h+1}.
\]
这恰为总体均值中a的系数。因此m-1次二块平均后，已有2h份值mu；剩下h块及单点的总和由全局总和保证为(h+1)mu。

最后取这h+1个位置，再加h-1份已经等于mu的位置，恰好2h个，平均一次。全部n项等于mu。总次数2+(m-1)+1=m+2。

这是三块收缩误差与单点权重精确匹配的构造，整个过程中单点直到最后才参与，但最后一步严格核对了全局均值；没有把局部均值误当总体目标。

## 4. 十平均十六元的明确索引

以下位置为1基。依次十平均：

```
1,2,3,4,5,6,7,8,9,10
1,2,3,4,11,12,13,14,15,16
5,6,7,8,9,1,2,3,4,11
1,2,3,4,11,12,13,14,15,16
12,13,14,15,16,5,6,7,8,9
1,2,3,4,11,10,5,6,7,8
```

其后三次块混合依次产生(a+b)/2、(a+3b)/4、(3a+5b)/8；最后一个值就是6份a与10份b的总体均值。

## 5. 证据与范围

[核验](../work/verify_dyadic_three_block_fixed_network.py)对b=1、2、3的全部84个标准基重放固定网络，确认整个矩阵为J_n/n；另检查40组精确递推恒等式。没有搜索原子词或用样本外推固定网络。

其他参数给42平均64元、170平均256元等自动G维数。这些是整族结果，但不保证每个点都在各自的最早边界。十平均十六元恰与旧下界相接，是本页新增的最早成立结论。

<!-- END SOURCE doc-016b9066b0a0 -->

---

<a id="doc-efc595179bd5"></a>

## 原文导签：十平均与十二平均17元完整G判据，以及原B公式中的自动维数

来源：`work/document_reorganization_20260915/originals/outputs/ten_twelve_average_seventeen_complete.md` · [逐字节原样副本](../sources/work/document_reorganization_20260915/originals/outputs/ten_twelve_average_seventeen_complete.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-efc595179bd5 -->
# 十平均与十二平均17元完整G判据，以及原B公式中的自动维数

日期：2026-09-12。按用户要求，以G条件确实筛选输入且等价于可达性为研究目标。本文证明十平均17元、十二平均17元的完整判据，得到 \(H(10)=H(12)=17\)。十平均16元的全部输入可达性不由本文证明；其G自动合法不能代替这个数学问题。

## 1. 原来的B(q)中，哪些点自动满足G条件

此前定义
\[
S(q)=\max_{p^a\parallel q}p^{\lceil a/2\rceil},\quad t=q+S(q),
\]
\[
B(q)=
\begin{cases}
t,&\operatorname{rad}(t)\mid q,\\
t+1,&\operatorname{rad}(t)\nmid q.
\end{cases}
\tag{1}
\]
因为总有 \(G\mid n\)，原B(q)点的G条件自动成立当且仅当
\[
\boxed{\operatorname{rad}(B(q))\mid q.}
\tag{2}
\]

这里有两种来源：

- 原边界t本身只含允许素因子，因此B=t；
- 原边界t被反例排除，B=t+1恰好又只含允许素因子。例如q=10、12时，t=15，B=16，G条件仍然自动成立。

因此不能只把旧公式中“加0”的点视为自动点；“加1”的点也必须重新检查。

在之前重点讨论的元数表中，自动点为
\[
2\to4,\ 6\to9,\ 10\to16,\ 12\to16,\ 20\to25,\ 30\to36,
\]
\[
42\to49,\ 56\to64,\ 120\to125.
\tag{3}
\]
若完整检查 \(2\le q\le200\)，全部17项为：

| q | B(q) | B(q)分解 |
|---:|---:|---|
| 2 | 4 | \(2^2\) |
| 6 | 9 | \(3^2\) |
| 10 | 16 | \(2^4\) |
| 12 | 16 | \(2^4\) |
| 20 | 25 | \(5^2\) |
| 30 | 36 | \(2^2 3^2\) |
| 42 | 49 | \(7^2\) |
| 54 | 64 | \(2^6\) |
| 56 | 64 | \(2^6\) |
| 75 | 81 | \(3^4\) |
| 90 | 96 | \(2^5 3\) |
| 110 | 121 | \(11^2\) |
| 120 | 125 | \(5^3\) |
| 132 | 144 | \(2^4 3^2\) |
| 138 | 162 | \(2\cdot3^4\) |
| 156 | 169 | \(13^2\) |
| 182 | 196 | \(2^2 7^2\) |

本表只断言G条件对全部输入自动满足，**不同时断言这些维数全部可达**。有固定网络证明的点须另引用相应定理；未证明的点不能因为出现在表中便算作成功。

按现在的非自动G标准，候选下边缘应写为
\[
C(q)=\min\{n>q+S(q):\operatorname{rad}(n)\nmid q\}.
\tag{4}
\]
已有反例下界保证 \(H(q)\ge C(q)\)，等号一般仍为猜想。对q=10、12，两者均有 \(C(q)=17\)，以下完成这两个等号。

## 2. 主定理与量词

给定17个有理数，中心化、清分母并本原化为非零整数零和X，记
\[
G(X)=\gcd_{i<j}|X_i-X_j|.
\]
则分别有
\[
\boxed{
X\text{ 可有限步十平均归零}\iff G=1,
}
\]
\[
\boxed{
X\text{ 可有限步十二平均归零}\iff G=1.
}
\tag{5}
\]
全等输入允许空词。

因为 \(G\mid17\)，G只有1与17两种可能；17既不整除10，也不整除12。因此(5)分别等价于原猜想的
\[
G=2^a5^b,\qquad G=2^a3^b.
\]
没有修改一般G判据，只是在17元上简化。

[临界尺度下界](../sources/work/document_reorganization_20260915/originals/outputs/composite_critical_scale_and_conjecture.md)排除了十平均11至15元以及十二平均13至15元的全称G充分性；16元G自动满足，被H的定义排除。故
\[
\boxed{H(10)=H(12)=17.}
\tag{6}
\]
这不证明最终阈值N，也不证明所有 \(n\ge17\) 都成立。

## 3. 两种平均共用的合法入口

取q=10或12，\(r=16-q\)，核心形状为
\[
K_q(u,v)=(u^q,v^r,-qu-rv).
\tag{7}
\]
所以两个权重分别是(10,6,1)与(12,4,1)。

对任意本原G=1输入，找两个模17不同的位置，将它们放进一个r+1元补集。平均其余q项，得到q份a；补集模17不全相同，故有单点w满足 \(w\not\equiv a\pmod {17}\)。

接着取q-r份a和补集中除w外的r项，做第二次q平均，得到q份u；留下r份v=a与w。利用总和零，
\[
u-v=\frac{-16a-w}{q}\equiv\frac{a-w}{q}\ne0\pmod {17}.
\tag{8}
\]
所以合法入口至多两步完成。所有分母只含q的素因子，模17运算有效。

差坐标取
\[
(x,y)=(u,u-v).
\]
参数本原整数化后，
\[
G(K_q)=\gcd(y,17).
\tag{9}
\]
因为单点与u的差为 \(-(q+1)u-rv=-17u+ry\)，且 \(\gcd(u,v)=1\)。因此核心合法域为
\[
\gcd(x,y)=1,\qquad17\nmid y.
\tag{10}
\]

## 4. 一类真实两步返回模板

从(7)中先平均指定的q个位置，得到q份t。随后保留其中r份t，以及一个**没有参加第一步**的旧值z作为单点，再平均其余q个位置。输出核心为
\[
u'=-\frac{rt+z}{q},\qquad v'=t,\qquad w'=z.
\tag{11}
\]
这完整说明原位置如何选；并不增加副本。下面每个模板第一步外面都确实剩有所要求的z，且q≥r，所以保留r份t有足够位置。

### 十平均模板

此处r=6、\(w=-10u-6v\)。

| 名称 | 第一次选取 | 保留的旧单点z | 次数 |
|---|---|---|---:|
| R | \(u^5,v^4,w\) | u | 2 |
| P | \(u^7,v^2,w\) | u | 2 |
| H | \(u^4,v^5,w\) | u | 2 |
| S | \(u^8,v,w\) | v | 2 |
| E | \(u^8,v^2\) | u | 2 |
| B | 直接平均 \(u^9,w\)，留下v块与一份u | u | 1 |

在(x,y)坐标上的实际矩阵为
\[
R=\frac1{50}\begin{pmatrix}16&-6\\51&-16\end{pmatrix},\quad
P=\frac1{50}\begin{pmatrix}16&-12\\51&-32\end{pmatrix},
\]
\[
H=\frac1{50}\begin{pmatrix}16&-3\\51&-8\end{pmatrix},\quad
S=\frac1{50}\begin{pmatrix}16&-10\\51&-35\end{pmatrix},
\]
\[
E=\frac1{50}\begin{pmatrix}-35&6\\-85&16\end{pmatrix},\quad
B=\frac1{10}\begin{pmatrix}-7&6\\-17&16\end{pmatrix}.
\tag{12}
\]

### 十二平均模板

此处r=4、\(w=-12u-4v\)。

| 名称 | 第一次选取 | 保留的旧单点z | 次数 |
|---|---|---|---:|
| R | \(u^9,v^2,w\) | u | 2 |
| P | \(u^{11},w\) | u | 2 |
| H | \(u^8,v^3,w\) | u | 2 |
| S | \(u^{10},v,w\) | v | 2 |
| A | 直接平均 \(u^8,v^4\)，留下四份u和原单点 | 原w | 1 |

实际矩阵为
\[
R=\frac1{36}\begin{pmatrix}2&-2\\17&-8\end{pmatrix},\quad
P=\frac1{36}\begin{pmatrix}2&-4\\17&-16\end{pmatrix},
\]
\[
H=\frac1{36}\begin{pmatrix}2&-1\\17&-4\end{pmatrix},\quad
S=\frac1{36}\begin{pmatrix}2&0\\17&-9\end{pmatrix},
\]
\[
A=\begin{pmatrix}1&-1/3\\0&-1/3\end{pmatrix}.
\tag{13}
\]

所有表中矩阵模17可逆，并保持 \(17\nmid y\)。第一步若产生局部非法状态，就不可能经过后续q平均恢复为合法状态；也可直接检查保留的旧块见证。因此模板在合法核心上没有隐藏的中途非法调用。

## 5. 共用的正向二进资源

矩阵乘积按右侧先执行。用 \(\sim\) 表示相差非零全局共同标量；实际值从不物理缩放。

精确周期为
\[
q=10:\qquad R^2=-\frac1{50}I,\qquad(RE)^2=\frac1{2500}I;
\tag{14}
\]
\[
q=12:\qquad R^4=-\frac1{5184}I.
\tag{15}
\]
故R的射影逆均由正向词实现，十平均的E也由 \(RER\) 实现射影逆。

两种模板均满足
\[
R^{-1}P=\Delta(2),\qquad R^{-1}H=\Delta(1/2),\qquad
R^{-1}S=\Sigma,
\tag{16}
\]
其中
\[
\Delta(t)=\operatorname{diag}(1,t),\qquad
\Sigma=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
\]
两个相反倍率的实际正向存在一起保证 \(\Delta(2)\) 可逆；\(\Sigma^2=I\) 保证它也可逆。**两种不等大小块不能免费交换**，这里的 \(\Sigma\) 是实际返回词。

令D=\(\Delta(2)\)，则
\[
\Sigma D\Sigma D^{-1}=U(1/2),\qquad
U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix}.
\tag{17}
\]
取幂和共轭得到全部 \(U(\mathbb Z[1/2])\) 与逆；\(\Sigma U(1)=\Delta(-1)\) 给出符号。

## 6. 一个共同的交换子机制产生下根

若已有正向可逆下三角元
\[
F=\begin{pmatrix}1&0\\f&s\end{pmatrix},
\]
则精确计算
\[
\boxed{DFD^{-1}F^{-1}=L(f),\qquad
L(f)=\begin{pmatrix}1&0\\f&1\end{pmatrix}.}
\tag{18}
\]
注意F并不需要是幺幂；它的倍率s在交换子中自动抵消。

### 十平均

利用已实现的 \(U(-3/8)\) 和可逆E，得到
\[
F=U(-3/8)E\sim
\begin{pmatrix}1&0\\136/5&-128/25\end{pmatrix}.
\tag{19}
\]
所以 \(\ell=L(136/5)\) 可逆且正向存在，并且
\[
D^{-3}\ell^5D^3=L(17).
\tag{20}
\]
由逆和共轭得到 \(L(17\mathbb Z[1/2])\)。

### 十二平均

用已实现的 \(U(-1/4)\) 和可逆R，
\[
F=U(-1/4)R\sim
\begin{pmatrix}1&0\\-68/9&32/9\end{pmatrix}.
\tag{21}
\]
于是 \(\ell=L(-68/9)\) 可逆且正向存在，
\[
D^{-2}\ell^{-9}D^2=L(17).
\tag{22}
\]

到这里已给出两套17倍下根，不需要尚未实现的外部矩阵分解。

## 7. 为什么还要激活倍率5或3

模17中，带符号的2幂只有8种不同非零余数，不能覆盖全部16种。所以不能像模7或13那样只拿2幂代表便结束。

十平均有
\[
L(-136/5)F=\Delta(-128/25)
\]
（按(19)的规范化射影作用理解），因此可逆 \(\Delta(25)\) 已由符号与D的幂得到。另有明确正向元
\[
J=E^{-1}B=\Delta(5).
\tag{23}
\]
不能先假设J可逆；但现在 \(J^2=\Delta(25)\) 的逆已知，所以
\[
J^{-1}=\Delta(25)^{-1}J
\]
也正向存在。由此可用的环扩大到
\[
R_{10}=\mathbb Z[1/10].
\]

十二平均由
\[
L(68/9)F=\Delta(32/9)
\]
得到可逆 \(\Delta(9)\)。同时
\[
\Sigma A=\Delta(1/3)
\]
正向存在；乘以 \(\Delta(9)\) 得 \(\Delta(3)\)，两者互逆。因此可用的环为
\[
R_{12}=\mathbb Z[1/6].
\]

两种情况最终都得到
\[
\boxed{U(R_q),\quad L(17R_q),\quad\Delta(R_q^\times)}
\tag{24}
\]
的完整正向实现。每个逆都有明确正向表达式，绝不在物理系统中执行除法、放大或反向平均。

## 8. 两套完整模17陪集

十平均选择非零代表
\[
\{\pm1,\pm2,\pm4,\pm5,\pm8,\pm10,\pm20,\pm40\};
\tag{25}
\]
十二平均选择
\[
\{\pm1,\pm2,\pm3,\pm4,\pm6,\pm8,\pm12,\pm24\}.
\tag{26}
\]
每一套模17恰好是全部16个非零余数，且全部属于对应环的单位。

连同0取代表 \(ST^j\)，另添无穷点I，就得到
\[
[\mathrm{SL}_2(\mathbb Z):\Gamma_0(17)]=18
\]
个完整陪集。对S、T、T逆的全部54条回路，有限图右乘T时给17倍下根，右乘S时给
\[
\begin{pmatrix}-k&-1\\jk+1&j\end{pmatrix},
\qquad k\equiv-j^{-1}\pmod {17}.
\]
其中主元-k是已实现单位。因此Gauss分解
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=L(c/a)\operatorname{diag}(a,a^{-1})U(b/a)
\]
的全部因子均可正向实现。

标准Schreier生成定理给出 \(\Gamma_0(17)\) 的完整射影包含。这里是两个平均元数各自的54条回路，不是混用两种元数的操作。

## 9. 任意合法输入输送到终端

对本原合法参数 \((x,y)\)，有 \(\gcd(x,y)=1\)、\(17\nmid y\)。取Bezout系数 \(\alpha x+\beta y=1\)，再调整
\[
(\alpha,\beta)\mapsto(\alpha+ty,\beta-tx)
\]
使17整除 \(\alpha\)。于是
\[
H=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}\in\Gamma_0(17),
\qquad H(x,y)^T=(0,1)^T.
\]
整数Euclid及第8节的回路编译提供有限真实q平均词，输出到
\[
K_q(0,v)=(0^q,v^r,-rv).
\]
选r份v、单点-rv与q-r-1个零，做一次q平均即全零。十平均中需要3个零；十二平均需要7个零，均有足够原位置。

必要性：若G=17，输入所有坐标模17同余且非零，而10、12均在模17可逆，所以无法归零。例子为
\[
(1^{16},-16).
\]
这分别完成两套充要条件。

## 10. 证明发现与核验的边界

[返回发现脚本](../work/explore_seventeen_arity_returns.py)只枚举一／两次实际平均能回到目标核心的模板，十平均得到36种、十二平均25种，再检查一／两个返回乘积的有限周期。[发现表](../work/seventeen_arity_return_discovery.json)保留来源；未命中不具有不可达含义。

[正式核验器](../work/verify_ten_twelve_average_seventeen.py)不导入发现程序或表。它明确写出本页使用的六／五个模板及实际矩阵，核对：

- 十平均6个模板各两个基输入，共12个实际宏；
- 十二平均5个模板各两个基输入，共10个实际宏；
- 两套各288个本原模17行、54条完整Schreier回路；
- 两种平均各60个72位大整数合法入口与Bezout输送；
- 每种平均各3条完整原位置路径，并从原始输入Fraction独立重放；
- 2至200的全部旧B公式自动G点，计17个。

原本第一条随机测试的展开词超过87000个原子，逐步分数重放成本较大，主动停止该重放，改为挑选已编译词长不超过5000的测试输入。这只是控制核验样本的资源；全参数的有限词存在性由群包含与编译证明承担。

所以这里的3条样本不是均匀随机性能统计，35步和131步不是最短或最坏界。所有原子模板及群回路均独立完整检查，测试输入的额外筛选没有替代数学充分性。

~~~text
python work/run_verifications.py --id ten-twelve-seventeen-complete
~~~

输出：

~~~text
old B automatic-G arities through200: PASS 17
arity 10 n17 physical macros and full Gamma0(17): PASS 12 288 54
arity 10 n17 large-coordinate entry and transport: PASS 60
arity 10 n17 literal full paths: PASS 3 35
arity 12 n17 physical macros and full Gamma0(17): PASS 10 288 54
arity 12 n17 large-coordinate entry and transport: PASS 60
arity 12 n17 literal full paths: PASS 3 131
ten and twelve averaging seventeen-position G criteria: PASS
~~~

[完整1基索引记录](../work/ten_twelve_seventeen_witnesses.json)同时保存自动B列表、6条实际路径和一个非法G=17例子。本文没有证明十平均16元、九平均13元、所有更高维数、最优阈值或统一多项式展开长度。

<!-- END SOURCE doc-efc595179bd5 -->
