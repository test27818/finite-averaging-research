# 全部 3p-1 的统一完成与五平均最优阈值

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../../README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

日期：2026-09-15。p 表示每次平均的元数，n 表示原位置数。

## 1. 定理与剩余范围

**定理。** 对每个素数 p>=5，n=3p-1 的任意非全等有理输入，经有限次原位置 p 平均可达全等，当且仅当本原中心化差分 gcd 为 G=1。

特别地，五平均14元完整解决。接已有11、12、13元及全部n>=15的定理，并结合10元反例，得到
\[
\boxed{N(5)=11.}
\]

一般证明适用于全部 p>=7，无参数表、平均词搜索或有限方向图。p=5使用同一类重叠返回，加一个显式夹乘恒等式；方向与单位尺度仍由解析公式完成，也不枚举模群。

证明沿用 Morris 2007 定理6.1(2)、Serre 强同余子群性质及项目既有深同余、正向取逆引理。原文访问与外部依赖边界见[深同余引理](../../history/prime_arity_even_middle_congruence_and_eighteen.md)。本文没有用程序证明这些外部无限群定理。

此后任意素数的临界全解仍剩：一般2p+2，以及3p+1至3p+9中尚未完成的偏移族。不是声称这些剩余维数均已证明。p=2、3、5、7现在各自已具有最优阈值。

## 2. 核心、标准对合及自由角色交换

置
\[
r=p-1,\quad n=3p-1,\quad d=p^2-3p+1.
\]
无条件下半带入口把任意合法输入送到
\[
K(a,z)=(a^p,(rz-a)^p,(-pz)^r),
\quad \gcd(a,z)=\gcd(a+pz,n)=1.
\tag{2.1}
\]
标准两步对合及等大块角色交换为
\[
A=\begin{pmatrix}0&-d\\-1&0\end{pmatrix},
\quad A^2=dI,\qquad
S=\begin{pmatrix}-1&r\\0&1\end{pmatrix}.
\tag{2.2}
\]
A 的实际尺度为1/p，S只更新两个p块的角色标签。d与pn互素。

以下全部矩阵表示整体非零标量意义下的真实核心返回。所有位置共同缩放只用于分析，不作为额外物理操作。

## 3. 三步重叠对合

给定 sigma和h，先平均
\[
(A^{p-\sigma},C^\sigma),
\]
得到p份新值
\[
D=\frac{p-\sigma}{p}a-\sigma z.
\]
保留其中r=p-1份作最终载体。其余位置为 sigma份旧A、p份旧B、r-sigma份旧C以及一份D。

平均
\[
(A^{h-\sigma},B^h,C^{p+\sigma-2h}),
\]
再平均其余p份，总计三次原子平均。只需
\[
0\le h-\sigma\le\sigma,\quad h\le p,\quad
0\le p+\sigma-2h\le p-1-\sigma.
\tag{3.1}
\]
实际返回矩阵为p^-2乘
\[
J_{\sigma,h}=
\begin{pmatrix}
-p\sigma&p[nh-p(p+\sigma)]\\
-(p-\sigma)&p\sigma
\end{pmatrix}.
\]
其平方为
\[
\boxed{J_{\sigma,h}^2=p f_{\sigma,h}I,\qquad
f_{\sigma,h}=p^3-n(p-\sigma)h.}
\tag{3.2}
\]
f模n为p³，故非零且与n互素。重复三步返回提供真实正向射影逆。

对所有p>=7，以下四个参数同时满足(3.1)：
\[
(\sigma,h)=(2,3),(2,4),(3,4),(3,5).
\tag{3.3}
\]
最紧的计数是p+2-2*4=p-6和p+3-2*5=p-7，均非负。这是整个一般证明唯一的p>=7容量门槛。

## 4. 自由角色交换把根理想降到2n

固定sigma=2或3，取h=sigma+1，记
\[
f_\sigma=f_{\sigma,h},\quad
g_\sigma=f_{\sigma,h+1}=f_\sigma-n(p-\sigma).
\]
由于p不整除sigma，且f_sigma与n互素，
\[
\gcd(f_\sigma,g_\sigma)
=\gcd(p^3,n(p-\sigma))=1.
\]
相邻对合的商为
\[
T_\sigma=J_{\sigma,h}^{-1}J_{\sigma,h+1}
=\begin{pmatrix}1&-p\sigma n/f_\sigma\\0&g_\sigma/f_\sigma\end{pmatrix}.
\]
它与角色交换S的交换子恰为
\[
\boxed{[S,T_\sigma]=
U\left(\frac{n[n\sigma-pr]}{g_\sigma}\right).}
\tag{4.1}
\]
两个整数系数相差n，并且
\[
\gcd(2n-pr,3n-pr)=\gcd(n,pr)=2.
\tag{4.2}
\]
令
\[
R_0=\mathbb Z[1/|f_2g_2f_3g_3|].
\]
两个倍率及其逆生成R_0，因而上根参数在R_0上封闭。式(4.1)、(4.2)与Bezout给出U(2nR_0)。

不需要先假定d可逆：对任意x属于2nR_0，已可执行U(dx)，而
\[
A\,U(dx)\,A^{-1}=L(x).
\]
因此也有L(2nR_0)。深同余引理给出
\[
\boxed{\Gamma(4n^2,R_0)\text{ 正向可执行}.}
\tag{4.3}
\]
2已整除n，故控制层没有任何额外素数。这比先产生含r或p的深根再逐项消除更直接。

## 5. 单位像满时，可以在方向调整后重新本原化

以下小引理避免一个不必要的行列式局部化要求。

**局部本原化引理。** 设R的反演素数均不除正整数M，Gamma(M,R)已可执行，且R单位模M满射。给定本原整数列v，若一条实际正向路径的矩阵属于GL2(Z_(M))，其中Z_(M)表示分母与M互素的有理数环，并使其方向满足z/y=0模M、y为局部单位，则可以正向精确送到(0,epsilon)，epsilon为某个R单位。

证明：将路径后的矩阵列清去与M互素的分母，得到整数列(z_0,y_0)。因矩阵在每个ell|M处可逆，该列仍局部本原，故其整数坐标gcd与M互素。除这个gcd后得到本原整数列(z,y)，仍有z=0模M、y为单位。单位像满射给epsilon=y模M。

取alpha z+beta y=1，调整(alpha,beta)为(alpha+ty,beta-tz)，使alpha=0模M。则
\[
P=\begin{pmatrix}
y/\epsilon&-z/\epsilon\\
\epsilon\alpha&\epsilon\beta
\end{pmatrix}
\in\Gamma(M,R),\qquad
P(z,y)^T=(0,\epsilon)^T.
\tag{5.1}
\]
Gamma(M,R)提供真实正向实现。实际状态和分析列之间仅差共同非零尺度，因此同样产生零终端。证毕。

引理不允许忽略本原化；它明确追踪被除因子在模M下是单位。只有在R单位像满时，才可不将路径中每个行列式因子预先反演。若单位像只是一个真子群，原来保留R本原性的要求仍然重要。

## 6. 奇数数字与乘3折返给全部模n单位

保留旧C的两块混合为
\[
F_t=\frac1p
\begin{pmatrix}
t&r(p-t)/2\\0&p
\end{pmatrix},
\qquad t\text{ 奇},\quad -p\le t\le p.
\tag{6.1}
\]
它的原位置两组分别取(p-j,j)和(j,p-j)份A、B，其中j=(p-t)/2。

F_1的整数代表行列式为p，与4n²互素，故既有安全整数返回取逆引理适用。其上三角倍率反演p，先将p加入R。随后
\[
C_b=F_bF_1^{-1}
=\begin{pmatrix}b&r(1-b)/2\\0&1\end{pmatrix}
\]
对每个奇数1<=b<=p、gcd(b,n)=1都实际存在。行列式b与控制层互素，故C_b的逆可执行。上下根随倍率共轭扩张到这些b全部反演后的有限局部化环R，且Gamma(4n²,R)继续成立。

因为n=3p-1不被3整除，3属于这些安全数字。对任意模n单位u，取正平衡绝对代表b<n/2；n偶使b必奇。若b>n/4，以
\[
b\longmapsto |n-3b|
\tag{6.2}
\]
替代。结果仍是正奇数、与n互素，并严格减小；它只改变u所乘的符号和3的幂。最终
\[
1\le b\le n/4<p.
\]
这个b已是R单位。倒推(6.2)，得到u的R单位提升。因此
\[
R^\times\longrightarrow(\mathbb Z/n\mathbb Z)^\times
\quad\text{满射}.
\tag{6.3}
\]
没有要求3是模n的原根，也没有单位代表表。

## 7. 同一条方向循环适用于全部p>=7

取
\[
V=J_{3,4}A/p^3,
\]
在整幺模(z,y)=(z,a+pz)坐标中有
\[
V=\begin{pmatrix}1&-3/p^2\\0&1\end{pmatrix}\pmod n,
\]
\[
\operatorname{tr}V=2-\frac{n(5p-3)}{p^3}=2\pmod4.
\tag{7.1}
\]
平移系数在所有ell|n处均为单位，因为3不整除n。迹的模4条件适用于全部p，不必选择奇偶分支。

已有局部射影循环引理因此适用于所有2幂和所有奇素数幂ell|n。指数CRT用V的一次非负幂将任意合法方向送到
\[
z/y=0\pmod{4n^2}.
\tag{7.2}
\]
A的行列式可能未在R中反演，但它与n互素；第5节正好允许在方向调整后处理这个共同内容。

## 8. 从n到4n²的全部单位尺度

已有R单位
\[
\kappa_2=g_2/f_2=1-\frac{n(p-2)}{f_2},\quad
\kappa_3=g_3/f_3=1-\frac{n(p-3)}{f_3}.
\]
对任意奇素数ell|n，有gcd(p-3,n)只含2，因此
\[
v_\ell(\kappa_3-1)=v_\ell(n).
\]
kappa_3的幂生成全部奇素数处的主单位核。

二进处，p-2为奇数，故
\[
v_2(\kappa_2-1)=v_2(n).
\]
若4|n，先用kappa_2调好全部二进位；随后用kappa_3的完整二进阶次幂修复奇素数处。该阶是2幂，不改变任何奇素数处的LTE起始深度。

若n=2模4，则p=1模4，v_2(p-3)=1。kappa_2=3模4补两类中的一类，kappa_3从1模4开始生成余下全部二进主单位。再同样用完整二进阶次幂修复奇素数处。于是主单位核全部生成。

接(6.3)，R单位模4n²满射。第5节把(7.2)精确送到(0,epsilon)。核心成为
\[
(\epsilon^p,(-\epsilon)^p,0^{p-1}).
\]
以(p-1)/2份epsilon、同样多份-epsilon和一个零组成零和p元组，即可触发统一零收尾。这完成全部p>=7。

## 9. 五平均14元：一个显式夹乘补齐最小容量

这里p=5、r=4、n=14。只需以下三个已实现变换：
\[
A=\begin{pmatrix}0&-11\\-1&0\end{pmatrix},\quad
S=\begin{pmatrix}-1&4\\0&1\end{pmatrix},\quad
J=J_{1,2}=\begin{pmatrix}-5&-10\\-4&5\end{pmatrix}.
\]
A²=11I、J²=65I，J仍是第3节的三原子返回。

令
\[
W=ASASJ=
\begin{pmatrix}-121&330\\0&65\end{pmatrix}.
\]
直接得到
\[
[S,W]=U(84/65).
\tag{9.1}
\]
这个上三角词也可以由有理方向确定：J送无穷远到5/4，S送到11/4，A送到4，S送到0，再由A送回无穷远。不是平均词搜索的输出。

由于121与65互素，W的倍率及其逆生成
\[
R_0=\mathbb Z[1/(5\cdot11\cdot13)].
\]
所以U(84R_0)、L(84R_0)及Gamma(7056,R_0)已可执行。

F_1的整数行列式5与7056互素，故可激活其逆，得到
\[
C_3=F_3F_1^{-1}=\begin{pmatrix}3&-4\\0&1\end{pmatrix}.
\]
虽然3整除旧控制层，下面的夹乘直接提供其逆：
\[
H=\frac13C_3JC_3
\ =\begin{pmatrix}1&-18\\-4&7\end{pmatrix},
\quad \det H=-65=\det J.
\tag{9.2}
\]
HJ^{-1}属于SL2(R_0)，且正向可执行。有限逆提升引理因而给出H^{-1}，再用
\[
JC_3H^{-1}=3C_3^{-1}
\]
取得C_3的真正正向射影逆。

共轭上根反演3。令R=Z[1/(3*5*11*13)]，则84R=28R，再次用深同余引理得到
\[
\boxed{\Gamma(784,R).}
\tag{9.3}
\]

### 9.1 不用有限轨道图的方向与尺度

取V=JA/125。其模14平移为-1/25，迹为2-196/125=2模4。因此一个V的CRT指数覆盖模16和模49的全部合法仿射方向。

以下三个实际R单位的余数为
\[
\begin{array}{c|cc}
&\bmod16&\bmod7\\ \hline
15&-1&1\\
10725&5&1\\
2145&1&3
\end{array}
\]
因为-1和5生成模16单位群，3生成模7单位群，这三者已覆盖模112的所有单位。它们分别为3*5、3*5²*11*13、3*5*11*13。

再令lambda=-121/65，有
\[
\lambda^2-1=\frac{10416}{4225},
\quad v_2(10416)=4,\quad v_7(10416)=1.
\]
故lambda²模16为1，并生成模49到模7的七阶单位核。于是R单位模784满射。

由(9.3)、第5节和同一个相反值终端，全部合法14元核心及全输入均归零。

## 10. 五平均最优阈值及验证边界

已有[十一元](../../examples/five_average_eleven_complete.md)、[十二元直接下降](../../tools/prime_arity_unified_weighted_core_theorem.md)第11节、[十三元](../../examples/five_average_thirteen_congruence_complete.md)和[全部n>=15](../../examples/five_average_three_p_threshold.md)的完整判据。本文补齐14元，故N(5)<=11；10元的既有G=1不可达例排除更低阈值，得到N(5)=11。

[核验程序](../../../../work/verify_three_p_minus_one_completion.py)只用精确矩阵、闭式计数和逐位模幂：

- p<250的50组一般参数及7874个完整模n单位代表；
- 200组局部方向、主单位和精确纤维接口；
- 78条原位置返回及重复闭路；
- 五平均夹乘、336个模784单位的显式指数，以及12组完整终端接口。

这些有限核验用于发现公式与实现错误；全部输入与全部p的量词由正文证明承担，没有搜索平均词或有限方向轨道。记录文件仅保存单位指数与核验统计，不是一般群词提取器。

核验入口：python work/run_verifications.py --id three-p-minus-one-completion。
