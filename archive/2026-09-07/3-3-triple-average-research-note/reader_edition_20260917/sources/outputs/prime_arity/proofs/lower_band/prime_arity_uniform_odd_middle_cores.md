# 任意素数的奇余量中间核：两个对合、主同余控制与小代表

> **当前定位（2026-09-15整理）：**本页为技术附录／历史研究记录。素数最优最终阈值及完整覆盖见[统一证明入口](../../README.md)；正文的阶段性“未解／下一步”须据该入口判断，不能作当前总状态。

**2026-09-15全部奇数维数完成：** [三单点交换子的无条件入口](prime_arity_unrestricted_endpoint_and_odd_band.md)已进一步删除r>=omega(n)条件。接本页核心定理后，对任意素数p>=5、全部奇数3<=r<p，n=2p+r的任意原输入均有完整G=1判据；r=1由同一新入口接端点核心完成。因此现在2p<n<3p的全部奇数维数确已全输入解决。下文旧入口条件及第7节限制只反映原稿阶段。

同日偶数后续：[偶数深同余与七平均十八元](../../history/prime_arity_even_middle_congruence_and_eighteen.md)给出内部偶余量的深主同余控制、新的无周期密度入口，并完成七平均18元。下文18元未解表述保留为本页原始阶段；最新七平均临界未解为20、22，一般偶余量仍未全解。

日期：2026-09-14。本页把[五平均十三元](../../examples/five_average_thirteen_congruence_complete.md)推广到所有奇素数p及全部奇余量3<=r<=p-2。外部依赖与[端点同余闭合](prime_arity_endpoint_congruence_completion.md)一致：Morris 2007定理6.1(2)及Serre对SL2(Z[1/2])的强同余子群性质。本页不依赖逐p搜索。

## 1. 定理与全输入范围

**核心定理。** 设p>=5为素数，r为奇数且3<=r<p，n=2p+r。每个合法全系统核心
\[
\mathcal K_{p,r}(x,z)=(x^p,(rz-x)^p,(-pz)^r),
\qquad \gcd(x,z)=\gcd(x+pz,n)=1
\]
都能在原n个位置上有限步p平均归零。

**全输入推论。** 若还满足已有入口条件
\[
r\ge\omega(n),\qquad
\sum_{\ell\mid n}1/o_\ell(p)<1,
\]
其中p=-1模ell时o_ell(p)=ell，否则o_ell(p)=ord_ell(-p^{-1})，则该n元问题的全输入判据为G=1。入口引用[中间带归约](../../history/prime_arity_band_period_and_involutions.md)，不把任意输入自动视为核心。

**统一素数维数推论。** 对每个奇素数p，所有满足
\[
\boxed{2p<\ell<3p,\qquad\ell\text{为素数}}
\]
的维数均有完整G=1判据。r=1由端点定理承担；r>=3时上述入口条件自动成立。p=3只需已有七元定理。

同一论证更一般地覆盖所有奇素数幂维数n，2p<n<3p：仍只有一种危险素数，入口周期至少为2。这里素数幂指位置数，不是平均元数。

新增包括七平均17、19元，以及更大p的全部上述奇素数幂维数和满足入口条件的其他奇合数维数。七平均仍缺18、20、22元，N(7)<=23未因此降低。

## 2. 合法坐标与两个始终存在的对合

gcd(p,r)=1使整数三块零和状态恰有上述表示，本原性等价于gcd(x,z)=1。差分2x-rz与x+pz的gcd等于gcd(x+pz,n)。记y=x+pz。

取已有返回的两个奇参数s=r、r-2。设a=x、b=rz-x、c=-pz及i=(p-s)/2，分别平均两个不交p组
\[
(a^i,b^i,c^s),\qquad
(a^{p-r-i},b^{p-i},c^{r-s}),
\]
留下r份原a。r<=p-2保证两种s都满足容量。

实际矩阵是J/p和Q/p，其中
\[
J=\begin{pmatrix}0&d\\-1&0\end{pmatrix},\quad
Q=\begin{pmatrix}0&e\\-1&0\end{pmatrix},\qquad
d=-r(p+r)/2,\quad e=d+n.
\]
d、e非零、互素，均与n互素且奇偶相反。由J^2=-dI、Q^2=-eI，两者及射影逆都正向可执行。换两个p块的标签给
\[
\Sigma=\begin{pmatrix}-1&r\\0&1\end{pmatrix}.
\]
模ell|n时，未除p的J、Q将y乘以-p，Sigma将y乘以-1，故保持合法性。

## 3. 统一双向根

直接计算
\[
D=J^{-1}Q=\operatorname{diag}(1,e/d),\qquad
\boxed{\Sigma D\Sigma D^{-1}=U(rn/e)}.
\]
gcd(d,e)=1给出倍率及其逆生成的环
\[
R=\mathbb Z[e/d,d/e]=\mathbb Z[1/(de)].
\]
用D的共轭、逆共轭及根的整数线性组合得到U((rn/e)R)。因r整除d，r与e都是R单位，所以这恰为U(nR)。又
\[
JU(t)J^{-1}=L(-t/d),
\]
故也有L(nR)。d、e奇偶相反，因此A=Z[1/2]包含于R，特别得到U(nA)、L(nA)及其正向逆。

## 4. 主同余子群可执行

令
\[
V=J\Sigma J^{-1}\Sigma
=\begin{pmatrix}-1&r\\r/d&-1-r^2/d\end{pmatrix},
\]
它行列式为1且正向可逆。三个整数幂零矩阵为
\[
N_1=E_{12},\quad N_2=E_{21},\quad
N_3=d^2VN_1V^{-1}
=\begin{pmatrix}rd&d^2\\-r^2&-rd\end{pmatrix}.
\]
所有I+ntN_i（t属于A）可执行；第三族来自V共轭U(nd^2t)。

V未必属于SL2(A)，但这三个幂零族都属于SL2(A)。令G_0为这三个族生成的子群，在G_0上应用外部定理，不把任意d分母直接当成二进分母。

G_0包含U(nA)、L(nA)。Morris定理应用于Gamma(n,A)，说明这些根生成有限指数子群。因此G_0在SL2(A)中有限指数，Serre定理给Gamma(M,A)包含于G_0；可令M奇且n|M。

对任意ell|n，rd是模ell单位，故N_1、N_2、N_3在sl2(F_ell)中线性无关。精确恒等式
\[
(I+ntN_i)^{\ell^k}=I+n\ell^k tN_i
\]
使三个方向逐层生成从v_ell(n)开始的全部主同余层。ell不整除n时，上下根已经生成整个有限局部SL2。各处参数用CRT独立提升，故G_0模M覆盖Gamma(n,A)模M的像。再用已包含的Gamma(M,A)，得到
\[
\boxed{\Gamma(n,A)\subseteq G_0.}
\]
该论证适用于任意奇合数n及任意指数，未由有限模样本外推。

## 5. 主同余控制给旧收缩构造正向逆

保留载体，在两个p块间取两组互补组成
\[
(a^{(p+t)/2},b^{(p-t)/2}),\quad
(a^{(p-t)/2},b^{(p+t)/2}),
\]
其中t奇、|t|<=p。实际返回为
\[
F_t=\begin{pmatrix}t/p&r(p-t)/(2p)\\0&1\end{pmatrix}.
\]
gcd(t,n)=1时合法，因为模n有y'=(t/p)y。F_1始终安全。

令
\[
M=pF_1=\begin{pmatrix}1&r(p-1)/2\\0&p\end{pmatrix}.
\]
取k使p^k=1模n，写
\[
P=M^k=\begin{pmatrix}1&b\\0&\delta\end{pmatrix},
\quad\delta=p^k,\quad b=r(\delta-1)/2.
\]
于是P=I模n，gcd(delta,n)=1。矩阵
\[
g_*=\begin{pmatrix}b&1\\-1&0\end{pmatrix}
\]
满足Pg_*P=delta(0,1;-1,-b)。由CRT和SL2(Z)到有限商的满射，取整数行列式一矩阵g，使g=g_*模delta、g=I模n。有限商满射可由单位主元消元和初等矩阵的整数提升证明，不需新增平均操作。

于是
\[
h=\delta^{-1}PgP
\]
是整数行列式一矩阵且h=I模n。因此g、h及其逆属于已可执行的Gamma(n,A)。恒等式
\[
gPh^{-1}=\delta P^{-1}
\]
给出P的正向射影逆，再接M^{k-1}得到M^{-1}，也就得到F_1^{-1}。

求逆词中的主同余操作会移动载体，所以这不违反固定外部非零坐标时的旧尺度障碍。现在对每个安全奇数t、0<|t|<=p，都可以正向执行
\[
\boxed{C_t=F_tF_1^{-1}
=\begin{pmatrix}t&r(1-t)/2\\0&1\end{pmatrix}.}
\]
后面只需执行C_t一次，不要求预先取得它的逆。

## 6. 小代表引理替代“2是原根”

在(z,y)=(z,x+pz)坐标中，
\[
V\equiv\begin{pmatrix}1&2p^{-1}\\0&1\end{pmatrix}\pmod n.
\]
由于y是模n单位，取V的一个0至n-1次幂使z=0模n。输出取本原整数代表(a,b)，仍有b=0模n、gcd(a,n)=gcd(a,b)=1。清分母及本原化的尺度在n的每个素因子处都是单位，故保留该结论。

**小代表引理。** 对任意模n单位u，存在奇整数t及整数j，使
\[
0<|t|\le p,\quad\gcd(t,n)=1,\qquad t=2^ju\pmod n.
\]
证明：取|u|<=n/2的平衡代表。若|u|>p，用v=2u-sgn(u)n替换，则0<|v|<r<p，且v=2u模n；否则v=u。再去掉v的全部2因子，即得所需奇t。这使用n<3p，但不要求2生成模n的全部单位群。

将引理用于u=a^{-1}，得到t*a=s模n，其中s=2^j属于A单位。先用L(nh)使b与t互素：对每个素数q|t，若b=0模q取h=1，否则取h=0；gcd(a,b)=gcd(n,t)=1保证有效，用CRT同时满足。这个操作保留a及b模n。

随后执行C_t，得到
\[
a'=ta+r(1-t)b/2,\qquad b'=b.
\]
因为gcd(t,b)=1，新的两坐标仍本原，而且a'=s模n、b'=0模n。选alpha、beta属于A使alpha*a'+beta*b'=s，沿Bezout通解调整到beta=0模n，便也有alpha=1模n。于是
\[
H=\begin{pmatrix}\alpha&\beta\\-b'/s&a'/s\end{pmatrix}
\in\Gamma(n,A)
\]
将(a',b')精确送到(s,0)，第4节已经提供其正向实现。

到达(s^p,(-s)^p,0^r)后，两次各平均(p-1)/2对相反值与一个零，最后平均一对相反值与p-2个零，三次完成。核心定理得证。

## 7. 全输入结果及限制

接已有入口，所有满足第1节条件的奇余量维数完成。特别n为素数时只有一个危险素数，交换周期至少2，入口自动成立；r=1另接端点定理。因此对每个奇素数p，2p与3p之间的全部素数维数均解决。

例如p=7时17、19元完成；p=11时25、27也满足原入口条件，再加29、31等素数维数。上述结果没有逐维数的新种子或终端表。

一般奇数维数若不满足入口条件，不能直接调用核心定理；一般偶数r、3p上半带及4p上方接续也未由本页解决。因此没有降低任意p的最终阈值N(p)。七平均仍缺18、20、22元，五平均仍缺12、14元。

## 8. 核验与效率边界

[核验程序](../../../../work/verify_uniform_odd_middle_cores.py)检查71组(p,r)参数恒等式，426个原位置返回，284条大整数参数的精确终端矩阵构造，其中52条使用小代表折返。另以CRT和有限环消元构造六组取逆引理的整数g、h，以及69条已有全输入入口。

计算未搜索平均词。主同余包含依赖外部定理及一般证明；程序检查目标H，但未提取任意H的完整平均词。因此不承诺短词、统一精度或位长多项式算法。迭代返回后的块角色由位置账本重标记，不能要求全局标量关系保持每个最初位置的角色不变。

记录：[uniform_odd_middle_core_records.json](../../../../work/uniform_odd_middle_core_records.json)。
