# 历史推导、失败路线与审计 · 第8分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [全局标量周期的谱判据：Newton 多边形、Kronecker 与分圆验证](#doc-189ed272e3b0)
- [三份复制消去：同步路径、算术商与严格边界](#doc-6a53df23b854)
- [研究复核：目标平均值、动力学方向与算法边界](#doc-a1831df1e121)
- [三平均研究最新总览与交接说明（2026-09-09）](#doc-afb84f840542)
- [更内在的代数对象：Reynolds 半群、交叉计数与判别式对偶](#doc-d41c21d90b67)
- [非分裂素数路线复盘：停止局部拼接，返回二维除法结构](#doc-6039e2005c5f)
- [B12、B15、B18、B21 的统一有限比较](#doc-59a71841611a)
- [所有 p=1 mod3 素数的完整判据：高斯周期正向控制器](#doc-6e8f7854c3fe)
- [结构图景复核：可用的局部到整体机制及数域边界](#doc-4a708197aa0f)
- [三平均问题的局部算术轨道图景：结构性猜测与证明路线](#doc-3601bd1cd400)
- [子问题调用的缺失素数障碍与奇素数维数](#doc-2a65f1576ada)

---

<a id="doc-189ed272e3b0"></a>

## 原文导签：全局标量周期的谱判据：Newton 多边形、Kronecker 与分圆验证

来源：`outputs/triple_average/history/triple_average_projective_spectral_balance.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_projective_spectral_balance.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`projective-spectral-balance`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-189ed272e3b0 -->
# 全局标量周期的谱判据：Newton 多边形、Kronecker 与分圆验证

日期：2026-09-10。本文把经典代数数论工具接到任意秩正向宏的周期验证，不声称这些经典工具本身是新定理。结论适用于已经给定的有理矩阵或宏词；一般三平均可达性仍未解决，最小未解维数为47。

## 1. 精确的局部到整体判据

设A属于GL_d(Q)，特征多项式为
\[
f_A(t)=t^d+c_1t^{d-1}+\cdots+c_d,
\qquad D=\det A=(-1)^dc_d.
\]
定义射影不变量
\[
I_k(A)=\frac{c_k^d}{D^k},\qquad1\le k<d.
\tag{1}
\]
共同有理缩放A和共轭变换都不改变这些量。

**周期判据。** 存在h>=1及非零有理数lambda，使
\(A^h=\lambda I\)，当且仅当以下三项同时成立：

1. A在代数闭包上半单，即没有非平凡Jordan块。
2. A的全部复特征值具有相同绝对值。
3. 对每个k=1,...,d-1，都有 \(I_k(A)\in\mathbb Z\)。

第三项正好等价于：对每个有限素数q，A在 \(\overline{\mathbb Q}_q\) 中的全部特征值具有相同q进赋值。因此该判据要求所有地方的特征值比值都为单位，再加半单性。

## 2. 有限处的 Newton 多边形证明

固定q，令 \(v_q(D)=a\)。式(1)的q整性等价于
\[
v_q(c_k)\ge\frac{k}{d}a\qquad(1\le k<d).
\tag{2}
\]
系数为零时取赋值为正无穷。Newton多边形的端点是(0,a)和(d,0)，中间系数点(d-k,v_q(c_k))全部位于连接端点的直线上方或线上，当且仅当(2)成立。

因此其下凸包只有这一条边，全部d个根的赋值都为a/d。反向亦然。这证明有限处等价关系，允许a/d不是整数；例如A为 \(t^3-2\) 的伴随矩阵时，A^3=2I，全部2进斜率是1/3。

实际检验(1)只需计算有理数并判断分母是否为1，不需要分解所有相关整数的素因子。也不需要先构造特征值所在数域。

## 3. Kronecker 给出充分性

令 \(\lambda_1,\ldots,\lambda_d\) 为A在一个分裂域中的特征值。有限处条件说明，每个比值
\(\rho_i=\lambda_i/\lambda_1\) 在分裂域的所有有限处都具有赋值零，故是代数整数单位。

由于A为有理矩阵，任何数域嵌入都将这些特征值置换。复绝对值相等保证rho_i的全部共轭都具有模1。Kronecker定理遂说明每个rho_i都是单位根。

取其阶的公倍数h。半单性保证A^h为标量；而A^h的条目有理，所以该共同标量也有理。充分性得证。

必要性来自A的最小多项式整除 \(t^h-\lambda\)：后者在特征零下无重根，所有根在每个地方的绝对值或赋值相同。

这将“找到一个全局标量周期”严格翻译为特征值比值的单位根问题。仅有一个地方的紧性或有限剩余类周期，不能替代所有地方的条件。

## 4. 三个条件不能混用

下列精确例子区分各项条件。

| 矩阵 | 满足的条件 | 失败原因 |
|---|---|---|
| [[2,1],[1,1]] | 半单，全部有限处平衡 | 实特征值模长不同 |
| [[3/5,-4/5],[4/5,3/5]] | 半单，复特征值模长相同 | I_1=36/25，5进处不平衡 |
| [[1,1],[0,1]] | 所有地方的谱都平衡 | 存在非平凡Jordan块 |

迹也不足以替代所有特征系数。\(t^4+t^2+2\) 的伴随矩阵迹为零，但I_2=1/4不整，所以不可能具有有限射影阶。

此前用于等值载体重分组的 \((\operatorname{tr}A)^d/\det A\) 整数性，正是本判据的k=1部分。高秩候选应同时检查全部I_k，避免仅凭迹零就推断周期。

## 5. 给定宏词的多项式时间精确验证

还可以完全避免复根数值判定。考虑共轭表示
\[
\operatorname{Ad}_A:X\longmapsto AXA^{-1},
\]
它是维数N=d^2的有理矩阵，特征值恰为全部 \(\lambda_i/\lambda_j\)。

**精确算法。**

1. 用有理多项式运算计算A的特征多项式f及其无重根部分 \(f/\gcd(f,f')\)。把该无重根多项式代入A；结果为零恰好说明A半单。
2. 计算全部I_k；任何一个不整就拒绝。此步是方便的前筛，不是后两步逻辑所必需。
3. 计算Ad_A的有理特征多项式g。
4. 对所有满足 \(\varphi(m)\le N\) 的m，精确除去g中的分圆因子Phi_m及其重数。若最终余下常数1，则接受，否则拒绝。

候选m有显式多项式范围：
\[
\varphi(m)^2\ge m/2,
\quad\text{故}\quad m\le2N^2=2d^4.
\tag{3}
\]
这个下界直接来自素数幂乘积：\(\varphi(p^a)^2/p^a=p^{a-2}(p-1)^2\)，只有p=2,a=1的因子小于1，且其值为1/2。

因此只需枚举m<=2d^4，计算分圆多项式并作有理多项式除法。矩阵求逆、特征多项式、半单性和上述有限范围运算都可在输入矩阵的维数与总位长的多项式时间内完成。实现可以进一步优化；本项目的参考实现以可核验为先。

接受时，实际出现的Phi_m下标的最小公倍数正好是A的射影阶。这个阶的数值可能大，但其二进制位长受多项式控制；不需要展开可能含极大分子的A^h来验证结论。

**范围必须明确：这是给定矩阵／已给定宏词的周期判定算法，不是原三平均可达性的多项式算法。** 尚未证明可以在多项式范围内找到所需宏词，甚至未证明每个未解n的当前宏库含有一个非平凡周期。

## 6. 正向宏中的使用方式

假设一个已核对位置账本的可逆返回词为 \(W=T_s\cdots T_1\)。如果上述算法证明W具有有限射影阶，则W^h是实际正向标量词。

将这个循环在任意一个因子处旋转，再删除那个因子，剩余正向词就实现该因子的射影逆。这个步骤只使用可逆矩阵的循环旋转和实际词拼接，完全保留物理尺度。

但谱判据只检查该完整词，不会自动为当前字母库提供一个这样的词。带条件宏也必须逐步证明实际适用域，不能从形式乘积的有限阶忽略中间调用条件。

## 7. 47元出现的实二次范数环面

后续更新：[正向根群饱和](../sources/outputs/triple_average/history/triple_average_positive_root_saturation.md)第4节已给出下述共轭算子的57模板正向证书。这里保留首次识别数域时的算术障碍与共轭目标；其单宏非周期结论不受影响。

在当前B47的167个通用模板中，矩阵
\[
M=\begin{pmatrix}-9&5\\162&-72\end{pmatrix}
\]
的实际物理比例为 \(-2/243\)。它只调用9、27、43元子块，均已有完整判据。

令B=M/9，则
\[
\chi_B(t)=t^2+9t-2,\qquad
B\begin{pmatrix}1&-1\\0&18\end{pmatrix}
=\begin{pmatrix}1&-1\\0&18\end{pmatrix}
\begin{pmatrix}0&2\\1&-9\end{pmatrix}.
\tag{4}
\]
所以B等价于在 \(\mathbb Q(\sqrt{89})\) 上乘以
\[
\theta=\frac{-9+\sqrt{89}}2,\qquad N(\theta)=-2.
\]
这是有理宏的辅助数域解释，不是将输入换到数域。

在3处，\(t^2+9t-2\) 模3是不可约的 \(t^2+1\)；两个特征值均为3进单位。在2处，迹为单位、行列式赋值为1，所以两个特征值赋值分别为0、1。89=1 mod8也与2在该二次域分裂相符。

因此一个仅看3进谱似乎“平衡”的宏，在2处具有无法用共同尺度去掉的相对膨胀。射影不变量
\[
I_1(B)=\frac{(-9)^2}{-2}=-81/2
\]
立即排除它的有限射影阶。实方向上，两根也具有不同模长。

范数环面解释仍有建设性用途：如果能用真实正向宏实现共轭乘法 \(\bar\theta=-9-\theta\)，两者乘积便是标量-2。但当前库中还没有为这个共轭算子提供正向证书；共轭在数域中存在不等于物理词已存在。

## 8. 可交换宏的正向词存在性可化为整数锥

谱判据检查一个已经给定的词。若所有候选宏恰好来自同一数域F的乘法，则还可以处理“是否存在某条正向周期词”。以下结论只适用于这类可交换库，不覆盖一般不交换返回宏。

设 \(\alpha_1,\ldots,\alpha_s\in F^\times\)，以某个有理基表示乘法矩阵。取有限有理素数集合S，使每个alpha_i及其逆都在 \(\mathcal O_F[S^{-1}]\) 中。允许共同有理非零尺度，所以需要判断是否存在
\[
e\in\mathbb Z_{\ge0}^s\setminus\{0\},\quad h\ge1,
\qquad\left(\prod_i\alpha_i^{e_i}\right)^h\in\mathbb Q^\times.
\tag{5}
\]

S单位群模有限单位根是有限生成自由阿贝尔群。利用一个S单位基表示alpha_i，并加入各个有理S素数的指数列，再对这些有理尺度列取饱和商，得到一个明确的整数矩阵C，使
\[
(5)\quad\Longleftrightarrow\quad Ce=0,
\quad e\in\mathbb Z_{\ge0}^s\setminus\{0\}.
\tag{6}
\]
取饱和商会忽略有限挠元，这恰好对应(5)允许再取有限次幂，而非要求乘积立即为有理数。

因此可以在有理数上求解
\[
Ce=0,\quad e_i\ge0,\quad\sum_i e_i=1.
\tag{7}
\]
若可行，清分母便得到整数正向周期的指数。给定整数关系矩阵C以后，这只是有理线性规划；计算数域和S单位基的代价另计，本文不声称整个数论预处理为多项式。

若希望整个宏半群在射影意义上成为群，则需要一个更强、也准确的条件：
\[
Ce=0,\qquad e_i>0\quad\text{对每个 }i.
\tag{8}
\]
充分性是用含所有生成元的标量周期为每个生成元删首位造正向逆。必要性是：若每个生成元都有正向逆，将相应的正向关系相加，便得到所有坐标都为正的周期关系。故(8)完全刻画这类可交换库的正向群化。

### 8.1 二次域中的两层约束

对二次域，可以先记录每个分裂素理想对上的相对赋值；这些整数线性约束消去后，乘积的 \(\alpha/\bar\alpha\) 变成一个范数一单位。

- 虚二次域的单位群有限，模单位根后没有额外单位行。
- 实二次域还剩一个无限单位指数，需要再加一条整数线性约束。

这里无需使用浮点对数判等：通过单位群表示记录精确整数指数即可。全局单位约束解释了为什么“全部有限素理想赋值相消”在实二次域中还不足以得到周期。

### 8.2 Q(sqrt89) 的具体例子

令theta如(4)，并取
\[
\varepsilon=500+53\sqrt{89},\quad N(\varepsilon)=-1,
\qquad u=\varepsilon^2=500001+53000\sqrt{89}>1.
\]
考虑乘法库theta、bar(theta)、u。theta与bar(theta)分别产生2上方两素理想，u是单位。非负指数(a,b,c)的乘积具有有限射影阶，当且仅当
\[
a-b=0,\qquad c=0.
\tag{9}
\]
第一式来自2处相对赋值；在a=b后，乘积为 \((-2)^a u^c\)，u的实绝对值大于1，所以第二式不可省略。

theta和bar(theta)一起有正向标量关系，但加入u后不能让全部三者都具有正向逆。若再加入u逆，则(8)可以满足。这是数域乘法库的例子；当前三平均库只已证theta的实际宏，未声称bar(theta)或u已由正向平均实现。

分裂素数高斯周期定理中的范数循环，正是(8)有显式全正整数解的情形：取每个Galois共轭一次。这里给出了将该成功结构推广到其他可交换宏族时，可以精确检验的关系格条件。

## 9. 核验

脚本：[verify_projective_spectral_balance.py](../sources/work/verify_projective_spectral_balance.py)，统一ID `projective-spectral-balance`。

- 85个任意秩共轭／缩放与有限阶精确例子，含 \(t^3-2\) 的非整数公共赋值。
- 四个独立条件边界及高阶特征系数反例。
- 十个给定矩阵的精确Ad分圆判定，包括实际阶1、2、3、4、6及无限阶对照。
- 47元范数-2宏的独立子问题重放、基变换及2／3处赋值。
- 125个Q(sqrt89)可交换乘法指数，核对相对赋值与实单位约束缺一不可。

一般必要充分性与算法复杂度由正文的Newton、Kronecker及分圆次数证明承担；第8节使用S单位群及整数关系格的标准结构。脚本未实现一般数域S单位基求解器，125个例子不替代该理论。

<!-- END SOURCE doc-189ed272e3b0 -->

---

<a id="doc-6a53df23b854"></a>

## 原文导签：三份复制消去：同步路径、算术商与严格边界

来源：`outputs/triple_average/history/triple_average_replica_elimination_research.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_replica_elimination_research.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`ai5-synchronized-replica-audit`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-6a53df23b854 -->
# 三份复制消去：同步路径、算术商与严格边界

本文专门研究下面的命题：给定 (n) 个位置的状态 (X)，记

\[
X^{[3]}=(x_1,x_1,x_1;\ldots;x_n,x_n,x_n).
\]

如果 (X^{[3]}) 能由真实三平均归零，是否必有 (X) 本身能由真实三平均归零？这正是复制稳定化之后的剩余问题之一。本文不把双随机矩阵证书误认为真实平均路径，而是给出一个可直接使用的同步子类、一个矩阵层面的必然结论，以及当前不能跨越的边界。

## 1. 三个层次必须分开

设一次真实操作选取三个不同的位置，并把这三个位置都改成它们的平均值。对复制状态，位置写成 ((i,c))，其中 (i\in\{1,\ldots,n\}) 是原坐标，(c\in\mathbb Z/3\mathbb Z) 是复制标签。

需要区分：

1. **算术运输证书。** 存在 (P\in M_n(\mathbb Z[1/3]))，满足 (P\ge0)、行和列和为 (1)、且 (PX=0)。复制稳定化定理已证明，这等价于 (G(X)) 为三幂。
2. **复制状态的真实路径。** 存在一个由 (3n) 个位置上的三平均矩阵相乘得到的 (M)，满足 (M X^{[3]}=0)。
3. **真实复制消去。** 从复制状态的路径构造一个只在 (n) 个原位置上的三平均路径。

第 1 层不自动给出第 3 层。即使把第 2 层的矩阵对复制标签做循环平均，得到的仍然只是一个新的双随机矩阵；凸组合不保留“由正向三平均生成”的半群分解。

## 2. 可严格消去的同步轨道

令 (\tau(i,c)=(i,c+1)) 为复制标签的循环平移。取三个互异的原坐标 (i,j,k)，以及三个固定偏移量 (a,b,d\in\mathbb Z/3\mathbb Z)。定义三个 lifted triples

\[
S_c=\{(i,c+a),(j,c+b),(k,c+d)\},\qquad c=0,1,2.
\]

由于 (i,j,k) 互异，三个 (S_c) 两两不交。把三次真实平均分别作用于 (S_0,S_1,S_2)，称为一个**干净同步轨道宏**。

### 同步轨道引理

若输入状态具有复制对称性

\[
Y_{i,0}=Y_{i,1}=Y_{i,2}=y_i,
\]

则一个干净同步轨道宏的输出仍具有复制对称性，而且在原坐标上恰好等于一次三平均

\[
(y_i,y_j,y_k)\longmapsto
\left(\frac{y_i+y_j+y_k}{3},\frac{y_i+y_j+y_k}{3},\frac{y_i+y_j+y_k}{3}\right).
\]

**证明。** 三个 (S_c) 不交，所以三次操作互不干扰。每个 (S_c) 在输入时看到的值都是 (y_i,y_j,y_k)，因而都产生同一个均值 (m=(y_i+y_j+y_k)/3)。宏结束后，(i,j,k) 的三个复制位置全部为 (m)，其余位置保持复制对称。\(square)

### 复制消去的严格弱化定理

如果 (X^{[3]}\to0) 存在一个路径，并且该路径可以分解成上述干净同步轨道宏，那么 (X\to0) 存在。具体地，把每个同步宏的三个 lifted triples 压缩成其投影的一个原始 triple，即得到一条真实路径；原路径长度为 (3L) 时，压缩路径长度为 (L)。

这一定理是完全的操作账本结论，不使用有限搜索，也不依赖 (G) 条件。它覆盖以下常见构造：先在原状态上选一条三平均路径，再把每一步复制到三个互不相交的标签层；偏移量可以随宏改变，只要每个宏内部保持同一组原坐标和三份互不相交的标签。

## 3. 一个局部负结果：重复原坐标不能组成干净同步宏

如果一个复制轨道的 triple 投影为 (\{i,i,j\})，例如

\[
\{(i,c+p),(i,c+q),(j,c+r)\},\qquad p\ne q,
\]

则三个平移后的 triples 会重叠。将这三个操作按任意顺序作用于复制对称输入 (i\mapsto a,j\mapsto b)，其终点不能对所有 (a,b) 保持复制对称。这个结论可以直接在二维系数向量上验证：把 (a,b) 分别表示为 ((1,0),(0,1))，逐步更新三个 (i)-副本和三个 (j)-副本，全部 (3\cdot2\cdot3\cdot3!\cdot2=216) 个偏移和顺序均失败。

因此，想要把一个一般复制路径逐宏压缩，不能只要求“每个 triple 在三个复制标签下出现一次”；还必须排除同一原坐标在一个 triple 中出现两次。这个重叠现象是同步路线的第一处真实障碍。

## 4. 算术矩阵可以对称化，但路径不能随之对称化

设 (M\in M_{3n}(\mathbb Z[1/3])) 是任意非负双随机矩阵，且

\[
M X^{[3]}=0.
\]

令 (S) 是复制标签的循环置换矩阵，定义

\[
\overline M=\frac13\left(M+SMS^{-1}+S^2MS^{-2}\right).
\]

因为 (X^{[3]}) 在 (S) 下不变，仍有

\[
\overline M X^{[3]}=0,
\]

且 (\overline M) 非负、双随机、与 (S) 对易。令

\[
P_{ij}=\sum_{d=0}^2\overline M_{(i,0),(j,d)}.
\]

则 (P\in M_n(\mathbb Z[1/3])) 非负、行和列和为 (1)，并且

\[
PX=0.
\]

所以任意复制态的算术消灭证书都可以下降到原维数的算术证书。这重新得到复制稳定化的必要方向，但没有给出原维数的真实三平均路径。原因是 (\overline M) 是三个共轭矩阵的凸组合，而不是它们在三平均半群中的乘积；三平均操作只允许正向乘法，不能把这个凸组合当成可执行的同步操作。

## 5. 无条件可处理的低支持集

还有一个与复制路径无关的严格弱化版本。若 (X) 是零和状态，非零坐标数为 (r)，并且存在 (q=3^k\ge r) 且 (q\le n)，则把 (q-r) 个零补入这些坐标，得到一个 (q) 元零和块。标准三进网络在该块上把所有位置归零。因此：

\[
\boxed{\#\operatorname{supp}(X)\le q=3^k\le n
\quad\Longrightarrow\quad X\to0.}
\]

例如 (n\ge9) 时，所有支持数不超过 (9) 的状态都可以直接归零；这类状态的三份复制消去无需使用任何复制路径。这个结论对任意有理数坐标成立，操作账本只使用 (qk/3) 次平均。

同样，若状态已经分解为若干互不相交的零和三幂大小块，也可以逐块归零。真正未解决的情形是支持数超过最近的三幂、且不能被已知的七、八、十、十二、十三、十五、十八元子块覆盖的高重数核。

## 6. 复制消去路线目前能交付什么

当前可以作为正式引理使用的是：

- 干净同步轨道宏的逐宏消去；
- 任意复制态双随机证书的循环对称化与矩阵商；
- 低支持集和三幂零和块的直接归零；
- 重复原坐标的轨道宏不能保持复制对称这一局部障碍。

尚未证明的是：任意 (X^{[3]}\to0) 路径都能重写成干净同步轨道宏，或能通过有限个额外宏变成这种形式。尤其是路径中一旦出现跨标签的重叠操作，复制对称性会在中间时刻丢失。将三个共轭矩阵取算术平均只产生一个双随机矩阵；把三个共轭路径串联则产生矩阵乘积，二者都不能自动恢复一条原维数的真实正向路径。

因此，三份复制消去仍然是主猜想级别的开放命题。同步路线的下一步应是寻找一种允许重叠操作的更大“可压缩宏”类，并证明其端点在复制对称子空间上诱导真实三平均词；单纯扩大矩阵群或做有限状态搜索不足以完成这一步。

证据等级：同步轨道引理、矩阵商命题和低支持集命题是符号证明；脚本只验证精确账本、局部重叠障碍和随机同步样本，不把有限枚举当作全称证明。

<!-- END SOURCE doc-6a53df23b854 -->

---

<a id="doc-a1831df1e121"></a>

## 原文导签：研究复核：目标平均值、动力学方向与算法边界

来源：`outputs/triple_average/history/triple_average_research_corrections.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_research_corrections.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`stabilization-theorem`, `n91-congruence-container`, `n91-corrected-witness`, `n91-cusp-depth4`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-a1831df1e121 -->
# 研究复核：目标平均值、动力学方向与算法边界

本稿保留全部原始文档，只校正会影响后续推理的表述。新增任意维数结果见 [复制稳定化定理](../sources/outputs/triple_average/history/triple_average_stabilization_theorem.md)。

新增[等值载体与虚拟位置边界](../sources/outputs/triple_average/history/triple_average_paired_carrier_reset.md)：两个真实载体相等，不代表可删去p+1射影模型中的虚拟点。中心收缩后虚拟值通常改变，删除它会使剩余物理值总和非零。原位置数上的有效替代是4r-3步二进重分组宏，W=2V且V为R可逆；这仍不提供全局正向逆。周期的精确迹整性和行列式次数下界另行记录。

最新状态：[41元完整证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_one_arithmetic_complete.md)已闭合，最小未解维数为47。此前仅21个可逆宏的41元共轭搜索没有闭合，并在第三层停止；完整短周期库提供32个可逆宏后，一层整数共轭已足够。正式证书删减为21个宏和10个整数词，独立核验不依赖被停止的搜索。

[实能量与本原高度的边界](../sources/outputs/triple_average/history/triple_average_modular_height_barrier.md)给出统一反例族：有限模正向恒等词保持合法性，实能量下降，本原高度却按3^(2h)增长。因此不能把模调度成功或最后一次子调用下降作为整条路径终止的证明。

最新状态：[29元完整证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)已经闭合，最小未解维数变为41。旧1195模板的二因子周期排除和A0^jB全指数排除仍正确；新证书使用三因子周期及整数共轭，不与旧负结果冲突。正式18个模板全部来自冻结旧库，仅调用3/9/25/27。

最新进展：[全部p=1 mod3的正向高斯控制器](../sources/outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md)已统一解决一个无限素数族，并扩展其因子闭包。早期“所有p>=29都仍需单独处理”已过时；剩余统一任务是p=2 mod3。最小未解仍为29，任意n总定理仍未完成。

最新修正：[九十一元两处字符耦合](../sources/outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md)已经证明旧21504容器严格大于特定宏群的整数部分，故“该群等式仍待证明”应改为“该等式不成立”。新必要容器指数43008，有192尖点、48合法尖点；是否等于实际宏群仍未证明。旧自动机与终端缓存保留历史标签。

新增[原维数平坦核形式算术性](../sources/outputs/triple_average/history/triple_average_flat_star_arithmeticity.md)统一全部p>=13的形式群有限指数和第一层模2p终端相容性。这里确实使用形式逆；不得据此宣布正向半群已经群化或29元已经解决。

2026-09-10 后续更新：[一次三份复制](../sources/outputs/triple_average/history/triple_average_one_tripling_stabilization.md)已将副本数统一降为三，并无条件解决所有N>=9的三整除维数。原维数消去和29元仍开放。[结构图景审计](../sources/outputs/triple_average/history/triple_average_structural_picture_audit.md)另纠正高次level不能仅由合法域推得、扩张域不改变固定输入可达性、内容理想及所提类群条件不是必要条件；准确必要对象为R加法模。原结构猜测及其他AI报告均保留。

最新状态：[任意维数到素数的总归约](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_to_primes.md)已证明全部n>=7的判据等价于全部素数p>=7的判据，合数归约已闭合。所有23光滑维数n>=7均已解决，最小未解维数变为29。下文或旧报告中“20最小未解”“低二进偶数桥仍开放”均是历史状态；统一素数定理仍未证明。

历史版本的[奇数合数乘法闭包](../sources/outputs/triple_average/history/triple_average_odd_composite_factor_closure.md)曾先得到“至多一个5”；这只是A(25)尚未补齐时的边界。结合现已完成的[25元完整证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)，当前结论已升级为可再乘任意五幂和三幂。49、77、91、121等已解；早期“91元仍缺群等式所以整体未解”的状态已由另一条因子证明替代。后续耦合字符又独立否定了旧21504群等式，不能把可达性定理与某个特定返回群的等式混同。

进一步：[25元完整证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)已补齐最后一个奇数小基例，所以上述额外5现在可以任意次幂。全部奇数严格归约到p>=7素数；8整除乘法族也已完成相应归约。一般n仍开放，主要剩余维数接口为未统一的素数与v2(n)=1、2的偶数。

2026-09-10 状态更新：[十九元](../sources/outputs/triple_average/arithmetic_cases/triple_average_nineteen_arithmetic_complete.md)与[二十三元](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md)均已完成及其三进塔，此前十七元也已完成。早期“B17仍开放”“共轭范数素元尚不可实现”及最小未解维数17／19都是历史状态；当前最小未解维数为20，下一个未解素数为29。旧五宏库的固定逆词不可能定理仍成立，新宏不在该库内。23处负三进单位循环的排除也仍正确；实际使用4/27、2/3^7，含有额外2因子，故不与周期定理矛盾。全部一般n、三份复制消去及多危险素数桥仍未解决。

## 1. 局部平移后，必须同时平移目标

原有“见证重置”笔记在把主余类平移到 $0$ 后，遗漏了目标平均值的变化。这使“选中危险支持就会产生可约去的中心化公因子”的一般表述不成立。

准确地说，设 $X$ 已中心化，$\sum_i x_i=0$，$p\ne3$ 且 $p\mid n$。未选位置都满足 $x_i\equiv c\pmod p$，三平均后的整数状态记为 $Z$。由总和保持为零，选中位置的平均值也同余于 $c$。因此

$$
Z\equiv c\mathbf1\pmod p.
$$

必须区分：

* 若 $c\not\equiv0\pmod p$，则 $Z$ 的坐标公因子不含 $p$，而所有差都被 $p$ 整除。其本原中心化代表确实出现 $p\mid G$，已经不可达。
* 若 $c\equiv0\pmod p$，则 $Z=pY$，且 $Y$ 仍零和。这时约去 $p$ 才是保持目标为零的合法重置。是否恢复 $p\nmid G$ 仍需检查更深层余数。

任意平移为 $Z-c\mathbf1$ 后再除以 $p$ 当然保留“能否达到自身平均值”的问题，但商状态的平均值是 $-c/p$，不能再把目标当作零。尤其不能只看商状态的未中心化差分 gcd。

一个七元显式例子是

$$
X=(3,3,3,3,3,1,-16),\qquad G(X)=1.
$$

平均 $(3,1,-16)$ 得

$$
Z=(3,3,3,3,-4,-4,-4),\qquad G(Z)=7.
$$

若把主余类 $3$ 平移掉并除以 $7$，得到 $(0,0,0,0,-1,-1,-1)$。虽然其未中心化差分 gcd 为 $1$，目标却是 $-3/7$，三平均从整数只能产生三幂分母，故不可达。重新中心化、清分母，正好恢复 $Z$ 的模七障碍。

原覆盖设计使用的背景 $u=3n$ 在每个危险素数下都同余于零，所以其具体“出现可约公因子”的计算不受此修正影响。

## 2. 应记录中心化坐标深度和差分深度两个量

对非零中心化有理状态 $Z$ 定义

$$
\alpha_p(Z)=\min_i v_p(z_i),\qquad
\beta_p(Z)=\min_{i<j}v_p(z_i-z_j).
$$

若 $Z_{\mathrm{prim}}$ 是其本原整数代表，则

$$
\boxed{v_p(G(Z_{\mathrm{prim}}))=\beta_p(Z)-\alpha_p(Z).}
$$

这是对全局非零缩放不变的精确公式。对 $p\ne3$，局部合法条件是 $\alpha_p=\beta_p$。

单独的缺口轮廓

$$
\epsilon_{p,k}(Z)=\min_c\#\{i:z_i\not\equiv c\pmod{p^k}\}
$$

只看到差分是否集中，未记录共同余类相对于零的位置。今后的见证控制器应把它与目标平均值，或等价的中心化深度 $\alpha_p$ 一起记录。

对真正零和的 $Z=pY$，原来的公式

$$
\epsilon_{p,k}(Y)=\epsilon_{p,k+1}(Z)
$$

仍然成立。若两个未选位置的差恰有 $p$ 进赋值 $1$，那么除以 $p$ 后有单位差，确实恢复局部合法性。但“没有这样的锚点”只能说明还需继续检查，不能证明能安全重置。

## 3. 重写系统的无向连通性和严格实下降都不够

三平均正向规则

$$
\delta_a+\delta_b+\delta_c\longrightarrow3\delta_{(a+b+c)/3}
$$

有严格实能量下降，但有理能量可以无限下降而不等于零。因而原托里克笔记中的“问题的困难不是终止性”表述应撤回。只有整数高度在某个离散格上严格下降，并且非零终端能够处理，才有有限终止结论。

同样，托里克二项式或无向 Markov 移动允许反向拆分。无向纤维不连通当然排除可达，但有向不可达不能自动证明无向纤维不连通；无向连通也不能保证沿能量下降方向抵达指定目标。五元反例给出有向动力学障碍，不能仅据此断言相应三次关系不是无向 Markov 基。

因此返回宏必须继续附带真实正向平均词。新运输矩阵定理之所以是动态结果，正在于它明确给出了副本分块及每块的正向三进网络。

## 4. 两处十三元公式及宏适用范围

十三元核

$$
\mathcal B_{13}(u,v)=(u^9,v^3,-9u-3v)
$$

的能量为

$$
E=90u^2+54uv+12v^2.
$$

原十三元宏前沿把这一个式子同时记作 $Q=E/3$，比例有误。应为 $Q=E$；四步宏的实际恒等式仍然正确：

$$
E\left(-\frac u3-\frac v9,u\right)
=\frac13E(u,v)-\frac{26}{9}(3u+v)^2.
$$

坐标 $x=u,y=9u+4v$ 下仍有 $4E=117x^2+3y^2$。$y=0$ 在非零本原参数下强迫 $(u,v)=\pm(4,-9)$，故 $G=13$；它是非法方向，不能当成十三元的合法终点。$u=0$ 才是可用终端方向：此时非零位置至多四个，可补零组成九元零和块。

对一般 $\mathcal B_n$，连续三次平均 $(v,u,u)$ 确实可执行，但结果是

$$
\left(u^{m-6},\left(\frac{2u+v}{3}\right)^9,-mu-3v\right),\qquad m=n-4.
$$

它只有在 $m=9$ 时直接返回同一种 $(m,3,1)$ 核。此前单素数降维笔记把它写成对所有 $m\ge6$ 都有同一参数返回公式，这个适用范围应缩回十三元。三幂块推广仍有效，但其中保留的单独坐标始终是 $-mu-3v$；重建完成后它等于 $-ma_k-3u$，不是 $-mu-3a_k$。

## 5. 判定复杂度不依赖构造证书长度

若原问题对所有 $n\ge7$ 的判据确实是 $G=3^s$，则中心化、清分母、gcd 和除三测试直接构成输入总位长多项式时间判定。这里无需分解大整数，也无需生成平均路径。

所以旧总纲中“即便充分性证明完成，判定仍需另外控制宏长度”的说法不准确。额外需要长度和中间位长分析的是**输出真实平均序列的构造算法**。

复制稳定化定理已经给出稳定问题的多项式时间判定，以及紧凑矩阵证书的多项式时间构造；它没有给出原维数问题的充分性，也没有给出原问题的多项式长度操作证书。

## 6. 实验记录的证据边界

此前支持压缩实验与十三元贪心脚本是探索程序，不是证明。特别地，旧十三元贪心脚本曾把 $A$ 的 $y$ 坐标更新写错；应为 $y\mapsto-y/3$。它原先报告的长轨迹不能当作正确宏的实验结论。

即使修正后在某个步数截止仍未归零，也只能说该策略在截止内没有成功，不能说已证明无限运行。现有严谨结论是：实能量收缩本身不保证离散有限终止；支持压缩策略则有第 7 节稳定化笔记所列的明确七元反例。

## 7. 九十一元粗同余群不能当作真实返回群

对 ((81,9,1)) 核，本原化后的差值乘子群应为

\[
\langle-1,3\rangle\subset(\mathbb Z/91\mathbb Z)^\times,
\]

不是 (langle-1,9\rangle)。修正后，只记录模 (91) 行标签与模 (2) 置换奇偶的粗同余容器指数为 (1344)，其 Kurosh 数据为

\[
F_{209}*(C_3)^{*24}.
\]

但这仍不是正确的完整候选。真实整数返回宏还有模 (8) 限制；已知六元素局部像为

\[
L_8=\langle C_9,3I\rangle.
\]

同时独立加入模 (91) 与模 (8) 条件得到历史上的指数 (21504) 容器。它有 (96) 个尖点，其中 (24) 个满足 (G=1)。后续字符耦合已证明真实整数宏群严格小于这个容器，并给出指数43008的新必要容器；因此旧的“指数 (1344) 群已经生成，只剩六个终端类”推断仍无效。

`work/cyclotomic_schreier.py` 现在只应理解为粗模 (91\times2) 商；完整必要局部模型由 `work/cyclotomic_congruence.py` 给出。

## 8. 九十一元缺失类的坐标与终端路径

对代表 ((u,v)=(1,-3))，单独坐标为

\[
-81u-9v=-54,
\]

不是旧脚本中的 (-72)。旧起点的总和为 (-18)，因而从该起点得到的所谓零和块证书无效。

修正后的真实路径为

\[
(1^{81},(-3)^9,-54)
\to(1^{81},(-3)^7,(-20)^3)
\to(1^{79},(-3)^7,(-20)^2,(-6)^3).
\]

第二个状态包含零和 (27) 元块

\[
1^{21},(-3)^5,-6.
\]

归零该块后，剩余 (64) 个非零位置与 (17) 个新零形成一个 (81) 元零和块。因此模 (91) 的六个差值类均有真实终端。经整数子集和 DP 与多进程优化后，深度四搜索覆盖 (23/24)；随后对尖点 (29) 代表 $(-13,18)$ 的深度五定向搜索得到五步证书，已知同余容器内的有限深度覆盖达到 (24/24)。这仍不等于真实宏群等于容器，也不是任意九十一元输入的桥定理。

## 9. 高秩返回矩阵必须使用精确行列式

早期的 `work/explore_weighted_kernel_group.py` 在高斯消元时把整数除法落入浮点数，导致许多真实的 (det=\pm1) 返回矩阵被漏掉。对 ((27,9,3,1)) 核，深度七的整数返回矩阵实际为 (55) 个，而非旧输出的 (8) 个；深度八为 (96) 个。

该函数现已把所有输入先转换为 `Fraction`，并另加纯整数三阶行列式核验。任何此前依赖“深度七只有八个整数回路”的薄群猜测都应撤回。

## 10. Burau 识别取代“逐秩猜逆元”

十三元中的三阶关系已经推广为任意秩定理。几何三幂链

\[
R s^{t-1},\ldots,R
\]

上的相邻块宏给出参数 (1/s) 的 Burau 表示，且 Coxeter 元在加权零和空间满足 (C^t=s^{-t}I)。因此所有相邻宏的射影逆元都有正向宏词。

这条定理只适用于整条链的加权零和空间。若链嵌在更大的核中而自身总和不为零，不能把正词误写成整个状态上的射影逆元。完整证明与边界见 [Burau 幂链定理](../sources/outputs/triple_average/history/triple_average_burau_power_chain.md)。

## 11. 十二元状态更新与基维数术语

十二元已经由新的四个正向宏与共轭 \(\Gamma_0(8)\) 的指数 12 子群完成；旧文档中“最小未解维数为 12”现由“14”取代。完整证书见 [十二元证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md)。对应新维数族为 \(12\cdot3^k\)；由于 12 可被三整除，它是新传播塔的起点，不是三进无关的整数基数。B21 早已由七元提升解决，有限实验不能写成新的维数定理。

## 12. 十八元并非继续扩大固定核搜索

[十八元完整归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_eighteen_via_twelve_complete.md) 已利用十二元定理和重数配对，证明 \(18\cdot3^k\) 全部维数的充分性。新证明不依赖其七步返回表没有混合矩阵的有限观察。此前框架中把 B18 列为未解决，以本更新为准；仍未解决的最小维数是 14。

## 13. 符号返回搜索的均值碰撞剪枝

早期整数符号搜索使用“每步至多消去两个不同值”来剪枝，未考虑三个单重值的均值恰好为已有值：这时可一次消去三个不同值。安全支持界已改为剩余 L 步最多减少 3L 个值，并加入六种形式值一步返回三块核的反例型回归测试。

保存的 B12 深度6、7及 B15/B18 返回表只保留其逐条正向证书效力，撤回完备枚举声明；B12 深度5另有独立未剪枝程序对照。十二元完整证明独立重放四个明确宏并核验有限指数子群，十八元证明只使用十二元定理和配对归约，两者均不依赖这些搜索表的完整性。B21 的数值整数 BFS 没有这个支持剪枝，不受影响。

## 14. 十五元完成与偶维核桥的边界

[十五元完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md) 已通过模8八循环、合法十二元调用和十元收尾闭合，推广到 \(15\cdot3^k\)。此前“B15 仍开放”属于早期状态，应以此更新为准。没有依赖手写条件宏表的有限高度下降统计。

[偶维 B 核减半桥](../sources/outputs/triple_average/history/triple_average_even_kernel_halving_bridge.md) 进一步解决一批结构核，包括合法 B14；但多危险素数的一般十四元输入尚未统一归约到该核，故最小未解维数仍是14，不能因 B14 可解而宣布十四元判据。

## 15. 十四元的高维桥现已补齐

上一节记录的是只有 B14 核可解时的状态。现已证明任意 d 的安全终端具有 \(n-d-2\) 重值，并在十四元两个危险集不交的情况下完成512类模8／模7余数桥。由独立十二元调用和既有 B14 减半接口，[十四元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_fourteen_complete.md) 已完成，最小未解维数更新为16。没有把旧的结构核结论直接升级；新补出的高维证明和有限证书均有独立文档与核验入口。

## 16. 二三光滑维数的统一归纳

[统一减半证明](../sources/outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md) 已将全部 \(2^a3^b\ge7\) 纳入完整判据。十六元的96类发现过程最终提炼成一个全参数模板，数学证明不依赖这份小表的穷尽性。最小未解维数现为17；此前16的记录保留其历史顺序。

## 17. 全部偶维 B 核与完整维数的区别

[全部偶维 B 核减半](../sources/outputs/triple_average/history/triple_average_all_even_B_kernel_halving.md) 已覆盖每个偶数 \(n\ge14\)，通过至多一次预备三平均和合法八元／十二元子问题形成两份合法 \(n/2\) 元状态。这只是结构核的条件桥，尚不解决一般多危险素数输入。因此不能据 B20、B28 核可解而宣布任意20、28元判据；二三光滑输入可以归约到 B 核，所以其完整归纳成立。

<!-- END SOURCE doc-a1831df1e121 -->

---

<a id="doc-afb84f840542"></a>

## 原文导签：三平均研究最新总览与交接说明（2026-09-09）

来源：`outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`n91-congruence-container`, `n91-corrected-witness`, `n91-cusp-depth4`, `n91-cusp29-depth5`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-afb84f840542 -->
# 三平均研究最新总览与交接说明（2026-09-09）

持续更新至2026-09-10。并行研究的主线接口与已确认结论见[团队交接](../sources/outputs/triple_average/history/triple_average_team_handoff_2026-09-10.md)。

**最新统一条件归约：** [混合单点迹零返回](../sources/outputs/triple_average/history/triple_average_mixed_singleton_controller.md)证明，对每个p=2 mod3，只要两个显式缩放返回能在原p位置实现，周期、上下根、Schreier输送和终端即全部闭合。两个目标已有严格正三进副本运输；原位置半群分解是这条充分路线的唯一缺口，而非原猜想的必要形式。进一步的精确方程、返回商及高效短语法边界见[原位置分解前沿](../sources/outputs/triple_average/history/triple_average_original_position_factorization_frontier.md)。

**最新纯代数模型与判别式边界：** [Reynolds／Hecke／Hodge结构](../sources/outputs/triple_average/history/triple_average_reynolds_hecke_hodge.md)证明所有n>=5的原子生成有理代数等于End(V)，所以不能据完整代数推正向可达。1／3块重数的运输表给出全部普遍可执行层及伴随闭包；单三重块模型无损编码全部原子词，多个三块加双载体模型更小但只作为充分子系统。三元组交数s导致秩n-3-max(0,2-s)。B_p能量Hodge对偶因判别式p的一次赋值，将全部合法方向送到非法线，局部形如[[0,eta],[-p,0]]，正规化Iwahori但交换树边两端。ID reynolds-hodge-structure、contingency-layer-semigroup；最小未解仍53。

当前素数路线的集中入口是[证明路径与剩余猜想](../sources/outputs/triple_average/history/triple_average_prime_proof_roadmap.md)。该页将已证入口、条件性同余生成、已证终端与尚缺的正向种子／算术资源逐层分开，并指出全部Rp资源属于偏强的充分目标，只实现必要Schreier回路或合法轨道也可完成原问题。

**47元历史节点，后续最小未解已更新为71：** [完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_seven_arithmetic_complete.md)把新宽度一尖点词接到两个校正伸缩，得到C基下的E12(R)、E21(47R)，R=Z[1/6]。全部18个Schreier生成元的下左条目为0/47/94/141，单位提升和高斯消元逐个正向实现；48陪集与独立标签确认共轭Gamma_0(47)，唯一合法轨道可归零。47已加入solved_size因子闭包，冻结certificate_size不变；53、59随后也已完成。ID n47-complete。

**一般同余生成接口进一步闭合：** [局部化Iwahori生成](../sources/outputs/triple_average/history/triple_average_localized_iwahori_generation.md)用I、ST^j的统一陪集代表，证明Rp=Z[1/(p-1)!]上的正向上根、p倍下根与对角单位足以生成Gamma_0(p)。另证明对所有p和奇数k，特定R_p(3^-k)返回与标准A_p及pZ[1/3]平移产生同一个宽度一尖点。原维数普遍实现这些资源仍开放；47已实例化全部接口。ID localized-iwahori-generation。

**此前47元全库正向逆与统一素数目标：** [正向根群饱和](../sources/outputs/triple_average/history/triple_average_positive_root_saturation.md)证明一般二维迹根激活引理；由九个种子出发，46、113、2三层激活全部167旧模板，连同新增三宏共170个。固定JSON与独立重放无需重新搜索。Q(sqrt89)共轭有57模板正向词；整数换基后包含E12(47Z[1/6])、E21(47Z[1/6])。该阶段未完成的同余与合法轨道部分现由n47-complete补齐。ID b47-root-activation。

该页第6至8节回答素数策略：合数归约、全部p=1 mod3、高维进入与Bezout终端已统一；剩余是p=2 mod3的正向算术生成。明确充分猜想为C Gamma_0(p) C^(-1)包含于真实可逆正向群。此前共轭的限定搜索阴性记录仍保留，已被不同词形的正向实现越过。

**47元新增正向对合及整条局部化根群：** [固定接口](../sources/outputs/triple_average/history/triple_average_b47_extra_atom_and_adjoint.md)在旧两步预备后只加一个原子三平均，得到J、K、L三个全参数对合，实际平方为25/2187、25/2187、8/243。L与旧宏形成三个三因子周期，使标准A0等六宏都可正向取逆。时间词LBAbLa给出U(47)，A0共轭除以-3，词bL的斜率倍率为-2，因此正向群包含全部U(47Z[1/6])。尚无有限指数或完整终端覆盖，47仍开放。ID b47-extra-atom-involutions。

同页提炼(n-1)t+beta=3的对合模板方程；这个单参数对合族的两两乘积共用两条有理特征线，位于同一分裂环面，不能单靠它们生成模群有限指数。已证局部化平移可用于精确整性插值；本轮插值未闭合，停止不表示指数无限。新增extra字段不改变旧模板默认集合或既有短周期排除。

**伴随与共轭数域接口审计：** 倒序子集投影加源核投影形式上给出G^-1 A^T G；只有全部倒序子调用合法才是正向宏，只有A^TGA=lambda G才是射影逆。旧B47的167个形式伴随恒等式全部核对，15个倒序域普遍合法且都已在旧库。Q(sqrt89)目标共轭在额外3/9调用的20426/111393个限定中间态中未找到，不排除其他词形。ID adjoint-return-domain-audit。

**任意秩周期验证已统一：** [全局谱平衡判据](../sources/outputs/triple_average/history/triple_average_projective_spectral_balance.md)将有理A的有限射影阶等价为半单、全部复根等模、c_k^d/det(A)^k全部为整数。有限处由Newton单斜率证明，充分性由Kronecker单位根定理。Ad_A的分圆多项式检测给出给定矩阵的多项式时间精确算法，候选阶只需phi(m)<=d^2、m<=2d^4。它不证明可用宏词存在。ID projective-spectral-balance。

同页第8节补齐可交换数域乘法库的周期存在性接口：对S单位关系格取模有理尺度的饱和商，得到整数矩阵C；非零非负e满足Ce=0等价于正向标量周期，全严格正e等价于全部生成元有正向射影逆。实二次域还需一个单位指数行，不能只消去有限素理想赋值。给定关系矩阵后是有理线性规划；一般S单位基计算未实现、未宣称多项式。高斯范数周期是全正关系的显式实例。

**47元短周期范围已精确封闭：** [库边界](../sources/outputs/triple_average/history/triple_average_b47_cycle_frontier.md)对当前167模板排除全部长度1至4周期及任意j>=0的A0^jBC。4657463三因子、27160不同二因子；四因子737665600组合经整数模筛选仅3896幸存，精确复核全拒绝。浮点发现扫描另保留，不能与该证书混同。ID b47-short-cycle-boundary（full）。其中一个9/27/43调用宏是Q(sqrt89)的范数-2乘法，3处谱平衡却在2处分裂成不同赋值；它说明只看三进处不够。47及任意n仍未解。

**等值载体核与统一二进重分组：** [完整证明](../sources/outputs/triple_average/history/triple_average_paired_carrier_reset.md)用有限模桥安排安全的一步等载体入口，得到(u_i^3,a^2)核。其自然参数格Gram判别为2n*3^(r-2)，纯载体交换保持叶奇偶、故不可能有非空全局标量周期。固定12位置层K4/3通过两遍广播将叶模2矩阵变为J，再一次载体交换，在4r-3步得到W=2V，V为R可逆、det V=-3^(-(3r-2))。两个完整R理想均恰乘2，G保持。

新宏不自动周期：六个秩的迹整性均排除当前单宏有限射影阶，r5/7的全部5160个输出置换也被精确排除；一般标量词若只用W的置换共轭与额外载体交换，两类宏次数均须被r整除。虚拟射影点还存在总和障碍，不能凭两个载体相等就删掉。ID paired-carrier-two-adic-reset；最小未解仍为47。

**四十一元已完整解决，最小未解变为47：** [固定证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_one_arithmetic_complete.md)使用21个通用宏、10个三因子对合周期及10个整数词，独立验证42陪集、共轭Gamma_0(41)、属3及唯一合法尖点。子调用仅3/9/18/27/37/38/39；37使用已证分裂素数定理。完整输入输送由Bezout公式和安全核心完成，41已加入因子闭包。ID n41-complete。

**有限模控制尚不足以给出高度下降：** [统一高度边界](../sources/outputs/triple_average/history/triple_average_modular_height_barrier.md)在(1^(n-2),0,-(n-2))上反复局部载体交换，给出所有有限h的闭式。模任意指定M的正向恒等词保持G=1及本原剩余类，实能量严格下降，但本原高度精确为([4(n-2)^2+4n-11]3^(2h)+3)/4。ID modular-primitive-height-barrier，重放2304个实际操作。该结果不否定新模桥，只说明统一终止还需净实／三进控制。

**一般n=5 mod6的正向二例外归约已证：** [完整证明](../sources/outputs/triple_average/history/triple_average_two_carrier_modular_bridge.md)对每个n>=17（不要求素数）先作r个三元块加两个单位置的同时好划分，再用局部主同余群分别控制模n和模m，m为r=(n-2)/3的非三部分。模n常值稳定子保持全局合法性，保护模n的两个局部SL_r块在模m生成全部SL_(r+1)。有限模逆以统一ord_nm(-1/3)次幂正向实现，最后合法调用已解n-2元子块，输出G=1的(u^(n-2),a,b)核。此桥不依赖安全能量下降或因子归纳。

新桥不解决终止：素数二例外核在n-2非三幂时，单靠这个大子块调用没有安全的非平凡推进。必须区别子问题合法与全局安全；(5^15,1,-76)的15元子调用合法却产生全局G=17陷阱。ID two-carrier-modular-bridge，包含5条共567步的实际正向模调度样本。当前最小未解维数为47。

二例外参数x=u、y=a-b给出2E=n(n-2)x^2+y^2、G=gcd(y,n)；平均a与两个u后一步进入合法B_n，y_B=(nu+2y)/3。因此所有n=5 mod6、n>=17的多素数标准核接口已闭合。第6.1节另给出一般非三profinite原则：无条件R可逆正向宏的有限商像等于形式群像，可以启用任何有限同余适用域，但不能据此声称精确终端可达。

**二十九元已完整解决，最小未解变为41：** [完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)固定18个通用模板、9个三因子正向标量周期和7个整数生成词。精确折叠与独立模29标签给出完整30陪集、共轭Gamma_0(29)、唯一合法尖点及六步终端。全部调用大小仅3/9/25/27；最终证书使用冻结旧库的1194模板，不依赖本轮新增维数或扩展首步。ID n29-complete。29已加入任意幂和因子的闭包。

非分裂射影三阶轨道可在原p位置上组织成三块与二载体，但平移层可能奇异且不交换；p29的奇异位移为8/12/17/21。这解释了高斯范数循环不能直接迁移。ID nonsplit-projective-layer-boundary保留精确有限边界；41元随后由三因子对合和整数子群证书完成。

**全部p=1 mod3素数已统一解决：** [高斯周期正向控制器](../sources/outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md)直接在原p个位置上，以三阶乘法轨道及平移重分组构造高斯周期层。全部共轭的乘积为全局正标量；两个Eisenstein格周期恒等式给出根到根、根到单位坐标的稀疏映射。关键单位theta*conjugate(theta)-1的范数为1，由此对任意素数排除剪切系数的共同分子因子，正向实现所有整数平衡剪切和全部整数仿射行群。两次仿射正规形及一次高斯层消去差分gcd，最后九元网络归零。p=7/13用已证基例，其余p>=19由同一证明覆盖。

结合29、41元后续证书，任意n进一步归约到p=2 mod3、p>=47的素数。已解因子现在允许任意p=1 mod3，以及2、3、5、11、17、23、29、41；所有N>=9的三整除维数仍无条件解决。原子词长度未证明多项式。高斯证明不依赖Tits形式算术性，也未将扩张域作用当作原位置操作。核验ID split-prime-gaussian-controller；solved_size已更新，certificate_size未动。

**原维数形式群的算术性已统一：** [完整证明](../sources/outputs/triple_average/history/triple_average_flat_star_arithmeticity.md)从载体交换构造秩一幺幂、参数4的平衡剪切及行差剪切；结合Tits／Bass--Milnor--Serre初等同余群定理，r>=4的一载体群包含Gamma_r((192(3r+1))^2)，两载体群也含有限指数整数特殊线性子群。因此全部p>=13的原维数平坦核，形式群算术性不再逐素数开放。模2像为交错块置换群，模p像为常值向量稳定子，Goursat引理给出第一层直接乘积；每个合法第一层轨道有含零三重块的代表。尚未证明整体正向逆或更高层全部终端覆盖。ID flat-star-formal-arithmeticity。

**九十一元旧群等式已被否定：** [置换level与尺度耦合](../sources/outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md)发现模91倍率与模8标量共用二阶字符。显式矩阵(547,728;74256,98827)属于旧21504容器却不属于宏群。新必要容器指数43008，有192尖点、48合法尖点、属3473；它到旧属1737紧模曲线是无分歧二重覆盖。未证明宏群等于新容器。旧计算标签保留，91元整体的因子证明不受影响。ID cyclotomic-level-entanglement。

**副本宏的完整算术群已识别：** [数字同余群定理](../sources/outputs/triple_average/history/triple_average_digit_congruence_group.md)证明，n>=5时平衡剪切加置换等于整个整数保和／保常值群，限制到A_(n-1)为B*eta=eta模n的稳定子。若2<=q<=n-2且gcd(q,n)=1，再加入数字算子，恰得到B*eta=q^j*eta模n的同余群；它是阶ord_n(q)的分裂循环扩张。有理射影轨道由d|n及单位c模d对<-1,q>分类，合法d=1只有一个轨道。这是一般整数初等生成证明，不是有限模像推断；正向实现仍在q份副本上。核验ID balanced-digit-congruence-group。

原维数29的当前1195模板另经审计：714610个二因子乘积无有限周期；对任意j>=0，A^jB无有限周期，指数由五个精确二次迹方程一次处理，未作无限深度搜索。见[复核第11节](../sources/outputs/triple_average/history/triple_average_structural_picture_audit.md)，ID b29-current-cycle-boundary。不要继续只增加A重复次数；更长混合词、条件宏及平坦高秩核仍未被排除。

**一次三份复制已足够：** [完整证明](../sources/outputs/triple_average/history/triple_average_one_tripling_stabilization.md)给出数字算子KD=DF与Hilbert90周期，进而在三份副本上正向实现任意平衡剪切。至少五个整数坐标的轨道由总和、差分gcd和共同余类完全分类。结合同时好划分，所有N>=9且3整除N的维数均无条件解决，非三素因子任意；87元无需29元假设，123元同样无需41元假设。一般原维数充分性与复制消去仍开放。

**结构图景新增数域章节的复核：** [独立审计](../sources/outputs/triple_average/history/triple_average_structural_picture_audit.md)保留原稿并给出反例：固定输入的数域扩张不改变可达性，内容理想支撑及所提类群条件并非必要，O_K理想相等也会漏掉R加法模障碍。可用的辅助数域是宏矩阵的分圆Hilbert90及范数环面，不应与改变输入值域混同。核验ID为one-tripling-stabilization。

同一证明的第10节已推广到q平均：n>=max(5,q+2)、gcd(n,q)=1时，q份复制上的完整判据为G=1，核心是两个循环区间之差。原维数新接口见审计第9、10节：任意B_p一步进入三重块加一／二载体；同一组六项Artin关系给出七元局部中心收缩及五步正向逆。局部中心不与其他载体交换对易，拼接仍开放。对n>=9，一旦形成三个零即可用最近的三整除子块统一收尾。

**任意维数已严格归约到素数：** [总归约定理](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_to_primes.md)补齐v2=1、2。2p^e、4p^e的四例外核心用至多两次预备平均加十二元子问题减半；70、110、130的五行边界用一个可变深度梳状分裂修复，其余维数由统一容量强归纳处理。因此原猜想等价于全部素数p>=7的判据，合数接口不再是独立缺口。

因子归约允许任意二、三、五幂及已解奇素数的任意乘积；20、22、26、28等均已补齐。结合分裂素数族和29、41元，所有n>=7且素因子属于2、5、11、17、23、29、41或p=1 mod3均已解决，最小未解维数为47。仍未证明统一素数定理。

**奇数合数的统一乘法闭包已证：** [完整证明](../sources/outputs/triple_average/history/triple_average_odd_composite_factor_closure.md)将进位桥推广到r个例外，并用两个可选系数h=1、2满足行容量。结合n-d-2核心，已解素数集合P>=7的任意乘积和素数幂均可解；35元边界与[25元30陪集证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)均已补齐，因此可再乘任意三幂和五幂。当前P={7,11,13,17,19,23}；25、35、49、55、65、77、91、121、125、143等无限族已解。

全部奇数现已严格归约到全部p>=7素数：25元不再是条件，二例外入口也不再需要额外假设。25元证书只调用已解21元子问题，具有独立模25标签与唯一合法cusp。91元整体判据已经由7、13因子接口完成；后续耦合字符已证明旧(81,9,1)宏群不等于21504容器，是否等于新43008容器仍开放。

**此前的八整除阶段：** 同一因子容量证明先完成a>=3的二幂因子；新总归约已取消这个限制，因此二进指数也可任意。40、56、88、200等继续是已解族中的例子。

**其他AI报告重新复核：** [局部到整体综合](../sources/outputs/triple_average/history/triple_average_other_ai_local_global_review.md)重新读取AI-3运输与模板、AI-4高秩、AI-5复制报告，给出一个一般结构定理：任意连通的不等权块交换图，在加权零和空间的Zariski闭包为整个GL。证明使用秩一投影与Lie括号，非有限模像外推；算术有限指数和终端覆盖仍未证明。

同页加强交换为完整仿射格保护，并给出非零均值Burau的准确正向逆接口、跨链耦合的秩二公式，以及重新分组副本后一层平均与K/3双随机商的等价。可逆商的秩障碍排除无条件逐层消去。原AI文件保留，新发现与修正由主线综合页登记；当前已解维数不变。

**素数优先的归约推进：** [因子接口与三进进位定理](../sources/outputs/triple_average/history/triple_average_prime_first_factor_reduction.md)把素数算术与合数归约单列。对任意a>=7、b>=3，合法(u^(ab-2),v,w)可在至多ceil(log_3(a的非三部分))次原子操作后分成合法a元行及合法b元均值商。对(1^(ab-2),0,2-ab)且b含非三素因子，这个准备步数精确最优。X49直接七乘七划分失败，但两步进位即修复。

两份与三份复制的加法闭包结合十／十五元定理，可处理任意至少两份合法五元状态，因此因子5不需要假设错误的五元充分性。早期二例外桥已推广到d+2核心，25元和低二进重数接口也均已补齐。剩余统一任务是素数核。

modern frame 已按用户要求[重写](../sources/outputs/triple_average/history/triple_average_unified_modern_framework.md)，[完整原稿](../sources/outputs/history/triple_average_unified_modern_framework_before_2026-09-10_revision.md)已存档且哈希核对一致。修改理由见[主线严格化说明](../sources/outputs/triple_average/history/triple_average_modern_framework_review_and_contract.md)：全体真实宏使用带适用域的有向范畴，只有正向可逆子类形成群胚；终端反向可达集需额外的覆盖与终止证书。

**二十三元已完整解决：** [完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md)用15、17、24步固定原子宏和指数24子群收尾。该模曲线属为2，仍由一个合法cusp完成。它现在作为总归约的素数基例；最小未解维数是29。

**同轮十九元完成：** [完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_nineteen_arithmetic_complete.md)通过七个通用十五元调用宏和指数20子群闭合19*3^k。内部调用允许依赖参数；二十三元最终宏已经全部原子化。不要把两种证书的长度混同。

**素数结构与搜索前筛选：** [稳定子和尺度周期定理](../sources/outputs/triple_average/history/triple_average_prime_congruence_structure.md)说明，保持素数p合法方向的群，其整数部分受共轭 Gamma_0(p) 约束；但真实正向群达到这一上界并非自动成立。23处不能复制负三进单位循环，实际成功的尺度是4/27与2/3^7，因此不能丢掉物理比例或忽略2处。整系数编译器缓存重数选择与支撑格，95个十七元矩阵与旧版逐项一致，222个十九元、60个二十三元模板均通过独立 Fraction 重放。

**此前十七元完成：** [完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_seventeen_arithmetic_complete.md)构造固定原子逆词，给出共轭 Gamma_0(17) 的指数18充分子群、六步终端和一般进入桥。十九元用的是通用十五元调用，内部路径可能依赖参数，不能把两种证书长度混同。

**一般方法进展：** [参数无关子问题调用与范数环面](../sources/outputs/triple_average/history/triple_average_universal_subproblem_lattice.md)的任意参数维数模包含判据驱动了这次发现。十七元进一步给出统一充分目标：对 n>=9，若真实正向 B_n 群包含 C Gamma_0(N) C^-1，N为n的非三部分、C=[[1,0],[1,1]]，则整个 B_n 核由同一 Bezout 公式收尾。该包含对任意n尚未证明，多危险素数的一般进入桥也仍开放。

历史阶段的五宏有17／19步原子证书和35步调度。那个特定无条件宏半群不含 B 的固定逆词；新增 Q、T、U 宏已打破其模3不变集。48类十四元预备调度的净下降没有被证明，其中一支实际处处增高；完整十七元证明由新的群轨道方法完成，不依赖这个旧调度成为下降算法。

对应的首个[十七元带条件调用实验](../sources/outputs/triple_average/history/triple_average_b17_guarded_subproblem_experiment.md)已生成10个真实返回模板，逐项核验局部整除域与输出合法性。高度24、至多12次调用中542/683个方向可下降或进入已知终端，141个未覆盖，未得到十七元定理。深度指子问题调用而非原子操作。

旧库的缺口已加强为一个有证明的无限不变域：[旧库第5节](../sources/outputs/triple_average/history/triple_average_b17_guarded_subproblem_experiment.md)。历史[奇背景跨核桥](../sources/outputs/triple_average/history/triple_average_b17_cross_stratum_escape.md)给出受限逃逸及一个净下降见证；最新的通用 B 宏调度已去掉该桥的奇偶、模7和模13限制。[同余方法边界](../sources/outputs/triple_average/history/triple_average_congruence_method_scope.md)则说明有限有理轨道原则的准确条件，并给出有限模像很大但指数无限的反例。

**二三光滑维数已统一：** [完整证明](../sources/outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md) 给出对所有 \(8\mid n,\ n\ge16\) 的 B 核安全减半模板，结合八、十二、十八元定理完成全部 \(2^a3^b\ge7\)。该结果包含16、32、64等无限多个二幂及其三进塔。

**结构核接口加强：** [所有偶维 B 核减半](../sources/outputs/triple_average/history/triple_average_all_even_B_kernel_halving.md) 已覆盖任意偶数 \(n\ge14\)。若 \(n/2\) 维可解，则合法 B_n 可解；尚不提供多危险素数一般输入的高维进入桥。

**奇素数维数的策略限制：** [子问题调用的缺失素数障碍](../sources/outputs/triple_average/history/triple_average_subproblem_prime_obstruction.md) 证明：若调用大小都不含某个 \(p\mid n\)，统一有界次数的调用不能覆盖全部合法 B_n 有理方向。因此十七元不能仅靠有限深度的严格更小子问题调用表完成，必须保留可重复的局部归约循环或群轨道机制。这是算法结构下界，不是不可达结论。

**B17 范数环面接口：** [普遍子问题格判据](../sources/outputs/triple_average/history/triple_average_universal_subproblem_lattice.md)中的 B 在 \(\mathbb Q(\sqrt{-2})\) 中是范数3乘法。现在其共轭素元已由61步正向词实现；两个 theta 格分支均有真实操作。核的全覆盖另由级17同余子群完成，两种算术对象的作用不应混同。

本文是在保留全部旧笔记基础上的最新权威索引。阅读时以本文、[研究勘误](../sources/outputs/triple_average/history/triple_average_research_corrections.md) 和各个“完整判据/定理”文档为准；早期探索稿保留发现过程，其中被后续结果替代的开放问题或猜测不应继续引用为当前结论。

**一般结构与十四元完成：** [危险支持集图论核心](../sources/outputs/triple_average/history/triple_average_blocker_graph_core.md) 将安全终端的重复值下界提高为 \(n-d-2\)。借此，[十四元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_fourteen_complete.md) 把最后缺口缩为两个不交危险二元组，并用512个模8／模7模式的至多两步预备操作接入十二元定理与 B14 减半桥，完成 \(14\cdot3^k\) 全部维数。

**十二元完成：** [十二元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md) 的四个真实宏含正向逆元，生成一个共轭于 \(\Gamma_0(8)\) 的指数 12 子群，其唯一合法尖点可终止。它解决了 \(12\cdot3^k\) 整条维数族，并被后续十四、十五、十八元归约调用。

**进一步推广：** [十八元及其三进塔](../sources/outputs/triple_average/arithmetic_cases/triple_average_eighteen_via_twelve_complete.md) 已通过调用合法十二元子问题、形成偶重数、分成两份三幂零和块证明。新增 \(18\cdot3^j\) 全部维数，无须单独建立 B18 算术群。B21 深度五已改用整数状态商，同样八进程从约 98 秒降至约 11 秒，见 [性能复核](../sources/outputs/triple_average/history/triple_average_b21_integer_search_optimization.md)。

**十五元完成：** [十五元完整归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md) 利用模8八循环，先调用十二元子问题，再调用十元子问题归零。新增 \(15\cdot3^k\) 全部维数；不依赖新的十五元大算术群。[偶维 B 核减半桥](../sources/outputs/triple_average/history/triple_average_even_kernel_halving_bridge.md) 本身只解决结构核，十四元一般输入的进入步骤由最新完整证明另行提供。

## 1. 当前总问题

将输入中心化、清分母并本原化，得到

\[
X=(x_1,\ldots,x_n)\in\mathbb Z^n,
\qquad \sum_i x_i=0,\qquad\gcd_i x_i=1,
\]

并定义

\[
G(X)=\gcd_{i<j}|x_i-x_j|.
\]

对任意 $n$，可达都蕴含 $G(X)\mid n$ 且 $G(X)$ 是三的幂。主猜想仍是

\[
\boxed{n\ge7:\quad X\text{ 可达}\iff G(X)=3^a.}
\tag{1.1}
\]

式 (1.1) 尚未证明。若它成立，判定算法只需规范化、求 gcd 和反复除以 $3$，所以直接是输入总位长的多项式时间算法；平均路径是否有多项式长度是另一个更强的问题。

## 2. 已经完整解决的维数

目前已证明：

最新完整族可以统一写成
\[
n=2^a3^b5^c7^{e_7}11^{e_{11}}13^{e_{13}}17^{e_{17}}19^{e_{19}}23^{e_{23}}\ge7,
\]
所有指数任意非负。以下较早的族都包含于这一结论中。

\[
n=3^k;\qquad
n=2^a3^b\ge7;\qquad
n=m3^k\quad(m\in\{7,10,11,13,14,15,17,19,23\},\ k\ge0).
\tag{2.1}
\]

最新再加入整个乘法族
\[
n=3^a5^b\prod_{p\in\{7,11,13,17,19,23\}}p^{e_p}\ge7,
\qquad a,b,e_p\ge0.
\tag{2.2}
\]
这包括35、49、77、91等，不是逐个维数的有限样本结论。

还有全部
\[
n=2^a3^b5^c\prod_{p\in\{7,11,13,17,19,23\}}p^{e_p},
\qquad a\ge3,\quad b,c,e_p\ge0.
\tag{2.3}
\]

这些维数中，$G$ 为三幂是充要条件。五元和六元有 $G=1$ 的反例；结合后续分裂素数族与29、41元证书，最小尚未闭合的 $n\ge7$ 是 $47$。

各基维数证明见：

* (25)：[二十五元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)；

* 奇数合数乘法闭包及35元：[多例外因子归约](../sources/outputs/triple_average/history/triple_average_odd_composite_factor_closure.md)；

* (23)：[二十三元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md)；

* (19)：[十九元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_nineteen_arithmetic_complete.md)；

* (17)：[十七元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_seventeen_arithmetic_complete.md)；

* 二三光滑维数：[统一减半与归纳](../sources/outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md)；

* (7,8)：[七元与八元完整判据](../sources/outputs/triple_average/proofs/triple_average_seven_eight_complete.md)；
* (10)：[十元完整判据](../sources/outputs/triple_average/proofs/triple_average_ten_complete.md)；
* (11)：[十一元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_eleven_complete.md)；
* (12)：[十二元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md)；
* (18)：[十八元完整归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_eighteen_via_twelve_complete.md)；
* (15)：[十五元完整归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md)；
* (14)：[十四元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_fourteen_complete.md)；
* (13)：[十三元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_thirteen_arithmetic_complete.md)。

三进塔传播和同时好划分见 [一般维数综合](../sources/outputs/triple_average/history/triple_average_general_n_synthesis.md)。

## 3. 任意维数已经完成的两个归约

第一，[复制稳定化定理](../sources/outputs/triple_average/history/triple_average_stabilization_theorem.md) 证明：

\[
G(X)=3^a
\iff
\text{每个坐标复制某个共同三幂次数后可达}.
\]

它等价于存在 $\mathbb Z[1/3]$ 上的正双随机矩阵 $P$ 满足 $PX=0$。原猜想因而等价于 $n\ge7$ 时的“三份复制消去”。稳定化已经消除了所有复制后仍存在的算术障碍，但没有取消原维数中的额外副本。

第二，[三幂分块压缩定理](../sources/outputs/triple_average/history/triple_average_power_partition_reduction.md) 证明任意合法 \(n\) 元输入可在 \(O(n\log n)\) 次真实三平均后进入

\[
(u_1^{r_1},\ldots,u_t^{r_t}),\qquad
r_i=3^{k_i},\quad t=O(\log n),\quad\sum_i r_i=n,
\tag{3.1}
\]

并保持 $G$ 为三幂。多危险素数的高维组合压缩因此已经统一；未解部分集中在对数秩三幂权重核。

## 4. 最新突破：Burau 幂链群

若式 (3.1) 的权重形成几何链

\[
R s^{t-1},R s^{t-2},\ldots,R,\qquad s=3^k,
\]

相邻块之间的真实扩张宏给出参数 $1/s$ 的 Burau 表示。它们满足 Artin 辫子关系；Coxeter 乘积 $C$ 在加权零和空间上满足

\[
C^t=s^{-t}I.
\]

由此每个相邻宏的射影逆元都能写成正向宏词。换言之，任意秩几何链上的正向平均宏半群自动成为射影群。

完整定理与证明见 [Burau 幂链定理](../sources/outputs/triple_average/history/triple_average_burau_power_chain.md)。它统一了十三元 $(9,3,1)$ 核中的三阶分圆关系，并给出 $(27,9,3,1)$ 核上参数空间维数为三的可逆 Burau 返回群；尚未给出其完整下降控制器。

这个结果没有直接证明一般核可达。关键边界是：几何链必须对自身加权零和，嵌入更大核后的非零链平均会阻止正词成为整个状态上的射影逆元。一般问题现在具体化为“链之间转移加权和”以及“Burau 像是否足够算术”两件事。

## 5. 九十一元支线的最新复核

**当前总状态：91元已经由奇数合数因子定理完整解决。** 以下保留旧(81,9,1)独立局部容器的支线；后续耦合字符已证明该21504容器严格过大，新43008容器见本页顶部链接。

核

\[
(u^{81},v^9,-81u-9v)
\]

仍有统一的三个真实宏，但旧的群论候选需要两处修正。

第一，本原化允许差值乘子属于

\[
\langle-1,3\rangle\subset(\mathbb Z/91\mathbb Z)^\times,
\]

而不是只用 $\langle-1,9\rangle$。只记录模 $91$ 行标签与模 $2$ 奇偶时得到指数 $1344$ 的粗容器。

第二，真实整数返回宏还带有模 $8$ 条件。当时的独立局部容器使用六元素局部像

\[
L_8=\langle C_9,3I\rangle,
\]

指数为

\[
21504.
\]

这个历史容器有 $96$ 个尖点，其中 $24$ 个满足 $G=1$，恰为六个模 $91$ 差值类各分四个二进尖点。现在已经证明真实整数宏群严格包含于它，不能把这组尖点当成实际宏群的完整轨道分类。

旧缺失类代表也曾写错：对 $(u,v)=(1,-3)$，单独坐标是 $-54$，不是 $-72$。正确两步路径为

\[
(1^{81},(-3)^9,-54)
\to(1^{81},(-3)^7,(-20)^3)
\to(1^{79},(-3)^7,(-20)^2,(-6)^3).
\]

其中 $1^{21},(-3)^5,-6$ 是 $27$ 元零和块；归零后剩余 $64$ 个非零位置与 $17$ 个新零组成 $81$ 元零和块。因此六个模 $91$ 差值类都存在终端。深度四的离核搜索覆盖旧容器中 $23/24$ 个合法尖点；随后对尖点 $29$ 的深度五搜索又得到一条五步证书，完成旧容器的 $24/24$ 有限深度覆盖。它不自动覆盖新容器的48个合法尖点；该支线不再承担91元整体判据的证明。

## 6. 现阶段最接近一般证明的结构

目前可以把全局路线画成

\[
\text{任意合法输入}
\longrightarrow
\text{对数秩三幂核}
\longrightarrow
\text{几何链 Burau 群与链间耦合}
\longrightarrow
\text{零和三幂终端块}.
\]

第一箭头已经证明。第二层中的单条几何链已经群化。真正未解的是：

1. 把任意三幂权重多重集组织成少量链，并在链之间可控地移动加权和；
2. 证明所得高秩返回群是足够大的算术群，而不是薄群；
3. 证明每个满足全部非三局部条件的有理轨道都与某个零和三幂子块相交；
4. 或者从复制稳定化一侧，直接证明这些核上的三份复制可以消去。

十三元的参数格维数为二，相应 PGL2 的群秩为一。Burau 定理提示研究更高参数维数的算术群与终端超平面；奇异降维宏另属分层间有向对应，不能全部视为群作用。

## 7. 哪些文档应如何阅读

已证明定理、总纲与勘误：

* [研究总纲](../sources/outputs/triple_average/history/triple_average_master_summary.md)
* [研究勘误](../sources/outputs/triple_average/history/triple_average_research_corrections.md)
* [复制稳定化](../sources/outputs/triple_average/history/triple_average_stabilization_theorem.md)
* [三幂分块压缩](../sources/outputs/triple_average/history/triple_average_power_partition_reduction.md)
* [Burau 幂链](../sources/outputs/triple_average/history/triple_average_burau_power_chain.md)
* [可填充三幂块](../sources/outputs/triple_average/history/triple_average_zero_padding_theorem.md)
* [单危险素数降维](../sources/outputs/triple_average/history/triple_average_isolated_prime_reduction.md)
* [多危险素数核心](../sources/outputs/triple_average/history/triple_average_multi_prime_core.md)
* [加强图论核心](../sources/outputs/triple_average/history/triple_average_blocker_graph_core.md)：将上一项的 \(n-3d-1\) 提高为 \(n-d-2\)，且明确一步 B 核桥并非自动安全。
* [二三光滑维数](../sources/outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md)：通过十二元子问题统一消去额外二因子。
* 上述九个已解决起始维数的完整证明（12、15、18 含三因子，分别是一条新传播塔的起点）。

严格接口、条件定理和开放猜想：

* [标准核接口与自守路线](../sources/outputs/triple_average/history/triple_average_kernel_interface_and_automorphic_route.md)
* [q-平均根格与 \(S\)-算术控制器](../sources/outputs/general_arity/triple_average_q_average_arithmetic_geometry.md)
* [三进扩张修复宏与算术接口](../sources/outputs/triple_average/history/triple_average_carry_repair_and_arithmetic_interface.md)：含一般宏族与下界证明，完整控制器仍开放。
* [B12 六步下降与导子塔](../sources/outputs/triple_average/history/triple_average_b12_six_step_and_conductor_tower.md)：保留十二元闭合之前的局部范数路线，以及严格 theta 子格公式。
* [十二元四宏的参数延拓](../sources/outputs/triple_average/history/triple_average_twelve_macro_family_extension.md)：三个真实宏可延拓，但已用的二阶和抛物关系只在十二元成立。
* [偶维 B 核减半桥](../sources/outputs/triple_average/history/triple_average_even_kernel_halving_bridge.md)：对 \(n=2\pmod4,\ n\ge14\) 给出调用八元子块的减半接口。

有限实验与审核记录：

* [B12 二维核有限实验](../sources/outputs/triple_average/history/triple_average_b12_kernel_experiment.md)
* [四维数核比较](../sources/outputs/triple_average/history/triple_average_single_prime_kernel_comparison.md)
* [外部 audit 修订记录](../sources/outputs/triple_average/history/triple_average_audit_resolution_2026-09-09.md)

结构解释文档仍然有用，但应连同勘误阅读：

* [根格与一般维数综合](../sources/outputs/triple_average/history/triple_average_general_n_synthesis.md)
* [算术几何视角](../sources/outputs/triple_average/history/triple_average_arithmetic_geometry_view.md)
* [测度、托里克与重写视角](../sources/outputs/triple_average/history/triple_average_barycentric_toric_view.md)
* [覆盖设计障碍](../sources/outputs/triple_average/history/triple_average_covering_design_obstruction.md)
* [见证重置](../sources/outputs/triple_average/history/triple_average_witness_reset_lemma.md)

早期探索记录包括 `ternary_averaging_*`、`binary_vs_ternary_averaging_followup.md`、`triple_average_global_breakthrough.md`、`triple_average_arbitrary_n_outlook.md` 与 `triple_average_thirteen_macro_frontier.md`。它们保存搜索过程和局部引理，但其中“待解决维数”、旧公式、算法边界或实验外推可能已经被后续文档替代。

## 8. 核验入口

完整的“结论—文档—脚本—命令—输出—证据边界”映射见 [计算核验指南](../sources/outputs/algorithms/triple_average_verification_guide.md)。机器可读清单为 `work/verification_manifest.json`，统一入口为：

```text
python work/run_verifications.py --list
python work/run_verifications.py --profile smoke
python work/run_verifications.py --profile core
```

其中最关键的精确核验为：

```text
work/verify_thirteen_arithmetic_group.py
work/verify_twelve_arithmetic_group.py
work/verify_stabilized_averaging.py
work/verify_power_partition_compression.py
work/verify_burau_power_chain.py
work/cyclotomic_congruence.py
work/analyze_n91_terminal_cusps.py
```

Burau 核验对 $3\le t\le8$、$s=3,9$ 的十二组参数全部通过。九十一元脚本区分“真实宏群”“已知同余容器”和“终端覆盖”，不再把粗模 $91\times2$ 标签误当作完整群。

九十一元深度四的 $23/24$ 用

```text
python work/analyze_n91_terminal_cusps.py --depth 4
```

重现；脚本默认深度为 $2$，覆盖 $14/24$，深度 $3$ 覆盖 $20/24$。优化后的深度 $4$ 默认使用全部逻辑处理器，本机实测约 $14.2$ 秒（前一版整数 DP 约 $118$ 秒），找到尖点 $30,32,35$ 的新证书。随后对唯一开放的尖点 $29$ 使用

```text
python work/analyze_n91_terminal_cusps.py --cusp 29 --depth 5 --jobs 8 --split-depth 2
```

在本机用时约 $273$ 秒，得到五步终端证书，因此已知同余容器内的 $24/24$ 个合法尖点均有有限深度见证。程序中的 `OPEN` 是有限深度内未找到见证，不是不可达证明；$24/24$ 仍不等于真实返回宏群等式，也不替代任意输入进入二维核的桥。性能剖析与优化依据见 [计算性能审计](../sources/outputs/algorithms/triple_average_computation_performance_audit.md)。

## 9. 当前结论

现在还不能宣布任意 $n\ge7$ 已解决，但它已经严格等价于全部素数p>=7的判据。d+2核心、奇数因子桥、低二进减半及有限边界修复共同闭合了所有合数归约。结合分裂素数统一证明和29、41元证书，最小未解维数为47。下一步可在最小反例素数p的假设下使用全部更小维数已解子问题，集中研究非分裂正向控制；复制消去仍为等价路线。有限模调度本身没有控制本原高度，必须另证整个词的净下降或全局周期。

<!-- END SOURCE doc-afb84f840542 -->

---

<a id="doc-d41c21d90b67"></a>

## 原文导签：更内在的代数对象：Reynolds 半群、交叉计数与判别式对偶

来源：`outputs/triple_average/history/triple_average_reynolds_hecke_hodge.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_reynolds_hecke_hodge.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`reynolds-hodge-structure`, `contingency-layer-semigroup`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-d41c21d90b67 -->
# 更内在的代数对象：Reynolds 半群、交叉计数与判别式对偶

日期：2026-09-10。当前最小未解维数仍为53。本文回应一个具体问题：能否把尚缺的正向实现完全交给代数或数论，而不是继续猜返回宏？

结论分两层。原问题可以无损地转成一个明确有限生成的有理矩阵半群问题；在统一分块空间内，还可以将每个允许字母直接写成整数运输表，使物理实现条件自动满足。但用这个半群的线性包、整个算术群或凸包替代它会严格丢失信息。本轮给出两项一般定理解释这种损失，并提出一个保留全部正向信息的Hecke型模型。

## 1. 三平均恰是有限群的 Reynolds 投影

令V为Q^n的零和标准表示。对三元组S={i,j,k}，取三循环sigma=(ijk)，用rho表示置换表示。一次真实三平均准确等于
\[
P_S=\frac{I+\rho(\sigma)+\rho(\sigma)^2}{3}.
\tag{1}
\]
所以它是循环子群C3的Reynolds幂等元，既自伴又满足P_S²=P_S。全部原子操作来自Q[S_n]，也来自Q[A_n]。

记有限生成半群
\[
\mathscr S_n=\langle P_S:|S|=3\rangle.
\]
原问题准确等价于给定x，判断
\[
\exists W\in\mathscr S_n,\qquad Wx=0.
\tag{2}
\]
这是特殊的有理矩阵半群向量消灭问题。它已是纯代数命题，没有遗漏物理步骤；每个字母都是真的一次平均。但“已经转写成矩阵半群”与“存在可直接求解它的已知定理”是两回事。本文不宣称一般矩阵半群的不可判定结果适用于这个特殊自伴幂等字母表。

## 2. 新的一般定理：生成代数早已是整个矩阵代数

**定理。** 对所有n>=5，P_S在V上生成的有理含幺结合代数是End_Q(V)。

这有显式证明，不需要仅凭不可约性援引Burnside定理。对i<j，置
\[
L_{ij}=(e_i-e_j)(e_i-e_j)^T,
\quad T_{ijk}=3(I-P_{ijk})=L_{ij}+L_{ik}+L_{jk}.
\]
记\(L=\sum_{i<j}L_{ij}\)、\(L_i=\sum_{j\ne i}L_{ij}\)。有
\[
L=\frac1{n-2}\sum_{i<j<k}T_{ijk},
\]
\[
L_i=\frac{\sum_{\{j,k\}\subset[n]\setminus\{i\}}T_{ijk}-L}{n-3},
\]
\[
\boxed{L_{ij}=\frac{\sum_{k\ne i,j}T_{ijk}-L_i-L_j}{n-4}.}
\tag{3}
\]
故所有根秩一算子都在生成代数中。以r_i=e_i-e_n为V的基，r_i^T r_j在i!=j时为1、在i=j时为2，因此
\[
L_{in}L_{jn}=(r_i^Tr_j)r_ir_j^T.
\]
这些秩一算子张成End_Q(V)，证毕。

这个结论对存在反例的n=5同样成立。因此，完整矩阵代数、绝对不可约性或其线性表示类别，不能区分五元失败与较大维数成功。式(3)用了减法和任意有理系数，而正向平均只允许乘积；关键差别在乘法子集，不在生成的代数有多大。

## 3. 凸化同样会消去有限步问题

全体原子投影的平均准确为
\[
\frac1{\binom n3}\sum_{|S|=3}P_S
=\frac{J_n}{n}+\frac{n-3}{n-1}\left(I-\frac{J_n}{n}\right).
\tag{4}
\]
在V上它只是正标量\((n-3)/(n-1)\)乘I。因此，若允许“对许多不同操作词作外部随机混合”，就立刻得到各方向完全平衡的收缩；重复后其期望趋零。但一次随机选择或平均矩阵并不等于一条确定的正向词，更不保证有限时间准确为零。

另一个严格边界是：若同一个词对所有零和输入归零，则它在Q^n上必须为J_n/n。真实词的条目属于Z[1/3]，故只有n为3幂时可能；三幂网络证明该条件也充分。原猜想在其余维数必然依赖输入选词。

在已解素数的B_p射影线上，可达方向恰为p不整除u-v的本原有理方向。它与补集都无限，因此不是P1上的Zariski可构造子集。单纯的有限代数簇分层也不能完整表达这个p进合法域；需要保留整格或局部条件。

## 4. 把位置账本压成一个完全合法的有限字母表

取块重数w=(w_1,...,w_d)，每个w_i只为1或3，总质量n。以块值z为参数，令D=diag(w)。定义有限集合
\[
\mathcal C_w=\{M\in M_d(\mathbb Z_{\ge0}):
M\mathbf1=w,\ M^T\mathbf1=w\},
\]
及有理矩阵
\[
Q_M=D^{-1}M.
\tag{5}
\]

**精确实现定理。** M属于C_w，当且仅当它描述一层原n位置的重分组：第i个输出块从第j个输入块取M_ij个实际位置；大小3的输出块做一次三平均，大小1的保留。输出块值恰为Q_M z。

证明：列和保证每个输入副本恰使用一次，行和保证输出容量；在每个输入块内任意分配不同位置即可。反向直接数交叉位置。这个证明对全部有理参数同时成立，没有更小子问题调用，也没有隐含gcd守卫。

因此固定重数上的所有这种层都对应有限有理矩阵半群
\[
\mathscr T_w=\langle Q_M:M\in\mathcal C_w\rangle.
\tag{6}
\]
字母数量可能很大，不宜立即全部枚举，但每个字母的存在、适用域和一步实现已经被行列和条件完全解决。它包含全部单载体／双载体交换以及已有的12位置叶重分组层。

更强地，这个半群自动关于加权伴随封闭：
\[
Q_M^\dagger=D^{-1}Q_M^TD=D^{-1}M^T=Q_{M^T}.
\tag{7}
\]
M^T仍属于C_w，所以倒序伴随在这一完整层字母表中确实正向可用。此前特定B_p大子块宏的倒序域可能失败；这里全部输出块仅为1或3，故没有那个适用域问题。伴随仍不等于逆。

## 5. 这是准确的有限 Hecke 型角，而不是类比

固定实际块划分，令H为各三重块内部S3的直积，单点对应平凡因子。H的平均幂等元e_H将状态投影到块常值空间；它本身就是对不交三块各平均一次，真实可执行。

对任意位置置换g，算子e_H rho(g)e_H限制到块常值空间，恰为(5)。双陪集H\S_n/H由交叉计数M分类。因此(6)是有限Hecke角
\[
e_H\mathbb Q[S_n]e_H
\]
在块值空间表示中的一个明确乘法半群。普通Hecke代数允许对双陪集算子求和；我们保留的是实际矩阵乘积，所以没有把Hecke求和中的某个项擅自当成可用动作。

位置置换只负责选择输出块并重新记账。若在原操作词间显式插入置换，可以将其共轭移到末端，同时把后续三元组标签改写；末端置换不影响零状态。故这个表示不会额外允许改变数值的操作。

取w=(3,1,...,1)，只保留一个三重块时，这个有限Hecke乘积模型已经能编码任意非空原子词：每次平均后将被选三元组作为标准块，其余作为单点。因而在第一次平均之后，原问题可以无损地写成维数n-3的有理矩阵半群向量消灭；没有未知的宏实现条件。

取更紧凑的w=(3,...,3,1,1)时，模型只允许完整重分组层，是原过程的一个明确子系统；不能未经证明把所有原子词都压成这个固定重数。其优点是维数约n/3，并且已有的统一入口与载体群都处于其中。

## 6. 秩变化由三元组交数决定

设F_S={x in V:x在S上相等}，dim F_S=n-3。对另一个三元组T，P_T限制到F_S的核为
\[
F_S\cap\ker P_T,
\]
后者是在T上支持、总和为零，且S上的值相等的向量。

若s=|S交T|，直接分情况得到
\[
\boxed{\operatorname{rank}(P_T|_{F_S})
=n-3-\max(0,2-s).}
\tag{8}
\]

| 交数s | 降秩 | 含义 |
|---|---:|---|
| 0 | 2 | 独立的差分平面被消去 |
| 1 | 1 | 两个剩余位置之间的差分被消去 |
| 2 | 0 | 核内可逆转移，但未必有正向逆 |
| 3 | 0 | 原投影在当前层上为恒等 |

这把可逆部分与降秩箭头自然放在同一个有限Hecke型结构中，而不是先假设所有动作都属于PGL2。式(8)针对整个F_S；一个长词的实际像可能是更小子空间，后续真实降秩还需计算与核的相交。

## 7. 新的判别式障碍：为什么伴随不能自然变成逆

在二维有理空间上给定正定对称Gram矩阵G，令
\[
\Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
J_G=G^{-1}\Omega,\quad A^\dagger=G^{-1}A^TG.
\]
二维线性代数给出
\[
J_G^2=-\frac1{\det G}I,\qquad
J_G^TGJ_G=\frac1{\det G}G,
\]
\[
\boxed{J_GA^\dagger J_G^{-1}=\det(A)A^{-1}.}
\tag{9}
\]
因此如果能正向实现伴随与规范四分之一转J_G，所有逆元都可统一得到，不必寻找周期。

但B_p能量格恰好阻止这个办法。写m=p-4，其Gram矩阵为
\[
G_p=\begin{pmatrix}m(m+1)&3m\\3m&12\end{pmatrix},
\qquad\det G_p=3pm.
\tag{10}
\]
在p>3处判别式赋值为1，G_p模p的根空间恰为ell=F_p(1,1)，也是不合法方向。

J_G的一个整数射影代表为
\[
\Omega G_p=\begin{pmatrix}3m&12\\-m(m+1)&-3m\end{pmatrix}
\equiv12\begin{pmatrix}-1&1\\-1&1\end{pmatrix}\pmod p.
\tag{11}
\]
对任意本原合法(u,v)，其像模p是非零的12(v-u)(1,1)。所以像本原化后仍为不合法方向。

**结论。** 对每个p>3，能量规范四分之一转都不保持B_p合法域，因此不能属于合法域上的正向可逆群。进一步，对p>=11，它不可能是对全部有理B_p参数都可执行的返回宏：取已经能由九元网络归零的z=(0,1)，令x=J_Gz，则x不合法，而J_Gx为z的非零倍数；若J_G在这个不合法x上也可执行，就违反共同余数障碍。

最后一句使用了“全部参数可执行”。若一个动作仅在合法输入定义，并将其送入不合法陷阱，这本身并不矛盾，因为真实平均可以破坏合法性。此时能排除的是它作为保持合法域的可逆控制器，而不能误称任何这种单向丢弃动作都不可能。

这个排除不是缺少某条短词，而是整格判别式决定的局部不相容。需要谨慎区别：形式算子存在、保持实能量到尺度、具有射影二阶，都不能推出真实正向可执行。

## 8. 与局部 Fricke／Atkin--Lehner 对合的精确联系

令
\[
P=\begin{pmatrix}1&0\\-m/4&1\end{pmatrix}.
\]
它在p处整可逆，且P模p等于前述C。直接得到
\[
P^TG_pP=\operatorname{diag}(pm/4,12),
\]
\[
[P^{-1}J_GP]=
\left[\begin{pmatrix}0&\eta\\-p&0\end{pmatrix}\right],
\qquad\eta=48/m\in\mathbb Z_{(p)}^\times.
\tag{12}
\]
记右侧代表为w。对局部Iwahori矩阵[[a,b],[pc,d]]，有
\[
w\begin{pmatrix}a&b\\pc&d\end{pmatrix}w^{-1}
=\begin{pmatrix}d&-\eta c\\-pb/\eta&a\end{pmatrix}.
\tag{13}
\]
因此w正规化Iwahori，却交换它所稳定的树边两端。射影参数x/y属于Z_p时，w把它送到\(-\eta/(p(x/y))\)，即另一侧；x=0送到无穷远。这就是局部Fricke／Atkin--Lehner型对合的准确形式。

这里仅断言p处的标准正规化子结构，不将含额外有理单位eta的矩阵擅自认作某个全局模曲线的经典w_p算子。其全局整性在其他素数处另有条件。

还有一个数域层面的解释：J_G生成虚二次域Q(sqrt(-det G_p))，即Q(sqrt(-3p(p-4)))；因为p>3且判别式的p赋值为1，p在这个二次域中分歧。能量形式、局部格的非自对偶性和跨树边的对偶动作在同一个分歧处相遇。这比仅给二次型附上theta级数更直接地触及正向实现的限制。

同时，不应把J_G的障碍误读为伴随本身必破坏局部合法性。由(9)、(13)，能量伴随将自然Iwahori仍送到自身：它是取逆再用正规化子共轭。困难是从正向可用的A^dagger得到A^(-1)还需那个不可直接执行的共轭。即使某个字母表关于伴随封闭，也不自动关于逆封闭。

这解释了一个此前没有指出的结构：最自然的伴随取逆机制需要交换合法域两侧，而真实可逆宏必须留在同一侧。可以尝试在另一个参数格中实现对偶，或把两次跨侧代数动作合并成保持合法域的整体宏；不能让中间真实状态先落入不可达公共余类。

## 9. 由此得到更准确的剩余纯代数猜想

对p=3r+2>=17，统一入口已经可以进入w=(3^r,1,1)的合法平坦状态。定义C_w、T_w如(5)、(6)，并令有限终端超平面族
\[
\mathcal Z_w=\bigcup_{s}\{z:s^Tz=0\},\qquad
0\le s_i\le w_i,\quad s_i\in\mathbb Z,\quad\sum_i s_i=3.
\tag{14}
\]
每个s对应一个真实三元组的选择；到达这个超平面，下一次平均产生三个零，已有统一三零终端定理便完成归零。

**运输半群终端猜想。** 每个非零、展开后本原G=1的有理块向量z，满足w^Tz=0时，都存在有限词W in T_w使Wz属于Z_w。

这是一个完全明确的有理矩阵半群轨道命中问题。所有字母仅由非负整数行列和定义，字母、伴随和每个终端超平面的物理实现已经自动证明；没有“假设某个候选宏可实现”的循环。它是解决剩余素数的一个充分猜想，较全体原子可达性更强，尚未证明等价。

更弱的版本只要求覆盖从B_p经一步进入的二维子族，不要求全部平坦参数。更宽的精确等价版本则采用w=(3,1,...,1)，维数更大但覆盖全部原子词。

这个转化适合尝试有限群表示、Hecke半群、秩分层及带整格的幂等乘积理论。只研究关联代数、谱隙或凸化仍不够，第2、3节已经给出具体原因。

## 10. 这次实际推进与仍然开放的部分

本轮没有新增已解素数。新增的是三个可严格使用的结构：所有n>=5的原子生成代数完全一致；原位置层的正向可执行性由运输表完整参数化；二维能量对偶在危险素数处必然跨越Iwahori边，解释了一条自然统一取逆路线为何失效。

现在可以更加明确地回答“是否依赖具体构造”：证明可以转交给上述半群的统一轨道或乘积分解定理，而无需输出每个输入的手工宏；但这个特定半群所需的定理尚未建立。将它只换成群、代数或模形式会丢掉原问题，不能视为已经完成等价归约。

下一步应优先研究完整运输字母表的秩保持部分与终端超平面是否有统一结构，或利用其自动伴随封闭性建立保持整格方向的取逆／轨道定理。与此同时，判别式对偶提示应跟踪局部格边的方向及中间像的秩，而不仅是二次型或群的大小。

## 11. 核验契约

- `reynolds-hodge-structure`：[verify_reynolds_hodge_structure.py](../sources/work/verify_reynolds_hodge_structure.py)，209个Reynolds与凸标量实例，110个根恢复和190个秩一乘积，27个Hodge逆／Fricke接口、1238个合法到不合法像、27个Iwahori共轭、1716个判别式一次赋值控制。
- `contingency-layer-semigroup`：[verify_contingency_layer_semigroup.py](../sources/work/verify_contingency_layer_semigroup.py)，60层原位置重放共336次原子平均，54个载体字母，25个终端超平面，205个按交数分类的秩计算。

任意n、p的结论由正文的线性恒等式、计数和局部格论证承担；有限核验不证明第9节的终端猜想。没有扩大当前solved_size，最小未解仍为53。

<!-- END SOURCE doc-d41c21d90b67 -->

---

<a id="doc-6039e2005c5f"></a>

## 原文导签：非分裂素数路线复盘：停止局部拼接，返回二维除法结构

来源：`outputs/triple_average/history/triple_average_route_reassessment_2026-09-11.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_route_reassessment_2026-09-11.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-6039e2005c5f -->
# 非分裂素数路线复盘：停止局部拼接，返回二维除法结构

日期：2026-09-11。本文记录载体扫掠与等载体冻结方向的全部新增经验，
重新评估此前四条重点路线，并确定下一阶段的研究纪律。一般猜想仍未解决；
最小未解维数仍为71。

**最后检验更新：** 本页后半提出的直接Hecke／模符号主线已暂停，见
[最终审计](../sources/outputs/triple_average/history/triple_average_final_hecke_audit.md)。标准矩阵可整数幺模共轭，旧
指数p解释非内在；第二算子与标准生成元无共同正定星结构，普通线性Manin
编码被中心负号排除。原来的T_3、Eisenstein／Steinberg、删点PGL2解释也
已修正。本页保留历史尝试，不作为这些解释已经成立的依据。

## 1. 本轮新增的严格结果

### 1.1 等载体形式终端已经闭合

对
\[
\mathcal D_r=(u_1^3,\ldots,u_r^3,a^2),
\qquad3\sum_i u_i+2a=0,
\qquad p=3r+2,
\]
加入等载体交换的形式逆后，形式群显式包含
\[
\operatorname{diag}(SL_{r-1}(\mathbb Z),1).
\]
更强地，每个合法素数核只需
\[
K_1\ S_r\ K_2,
\qquad K_1,K_2\in SL_{r-1}(\mathbb Z),
\]
便能产生一个零叶块。证明先把叶差化为单gcd坐标，做一次真实等载体
交换；素数合法性保证新的叶差gcd整除新的基值，第二个整数SL块便能
产生零坐标。完整证明见[等载体形式冻结定理](../sources/outputs/triple_average/history/triple_average_equal_carrier_formal_freezing.md)。

这解决了一个此前不确定的问题：高秩形式轨道是否可能根本不遇到终端。
答案是否定的。终端超平面足够多，问题完全在正向实现。

### 1.2 固定局部正向SL被凸锥严格排除

若一个正向词只使用固定叶子集，并且某个输出叶行重新不依赖全部外部叶，
那么该行只能是参与叶值的非负组合。原因是实际输出始终是原始值的凸组合；
消去载体后，所有未参与叶具有同一个负边界系数。要令这个边界系数为零，
必须令载体权重为零，剩余叶系数便全非负。

所以固定局部正向词不可能实现
\[
e_i^T-e_j^T
\]
或其他混合正负号的平衡整数剪切。十位置催化器中的负根系数只存在于
减去局部均值并除去共同收缩后的射影坐标；把它嵌入大核时，边界系数并未
消失。这是一个全称障碍，不应再用增加词深的方法搜索“局部正向SL”。

### 1.3 有限域没有额外终端轨道障碍

等载体交换在小有限域射影空间上的精确轨道检查给出统一模式：

- 若 $q\nmid3r+2$，所测射影空间为单轨道并遇到零叶超平面；
- 若 $q\mid3r+2$，唯一避开零叶的轨道是常值直线；
- 在素数维数 $q=p=3r+2$ 时，这条直线恰是非法 $G=p$ 方向。

本轮计算对十个 $(r,q)$ 情形遍历140080个射影点，没有合法避开轨道。
正文进一步由形式SL块和一次交换证明了这个有限域模式的一般版本。因此
继续扩大有限模轨道表不会解决正向性。

### 1.4 低秩正向实验及其边界

秩三中，正向等载体交换的终端协向量一次枚举、批量测试全部高度不超过24、
叶坐标均非零的45873个合法本原输入：深度13剩9个方向，深度14全部覆盖。这个结果说明
直接命中零叶并非稀有现象，但不能外推到高秩；一个提取出的14步输出行在
更高秩嵌入后，对每个外部叶都带系数 $-192$，不是局部叶差宏。

秩二表现不同。协向量树到深度22恰有8388608个不同节点，若干简单斜率
仍未出现。并且存在严格奇偶反例：两叶均为奇数时，等载体交换保持叶奇偶，
永远不能产生零叶。剩余非分裂素数有奇数个叶块，所以该反例不直接嵌入，
但它证明“等载体交换对任意秩自动充分”是错误命题。

### 1.5 真实 $B_{71}$ 计数搜索

对标准核
\[
\mathcal B_p(u,v)=(u^{p-4},v^3,-(p-4)u-3v),
\]
使用真实三平均、按相同值重数压缩的整数计数搜索得到：

- $p=17,23,29,41,47,53,59,71$，每个取9个参数，72/72在至多5步内
  产生零和三元组；
- 对 $p=71,u=1$ 的 $v\in[-100,100]$，去掉三个非法方向后共198个合法
  参数；其中192个在5步内命中，剩余
  $-76,-73,-10,44,81,89$全部在第6步命中；
- 例如 $v=-76$ 的六步选择后得到零和三元组 $(-20,3,17)$。

这些是有限发现结果，不是全参数证明。它们的意义是：直接制造终端比构造
正向逆或全局SL更贴近真实动力学，并且在首个未解素数上没有显示稀疏性。

必须记录一次实现勘误。早期具体等载体BFS只把最后异常叶乘3清分母，未将
背景叶和第二异常叶同步乘3；那批“具体参数命中”全部作废。修正后的整数
实现与符号系数状态逐项一致。形式冻结定理、有限域轨道和计数状态搜索不受
这次错误影响。

### 1.6 两项负面有限实验

四种自然贪心规则都失败。对 $p=71$ 的198个参数、最多30步，按三元组和
最小、相对和最小、能量降幅最大、值类型数最小选择，分别只覆盖
7、27、12、9个参数。六步证书需要先制造中间值，不能由眼前最优的局部
量控制。没有证据支持这些朴素贪心量存在下降定理。

另一个同步尝试也没有成功。固定三个叶块，分别对两个载体施加“正向根词
接其正向逆词”产生的 $3^{-8}$ 局部中心收缩；全部长度不超过12的8190个
非空二字母词都没有把等载体子空间送回自身。该结果只限制这个固定收缩
字母表，不是否定所有同步窗口方案；但它排除了最自然的交替压缩闭路。

## 2. 为什么载体扫掠不再作为默认主线

载体扫掠给出的数学本身是可靠而且有价值的：固定十位置窗口中存在正向
双向幺幂、有限指数算术群和完整有理碰撞算法。问题在于从这些局部结论到
原 $p$ 位置终止，需要连续跨越三个不自然接口：

1. 每个窗口的射影逆都附带自己的中心收缩尺度；
2. 换窗口后局部均值改变，本原高度可按 $3^{8k}-1$ 指数增长；
3. 碰撞只产生相等值，不自动产生可冻结的零和块。

形式冻结定理又表明终端轨道本身并不难；真正缺的是正向实现。凸锥障碍
进一步排除了把局部根直接拼成平衡SL的方案。若继续强行补同步尺度、窗口
运输、碰撞冻结和正向SL四层接口，证明即使最终成立，也很可能比原问题
更复杂，而且无法解释为什么 $B_p$ 的二维证书从17到59如此统一。

因此载体扫掠降为辅助结构，保留三种用途：解释七元Artin中心、提供局部
正向根、给候选全局算法做局部终端子程序。它不再被称为“当前唯一主线”。

## 3. 回顾四条重点方向

### 3.1 非分裂轨道：保留为结构来源，改变目标

非分裂三阶元自然作用于 $\mathbf P^1(\mathbb F_p)$ 的 $p+1$ 个点，这是
$p\equiv2\pmod3$ 与分裂高斯机制最直接的对应物。已有结果解释了平移层
的迹、Legendre判别式、交错群影子以及Reynolds/Hecke代数。

原目标是从全共轭乘积中找标量范数周期。困难是 $p+1$ 到 $p$ 的删点质量
缺陷以及双单点等角障碍。现在应把目标从“正向单位”改为“奇异终端”：
研究punctured Reynolds词何时让 $B_p$ 二维像中的某个三元组和线性形式
消失。奇异像直接产生零和三元组，不需要先构造逆元，也避开局部中心同步。

这是下一阶段的主结构来源。

### 3.2 仿射交换子理想：定理已完成，只作为后处理器

一旦得到若干正向可逆仿射宏，导群参数理想由
\[
c_{ij}=(1-d_j)b_i+(d_i-1)b_j
\]
及倍率局部化环完全决定；本原性又由多项式gcd和Bezout整数控制。这部分
已经结构化，不需要继续搜索根。

它不能产生最初的正向种子，所以不应单独作为主线。以后每出现一个候选
可逆族，立即用交换子理想判断它是否值得继续；若理想含随 $p$ 变化的新
因子，立刻淘汰。若直接终端路线成功，则甚至可以绕过它。

### 3.3 参数周期刚性：作为搜索纪律和否定工具

任何固定有理函数矩阵词若不在 $\mathbb Q(p)$ 上恒等满足有限阶迹条件，
只能命中有限多个 $p$。59元短周期正是孤立根，不是统一规律。

因此今后不再扩大固定词深、逐素数寻找周期。允许的周期候选只有两类：

1. 在 $\mathbb Q(p)$ 上可符号证明的恒等周期；
2. 词长按 $p$ 明确增长、来自完整非分裂轨道范数或Hecke卷积的周期。

任何程序发现的周期必须立即参数化；非恒等者只可用于该固定维数。

### 3.4 统一迹零返回：保留为标杆，暂停原位置分解

$R_0$ 与 $R_\beta$ 的周期、根理想、Bezout消元和终端覆盖已经闭合成一条
严格充分路线。问题只剩两个指定双随机运输的原位置因子化，但这个问题
本质上接近复制消去：非负三进运输不自动属于三平均正半群。

此外目标矩阵先由迹零方程指定，再要求真实动力学实现，缺乏内生解释；
短编译语法、二因子产品、叶数字字母表和两层伴随闭路均没有显示自然入口。
所以暂停直接攻原位置分解。迹零返回继续充当标杆：新的结构若能实现它，
就立即得到完整证明；但不再把实现它视为必须经过的道路。

## 4. 现在的主问题应怎样重写

所有剩余素数输入已经能正向进入二维标准核 $\mathcal B_p(u,v)$。所以应
直接研究有向参数动力学，而不把它再次扩张成高秩局部群：
\[
\boxed{
\text{对每个合法 }[u:v]\in\mathbf P^1(\mathbb Q),
\text{构造依赖输入的正向词，命中一个零和三元组。}}
\tag{1}
\]

这允许词依赖输入，与固定词一致性障碍相容；也不要求半群整体群化。理想
证明应类似Euclid或连分数：有有限个自然的 $p$ 参数宏，每一步根据当前
斜率选择一个，使某个整数高度严格下降，终点就是零和三元组超平面。

关键区别是高度必须定义在全局 $B_p$ 二维参数上。局部窗口的本原高度、
实能量和不同值个数都已有反例；不能再次使用它们。

后续Hecke分析把这个目标进一步修正为**有向Hecke终端覆盖猜想**：路径
允许离开二维 $B_p$ chart进入其他真实重数分层，只要求一个完整可执行宏段
回到更低的全局高度或直接终止。要求每个原子步骤都写成
$B_p(u,v)\to B_p(u',v')$ 会被短Reynolds chart边界人为卡死，也不是现有
$B_{71}$ 六步终端证书的实际行为。完整同余子群包含保留为更强备选结论，
不再作为弱轨道证明的前置条件。

## 5. 下一阶段的具体工作顺序

### 第一目标：从非分裂Reynolds层提取二维终端算子

在punctured原 $p$ 位置层上，不搜索完整返回矩阵，只计算
\[
W E_p
\]
中与三元组和有关的少数行线性形式。利用置换词固定点计数、二次判别式
字符和Hecke卷积，把这些行写成 $p$ 与轨道参数的闭式。优先寻找奇异词，
而不是有限阶词。

每个候选必须回答：它是否真实使用原 $p$ 个位置；适用域是否全参数；命中
超平面是什么；选择轨道参数后是否给出类似余数 $a-qb$ 的除法步。

后续[三平均的Iwahori--Hecke与模形式接口](../sources/outputs/triple_average/history/triple_average_iwahori_hecke_modular_interface.md)
把这一步进一步收紧：几何链宏已经严格给出参数3的Hecke代数表示，数字
算子也恰是三个仿射分支的转移和；标准 $B_p$ 宏则精确给出 $T_3$ 的回边
陪集。现在应先证明这些真实分支与
$\Gamma_0^{(3)}(p)$商上的定向 $U_3$ 对应逐分支交织；若成立，再用模符号
Euclid约化或Eisenstein/Busemann超调和高度选择下降分支。只比较算子和
或特征值仍不足够。

### 第二目标：建立二维除法引理

从候选算子中提取对本原整数对 $(u,v)$ 的变换。需要证明存在一个可执行
选择，使
\[
H(u',v')<H(u,v)
\]
或一步直接终止。$H$可以结合实大小与有限个 $p$/3进边界，但必须在
$B_p$ 的共同全局尺度上定义。若只得到可逆仿射元，立即调用仿射交换子
理想和Bezout定理，避免重复做群搜索。

### 第三目标：程序只做符号候选发现

计算应枚举轨道参数、交数类型或短Hecke卷积，并把所有 $p$ 保持为符号；
不同组合类型并行。每发现候选立即检查：

- 是否在 $\mathbb Q(p)$ 上恒等；
- 是否命中终端或给出严格除法；
- 是否触发已知质量、凸锥、周期刚性或参数理想障碍。

只有通过这些筛选才扩大计算。停止逐素数返回库和无目标深度BFS。

## 6. 路线状态表

| 路线 | 当前判断 | 后续角色 |
|---|---|---|
| 十位置载体扫掠 | 局部成功，全局拼接繁琐 | 辅助局部子程序，暂停主线 |
| 等载体形式SL冻结 | 形式终端完成，正向SL被局部凸锥阻挡 | 提供终端存在性，不直接群化 |
| 等载体直接正向命中 | 小样本强，但没有自然下降规则 | 保留证据，不继续盲目BFS |
| 混合迹零原位置分解 | 充分但过强，接近复制消去 | 暂停，作为标杆 |
| 仿射交换子理想 | 一般定理已完成 | 所有可逆候选的后处理器 |
| 参数周期刚性 | 一般定理已完成 | 淘汰伪统一周期 |
| 非分裂Reynolds单位 | 质量与两层周期受阻 | 不再优先找单位 |
| 非分裂Reynolds奇异终端 | 尚未系统开发，最贴近真实操作 | 新主线 |
| $B_p$二维Euclid下降 | 终端实验支持，尚无生成元定理 | 新核心证明目标 |

## 7. 程序与证据边界

- `work/verify_equal_carrier_formal_freezing.py`核验形式冻结恒等式；已登记
  `equal-carrier-formal-freezing`。
- `work/explore_equal_carrier_freezing.py`检查有限域射影轨道。
- `work/explore_equal_carrier_positive_freezing.py`批量检查秩三正向终端
  协向量；只属有限高度实验。
- `work/explore_equal_carrier_bcore_terminal.py`与
  `work/explore_equal_carrier_concrete.py`分别做符号和具体等载体搜索；具体
  脚本已修正共同尺度错误。
- `work/explore_bcore_zero_triple.py`使用值--重数整数状态搜索真实零和
  三元组；72/72和 $B_{71}$ 的198/198是有限参数结果。
- `work/explore_bcore_zero_triple_greedy.py`复现四种贪心规则的失败。
- `work/explore_equal_carrier_contraction_sync.py`精确检查固定双载体中心
  收缩字母表长度至12无返回。

除形式冻结及凸锥障碍外，本页新增数字均是探索证据，不承担任意 $p$ 或
任意参数的全称量词。当前没有后台搜索进程应被视为证明的一部分。

<!-- END SOURCE doc-6039e2005c5f -->

---

<a id="doc-59a71841611a"></a>

## 原文导签：B12、B15、B18、B21 的统一有限比较

来源：`outputs/triple_average/history/triple_average_single_prime_kernel_comparison.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_single_prime_kernel_comparison.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`bn-comparison-depth4`, `b15-two-depth5`, `b21-depth5`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-59a71841611a -->
# B12、B15、B18、B21 的统一有限比较

**后续状态：** [十二元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md)、[十五元完整归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md)与[十八元完整归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_eighteen_via_twelve_complete.md) 已闭合，B21 是七元提升的已知对照。本表仍保留有限实验本身的证据范围，不能把小高度覆盖替代这些一般证明。

本记录对应 work/explore_single_prime_kernels.py。搜索的是
\[
\mathcal B_n(u,v)=(u^{n-4},v^3,-(n-4)u-3v)
\]
的本原整数参数，按全局符号取商。合法域为
\[
\gcd(u,v)=1,\quad
\gcd(u-v,n/3^{v_3(n)})=1,\quad \max(|u|,|v|)\le8.
\]
包括所有 G 为三幂的方向，不能再限制成 G=1。B21 属于已解决的 \(7\cdot3\) 塔，本实验是其二维核方法的对照，不是新的一般判据。

## 终端契约

搜索只认与 n 的三进展开对应的零和三幂块分拆：

| n | 分拆 | 归零网络的固定尾段步数 |
|---:|---|---:|
| 12 | 3+9 | 7 |
| 15 | 3+3+9 | 8 |
| 18 | 9+9 | 12 |
| 21 | 3+9+9 | 13 |

每个证书包括前缀操作词、前缀末状态及所有块的计数；父进程复核操作重数、状态、各块零和、各块大小及完整分拆。搜索深度只计前缀；完整归零长度还要加尾段。

这是充分终端条件，未找到这种分拆并不排除其他归零路线。最终全零状态显然满足这种分拆，故不影响无深度界搜索的完备性；但不能因此把有界搜索认作判定算法。

## 实测边界

| n | 合法符号类数 | 深度 3 已覆盖 | 深度 4 已覆盖 | 深度 5 补充 |
|---:|---:|---:|---:|---|
| 12 | 62 | 60 | 62 | 无需加深 |
| 15 | 73 | 50 | 71 | 两个缺口全部找到证书 |
| 18 | 62 | 46 | 62 | 无需加深 |
| 21 | 79 | 37 | 66 | 全量得到 79/79 |

因此此高度界内完整覆盖的前缀最大深度为 4、5、4、5。B15 的两个四步缺口为 (-8,3)、(-7,-6)；B21 的四步缺口共 13 个。没有把这些有限数据提升为无界定理。

复现四维数深度四：

    python work/explore_single_prime_kernels.py --bound 8 --depth 4 --jobs 8 --summary

复现两项深度五补充：

    python work/explore_single_prime_kernels.py --n 15 --bound 8 --depth 5 --jobs 2 --pair=-8,3 --pair=-7,-6 --summary
    python work/explore_single_prime_kernels.py --n 21 --bound 8 --depth 5 --jobs 8 --summary

数值搜索默认使用本原整数状态商，并在命中后精确恢复每步实际 Fraction 值；证书仍由原始轨迹重放。旧引擎可用 --engine fraction 对照。两者最短深度分布一致；[B21 性能复核](../sources/outputs/triple_average/history/triple_average_b21_integer_search_optimization.md) 记录了等价性证明和实测加速。

## 计算改进与数学结论

只按不同数值及其重数枚举三元组；零和分拆统一清分母成整数；尾部两个计数由线性方程解出，最后一个块直接检查补集。这些优化保留全部候选分拆，用独立的位置子集枚举做了 720 项比对。

一般宏族、混合返回长度下界、实范数下降的三进障碍和 theta 格对应，见 [三进扩张修复宏与算术接口](../sources/outputs/triple_average/history/triple_average_carry_repair_and_arithmetic_interface.md)。有限覆盖本身不证明类数决定搜索深度，也不证明固定核返回群是算术群。

<!-- END SOURCE doc-59a71841611a -->

---

<a id="doc-6e8f7854c3fe"></a>

## 原文导签：所有 p=1 mod3 素数的完整判据：高斯周期正向控制器

来源：`outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`split-prime-gaussian-controller`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-6e8f7854c3fe -->
# 所有 p=1 mod3 素数的完整判据：高斯周期正向控制器

日期：2026-09-10。本文证明一个无限素数族，不按素数逐个搜索宏或陪集。所有操作都在原来的p个位置中进行，不复制输入。

后续更新：[29元独立证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)、[41元独立证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_one_arithmetic_complete.md)及[47元完整证明](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_seven_arithmetic_complete.md)均已完成，因此当前剩余p=2 mod3素数从53开始。本文的分裂素数证明及其核验保持不变；当前整体路线见[素数证明路径与剩余猜想](../sources/outputs/triple_average/history/triple_average_prime_proof_roadmap.md)。

## 1. 主定理

**分裂素数定理。** 对每个 \(p\equiv1\pmod3\) 的素数，p元有理输入在中心化、本原化后，有限步三平均可归零，当且仅当 \(G(X)=1\)。

p=7、13已有独立完整证明。下面对所有p>=19、p=1 mod3给出同一个正向构造。必要性仍是非三共同非零余类障碍。

结合[全部维数到素数归约](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_to_primes.md)，任意n的问题进一步归约到p=2 mod3的素数。11、17、23已解，剩余素数从29开始。所有三整除维数仍由此前定理无条件处理。

本族的判定只需计算G，属于输入位长多项式时间。本文不声称展开后的原子路径长度已有多项式界。

## 2. 原位置数内的高斯周期层

写 \(p=3r+1\)。在 \(\mathbb F_p^\times\) 中取三阶子群
\[
H=\{1,\omega,\omega^2\},\qquad1+\omega+\omega^2=0.
\]
把p个真实位置标为 \(\mathbb F_p\)。位置0为载体，其余位置按H的乘法陪集分成r个三重块。记块值为 \(u_C\)，载体为
\[
w=-3\sum_C u_C.
\]
这正是原维数的一载体平坦核；高维输入到此的合法进入桥已有证明。

对每个非零c，按所有乘法陪集C分别平均三个位置
\[
c+C=\{c+x:x\in C\}.
\tag{1}
\]
它们两两不交，并恰好覆盖除c外的全部位置，所以这一层恰用r次真实三平均。然后以 \(x\mapsto x+c\) 重新记位置编号，便再次得到H三重块及位置0载体。记该层在u上的矩阵为P_c，令K_c=3P_c。

K_c整系数。每个输出块的三项若不含旧位置0，就直接统计输入块次数；若含0，则使用 \(w=-3\sum u_C\)。这给出完全显式的整数矩阵。

在下文固定c=1，并记
\[
K=K_1,\quad e_0=e_H,\quad z=-H,\quad\eta=(1,\ldots,1)^T.
\]
载体输出是旧u_H，故
\[
\eta^TK=-e_0^T,
\qquad K\eta=3\eta-p e_z.
\tag{2}
\]

## 3. 高斯范数给出全局正向逆

令 \(L=\mathbb Q(\zeta_p)\)、\(F=L^H\)，定义高斯周期
\[
\theta_a=\sum_{h\in H}\zeta_p^{ah}.
\]
零和H不变状态的傅里叶变换给出同构
\[
u\longmapsto\sum_C u_C(\theta_C-3)\in F.
\tag{3}
\]
K_c在此同构下就是乘以 \(\theta_{-c}\)。确实，H不变输入上，“平移再按H平均”也可写成三个循环平移的平均。

所以全部K_c相互交换。取每个非零乘法陪集的一个代表c，便有
\[
\prod_{c\in\mathbb F_p^\times/H}K_c=\nu_p I,
\qquad\nu_p=N_{F/\mathbb Q}(\theta_1)\in\mathbb Z_{>0}.
\tag{4}
\]
三个不同p次单位根之和不为零；复共轭成对给出正范数，而且每个共轭的绝对值严格小于3。故
\[
0<\lambda_p=\frac{\nu_p}{3^r}<1,
\qquad\prod_c P_c=\lambda_p I.
\tag{5}
\]
这是一条使用r^2次原子平均的**原维数全局标量循环**。每个P_c的射影逆，正是其余r-1层的乘积。整个循环不是某个非零均值子块的收缩，而是全局零和核上的标量。

例如p=7、13、19、31的 \(\nu_p\) 分别为2、3、7、25，对应标量为2/9、1/27、7/729、25/59049。范数不必是三幂；它始终与p互素，并满足 \(\nu_p\equiv3^r\pmod p\)。

因此，P_c及任意叶块置换生成的射影半群已经是一个群。以下任何群词的逆都可以展开为正向平均层。

## 4. 两个统一的稀疏根恒等式

以下下标均表示H陪集。周期乘法只需分开三个对角项和六个非对角项，就得到
\[
\theta_{-1}(\theta_1-\theta_{-2})=3-\theta_{-3},
\tag{6}
\]
\[
\theta_{-1}(\theta_{\omega-1}-\theta_{1-\omega})
=\theta_{\omega-2}-\theta_{1-2\omega}.
\tag{7}
\]
例如(7)左侧两个乘积分别为
\(\theta_{\omega-2}+\theta_{-1}+\theta_2\) 和
\(\theta_{1-2\omega}+\theta_{-1}+\theta_2\)，公共项相消。

由(3)，这些恒等式转成整数矩阵恒等式：
\[
K(e_H-e_{-2H})=-e_{-3H},
\tag{8}
\]
\[
K(e_a-e_b)=e_i-e_j,
\quad a=(\omega-1)H,\ b=(1-\omega)H,
\quad i=(\omega-2)H,\ j=(1-2\omega)H.
\tag{9}
\]
对p>=19，(9)中的源下标互异、目标下标互异且非零；源和目标可以交叠，不影响后面的公式。

## 5. 范数一单位是关键

设 \(D=\omega-1\)。另一个周期恒等式为
\[
\theta_1\theta_{-1}-1
=2+\theta_D+\theta_{-D}
=\prod_{h\in H}(1+\zeta_p^{Dh}).
\tag{10}
\]
右侧是分圆单位的相对范数。由于p为奇素数，
\[
N_{L/\mathbb Q}(1+\zeta_p^D)=\Phi_p(-1)=1.
\]
因此整数矩阵
\[
B=K_{-1}K-I
\tag{11}
\]
满足 \(\det B=1\)。注意这与 \(\det K=\nu_p\) 不一定为单位是两件事。

令 \(G_0=I+3J\)。展开状态的平方能量为 \(3u^TG_0u\)，卷积算子的伴随关系给出
\[
K^TG_0=G_0K_{-1},\qquad\det G_0=1+3r=p.
\tag{12}
\]
并且由(2)
\[
B\eta\equiv8\eta\pmod p.
\tag{13}
\]
这三条整格事实会排除剪切系数中的所有不可消去分子素因子。

## 6. 本原剪切引理

用(9)的下标，置
\[
v=e_i-e_j,\quad f=e_i^T-e_j^T,\quad
g=(e_a^T-e_b^T)K^{-1},\quad h=g-f.
\]
有 \(g(v)=f(v)=2\)，故 \(h_i=h_j\)。两次换位的乘积为
\[
U=R_{ij}K R_{ab}K^{-1}=I+vh.
\tag{14}
\]
对i,j之外的k,l，令 \(\tau=R_{kl}\)，则
\[
U\tau U^{-1}\tau
=I+(h_k-h_l)(e_i-e_j)(e_k^T-e_l^T).
\tag{15}
\]
这些都是已有正向群中的词。

**本原剪切引理。** 外部差 \(h_k-h_l\)、k,l不在{i,j}，生成的加法子群恰为 \(D_0^{-1}\mathbb Z\)，某个正整数D0。特别地，它们能用整数线性组合和整数倍生成1。

证明需要以下简单行结构。K只有第z=-H行含旧载体；它的行和为3-p，其余行和为3。除第H行外，非载体行的三个输入属于三个不同旧叶块，因此该行仅有三个1。唯一双交的旧点为 \(-\omega,-\omega^2\)，对应新行H和旧列-H。

行结构的直接证明如下。若同一输出轨道中的两个旧输入落在同一非零旧轨道，则在旋转下标后有
\(1+x=t(1+xs)\)，其中s,t属于H且都不等于1。若ts=1，等式不可能；否则H只有三元，迫使t=s，继而 \(x=(s-1)/(1-s^2)=s\in H\)。所以只有输出H行发生双交。该行三个旧值是2、-omega、-omega平方，后两者同属-H。

对p>=19，a,b不等于H，i,j不等于H或z。这些排除可直接代入 \(\omega^2+\omega+1=0\) 检查：
\[
(\omega-1)^3=3+6\omega,\quad
(\omega-2)^3=18\omega-1,\quad
(1-2\omega)^3=-19-18\omega.
\]
可能出现的额外相等只涉及p=7、13。因而第i,j行均为0/1行。结合(9)，它们在列a的值分别为1、0，在列b分别为0、1。

更明确地，a或b等于H会迫使p整除7；i或j等于H或-H会迫使p整除91或属于2、3；i或j为零会迫使p=7；i=j则迫使p=3。这说明小素数排除是有限代数恒等式的结果。

假设某个素数q将全部外部差整除，即它们都在 \(q\mathbb Z_{(q)}\) 中。选一个外部位置作为参考，可写
\[
g=\alpha\eta^T+\beta(e_i^T+e_j^T)+f+\varepsilon,
\]
其中 \(\varepsilon_i=\varepsilon_j=0\)，其余 \(\varepsilon_k\in q\mathbb Z_{(q)}\)。alpha和beta开始时允许不是q整的。

利用 \(gK=e_a^T-e_b^T\)，比较列a并用(2)，得到 \(\beta\in q\mathbb Z_{(q)}\)。再将所有列相加，得到
\(-\alpha+6\beta+\varepsilon K\eta=0\)，故 \(\alpha\in q\mathbb Z_{(q)}\)。所以全部g均q整，且 \(g\equiv f\pmod q\)。

记 \(x=e_a-e_b\)。于是 \(Kx=v\)、\(K^Tv\equiv x\pmod q\)。x、v的坐标和均为零，由(12)得到
\[
G_0Bx\equiv0\pmod q.
\]
若q!=p，G0与B模q均可逆，矛盾。若q=p，G0的核恰为 \(\mathbb F_p\eta\)；由(13)、p>=19及B可逆，B及其逆保持这条线，所以x必须是eta的倍数，也矛盾。

因此没有素数能同时整除所有外部差的本原分子。外部差不可能全零，其有理gcd的分子只能为1，引理得证。

通过叶块置换，可将(15)中不同源位置的剪切搬到同一对源位置。剪切参数相加，逆词提供负参数；Bezout线性组合和一次整数倍遂给出参数恰为1的剪切。因此正向高斯群包含所有
\[
I+(e_i-e_j)(e_k^T-e_l^T),\quad i,j,k,l\text{ 互异}.
\tag{16}
\]

## 7. 从平衡群到全部整数仿射行操作

p>=19时r>=6。由[平衡生成定理](../sources/outputs/triple_average/history/triple_average_digit_congruence_group.md)，(16)及置换生成全部
\[
\mathcal H_r=\{M\in GL_r(\mathbb Z):M\eta=\eta,\ \eta^TM=\eta^T\}.
\]
该群的每个射影作用现在都已有原维数正向实现。

令 \(v_0=e_H-e_{-2H}\)、\(I_0=-3H\)，由(8)有Kv0=-e_I0。选择k,l避开I0和z，并置
\[
F=(e_k^T-e_l^T)K.
\]
F整系数，且 \(Fv_0=0\)、\(F\eta=0\)。因此 \(I+v_0F\in\mathcal H_r\)。将它用K共轭，得到
\[
K(I+v_0F)K^{-1}=I-e_{I_0}(e_k^T-e_l^T).
\tag{17}
\]
叶块置换与取逆给出所有三个互异下标的单位行差剪切。

这些剪切与置换生成整个
\[
\mathcal A_r=\{M\in GL_r(\mathbb Z):M\eta=\eta\}.
\tag{18}
\]
这是[列稳定子生成证明](../sources/outputs/triple_average/history/triple_average_digit_congruence_group.md)第4节的结论：在基 \((e_1,\ldots,e_{r-1},\eta)\) 中，先生成全部左上整数初等矩阵，再生成最后一行的单位平移。

这里没有使用形式群算术性或有限指数作为替代条件；(18)中的每个矩阵已经由正向高斯词实现到一个全局非零尺度。

## 8. 任意合法状态只需两次仿射正规形

对本原整数叶向量u，整个展开状态的坐标gcd也为1。令
\[
d=\gcd_{C,D}(u_C-u_D),\qquad c=u_C\pmod d.
\]
若u恒定而非零，则展开状态的G为p，不合法，所以只需d>0的情形。由于u本原，\(\gcd(c,d)=1\)。载体是 \(-3\sum u_C\)，故
\[
G(u_C^3,w)=\gcd(d,p).
\tag{19}
\]

整数仿射行群A_r的轨道由仿射格 \(c+d\mathbb Z\) 分类。具体地，以一个叶值为参考，对其余r-1个差做Euclid消元，再以最后一行平移调整参考值模d，可将u送到
\[
u^*=c\eta+d e_H.
\tag{20}
\]
这不要求知道u的总和；载体随之由零和关系确定。

现在应用一次高斯层。K的第H列在z之外恰有两个1，其余为0，且第z项为-3。于是 \(Ku^*\) 的值包括
\[
3c,\quad3c+d,\quad(3-p)c-3d.
\]
前两种都出现，因为r>=6。其全部差的gcd恰为
\[
\gcd(d,pc)=1
\tag{21}
\]
，这里使用合法性p不整除d及 \(\gcd(c,d)=1\)。实际P层只多一个共同尺度1/3。

第二次使用A_r正规形，便将新的叶向量送到e_H。因此原p个位置成为共同非零尺度乘以
\[
(1^3,0^{p-4},-3).
\]
选择三个1、单独的-3及五个零，使用九元三幂网络即可全部归零。

每个仿射行操作在第7节已经有正向实现，所有逆词由第3节的全局高斯范数周期提供。因此这是有限正向路径的证明，分裂素数定理成立。

## 9. 整数格与数域的本质联系

这里的数域是有理宏的辅助表示，不是更换输入值域。高斯周期 \(\theta_C\) 构成F的整数正则基；\(\theta_C-3\) 构成其上方唯一p素理想的一组整数基。两组基的过渡矩阵是 \(I+3J\)，行列式恰为p。

这两个整数格声明也有直接证明：\(\zeta_p,\ldots,\zeta_p^{p-1}\) 是 \(\mathcal O_L\) 的整数基，H置换这组基，所以其不变整格 \(\mathcal O_F\) 以轨道和theta_C为基。由 \(\sum_C\theta_C=-1\)，替换为theta_C-3的过渡矩阵正是I+3J；每个新基元都模唯一的p素理想为零，且该整格指数为p，故它就是这个素理想。

于是三件事在同一个格中自然相接：

- 模p障碍来自这个指数p的格；
- 正向逆来自高斯周期的全局范数；
- 单位剪切来自 \(\theta_1\theta_{-1}-1\) 的范数一单位。

最终的G判据由仿射整数格正规形得到。证明没有为每个p重新寻找cusp代表或单独计算同余子群指数。

## 10. 边界与下一问题

这个构造使用 \(\mathbb F_p^\times\) 的三阶子群，故适用于p=1 mod3。p=2 mod3时该子群不存在；不能把它直接移到二次扩张域并当作原p个位置上的操作。

所有n仍已归约到素数，所以剩余统一任务现在是p=2 mod3、p>=29的原维数正向控制器。非分裂三阶作用、两个载体及已有高秩形式算术性是明确的下一接口，尚未形成充分性证明。

## 11. 核验契约

主脚本：[verify_gaussian_prime_controller.py](../sources/work/verify_gaussian_prime_controller.py)。构造辅助：[explore_gaussian_period_layers.py](../sources/work/explore_gaussian_period_layers.py)。统一ID为 `split-prime-gaussian-controller`。

- 6个素数的范数周期，在固定真实位置和完整系数基上重放496次原子平均。
- 10个素数核对两个稀疏根恒等式、范数一矩阵、外部差的本原性及整数仿射群接口。
- p=13、19、31的单位平衡剪切独立正向重放，共800次原子操作。
- 320个带非平凡差分gcd的本原输入，核对两次整数仿射正规形、一次高斯层的精确gcd消去及九元终端。

一般本原剪切引理由第6节对任意素数q的证明承担。320个正规形实例不等于逐个展开了其全部群生成词；正向生成词的存在性由第3、6、7节证明。有限检查不是所有分裂素数的外推依据。

<!-- END SOURCE doc-6e8f7854c3fe -->

---

<a id="doc-4a708197aa0f"></a>

## 原文导签：结构图景复核：可用的局部到整体机制及数域边界

来源：`outputs/triple_average/history/triple_average_structural_picture_audit.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_structural_picture_audit.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`b29-current-cycle-boundary`, `one-tripling-stabilization`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-4a708197aa0f -->
# 结构图景复核：可用的局部到整体机制及数域边界

日期：2026-09-10。对照[原结构图景](../sources/outputs/triple_average/history/triple_average_structural_picture_conjecture.md)的当前版本，特别是新增第 7 节。原文件保留，下面的修正由本页独立记录。

## 1. 哪些部分已经形成严格接口

原稿把局部格、正向实现、轨道覆盖和终端区分开，这是正确的研究组织方式。现在可把三条路线按证明状态排列：

| 路线 | 已证内容 | 尚缺内容 |
|---|---|---|
| 固定维数同余群 | 13/17/19/23/25 等正向逆、同余轨道、终端证书 | 任意素数的统一生成元与覆盖 |
| 不等权块与 Burau 链 | 全仿射 R 模保护、全 GL 的 Zariski 闭包、链内正向逆与秩二跨链缺陷 | 整数轨道控制及跨链终止 |
| 可重新分组的三份复制 | Hilbert 90 标量周期、所有平衡剪切的正向实现、完整同余群等式及有理轨道分类 | 原维数的状态依赖复制消去 |

第三条已推进成[一次三份复制定理](../sources/outputs/triple_average/history/triple_average_one_tripling_stabilization.md)：所有 \(3\mid N, N\ge9\) 的维数无条件解决。这里先证明真实初等变换，再用欧几里得正规形完成局部到整体，不需要先证明整个宏群的算术有限指数。

全局周期的最新严格接口见[谱平衡与S单位关系格](../sources/outputs/triple_average/history/triple_average_projective_spectral_balance.md)：给定有理矩阵的有限射影阶，由所有地方的谱平衡与半单性完全刻画；可交换数域乘法库的正向群化，等价于饱和S单位关系格含全严格正向量。这把原稿的“局部稳定子到正向轨道”中的一个可交换子问题变成精确整数锥问题。非交换库仍需额外构造；47元固定模板的短周期排除不影响这些接口。

后续原维数的[等值载体二进重分组](../sources/outputs/triple_average/history/triple_average_paired_carrier_reset.md)给出另一个完整格接口：自然参数格判别的非三部分为2n，纯二重载体交换的叶奇偶保持阻止全局周期；固定十二位置重分组层可以用两遍广播产生4r-3步宏W=2V，其中V属于GL_r(R)。坐标与差分R理想均恰乘2，故本原G保持。它提供了原维数R可逆射影宏，但尚未证明正向逆或终端覆盖。

进一步的[完整群生成证明](../sources/outputs/triple_average/history/triple_average_digit_congruence_group.md)现已补齐有限指数：平衡群恰是模n本原向量稳定子，数字算子添加倍率3的分裂循环扩张。这个等式只属于所构造的副本宏库；不能据此断言原维数的不等权交换库也已算术化。

原稿猜想 II 在明确有限指数群、全域正向逆、有限合法轨道和终端代表之后，是一个条件定理：把任意输入送到相应代表，再拼接真实词即可。待证部分是这些条件能否统一构造，而不是拼接的逻辑。

## 2. 合法域本身不能识别 p 的高次 level

对 \(B_{p^k}(u,v)\) 的本原参数，合法性仍只是
\[
p\nmid u-v.
\]
对任意 \(k\ge2\)，矩阵
\[
M=\begin{pmatrix}1&0\\p&1\end{pmatrix}
\]
与逆都保持这个集合，因为模 \(p\) 均为单位矩阵。但 \(M\) 不保持模 \(p^k\) 的方向 \([1:1]\)：它将之送到 \([1:p+1]\)。

因此原稿猜想 III 及命题 A 中“合法域自动决定第 k 层稳定子”的论证不能成立。25 元证书确有 level 25；这个更高 level 来自对所有形式参数有效的实际算子、常值余类及尺度的约束，不能仅由合法参数集合恢复。

更准确的目标是区分三层：合法集合的自同构群、保持完整积分格与常值射线的算子群、由真实正向宏生成的子群。它们未必相等。

## 3. 固定输入换到扩张域，可达性完全不变

设 \(K\subset L\) 是数域，输入坐标在 \(K\)。任何三平均词的矩阵都在 \(M_n(\mathbb Q)\)，中间值仍在 \(K\)。故逐词有
\[
P_wX=0\text{ 在 }L\text{ 中成立}
\quad\Longleftrightarrow\quad
P_wX=0\text{ 在 }K\text{ 中成立}.
\]
于是
\[
X\text{ 在 }K\text{ 中可达}\quad\Longleftrightarrow\quad
X\text{ 在 }L\text{ 中可达}.
\]
原稿第 7.6 节所猜测的扩张改善可达性，在当前操作定义下不可能发生。无需额外的 Galois 下降定理。

## 4. 内容理想的支撑与类群不是所提形式的必要条件

最简单的反例已经在有理数中：\((5,-5,0)\) 一步归零，但坐标内容理想为 \((5)\)。乘一个共同非零尺度不改变可达性，所以内容支撑不能单独充当障碍。

类群版本也有反例。在 \(K=\mathbb Q(\sqrt{-10})\)、\(\mathcal O_K=\mathbb Z[\sqrt{-10}]\) 中，
\[
(2,\sqrt{-10},-2-\sqrt{-10})
\]
一步归零。内容理想 \(\mathfrak a=(2,\sqrt{-10})\) 的范数为 2，却非主理想：若主，则存在整数 \(a,b\) 满足 \(a^2+10b^2=2\)，显然不可能。

3 在该域中惰性，因为 \(t^2+1\) 模 3 无根。因此 3 上方素理想就是主理想 \((3)\)，局部化掉它不能消去 \([\mathfrak a]\)。这个可一步归零的输入，不满足原稿提出的“内容类由 3 上方素理想类生成”。

这些反例针对所写必要条件，并不否定辅助数域在研究宏矩阵时的价值。

## 5. 正确的线性对象是 R 加法模

对中心化、零和的代数数值状态，定义
\[
I_R(X)=\sum_i R x_i,\qquad
J_R(X)=\sum_{i,j}R(x_i-x_j),\qquad R=\mathbb Z[1/3].
\]
所有中间值均在初始仿射 R 模 \(x_1+J_R(X)\) 中。一般平均只保证新仿射模包含于旧模；有 R 整系数正逆的交换宏才保持等式。可达的必要条件为
\[
0\in x_1+J_R(X)
\quad\Longleftrightarrow\quad I_R(X)=J_R(X).
\tag{1}
\]
在本原有理零和情形，\(I_R=R,J_R=GR\)，所以 (1) 正好等价于 \(G\) 为三幂。

把 R 加法模改成 \(\mathcal O_K[1/3]\) 理想会加入实际操作不提供的乘法，从而漏掉障碍。即使类数为一也如此：在 \(\mathbb Q(i)\) 中取
\[
X=(1^5,1+i,-6-i).
\tag{2}
\]
总和为零；坐标理想因包含 1 为单位理想，差分理想因包含单位 \(i\) 也为单位理想。但取有理实分量得到 \((1^6,-6)\)，全体坐标模 7 都为 1，三平均保持这个非零共同余类，所以 (2) 不可达。

同样的例子可将 \(i\) 换为 \(\alpha=\sqrt{-2}\)。差分理想为 \((\alpha,7)=\mathcal O_K\)，因为 \(-4\alpha^2-7=1\)，仍漏掉实分量障碍。

真正的 R 模是
\[
I_R=R+R\alpha,\qquad J_R=7R+R\alpha,
\]
指数为 7，准确检测到障碍。

## 6. 数域版本是多个有理向量共用一个词

选择坐标值张成空间的一组 Q 基 \(b_1,\ldots,b_r\)，写
\[
X=b_1X^{(1)}+\cdots+b_rX^{(r)},\qquad X^{(j)}\in\mathbb Q^n.
\]
线性独立性给出
\[
P_wX=0\quad\Longleftrightarrow\quad
P_wX^{(j)}=0\quad\text{对每个 }j.
\tag{3}
\]
每个分量各有一条路径不够，必须存在同一个词。可达性在值空间的任意单射 Q 线性变换下不变；值域的乘法、单位和类群并非当前操作自动保留的结构。改变数域也不会提供“乘以新单位”的额外操作。

因此，应先研究有理关系子空间的共同消灭与 R 仿射模，而不是将 \(G\) 直接替换为内容理想。本文没有证明 (1) 对任意代数数值输入充分。

## 7. 保留哪些算术几何工具

与上述值域推广不同，附着于有理宏的辅助数域是有效工具：

- 新数字算子的 \(\mathbb Q(\zeta_p)\) 解释给出严格 Hilbert 90 余边界和正向周期。
- 已有 B17 的 \(\mathbb Q(\sqrt{-2})\) 范数环面解释具体有理二维矩阵的乘法与逆词。
- 同余稳定子、cusp 与 Bruhat--Tits 树仍可组织真实宏群；群中的存在性必须接上正向位置账本。

当前最可用的新局部到整体定理，是平衡初等变换对总和与完整仿射整数格的轨道分类。它已在三份复制上实现，并给出所有三整除维数的判据。下一步应研究在原维数的降秩核中如何获得同类轨道控制；这个问题没有被更换数域解决。

## 8. 核验

`work/verify_digit_replica_transvections.py` 精确检查 level 反例、二次域系数恒等式、R 模指数与一次平均；同一入口检查新副本定理。数域扩张不变性与一般模论必要性由上述线性证明承担。

未扩展任意权重辫子关系也是一条边界：权重 \((27,3,1)\) 的标签换位词 010/101 相等，但 \((27,1,3)\) 不相等。不能仅凭几何链的 Burau 关系为任意权重次序构造共同中心周期；脚本保留了这一精确反例。

## 9. 原维数的新接口：平坦三重块与六项 Artin 关系

还可以从 AI-3 的载体交换得到一条不增加位置数的统一结构。考虑 r 个三重块 \(u_i^3\) 和一个单位置载体 w。交换第 i 块与载体只需一次真实三平均：平均 w 和该块的两个位置，得到
\[
w'=u_i,\qquad u_i'=(2u_i+w)/3.
\]
第三个旧 \(u_i\) 位置成为新载体。以 \(d_i=u_i-w\) 为坐标，矩阵为
\[
T_i:\quad d_i'=-d_i/3,\qquad d_j'=d_j-d_i\ (j\ne i).
\tag{4}
\]
所有系数都与总维数无关。

固定两个不同三重块 i、j。其二维差分部分上
\[
T_i=\begin{pmatrix}-1/3&0\\-1&1\end{pmatrix},\qquad
T_j=\begin{pmatrix}1&-1\\0&-1/3\end{pmatrix}.
\]
乘积的迹为 1/3、行列式为 1/9，故
\[
(T_iT_j)^3=-\frac1{27}I
\]
在这七个位置的局部零和偏差空间上成立。全空间准确公式是
\[
C_{ij}=(T_iT_j)^3=(T_jT_i)^3,
\qquad C_{ij}|_{\{i,j,w\}}=\Pi_{ij}-\frac1{27}(I-\Pi_{ij}),
\tag{5}
\]
其中局部均值为 \(\mu=(3u_i+3u_j+w)/7\)，其余块值保持不变。

于是各对生成元满足六项 Artin 关系
\[
T_iT_jT_iT_jT_iT_j=T_jT_iT_jT_iT_jT_i.
\tag{6}
\]
五步正向词 \(T_jT_iT_jT_iT_j\) 精确实现 \(C_{ij}T_i^{-1}\)。这给出一个对所有 r 有效的局部逆接口，不需要重新搜索每个素数的宏。

但 r>=3 时，\(C_{ij}\) 不与第三个 \(T_k\) 交换，且不是全局零和空间上的标量。它不能直接当作全局射影逆。脚本独立核对35对矩阵关系、18次完整系数基上的真实交换，并检查这种不交换。

从群表示角度，这给出所有边标签为6的 Artin 群到实际宏群的同态。两个生成元对应球面型 \(I_2(6)\)，存在局部中心；至少三个生成元的抽象 Coxeter 伴群已经不是有限群。三节点的标准 Gram 矩阵对角为1、非对角为 \(-\sqrt3/2\)，特征值包括 \(1-\sqrt3<0\)。因此不能直接套用球面 Artin 群的共同全扭转论证。这里没有证明表示忠实，也没有排除像中存在其他正向中心关系。

五元的对照解释了资源差别。对 \((u^3,a,b)\)，以大块为参考的两次载体交换，其归一化乘积迹为 \(-5/3\)、行列式为1。若它有有限射影阶，则该有理迹须为代数整数，矛盾。三重块从一个增至两个，确实创造了新的局部正向逆周期；并非只增加了几个可选三元组。

## 10. 素数问题可统一进入这些固定公式

设 \(p=3r+\delta\ge7\)，\(\delta\in\{1,2\}\)。已有素数高维归约先得到
\[
B_p(u,v)=(u^{p-4},v^3,w),\qquad w=-(p-4)u-3v.
\]
平均 w 与两个 u，令 \(t=(w+2u)/3\)。结果可组织为
\[
\bigl((u^{r-2},v,t)^{[3]},\ u^\delta\bigr).
\tag{7}
\]
尚存至少一个 u 与一个 v，所以 \(p\nmid u-v\) 的见证不会丢失；清三进分母和本原化也保持该见证。该入口只需一次原子操作。

由此，每个未解素数都进入 r 个等重三块加一或两个单位置载体。任选一个载体及两个三重块，均可调用第9节同一组六步／五步公式。其不等权交换图连通，所以已有全 GL 的 Zariski 闭包定理适用；但算术有限指数与正向终端覆盖仍须另证。

一个更统一的待证接口是：对 (7) 这个二维输入族，允许上述载体交换及块重新标号，能否总使某个实际三元组的和为零？可以允许轨道进入更高维平坦核，不必每轮返回 B_p。由[三个零的统一终端](../sources/outputs/triple_average/history/triple_average_one_tripling_stabilization.md)第11节，p>=11时这就足以收尾。

这条路线的优势是原位置数不变、生成元公式不随 p 改写；明确缺口是重叠七元控制器的中心收缩如何拼接。它是一个具体的新研究问题，本文尚未证明这种受限生成元库已经充分。

## 11. 29元当前返回库的严格搜索边界

后续状态：[29元完整证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)已通过三因子周期闭合。本节排除的是二因子及A0^jB词形，结论保持成立；它没有排除新证书使用的词形。

启用全部已证的小于29的子问题，当前编译器产生1195个返回矩阵，其中已经包括一步宏
\[
A=\begin{pmatrix}-3&0\\25&1\end{pmatrix}
\]
的射影代表。逐对检验714610个无序乘积，没有有限射影阶乘积；因此该库没有一因子或二因子的正向标量周期。这里只判断周期，不声称一般归零路径不存在。

还可完全排除所有指数的 \(A^jB\)，而不逐层搜索。令 \(r=n-4\)、\(B=(a,b;c,d)\)，在坐标 \((u,ru+4v)\) 中，A 的射影作用为 \(\operatorname{diag}(1,-1/3)\)。置
\[
t=(-1/3)^j,\quad U=4a-rb,\quad V=4d+rb,\quad\Delta=ad-bc.
\]
则 \(A^jB\) 的迹平方与行列式满足有限阶必要条件之一
\[
(U+Vt)^2=16k\Delta t,\quad k\in\{0,1,2,3,4\}.
\tag{8}
\]
k=0包含射影二阶；k=1、2、3对应三、四、六阶；k=4只保留真正标量，排除非平凡抛物矩阵。

对每个B精确求这五个二次方程的有理根，再检查根是否为 \((-1/3)^j\)、j>=0，就覆盖了全部指数。当前1195个模板均无这种周期。程序另用人为构造的指数57、100等标量周期检验求根算法，确保它不是有限深度截断。

脚本为 `work/audit_bn_current_cycles.py`，统一ID为 `b29-current-cycle-boundary`。该结论不排除三个以上不同模板组成周期、条件宏、跨B核路径或高秩载体控制器；它仅说明增加A的重复次数不能为当前单个B补出所需周期。

<!-- END SOURCE doc-4a708197aa0f -->

---

<a id="doc-3601bd1cd400"></a>

## 原文导签：三平均问题的局部算术轨道图景：结构性猜测与证明路线

来源：`outputs/triple_average/history/triple_average_structural_picture_conjecture.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_structural_picture_conjecture.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-3601bd1cd400 -->
# 三平均问题的局部算术轨道图景：结构性猜测与证明路线

日期：2026-09-10。

本文记录一个解释当前各种结果的结构性图景。它不是任意 (n) 的定理，也不把有限计算、单个维数证书或样本群轨道外推成一般结论。文中使用“已证”“观察”“猜测”“待证”四种层级。

## 1. 核心判断

目前的因子归约看起来琐碎，是因为它们把一个可能具有统一算术结构的问题拆成了位置级的行—列操作。真正反复出现的对象不是某个特定素数维数，而是：

1. 三平均在 (R=\mathbb Z[1/3]) 上产生的有向线性操作；
2. 合法性在每个非三素数处给出的局部 (p)-进条件；
3. 正向可实现宏及其正向逆词生成的算术半群；
4. 该半群在局部射影空间上的有限轨道和终端 cusp。

因此可以把原问题的深层版本表述为：

> 对每个维数 (n)，三平均宏在其参数核上是否生成足够大的正向算术轨道，使每个满足 (G=3^a) 的合法有理点都能进入一个可终止的终端轨道？

这里“足够大”不能只理解为有限模像大，也不能只理解为 Zariski 稠密；还必须包含正向实现、局部适用域、真实物理尺度和终端覆盖。

## 2. 当前已经观察到的统一现象

### 2.1 素数层级不是偶然的模数标签

对 (p>3) 的素数维数，(B_p(u,v)) 的合法方向要求 (p\nmid u-v)。换坐标后，合法方向对应于

\[
t=\frac{u}{v-u}\in\mathbb Z_{(p)},
\]

在 (\mathbb Q_p) 中就是闭开圆盘 (\mathbb Z_p)。保持这个圆盘的射影稳定子是 Iwahori 型稳定子；其整数部分是一个共轭的

\[
\Gamma_0(p)
\]

子群。因此，(p) 出现在同余子群中不是搜索算法碰巧选择的模数，而是合法域本身的局部几何决定的。

已证的 (17,19,23) 正好实现了共轭 (\Gamma_0(p)) 的充分子群；(13) 使用了带额外模 2 数据的有限指数子群；(12) 则出现了共轭 (\Gamma_0(8))。这说明“素数”和“同余子群”之间存在自然联系，但素数既不是同余方法的充分条件，也不是必要条件。

### 2.2 (25) 是 (5)-进层级的延伸

二十五元证书实现了

\[
H_{25}=C_0\Gamma_0(25)C_0^{-1}
\]

并完整遍历

\[
|\mathbf P^1(\mathbb Z/25\mathbb Z)|=25+5=30
\]

个标签。这里不是把模 25 粗略降为模 5；模 (25) 的额外层级保留了 (5)-进精度，并产生 6 个 cusp，其中只有宽度 25 的 cusp 合法。

因此 (25) 更合理的解释是：它展示了同一个局部稳定子机制在素数幂 level 上的第一层非平凡延伸，而不是一个孤立的小基例。

### 2.3 因子闭包是算术轨道的组合实现

若 (n=ab)，且已经证明 (A(a))、(A(b))，因子桥并不是把两个不同维数的宏群形式相交，而是把 (n) 个真实位置安排成 (b) 行、每行 (a) 个位置：

\[
\text{合法 }n\text{ 元状态}
\longrightarrow
\text{合法 }a\text{ 元行}
\longrightarrow
\text{合法 }b\text{ 元商}.
\]

这是一种位置级的诱导—限制过程：先在纤维方向使用 (A(a))，再在商方向使用 (A(b))，必要时转置后重复。多例外三进进位负责保证行容量、局部见证和商合法性。

所以奇数合数闭包虽然外观琐碎，实质上是在构造一个兼容局部合法性的乘法范畴。当前证明只在位置账本层面实现这个范畴，还没有把它抽象成统一的表示论或 Hecke 对应。

### 2.4 (5) 的特殊收尾是复制半群，不是 (A(5))

五元本身不是可直接调用的充分性接口。商为 5 时，归并得到若干份相同合法五元状态；副本数 (a\ge2) 可写为

\[
a=2x+3y.
\]

两份复制调用 (A(10))，三份复制调用 (A(15))。这说明 (5) 的一次出现可以由复制半群 \(\langle2,3\rangle\) 收尾。二十五元后来由独立的 (\Gamma_0(25)) 证书补齐，才把这个历史上的“一次 5”边界升级为任意五幂。

这个现象提示：因子递推中出现的小素数障碍，有时可由复制半群消除，有时则需要新的局部 level 证书；两者不能混为一谈。

## 3. 结构性猜想

### 猜想 I：局部稳定子实现猜想

令 (N) 为 (n) 的非三部分。对适当参数核 (K_n)，真实正向可逆宏半群的整数部分应包含一个由 (N) 的局部稳定子决定的有限指数算术子群：

\[
H_n\supseteq C\Gamma_0(N)C^{-1}
\]

在二维情形成立；更高秩时应替换为保持相应局部格、旗标或多圆盘的算术子群。

这不是说 (\Gamma_0(N)) 必须等于真实宏群，也不是说所有合数都需要独立构造同余群。因子桥可能把多个较低秩局部系统组合起来，而不产生新的独立二维群。

### 猜想 II：有限轨道—终端覆盖猜想

若 (H_n) 是真实正向可实现的有限指数子群，并且每个生成元的逆也有正向词，那么满足局部合法性的本原参数只有有限多个 (H_n)-轨道。对每个合法轨道，只需给出一个终端代表和有限正向收尾词，即可得到整个核的充分性。

二维时终端代表是 cusp；高秩时可能是终端射影点、旗标或一个已解子块的边界轨道。

需要强调，有限模像大、Zariski 稠密或群的抽象生成性都不足以推出该猜想。还必须证明：

- 每个矩阵在实际参数域中可执行；
- 逆矩阵由正向三平均词实现；
- 物理尺度满足三进分母和局部余数限制；
- 终端代表覆盖所有合法轨道；
- 从任意一般输入确实能进入该参数核。

### 猜想 III：素数幂 level 的递归局部猜想

对 (p^k) 的维数，合法域应对应 (p)-进稳定子过滤的第 (k) 层，真实宏的整数部分应逐层包含足够大的

\[
\Gamma_0(p^k)
\]

型子群，或包含具有相同轨道覆盖能力的替代算术群。(25) 是 (p=5,k=2) 的第一个完整样本。

更强的版本要求这些 level 之间由自然的投影、提升和 Hecke 型对应连接，使 (A(p^k)) 不必每次重新搜索。

### 猜想 IV：合数的局部—组合兼容猜想

若 (n=\prod p_i^{e_i})，则高维参数核应同时携带各个 (p_i)-局部见证。因子桥的作用不是消灭这些见证，而是把它们分散到不同的行和商坐标中，使每个局部条件至少在某个方向被保留。

因此，合理的统一对象可能是一个局部条件的乘积空间：

\[
\prod_{p\mid N}\mathcal X_p
\]

上的有向算术轨道，而不是单一模 (N) 的粗标签。多危险素数进位桥是这个乘积空间上的显式坐标分解。

### 猜想 V：二进层需要不同的稳定子理论

因子 (2) 和 (4) 不能简单照搬奇素数。(2)-进处同时出现：

- 奇偶性是单位/非单位的第一层信息；
- 三平均除以 3 不改变二进单位性，却改变实际重数和均值格；
- 减半桥要求先构造全偶重数；
- 在早期桥中，(v_2(n)=1,2) 的一般输入可能只留下两个相反均值，使本原 (G) 含有 2。

现在的低二进重数定理已经用至多两次预备平均、十二元子问题和强归纳补齐了 (v_2(n)=1,2) 的合数入口。因此“二进方向尚未解决”已经是过时表述。尚待理解的是：这些具体的奇偶分支能否统一成一个带层级的 Iwahori/Parahoric 型稳定子，以及“偶重数形成—减半—重新合法化”是否真的是不同二进 level 之间的自然对应。

## 4. 为什么现有证明看起来琐碎

现有证明混合了三种不同层次的工作：

1. **局部算术控制：** 模 (p^k)、(p)-进稳定子、尺度周期、cusp 和正向逆词；
2. **组合调度：** 多例外进位、行容量、位置重排、复制 2/3 半群；
3. **终端算法：** 已解子问题、零填充、减半和具体三平均词。

当第二、三层还没有被第一层的算术对象统一解释时，每个新维数都需要重新写行容量和调度账本，于是产生大量局部引理。它们未必是最终数学结构，只是当前结构理论尚未完成时的坐标化实现。

更理想的证明应把三层压缩为：

\[
\text{局部稳定子}
\longrightarrow
\text{正向算术轨道}
\longrightarrow
\text{终端 cusp/边界}
\longrightarrow
\text{统一收尾}.
\]

因子归约则应成为这个框架中的诱导函子，而不是一组互不关联的特例。

## 5. 可检验的中间命题

以下命题比“任意 (n) 都可解”弱，但足以检验上述图景是否正确。

### 命题 A：局部稳定子上界的 level 版本

对每个 (p^k\mid N)，证明合法参数集合的双射自同构群在坐标变换后包含于相应的 (p^k)-Iwahori 稳定子；明确其整数部分和射影标签空间。

### 命题 B：正向生成元的局部提升

若已在 level (p^k) 构造一组正向生成元，研究它们能否通过固定的三进模板提升到 level (p^{k+1})，并保持正向逆词。(25) 的 30 陪集证书可作为第一个测试对象。

### 命题 C：多素数的局部张量接口

对 (N=pq) 或 (p^aq^b)，建立一个不依赖具体输入的局部标签空间和行—商投影，使每个 (p)-见证和 (q)-见证分别在至少一个商坐标中保留。该命题若成立，可把多危险素数桥解释为局部张量分解。

### 命题 D：二进减半的算术对应

把已经证明的 (v_2(n)=1,2) 低二进桥，以及已有的 (B_n) 偶重数减半，写成一个统一的 (2)-进层级对应。目标不是再补一个合数入口，而是识别预备平均、十二元调用和减半步骤在局部稳定子或 Hecke 型对应中的共同算术对象。

### 命题 E：正向轨道的终止函数

在每个局部轨道上寻找一个同时控制实高度、(p)-进深度和副本复杂度的良序函数。仅有平方能量下降不够，因为清分母和本原化可能增加整数高度。

## 6. 与自守/Hecke 视角的关系

同余子群提供了算术轨道；Hecke 型对应可能描述不同 level、不同因子分解和不同子块调用之间的转换。一个可能的字典是：

- 正向三平均宏：局部算术对应或带适用域的 Hecke 箭头；
- 正向逆词：可逆的 Hecke 路径，而不是形式矩阵逆；
- 因子桥：诱导/限制或纤维化后的对应；
- cusp：终端退化方向；
- 三进复制：沿 (3)-局部方向的稳定化或退化；
- (2)-进减半：不同 level 之间的二进对应。

这套语言目前只是解释框架。必须先为具体宏证明算术格保持、正向实现和轨道覆盖，才能称为 Hecke 结构；不能因为矩阵形状类似就直接宣称存在自守表示。

## 7. 换数域后的大胆图景

下面把底域从 \(\mathbb Q\) 换成数域 \(K\)。这部分是研究猜想，不是当前项目已经证明的定理。

### 7.1 从整数 gcd 到内容理想

令

\[
R_K=\mathcal O_K[1/m]
\]

并在 \(K\) 中使用 \(m\)-平均。中心化、清分母后，坐标属于 \(R_K\)。对状态 \(X=(x_i)\)，用坐标生成的分数理想记为

\[
\operatorname{cont}(X)=\sum_i R_K x_i.
\]

在 \(\mathbb Q\) 中，这个理想就是坐标 gcd 生成的主理想。一般数域中，它可能不是主理想，因此“除以 gcd 后本原化”必须改成理想本原化，并且可能留下类群信息。

最自然的必要条件是：若 \(\mathfrak p\nmid m\)，且所有中心化坐标在 \(\mathfrak p\) 下同余，则一次 \(m\)-平均仍保持这个余类，因为 \(m\) 在 \(R_K/\mathfrak p\) 中可逆。因此不可消除的局部见证只能位于 \(m\) 上方。

由此得到第一层猜想：

\[
\boxed{\operatorname{Supp}(\operatorname{cont}(X))\subseteq
\{\mathfrak p:\mathfrak p\mid m\}}
\]

可能是可达性的理想版必要条件。对类数为 1 的数域，它有希望退化为“gcd 的所有素因子整除 \(m\)”；对一般数域，还可能必须加入

\[
[\operatorname{cont}(X)]\in
\langle[\mathfrak p]:\mathfrak p\mid m\rangle\subseteq\operatorname{Cl}(K)
\]

这样的类群兼容条件。

### 7.2 局部空间由素理想而不是有理素数组成

同一个有理素数 \(p\) 在 \(K\) 中可能分裂、惰性或分歧。因此原来一个模 \(p\) 的合法性条件会分裂成若干 \(\mathfrak p\)-局部条件。若 \(N\) 是维数的非操作部分，合理的局部参数空间不是单一的模 \(N\) 标签，而是

\[
\prod_{\mathfrak p\mid N,\ \mathfrak p\nmid m}\mathcal X_{\mathfrak p}.
\]

多危险素数三进进位桥可以被看作这个乘积空间上的显式坐标分解：它把不同素理想的见证分散到不同的行和商坐标中，而不是寻找一个同时对所有素理想都为单位的共同见证。

### 7.3 同余子群升级为 \(S\)-算术群

在二维参数核中，\(\mathbb Q\) 上的共轭 \(\Gamma_0(p)\) 应被替换为

\[
\Gamma_0(\mathfrak p)\subseteq SL_2(\mathcal O_K),
\qquad
\Gamma_0(\mathfrak n)=
\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}:c\in\mathfrak n\right\}.
\]

若允许在有限集合 \(S\) 中的素理想处取分母，真实对象更自然地是 \(S\)-算术群。多个无限嵌入还会产生

\[
\operatorname{Res}_{K/\mathbb Q}SL_2
\]

的实点/复点作用，而不是单一的实射影群。相应的有限轨道可能位于 Hilbert 模曲面、Hilbert 模簇或多个 Bruhat--Tits 建筑的积上；\(\mathbb Q\) 中的 cusp 只是最低秩投影。

因此第二层大胆猜想是：

> 三平均的同余子群结构在数域上会变成 (S)-算术群在局部 Bruhat--Tits 建筑积上的有向轨道问题。

### 7.4 单位群会改变尺度周期

在 \(\mathbb Q\) 中，单位只有 \(\pm1\)。在一般数域中，

\[
\mathcal O_K^\times\cong\mu_K\times\mathbb Z^{r_1+r_2-1}
\]

可能是无限的。因此同一理想尺度下会有无限多个单位方向，归一化不再唯一，宏的物理返回尺度也不再只由 \(\pm m^{-k}\) 描述。

一个合理的尺度猜想是

\[
\lambda\in\langle m^{-1},\mathcal O_K^\times\rangle,
\qquad
\lambda\equiv1\pmod{\mathfrak n}
\]

对所有相关 level \(\mathfrak n\) 成立。\(\mathbb Q\) 中的
\(3^k\equiv\pm1\pmod p\) 会推广为 \(S\)-单位群在各局部剩余群中的联合阶问题。

如果单位秩为正，有限 cusp 覆盖可能必须先对单位作用取商；否则同一个局部轨道可能分裂成无限多个尺度方向。

### 7.5 类群可能制造新的全局障碍

在非主理想数域中，局部合法性不一定足以保证全局可达。可能出现

\[
\text{所有局部见证均可消除，但 }\operatorname{cont}(X)\text{ 的理想类非平凡}.
\]

如果真实宏只能产生主理想尺度，那么这类状态即使在每个局部建筑中都合法，也可能无法归零。因此更强的数域判据可能是

\[
\boxed{\text{局部 }m\text{-光滑性}
\ +\ \text{类群兼容性}
\ +\ \text{单位轨道兼容性}.}
\]

这也是为什么类数为 1 的数域应作为第一批实验对象：它们能隔离局部轨道问题，暂时排除类群障碍。

### 7.6 数域扩张可能改变可达性

若 \(L/K\) 是数域扩张，\(K\) 中的一个素理想可能在 \(L\) 中分裂：

\[
\mathfrak p\mathcal O_L=\mathfrak P_1\cdots\mathfrak P_g.
\]

原来不可分离的局部见证可能因此在 \(L\) 中分裂成多个方向。于是我猜：

\[
X\text{ 在 }K\text{ 中不可达}
\not\Rightarrow
X\text{ 在 }L\text{ 中不可达}.
\]

反向地，\(K\) 中的路径当然可以视为 \(L\) 中的路径，所以可达性具有上升性，但通常没有下降性。一个可能的研究策略是先在类数较小、分裂较充分的扩张域中构造局部轨道，再研究 Galois 不变路径能否下降回原数域。

### 7.7 虚二次域可能最适合检验范数环面

实二次域的单位秩会使轨道变得复杂；虚二次域的单位群有限，却仍保留二次型、范数形式、theta 级数和 Hecke 字符。项目中出现的

\[
\mathbb Q(\sqrt{-2}),qquad 3=N(1+\sqrt{-2})
\]

提示某些二维返回宏可能来自范数环面。大胆猜想是：

> 某些三平均返回宏的二维参数核，本质上是一个 (S)-单位范数方程；宏复合对应范数乘法，正向逆词对应范数为 (3^k) 的元素，终端 cusp 对应极小范数或唯一合法边界类。

当前证据只证明了二次型和范数的候选关系，尚未证明实际宏就是理想乘法；因此这仍属于结构猜想。

### 7.8 数域与操作平均数的统一局部化

若操作是 \(m\)-平均，底域是 \(K\)，自然的局部集合为

\[
S_{m,K}=\{\mathfrak p:\mathfrak p\mid m\}.
\]

真正的局部数据同时依赖操作分母和数域分解：

\[
(m,K)\longmapsto\{K_{\mathfrak p}:\mathfrak p\mid mN\}.
\]

最大胆的总猜想是：若 (K) 的类群障碍已被排除，且状态在所有 \(\mathfrak p\nmid m\) 处没有不可消除的共同余类见证，则

\[
\boxed{
X\text{ 可达}
\Longleftrightarrow
\text{局部 }m\text{-光滑性}
 +\text{全局类群/单位兼容性}
 +\text{局部正向轨道可进入终端边界}.
}
\]

在 \(K=\mathbb Q\)、\(m=3\) 时，这应退化为当前的三幂内容判据；在一般数域中，它会成为一个真正的 adelic 局部—整体问题。

### 7.9 建议的数域对照实验

最先比较的不是大量随机数域，而是三组性质不同的底域：

\[
\mathbb Q,qquad \mathbb Q(i),qquad \mathbb Q(\sqrt{-2}).
\]

它们分别测试平凡单位群、有限但不同的分裂行为，以及范数环面和 theta 结构。每个底域应记录：

- 内容理想及其 \(S\)-支撑；
- 各素理想局部见证；
- 单位作用下的轨道数；
- 返回宏的实际 \(S\)-单位尺度；
- 是否存在类群或 Galois 下降障碍；
- 终端边界是否仍表现为有限 cusp 或更高秩旗标。

如果三个底域中都出现同一类“局部稳定子—正向轨道—终端边界”链条，那么同余子群就更可能是普遍的 (S)-算术动力系统，而非有理数域的偶然现象。

## 8. 不能从当前证据推出的结论

- 不能由 (17,19,23,25) 的成功证明推出所有素数都有同余子群证书。
- 不能由大有限模像推出真实宏群有限指数。
- 不能由 Zariski 稠密推出正向可达性或终端覆盖。
- 不能把不同维数的宏群形式相交来证明合数闭包。
- 不能把某一个 (B_n) 核减半桥单独当作任意维数的素数定理；低二进合数入口已有独立的多例外证明，二者的适用范围必须分开。
- 不能把 (A(5)) 当作已证；当前放开五幂依赖的是 (A(25)) 加强归纳。

## 9. 建议的研究顺序

1. 先完成 (p^k) level 的统一局部稳定子和标签理论，特别是检验 (25) 是否能自然推广到 (125) 或一般 (p^k)。
2. 再研究真实正向宏半群的有限指数性质，优先使用共同第一行、初等平移和物理尺度周期，而不是无区别长词搜索。
3. 对两个不同危险素数，建立局部见证分配的张量/诱导形式，把多例外进位桥提升为一个可复用的局部—整体定理。
4. 把已经完成的 (v_2(n)=1,2) 桥重写成二进 Parahoric/减半接口，检验它是否能与奇素数局部标签形成统一的局部乘积空间。
5. 集中解决素数核的正向算术控制、轨道覆盖和终端 cusp，再把合数归约作为已完成的外层归纳接回去。

## 10. 当前定位

这份图景把项目的已证结果分成两类：

- (7,11,13,17,19,23,25) 等维数提供局部算术轨道和 cusp 证书的样本；
- 奇数闭包、低二进桥、八整除闭包和复制收尾已经把全部合数问题严格归约到素数问题。

两类结果目前还没有被一个统一定理完全连接起来。真正的突破点不是再增加一个孤立合数维数，而是证明“局部稳定子—正向轨道—终端覆盖”这条链对所有素数 level 和一般参数核具有稳定性；一旦素数定理完成，合数部分已经有严格归约。

<!-- END SOURCE doc-3601bd1cd400 -->

---

<a id="doc-2a65f1576ada"></a>

## 原文导签：子问题调用的缺失素数障碍与奇素数维数

来源：`outputs/triple_average/history/triple_average_subproblem_prime_obstruction.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_subproblem_prime_obstruction.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`subproblem-prime-obstruction`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-2a65f1576ada -->
# 子问题调用的缺失素数障碍与奇素数维数

## 1. 什么算一次调用

在固定 n 个位置上，选一个子块 C，将其全部位置变为 C 的均值，称为一个归并调用。调用只能在该子问题已有真实三平均可达证书时执行。

合法调用的内部原子词可以依赖输入并且任意长，但它在原来的 n 个数值上产生的最终线性算子始终是固定矩阵
\[
A_C=I\text{（补集）}\oplus\frac1{|C|}\mathbf1\mathbf1^T.
\]
因此可以把“归并调用次数”与“内部原子操作次数”区分开。下面定理针对前者，不否定不定长原子或宏路径。

## 2. 缺失素数定理

**定理。** 设 \(n\ge7\)，素数 \(p\ne3\) 整除 n。允许使用有限集合 S 中大小的子块归并，且每个 \(s\in S\) 都满足 \(p\nmid s\)。则不存在一个统一常数 L，使所有合法 \(\mathcal B_n\) 有理方向都能经至多 L 次这些调用归零。

允许任意依赖输入的分支、子块位置选择、真实调用词和碰撞；结论仍成立。零调用不改变输入，全零状态单独排除。

**证明。** 每个 \(A_C\) 的系数在 \(\mathbb Z_{(p)}\) 中，并模 p 固定常值向量。固定一个调用词 W，从二维 B 核嵌入
\[
J_n(u,v)=(u^{n-4},v^3,-(n-4)u-3v)
\]
出发，取形式参数 (1,1)。其 n 个坐标在模 p 下全为1，因为最后一个坐标为 \(1-n\)。所以
\[
WJ_n(1,1)\equiv\mathbf1\ne0\pmod p.
\tag{1}
\]
因此线性映射 \(WJ_n:\mathbb Q^2\to\mathbb Q^n\) 不是零映射，其核至多一维。一个固定 W 至多消灭一个非零射影方向。

长度至多 L 的调用词只有有限多个，因为 n 和 S 固定、每步选取的位置子集有限。因此它们的消灭方向只有有限多个。另一方面，取
\[
(u,v)=(1,qn),\quad q=1,2,\ldots
\]
得到无限多个本原合法方向，差值与 n 互素，G=1。这些不可能被有限集合覆盖。证毕。

参数 (1,1) 本身并不合法；证明仅将它用于检验固定线性矩阵不恒为零。无论该词的实际合法域是否包含 (1,1)，这个矩阵恒等式测试都有效。

## 3. 定量形式

设每一步可以使用的不同子集数为
\[
K=\sum_{s\in S}\binom ns.
\]
至多 L 步的词数不超过 \(1+K+\cdots+K^L\)。任何 N 个不同合法射影方向若均可在 L 次调用内归零，则必须
\[
N\le1+K+\cdots+K^L.
\tag{2}
\]
对固定奇素数维数 p，族 \((1,v),1\le v\le H,\ v\not\equiv1\pmod p\)
包含 \(H-1-\lfloor(H-1)/p\rfloor\) 个合法方向，故最坏调用次数至少随
\(\log H/\log K\) 增长。

这个下界仍允许关于输入位长的多项式算法；它只排除统一常数深度的调用树，并解释为何不断扩充一个固定短词表不能完成素数维数的全称证明。

## 4. 十七元的直接后果

对 n=17，每个严格小于17的子问题大小都与17互素，所以即使允许调用所有已经解决的7至16元子问题，也不能用统一有界的调用次数覆盖所有 B17 合法方向。

这与十二、十四、十五、十八元的归约不同：它们使用的子问题大小分别包含所需障碍素数，例如14调用七元，15调用十元，18调用十二元。因而上述 p 整性障碍不适用。

已解决的十三元说明可能的正确替代方式：从真实宏得到可用的群或半群，在参数上进行依赖输入的无界轨道归约。十七元仍可使用小子问题，但必须允许其调度次数增长，或者构造一个良序的局部--实势函数；不能要求有限数目的固定调用模板一步覆盖所有有理斜率。

## 5. 局部仿射格接口

对整数子块 \(c_1,\ldots,c_s\)，取 \(a=c_1\)，差值 gcd 为 d，令
\[
T=\sum_i(c_i-a)/d.
\]
若非全等，则其中心化本原 G 恰为
\[
G_C=s/\gcd(s,T).
\tag{3}
\]
因此在已解决的子问题大小上，可用精确条件
\[
\mu_C\in a+d\mathbb Z[1/3]
\]
决定是否调用。式 (3) 的证明与程序见[十五元完整归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md)。

把这些合法域与固定词作用同时保留，得到的是带局部条件的有向控制系统。第2节表明：如果调用的分母集合遗漏某个 \(p\mid n\)，这个系统必须有可重复执行的控制循环，而非统一有界的有向无环调用图。

这是一条适用于任意 n 的算法结构限制，不证明不可达，也不证明某个具体返回群薄。它与复制消去开放性并行：复制可能允许使用含 p 因子的更大子块，但如何消去新增位置仍是独立问题。

## 6. 核验与后续

work/verify_subproblem_prime_obstruction.py 检查6组 (n,p)、每组120步精确符号归并，逐步核验模p常值方向与加权零和；另检查允许分母含p时公式失效的边界。一般任意长度的结论由 p 整性与维数论证给出，不来自720个有限步骤。

下一步应在 B17 的合法局部域寻找带循环的调用系统，并证明每个循环的终止进度。三个代理继续分别处理多链运输、高秩算术群和复制下降；本定理可用于排除它们方案中不必要的统一常数步数要求。

<!-- END SOURCE doc-2a65f1576ada -->
