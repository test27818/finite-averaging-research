本节用于 $p\ge83$、$p<r<2p$、$n=2p+r$。第3段的计数也列出其可同时覆盖的部分下半带，但本证明的下半带由前述各构造承担。

# C18.2 一组或两组来源：同一实际反射

由[共同形状入口](common_shape_integer_relations_and_mainstream_structure.md)，所有本范围合法输入可以进入
\[
K_{p,r}(a,z)=(A^p,B^p,C^r),\quad
A=a,\quad B=rz-a,\quad C=-pz,
\]
\[
\gcd(a,z)=\gcd(a+pz,n)=1.
\]
入口由双块安全入口、上半带三值压缩及两次核心转换组成。

选q∈{1,2}，来源c=(i,j,k)、i+j+k=p。在原位置上平均q组不交且组成相同的p元组，产生qp份
\[
D=((i-j)a+(rj-pk)z)/p.
\]
保留r份D作新载体。剩余库存恰为
\[
(p-qi,\ p-qj,\ r-qk,\ qp-r).
\tag{2.1}
\]
选输出o=(x,y,u,v)，非负且不超过(2.1)，总数p；平均该组及其p元补组。共q+2次原子平均，重新得到相同核心形状。

令α=i−j>0、β=rj−pk。实际返回是p⁻²J，其中
\[
J=\begin{pmatrix}
p(x-y)+\alpha v&pry-p^2u+\beta v\\
-\alpha&-\beta
\end{pmatrix}.
\tag{2.2}
\]
若
\[
p(x-y)+\alpha v=\beta,
\tag{2.3}
\]
则J迹零且J²=pfI。由[整数关系计算](common_shape_integer_relations_and_mainstream_structure.md)，
\[
pf\equiv p^4\pmod n,
\qquad
\widehat J=p^{-2}J\equiv
\begin{pmatrix}1&-\alpha/p^2\\0&-1\end{pmatrix}\pmod n
\tag{2.4}
\]
（第二式在(z,y_*)=(z,a+pz)基中）。因此返回非奇异、合法，重复它即给全系统非零标量，提供真实正向射影逆。q只改变容量和原子次数，不改变(2.2)—(2.4)。

所有以下反射成对选取，第二输出为
\[
o'=o+(-1,-1,2,0).
\]
记相应平方系数为f,g，则g−f=αn。

# C18.3 四个容量选择覆盖整个定理范围

### 3.1 随载体余量变化的计数：下半段与上端共用

用于ceil(p/3)+4≤r<p，以及r>3p/2。令
\[
q=\begin{cases}1&r<p,\\2&r>3p/2,\end{cases}
\quad d=qp-r,\quad
a_0=\left\lceil\frac{d+4}{q}\right\rceil.
\]
对α=a₀,a₀+1，来源取
\[
\boxed{(i,j,k)=(\alpha,0,p-\alpha).}
\tag{3.1}
\]
输出取
\[
\boxed{o_l=(l,p-\alpha+l,\alpha-2l,0).}
\tag{3.2}
\]
总数与迹零自动成立。所有来源和输出容量由
\[
\boxed{
\max\left(0,\left\lceil\frac{d-(q-1)\alpha}{2}\right\rceil\right)
\le l\le
\min\left(\lfloor\alpha/2\rfloor,p-q\alpha\right)
}
\tag{3.3}
\]
保证。设左端为L，取l=L+1,L；第二张表减一份A、一份B、增加两份C。

**q=1的容量。** 此时α=d+4或d+5、L=ceil(d/2)。两种α均有floor(α/2)≥L+1。另一上界要求
\[
p\ge d+\lceil d/2\rceil+6.
\]
由r≥ceil(p/3)+4，有d≤floor(2p/3)−4。代入p=3k+1或3k+2，右边最大分别为p−1或p，故成立。来源剩余C为α−d≥4，其他库存也非负。

**q=2的容量。** 此时0<d<p/2，α=ceil(d/2)+2或ceil(d/2)+3。因为d≤2α−4且α≥3，(3.3)左端L满足L+1≤floor(α/2)。又
\[
2\alpha\le d+7,\qquad L+1\le d/4+1,
\]
所以p−2α≥L+1由p≥5d/4+8保证。d≤(p−1)/2且p≥83蕴含该条件。来源剩余C为2α−d≥4，其余库存同样非负。

因此(3.1)—(3.3)共用一个公式覆盖下半带的一整段与靠近4p的整段。每处只有两组相邻α、每组两张实际反射表。

### 3.2 平衡来源：覆盖上半带中部

设r=p+s，10≤s≤floor(p/2)。取q=2、a₀=ceil(p/6)，对α=a₀,a₀+1取
\[
\boxed{(i,j,k)=(2\alpha,\alpha,p-3\alpha),}
\]
\[
\boxed{o_e=(\alpha-e,p-3\alpha-e,2\alpha-s+2e,s).}
\tag{3.4}
\]
来源总数、输出总数和迹零恒成立。精确可行区间为
\[
L=\max(5\alpha-p,\lceil s/2\rceil-\alpha),\qquad
U=\min(\alpha,2\alpha+s-\lceil p/2\rceil).
\tag{3.5}
\]
取e=L,L+1。

证明L+1≤U，只须四个比较：
\[
4\alpha\le p-1,\quad
3\alpha\le\lfloor p/2\rfloor+s-1,\quad
\lceil s/2\rceil+1\le2\alpha,\quad
\lceil p/2\rceil+1\le3\alpha+\lfloor s/2\rfloor.
\tag{3.6}
\]
由p/6≤α≤(p+11)/6、p≥83、10≤s≤(p−1)/2逐项成立：第一式p≥25足够；第二式最多差6而s−1≥9；第三式p≥15足够；最后一式因3α≥ceil(p/2)、floor(s/2)≥5。4α≤p还保证来源及被删去的上界p−3α≥α；s≤p/2保证D库存，6α≥p保证C来源容量。

### 3.3 紧邻3p：使用已证计数公式，共用同一收尾

剩下r=p+s、1≤s≤9。继续使用已经书面证明的[三连参数公式](../../outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)，其p≥83界不需要有限反射记录。

令a₀=floor(s/3)+1，对α=a₀,a₀+1及
\[
h=\lfloor p/(3\alpha)\rfloor-1,\quad\lfloor p/(3\alpha)\rfloor
\]
取
\[
i=\alpha(h+1),\quad j=\alpha h,\quad k=p-\alpha(2h+1),
\]
\[
o_e=(j-e,k-e,(\alpha-s)h+\alpha+2e,sh).
\tag{3.7}
\]
令
\[
e_0=\max\{0,\alpha(3h+2)-p,\lceil((s-\alpha)h-\alpha)/2\rceil\},
\]
使用e=e₀,e₀+1，q=2。旧容量定理保证连续三个e，这里只需前两个。不再要求第三个e承担二进周期／单位修补；第6节会统一完成。



# C18.4 同一根理想与同一深同余群

在上述每组来源中，j为α的倍数，故
\[
f\equiv p^3\pmod\alpha,\quad
g-f=\alpha n,\quad
\gcd(f,n)=\gcd(g,n)=1,
\quad\gcd(f,g)=1.
\]
最后用gcd(p,α)=1。所有计数均使0<α<p。

令R₀为全部f,g素因子的有限局部化环。相邻反射与正向逆给
\[
T=J_f^{-1}J_g=
\begin{pmatrix}1&-\beta n/f\\0&g/f\end{pmatrix}.
\]
其倍率及逆倍率因gcd(f,g)=1恰生成R₀。两个等大块的自由角色交换S=(-1,r;0,1)给
\[
\boxed{[S,T]=U(nH/g),\qquad
H=2\beta+r\alpha=n(2j+\alpha)-2p^2.}
\tag{4.1}
\]
通过倍率共轭与根参数的整数加法，得到U(δnR₀)，其中δ为全部H的正gcd。

四种容量选择的gcd均为
\[
\boxed{\delta=\gcd(n,2).}
\tag{4.2}
\]
第3.1节j=0，相邻α使H相差n，故gcd为gcd(n,2p²)=gcd(n,2)。第3.2节j=α，相差3n，且p≠3，所以gcd(3n,2p²)=gcd(n,2)。第3.4节j=(t−1)α，差为(2t−1)n；而2t−1为正奇数且小于p（rt≤p、r≥4t蕴含2t≤sqrt(p)），故同样的gcd为gcd(n,2)。第3.3节固定α的两个h使H相差2αn，相邻α互素使总gcd整除2n；再用H≡−2p² modn，去掉奇因子。n奇时奇α给奇H；n偶时偶α给H≡2 mod4，故仍恰为(4.2)。

横向反射的α含两个相邻数，gcd为1。沿用原已证换基level计算：设b=δn，P=(e₁,Je₁)=(1,β;0,−α)，则
\[
P^{-1}U(t)P=U(-\alpha t),\qquad
P^{-1}JU(t)J^{-1}P=L(\alpha t/\det J).
\]
第二式以参数t=(det J)bx清去分母，不假设p已在R₀中可逆。Morris／Serre深核定理在P基给Γ(α²b²,R₀)，换回原基包含Γ(α³b²,R₀)。互素α的level合并得到
\[
\boxed{\Gamma(b^2,R_0).}
\tag{4.3}
\]
R₀有无限单位：相邻f,g互素且差αn>2，不可能全部绝对值为1。原深核定理的适用条件满足，未从有限模像倒推无限群包含。

先用旧安全返回夹乘引理取得F₁及其逆，反演p；再激活所有奇数1≤q≤p、gcd(q,n)=1的保载体互补混合F_q。倍率共轭扩环，并在最终R上重新建立同一Γ(b²,R)。n奇时一组奇α使f,g奇偶相反，2已经在R₀中反演。最终R单位包含全部安全小整数1≤q≤p。全部所用规范反射属于GL₂(R)，完整本原列可在同一环内追踪。

在(z,y_*)基中，原U(bR)恰变成L(bR)。再由相邻α及Bezout，反射乘换块给实际可逆V满足
\[
V\equiv\begin{pmatrix}1&-p^{-2}\\0&1\end{pmatrix}\pmod n.
\tag{4.4}
\]
不要求V的迹模4或模9满足额外条件。

# C18.5 全部2p<n<4p的小单位引理

**引理。** p≥5为奇素数、2p<n<4p、gcd(p,n)=1。由−1和所有1≤q≤p、gcd(q,n)=1的剩余类生成的子群H，等于(Z/nZ)×。

**n奇。** 若H不满，取最小正缺失单位a。利用−1可设p<a<n/2，又p>n/4。若a<n/3，取4a−n；若a>n/3，取n−2a。它总是严格介于0与a之间，且为缺失单位，矛盾。a=n/3与gcd(a,n)=1、n>2p≥10不相容。2、4都属于H，所以折返合法。

**n=2m，m奇。** 单位约化到模m为同构。选ε∈{−1,1}使q=(m+ε)/2为奇数。因m<2p，有q≤p且gcd(q,n)=1，故H模m包含2的逆（差一个符号）。任一单位模m取正平衡代表a≤m/2<p，除尽2因子得到奇数c≤p；c也与n互素，已在H中。乘回2的幂即可覆盖原单位。

**4整除n。** 在区间(0,n/2)内，a↦n/2−a是单位的无固定点对合，故(0,n/4)恰有φ(n)/4个单位。它们都小于p，连同负数已有φ(n)/2个H元素。p本身与n互素且n/4<p<n/2，故±p又给两个不同元素。因此|H|>φ(n)/2，H只能是满群。

证毕。这个引理无九偏移限制，不用有限单位群枚举、原根假设或容斥误差。它与第4节实际小数字激活结合后，给
\[
\boxed{R^\times\twoheadrightarrow(\mathbb Z/n\mathbb Z)^\times.}
\tag{5.1}
\]

# C18.6 移动终端族，共用一次列输送

终端列在(z,y_*)基中仍取
\[
t_j=(1,p^2-nj).
\tag{6.1}
\]
对应零和p元组为(j+1)份A、j份B及p−1−2j份C。其精确容量是
\[
\boxed{\max(0,\lceil(p-1-r)/2\rceil)\le j\le(p-1)/2.}
\tag{6.2}
\]
旧九偏移取j=0或1。r<p时只需把选择区间移到(6.2)，不必改变列算法。该区间含至少两个连续整数（本范围r≥12），所以可以选出任意j modδ，δ∈{1,2}。所有t_j本原，且p²−nj与n互素。

现在已有L(bR)、Γ(b²,R)、(4.4)、(5.1)，以及安全小数字的可逆乘法。按[分裂乘法与两根列输送](split_torus_completes_all_directions.md)：

1. 用V的非负幂和一个R单位ε，使当前列w≡ε(1,p²) modn。
2. n偶时，用安全q≡3或5 mod8与符号组成的分裂乘法，匹配首坐标的完整二进精度；再用V的一个2幂倍次数恢复奇数部分。该小q对p≥11、n<4p始终存在。
3. 由当前第二坐标确定j modδ，在(6.2)选取j，使w≡εt_j modb。与旧证明相比，只改变这次整数代表选择。
4. 在奇数部分，两个根方向E₂₁与VE₂₁V⁻¹在εt_j上作用的行列式为2ε²/p² modn，是单位；解一次二维线性同余修正到奇数平方精度。根参数用CRT保持二进精度。
5. n偶时再用一次L(bx)补第二坐标的二进精度；最后得到w_out≡εt_j modb²。
6. 两列均R本原，Γ(b²,R)的精确纤维作用将其真正送到εt_j。执行(6.2)对应的零和p平均，再接独立已证的零触发尾部，全系统归零。

这些步骤对整个(1.1)使用相同算术条件。零触发依赖的是先行端点含零尾部、3p、4p与宽尾部，不循环调用本文新合并的区间证明。单个反射的正向逆、扩环与完整列尺度已在前面准备好，未把模逆当成有理逆。
