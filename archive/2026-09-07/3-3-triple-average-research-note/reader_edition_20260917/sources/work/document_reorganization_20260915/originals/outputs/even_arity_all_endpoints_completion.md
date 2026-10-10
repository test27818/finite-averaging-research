# 全部偶数元数的2k+1端点：旧种子与统一取逆

日期：2026-09-15。本页用于一般k的区间任务；没有讨论去掉GRH。本页恰只需已有无条件算术群工具，不使用GRH。

## 1. 完整结论

**定理。** 对每个偶数k>=2，n=2k+1的全部有理输入满足完整G=1可达性判据。

结合[已有任意奇元数端点](prime_arity_unrestricted_endpoint_and_odd_band.md)，得到**每个整数k>=2的2k+1元均已完整解决**。这不等于一般N(k)<=2k+1；其后维数仍有接续任务。

核心起点是[四平均九元第6节](four_average_nine_complete.md)已经写出的所有偶数元数种子，本页补齐一般倍率逆、完整根和终端，不重搜种子。

## 2. 一般真实返回

k=2b，n=4b+1。核心为(a^k,b_value^k,-k(a+b_value))，坐标(x,y)=(a,a-b_value)。记Sigma=(1,-1;0,-1)，是两个等大块的角色交换。

已有真实两原子返回为T_j/k，1<=j<=k，
\[
T_j=\begin{pmatrix}-k-1&j\\-n&2j\end{pmatrix},\qquad\det T_j=-j.
\]
另有保留单点的真实两原子返回
\[
F_r=\begin{pmatrix}1&(r-k)/(2k)\\0&r/k\end{pmatrix},
\quad r\text{ 偶},\quad |r|\le k.
\]
每个gcd(j,n)=gcd(r,n)=1的返回在危险素数处可逆、保持合法性。

置J=T_b Sigma，则
\[
J^2=-bI,\qquad T_b^{-1}T_j=\Delta(j/b).
\tag{2.1}
\]
所以T_b及其射影逆正向存在。

## 3. b偶时直接取得二进根

取j=k与j=b/2，式(2.1)分别给Delta(2)和Delta(1/2)。于是Sigma交换子直接给U(1/2)，且Sigma共轭将其变号。Delta(2)正逆共轭给全部U(Z[1/2])。

令Delta(-1)=Sigma U(1)。真实T1提供
\[
U(-1/2)T_1\Delta(-1/4)=-\tfrac12L(2n).
\tag{3.1}
\]
所以L(2n)正向存在；Delta(-1)给其逆，二进共轭给全部L(nZ[1/2])。到此可直接调用Gamma1精确生成引理。

## 4. b奇时先取得b倍率的逆

k=2即二平均五元，已有定理。以下b>=3。

取epsilon=-1（b=1模4）或+1（b=3模4），令
\[
a_0=(4b+1+\epsilon b)/4.
\]
a0为1至k之间的安全整数。直接迹公式给
\[
\operatorname{tr}(T_{a_0}F_{2\epsilon})=0,
\qquad (T_{a_0}F_{2\epsilon})^2=\frac{a_0\epsilon}{b}I.
\]
实际返回的非零共同尺度一并计入，仍是正向标量周期。因此F_(2epsilon)有正向逆，再由F_-2=Sigma F2得到F2^-1。

Delta(1/b)=T_b^-1 T1已正向存在；与F2^-1配对有
\[
\Delta(1/b)F_2^{-1}=U((b-1)/2).
\]
Sigma将这个上平移共轭为其逆，所以原两因子均获得正向逆。由此Delta(b)及Delta(1/b)都可执行。

Sigma与Delta(b)给U((b-1)/b)，其双向共轭给U((b-1)R0)，R0=Z[1/b]。用J的横向共轭、清分母换基和Morris／Serre深同余引理，得到
\[
\Gamma((b-1)^2n^3,R_0).
\tag{4.1}
\]

Delta(2)可由(2.1)直接取j=k得到。其逆不能因为2不除n就绕过(4.1)含2的事实，需要下一步。

## 5. 一个夹乘统一给除二

令J'=Sigma J Sigma=(2b,-b;n,-2b)，其平方仍为-bI。取
\[
H=\tfrac12\Delta(2)J'\Delta(2)
=\begin{pmatrix}b&-b\\n&-4b\end{pmatrix}.
\]
H整于R0，det H=b=det J'，故Z=H(J')^-1属于SL2(R0)，正向可执行。由(4.1)的有限逆提升，Z^-1可执行，从而H^-1=(J')^-1Z^-1也可执行。

精确有
\[
J'\Delta(2)H^{-1}=2\Delta(1/2).
\]
于是所有b奇的情形也取得Delta(2)及逆，Sigma交换子给U(1/2)，第3节的式(3.1)再给L(nZ[1/2])。所有偶数元数统一到同一二进根接口。

## 6. 全部尺度与精确终端

已有Gamma1(n,Z[1/2])包含Gamma(n)。现在以安全返回取逆激活(2.1)的Delta(1/b)及逆；对所有安全j<=k，取得Delta(j)、Delta(j)^-1。

用这些倍率的共轭把上下根扩到R=Z[1/ell:ell<=k素数且ell不整除n]，再在这个R上应用Gamma1引理。任意模n单位都有非零平衡代表u满足|u|<=k，所有素因子在R中可逆，所以R单位模n满射。

本原合法(x,y)以Bezout取F=(y,-x;alpha,beta)、alpha x+beta y=1且n|alpha。用实际R单位epsilon=y模n校正对角，使剩余因子属于Gamma1(n,R)，得到F的正向实现，精确送到(0,1)。

此时核心为(0^k,(-1)^k,k)。先平均单点k与k-1个零，产生k份1并留一个零；再分两次，各平均k/2份1和k/2份-1，全部归零。终端始终在原n位置上。

## 7. 全输入入口与核验

既有单块—三单点入口引理本来适用于任意整数k>=2且gcd(k,n)=1。n=2k+1满足该条件；交换子失效素数由gcd(k-1,2k+1)=gcd(k-1,3)控制，至多一个3，一个保留单点足够。该入口不使用k为奇数，奇偶只影响后来的控制器。因此全部合法输入均进入本页双块核心。

[精确核验](../work/verify_even_arity_endpoint_uniform.py)核对199个偶元数的通用恒等式及26条在两个基方向上的真实标量闭路。任意k、全输入和全部尺度量词由正文承担；不枚举平均词、模群或输入高度。

这里完成的是接续任务的一条全参数边界。没有将其写成整个2k至旧尾部区间已完成。
