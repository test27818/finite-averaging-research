# 历史推导、失败路线与审计 · 第4分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [三进低余量：共同 CRT 终端与一次局部筛选](#doc-0cc981c94ada)
- [单位见证的补回阶段：Hilbert 基、精确容量与相邻重值障碍](#doc-28cd1944af6f)
- [三平均研究历史](#doc-ebec1ec81c79)
- [B_n 参数无关子问题模板编译器](#doc-ca9dbd7f83fe)
- [多危险素数三幂核的链间耦合与加权和转移](#doc-ce9ba26a79c4)
- [三平均的继续研究：正确级联、反向分拆编码与对数界的核心障碍](#doc-bc3da3b4a273)
- [三平均的进一步结构：五元精确递归、三进连分数与判定边界](#doc-ea211deb7404)
- [三平均的进一步推进：二字母逆树、严格高度枚举与对数界的剩余核心](#doc-959034b8a9d1)
- [三平均问题的新结构：三进支持集、提升机制与五元特殊性](#doc-ad82640623de)
- [所有偶维 B 核的统一减半定理](#doc-66e3f48a55d6)
- [三平均任意维数的全局视角：有限基维数究竟说明了什么](#doc-82e0619e54b5)
- [三平均的算术几何结构：射影投影、二次型与 adelic 高度](#doc-47a119cd7ff0)
- [外部 audit 的修订与证据登记](#doc-8ee0382bca27)
- [\(\mathcal B_{12}\) 二维核有限实验](#doc-ec8ac9b97d9e)
- [B12 六步局部下降与二次序导子塔](#doc-91e0ab966585)

---

<a id="doc-0cc981c94ada"></a>

## 原文导签：三进低余量：共同 CRT 终端与一次局部筛选

来源：`outputs/prime_arity/history/prime_arity_triadic_packed_carrier_completion.md` · [逐字节原样副本](../sources/outputs/prime_arity/history/prime_arity_triadic_packed_carrier_completion.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`triadic-packed-carrier-completion`, `nine-offset-residue-one`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-0cc981c94ada -->
# 三进低余量：共同 CRT 终端与一次局部筛选

日期：2026-09-15。p为平均元数，n为原位置数。

## 1. 完整结果与当前边界

**定理。** 设p>=5为素数，b属于{1,2}且p=b模3。则
\[
\boxed{n=3(p+b)}
\]
的全部非全等有理输入具有完整G=1充要判据。

这同时完成：
\[
n=3p+3,\quad p=1\pmod3;
\qquad
n=3p+6,\quad p=2\pmod3.
\]
两个分支使用同一载体打包、模3相位调整、两次状态相关返回和精确主同余纤维。没有平均词、有限群或有界高度轨道搜索。

**没有完成全部p平均。** 相反同余类、其余低余量以及p=2模3的3p+9仍须证明。全体素数的N(p)<=3p+10上界不变，目标仍是所有n>=2p+1。

本证明沿用已证原位置入口、Morris 2007定理6.1(2)、Serre强同余子群性质及深同余引理。新增的有理换基控制层和CRT选择在下文给出，不增加未说明的无限群假设。

第11节另完成n=3p+9、p=1模3的全输入证明，并得到这一素数类的N(p)<=3p+8。全体素数的最终上界仍是3p+10。

## 2. 同一组坐标和上根

以下先设p>3b；唯一较小情形p=5,b=2,n=21已经由旧大维数定理覆盖。

写
\[
j=(p-b)/3,\quad m=p+b,\quad r=3b,\quad n=3m.
\]
从既有无条件入口得到(A^(2p),B^p,C^r)，改写成
\[
A=u+v,\qquad B=u-2v,\qquad C=-pu/b.
\tag{2.1}
\]
它与(a,z)坐标的关系为a=u+v、z=u/b。由于b与n互素，在环R=Z[1/(pb)]上这是合法的可逆换基。取本原整数(u,v)代表后，合法性为
\[
\gcd(v,m)=1,\qquad 2u+v\ne0\pmod3.
\tag{2.2}
\]
这里m/b=2模3，而全局合法坐标是y=(m/b)u+v。b=1时m偶，所以v必奇；b=2时2在R中已可逆。

[载体打包逆](../sources/outputs/prime_arity/history/prime_arity_even_low_offsets_common_controller.md)取s=3b、打包数3，给保载体F_b的真正正向逆。F_b在(u,v)上作用为diag(1,b/p)。

两个标准迹零返回为
\[
A_{j,b}=\begin{pmatrix}0&-b^2\\-1&0\end{pmatrix},
\quad
B_{j-b,b}=\begin{pmatrix}3b&-4b^2\\2&-3b\end{pmatrix}
\]
（这里矩阵在(a,z)上，实际尺度1/p）。它们的原位置容量由p>=4b保证；p=1模3的最小素数7、p=2模3且p>3b的最小素数11都满足。

换到(u,v)并忽略非零共同尺度，两者为
\[
S_0=\begin{pmatrix}1&1\\0&-1\end{pmatrix},
\quad
S_1=\begin{pmatrix}1&-2\\0&-1\end{pmatrix},
\quad
S_0S_1=U(-3).
\]
它们及逆均正向可执行。F_b的双向共轭和gcd(p,b)=1给
\[
\boxed{U(3R),\qquad R=\mathbb Z[1/(pb)].}
\tag{2.3}
\]

## 3. 一个横向反射，只有一个取整修正

使用[四原子反射接口](../sources/outputs/prime_arity/history/prime_arity_low_offset_unified_frontier.md)：

先平均(A^(p-t-b),B^t,C^b)，得到p份D，保留r=3b份D作载体。再平均两个相同组成(A^x,B^y,C^e,D^w)的p组，最后平均其余p份。

若b=2，或者b=1且p不等于4模9，取
\[
k=b,\quad t=w=j-b,\quad
e=2j\bmod3,\quad
y=(2j+3b-e)/3,\quad x=p-y-e-w.
\tag{3.1}
\]
b=2时e属于{0,1,2}，均不超过b。b=1时，除p=4模9外e属于{0,1}。

在唯一取整例外b=1、p=4模9时，取
\[
k=2,\quad t=j-2,\quad w=(p-7)/6,\quad
e=1,\quad y=(p-w)/3,\quad x=p-y-e-w.
\tag{3.2}
\]
参数非负。直接代入可验证所有组长为p，且
\[
2x\le p+t+b,\quad2y\le p-t,\quad
2e\le2b,\quad2w\le p-3b.
\]
这些不等式由j>=2（b=1）或j>=3（b=2）成立，(3.2)从p=13起也成立。

令
\[
\alpha=p-3t-b=3k,\quad \beta=3bt-pb=-b^2-3bk,
\]
\[
Q_0=3bp\,y-p^2e+w\beta.
\]
原(a,z)矩阵为(beta,Q_0;-alpha,-beta)。换到(u,v)并除去共同因子b²，得到
\[
J=\begin{pmatrix}1&-3k/b\\c&-1\end{pmatrix},
\quad J^2=(1-3kc/b)I=:\lambda I.
\tag{3.3}
\]
实际四原子返回的尺度为b²/p²。

在(3.1)中
\[
c=\frac{m[b(2j+b)-pe]}{b^3};
\]
在(3.2)中c=-mj/2。于是
\[
c\ne0,\quad c=2\pmod3,\quad c\in mR,\quad
\lambda=1\pmod{3m}.
\tag{3.4}
\]
非零性也可由p不整除b(2j+b)直接推出。因此J的射影逆正向可执行，且它保持合法域。

## 4. 两条横向根足以产生明确的控制层

这里不强求第二条根已经位于原坐标的下三角方向。

令P=(e_1,Je_1)，即
\[
P=\begin{pmatrix}1&1\\0&c\end{pmatrix}.
\]
则对任意t，
\[
P^{-1}U(t)P=U(ct),\qquad
P^{-1}J U(t)J^{-1}P=L(-ct/\det J).
\tag{4.1}
\]
选择t=3(\det J)x时，所需上根仍属于(2.3)，第二式成为L(-3cx)。第一式给U(3cR)。

取正整数g使cR=gR，即将c分子的p、b单位因子去掉。第(4.1)式表明，在P基下已有U(3gR)、L(3gR)。深同余引理给Gamma(9g²,R)。

换回原基时，P不必可执行，也不必整幺模，但必须清楚计算格的指数。因为c/g为R单位，取
\[
\boxed{M=9g^3}
\tag{4.2}
\]
便有
\[
P^{-1}\Gamma(M,R)P\subseteq\Gamma(9g^2,R).
\]
理由是gP^{-1}及P的条目都在R；共轭后误差仍含9g²。故
\[
\boxed{\Gamma(M,R)\text{ 正向可执行}.}
\tag{4.3}
\]

这里m整除g，3不整除g，gcd(M,pb)=1，因此n=3m整除M。辅助素数可以留在M中，下面的CRT返回直接处理它们。

注意det J不一定是R单位。式(4.1)中乘det J的目的就是清去其分母，不能省略。用于相位调整时，J在模M处仍可逆，因为lambda=1-(3k/b)c与3g互素。

## 5. 模3相位调整与奇数代表

把当前(u,v)取整数本原代表。合法性(2.2)保证：

- 若v=0模3，执行J。由c=2模3，输出满足u+v=0模3且v不为0。
- 若v不为0、u+v不为0模3，则(2.2)迫使u=0模3。执行S_0后，同样满足u+v=0模3。
- 已满足时不操作。

所以至多一次已知反射即可进入
\[
u+v=0\pmod3,\qquad3\nmid v.
\tag{5.1}
\]
这是对全部六个合法非零模3列的直接论证，没有有限群轨道搜索。

b=2时，若v偶，执行保载体逆(u,v)->(u,pv/2)，并取整数本原代表。每次v的二进赋值严格减少；公因子至多来自奇数p，不影响这一下降。它模3只乘单位，不破坏(5.1)。因此可再令v奇。b=1时v由合法性原本就奇。

最后保留
\[
\gcd(u,v)=1,\quad v\text{ 奇},\quad3\nmid v,\quad
\gcd(v,m)=1,\quad u+v=0\pmod3.
\tag{5.2}
\]

## 6. 两类真实数字返回

U(3R)允许对u作u->u+3kv。取
\[
a=(u+v)/3\pmod v.
\tag{6.1}
\]
同一剩余类也等于(u-2v)/3模v。

保留旧A、每个重复组不取C、B计数为q时，若
\[
\lceil3b/2\rceil\le q\le(p-1)/2,
\]
先将u变成3a-v，再执行A_{q,0}。取掉共同尺度3/p后得到
\[
(u',v')=(-ba,\ ma-qv).
\tag{6.2}
\]

保留旧B时，取0<=t<=floor((p-3b)/2)，令q=t-p<0，先将u变成3a+2v，再执行B_{t,0}。取掉同一个共同尺度3/p后，仍得到完全相同的(6.2)。

因此可用数字集合为
\[
\mathcal D=
[\lceil3b/2\rceil,(p-1)/2]
\ \cup\
\{-p,-p+1,\ldots,\lfloor(p-3b)/2\rfloor-p\}.
\tag{6.3}
\]
这里两类返回都是实际三个p组及保留载体，位置容量完整。除掉3只是选取分析代表；下面单独保证新的本原状态合法。

## 7. 第一返回：把v变成整个控制层的单位

先用负数字q=-p，即B_{0,0}。选a满足(6.1)，并且a=-v模3。对每个ell|M：

- ell|m时，ma+pv=pv非零模ell；
- ell|v时，ell不整除m，且(6.1)使a非零，故ma+pv非零；
- 其余ell不等于3时，可指定a=(1-pv)/m模ell。

再令p不整除a；如果p|v，此条件已经由(6.1)保证，否则另用CRT指定。b=2时再取a偶；这与其余条件相容，因为M和v均为奇数。

输出
\[
(u_1,v_1)=(-ba,\ ma+pv)
\]
满足
\[
\gcd(u_1,v_1)=1,\quad \gcd(v_1,M)=1,\quad
u_1+v_1=p(a+v)=0\pmod3.
\tag{7.1}
\]
其全局合法坐标为(m/b)u_1+v_1=pv，仍在模3为单位；模m也保留见证。b=2的偶数a保证v_1奇，清除了可能的共同因子2。

## 8. 第二返回：少数单位倍足以指定终端尺度

取v_1逆元模m的正平衡绝对代表d，记d v_1=eta模m，其中eta起初为±1。

b=1时，1<=d<=(p-1)/2。b=2时，先作两个可能的调整：
- 若d=1，以2替代，eta乘2；
- 若d=(m-1)/2，以2替代，eta乘-4，因为-4d=2模m。

因此b=2时可以保证2<=d<=(p-1)/2，eta仍是R单位。

如果d在正数字范围且3不整除d，就取q=d；否则取q=d-m，使用负数字。两者模m相同。它们不可能同时被3整除，因为3不整除m。b=1的缺失数字d=1由q=-p补上；b=2的缺失数字d=2同样由q=-p补上。b=2时最大正数字(p-1)/2不被3整除，所以它没有负数字副本也不造成缺口。

故总能选择
\[
q\in\mathcal D,\quad3\nmid q,\quad qv_1=\eta\pmod m.
\]
单位tau=-p/b在模m下为1，在模3下为-1。因此从
\[
\epsilon=-\eta\quad\text{或}\quad-\eta\tau
\]
中选一项，即得到
\[
\boxed{qv_1+\epsilon=0\pmod{3m},\quad\epsilon\in R^\times.}
\tag{8.1}
\]
不要求整个R单位群模M满射。

置K=M/m，并选整数E=epsilon模M。由(8.1)，qv_1+E被m整除。CRT给a满足
\[
a=(u_1+v_1)/3\pmod{v_1},\qquad
a=(qv_1+E)/m\pmod K.
\tag{8.2}
\]
两个模数互素。第二式自动给a=0模3。再对尚未被这两个模数约束的ell|q指定a不为0，即可保证gcd(a,q)=1；若ell已整除某模数，(8.2)已强制a非零。可能例外的ell=p并不整除K，仍可选择。

b=2时还指定a=q+1模2，保证ma-qv_1为奇数。q偶时这同时使a奇，和gcd(a,q)=1相容；q奇时也不妨碍其他条件。

再执行对应(6.2)，得到整数本原列
\[
(u_2,v_2)=(-ba,\ ma-qv_1),\qquad
u_2=0\pmod3,\quad v_2=\epsilon\pmod M.
\tag{8.3}
\]
全局合法性由模m的单位条件及(m/b)u_2+v_2=-qv_1不被3整除保证。

## 9. 精确终端与全输入

因为u_2被3整除、v_2为模M单位，以U(3k)可使u_3=u_2+3kv_2=0模M。现在(u_3,v_2)为整数本原列，与(0,epsilon)模M相同。

取alpha u_3+beta v_2=1，并调整使alpha=0模M。则
\[
P_{\rm final}=
\begin{pmatrix}
v_2/\epsilon&-u_3/\epsilon\\
\epsilon\alpha&\epsilon\beta
\end{pmatrix}
\in\Gamma(M,R)
\]
将列精确送到(0,epsilon)。式(4.3)给原位置实现。

终端为(epsilon^(2p),(-2epsilon)^p,0^(3b))。取floor(p/3)份-2epsilon、其两倍份epsilon，再以p模3份零补满p个位置；已有3b个零，容量成立。统一零触发尾部结束。

整个过程从既有无条件入口出发，所有准备和数字返回都给出原位置索引规则，所以这是全输入定理，不是仅有合法核心或有限模可达。

## 10. 验证范围与后续

[精确核验程序](../sources/work/verify_triadic_packed_carrier_completion.py)检查p<500的92组共同反射及控制层、66条原位置打包/反射闭路，以及828组两次CRT和精确终端矩阵。p<=31的两次数字返回也独立逐位置重放。六种数字分支均触及，包括b=2时epsilon含分母2的情形。

一般量词由正文的计数、换基清分母和CRT相容性承担。没有搜索平均词，没有枚举模群，也没有把有限高度样本外推为一般可达性。

新接口可概括为：已有上根不必是全部U(R)，U(3R)也够；先修复模3相位，再用两类数字代表和单位tau安排终端。辅助素数直接留在控制层，由第一次CRT返回统一处理。

相反同余类的n=3p+3、3p+6满足v_3(n)>=2，而本定理两族恰有v_3(n)=1。n=3p+9的打包参数b=3不满足本段b为模3单位的前提，不能自动套用；第11节用另一条短筛选证明其p=1模3分支，p=2模3仍未解决。

核验入口：python work/run_verifications.py --id triadic-packed-carrier-completion。

## 11. 同时补齐3p+9的p=1模3分支

**补充定理。** 若p=1模3为素数，则n=3p+9的完整G=1判据成立。p=7时沿用既有全部n>=15的定理；以下设p>=13。

置j=(p-1)/3。旧四返回参数区间在r=9时仍含
\[
j-1,j\quad\text{两条A},\qquad
j-4,j-3\quad\text{两条B}.
\]
其四个平方标量恰为
\[
d=p+12,\quad e=3-2p,\quad \mu=3-2p,\quad \nu=4p+21.
\]
于是已有真实根U(9n²R_0)、L(9n²R_0)，以及
\[
\Gamma(81n^4,R_0),\qquad
R_0=\mathbb Z[1/|de\mu\nu|].
\tag{11.1}
\]
r的素因子只有3，且3|n，所以没有n以外的辅助素数需要处理。安全整数返回的逆可以直接由(11.1)激活。

### 11.1 三进返回用同一个短筛选

取保留A的返回A_{t,2}，其数字q=3t+2。所需容量仅为
\[
3\le t\le(p-1)/2.
\]
同时要求
\[
t\text{ 奇},\qquad t\ne1\pmod3,\qquad
3t+2\ne0\pmod\ell\quad(\ell\mid n,\ \ell\ge5).
\tag{11.2}
\]
这些条件对每个ell|n只禁止一个t的余数类。

设d_0=omega(n)、rho=phi(rad n)/rad n。对于d_0<=4，已有初等短区间引理保证长度2^{d_0}足够。n同时被2、3整除：d_0=2时p>=13的参数区间长至少4；d_0=3时p>=23的区间长至少9，小参数p=19直接取t=5；d_0=4时rad n>=210，故p>=67，区间更长。

若d_0>=5，则phi(rad n)>=480，且由增加素因子的归纳有
\[
\varphi(\operatorname{rad}n)>6\cdot2^{d_0}+18.
\]
参数区间长度L=(p-5)/2=(n-24)/6，因此
\[
L\rho\ge \varphi(\operatorname{rad}n)/6-4>2^{d_0}-1.
\]
容斥遂保证(11.2)有解。算法只标记每个素数的一条禁止等差数列，不搜索平均词。

这个A返回在(z,y)坐标中为
\[
p^{-1}\begin{pmatrix}p&-1\\nt&-(3t+2)\end{pmatrix}.
\]
n=3(p+3)恰有一层3，迹半数归一化后的参数c满足c/3=-t模3。条件t!=1保证c!=6模9，所以它在全部3幂上有完整射影循环。

先调好三进方向，再用旧BA返回的完整三进阶保护它，以CRT同时处理其他素数；二进迹仍由相邻B选择。此部分直接复用已证上半带局部循环论证。

### 11.2 单位尺度及精确终端

对p>=19，允许的安全数字区间是
\[
9\le q\le(3p+5)/2.
\]
令k=n/3=p+3。已有“模k平衡代表，再在k-b、k+b、b中取单位”的论证全部成立，因为
\[
k/2-2\ge9.
\]
数字k+1同时提供模n到模k单位核的非平凡元素。故安全A返回的行列式反演给出全部模n单位提升。

唯一p=13时n=48，初始d=25提供单位5；激活保载体F_1的逆后，13也是单位。模48的5、13、-1生成全部16个单位：5阶为4，13不在其循环群而13²=5²，二者生成全部1模4的8个单位，-1补另一半。因此无需新的轨道证书。

d、e、mu、nu的相邻比按LTE生成模81n^4到模n的全部主单位核。最终用Gamma(81n^4,R)的精确纤维送至z=0，再由p个零和位置完成收尾。一般全输入入口由已有上半带归约保证，补充定理得证。

[核验](../sources/work/verify_nine_offset_residue_one.py)检查p<500的44组四返回、10条原位置三进返回、9592个完整单位代表和132组方向尺度输送。通用容量、筛选及提升量词由本节承担。

结合此前所有3p+8及全部n>=3p+10均已完成，立即有
\[
\boxed{p=1\pmod3\text{ 为素数}\quad\Longrightarrow\quad N(p)\le3p+8.}
\]
这不是全体素数的新上界；p=2模3的3p+9仍未完成。

核验入口：python work/run_verifications.py --id nine-offset-residue-one。

## 12. 相反同余类可用的状态相关三进消去

下面记录一个已验证的条件恒等式，用于剩余高三进分支；它不是完整终止证明。

仍令r=3b、n=3(p+b)，但暂不要求p=b模3。若本原核心已经满足
\[
(a,z)=(3u,v),\qquad \gcd(3u,v)=1,
\]
则保留A、重复组不取C的A_{t,0}给
\[
\frac1p
\begin{pmatrix}p-3t&3bt\\-1&0\end{pmatrix}
\binom{3u}{v}
=
\frac3p\binom{(p-3t)u+btv}{-u}.
\tag{12.1}
\]
容量为ceil(3b/2)<=t<=floor(p/2)。

若gcd(t,n)=1，输出的本原合法性自动保持。因为新未约分的y坐标为t(bv-3u)，而
\[
p(bv-3u)-b(3u+pv)=-nu.
\]
b、p在模n下都是单位，原y=3u+pv为单位，故新y仍是单位；两输出坐标的共同因子gcd(u,bt)也与n互素。

这说明危险素数3可以通过“先令a含一个3，再真实平均，最后取本原代表”被消去，而不必把3加入全局局部化环。尚缺的是：在剩余相反同余类中，如何始终进入这个输入格，并让这种消去阶段递归闭合。不能把(12.1)单独写成全部高三进情形的证明。

<!-- END SOURCE doc-0cc981c94ada -->

---

<a id="doc-28cd1944af6f"></a>

## 原文导签：单位见证的补回阶段：Hilbert 基、精确容量与相邻重值障碍

来源：`outputs/prime_arity/history/prime_arity_unit_witness_replenishment.md` · [逐字节原样副本](../sources/outputs/prime_arity/history/prime_arity_unit_witness_replenishment.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`unit-witness-replenishment`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-28cd1944af6f -->
# 单位见证的补回阶段：Hilbert 基、精确容量与相邻重值障碍

日期：2026-09-14。接续[来源关系、动态见证与整数返回阶段](../sources/outputs/prime_arity/structure/prime_arity_provenance_dynamic_and_integer_stages.md)。

最新补齐：[全碰撞单位分支统一补回](../sources/outputs/prime_arity/structure/prime_arity_complete_unit_collision_recovery.md)已经处理本页未覆盖的全部局部参数；最坏在规定载体步骤之后需要三次平均。它没有宣称任意多值输出都可再次套用该入口。

后续：[欧几里得见证转移](../sources/outputs/prime_arity/history/prime_arity_euclidean_witness_transfer.md)已统一推进任意h的d>h和一大片d<h分支，并接续正余项的实际输出，实现旧高值消去及最大值下降。本页所列h>=4边界因而已经进一步缩小，仍未证明完整递归闭包。

前文在核心出口的全碰撞分支中证明了 $A-M=\pm1$。本页完整处理一个具体后续问题：消耗一份旧载体后，能否再用一次整数平均，把这个单位差重新补成两个 $p$ 重值？

得到的是一个有闭式充要条件的两原子阶段，以及补齐缺额 $d=1$ 和 $(h,d)=(3,2)$ 的三原子阶段。它们可以实际更换见证位置，并在原整数格内降能；但阶段输出不一定又落在同一个入口类。另给出任意元数的统一反例，排除“存在相邻整数重值对”作为单步闭合不变量。未降低阈值，未证明递归终止。

## 1. 全碰撞分支的完整整数参数

设 $p\ge5$ 为素数，$n=3p+r$、$1\le r<p$。考虑前文单载体出口
\[
(A^{h-1},B^{p-h},C)\longmapsto M^p,\qquad M=A-1,
\tag{1}
\]
其中 $1\le h\le p-1$。整体取负可处理 $A-M=-1$，故这里只写正单位差。

设全部不使用剩余 $C$ 的储备候选都碰撞到 $A$。前文整数格证明给出
\[
B=A+s,\qquad s\in\mathbb Z_{\ge1},\qquad hs<p.
\tag{2}
\]
写
\[
D_0=p(s+1)-hs,\qquad T=3D_0+s=3p(s+1)-(3h-1)s.
\]
来源式与核心零和式迫使
\[
n\mid T,\quad \nu=T/n,\quad
A=D_0-p\nu,\quad B=A+s,\quad C=-p\nu.
\tag{3}
\]
由于 $n>3p$，有 $1\le\nu\le s$，从而 $A\ge p-hs\ge1$。又
\[
3A+s=r\nu
\tag{4}
\]
排除 $r=1$，故实际分支自动满足 $r\ge2$。

反过来，给定 $p,h,s$ 满足 (2)，若 $T$ 有约数 $n$ 落在 $(3p,4p)$，由 (3) 定义的核心 $(A^{2p},B^p,C^r)$ 确实零和且
\[
G=\gcd(s,D_0)=\gcd(s,p)=1.
\]
(1) 是指定的单载体出口。储备候选选 $k$ 份 $A$、$l$ 份 $B$，其余用 $M$ 补足，其中
\[
1\le l\le h,\qquad k\le p-h+1,\qquad k+l\le p.
\]
相对 $M$ 的实际和为 $k+(s+1)l$，严格介于 $0$ 与 $2p$，因为最大不超过 $p+hs<2p$。所以凡为整数平均者，实际和只能是 $p$，均值必为 $A$。这证明这些公式刻画实际全碰撞分支，而非样本拟合。

若 $A=1$，第一步已经产生 $p$ 个零，直接收尾。

## 2. 消耗一份载体，留下一个单位见证

在 (1) 之后，四类重数为
\[
A^{2p-h+1},\quad B^h,\quad C^{r-1},\quad M^p.
\]
执行
\[
(A^{p-1-hs},M^{hs},C)\longmapsto P^p,\qquad P=A-s-1.
\tag{5}
\]
所有计数非负，均值公式直接由 $A-C=D_0$ 验证。输出为
\[
A^{p+\alpha},\quad B^h,\quad M^d,\quad P^p,\quad C^{r-2},
\qquad
\alpha=h(s-1)+2,\quad d=p-hs\ge1.
\tag{6}
\]
旧 $A$ 仍至少 $p$ 重，旧 $M$ 至少剩一份。因为 $A-M=1$，全程合法；不必为 $n$ 的每个素因子分别保留位置。若 $P=0$，已经终端。

现在的问题完全具体：在 (6) 上，不再使用 $C$，能否一次平均产生 $M$，同时留下至少 $p$ 份 $A$？

## 3. 所有补回关系的 Hilbert 基

相对目标值 $M=A-1$，参与值的偏差恰为
\[
A-M=1,\quad B-M=s+1,\quad P-M=-s,\quad M-M=0.
\]
设选择数为 $k,l,u,m$，则所求平均的充要条件是
\[
k+(s+1)l=su,\qquad k+l+u+m=p,
\tag{7}
\]
\[
0\le k\le\alpha,\quad 0\le l\le h,\quad
0\le m\le d,\quad u\ge0.
\tag{8}
\]
$u\le p$ 由组长自动保证。

这是二维非负整数锥。令 $z=u-l$，则
\[
k=sz-l,\qquad u=z+l,\qquad 0\le l\le sz.
\]
其全部不可分解的非零整数关系为
\[
\boxed{(k,l,u)=(s-j,j,j+1),\qquad j=0,\ldots,s.}
\tag{9}
\]
证明：非零关系必有 $z\ge1$；将 $l$ 写成 $z$ 个介于 $0$ 与 $s$ 的整数之和，就把该关系分成 $z$ 个 (9)。而 (9) 的 $z=1$，不能再拆成两个非零关系。这正是该整数锥的 Hilbert 基。

每个基本零和包的长度为 $s+1+j$。真正的限制是各类型副本的上限，以及可用于补足的 $d$ 个旧 $M$；只知道存在整数零和关系，或只使用无容量的半群生成结论，都不足以执行操作。

写非零偏差位置总数 $L=k+l+u=(s+1)z+l$，则 (8) 化为
\[
hs\le L\le p,\quad 0\le l\le h,\quad
0\le sz-l\le h(s-1)+2.
\tag{10}
\]

## 4. 补回阶段的精确充要条件

**定理。** 对所有正整数 $h,s$ 和整数 $p>hs$，(7)、(8) 有非恒等解，当且仅当
\[
\boxed{
2h\ge s+1
\quad\text{或}\quad
p-hs\ge h+\max(0,h-2).
}
\tag{11}
\]
这里 $p$ 不必为素数。素性仅用于第 1 节的核心入口和合法性。

### 4.1 $2h<s+1$

若 $z\le h-1$，则
\[
L\le(s+1)(h-1)+h=hs+2h-(s+1)<hs.
\]
所以 $z\ge h$。由 $sz-l\le h(s-1)+2$ 得 $l\ge h-2$，故
\[
L\ge hs+h+\max(0,h-2).
\]
这给出 (11) 第二项的必要性。反之直接取
\[
z=h,\quad l=\max(0,h-2),\quad
k=hs-l,\quad u=h+l,\quad m=p-L.
\]
所有容量条件均成立。因此必要条件也是充分条件。

### 4.2 $2h\ge s+1$

除 $(h,s)=(1,1)$ 外，可以直接安排 $L=hs$，即恰好用尽 $d=p-hs$ 个旧 $M$。条件等价于
\[
l\equiv-h\pmod{s+1},\qquad
k=\frac{hs^2-(2s+1)l}{s+1},
\tag{12}
\]
\[
\max\left(0,\left\lceil\frac{h-2(s+1)}{2s+1}\right\rceil\right)
\le l\le
\min\left(h,\left\lfloor\frac{hs^2}{2s+1}\right\rfloor\right).
\tag{13}
\]

当 $s\ge3$，上界就是 $h$。若 $h\le2(s+1)$，下界为 $0$；$-h$ 的最小非负余数不超过 $h$：$h<s+1$ 时使用 $2h\ge s+1$，否则余数本来就小于 $s+1\le h$。若 $h>2(s+1)$，记下界为 $b$，则 $b\le(h-2)/(2s+1)$，从而 $b+s\le h$；连续整数 $b,\ldots,b+s$ 覆盖全部模 $s+1$ 余数，故仍可选 $l$。

当 $s=2$，有 $h\ge2$。区间为
\[
\max(0,\lceil(h-6)/5\rceil)\le l\le\lfloor4h/5\rfloor.
\]
$h=2$ 取 $l=1$；$h=3,4,5,6$ 分别取 $l=0,2,1,0$。$h\ge7$ 时该区间至少含三个连续整数，故能满足模 $3$ 条件。

当 $s=1,h\ge2$，按 $h\bmod3$ 分别取
\[
\begin{array}{c|ccc}
h & k&l&u\\\hline
3q &0&q&2q\\
3q+1\ (q\ge1)&2&q-1&2q\\
3q+2&1&q&2q+1
\end{array}
\]
即可使 $L=h$。最后 $(h,s)=(1,1)$ 取 $k=u=1,l=0,m=p-2$。定理得证。

### 4.3 原位置执行与见证更换

选择满足 (7)、(8) 的组
\[
(A^k,B^l,P^u,M^m)\longmapsto M^p.
\tag{14}
\]
均值确为 $M$，至少留下 $p$ 份 $A$。即使旧 $M$ 全被选走，新的平均组也立即提供 $p$ 份 $M$；因此单位同余见证可以转移到新位置，操作后仍有两个相邻整数重值。

(5)、(14) 均为非恒等整数平均，平方能量严格下降。计数可在 $O(h)$ 时间确定：对每个 $l\in[0,h]$ 检查
\[
\max\left(0,\left\lceil l/s\right\rceil,
\left\lceil(hs-l)/(s+1)\right\rceil\right)
\le z\le
\min\left(\left\lfloor(\alpha+l)/s\right\rfloor,
\left\lfloor(p-l)/(s+1)\right\rfloor\right).
\]
无需枚举原位置子集或平均词。

## 5. 容量不足只出现在狭窄边界

(11) 失败意味着
\[
h\ge2,\quad s\ge2h,\quad 1\le d=p-hs<2h-2.
\tag{15}
\]
尤其
\[
2h^2\le hs<p,\qquad h<\sqrt{p/2}.
\]
本分支的困难被压缩到 $hs$ 接近 $p$ 的小缺额区域。$p=3,5,7$ 不可能满足 (15)。这只解释本补回分支在小元数处为何没有容量障碍，不解释全部维数阈值，也不是一般平均问题的小元数归纳证明。

有时不必先作 (5)。若存在 $c_0\in[1,r-1]$，使
\[
b_0=-hc_0\pmod p,\quad b_0\le h,\quad
0\le a_0=p-b_0-c_0\le p-h+1,
\]
则在 (1) 后直接平均 $(A^{a_0},B^{b_0},C^{c_0})$，本来就保留至少 $p$ 份 $A$ 和全部 $p$ 份 $M$，且来源式保证均值为整数。下面的核心实例同时逃过这种单步保存。

### 5.1 缺额 $d=1$：三个原子统一补齐

现在允许在 (5) 后多用一次平均。对于 (15) 中的 $d=1$，有 $p=hs+1$。令
\[
w=s-\nu,\qquad A=pw+1,\qquad M=A-1.
\]
非终端时 $w\ge1$；由 (4) 及 $\nu\le s$，
\[
r\ge(3p+s+3)/s>3h+1.
\]
因此下列操作有足够的载体副本，且 $p-h-3\ge0$。

从 (1) 的后继开始，令 $P=A-s-1$、$Q=A-(p-1)$，依次实施
\[
\begin{array}{c|l|l}
 &\text{选组}&\text{均值}\\\hline
1&(M^{p-1},C)&P\\
2&(A,P^{p-h},C^{h-1})&Q\\
3&(A^{p-h-3},B^h,Q^2,M)&M
\end{array}
\tag{15a}
\]
第二组的相对 $A$ 偏差总量为
\[
-(p-h)(s+1)-(h-1)(ps+1)=-p(p-1),
\]
所以均值为 $Q$。第三组相对 $A$ 的偏差和为
\[
hs-2(p-1)-1=-p,
\]
所以均值为 $M=A-1$。

每一步的组长均为 $p$。前两步始终保留旧 $M$ 的最后一份和旧 $A$；第三步把该见证复制到新平均组。最终重数为
\[
A^{p+3},\quad M^p,\quad P^h,\quad Q^{p-2},\quad C^{r-h-1}.
\]
故相邻重值对已经恢复，且三次均为安全非恒等整数平均。任一中间均值若为零，直接改接零触发收尾。

因此，两原子菜单在 $d=1$ 的失败已经由一个对任意素数适用的三原子阶段补齐，不必逐个 $p$ 搜索。

### 5.2 $(h,d)=(3,2)$：另一个三原子阶段

此时 $p=3s+2$，容量不足分支有 $s\ge7$。写 $A=pw+2$。若 $w=0$，(4) 要求 $(r-1)s=6$，不可能；故 $w\ge1$，进而 $r\ge11$。

令 $P=A-s-1$、$Q=A-2s+1$，从 (1) 的后继依次实施
\[
\begin{array}{c|l|l}
 &\text{选组}&\text{均值}\\\hline
1&(A,M^{p-2},C)&P\\
2&(A^5,P^{p-6},C)&Q\\
3&(A^{p-9},B^3,P^2,Q^2,M^2)&M
\end{array}
\tag{15b}
\]
第二步相对 $A$ 的损失为
\[
(p-6)(s+1)+(ps+2)=p(2s-1).
\]
第三步相对 $A$ 的损失为
\[
-3s+2(s+1)+2(2s-1)+2=3s+2=p.
\]
所以均值公式成立。三步中 $A$ 的数量依次为 $2p-3,2p-8,p+1$；旧 $M$ 的两份在最后一步复制为 $p$ 份。最终状态为
\[
A^{p+1},\quad M^p,\quad P^4,\quad Q^{p-2},\quad C^{r-3}.
\]
这再次给出安全、整数、严格降能的单位见证补回。

$h=2$ 的所有容量不足情形都只有 $d=1$。$h=3$ 时由 (15) 有 $d\le3$，而 $p=3s+d$ 为素数排除 $d=3$。因此本页把所有 $h=2,3$ 的不足分支统一补齐。当时余下的 $h\ge4,d\ge2$ 算术边界，现已由[统一补回定理](../sources/outputs/prime_arity/structure/prime_arity_complete_unit_collision_recovery.md)处理；输出状态的递归闭包仍未证明。

## 6. 真正来自核心的单步相邻重值障碍

取 $p=29,r=8,n=95,h=2,s=14$。这里 $hs=28=p-1$。合法核心
\[
(30^{58},44^{29},(-377)^8)
\]
实施指定第一步
\[
(30,44^{27},-377)\longmapsto29^{29}
\]
得到
\[
\boxed{Y=(30^{57},44^2,(-377)^7,29^{29}).}
\tag{16}
\]
它已有相邻重值 $29,30$，但不存在一次非恒等整数平均，使输出仍有某个相邻整数重值对；也不存在直接造零的 $29$ 元组。

**完整证明。** 设一组选取 $a,b,c,m$ 份 $30,44,-377,29$，则
\[
a+b+c+m=29,\quad 0\le b\le2,\quad0\le c\le7,
\]
组和为
\[
\Sigma=870+14b-m-407c.
\tag{17}
\]

- 保留原重值对要求 $m=0,a\le28$。整数性为 $14b-c=0\bmod29$；容量内只有 $b=c=0$，但此时 $a=29$，超出保留容量。
- 新相邻对只能以当前重值 $29$ 或 $30$ 为一端。新均值 $31$ 要求 $14b-m-407c=29$，而左边至多 $28$。新均值 $29$ 要求左边为 $-29$；只能是 $c=b=0,m=29$，即恒等平均。
- 保留旧 $29$ 时必须 $m=0$。新均值 $30$ 要求 $14b-407c=0$，只有纯 $30$ 恒等组；新均值 $28$ 要求 $14b-407c=-58$，同样无解。
- 若 $c\le2$，(17) 严格为正；最紧 $c=2$ 时由 $m\le27-b$ 得 $\Sigma\ge29+15b$。若 $c\ge3$，$\Sigma\le870+28-3\cdot407<0$。故没有零和组。

此证明检查全部可能原位置类型，不依赖搜索失败。执行 (5) 则为 $(29^{28},-377)\mapsto15^{29}$，输出
\[
(30^{57},44^2,29,15^{29},(-377)^6).
\tag{18}
\]
此时 $29$ 从重值降为单点见证。排除 $15$ 块后，其他值相对 $30$ 的模 $29$ 例外恰为 $14^2,(-1)^7$。它们没有非空零和子序列，所以该外部池只有恒等整数平均。不能固定保护整个新 $15$ 块，再假设外部池总能继续。

第 5.1 节已实际越过这个单步障碍。该具体核心甚至有四次平均的直接造零前缀：
\[
\begin{array}{c|l|l}
1&(30,44^{27},-377)&29\\
2&(29^{28},-377)&15\\
3&(30,15^{27},-377)&2\\
4&(30^9,44,29,-377,2^{17})&0
\end{array}
\]
最后一组的和为 $270+44+29-377+34=0$。各步副本足够，逐步合法。故单步不变量确实失败，但这个输入并没有陷入不可达状态。

## 7. 任意元数都有这种过强不变量的障碍

**命题。** 对任意平均元数 $k\ge2$、任意 $n>3k$ 且 $k\nmid n$，存在本原整数零和、$G=1$ 的状态，具有相邻的两个 $k$ 重值，却没有一次非恒等整数 $k$ 平均保留或重新建立任何相邻重值对，也没有直接零和 $k$ 元组。

**证明。** 取
\[
F=n-2k-1\ge k,\quad Q=6k+1,\quad C=-3k-FQ,
\qquad X=(1^k,2^k,Q^F,C).
\tag{19}
\]
零和及 $G=1$ 显然。任何含 $C$ 的 $k$ 组，其和不超过
\[
C+(k-1)Q=-3k-(F-k+1)Q<0;
\]
不含 $C$ 的组全为正，所以没有零和组。

若保留原 $1,2$ 两个重值，只能从 $Q,C$ 中选组。纯 $Q$ 组恒等；混合组只能是一份 $C$、$k-1$ 份 $Q$，组和模 $k$ 为 $-n\ne0$，故不能是整数平均。

任何新相邻重值对，必以原重值 $1,2,Q$ 之一为一端，因为一次平均只增加一个实际值的重数。含 $C$ 的组均值为负；不含 $C$ 时，新均值 $1,2$ 只能来自相应恒等组，均值 $3$ 不可能，因为 $Q>3k$，而只用 $1,2$ 均值不超过 $2$。均值 $Q+1$ 超过最大值；其余可能产生 $Q-1$ 的非恒等组均值至多
\[
\frac{(k-1)Q+2}{k}<Q-1.
\]
所有可能的新邻居 $0,1,2,3,Q-1,Q+1$ 均被排除，得证。

此障碍甚至存在于已知可解的大维数区间。应当放弃的是“单步始终保有相邻重值对”这一过强要求，不能据此推断平均问题失败。本页两原子补回阶段允许中途只剩一个单位单点见证，正是对这个区别的实际运用。

## 8. 已证明的范围与未闭合的接口

已得到：全碰撞入口的完整参数化；显式 Hilbert 基；两原子补回的精确容量充要条件；缺额 $1$ 和 $(h,d)=(3,2)$ 的三原子补齐；原位置上的见证重新复制；以及单步相邻重值障碍。

还没有得到：阶段输出仍属于同一个入口类。补回后通常留下 $P$ 的若干副本、改变 $B$ 的数量，并可能只给旧 $A$ 留下 $p$ 份。因此即使 (11) 本次成立，也不能不检查容量就原样重复。

下一项加强应允许重值之间的差改变，只把同余见证作为可更新的少量位置；或者规定真正返回整数格的完整阶段。要求每一步都重新得到相邻重值对已经被第 7 节排除。没有证明所有较弱策略失败，也没有把其存在性当作假设来宣称终止。

## 9. 核验与范围

核验入口：[verify_unit_witness_replenishment.py](../sources/work/verify_unit_witness_replenishment.py)。

程序先用两个线性方程消去变量，再检查计数容量。241187 个整数容量系统中，238655 个可补回，2532 个不可补回；全部与 (11) 一致。这里包含非素数 $p$，以核对容量定理本身。

对 $5\le p\le101$ 的全部素数，以及满足本页参数和约数条件的核心，排除第一步或 (5) 已造零的 68 例后，重放 1051 条两原子补回，另有 14 个该菜单不足的入口。其中 8 个由 (15a)、3 个由 (15b)、3 个由第 5 节的直接保存路径处理，均已逐位置核验。该有限范围内本特定入口分支没有未覆盖项；这不证明所有更大 $p$ 或后续迭代已覆盖。

另独立消元核对 $p=29,n=95$ 的全部相邻重值目标、保存旧重值对的全部配比及零和目标，重放其四步造零，并核对 49 个统一障碍实例，包含合数元数及 $n>4k$ 的位置数。一般量词由正文证明承担，不由有限计数替代。

<!-- END SOURCE doc-28cd1944af6f -->

---

<a id="doc-ebec1ec81c79"></a>

## 原文导签：三平均研究历史

来源：`outputs/triple_average/history/README.md` · [逐字节原样副本](../sources/outputs/triple_average/history/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ebec1ec81c79 -->
# 三平均研究历史

含非分裂轨道、仿射交换子、周期刚性、迹零返回、Hecke等；按文件标题查阅，范围以正文和后续审核为准。

[回到成果索引](../sources/outputs/README.md)

- [B_n 参数无关子问题模板编译器](../sources/outputs/triple_average/history/ai3_bn_template_compiler.md)
- [多危险素数三幂核的链间耦合与加权和转移](../sources/outputs/triple_average/history/ai3_multprime_chain_report.md)
- [三平均的继续研究：正确级联、反向分拆编码与对数界的核心障碍](../sources/outputs/triple_average/history/ternary_averaging_continued_research.md)
- [三平均的进一步结构：五元精确递归、三进连分数与判定边界](../sources/outputs/triple_average/history/ternary_averaging_deeper_results.md)
- [三平均的进一步推进：二字母逆树、严格高度枚举与对数界的剩余核心](../sources/outputs/triple_average/history/ternary_averaging_further_progress.md)
- [三平均问题的新结构：三进支持集、提升机制与五元特殊性](../sources/outputs/triple_average/history/ternary_averaging_new_insights.md)
- [仿射交换子理想：从可逆宏预测整个根参数族](../sources/outputs/triple_average/history/triple_average_affine_commutator_ideal.md)
- [所有偶维 B 核的统一减半定理](../sources/outputs/triple_average/history/triple_average_all_even_B_kernel_halving.md)
- [三平均任意维数的全局视角：有限基维数究竟说明了什么](../sources/outputs/triple_average/history/triple_average_arbitrary_n_outlook.md)
- [三平均的算术几何结构：射影投影、二次型与 adelic 高度](../sources/outputs/triple_average/history/triple_average_arithmetic_geometry_view.md)
- [外部 audit 的修订与证据登记](../sources/outputs/triple_average/history/triple_average_audit_resolution_2026-09-09.md)
- [\(\mathcal B_{12}\) 二维核有限实验](../sources/outputs/triple_average/history/triple_average_b12_kernel_experiment.md)
- [B12 六步局部下降与二次序导子塔](../sources/outputs/triple_average/history/triple_average_b12_six_step_and_conductor_tower.md)
- [绕开 B17 调用库封闭域的跨核桥](../sources/outputs/triple_average/history/triple_average_b17_cross_stratum_escape.md)
- [B17 的带条件子问题返回实验](../sources/outputs/triple_average/history/triple_average_b17_guarded_subproblem_experiment.md)
- [B21 深度五性能复核与整数状态商](../sources/outputs/triple_average/history/triple_average_b21_integer_search_optimization.md)
- [47元当前模板库的精确周期边界](../sources/outputs/triple_average/history/triple_average_b47_cycle_frontier.md)
- [47元新正向对合与三进平移群：模板内部的一步扩展](../sources/outputs/triple_average/history/triple_average_b47_extra_atom_and_adjoint.md)
- [三平均的本质结构：重写系统、托里克关系与有限时间共识](../sources/outputs/triple_average/history/triple_average_barycentric_toric_view.md)
- [危险支持集的图论核心：从 n-3d-1 提高到 n-d-2](../sources/outputs/triple_average/history/triple_average_blocker_graph_core.md)
- [三幂几何链上的 Burau 群：任意秩可逆宏定理](../sources/outputs/triple_average/history/triple_average_burau_power_chain.md)
- [(t=4,s=3) Burau 高秩算术性审计](../sources/outputs/triple_average/history/triple_average_burau_rank4_arithmetic_audit.md)
- [载体扫掠催化器：从七元 Artin 中心到十元局部 SL3](../sources/outputs/triple_average/history/triple_average_carrier_sweep_catalyst.md)
- [三进扩张修复宏与严格算术接口](../sources/outputs/triple_average/history/triple_average_carry_repair_and_arithmetic_interface.md)
- [同余子群是否是通用方法：有限轨道原则与严格边界](../sources/outputs/triple_average/history/triple_average_congruence_method_scope.md)
- [多危险素数的覆盖设计：为何局部安全下降不能直接统一](../sources/outputs/triple_average/history/triple_average_covering_design_obstruction.md)
- [对角资源压缩：根群加一个剩余单位种子](../sources/outputs/triple_average/history/triple_average_diagonal_resource_reduction.md)
- [数字算子的完整同余群：平衡生成、循环扩张与有理轨道分类](../sources/outputs/triple_average/history/triple_average_digit_congruence_group.md)
- [等载体形式冻结定理：SL--交换--SL 三段正规形](../sources/outputs/triple_average/history/triple_average_equal_carrier_formal_freezing.md)
- [偶维 B 核的八元归并减半桥](../sources/outputs/triple_average/history/triple_average_even_kernel_halving_bridge.md)
- [偶次返回：参数交换与宽度四根](../sources/outputs/triple_average/history/triple_average_even_return_root_interface.md)
- [精确返回的支撑刚性：载体必须最后混合](../sources/outputs/triple_average/history/triple_average_exact_return_support_rigidity.md)
- [Hecke 与模符号路线的最后检验](../sources/outputs/triple_average/history/triple_average_final_hecke_audit.md)
- [原维数平坦核的统一算术性：显式幺幂与高秩初等群](../sources/outputs/triple_average/history/triple_average_flat_star_arithmeticity.md)
- [三平均的任意维数框架：根格、二维核与三进维数提升](../sources/outputs/triple_average/history/triple_average_general_n_synthesis.md)
- [三平均的整体复审：六元有限判定与七八元完整判据](../sources/outputs/triple_average/history/triple_average_global_breakthrough.md)
- [三进无关部分只有一个素数时的统一降维](../sources/outputs/triple_average/history/triple_average_isolated_prime_reduction.md)
- [Hecke 代数恒等式与尚未建立的模形式接口](../sources/outputs/triple_average/history/triple_average_iwahori_hecke_modular_interface.md)
- [标准核接口与自守路线的统一说明](../sources/outputs/triple_average/history/triple_average_kernel_interface_and_automorphic_route.md)
- [从局部化根群到素数同余群：统一生成定理](../sources/outputs/triple_average/history/triple_average_localized_iwahori_generation.md)
- [三平均有限步可达性：研究总纲与当前路线](../sources/outputs/triple_average/history/triple_average_master_summary.md)
- [混合单点迹零返回：全非分裂素数的单一条件归约](../sources/outputs/triple_average/history/triple_average_mixed_singleton_controller.md)
- [Modern Frame 的可用部分与严格化契约](../sources/outputs/triple_average/history/triple_average_modern_framework_review_and_contract.md)
- [有限模正向化与高度的严格边界](../sources/outputs/triple_average/history/triple_average_modular_height_barrier.md)
- [多个危险素数仍给出线性高重数核心](../sources/outputs/triple_average/history/triple_average_multi_prime_core.md)
- [固定词一致性障碍：统一证明必须依赖状态或降维](../sources/outputs/triple_average/history/triple_average_no_oblivious_consensus.md)
- [非分裂Reynolds层的完整置换影子：交错群](../sources/outputs/triple_average/history/triple_average_nonsplit_alternating_shadow.md)
- [非分裂素数的可预测结构：17至59证书后的综合](../sources/outputs/triple_average/history/triple_average_nonsplit_prime_structure_synthesis.md)
- [非分裂三阶轨道与双载体：原位置实现](../sources/outputs/triple_average/history/triple_average_nonsplit_punctured_orbits.md)
- [合数的统一因子归约：奇数乘法闭包与八整除族](../sources/outputs/triple_average/history/triple_average_odd_composite_factor_closure.md)
- [奇次返回的容量族与53元目标](../sources/outputs/triple_average/history/triple_average_odd_return_capacity_family.md)
- [一次三份复制稳定化：离散梯度、Hilbert 90 与平衡初等变换](../sources/outputs/triple_average/history/triple_average_one_tripling_stabilization.md)
- [统一混合返回的原位置分解前沿](../sources/outputs/triple_average/history/triple_average_original_position_factorization_frontier.md)
- [其他 AI 报告复核：可用的局部到整体接口](../sources/outputs/triple_average/history/triple_average_other_ai_local_global_review.md)
- [等值载体核与二进重分组：一个统一的保秩正向宏](../sources/outputs/triple_average/history/triple_average_paired_carrier_reset.md)
- [参数周期刚性：为什么逐素数短周期不能成为统一证明](../sources/outputs/triple_average/history/triple_average_parametric_cycle_rigidity.md)
- [置换剩余像与局部耦合：九十一元旧容器的严格修正](../sources/outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md)
- [正向根群饱和：47元全库逆元与统一素数策略](../sources/outputs/triple_average/history/triple_average_positive_root_saturation.md)
- [(n-4) 为三幂时的统一返回宏](../sources/outputs/triple_average/history/triple_average_power_block_macro.md)
- [任意维数的三幂分块压缩：把一般输入降到对数秩标准核](../sources/outputs/triple_average/history/triple_average_power_partition_reduction.md)
- [素数维数为什么出现同余子群：稳定子定理与尺度周期](../sources/outputs/triple_average/history/triple_average_prime_congruence_structure.md)
- [先解素数再归约合数：可行主线、严格接口与三进进位桥](../sources/outputs/triple_average/history/triple_average_prime_first_factor_reduction.md)
- [素数情况的完整证明路线与剩余猜想](../sources/outputs/triple_average/history/triple_average_prime_proof_roadmap.md)
- [全局标量周期的谱判据：Newton 多边形、Kronecker 与分圆验证](../sources/outputs/triple_average/history/triple_average_projective_spectral_balance.md)
- [三份复制消去：同步路径、算术商与严格边界](../sources/outputs/triple_average/history/triple_average_replica_elimination_research.md)
- [研究复核：目标平均值、动力学方向与算法边界](../sources/outputs/triple_average/history/triple_average_research_corrections.md)
- [三平均研究最新总览与交接说明（2026-09-09）](../sources/outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md)
- [更内在的代数对象：Reynolds 半群、交叉计数与判别式对偶](../sources/outputs/triple_average/history/triple_average_reynolds_hecke_hodge.md)
- [非分裂素数路线复盘：停止局部拼接，返回二维除法结构](../sources/outputs/triple_average/history/triple_average_route_reassessment_2026-09-11.md)
- [B12、B15、B18、B21 的统一有限比较](../sources/outputs/triple_average/history/triple_average_single_prime_kernel_comparison.md)
- [所有 p=1 mod3 素数的完整判据：高斯周期正向控制器](../sources/outputs/triple_average/history/triple_average_split_prime_gaussian_controller.md)
- [任意维数的新统一结果：复制稳定化、双随机矩阵与消去猜想](../sources/outputs/triple_average/history/triple_average_stabilization_theorem.md)
- [结构图景复核：可用的局部到整体机制及数域边界](../sources/outputs/triple_average/history/triple_average_structural_picture_audit.md)
- [三平均问题的局部算术轨道图景：结构性猜测与证明路线](../sources/outputs/triple_average/history/triple_average_structural_picture_conjecture.md)
- [子问题调用的缺失素数障碍与奇素数维数](../sources/outputs/triple_average/history/triple_average_subproblem_prime_obstruction.md)
- [主线与三个并行研究方向的交接](../sources/outputs/triple_average/history/triple_average_team_handoff_2026-09-10.md)
- [参数无关宏编译器与范数环面：从 B17 走向任意 n](../sources/outputs/triple_average/history/triple_average_template_compiler_and_torus.md)
- [十三元二维核：已得到的真实宏与剩余的三进高度问题](../sources/outputs/triple_average/history/triple_average_thirteen_macro_frontier.md)
- [三进运输稳定化：双随机返回与复制消去的精确接口](../sources/outputs/triple_average/history/triple_average_triadic_transport_stabilization.md)
- [十二元四宏的参数延拓及其关系边界](../sources/outputs/triple_average/history/triple_average_twelve_macro_family_extension.md)
- [有限模控制的正向实现：所有 n=5 mod6 的二例外归约](../sources/outputs/triple_average/history/triple_average_two_carrier_modular_bridge.md)
- [两个统一迹零返回：根10与有限局部终端](../sources/outputs/triple_average/history/triple_average_two_trace_zero_returns.md)
- [三平均的统一框架：带局部条件的有向操作与算术轨道](../sources/outputs/triple_average/history/triple_average_unified_modern_framework.md)
- [参数无关子问题调用：局部化整数模判据与十七元新宏](../sources/outputs/triple_average/history/triple_average_universal_subproblem_lattice.md)
- [统一迹零返回目标：从孤立周期到参数恒等式](../sources/outputs/triple_average/history/triple_average_universal_trace_zero_target.md)
- [危险素数的见证重置：局部约分为何必须纳入一般算法](../sources/outputs/triple_average/history/triple_average_witness_reset_lemma.md)
- [可填充三幂块的统一收尾](../sources/outputs/triple_average/history/triple_average_zero_padding_theorem.md)

<!-- END SOURCE doc-ebec1ec81c79 -->

---

<a id="doc-ca9dbd7f83fe"></a>

## 原文导签：B_n 参数无关子问题模板编译器

来源：`outputs/triple_average/history/ai3_bn_template_compiler.md` · [逐字节原样副本](../sources/outputs/triple_average/history/ai3_bn_template_compiler.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`ai3-template-report-audit`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ca9dbd7f83fe -->
# B_n 参数无关子问题模板编译器

本文把“一个子问题能否对所有参数调用”写成可计算的 Smith/Fitting 条件，并把它和返回后的局部合法性分开处理。结果给出两个适用于任意 (n) 的真实模板族，以及以三幂维数为子问题的无穷多条严格规模递减调用边。

这里不重复十七元的具体宏，也不声称这些返回宏已经给出任意 (B_n) 的终止控制器。

令

\[
R=\mathbb Z[1/3],\qquad
\mathcal B_n(u,v)=(u^{n-4},v^3,w),\quad
w=-(n-4)u-3v.
\]

对整数 (N\ne0)，记

\[
N_{\ne3}=N/3^{v_3(N)}.
\]

## 1. 可编译模板的状态数据

一个参数无关调用模板包含：

1. 一个实际三平均前置词，把 (\mathcal B_n(u,v)) 送到若干坐标
   \[
   x_i=u+c_i d,\qquad d=(v-u)/m,
   \]
   其中 (m) 是三幂；
2. 一个大小为 (s) 的子块 (C)，其系数为 (c_1,\ldots,c_s\)；
3. 一个已证明完整判据的 (s) 元子程序；
4. 一个实际三平均后置词，把子块归并值与残余位置重新编译为
   \(\mathcal B_n(u',v')\)；
5. 输出矩阵 (M\in M_2(R))，使
   \[
   \binom {u'}{v'}=M\binom uv.
   \]

前置和后置词必须有独立的位置重数账本。下面的格判据只负责第 2 步的“可调用性”，不能凭形式矩阵取代真实词。

## 2. 秩一 Smith/Fitting 判据

令 (a=c_1)，并定义

\[
g=\gcd_i(c_i-a),\qquad T=\sum_{i=1}^s c_i.
\]

系数差模是秩一 (R)-模

\[
L=gdR.
\]

子块均值减去锚点值为

\[
\mu-(u+ad)=\frac{T-sa}{s}d.
\]

故得到如下精确的编译判据。

> **秩一模板定理。** 子块均值对全部参数 (u,v) 都属于原子块的仿射 (R)-格，当且仅当
> \[
> \boxed{(sg)_{\ne3}\mid T-sa.}
> \tag{2.1}
> \]

证明只需将上式除以 (gd)：所需系数属于 (R)，当且仅当

\[
\frac{T-sa}{sg}\in R.
\]

这正是 (2.1)。在一般二维参数模板中，同一个条件由差系数矩阵的 Smith 标准形给出；这里的唯一非零 Smith 不变量就是 (g)。

从 Fitting 理想的角度，局部障碍由有限商

\[
(L+R(\mu-x_1))/L
\]

在每个 (p\ne3) 的长度决定；其支撑恰是

\[
\frac{(sg)_{\ne3}}
{\gcd((sg)_{\ne3},T-sa)}.
\]

它为 1 当且仅当 (2.1) 成立。

若 (d=0)，子块本来全等。若 (d\ne0)，条件 (2.1) 等价于子块中心化本原化后的差分 gcd 只含 3。故当大小 (s) 已有完整 (G)-判据时，(2.1) 使该子程序可对**所有** (u,v) 调用。

## 3. 返回合法性的独立行列式条件

所有下文模板的输出矩阵有行和 1，可写成

\[
M=
\begin{pmatrix}
1-\lambda&\lambda\\
1-\beta&\beta
\end{pmatrix}.
\]

于是

\[
u'-v'=\det(M)(u-v),\qquad \det(M)=\beta-\lambda.
\tag{3.1}
\]

若 (M\) 的条目在 (R)，且其行列式在每个 (p\mid n, p\ne3) 处为单位，即若写成既约分数

\[
\det(M)=A/3^h
\]

后满足

\[
\boxed{\gcd(A,n_{\ne3})=1,}
\tag{3.2}
\]

那么合法 (B_n) 参数必被送到合法 (B_n) 参数。因为对每个这样的 (p)，式 (3.1) 不会使原来的非零 (u-v\pmod p) 消失。

条件 (2.1) 和 (3.2) 逻辑独立。前者只保证子问题对所有参数可调用；后者才保证该调用编译成的返回宏可以继续作用在合法 (B_n) 参数上。

## 4. 模板 T1：调用大小 n-4 的子问题

设

\[
r=n-4,qquad m=3^h\ge3,qquad r\ge m+1.
\]

先对 ((u^{m-1},v)) 执行一个大小 (m) 的真实三进网络，得到

\[
a=u+d,\qquad d=(v-u)/m.
\]

选择 (r) 元子块

\[
C_1=(a^{m-1},u^{r-m-1},v^2).
\tag{4.1}
\]

它的系数模式是

\[
(1^{m-1},0^{r-m-1},m^2),
\]

故 (g=1,T=3m-1)。判据 (2.1) 变为

\[
\boxed{r_{\ne3}\mid3m-1.}
\tag{4.2}
\]

在 (4.2) 下，若 (r) 元问题已经解决，归并 (C_1) 后尚余一个 (a)、两个 (u) 和 (w)。真实平均 ((a,u,u)) 后得到新的 (B_n)。输出为

\[
\begin{aligned}
u'&=u+\frac{3m-1}{mr}(v-u),\\
v'&=u+\frac1{3m}(v-u),
\end{aligned}
\tag{4.3}
\]

因而

\[
M_1=
\begin{pmatrix}
1-\frac{3m-1}{mr}&\frac{3m-1}{mr}\\
1-\frac1{3m}&\frac1{3m}
\end{pmatrix},
\qquad
\det(M_1)=\frac{n-1-9m}{3m(n-4)}.
\tag{4.4}
\]

分母只含 3 的部分之外来自 (n-4)，但 (4.2) 已保证在其非三素数处约掉；最终是否保持 (B_n) 合法性仍由 (3.2) 对既约形式检测。

位置账本如下：前置网络使用 (m) 个位置；子块使用 (m-1) 个新 (a)、(r-m-1) 个 (u)、两个 (v)；后置三平均使用留下的一个 (a) 和两个 (u)。最终正好保留 (r) 个子块均值、三个新 (v') 和原单点 (w)。

## 5. 模板 T2：调用大小 n-2 的子问题

仍令 (r=n-4)，并设 (m=3^h\ge3)、(r\ge m-2)。先对

\[
(u^{m-2},v^2)
\]

执行真实大小 (m) 三进网络，得到

\[
a=u+2d,\qquad d=(v-u)/m.
\]

选择 (s=n-2=r+2) 元子块

\[
C_2=(a^{m-1},u^{r-m+2},v).
\tag{5.1}
\]

其系数模式为

\[
(2^{m-1},0^{r-m+2},m),
\]

仍有 (g=1,T=3m-2)，故通用调用条件为

\[
\boxed{(n-2)_{\ne3}\mid3m-2.}
\tag{5.2}
\]

归并后，只留下一个 (a)、原单点 (w) 和 (n-2) 个均值。平均 ((a,\mu,\mu))，便重建 (B_n)。输出矩阵是

\[
M_2=
\begin{pmatrix}
1-\frac{3m-2}{m(n-2)}&\frac{3m-2}{m(n-2)}\\
1-\frac{2(n-4+3m)}{3m(n-2)}&
\frac{2(n-4+3m)}{3m(n-2)}
\end{pmatrix},
\tag{5.3}
\]

且

\[
\det(M_2)=\frac{2n-2-3m}{3m(n-2)}.
\tag{5.4}
\]

同样，必须对这个既约行列式应用 (3.2)，才可将它登记为保持合法域的返回宏。

## 6. 以三幂子问题为终端库的无穷递归边

已知所有 (3^e) 元问题都已解决。把它们作为子问题库，可得到两族完全符号化的调用边。

取 (m=3)。

**T1 族。** 令

\[
n=3^e+4,\qquad e\ge2.
\]

子问题大小为 (n-4=3^e)，所以 (4.2) 自动成立。由 (4.4)

\[
\det(M_1)=\frac{3^{e-1}-8}{3^{e+1}}.
\]

并且

\[
\gcd(3^e+4,3^{e-1}-8)=\gcd(3^e+4,28).
\]

因此 T1 是保持合法域的全参数返回宏，当且仅当

\[
e\not\equiv1\pmod6.
\tag{6.1}
\]

**T2 族。** 令

\[
n=3^e+2,\qquad e\ge2.
\]

子问题大小 (n-2=3^e)，故 (5.2) 自动成立。由 (5.4)

\[
\det(M_2)=\frac{2\cdot3^e-7}{3^{e+2}},
\]

并且

\[
\gcd(3^e+2,2\cdot3^e-7)=\gcd(3^e+2,11).
\]

因此 T2 是保持合法域的全参数返回宏，当且仅当

\[
e\not\equiv2\pmod5.
\tag{6.2}
\]

这两条结论都给出无穷多个 (B_n) 到一个严格更小、且已解决的 (3^e) 子问题的调用边，规模分别下降 4 和 2。

更一般地，固定任意三幂 (m)，将 T1、T2 分别作用于 (n=3^e+4)、(n=3^e+2) 时，子问题 Smith 条件自动成立。行列式的非三障碍完全落在固定常数上：

\[
\gcd(3^e+4,9m+1),
\qquad
\gcd(3^e+2,3m+2).
\tag{6.3}
\]

故每个固定 (m) 的可用指数集合都是可有效计算的周期同余集合。若该有限周期表存在一个安全余类，就立刻给出无穷模板族；(m=3) 的安全余类已由 (6.1)、(6.2) 明确给出。

## 7. 递归边的边界

这里“规模下降”只指调用的子问题从 (n) 降到 (n-4) 或 (n-2)。调用完成后，整体状态被编译回同一个大小的 (B_n)，并没有把整个 (n) 元问题缩到子问题大小。

因此，模板编译器生成的是带已解子程序的合法**自返回边**：

\[
B_n\xrightarrow{\text{调用已解 }s<n}B_n.
\]

要从这些边推出 (B_n) 完整定理，还须证明这些返回矩阵的半群对每个合法参数最终碰到终端，或把它们接到一个真正的尺寸缩减桥上。T1、T2 的行列式即使在实绝对值小于 1，也通常只把 (u-v) 乘以一个非零有理数，不能在有限步自动变为零。

也不能只检查 (2.1)。例如 (n=11,m=3) 的 T2 调用九元子问题满足 Smith 条件，但

\[
\det(M_2)=11/81.
\]

它在模 11 退化，会把某些合法 (B_{11}) 参数的模 11 差异消掉，所以不是保持合法域的返回宏。这是“子问题全参数合法”不足以推出“全局模板可重复”的明确反例。

## 8. 精确核验

[`work/verify_ai3_bn_template_recursion.py`](../sources/work/verify_ai3_bn_template_recursion.py) 用 `Fraction` 检查：

- 48 个实际前置三进网络、抽象已证子程序调用和后置三平均的位置账本；
- 2,131 组秩一 Smith/Fitting 数据及仿射格整除条件；
- 91 个行列式局部单位判据，其中 27 个故意保留的非单位边界；
- T1/T2 三幂子问题无穷族的 128 个指数前缀，以及 (B_{11}) 反例。

输出：

```text
template real-network and 2x2 matrix checks: PASS 48
Smith/Fitting child-lattice checks: PASS 2131
away-from-3 determinant checks: PASS 91 nonunit cases 27
infinite-family and determinant-boundary checks: PASS 128
```

一般量词由第 2--6 节的符号推导给出。脚本属于 `symbolic-check` 与 `finite-sanity`，不证明返回半群的终止，也没有改动统一验证清单。

<!-- END SOURCE doc-ca9dbd7f83fe -->

---

<a id="doc-ce9ba26a79c4"></a>

## 原文导签：多危险素数三幂核的链间耦合与加权和转移

来源：`outputs/triple_average/history/ai3_multprime_chain_report.md` · [逐字节原样副本](../sources/outputs/triple_average/history/ai3_multprime_chain_report.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ce9ba26a79c4 -->
# 多危险素数三幂核的链间耦合与加权和转移

本文只研究三幂分块核中的真实宏、局部非三素数见证和链间加权和转移，不处理十四元，也不声称已经得到任意核的终止算法。

设

\[
K_{\mathbf r}=\{(u_1^{r_1},\ldots,u_t^{r_t}):
 r_i=3^{k_i},\ \sum_i r_i u_i=0\},
\]

其中每个块 (i) 表示 (r_i) 个相同位置，值为 (u_i\in\mathbb Z[1/3])。对 (p\ne3)，定义块值的局部见证为

\[
W_p(u)=\{u_i\bmod p:1\le i\le t\}.
\]

称 (p)-见证存在，当且仅当 (W_p(u)) 至少含两个余类。由于 (r_i) 是三幂，所有 (r_i) 在模 (p) 下可逆。若展开状态的差分 gcd 为三的幂，则每个 (p\mid n, p\ne3) 都必须有这样的见证。

## 1. 等权三块合并

设三个块 (i,j,k) 的权重均为 (r)，值分别为 (a,b,c)。对每个偏移量 (0\le h<r)，选取这三个块在偏移量 (h) 的三个真实位置，执行一次三平均。共执行 (r) 次真实操作，得到一个权重 (3r) 的新块，值为

\[
m=\frac{a+b+c}{3}.
\]

位置账本是：三个输入块的 (3r) 个位置全部被使用；每次操作使用三个位置并产生三个 (m) 位置；输出是一个 (3r) 重的 (m) 块。加权和严格保持：

\[
r(a+b+c)=3r m.
\]

对固定 (p\ne3)，合并后的块值集合为

\[
\{m\}\cup\{u_\ell:\ell\notin\{i,j,k\}\}.
\]

因此有精确的安全判据：

> **等权合并见证判据。** 合并三块对 (p) 保持见证，当且仅当上述输出集合在模 (p) 下不全相同。

等价地，合并会破坏 (p)-见证，当且仅当所有未选块值都同余于某个 (d)，且

\[
a+b+c\equiv3d\pmod p.
\]

这个条件必须对每个危险素数分别检查，不能把不同素数的条件简单相乘。

存在真实且合法的破坏见证例子。取 (n=7)、七个权重都为 1，状态

\[
(1,1,5,0,0,0,-7).
\]

它总和为零，差分 gcd 为 1，且模 7 非全同余。合并前三个位置后得到

\[
\left((7/3)^3,0,0,0,-7\right).
\]

清除三进分母后，差分 gcd 变成 7。因此等权进位不是无条件的安全操作；必须使用上面的逐素数判据，或使用已经登记的危险支持集排除条件。

## 2. 任意不同三幂权重块的真实交换

取两个块，设大块权重为 (R)，小块权重为 (q)，并令

\[
R=sq,\qquad s=3^h>1.
\]

大块值为 (u)，小块值为 (v)。把小块的 (q) 个位置逐个作为种子；对每个种子，从大块取出 (s-1) 个位置，用标准三进扩张树把种子扩张成 (s) 个位置。每个种子使用

\[
\frac{s-1}{2}
\]

次真实平均，共使用

\[
q\frac{s-1}{2}=\frac{R-q}{2}
\]

次真实操作。大块还剩 (q) 个旧 (u) 位置。于是位置级输出账本为

\[
\begin{array}{c|c|c}
\text{输出块}&\text{位置数}&\text{输出值}\\ \hline
\text{原大块位置}&R& m=((s-1)u+v)/s\\
\text{原小块位置}&q&u
\end{array}
\]

即真实宏

\[
(u^R,v^q)\longmapsto(m^R,u^q),
\qquad m=\frac{s-1}{s}u+\frac1s v.
\tag{2.1}
\]

加权和恒等式为

\[
Rm+qu
 =q((s-1)u+v)+qu
 =Ru+qv.
\]

因此该宏可以用于不同链的块之间，而不要求任一条链单独加权和为零。

## 3. 对所有危险素数同时保持见证

交换宏 (2.1) 对每个 (p\ne3) 都保持非全同余见证，而且不需要分别为每个素数挑选交换边。

设交换后所有块值都同余于 (d\pmod p)。输出小块值是旧 (u)，故 (u\equiv d)。输出大块值满足

\[
s m=(s-1)u+v.
\]

由于 (s) 在模 (p) 下可逆，(m\equiv d\) 与 (u\equiv d) 联立得到 (v\equiv d)。其余未改变的块也都同余于 (d)，所以交换前所有块值已经同余。这证明了逆否命题：

> **跨链交换见证引理。** 若交换前对某个 (p\ne3) 存在至少两个块值不同，则交换后仍存在至少两个块值不同。该结论对所有 (p\mid n, p\ne3) 同时成立。

这里不要求 (p\nmid R) 或 (p\nmid q)，只要求 (p\ne3)，因为交换比例 (s) 是三幂。由此，交换宏比等权合并更适合作为多危险素数环境中的“安全耦合”操作。

## 4. 单位置载体交换

设有一个单独位置 (w)，以及一个权重 (r=3^h>1) 的块值 (u)。把单独位置作为种子，从 (r)-块中取出 (r-1) 个位置进行三进扩张树，使用

\[
\frac{r-1}{2}
\]

次真实平均，留下一个旧 (u) 位置。输出为

\[
(w^1,u^r)\longmapsto
\left(u^1,\left(\frac{w+(r-1)u}{r}\right)^r\right).
\tag{4.1}
\]

令 (d=u-w)，则新单位置仍为旧 (u)，新大块值为 (u-d/r)。因此

\[
d'=-\frac d r.
\tag{4.2}
\]

若还有其他块值 (u_i)，以新的单位置为参考，

\[
d_i'=u_i-u=d_i-d.
\tag{4.3}
\]

这正是三幂核中的局部多维减法公式。

载体交换也逐个保持所有 (p\ne3) 见证：如果输出全同余于 (c)，保留下来的单位置给出 (u\equiv c)，新大块值给出 (w+(r-1)u\equiv rc)，从而 (w\equiv c)。未改变块也必须同余，故输入本来已经全同余。

## 5. 链间加权和转移

把块索引划分为若干条链 (C_1,\ldots,C_m)，不要求每条链自身加权和为零。定义

\[
S_a=\sum_{i\in C_a}r_i u_i,
\qquad \sum_a S_a=0.
\]

若大块 (i\in C_a) 与小块 (j\in C_b) 进行交换，令

\[
\Delta=q(v-u),\qquad q=r_j.
\]

则

\[
S_a'=S_a+\Delta,
\qquad
S_b'=S_b-\Delta,
\tag{5.1}
\]

其他链和不变。也就是说，跨链交换把一份精确质量 (Delta) 从一条链转移到另一条链；总和恒为零。该转移量由实际选中的两个块值和小块权重决定，而不是任意可调参数。

如果恰好有

\[
\Delta=-S_a,
\tag{5.2}
\]

则链 (C_a) 被一次交换精确归零，非零链数量严格下降。这是一个可检验的链间终端判据。

更一般地，对链和平方势

\[
\Phi=\sum_a S_a^2,
\]

单次 (a,b) 交换满足精确恒等式

\[
\Phi'-\Phi=2\Delta(S_a-S_b)+2\Delta^2.
\tag{5.3}
\]

因此当

\[
\Delta\bigl(S_a-S_b+\Delta\bigr)<0
\tag{5.4}
\]

时，链和平方严格下降。条件 (5.4) 是一个真实可执行的局部下降判据。

## 6. 终止性的准确边界

式 (5.3) 尚不能给出一般终止定理。原因有两个：

1. 可用转移量只在集合
   \[
   \{r_j(u_j-u_i):i,j\text{ 属于不同链}\}
   \]
   中取值，不能任意选择。即使 (Phi>0)，也可能没有满足 (5.4) 的跨链边。
2. 交换包含除以 (s=3^h) 的步骤。若当前值分母只含 (3^K)，一次交换可能把分母高度提高到 (K+h)。因此把 (Phi) 乘以一个固定三幂后取整数，并不能形成已知的良序下降量。

可以使用如下条件势函数，但只能得到条件定理：

\[
\Psi=(z,\Phi),
\qquad
z=\#\{a:S_a\ne0\},
\]

先在满足 (5.2) 的交换中严格降低 (z)，否则在满足 (5.4) 且分母高度不增加的步骤中降低 (Phi)。要把它升级为全称终止定理，还必须证明：只要 (z>0)，总能找到一个保持局部见证的跨链交换，使 (z) 或该有界高度版本的 (Phi) 严格下降。目前没有这样的选择引理。

等权三块合并确实降低块数，但其局部见证可能被完全消除；跨链交换保持所有见证，却不一定降低块数或链和势。因此两类宏需要配合一个“安全合并或可下降交换”二择一引理，这正是多危险素数一般核的主要缺口。

## 7. 严格结论与未解决部分

本文得到以下可直接复用的命题：

1. 任意两个不同三幂权重块之间都有真实交换宏，操作数为 ((R-q)/2)；
2. 该宏精确转移链和 (q(v-u))；
3. 该宏对所有 (p\ne3) 同时保持非全同余见证；
4. 单位置载体交换给出 (d_j'=-d_j/r_j)、(d_i'=d_i-d_j)，并同样保持所有局部见证；
5. 等权三块合并的安全性有精确逐素数判据，但没有无条件安全性；
6. 链和平方势的变化式 (5.3) 给出可检查的条件下降。

尚未证明：

- 任意多链状态都存在满足 (5.2) 或 (5.4) 的交换；
- 允许等权安全合并和跨链交换后，块数必然有限步降到零和三幂终端；
- 动态三进分母高度可以和链和势联合形成良序；
- 多个危险素数的见证重置可以在合并失败时由统一的交换图控制。

因此本文是一个链间耦合接口和条件下降定理，不是一般 (K_{\mathbf r}) 的充分性证明。

## 8. 精确核验

脚本 [`work/verify_ai3_multprime_chain.py`](../sources/work/verify_ai3_multprime_chain.py) 只使用整数和 `Fraction`，包含：

- 19 个真实交换和单位置载体的位置账本；
- 43,784 个随机多危险素数局部见证保持检查；
- 823,536 个模 7 残基的等权合并判据穷举；
- 一个 (G=1) 但合并后出现 (p=7) 公因子的具体反例；
- 1,000 个链和转移及平方势恒等式检查。

运行输出：

```text
real exchange/carrier ledgers: PASS 19
simultaneous p!=3 witness preservation: PASS 43784
equal-carry safety criterion and p=7 counterexample: PASS 823536
chain-sum transfer identities and potential: PASS 1000
```

证据等级为 `symbolic-check` 加 `finite-sanity`。脚本不证明任意核的终止，也没有修改统一 manifest。

<!-- END SOURCE doc-ce9ba26a79c4 -->

---

<a id="doc-bc3da3b4a273"></a>

## 原文导签：三平均的继续研究：正确级联、反向分拆编码与对数界的核心障碍

来源：`outputs/triple_average/history/ternary_averaging_continued_research.md` · [逐字节原样副本](../sources/outputs/triple_average/history/ternary_averaging_continued_research.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-bc3da3b4a273 -->
# 三平均的继续研究：正确级联、反向分拆编码与对数界的核心障碍

更新：整体结论与六元、七八元的新证明见 [整体复审](../sources/outputs/triple_average/history/triple_average_global_breakthrough.md)。本篇反向高度猜想只对应成功轨道；它不自动给出失败轨道的线性对数界。

这份补充笔记推进两个已经提出的问题：支持集大小为 3 时的首次提升结构，以及五元递归能否从 (O((\log H)^2)) 进一步压缩到 (O(\log H))。结论分成已证明事实与仍待证明的高度问题；后者现在有一个精确的整数矩阵表述。

## 1. 支持集问题已经闭合

若当前本原状态满足

\[
x\equiv t\mathbf 1_T\pmod 3,
\qquad |T|=3,quad t\ne0,
\]

对任一三元组 (U)，令 (m=|T\cap U|)。则

\[
\sum_{i\in U}x_i\equiv mt\pmod3.
\]

所以提升恰好在 (m=0) 或 (m=3) 时发生；在 (m=1,2) 时，新的模 (3) 支持集就是 (U)，仍然恰有三个位置。因此从这种状态开始，在第一次提升以前，支持集大小始终为 3，首次提升必然使用当前支持集或一个与它不相交的三元组。

这比“存在一条最短路径”的说法更强：它对每条路径成立。它也解释了为什么此前支持集大小为 4 的六元反例没有矛盾。

## 2. 级联方向的审计

五元闭族的递归为

\[
(u,v)\mapsto
\begin{cases}
(v-u/3,-u/3),&3\mid u,\\
(u-v/3,-v/3),&3\mid v.
\end{cases}
\tag{1}
\]

其中本原非停机状态中恰有一个坐标能被 (3) 整除。若活动坐标有形状 (3^k t)，定义一次级联为连续执行，直到这个 (3)-进因子全部消耗。第一次递归后，活动坐标总在第二个位置；后续必须继续使用第二条分支，而不是交替使用两个分支。

令

\[
d_k=\frac{3^k+(-1)^{k-1}}4,
\qquad k\ge1.
\]

若 (a=3^k t) 是级联开始时的活动坐标，而 (b) 是另一个坐标，则直接归纳给出

\[
C_k(a,b)=(b-d_k t,\;(-1)^k t).
\tag{2}
\]

该式对初始活动坐标是 (u) 或 (v) 都成立，只需把 (a,b) 按活动坐标和伴随坐标理解。级联结束时第二个坐标不被 (3) 整除；若轨迹继续，第一个坐标就是下一段级联的活动坐标。

此前的验证程序在“第二个坐标先被 (3) 整除”的分支上错误切换了坐标方向。这个程序已修复；公式 (2) 和下面的两级联估计都以修复后的实现重新检查。

## 3. 仍然成立的平方对数上界

写

\[
\alpha_k=\frac{d_k}{3^k}
=\frac14+\frac{(-1)^{k-1}}{4\,3^k},
\qquad
\beta_k=\frac{(-1)^k}{3^k}.
\]

则 (2) 等价于

\[
C_k(u,v)=(v-\alpha_k u,\;\beta_k u),
\tag{3}
\]

其中第一坐标为下一段的活动坐标。由于

\[
0<\alpha_k\le\frac13,
\qquad |\beta_k|\le\frac13,
\]

连续两段级联后有

\[
|u_2|\le\frac49|u|+\frac13|v|,
\qquad
|v_2|\le\frac19|u|+\frac13|v|.
\]

从而

\[
H(u_2,v_2)\le\frac79H(u,v),
\qquad H(u,v)=\max(|u|,|v|).
\tag{4}
\]

单段级联至多把 (H) 放大到 (4H/3)。因此级联数是 (O(\log H_0))，每段的长度又至多 (O(\log H_0))，给出严谨的

\[
\boxed{\text{五元递归步数为 }O((\log H_0)^2).}
\]

这已经是输入位长的多项式时间判定界。它只适用于五元闭族及枚举第一次三元选择后的五元输入，不能外推到一般 (n\ge6)。

## 4. 反向级联的精确编码

公式 (2) 可以完全反解。令终点取为本原代表

\[
e=(1,-1).
\]

长度为 (k) 的反向级联是整数矩阵变换

\[
P_k(U,V)=
\left((-1)^k3^kV,\;
U+\gamma_kV\right),
\qquad
\gamma_k=\frac{(-1)^k3^k-1}{4}.
\tag{5}
\]

若一条成功轨道的级联长度依次为

\[
(k_1,\ldots,k_m),
\]

则其起点恰为

\[
(u_0,v_0)=P_{k_1}P_{k_2}\cdots P_{k_m}e.
\tag{6}
\]

更强的是，任意正整数序列 ((k_1,\ldots,k_m)) 都产生一条合法成功轨道。归纳理由是：在反向构造中，活动坐标是 (3^{k_i}) 乘以一个 (3)-进单位，而其伴随坐标保持为 (3)-进单位，所以每段的赋值恰好是指定的 (k_i)，不会意外延长或提前终止。

因此，长度总和为 (s) 的成功级联型与 (s) 的有序正整数分拆一一对应；忽略坐标交换和整体符号后，共有 (2^{s-1}) 种。这把五元成功轨道的结构从“带门控的递归”精确化为一个带权整数矩阵半群。

## 5. (O(\log H)) 的等价高度猜想

由 (6)，把平方对数改进为线性对数，等价于证明存在常数 (c>0)，使所有正整数序列都满足

\[
H\!\left(P_{k_1}\cdots P_{k_m}e\right)
\ge 3^{c(k_1+\cdots+k_m)}.
\tag{7}
\]

若 (7) 成立，递归总步数 (s=k_1+\cdots+k_m) 立即满足

\[
s\le c^{-1}\log_3 H(u_0,v_0).
\]

这给出了一个明确目标：不再需要猜测某个一般势函数，而是要证明这类特殊整数矩阵乘积对固定向量 (e) 的统一实高度下界。

这个问题并不由行列式单独解决。每个 (P_k) 的行列式绝对值为 (3^k)，但一个双曲矩阵仍可能有一条较小的实特征方向；证明必须排除由不同 (P_k) 连续把 (e) 逼近这些方向而造成的长期抵消。

## 6. 已有的局部证据与可证子类

当所有级联长度都不超过常数 (K) 时，(4) 立刻给出

\[
\text{总步数}\le K\cdot O(\log H)=O_K(\log H).
\]

另一条精确恒等式解释了全是长度 (1) 的情形。令

\[
Q(U,V)=U^2-UV+3V^2.
\]

则

\[
Q(P_1(U,V))=3Q(U,V).
\tag{8}
\]

故由 (k_i=1) 组成的轨道反向高度按 (3^{m/2}) 增长，前向步数为 (O(\log H))。真正困难仅来自高赋值级联和不同 (P_k) 之间可能发生的实数抵消。

`work/explore_reverse_cascades.py` 对总代价 (s\le18) 枚举所有 (2^{s-1}) 个分拆，逐一正向验证 (6)，并记录最小高度。结果没有显示次指数族；但这只是有限实验，不能替代 (7) 的证明。

## 7. 对一般维数的含义

支持集定理控制的是第一次整体三进提升以前的最低数字。五元中，第一次操作后的三重重数把后续问题压缩为上述二维矩阵系统；一般 (n\ge6) 在提升后保留更多独立坐标，尚无相应的反向分拆编码。因此这里得到的是五元算法结构的显著收紧，而不是一般三平均问题的多项式时间算法。

<!-- END SOURCE doc-bc3da3b4a273 -->

---

<a id="doc-ea211deb7404"></a>

## 原文导签：三平均的进一步结构：五元精确递归、三进连分数与判定边界

来源：`outputs/triple_average/history/ternary_averaging_deeper_results.md` · [逐字节原样副本](../sources/outputs/triple_average/history/ternary_averaging_deeper_results.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`cascade-bound`, `n5-bounded-search`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ea211deb7404 -->
# 三平均的进一步结构：五元精确递归、三进连分数与判定边界

更新：本篇保留五元证明的研究记录。六元现已获得完整的伪多项式有限判定，七八元已得到安全操作引理；见 [整体复审](../sources/outputs/triple_average/history/triple_average_global_breakthrough.md)。下文早期的朴素模三幂搜索建议已纠正。

## 结论先行

目前还没有一般输入规模 \(n\ge6\) 的充要判据，也没有可以确认的多项式时间判定算法。不过可以把问题推进到一个严格的新层次：

1. 对任意整数输入，(G) 是 (3) 的幂仍然只是必要条件，不是充分条件。
2. 对 (n=5)，在第一次操作之后，所有状态都落入一个二维射影族；这个族有一个完全的递归判定。
3. 该递归不是普通的模 (3) 检查，而是一个三进连分数式的确定性动力系统。它解释了为什么反例 ((-3,0,1,1,1)) 会永久停留在障碍中，也给出了五元情形的可验证证书。
4. 对五元递归，成功分支是确定性的；按三进级联分组后可得到严格的平方对数步数上界。关于把该界压缩为线性对数的精确高度问题，见 `ternary_averaging_continued_research.md`。

## 1. 统一的整数模型

把输入平移到全局平均为 (0)，再清除分母，得到

\[
x=(x_1,\ldots,x_n)\in\mathbb Z^n,
\qquad \sum_i x_i=0.
\]

一次三平均选取 (S=\{i,j,k\})。把新状态乘以 (3)，可以完全避免分数：

\[
y_r=
\begin{cases}
x_i+x_j+x_k,&r\in S,\\
3x_r,&r\notin S.
\end{cases}
\tag{1}
\]

整体乘以一个非零有理数不改变“能否到达零”的问题。因此可以在每一步把坐标整体约去公因子，再继续使用整数状态。

若某个素数 (p\ne3) 除 (G=\gcd_{i<j}(x_i-x_j))，则所有坐标在模 (p) 下相同。三平均在模 (p) 下合法，因为 (3) 可逆；相同的余数经过任意一步仍相同，不可能变成零向量。因此

\[
\boxed{G\text{ 必须是 }3\text{ 的幂}.}
\]

这同时等价于目标平均值具有分母为 (3) 的幂的非负凸组合表示。它是静态的数论筛选，但没有捕捉到局部操作的可达性。

## 2. 五元状态在第一步后闭合

五个坐标中任意选择三个后，这三个坐标变成同一个平均值。因此，除已经为零的状态外，第一步之后必然可以写成

\[
(a,b,c,c,c),\qquad a+b+3c=0.
\tag{2}
\]

令

\[
u=a-c,\qquad v=b-c.
\tag{3}
\]

由于整体缩放不影响可达性，后面把 ((u,v)) 视为有理射影坐标；计算时可以清分母并约去整体公因子。

三种非平凡的选取类型给出以下变换：

\[
\begin{array}{c|c}
\text{选取的三类坐标}&(u,v)\text{ 的新射影坐标}\\ \hline
(a,c,c)&(-u+3v,-u)\\
(b,c,c)&(3u-v,-v)\\
(a,b,c)&(-u-v,-u-v).
\end{array}
\tag{4}
\]

选取 ((c,c,c)) 只是把所有坐标乘以 (3)，在射影状态中是恒等操作。

## 3. 一个闭合的模三陷阱

定义

\[
\mathcal I=\{(u,v):u\equiv v\not\equiv0\pmod3\}.
\tag{5}
\]

这里的坐标先约去整体公因子；在 ​\(\mathcal I\)​ 中公因子不可能含有 (3)。由 (4) 直接得到：

\[
(-u+3v,-u)\equiv(-t,-t),
\quad
(3u-v,-v)\equiv(-t,-t),
\quad
(-u-v,-u-v)\equiv(-2t,-2t)
\pmod3
\]

当 (u\equiv v\equiv t\ne0) 时，三种变换仍在 ​\(\mathcal I\)​ 中。于是 ​\(\mathcal I\)​ 是一个真正的动力学闭集，而不是一次性的同余障碍。

特别地，第三类变换在 (u+v\ne0) 时直接把状态送到 (u'=v'\ne0)；约去公因子后这一定落入 ​\(\mathcal I\)​。只有在

\[
u+v=0
\tag{6}
\]

时，第三类操作才会立即完成最后一步。

## 4. 五元族的完全递归判定

对一个非零射影对 ((u,v))，定义 (R(u,v)) 如下。先把 ((u,v)) 约成整数本原对。

\[
R(u,v)=\text{真}
\]

当且仅当以下递归成立：

\[
\begin{aligned}
u+v=0&\quad\Longrightarrow\quad R(u,v)=\text{真};\\
3\mid u,\ u\ne0,\ 3\nmid v
&\quad\Longrightarrow\quad
R\!\left(\operatorname{prim}\left(v-\frac u3,-\frac u3\right)\right);\\
3\mid v,\ v\ne0,\ 3\nmid u
&\quad\Longrightarrow\quad
R\!\left(\operatorname{prim}\left(u-\frac v3,-\frac v3\right)\right);\\
\text{否则}&\quad\Longrightarrow\quad R(u,v)=\text{假}.
\end{aligned}
\tag{7}
\]

其中 ​\(\operatorname{prim}\)​ 表示除以整体最大公因子。第二行对应选择 ((a,c,c))，第三行对应选择 ((b,c,c))。

### 定理（五元闭族）

状态 ((a,b,c,c,c)) 能有限步三平均到零，当且仅当 (R(a-c,b-c)) 为真。

### 证明要点

若 (6) 成立，选取 ((a,b,c)) 后三者平均为 (0)，重复的三个 (c) 也同时被带入同一平均，完成收尾。

若 (3\mid u) 且 (3\nmid v)，选择 ((a,c,c))。把新状态乘以 (3) 后，用新的三个相等值作基准，得到

\[
\left(v-\frac u3,-\frac u3\right),
\]

再约去整体公因子即可。(3\mid v) 的情形对称。

反过来，若 (u+v\ne0)，第三类操作落入闭集 ​\(\mathcal I\)​，不能成功。若 (u,v) 都不被 (3) 整除且不满足 (6)，前两类操作虽然可以在有理数意义下执行，但清分母后会产生一个额外的 3 因子，并直接落入 ​\(\mathcal I\)​；因此它们不是可行的成功分支。若有一个坐标为零，则另一个本原坐标不被 (3) 整除，仍然不能产生成功分支。剩下的两种情况恰好是 (7) 的第二、三行。

递归的有限性来自一个简单的下降量。注意：在本原整数表示下，递归分支实际上保持 gcd=1，因此“约去公因子”不是主要的终止机制。若 (u=3q\ne0)，则新对是 ((v-q,-q))，满足

\[
|v-q|+|q|\le |v|+2|q|<|v|+3|q|=|v|+|u|.
\tag{8}
\]

若随后再选取对称分支，得到同样的欧几里得型不等式；所以沿成功路径每一步都严格降低 \(|u|+|v|\)，不会出现无限循环。这里的严格结论是数值幅度有限终止，而不是输入位长意义下的多项式步数。

## 5. 从五元闭族到任意五元输入

给定任意五元输入，枚举第一次选择的十个三元组。每个选择产生一个形如 (2) 的状态；对其中的重复值 (c) 和两个剩余坐标计算 ((u,v))，运行递归 (R)。只要有一个第一次选择使 (R) 为真，原输入就可达；若十个选择都为假，则不可达。

这给出五元问题的完整结构性判定和操作证书。证书由两部分组成：第一次选择，以及递归中每一步的 A/B 选择。把递归反向展开即可恢复原始平均操作序列。

这也是反例的精确解释。对

\[
(-3,0,1,1,1),
\]

有 ((u,v)=(-4,-1))，满足 (u\equiv v\equiv2\pmod3)，因而从一开始就在 ​\(\mathcal I\)​ 中。它的三进凸组合表示存在，但所有局部轨道都被闭集挡住。

对照一个可达对，例如

\[
(u,v)=(-23,18),
\]

递归给出 B B A B B A B，最后到达 ((-1,1))；再选取 ((a,b,c)) 完成收尾。这个过程是一个有限的三进欧几里得式轨迹。

## 6. 三进连分数视角

令 (r=v/u\in\mathbb Q\cup\{\infty\})。两种递归分支在射影直线上分别是

\[
T_A(r)=\frac1{1-3r},
\qquad
T_B(r)=\frac r{r-3}.
\tag{9}
\]

分支条件分别是约分后 (u\) 或 (v) 被 (3) 整除。目标是到达 (r=-1)。因此五元问题不是任意二维搜索，而是一个带有三进可除性门控的 Möbius 动力系统。

陷阱 ​\(\mathcal I\)​ 在射影语言中就是 (r\equiv1\pmod3) 的吸收余类。这个解释给出两个算法方向：

* 用三进位逐位判断某个候选轨迹能否继续；
* 研究从 (r=-1) 反向生成的三进连分数语言，若能证明其最短表示长度为 (O(\log H))，则五元递归将得到位复杂度多项式界。

仅由 (8) 的幅度下降不能推出位复杂度界；后面的级联分析给出了严格的 (O((\log H)^2)) 上界。把它进一步改进为 (O(\log H)) 的问题在 `ternary_averaging_continued_research.md` 中被化为一个反向矩阵高度问题。

### 6.1 一个更精确的射影编码

在成功分支中，本原对满足恰好一个坐标被 3 整除。令 \(r=v/u\)（允许 \(u=0\) 的无穷点），则两条分支为
\[
T_A(r)=\frac{1}{1-3r},\qquad T_B(r)=\frac{r}{r-3}.
\]
从终点 \(r=-1\) 反向展开时，两个逆变换分别为
\[
T_A^{-1}(r)=\frac{1-r^{-1}}3,\qquad
T_B^{-1}(r)=\frac{3r}{r-1}.
\]
因此，一个成功证书可写成字母表 \(\{A,B\}\) 上的有限词；对应矩阵
\[
M_A=\begin{pmatrix}-1&3\\-1&0\end{pmatrix},\qquad
M_B=\begin{pmatrix}3&-1\\0&-1\end{pmatrix},
\]
其乘积把初始射影点送到 \((1:-1)\)。这说明五元判定等价于一个带 3-进门控条件的有理半群成员问题，而不是普通的线性不变式检查。

### 6.2 失败证书与可计算下界

若递归在某个本原对停机且 \(u+v\ne0\)，则三种局部操作都不能离开障碍：第三类直接进入 \(u'=v'\ne0\) 的闭集；前两类在余数条件不满足时清分母后也进入同一闭集。这给出一个有限、可逐步验证的局部失败证书。由已证明的幅度下降，证书长度至多是数值幅度 \(H=\max(|u|,|v|)\) 的线性量级；把它改进为输入位长的多项式（例如 \(O(\log H)\)）仍需额外的三进连分数估计。该证书不等同于整个一般 \(n\) 问题的多项式算法。

### 6.3 后续改进：平方对数位复杂度

对五元递归可进一步按连续消耗同一坐标的 3-进赋值分成级联。若级联起点为 (u=3^k t)、(3\nmid t)，则它包含 (k) 个递归步；两次连续级联后满足

\[
H_{\rm after}\le \frac79 H_{\rm before},
\qquad H(u,v)=\max(|u|,|v|).
\]

每个级联起点的幅度至多为初始幅度的 (4/3) 倍，且 (3^k) 不超过该幅度的常数倍。因此级联数为 (O(\log H))，单个级联长度也为 (O(\log H))，总递归步数得到严格的 (O((\log H)^2)) 上界。这把此前“证书长度至多线性于数值幅度”的粗略估计改进为输入位长意义下的多项式界；是否能继续降到 (O(\log H)) 仍是开放的摊销问题。

## 7. 与一般 (n) 的关系

三平均的静态条件和局部可达性之间的差距现在可以清楚地分层：

* 第一层是 (p\ne3) 的同余不变量以及 (G=3^r)；
* 第二层是坐标重数和三进剩余类的动力闭集；
* 第三层才是能否构造一条轨道到达稀疏的“最后三元组”集合。

当 (n=5) 时，第一步制造的三重坐标使第二层闭合成二维系统，所以可以完全分析。(n\ge6) 时，第一次操作后还保留至少三个未选坐标，重数型会继续分裂和合并；二维闭合性消失，这是目前从五元结果推广到一般 (n) 的主要障碍。

仍然成立的充分构造是：如果当前状态能分成若干个大小为 (3^q) 的零和块，并且每个块平均值等于全局平均值，则每个块可独立用三进蝶形网络归零。这个条件容易验证其充分性，但尚未证明必要。

纠正：直接把清分母矩阵投影到模三幂的有限图，不能提供有用的否定证书。重复同一三元组即可使清分母矩阵的乘积模任意固定三幂为零，即使真实平均状态完全不变。每步本原化的转移又不由固定模三幂剩余类决定。需要另行设计并证明可靠的抽象系统，详见整体复审第 9 节。

## 8. 当前可以严谨宣称的范围

* (n=3)：一次操作完成。
* (n=4)：可达当且仅当初始状态已有一个坐标等于全局平均。
* (n=5)：第一次操作枚举加上递归 (R) 给出完整判定；这是本笔记新增的严格结果。
* 一般 (n\ge6)：(G=3^r) 与三进凸组合仍是必要筛选；本篇之后六元已获完整有限判定，但一般充要判据仍未得到。朴素有限三进商不是有效的否定算法。
* 不能据此宣称一般问题已经是 NP-hard，也不能据此宣称存在一般多项式算法；这两种结论都需要新的归约或构造定理。

用于交叉验证的精确程序位于 `work/verify_five_theorem.py`；它检查了小范围的五元闭族和一般五元初态，未发现递归与精确 BFS 的不一致。该实验只用于检验公式，不能替代上面的闭集和下降量证明。

<!-- END SOURCE doc-ea211deb7404 -->

---

<a id="doc-959034b8a9d1"></a>

## 原文导签：三平均的进一步推进：二字母逆树、严格高度枚举与对数界的剩余核心

来源：`outputs/triple_average/history/ternary_averaging_further_progress.md` · [逐字节原样副本](../sources/outputs/triple_average/history/ternary_averaging_further_progress.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-959034b8a9d1 -->
# 三平均的进一步推进：二字母逆树、严格高度枚举与对数界的剩余核心

更新：六元有限判定、七八元安全操作引理及旧有限模商方法的纠正，见 [整体复审](../sources/outputs/triple_average/history/triple_average_global_breakthrough.md)。本篇固定终点的反向编码仅讨论成功轨道。

本续篇继续研究两个问题：模 (3) 支持集恰为三个位置时的首次提升结构，以及五元闭族递归能否从 (O((\log H)^2)) 改进到 (O(\log H))。这里的结论将已证明的定理、严格的算法实验和仍未解决的一条数论引理分开陈述。

## 1. 第一个猜想已经是无条件定理

设当前整数状态满足

\[
x\equiv t\mathbf 1_T\pmod3,
\qquad |T|=3,\quad t\not\equiv0\pmod3.
\]

对任意被选三元组 (U)，记 (m=|T\cap U|)。所选三元组的和模 (3) 为 (mt)。因此：

\[
\begin{array}{c|c|c}
m&\text{所选和模 }3&\text{操作后的模 }3\text{ 支持集}\\ \hline
0&0&\text{发生整体三进提升}\\
1&t&U\\
2&2t&U\\
3&0&\text{发生整体三进提升}
\end{array}
\]

于是，在首次整体三进提升之前，支持集始终恰有三个位置；首次提升的三元组只能是当前支持集本身，或与其完全不相交的三元组。这对任意操作路径都成立，不需要最短路径假设。

这个定理也说明它的边界：支持集大小不等于 (3) 时，交集大小 (1) 或 (2) 仍可能触发提升。已有六元反例

\[
(-1,-1,0,1,0,1)\longrightarrow(0,-1,0,0,0,1)\longrightarrow0
\]

就在首次提升时使用了与模 (3) 支持集交集大小为 (2) 的三元组。因此不能把定理误推广到任意支持集。

## 2. 五元成功证书就是一个受限二字母词

五元闭族的正向递归为

\[
(u,v)\mapsto
\begin{cases}
(v-u/3,-u/3),&3\mid u,\ 3\nmid v,\\
(u-v/3,-v/3),&3\mid v,\ 3\nmid u.
\end{cases}
\]

令两种一步逆变换为

\[
A(U,V)=(-3V,U-V),\qquad B(U,V)=(U-V,-3V).
\]

它们的矩阵是

\[
A=\begin{pmatrix}0&-3\\1&-1\end{pmatrix},\qquad
B=\begin{pmatrix}1&-1\\0&-3\end{pmatrix}.
\]

长度为 (k) 的反向级联满足一个比原来的矩阵公式更透明的分解：

\[
\boxed{P_k=A B^{k-1}}.
\]

事实上，

\[
B^r=
\begin{pmatrix}
1&\frac{(-3)^r-1}{4}\\
0&(-3)^r
\end{pmatrix},
\]

所以这正好给出

\[
P_k(U,V)=\left((-1)^k3^kV,\ U+\frac{(-1)^k3^k-1}{4}V\right).
\]

若总递归步数为 (s)，所有本原射影成功证书一一对应于矩阵词

\[
A\{A,B\}^{s-1}.
\]

从左到右把该词按每个 (A) 后面的连续 (B) 分段，便恢复了正整数分拆 ((k_1,\ldots,k_m))。反过来，每个分拆都合法，因为每一段的伴随坐标始终是 (3)-进单位。不同的词不能产生同一起点：正向递归在每个非终止成功状态只有一个可行分支，故其级联长度序列是唯一的。

这把五元问题化为一个非常具体的命题：从 (e=(1,-1)) 出发，长度为 (s) 的受限二字母逆词是否必有指数高度。

## 3. 一个新的严格单调量，以及它不能单独解决问题的原因

对逆状态定义

\[
L(u,v)=|u|+|v|.
\]

无论选择 (A) 还是 (B)，逆像坐标的绝对值集合都是

\[
\{3|v|,\ |u-v|\}.
\]

故

\[
L(A(u,v))=L(B(u,v))=3|v|+|u-v|> |u|+|v|
\tag{1}
\]

（在合法逆树中 (v\ne0)）。最后的严格不等式按 (u,v) 同号或异号、以及同号时的大小关系逐项验证即可。

这给出两个实际收益。

1. 反向树没有环，且每个高度阈值下的成功证书可以完整枚举。
2. 若起点的最大高度至多为 (H)，则其 (L) 至多为 (2H)。沿反向路径 (L) 严格递增，所以只保留 (L\le2H) 的节点不会丢失任何这样的起点。

需要区分 (L) 与通常高度 (H(u,v)=\max(|u|,|v|))。最大高度并不沿反向路径单调：一个中间点可以较不平衡，之后又变得平衡。因此按 (H) 直接剪枝是错误的；按 (L) 剪枝才是完整的。

但 (1) 尚不能直接推出指数增长。矩阵 (B) 有特征向量 ((1,0)) 和特征值 (1)，且

\[
B^r(N,1)=\left(N+\frac{(-3)^r-1}{4},\ (-3)^r\right).
\]

当 (N\gg3^r) 时，这 (r) 步的 (L) 增长可以任意接近 (1)。所以不存在一个在所有平面方向上对 (A,B) 都统一扩张的固定范数，也不存在基于“每固定步数必收缩/扩张”的直接证明。长 (B) 块正是原平方对数分析中的慢级联。

这里的反例只否定这种全空间的粗略势函数；它没有否定从 (e) 可达的受限整数轨道存在指数高度下界。后者仍是待证的猜想。

## 4. 精确的高度截断实验

`work/height_truncated_reverse_tree.py` 从 (e) 反向生成所有合法父节点，并以 (L\le2H) 截断。由于 (1)，这不是抽样或束搜索，而是在该高度范围内的完整枚举。下表中“最大深度”是最大坐标绝对值不超过 (H) 的所有原始成功对的最大正向递归步数；整体符号视为同一射影状态。

| 高度上限 (H) | 成功射影状态数 | 最大深度 |
|---:|---:|---:|
| (10^2) | 163 | 11 |
| (10^3) | 2,173 | 17 |
| (10^4) | 30,399 | 25 |
| (10^5) | 413,263 | 36 |

这些数值同 (O(\log H)) 相容，也排除了小范围内明显的平方对数反例；它们不是渐近证明。特别地，成功状态数本身随 (H) 增长很快，直接反向枚举不能成为输入位长多项式算法。

实验同时复核了较早的全分拆枚举：总代价 (s\le18) 的全部 (2^{s-1}) 个证书均合法且可正向还原。此范围内的最小高度出现在

\[
(k_1,\ldots,k_9)=(4,1,1,1,5,2,2,1,1),
\qquad H=1291,
\]

其总代价为 (18)。它显示真实抵消会发生，但仍没有显示次指数高度。

## 5. 抵消受到的三进递推约束

令

\[
a_k=(-1)^k3^k,\qquad \gamma_k=\frac{a_k-1}{4}.
\]

把反向路径按级联块编号。若 (V_j) 是第 (j) 个块边界处的第二坐标，则每个 (V_j) 都是非零 (3)-进单位；相邻三项满足

\[
V_{j-1}=\gamma_{k_j}V_j+a_{k_{j+1}}V_{j+1}.
\tag{2}
\]

从而有强同余

\[
\boxed{V_{j-1}\equiv\gamma_{k_j}V_j\pmod {3^{k_{j+1}}}.}
\tag{3}
\]

并且，由 (V_{j+1}\ne0)，

\[
3^{k_{j+1}}
\le |V_{j-1}|+|\gamma_{k_j}|\,|V_j|.
\tag{4}
\]

式 (4) 已经说明：若一个级联长度 (k_{j+1}) 相对于前一块 (k_j) 突然增大，就必须在相邻边界出现大坐标。真正未解的情形是多次精细抵消，让每次大系数的贡献被下一项抵消；(3) 表明这些抵消不能独立选择，而必须满足嵌套的高精度三进同余。

因而，把 (O((\log H)^2)) 改进为 (O(\log H)) 的最直接充分命题为：存在常数 (c>0)，对任意正整数序列 ((k_1,\ldots,k_m))，

\[
\max\left|P_{k_1}\cdots P_{k_m}(1,-1)\right|
\ge3^{c(k_1+\cdots+k_m)}.
\tag{5}
\]

式 (2)--(4) 将 (5) 变成一个有明确局部算术条件的有符号 continuant 高度下界，而不是模糊的“寻找势函数”。证明它需要排除跨很多块的嵌套抵消。

## 6. 下一步最有希望的证明方向

1. 研究 (2) 的最小整数解。把 ((V_j,V_{j+1})) 视为射影斜率，按 (3) 分成有限个 (3)-进余类，寻找一个分段二次势函数。势函数不必在所有实方向扩张，只需在这些可达余类上给出摊销增长。
2. 对出现多次近抵消的区间使用 (3) 连乘。若每次近抵消都要求一个新的、独立的三进精度，则整数坐标的有限大小将强迫总精度为 (O(\log H))，从而直接得到 (5)。要完成这一步，需要严谨处理相邻同余之间可能的依赖。
3. 在计算上，以 (L) 截断的精确逆树可以继续到更高阈值，记录达到最大深度的词和它们的 (k_i) 分布。它适合检验候选势函数，却不能取代证明。

目前能严谨声称的是：五元闭族已有完整判定、严格 (O((\log H)^2)) 操作数界，以及上述二字母逆树和三进 continuant 结构。一般 (n\ge6) 仍没有由这些结论推出的多项式时间判定算法。

<!-- END SOURCE doc-959034b8a9d1 -->

---

<a id="doc-ad82640623de"></a>

## 原文导签：三平均问题的新结构：三进支持集、提升机制与五元特殊性

来源：`outputs/triple_average/history/ternary_averaging_new_insights.md` · [逐字节原样副本](../sources/outputs/triple_average/history/ternary_averaging_new_insights.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ad82640623de -->
# 三平均问题的新结构：三进支持集、提升机制与五元特殊性

更新：本篇是阶段性研究记录。六元不增分母定理、七八元安全操作引理以及有限模商方法的纠正，见 [整体复审](../sources/outputs/triple_average/history/triple_average_global_breakthrough.md)。

本文在 `ternary_averaging_deeper_results.md` 的五元精确递归基础上，提取一个适用于任意维数的三进结构。它不能直接给出一般情形的充要判据，但把 n=5 与 n≥6 的差别定位得更准确。

## 1. 清分母模型

平移到全局平均为 0，并把输入写成原始整数向量
\[
x=(x_1,\ldots,x_n),\qquad \sum_i x_i=0.
\]
选择三元组 \(S\) 后，乘以 3 的新状态为
\[
y_i=
\begin{cases}
s_S:=\sum_{j\in S}x_j,&i\in S,\\
3x_i,&i\notin S.
\end{cases}
\tag{1}
\]
整体除以任意公因子不改变是否能到达零，因此每一步都可以取本原整数代表。

## 2. 三进支持集压缩引理

**引理（一次操作后的模 3 形状）。** 对任意状态和任意选择的三元组 \(S\)，有
\[
y\pmod 3=s_S\,\mathbf 1_S.
\tag{2}
\]
因此：

* 若 \(s_S\not\equiv0\pmod3\)，则新状态模 3 恰好在三个位置 \(S\) 上非零，且这三个余数相同；
* 若 \(s_S\equiv0\pmod3\)，则整个 \(y\) 可被 3 整除，除以 3 后继续研究下一层三进数字。

证明就是把 (1) 对 3 取模：未选坐标含有显式因子 3，选中坐标都等于同一个和 \(s_S\)。

这个事实比最初的 gcd 条件更有信息：它说明每一步的低位三进数字不是任意向量，而是一个“大小为 3 的支持集加一个标量”。

## 3. 支持集自动机

在一次没有发生整体 3 提升的层上，假设当前本原状态的模 3 形状为
\[
x\equiv t\,\mathbf 1_T\pmod3,
\qquad |T|=3,\quad t\in\{1,2\}.
\tag{3}
\]
下一步选择三元组 \(U\)，令 \(m=|T\cap U|\)。则
\[
\sum_{j\in U}x_j\equiv mt\pmod3.
\tag{4}
\]
所以在“不除以 3”的分支上，支持集层有如下完全有限的转移规则；一旦发生提升，商向量的下一层数字需要额外记录，不能仅由支持集恢复。

| 重叠数 \(m\) | 下一步的三进事件 |
|---|---|
| 0 | 选中和为 0，清分母后的整向量至少多出一个整体 3 因子 |
| 1 | 新状态仍是支持集 \(U\)，标量变为 \(t\) |
| 2 | 新状态仍是支持集 \(U\)，标量变为 \(-t\) |
| 3 | 选中和为 0，进入一次三进提升；支持集层本身不决定商向量 |

这里“提升”指 \(s_U\equiv0\pmod3\)，此时 (1) 中每个分量都含因子 3，可写成
\[
\frac y3=
\begin{cases}
s_U/3,&i\in U,\\
x_i,&i\notin U.
\end{cases}
\tag{5}
\]
公式 (5) 显示：选中三元组产生一个三进进位，而未选坐标的低位数字被原样保留。因而完整状态可以看成“支持集自动机 + 更高三进位的提升系统”。

## 4. 为什么五元是特殊维数

当 \(n=5\) 时，两个三元组不可能不相交。因此在具有非零支持集 (3) 且尚未发生提升的状态中，只有：

* \(m=1,2\)：支持集移动，但不发生整体 3 提升；
* \(m=3\)：只能重新选择同一个支持集，才可能发生提升。

这正是五元闭合递归的来源。三重重复坐标把高阶三进信息压缩到两个差值 \((u,v)\)，而支持集层没有“第三种”不相交选择。此前得到的 A/B 递归实际上是在追踪 (5) 中两条可能的提升路径。

当 \(n\ge6\) 时，存在不相交的三元组 \(U\)。于是从任意非零支持集 \(T\) 都有一个 \(m=0\) 的选择，可以立刻触发一次整体 3 提升；提升后的商向量通常不再保持五元的重数形状。这个自由度解释了为什么五元的二维不变量不能直接推广到一般维数，也说明高维问题的核心不只是“模 3 障碍”，而是不同三进位层之间的耦合。

例如六元状态
\[
(-3,0,0,1,1,1)
\]
的模 3 支持集是后三个位置。选择前三个位置（与支持集不相交）时，清分母状态为
\[
(-3,-3,-3,3,3,3),
\]
整体除以 3 后变成 \((-1,-1,-1,1,1,1)\)。这一步把“支持集信息”全部送入下一组三进位，产生了五元闭合族中不存在的自由度。

## 5. 与二平均的结构对照

二平均的对应公式是
\[
y\pmod2=s_S\,\mathbf1_S,qquad |S|=2.
\]
支持集只有两个位置，重叠数只有 \(0,1,2\)，且中间情形只产生同一个非零余数，不会出现三平均的 \(m=2\) 所对应的符号翻转 \(t\mapsto-t\) 和三元重数约束。更关键的是，二元支持集天然适合成对消去；文献中的安全配对引理正是在更高层三进（或二进）数字上反复寻找这种局部配对。

三平均中，支持集大小等于操作大小，且 \(m=1,2\) 两种重叠都会把支持集改写成新三元组；当 n=5 又没有不相交选择，导致局部提升被迫在同一支持集上完成。这是“2 有简单判据而 3 没有”的结构性原因之一，而不是分母从 2 换成 3 的表面差异。

## 6. 可计算的有限层算法与局限

固定三进精度的抽象需要重新设计。支持集引理确实把清分母后第一层非零形状限制为
\[
2\binom n3+1
\]
种形状（包含零）。但不能直接据此建立有效的有限图否定证书：原始清分母矩阵重复作用，会使任意固定模三幂中的状态人为归零；若每步本原化，除去三因子又需要读取更高位。整体复审第 9 节给出了明确反例。因此，这里仍有支持集结构，但没有已经成立的有限精度否定算法。

## 7. 支持集猜想的反例与修正

原先的宽泛说法“每次非平凡提升都发生在当前支持集或其不相交补集上”并不成立。六元原始状态
\[
x=(-1,-1,0,1,0,1)
\]
有如下两步归零路径：
\[
(-1,-1,0,1,0,1)
\xrightarrow{\{0,2,3\}}
(0,-1,0,0,0,1)
\xrightarrow{\{0,1,5\}}
(0,0,0,0,0,0).
\]
第一步选中和为 0，且当前模 3 支持集为 \(\{0,1,3,5\}\)；选集与支持集交集大小为 2，既非相等也非不相交。第二步同样是三进提升，支持集大小已经变为 2。这说明支持集大小为 3 时的自动机不能直接外推到任意支持集大小。

更稳妥的修正版是：**在当前模 3 支持集恰好为三个位置、且轨道尚未发生高阶提升时，是否总能找到一条最短成功路径，使第一次提升只使用该支持集或其不相交补集？** 这是一个明确的有限状态问题；上面的六元反例不属于该修正版的假设，因为它的初始支持集大小为 4。

## 8. 五元复杂度猜想的严格子结果

令 \(H(u,v)=\max(|u|,|v|)\)。考虑五元递归中连续两步都满足：第一步被除坐标为 \(u=3q\)，且 \(3\nmid q\)。为了第二步继续，必有 \(v\equiv q\pmod3\)，写成 \(v=q+3r\)。两步递归精确变为
\[
(3q,q+3r)\longmapsto (-(q+r),-r).
\tag{6}
\]
并且
\[
H(3q,q+3r)=\max(3|q|,|q+3r|),
\qquad
H(-(q+r),-r)=\max(|q+r|,|r|).
\]
由
\[
|q|\le H/3,
\qquad |r|=|v-q|/3\le (H+H/3)/3=4H/9
\]
得到
\[
H(-(q+r),-r)\le 7H/9.
\tag{7}
\]
所以在“被除坐标的三进赋值恰好为 1”的子类中，每两步都有固定收缩，递归长度为 \(O(\log H)\)。

一般情形的障碍被精确定位：若 \(u=3q\) 且 \(3\mid q\)，第一次操作后会连续消耗 \(q\) 的更高三进因子；这段连续分支的长度最多为 \(1+v_3(q)\)，但其后的整体收缩尚未得到统一证明。换言之，五元位复杂度猜想已经化为一个“高三进赋值运行长度的摊销界”问题，而不再是笼统的范数估计问题。

## 9. 两个当前可检验的研究猜想

1. **条件支持集提升猜想。** 在当前支持集恰为三个位置、且尚未发生高阶提升时，存在一条最短成功路径，其第一次提升使用当前支持集或不相交补集。该命题避开了已知的支持集大小为 4、2 的反例。
2. **五元位复杂度猜想。** 五元递归成功或失败的步数为 \(O(\log H)\)，其中 \(H=\max(|u|,|v|)\)。已证明赋值为 1 的连续两步有固定收缩；剩余任务是证明高 \(3\)-进赋值运行的摊销长度也为对数级。

这两个猜想都比“\(G\) 是 3 的幂就充分”精确得多，并且可以通过有限层枚举和反向三进树继续检验；它们暂时不应被表述为一般充要条件。

## 10. 支持集提升猜想其实是一个定理

前面的条件支持集提升猜想可以直接证明，而且不需要最短性。设当前状态在模 3 下为

\[
x\equiv t\mathbf 1_T,
\qquad |T|=3,\quad t\in\{1,2\},
\]

并假设此前尚未发生提升。对任意三元组 (U)，令 (m=|T\cap U|)。则

\[
\sum_{i\in U}x_i\equiv mt\pmod 3.
\]

所以当且仅当 (m=0) 或 (m=3) 时，选中和为 (0\pmod3)，即发生提升；(m=1,2) 时不会提升，且新状态仍满足同样的形式，支持集变成 (U)，标量变成 (t) 或 (-t)。因此在首次提升以前，支持集永远保持大小 3，而首次提升必然使用当前支持集本身，或与其不相交的三元组。

这说明修正版命题不仅对最短成功路径成立，而是对任意成功路径成立。六元反例不构成矛盾，因为它的初始支持集大小为 4；一旦支持集大小不再等于 3，交叠数 (m=2) 也可能给出提升后的高阶状态。

## 11. 五元递归的严格平方对数上界

考虑五元递归中的本原非停机状态 ((u,v))，交换坐标后设

\[
u=3^k t,qquad 3\nmid t,qquad 3\nmid v,qquad k\ge1.
\]

从这个状态开始，先执行一次 A，随后连续执行 (k-1) 次 B。直接求和可得这个三进级联的终点

\[
(u,v)\longmapsto (v-\alpha_k u,\,\beta_k u),
\tag{10}
\]

其中

\[
\alpha_k=\frac{3^k+(-1)^{k-1}}{4\,3^k}
      =\frac14+\frac{(-1)^{k-1}}{4\,3^k},
\qquad
\beta_k=\frac{(-1)^k}{3^k}.
\tag{11}
\]

因而 (0<\alpha_k\le1/3)、(|\beta_k|\le1/3)。级联终点的第二坐标恰为 (\pm t)，所以若轨迹继续，下一次级联只能从第一坐标开始。设连续两个级联的参数为 (k,\ell)，由两次复合得

\[
|u_2|\le \frac49|u|+\frac13|v|,
\qquad
|v_2|\le \frac19|u|+\frac13|v|.
\]

令 (H(u,v)=\max(|u|,|v|))，便有

\[
H(u_2,v_2)\le\frac79 H(u,v).
\tag{12}
\]

单个级联还满足 (H_{\rm next}\le\frac43H_{\rm current})；结合 (12)，偶数编号级联的起点幅度按 (7/9) 几何下降，奇数编号至多多一个 (4/3) 因子。因此所有级联起点都满足 (H_i\le\frac43H_0)。每个级联的长度是 (k)，且 (3^k\le2H_0)，故单个级联长度至多 (O(\log H_0))；而每两个级联至少收缩一次，级联总数至多 (O(\log H_0))。于是

\[
\boxed{\text{五元递归的成功或失败轨迹长度为 }O((\log H)^2).}
\]

这给出了输入位长意义下的多项式时间上界：直接模拟确定性递归即可在平方对数次大整数步骤内完成。尚未解决的是把平方对数压缩为 (O(\log H))，这需要一个同时计数范数与三进赋值的更精细摊销势函数。

## 12. 结论边界

支持集大小为 3 的首次提升结构已经完全确定，但这不是任意支持集大小的自动机。五元递归的平方对数结果解决了位复杂度的多项式性，却仍不能推出一般 (n\ge6) 的多项式算法；高维状态在首次提升后不再保持二维重数闭合。一般问题仍需要新的高阶三进状态不变量，或一个能控制提升深度的统一定理。

<!-- END SOURCE doc-ad82640623de -->

---

<a id="doc-66e3f48a55d6"></a>

## 原文导签：所有偶维 B 核的统一减半定理

来源：`outputs/triple_average/history/triple_average_all_even_B_kernel_halving.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_all_even_B_kernel_halving.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`all-even-B-kernel-halving`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-66e3f48a55d6 -->
# 所有偶维 B 核的统一减半定理

本定理只处理 B 核，不能省略一般输入进入 B 核的高维桥。

## 1. 主定理

设 n 是偶数，\(n\ge14\)。任何合法
\[
\mathcal B_n(u,v)=(u^{n-4},v^3,w),\qquad w=-(n-4)u-3v
\]
都可经至多一次预备三平均，调用一个合法八元或十二元子问题，形成每种重数全偶的零和状态。其重数减半后的 \(n/2\) 元状态仍合法。

因此，若 \(n/2\) 维的完整 G 判据已证明，则全部合法 B_n 也可解。这里的调用是由已证子程序实现的有限三平均词，不是新增八平均或十二平均。

\(n=2\pmod4\) 的情形已由[八元减半桥](../sources/outputs/triple_average/history/triple_average_even_kernel_halving_bridge.md)证明，且预备操作至多一次。下面给出 \(4\mid n\) 的单一模板。

## 2. 四整除情形的单一模板

取本原整数参数 u、v，合法性要求 \(\gcd(u-v,n)\) 为三幂，故 u、v 奇偶相反，并对每个非三素数 \(p\mid n\) 模 p 不同。

先平均 \((w,u,u)\)，得
\[
a=-\frac{(n-6)u+3v}{3}.
\]
状态变成 \((u^{n-6},v^3,a^3)\)。因为 n至少16，有十个 u 可用于
\[
C=(u^{10},v,a).
\]
其大小12、均值
\[
\mu=\frac{10u+v+a}{12}
=\frac{36-n}{36}u=\frac{9-n/4}{9}u\in\mathbb Z[1/3].
\tag{1}
\]
C 含奇偶不同的 u、v，均值只有三进分母。中心化、清分母、本原化后 G 为奇数且整除12，所以是1或3；十二元完整定理保证 C 可有限步归并。

归并后的全部状态为
\[
(\mu^{12},u^{n-16},v^2,a^2).
\tag{2}
\]
各重数均为偶数，总和保持为零。重数减半得到
\[
Y=(\mu^6,u^{n/2-8},v,a),\qquad\sum Y=0.
\tag{3}
\]

## 3. 局部合法性

若 \(n\ge20\)，式(3)中 u、v 均保留；它们对每个 \(p\mid n/2,\ p\ne3\) 都不同余，故 Y 中心化（本来零和）、清三进分母、本原化后仍合法。

若 n=16，u 的独立重数消失，但
\[
\mu=\frac59u,\qquad a=-\frac{10u+3v}{3}.
\]
模2下 \(\mu=u\)，与保留的 v 奇偶相反；\(n/2=8\) 只有非三素数2，因此仍合法。这个边界不能通过“u一直被保留”处理。

把(2)每种值分成两份相同副本，即得到两个不交的 Y。若 Y 可解，分别对两份运行其真实算法即可归零，既没有二平均也没有增加位置。

## 4. 为什么八整除版本不直接外推

先前模板平均 \((w,u,v)\)，再选择 \((u^9,v^2,a)\)，其输出只保留 u、a 和新均值。它对八整除 n 有正确的二处见证；对四整除但不被八整除的某些参数会失去奇偶差异。

本模板改成平均 \((w,u,u)\)，始终保留两份 v（除数值恰合并的无害情况）。因此 n至少20时直接用原 u、v 保护全部素数，无需为每个新素数增加联合余数枚举。这是输入子问题接口层面的改进，不依赖更大的宏群搜索。

## 5. 与任意维数目标的关系

本定理证明的是条件蕴含
\[
\mathsf A(n/2)\Longrightarrow
\text{所有合法 B_n 可达}.
\]
它没有证明 \(\mathsf A(n/2)\Rightarrow\mathsf A(n)\) 对任意偶 n 成立，因为多危险素数输入的高维桥可能停在不交支持集。

单一非三素数是2时，已证安全核心提供 B 核入口，所以本定理与8、12、18三个起点可再次证明全部 \(2^a3^b\ge7\) 的[二三光滑定理](../sources/outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md)。

例如 B20、B28、B30、B32、B36 可分别调用已证的10、14、15、16、18维判据。不能仅凭这些结构核宣称一般20或28维数已解决：28不是14乘三幂，一般输入仍需独立高维入口。

## 6. 核验

work/verify_dyadic_kernel_halving.py 的新增 four_divisible_bridge 对15个 n（16至2048，包含多个奇素因子的420）检查子块实际选取、均值、中心化 G、重数和压缩后 G。只保存少数不同值，不按大 n 展开。一般 n 的结论来自上面的符号账本与保持 u、v 的证明，有限实例仅核对实现。

<!-- END SOURCE doc-66e3f48a55d6 -->

---

<a id="doc-82e0619e54b5"></a>

## 原文导签：三平均任意维数的全局视角：有限基维数究竟说明了什么

来源：`outputs/triple_average/history/triple_average_arbitrary_n_outlook.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_arbitrary_n_outlook.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-82e0619e54b5 -->
# 三平均任意维数的全局视角：有限基维数究竟说明了什么

> **2026-09-09 更新：** 十三元及其三进塔已经完整解决；任意输入也已统一压到对数秩三幂核。最新的 Burau 幂链定理进一步证明等比三幂链上的正向宏对任意秩自动群化。本文保留此前阶段的路线判断；当前结论与开放问题以 [最新交接总览](../sources/outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md) 为准。

> **更新：** 任意维数的复制稳定化已经证明，详见 [稳定化定理](../sources/outputs/triple_average/history/triple_average_stabilization_theorem.md)。本文“判定与构造”一节所列的额外复杂度条件针对输出操作路径；如果原问题的 gcd 充要性成立，单纯的多项式时间判定就已成立。完整勘误见 [研究复核](../sources/outputs/triple_average/history/triple_average_research_corrections.md)。

## 结论先行

目前不能把“\(G(X)\) 是 \(3\) 的幂”宣布为所有维数的充要条件。严格已知的是：

* \(G(X)\mid n\)，且可达性必然要求 \(G(X)=3^s\)；
* \(n=3^k\) 时有固定的三进张量网络；
* \(n=7,8,10,11\) 时，\(G(X)=1\) 已分别得到完整证明；
* 由三进等块提升，以上结论传播到
  \[
  n=3^k,\qquad n=m3^k\quad(m\in\{7,8,10,11\});
  \]
* \(n=5,6\) 存在 \(G=1\) 的不可达状态，所以阈值若存在不能低于 \(7\)。

因此，当前成果已经解决了无限多个维数，但还没有解决任意可变 \(n\)。真正未解决的不是三进部分，而是

\[
n=3^{v_3(n)}m,\qquad 3\nmid m,
\]

中的三进无关基维数 \(m\)。

## 有限维数结果已经统一了哪一部分

三进等块压缩给出一个严格的传播定理。把 \(n=mr\) 个位置分成 \(m\) 个大小为 \(r=3^k\) 的块，先在每个块内求平均，再在块之间模拟 \(m\) 元操作。非 \(3\) 素数的同余障碍可由块交换同时修复。因此

\[
\mathsf A(m)\Longrightarrow \mathsf A(3^km),
\]

其中 \(\mathsf A(m)\) 表示“所有满足 \(G=3^s\) 的 \(m\) 元状态可达”。这不是四个孤立例子的并列，而是四个完整的三进塔。

但这个压缩只有充分方向。一个 \(3^km\) 元状态可以通过打破块对称的操作成功，不能反向压缩成 \(m\) 元状态；同样，\(5,6\) 元反例也不能简单复制成高维反例。因此，已知维数并没有给出任意 \(m\) 的判据，却把问题精确地缩小到“研究三进无关的基维数”。

这已经是实质性进展：若 \(m\) 被解决，整条 \(m3^k\) 塔自动解决；但它还不是“有限个基维数足以覆盖所有 \(n\)”的定理。

## 一个新的十三元局部结果

十三元是第一个没有被现有基维数证书覆盖、且没有小维数特殊退化的自然测试点。这里可以把下一步拆得更细。

### 六重安全核心

对十三元本原零和整数状态，假设没有保持 \(G=1\) 的非恒等整数三平均。唯一的非三素数障碍是 \(13\)。若某个模 \(13\) 类没有至少 \(10\) 个位置，则任意三元组的补集都保留两个模 \(13\) 类；于是“无安全操作”只可能来自模 \(3\) 的组合结构。模 \(3\) 至多出现两个类，而每个出现至少三次的类必须由同一个实际值组成，所以立即得到至少六重值。

剩下的边界是某个模 \(13\) 类恰有 \(10\) 个位置。其补集 \(F\) 至多三个位置，设 \(K\) 是这十个以上的主类。若 \(|F|\le2\)，则 \(|K|\ge11\)，同样得到六重值。若 \(|F|=3\)，要避免六重值，\(K\) 只能按两个模 \(3\) 类分成 \(5+5\)，且两类各自为常值 \(a,b\)。把模 \(3\) 重标成 \(0,1,2\)，则对任意 \(f\in F\)：

* \(f\equiv0\) 时，三元组 \((f,a,a)\) 必须恒等，故 \(f=a\)；
* \(f\equiv1\) 时，\((f,b,b)\) 必须恒等，故 \(f=b\)；
* \(f\equiv2\) 时，\((f,a,b)\) 是安全三元组，矛盾。

所以 \(F\) 中只能出现 \(a,a,b\) 型值，这反过来产生至少 \(6\) 或 \(7\) 重值，矛盾。由此得到：

> **十三元六重核心命题。** 若十三元本原状态 \(G=1\) 没有安全整数三平均，则某个实际值至少出现六次。

这一步把一般安全核心在 \(n=13\) 的下界从通用的 \(5\) 提高到了 \(6\)。它说明安全核心估计还可以利用“唯一危险素数”的具体结构来加强，而不必满足于 \(n/2-O(\log n)\) 的粗界。

### 六重层到二维核的五步桥

设状态为

\[
X=(u^6,a_1,a_2,a_3,a_4,a_5,a_6,a_7),
\qquad 6u+\sum_{i=1}^7a_i=0.
\]

选两个不交的三元组 \(A,B\)，余下一个值记为 \(h\)。依次做：

1. 把 \(A\) 平均为 \(q^3\)；
2. 连续三次取 \((q,u,u)\)，得到 \(r^9\)，其中
   \[
   r=\frac{\sum A+6u}{9};
   \]
3. 把 \(B\) 平均为 \(s^3\)，其中 \(s=\sum B/3\)。

最后得到

\[
(r^9,s^3,h),\qquad h=-9r-3s,
\]

即十三元终端核

\[
\mathcal B_{13}(r,s)=(r^9,s^3,-9r-3s).
\]

还可以保证这一步合法。事实上

\[
9(r-s)=\sum A+6u-3\sum B=-(4\sum B+h).
\]

只需选择 \(B,h\) 使 \(4\sum B+h\not\equiv0\pmod{13}\)。七个例外值不可能全模 \(13\) 相同，否则由

\[
6u+7t\equiv0\pmod{13}
\]

得到 \(u\equiv t\)，从而 \(G\) 被 \(13\) 整除。故例外值中存在两个不同的模 \(13\) 类；选 \(B\) 避开这两个位置，补集中的两个候选 \(h\) 使上式不可能同时为零。

这给出一个很具体的结论：十三元的高维桥并不是主要障碍，剩下的是二维核的统一下降控制。对

\[
x=r,\qquad y=9r+4s,
\]

有

\[
4E=117x^2+3y^2,\qquad y\equiv9x\pmod4,\qquad G=1\Longleftrightarrow13\nmid y.
\]

因此十三元下一步可以精确表述为：构造真实平均词产生的返回半群，在上述参数格上覆盖所有 \(13\nmid y\) 的射影方向，并使相应的 adelic 高度严格下降。

## 为什么这不是“永无止境的特殊情况”

有限维数证书反复出现同一三层结构：

\[
\text{安全整数下降}
\longrightarrow
\text{高重数平坦}
\longrightarrow
\text{二维正交补}
\longrightarrow
\text{实方向与有限素数局部下降}.
\]

七、八、十、十一元的差异主要在最后两层的参数格和返回半群，不在基本几何。终端族的一般形式始终是

\[
\mathcal B_n(u,v)=(u^{n-4},v^3,-(n-4)u-3v),
\]

其正交补统一带有二次型

\[
Q_n(x,y)=n(n-4)x^2+3y^2,
\qquad y\equiv(n-4)x\pmod4.
\]

所以继续研究的对象不应是“再找一个维数的偶然操作序列”，而应是两个统一命题：

1. **统一高重数桥定理：** 对所有 \(n\ge7\)，无安全操作时得到足够强的重数层，并把它送入有限个可控的低秩核；
2. **统一二维控制器定理：** 对这些核，返回半群在有限局部签名和实射影方向上存在严格下降覆盖。

一旦这两个命题成立，有限维数只需要作为小范围边界证书；不需要逐个处理所有 \(n\)。目前十一元已经完整验证了这套分解，十三元的六重桥又表明第一层可以随危险素数结构加强。

## 判定结论与多项式算法必须分开

即使最终证明

\[
n\ge7,\qquad G(X)=3^s
\Longleftrightarrow\text{可达},
\]

这仍不自动给出可变 \(n\) 的多项式时间构造算法。还需分别控制：

* 高重数桥的描述长度和操作次数关于 \(n\) 的增
* 长；
* 二维控制器的局部签名数，及其关于 \(n\) 的生成复杂度；
* adelic 高度下降次数关于输入坐标位长的增长。

当前已经可以严格给出的统一算法范围是：计算 \(G\)，令 \(m=n/3^{v_3(n)}\)，若 \(m\in\{1,7,8,10,11\}\)，则判定只需检查 \(G\) 是否为 \(3\) 的幂。对其余 \(m\)，我们有统一必要条件、三进传播机制、一般安全核心和二维终端模型，但还没有完整判定算法。

因此，有限元成果的正确定位是“统一理论的实验室和归纳基底”，而不是最终答案，也不是无休止的特例清单。真正的突破点已经从“证明更多固定维数”转为“证明高重数桥与二维控制器的参数化定理”。

<!-- END SOURCE doc-82e0619e54b5 -->

---

<a id="doc-47a119cd7ff0"></a>

## 原文导签：三平均的算术几何结构：射影投影、二次型与 adelic 高度

来源：`outputs/triple_average/history/triple_average_arithmetic_geometry_view.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_arithmetic_geometry_view.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`general-lifting`, `arithmetic-geometry-structure`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-47a119cd7ff0 -->
# 三平均的算术几何结构：射影投影、二次型与 adelic 高度

> **2026-09-09 更新：** 十三元有限尖点法已经闭合，随后发现的 Burau 幂链定理把三阶分圆元推广到任意参数秩。本文的 adelic 高度框架仍有效；最新高秩路线与九十一元同余修正见 [最新交接总览](../sources/outputs/triple_average/history/triple_average_research_handoff_2026-09-09.md)。

## 0. 结论与定位

三平均确实有很自然的代数几何结构，但真正控制可达性的不是单独的复代数簇，而是

$$
\boxed{\text{定义在 }\mathbb Z[1/3]\text{ 上的射影投影半群}
+\text{整数格}
+\text{各素数处的局部条件}
+\text{实高度下降}.}
$$

复射影几何解释每一步在消去什么、为什么高重数状态落到射影直线、以及为什么有限步可达集是线性子空间的有限并。算术几何进一步解释：非 $3$ 素数给出良约化纤维和同余障碍，$3$ 是产生分母的坏约化位置，而二维终端核上的真实下降必须同时利用实方向和 $p$ 进约分。

这一视角给出一个新的严格结论。设 $n\ge3$，只考察本原中心化、$G=1$ 的有理状态，并把不可达状态的最短步数记为无穷。它们的最坏最短步数恰为

$$
\boxed{
L_n=
\begin{cases}
k3^{k-1},&n=3^k,\\
\infty,&n\ne3^k.
\end{cases}}
\tag{0.1}
$$

第二行的含义比“不存在固定通用序列”更强：即使允许针对每个输入自适应地选择不同序列，非三幂维数也没有统一的常数步数上界。在已解决的 $7,8,10,11$ 以及 $7\cdot3^r,8\cdot3^r,10\cdot3^r,11\cdot3^r$ 维中，所有合法输入确实可达，因此这些维数中存在最短成功路径任意长的输入族。

本稿严格区分以下三类内容。

* 第 1--6 节是证明或直接代数推导。
* 七元与十元的有限覆盖是已经独立核验的计算机辅助定理；八元是初等欧几里得型证明。
* 第 9--10 节提出的统一返回半群方案和一般桥定理仍是研究纲领或猜想。

## 1. 每一步是 $A_2$ 根平面的正交投影

中心化有理空间为

$$
V_n=\left\{x\in\mathbb Q^n:\sum_i x_i=0\right\},
\qquad L_n=V_n\cap\mathbb Z^n=A_{n-1}.
$$

固定 $S=\{i,j,k\}$，令

$$
\alpha=e_i-e_j,\qquad \beta=e_j-e_k,
\qquad B_S=(\alpha\ \beta).
$$

这两个根的 Gram 矩阵是 $A_2$ Cartan 矩阵

$$
C=B_S^TB_S=
\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\qquad
C^{-1}=\frac13
\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$

三平均算子恰为

$$
\boxed{P_S=I-B_SC^{-1}B_S^T.}
\tag{1.1}
$$

所以 $P_S$ 是沿着

$$
K_S=\operatorname{span}\{\alpha,\beta\}\cong A_2\otimes\mathbb Q
$$

投影到 $K_S^\perp$ 的正交投影。式 (1.1) 同时解释三件事：一次操作消去两个差分自由度；平方能量严格下降；矩阵系数只产生 $3$ 的幂分母。这里的 $3$ 不是偶然来自平均公式，而是局部根格 $A_2$ 的判别式。

把 $V_n$ 射影化，得到

$$
\mathbb P(V_n)\cong\mathbb P^{n-2}.
$$

$P_S$ 诱导一个有理线性映射

$$
[P_S]:\mathbb P(V_n)\dashrightarrow
\mathbb P(K_S^\perp)\cong\mathbb P^{n-4},
$$

其不定中心为 $\mathbb P(K_S)\cong\mathbb P^1$，像空间就是辫状排列

$$
x_i=x_j=x_k
$$

的余维二平坦。这个线性投影的图闭包是沿 $\mathbb P(K_S)$ 的 blow-up；它解析了单步射影映射的不定性。这里的 blow-up 描述的是单个生成元，不意味着整个半群已经被一个有限 blow-up 同时解析。

## 2. 有限步可达集是射影线性排列

令一个词 $w=S_1\cdots S_r$ 表示依次执行这些三平均，并记

$$
P_w=P_{S_r}\cdots P_{S_1}.
$$

中心化状态 $x$ 沿词 $w$ 到达零，当且仅当 $x\in\ker P_w$。因此至多 $L$ 步可达的射影状态集合为

$$
\boxed{
R_L=\bigcup_{|w|\le L}\mathbb P(\ker P_w).
}
\tag{2.1}
$$

对固定 $n,L$，词只有有限多个，所以 $R_L$ 是有限个有理线性子空间的并，因而是 Zariski 闭集。这给出了一个很直接的代数几何分层：

$$
R_0\subseteq R_1\subseteq R_2\subseteq\cdots,
\qquad
R_\infty=\bigcup_{L\ge0}R_L.
$$

总可达集是可数个线性闭集的递增并。可达性本身是“存在某个词”的无限并问题，不是一个固定次数多项式方程组的零点集。

这个观察还能把“固定通用词”和“自适应但步数一致有界”联系起来。若所有某类 Zariski 稠密的输入都能在至多 $L$ 步完成，则 $R_L$ 包含稠密集，只能等于整个 $\mathbb P(V_n)$。射影空间不可约，而 $R_L$ 是有限个线性子空间的并，所以其中必有一个 $\mathbb P(\ker P_w)$ 等于整个空间；也就是说，某一个固定词已经对所有输入通用。

## 3. 通用词与最坏步数的精确三幂分界

### 3.1 固定通用词只存在于三幂维数

每个 $P_S$ 的矩阵系数属于 $\mathbb Z[1/3]$，所以任何 $P_w$ 也属于

$$
M_n(\mathbb Z[1/3]).
$$

若一个词消灭整个 $V_n$，它又固定常数向量并保持坐标和，则在整个 $\mathbb Q^n$ 上必须等于

$$
P_w=\frac1nJ_n,
\tag{3.1}
$$

其中 $J_n$ 是全 $1$ 矩阵。式 (3.1) 的条目 $1/n$ 属于 $\mathbb Z[1/3]$ 当且仅当 $n=3^k$。反过来，若 $n=3^k$，标准三进张量网络确实把任意输入变成全局平均。

因此：

> **通用词定理。** 存在一个与输入无关的有限三平均序列，能对所有 $n$ 元输入求出全局平均，当且仅当 $n=3^k$。

### 3.2 $G=1$ 有理射线是 Zariski 稠密的

令 $N=\operatorname{rad}(n)$，取

$$
a=(1,-1,0,\ldots,0)\in L_n.
$$

考虑满秩格陪集

$$
\mathcal C=a+NL_n.
$$

对每个 $p\mid n$，$\mathcal C$ 中任一点的坐标模 $p$ 不全相同。把这样的点除以坐标 gcd 后，除数也不可能被 $p$ 整除，所以本原代表仍然模 $p$ 不全相同。又因本原零和向量总满足 $G\mid n$，故这些射线全部满足 $G=1$。

任何在满秩格陪集上恒为零的有理多项式都只能是零多项式。因此 $\mathcal C$ 的射影像、从而 $G=1$ 的有理射线，在 $\mathbb P(V_n)$ 中 Zariski 稠密。

### 3.3 自适应有限步也不能绕过分母障碍

若 $n$ 不是三的幂，通用词定理说明每个 $\ker P_w$ 都是 $V_n$ 的真子空间。因此每个 $R_L$ 都是真 Zariski 闭集。由上一节的稠密性，对每个 $L$ 都存在一个 $G=1$ 输入不在 $R_L$；它要么不可达，要么最短路径超过 $L$。

若 $n=3^k$，标准网络使用

$$
k3^{k-1}=\frac n3\log_3n
\tag{3.2}
$$

步。这个数也是最优的。把当前线性变换的每一行看成初始坐标上的概率分布，并令各行 Shannon 熵之和为 $\Phi$。初始 $\Phi=0$，全平均矩阵的 $\Phi=n\log n$。一次三平均把三行 $p,q,r$ 替换为 $s=(p+q+r)/3$；混合熵不等式给出

$$
H(s)\le\frac{H(p)+H(q)+H(r)}3+\log3,
$$

所以每步最多使 $\Phi$ 增加 $3\log3$。任何通用词至少需要式 (3.2) 的步数。

结合第 2 节的不可约性论证可得开头的公式 (0.1)：如果所有 $G=1$ 输入都有一个更小的统一自适应上界，那么有限个短词的核会覆盖稠密集，从而其中某个短词已经通用，与熵下界矛盾。

这也澄清一个算法学边界。非三幂维数没有常数步数上界，并不排除关于输入位长的多项式路径，也不排除只计算 gcd 的多项式时间判定；七、八、十元正是“判定很短，成功证书长度仍随数值增长”的情形。

## 4. 为什么纯复代数几何看不见完整判据

式 (1.1) 应当放在基底

$$
\operatorname{Spec}\mathbb Z[1/3]
$$

上理解。对每个 $p\ne3$，生成元可以良好地约化到 $\mathbb F_p$；在 $p=3$ 处，$C^{-1}$ 不再整，正是坏约化位置。

若 $p\mid n$，模 $p$ 的中心化空间中包含非零对角线

$$
\{(c,\ldots,c):c\in\mathbb F_p\}\subset V_n(\mathbb F_p).
$$

每个平均投影都逐点固定这条线。若本原状态的所有坐标模某个 $p\ne3$ 都等于同一非零 $c$，其轨道不可能到达零。这正是 $p\mid G$ 的局部障碍。

但 $G=1$ 点已经 Zariski 稠密；在七、八、十元，它们又全部可达。因此把问题基变换到 $\mathbb C$ 后，合法点和许多非法点都具有相同的 Zariski 闭包。纯复几何只看到线性投影与辫状排列，看不到本原化、模 $p$ 共同余数或 $3$ 进约分。

更准确的对象是：

$$
\text{射影半群动力系统}/\mathbb Z[1/3]
$$

连同它在各个 $\mathbb Z_p$ 上的积分结构。$p\ne3$ 控制不变量与合法性，$p=3$ 控制分母和压缩，实位置控制能量是否下降。

## 5. 辫状排列的重数平坦与二维终端核

坐标相等模式由集合分拆编码，它们正是 $A_{n-1}$ 辫状超平面排列的平坦。一次平均把状态送入一个含三元块的平坦；后续操作在分拆格中合并、打破或重建相等块。

令 $m=n-4$。终端族

$$
\mathcal B_n(u,v)=
(\underbrace{u,\ldots,u}_{m},v,v,v,-mu-3v)
\tag{5.1}
$$

位于重数型 $(m,3,1)$ 的平坦闭包中。块内差分给出正交根子系统

$$
A_{m-1}\oplus A_2\subset A_{n-1},
$$

其秩为 $n-3$，所以在 $V_n$ 中的正交补恰为二维。射影化后，(5.1) 的非零状态组成一条 $\mathbb P^1$。这说明七、八、十元证明最终出现二参数族并非搜索偶然，而是高重数层的正交余维决定的。

一般安全核心定理已经证明：若合法本原状态没有安全整数下降，则某个实际值至少出现

$$
\left\lceil\frac{n-3\omega_{\ne3}(n)}2\right\rceil
=\frac n2-O(\log n)
$$

次。几何上，这意味着轨道有限步后进入辫状排列中很深的高重数平坦。当前缺口是一个分拆格中的桥定理：把这个约 $n/2$ 重层继续导向有限个可控制的秩二正交补，尤其是 $(n-4,3,1)$ 层。

因此一般问题的高维部分可以重新表述为：寻找保持所有非 $3$ 局部见证的投影词，使轨道沿辫状排列的平坦格进入二维算术曲线。

```mermaid
flowchart LR
    A[根格 A_{n-1} 上的射影状态] -->|安全 A_2 投影| B[辫状排列的高重数平坦]
    B -->|有限桥词| C[二维核 B_n / 射影直线 P^1]
    C -->|真实返回宏| D[实方向与有限 p 进圆柱]
    D -->|adelic 高度严格下降| C
    C -->|零坐标或零和三幂块| E[全零]
```

## 6. 二元二次型、虚二次序及其限度

在 $(u,v)$ 坐标中，(5.1) 的平方能量是

$$
E_n(u,v)=m(m+1)u^2+6muv+12v^2.
\tag{6.1}
$$

其判别式为

$$
\Delta_{\rm raw}=(6m)^2-4m(m+1)\cdot12
=-12n(n-4).
\tag{6.2}
$$

令

$$
c_m=\gcd\bigl(m(m+1),6m,12\bigr).
$$

把 (6.1) 除以内容 $c_m$，便得到一个本原正定二元二次型；其判别式为 $-12n(n-4)/c_m^2$。前几个维数如下。

| $n$ | 本原二次型 $[a,b,c]$ | 判别式 |
|---:|---:|---:|
| 5 | $[1,3,6]$ | $-15$ |
| 6 | $[1,2,2]$ | $-4$ |
| 7 | $[2,3,2]$ | $-7$ |
| 8 | $[5,6,3]$ | $-24$ |
| 9 | $[5,5,2]$ | $-15$ |
| 10 | $[7,6,2]$ | $-20$ |
| 11 | $[28,21,6]$ | $-231$ |

本原正定二元二次型按 $\mathrm{SL}_2(\mathbb Z)$ 等价分类，与判别式为 $\Delta$ 的虚二次序的理想类对应。因此 Gauss 约化、理想类群、局部邻接图和 Hecke 型对应，确实可以为二维核提供候选坐标与候选小行列式变换。

但判别式或类数本身不可能决定三平均可达性。

* $n=5$ 与 $n=9$ 都得到判别式 $-15$；五元存在 $G=1$ 的闭合陷阱，九元却有固定三进网络对所有输入求平均。
* $n=6$ 的判别式是 $-4$，对应类数一的高斯整数情形，但仍有 $(-3,0,0,1,1,1)$ 这样的不可达状态。
* 返回宏通常既不是二次型的整数自同构，也不是相似变换。十元七个下降宏中没有一个满足 $M^T\operatorname{diag}(5,1)M=\lambda\operatorname{diag}(5,1)$。

原因是二次型只记录二维平坦上的度量；它没有记录哪些 $2\times2$ 有理矩阵能由真实的坐标重数操作实现。真正的动力学对象还必须包含“可实现返回半群”。

## 7. 参数格与 adelic 能量高度

采用统一正交坐标

$$
x=u,\qquad y=mu+4v,
$$

则参数格为指数 $4$ 的子格

$$
\Lambda_n=\{(x,y)\in\mathbb Z^2:y\equiv mx\pmod4\},
\tag{7.1}
$$

并有

$$
4E_n=Q_n(x,y),
\qquad Q_n(x,y)=mnx^2+3y^2.
\tag{7.2}
$$

为了把射影方向和本原状态精确对应，取标准格中的本原向量 $z=(a,b)$，并令

$$
h_n(z)=\frac4{\gcd(4,b-ma)}\in\{1,2,4\}.
\tag{7.3}
$$

这是使 $h_n(z)z\in\Lambda_n$ 的最小正整数；对应的 $(u,v)$ 自动本原。于是定义

$$
\boxed{\mathcal H_n([z])=h_n(z)^2Q_n(z)=4E_n(u,v).}
\tag{7.4}
$$

它是射影有理点上的正整数高度。合法条件也可写成有限局部条件，因为

$$
u-v=\frac{h_n(z)(na-b)}4,
\qquad
G(\mathcal B_n(u,v))=\gcd(u-v,n).
\tag{7.5}
$$

现在设一个真实返回宏在 $\mathbb P^1$ 上由本原整数矩阵

$$
M=\begin{pmatrix}r&s\\t&q\end{pmatrix},
\qquad \det M\ne0
$$

表示。令

$$
g_M(z)=\gcd((Mz)_1,(Mz)_2),
\qquad z'=\frac{Mz}{g_M(z)}.
$$

因为 $z$ 本原，伴随矩阵恒等式给出

$$
\boxed{g_M(z)\mid\det M.}
\tag{7.6}
$$

输出高度恰为

$$
\boxed{
\mathcal H_n(M[z])
=\frac{h_n(z')^2Q_n(Mz)}{g_M(z)^2}.
}
\tag{7.7}
$$

式 (7.7) 把此前证明中看似分散的量统一起来：$Q_n(Mz)$ 是无穷处的实伸缩，$g_M(z)$ 是所有有限素数处产生的共同因子，$h_n(z')$ 是参数格在 $2$ 处的积分尺度。

更明确地，令

$$
\|w\|_p=\max(|w_1|_p,|w_2|_p).
$$

对整数向量 $Mz$，有

$$
\prod_{p<\infty}\|Mz\|_p^2=\frac1{g_M(z)^2}.
$$

所以 (7.7) 是一个真正的局部--整体乘积：

$$
\mathcal H_n(M[z])
=h_n(z')^2Q_{n,\infty}(Mz)
\prod_{p<\infty}\|Mz\|_p^2.
\tag{7.8}
$$

严格说，$\mathcal H_n$ 是由正定二次范数和参数格局部度量给出的平方高度；它与通常的 Weil 高度平方可比。称它为 adelic 能量高度，能够准确表达其用途，而无需声称已有一个更强的算术动力系统高度定理。

## 8. “多项式覆盖”为何自然出现

对固定宏 $M$ 和固定局部类型，$h=h_n(z)$、$g=g_M(z)$、$h'=h_n(z')$ 都是常数。严格下降条件由 (7.7) 化为

$$
D_{M,\sigma}(z)
=h^2g^2Q_n(z)-h'^2Q_n(Mz)>0.
\tag{8.1}
$$

$D_{M,\sigma}$ 是二元齐次二次多项式。写斜率 $\tau=b/a$ 后，它变成一个次数至多二的单变量多项式。因此一个宏在 $\mathbb P^1(\mathbb R)$ 上的下降区间，边界最多由两个二次代数数给出。七元和十元证明中的“隔离所有实根、在区间内检查符号”，不是搜索技巧，而是射影直线上的二次半代数几何必然给出的有限胞腔分解。

局部部分同样是有限的。对一个有限宏集，只有以下素数需要记录：

$$
S=\{2\}\cup\{p:p\mid n\}\cup
\{p:p\mid\det M\text{ for some macro }M\}.
\tag{8.2}
$$

若 $p\nmid\det M$，本原 $z$ 在 $p$ 处不会使 $Mz$ 同时被 $p$ 整除。式 (7.3) 只依赖 $2$ 进余数，式 (7.5) 的合法性只依赖 $p\mid n$ 的有限余数，而 (7.6) 把约分指数限制在行列式的素因子中。因此足够深但有限的模数就能确定每个宏的局部签名。

这给出一个严格的抽象证明原则。

> **有限 adelic 控制器定理。** 设有有限个真实返回宏。若合法射影方向能按有限局部签名分块，并且在每个局部块与每个非终端实方向上，至少有一个保持合法性的宏满足 (8.1)，而未覆盖方向都属于显式可达终端集，则所有合法 $\mathcal B_n$ 状态均可达零。

证明只是迭代选择下降宏：正整数 $\mathcal H_n$ 每次严格下降，故有限步后必须进入终端集。验证一个给定证书只需有限剩余类计算和二次多项式的精确实根隔离。

在 $p$ 进几何中，$\mathbb P^1(\mathbb Q_p)$ 是 Bruhat--Tits 树的边界；模 $p^r$ 的本原射影类就是边界上的有限深度圆柱。于是十元模

$$
96=2^5\cdot3
$$

得到的十二种签名，可以理解为 $p=2,3$ 两棵树边界上的有限圆柱分块；实根隔离处理 $\mathbb P^1(\mathbb R)$。七元、八元、十元可统一解释为一类 $S$-算术继续分数算法：

* 七元用 18 个词覆盖五种 $3$ 进签名和全部实方向；
* 八元的两个反射生成平移，再用一个折叠宏严格降低欧几里得余数；
* 十元用七个宏覆盖十二种 $2,3$ 进签名和实方向，唯一例外是显式终点。

“有限 adelic 控制分块”是已经证明的准确表述。只有进一步验证每个分块在所选宏下转入哪些分块，才应称为完整的 Markov 分割。

## 9. 真正应分类的是返回半群，而非单个二次型

定义二维核的真实返回半群

$$
\mathcal M_n=
\left\{[M_w]\in\operatorname{PGL}_2(\mathbb Q):
w\text{ 在符号参数上把 }\mathcal B_n
\text{ 送回其某个坐标置换}\right\}.
\tag{9.1}
$$

“在符号参数上”排除了只在某个偶然数值点发生的重数碰撞。每个元素都必须附带一条真实三平均词，因而自动包含中间阶段的重数可实现性。奇异的直接终止词可作为 $\mathcal M_n$ 之外的终端对应单独记录。

对二维核，较完整的算术动力学数据不是判别式 $\Delta_n$，而是

$$
\boxed{
\mathscr D_n=(\Lambda_n,Q_n,\Omega_n,\mathcal M_n,\mathcal T_n),
}
\tag{9.2}
$$

其中 $\Omega_n$ 是式 (7.5) 给出的合法 adelic 区域，$\mathcal T_n$ 是零坐标或三幂零和块等终端集合。$n=5$ 与 $n=9$ 的判别式相同但行为相反，正是因为它们的重数和返回半群完全不同。

虚二次序仍可能发挥两种实质作用。

1. 二次型约化可给出实方向的规范基本域，减少需要搜索的宏。
2. 理想的局部邻接或小范数元素可提出行列式只含少数素因子的候选矩阵，再反向询问这些矩阵是否属于 $\mathcal M_n$。

但“矩阵在二次型或理想类意义下很好”只是候选条件。能否由真实平均词实现，是必须单独证明的组合约束。

## 10. 对一般 $n$ 的统一研究程序

现在可以把一般判定问题分成四层，而每层都有明确的数学对象。

1. **根格与局部障碍。** 在 $A_{n-1}$ 判别群和各良约化纤维中检查 $G$ 的非 $3$ 部分。这一层已经完成。
2. **辫状平坦中的桥。** 使用安全 $A_2$ 投影，把一般状态送入有限个高重数平坦，再进一步进入秩二正交补。一般安全核心已给出约 $n/2$ 重值，尚缺统一桥。
3. **返回半群合成。** 不再无目标地枚举所有短词，而是优先寻找 $\mathcal M_n$ 中的抛物型平移、反射和小行列式折叠矩阵，并逐个反解真实重数词。
4. **adelic 高度控制。** 在有限个 $p$ 进圆柱和实二次胞腔上建立严格下降，最好进一步得到每若干步按固定比例收缩的高度估计，以控制证书长度。

由此得到两个彼此独立的核心猜想。

> **桥猜想。** 对每个 $n\ge7$，任意 $G$ 为 $3$ 的幂的状态，都能通过保持合法性的有限轨道进入零坐标终点，或进入有限多个二维高重数核。

> **二维控制器猜想。** 对桥猜想中出现的每个合法二维核，其真实返回半群都含有有限 adelic 高度下降控制器。

两者同时成立才会推出“大维数静态充分性猜想”。即使如此，要得到一般可变维数的多项式时间构造算法，还需证明：桥和宏集能在关于 $n$ 的多项式时间内生成，并且下降次数关于输入位长为多项式。有限终止本身只给出数值高度界，可能仍是位长的指数界。

十一元已经完成了这套分解的首次完整验证。安全核心把轨道送入六重值层；五步符号桥把任意合法六重状态送入 $(7,3,1)$ 二维核；十二个下降宏和两个平移宏完成局部--实覆盖。下一步比继续扩大无方向搜索更有针对性的任务是：

* 对 $n=13$ 及更高的基维数，寻找类似的高重数桥；
* 研究 $\mathcal M_n$ 中平移、反射和折叠元素的统一生成规律；
* 用虚二次序约化域筛选候选矩阵，再严格验证其是否属于 $\mathcal M_n$；
* 估计桥和控制器的深度随 $n$ 的增长，以区分有限判定和统一多项式构造。

## 11. 当前认识的本质压缩

从这一视角看，二平均与三平均的差别也更自然。二平均消去 $A_1$，其局部核射影化后只是一个点；三平均消去 $A_2$，其局部核射影化后已经是一条 $\mathbb P^1$。二平均的安全配对引理主要处理离散同余与块结构；三平均即使进入最小二维核，仍必须控制一条射影直线上的实斜率、$3$ 进斜率和重数可实现性。

因此三平均问题目前最自然的归属不是单独的代数几何、二元二次型理论或组合搜索，而是三者的交叉：

$$
\boxed{
\text{辫状排列上的投影组合论}
+\text{射影直线上的 }S\text{-算术动力学}
+\text{整数高度的半代数下降}.}
$$

代数几何在这里已经给出了一个真正的新结论，即公式 (0.1) 的统一步数分界；算术几何则把七、八、十元看似不同的证书统一成同一个有限控制器问题。下一次突破最可能来自对 $\mathcal M_n$ 的结构性生成定理，或从高重数平坦到二维核的统一桥，而不是继续单独扩大无方向的词枚举深度。

## 12. 精确核验

十一元现在提供了第四个非三幂完整基维数案例：安全核心的六重桥是五步符号恒等式，二维核的控制器由十二个下降宏和两个平移宏组成。它把“桥”和“控制器”两个缺口分别封闭，完整陈述见 [十一元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_eleven_complete.md)。

`work/verify_arithmetic_geometry_structure.py` 使用整数运算检查：

* $n=5,ldots,11$ 的本原二次型和判别式表；
* 参数格尺度 $h_n\in\{1,2,4\}$ 与能量高度公式；
* 本原输入下 $g_M(z)\mid\det M$；
* 十元七宏的行列式只含素因子 $2,3$、统一保持模 $5$ 合法性，且它们并非能量二次型的相似自同构。

七元和十元的完整局部--实覆盖仍分别由 `work/verify_seven_descent_cover.py` 与 `work/verify_ten_descent_cover.py` 核验；一般三进塔传播由 `work/verify_general_lifting.py` 核验。

<!-- END SOURCE doc-47a119cd7ff0 -->

---

<a id="doc-8ee0382bca27"></a>

## 原文导签：外部 audit 的修订与证据登记

来源：`outputs/triple_average/history/triple_average_audit_resolution_2026-09-09.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_audit_resolution_2026-09-09.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`standard-kernel-interface`, `search-contracts`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-8ee0382bca27 -->
# 外部 audit 的修订与证据登记

审核源文件位于相邻工作区：
C:/Users/19226/Documents/Codex/2026-09-09/cha/outputs/triple_average_latest_document_audit_2026-09-09.md。
它对截至 20:42 的工作区快照审核，原文件保持原位。本记录说明本项目的后续修复，不修改审核原文。

| audit 项 | 已落实的修正 | 证据入口 |
|---:|---|---|
| 1 | B 核合法域统一为非三素数不整除 u-v；p=2 不再替换为 y 非零 | q-平均文档第 5 节；通用参数枚举 |
| 2 | S-高度须选 away-from-3 本原代表；格能量使用标准本原整数代表和二处 h 尺度 | q-平均文档第 5 节 |
| 3 | 固定分层非奇异返回群与分层间有向线性箭头分开；行列式单位单独检查 | 新的三进扩张修复文档第 1、3 节 |
| 4 | 删除未定义的合法旗标和混合商记法，商写为明确群对实对称空间和 building 的作用 | q-平均文档第 3、6 节 |
| 5 | B12 默认加入 18 个 G=3 类，完整高度 8 域为 62 类；历史 44 类可单独重现 | B12 和通用探索器 |
| 6 | 范数恒等式不再声称理想乘法；真实 R 已证明对应指数 9 子格及 theta 筛选 | 三进扩张修复文档式 (9)--(11) |
| 7 | 多项式构造另列宏展开长度和中间位长，区分判定与路径构造 | 两份接口文档 |
| 8 | 交接稿分开已证明结果、框架猜想、有限实验；修正参数维数与群秩术语 | 最新交接稿第 4、7 节 |
| 9 | 加速倍率改为 30.2、252.7、8.3，并明确各自基准 | 性能审计第 4 节 |
| 10 | 更新 full 描述；登记 B12、四核比较、两个深度五补充及符号探索 | manifest 和核验指南 |
| 11 | 运行器拒绝 -O / PYTHONOPTIMIZE，子环境移除该变量 | search-contracts 的两种拒绝测试 |
| 12 | 修复三幂压缩正文中的 LaTeX 转义、控制字符和交接稿公式 | 文档检查 |
| 13 | 重复计数逐项累加，拒绝非正/非整数/布尔重数，接口独立登记 | standard-kernel-interface：229 个网络样本及 9 个无效证书测试 |

额外修正：条目仅在 \(\mathbb Z[1/3]\) 不蕴含矩阵在 GL 中可逆；十三元用的是充分子群 \(H\subseteq\Gamma\)，不是等式；稳定化是某个输入相关的 \(3^k\) 倍复制，不能提前换成恰好三份；B21 已由七元的三进提升解决。

## 不变的证据边界

audit 没有发现此前五个基维数、稳定化、三幂压缩、Burau 或九十一元五步证书的新反例。这里的修订也不宣布一般问题已解决。新引入的标准接口是具体证书契约；有限实验是有界数据；theta 格模性使用标准模性定理，尚未建立覆盖全部合法状态的正向 Hecke 控制器。

不重跑与本次变更无关的长期发现搜索来制造 PASS 数量。修订后的统一入口运行相关短核验；长搜索的精确范围和单项命令在 manifest 中记录。

<!-- END SOURCE doc-8ee0382bca27 -->

---

<a id="doc-ec8ac9b97d9e"></a>

## 原文导签：\(\mathcal B_{12}\) 二维核有限实验

来源：`outputs/triple_average/history/triple_average_b12_kernel_experiment.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_b12_kernel_experiment.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`b12-complete-bounded-domain`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ec8ac9b97d9e -->
# \(\mathcal B_{12}\) 二维核有限实验

**状态更新：** 本实验保留为有限回归数据，已不承担十二元充分性证明。[十二元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md) 已由独立正向宏、指数 12 子群和唯一合法尖点完成。

为检验标准核接口，运行了

```text
python work/explore_b12_kernel.py --bound 8 --depth 4 --jobs 8
```

脚本枚举

\[
\mathcal B_{12}(u,v)=(u^8,v^3,-8u-3v),
\]

其中 \(\gcd(u,v)=1\)、\(\gcd(u-v,4)=1\)，并按全局符号取商。高度界 \(\max(|u|,|v|)\le8\) 得到 62 个本原符号类。历史版本只枚举 \(\gcd(u-v,12)=1\) 的 44 个 G=1 类，漏掉 18 个 G=3 类；现在默认覆盖完整合法域，历史子集可加 --g1-only 重现。

在深度 4 内，62 个类全部找到 3 元零和块（等价地也找到 9 元零和补块）。把两个块分别归零后才完成；搜索深度不计这固定的 7 步网络尾段：

```text
B12 primitive pair classes 62
B12 terminal coverage 62 / 62 depth 4 bound 8
B12 missing []
```

最深的两个方向之一是 \((-7,-2)\)，其四步路径为

\[
(-7,-7,-2),\quad(-7,-7,62),\quad(-7,16,16),
\quad(-7,-16/3,25/3),
\]

最后得到零和三元组 \((-7,25/3,-4/3)\)。另一个困难方向 \((-8,-7)\) 的四步路径为

\[
(-8,-8,85),\quad(-7,-7,23),\quad(-8,-7,3),
\quad(23,-4,-4),
\]

最后得到 \((-8,3,5)\)。每条路径都使用精确有理数重放，并检查了操作重数和零和见证。

这项实验支持三个判断：

1. \(\mathcal B_{12}\) 是单危险素数情形的合理第一个二维控制器样本；
2. 深度 3 的大多数方向已经可达，困难方向具有短的结构化路径，而非明显的随机搜索现象；
3. 仍不能由高度界和深度界推出所有有理方向可达，也不能推出任意三幂分块压缩的输出都能进入 \(\mathcal B_{12}\)。

## 一个算术解释

对 n=12，标准核二次型为

\[
4E=96u^2+3(8u+4v)^2.
\]

令 \(z=2u+v\)，便得到

\[
4E=48(z^2+2u^2).
\]

这正是 \(\mathbb Z[\sqrt{-2}]\) 的范数型，且 \(3=N(1+\sqrt{-2})\)。二次型恒等式本身不证明宏是理想乘法。新的真实宏 R 给出指数 9 子格、导子 9 二次序及精确 theta 筛选恒等式；同时它在低三进本原域反而增加整数高度。完整证明见 [三进扩张修复宏与算术接口](../sources/outputs/triple_average/history/triple_average_carry_repair_and_arithmetic_interface.md)。

因此 n=12 的下一步不是继续把高度界盲目扩大，而是提取四步路径中的宏族，寻找一个有限局部签名和严格下降量。这正是标准核接口中 B 步的具体原型。

<!-- END SOURCE doc-ec8ac9b97d9e -->

---

<a id="doc-91e0ab966585"></a>

## 原文导签：B12 六步局部下降与二次序导子塔

来源：`outputs/triple_average/history/triple_average_b12_six_step_and_conductor_tower.md` · [逐字节原样副本](../sources/outputs/triple_average/history/triple_average_b12_six_step_and_conductor_tower.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`b12-six-step-local-branches`, `b12-return-frontier-certificates`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-91e0ab966585 -->
# B12 六步局部下降与二次序导子塔

本轮继续研究完整 B12 控制器。得到两个可验证的新局部下降分支，但还没有覆盖全部合法射影方向。新的计算证书与此前 audit 修订一致：局部合法性指 u-v 为奇数，允许 G=3。

**后续定理：** [十二元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md) 已使用本轮发现的四个宏完成。下面两条范数分支本身不全覆盖，但更大的正向子群含共轭 \(\Gamma_0(8)\)，故可通过唯一合法尖点完成所有方向；本文的导子塔与子格公式继续有效。

## 1. 新的真实六步宏

令
\[
w=-8u-3v.
\]
首先平均 \((w,u,u)\)，产生
\[
a=-2u-v.
\]

T 宏的后五步为：

1. 平均 \((a,u,u)\)，得 \(b=-v/3\)；
2. 连续三次平均 \((b,v,u)\)，每次得 \(c=(3u+2v)/9\)；
3. 平均 \((a,c,u)\)，得 \(d=-(6u+7v)/27\)。

完整重数变化：
\[
(u^8,v^3,w)
\to(u^6,v^3,a^3)
\to(u^4,v^3,a^2,b^3)
\to(u,a^2,c^9)
\to(c^8,d^3,a).
\]
因 \(a=-8c-3d\)，真实返回为
\[
T(u,v)=\frac1{27}
\begin{pmatrix}9&6\\-6&-7\end{pmatrix}
\binom uv,\qquad \det T=-1/27.
\tag{T}
\]

S 宏在产生 a 后执行：

1. 平均 \((a,a,u)\)，得 \(b=-u-2v/3\)；
2. 平均 \((b,v,u)\)，得 \(c=v/9\)；
3. 平均 \((a,c,u)\)，得 \(d=-(9u+8v)/27\)；
4. 再执行两次 \((b,v,u)\)，均得到 c。

返回为
\[
S(u,v)=\frac1{27}
\begin{pmatrix}0&3\\-9&-8\end{pmatrix}
\binom uv,\qquad \det S=1/27.
\tag{S}
\]
这些是符号恒等式，任何数值重合只会合并可用重数，不破坏逐位置实现。两个清分母矩阵模 2 分别为恒等和交换矩阵，且共同约分因子只含 3，所以都保持合法性。

## 2. 共同约分与下降域

对本原整数参数：
\[
\begin{aligned}
g_T&=\gcd(9u+6v,6u+7v)=\gcd(27,v-3u),\\
g_S&=\gcd(3v,9u+8v)=\gcd(27,9u+8v).
\end{aligned}
\tag{1}
\]
共同因子必须整除行列式 27。分别检查模 3、9、27 即得 (1)：T 的共同因子达到 9、27 分别等价于 \(v=3u\pmod9,\pmod{27}\)；S 达到 9 需 \(9\mid v\)，达到 27 则等价于 \(v=9u\pmod{27}\)。

记本原能量型
\[
f(u,v)=6u^2+4uv+v^2=E/12.
\]
两个清分母矩阵的拉回型分别为
\[
f(M_Tz)=306u^2+336uv+97v^2,\quad
f(M_Sz)=81u^2+36uv+22v^2.
\tag{2}
\]
有严格的实不等式
\[
f(Tz)<f(z)/3,\qquad f(Sz)<f(z)/3\quad(z\ne0).
\tag{3}
\]
证明只需检查 \(243f-f\circ M\) 正定，其矩阵首主子式与行列式分别为：
T 的 1152、67068；S 的 1377、85293。

当 \(g=27\) 时，实际宏输出已经是本原整数参数，故 (3) 直接成为本原高度下降。这给出两个普适局部分支：
\[
\boxed{v\equiv3u\pmod{27}\ \Rightarrow T\text{ 严格下降}},
\qquad
\boxed{v\equiv9u\pmod{27}\ \Rightarrow S\text{ 严格下降}}.
\tag{4}
\]
两者都位于 \(3\nmid(u-v)\) 的低三进域，突破了只用 A、R 的高度增加障碍。

若希望输出还进入 \(3\mid(u'-v')\) 的 A 可下降域，则准确条件是
\[
v\equiv30u\pmod{81}\quad(T),\qquad
v\equiv36u\pmod{81}\quad(S).
\tag{5}
\]
这是 (1) 后再除以 27 检查新差值所得；模 27 与模 81 两种结论不能混用。

这两个分支仍不足以处理全部低三进方向。只有当相应同余成立时才可宣称整数下降，纯实收缩不替代共同约分条件。

## 3. 一个真实宏产生无界导子

继续使用上一轮的四步宏
\[
R=M_R/9,\qquad M_R=\begin{pmatrix}6&3\\-19&-8\end{pmatrix}.
\]
定义 \(f_k=f\circ M_R^k\)。则对任意 \(k\ge0\)，有
\[
f_k\text{ 本原},\qquad D(f_k)=-8\cdot3^{4k}.
\tag{6}
\]
判别式变换由 \(D(f\circ M)=D(f)(\det M)^2\) 得到。本原性的证明：
在 \((u,z=2u+v)\) 的整系数可逆坐标变换下，f 是 \(2u^2+z^2\)，
\[
M_R=\begin{pmatrix}0&3\\-3&-2\end{pmatrix}.
\]
模 3 时它及任意正幂都有非零的右下角，故拉回型不全被 3 整除。
对任何其他素数，矩阵是可逆的，不能使本原型全部系数被该素数整除。证毕。

由本原二元型与二次序的标准对应，\(f_k\) 所属二次序的导子为
\[
c_k=3^{2k}.
\]
K=\(\mathbb Q(\sqrt{-2})\) 的最大序类数为 1，3 在 K 中分裂，单位指数为 1。
二次序类数公式给出对 \(k\ge1\)
\[
h(\mathcal O_{c_k})
=c_k(1-1/3)=2\cdot3^{2k-1}.
\tag{7}
\]
对应偶格 level 为 \(8\cdot3^{4k}\)：对本原二元型 (a,b,c)，level N
须使 \(|D|\) 同时整除 Na、Nb、Nc。由 \(\gcd(a,b,c)=1\)，必有
\(|D|\mid N\)，而 N=|D| 又满足偶整 Gram 逆矩阵条件，故 level 恰为 |D|。

这解释了“起始范数来自类数一”为什么不足够：一个可执行宏反复作用，已产生导子和类数都无界的本原型族。不能把全部拉回 theta 级数默认塞入原 level 8 的固定空间。可以把这些函数放入共同加 level 的空间或 adelic 表示框架，但正向路径与本原约分仍要逐层证明。

## 4. 单分支与完整格对应的区别

对任意秩二整数格 L 和正定型 f，固定素数 p，枚举全部 p+1 个指数 p 子格。直接逐点计数给出严格恒等式
\[
\sum_{\substack{L'\subset L\\[L:L']=p}}\Theta_{L'}(\tau)
=\Theta_L(\tau)+p\,\Theta_L(p^2\tau).
\tag{8}
\]
因为 \(x\notin pL\) 只属于一个这样的子格，而 \(x\in pL\) 属于全部 p+1 个。
它是完整子格对应的求和公式，不预先等同于某种归一化的经典 Hecke 算子。

真实宏提供的通常只是一个带重数约束、方向固定的子格分支。因此完整 Hecke 或 Eisenstein 理论中的轨道求和，不能自动转化为某个允许分支的存在，更不能给出逐步本原高度下降。后续可检验的目标是识别真实宏能覆盖哪些子格分支及其局部类型。

## 5. 有界发现与核验

work/search_b12_return_frontier.py 以整数符号状态、全局缩放商和返回形状剪枝进行发现搜索。早期版本曾错误使用 \(3+2L\) 界；均值碰撞到已有值时，一次可以消去三个不同值。当前安全界为 \(3+3L\)，并有针对这一碰撞的回归测试。前两步分支并行；所有矩阵均保留规范化索引词并重放成实际 Fraction 词。以下旧缓存保留其发现结果，但撤回深度6、7的完备枚举声明。

| 深度 | 不同返回矩阵 | 本机此次发现耗时 |
|---:|---:|---:|
| 5 | 21 | 约 1.3 秒 |
| 6 | 87 | 约 8 秒 |
| 7 | 395 | 约 114 秒 |

JSON 证书保存在 work/b12_return_depth5.json、work/b12_return_depth6.json、work/b12_return_depth7.json。核验程序重放全部 503 个条目，并将深度 5 的完整矩阵集合与独立的旧 Fraction 搜索对照。深度 6、7 的缓存只作为正向证书集合，未重新证明完整性；最终十二元定理直接核验四个显式宏，不依赖发现表完整性。

work/verify_b12_local_branches.py 独立按未规范化符号重数实现 T、S，检查局部内容公式、正定性和迭代导子数据。数值核验只防止实现差错；全称恒等式与同余条件由前面证明给出。B12 可达性已由独立群证书完成；一般核控制器和复制消去仍开放。

<!-- END SOURCE doc-91e0ab966585 -->
