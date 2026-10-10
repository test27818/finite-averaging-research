

# C23.3 四原子大载体反射的一般计数

从 \(\mathcal L\) 先平均两个不交、组成相同的组
\[
(A^i,B^j,C^k),\qquad i+j+k=p.
\]
记
\[
\alpha=i-j>0,\quad \beta=rj-pk=nj-p(p-\alpha).
\]
得到 2p 份 D=(alpha a+beta z)/p。保留 r=p+s 份 D；剩余旧 A,B,C 和新 D 数目为
\[
p-2i,\quad p-2j,\quad r-2k,\quad p-s.
\]
平均一组 (A^x,B^y,C^u,D^v)，再平均其 p 元补组。注意这里只有**一个输出组及其补组**，不是上半带的两条重复输出行。

完整容量是
\[
\begin{gathered}
2i\le p,\quad2j\le p,\quad2k\le r,\qquad x+y+u+v=p,\\
0\le x\le p-2i,\quad0\le y\le p-2j,\quad
0\le u\le r-2k,\quad0\le v\le p-s.
\end{gathered}
\tag{3.1}
\]
当
\[
p(x-y)+\alpha v=\beta
\tag{3.2}
\]
时，总返回恰为 p^-2 乘
\[
J=\begin{pmatrix}\beta&Q\\-\alpha&-\beta\end{pmatrix},
\quad Q=pry-p^2u+v\beta.
\tag{3.3}
\]
定义 pf=beta²-alpha Q，则
\[
J^2=pfI,\qquad pf=p^4\pmod n.
\tag{3.4}
\]
这里 f 是整数：由 beta=alpha v mod p，有 Q=v beta mod p，故 p 整除 beta²-alpha Q。又 gcd(p,n)=1，故 f 非零且与 n 互素。

每个反射因此有真正的正向射影逆：重复同样四次平均。换到始终幺模的 (z,y)=(z,a+pz) 基，实际模 n 作用为
\[
p^{-2}J\equiv
\begin{pmatrix}1&-\alpha/p^2\\0&-1\end{pmatrix}.
\tag{3.5}
\]
这也直接证明它保持合法性。

# C23.5 换块交换子、双向根和主同余控制

先给适用于一般计数证书的接口。若同一个 alpha,j,v 有两条反射，后一条取 (x-1,y-1,u+2,v)，记平方系数为 f,g，则
\[
g=f+\alpha n,\qquad
T=J_f^{-1}J_g=
\begin{pmatrix}1&-\beta n/f\\0&g/f\end{pmatrix}.
\tag{5.1}
\]
与角色交换 S 的交换子为
\[
\boxed{[S,T]=U\!\left(\frac{nH}{g}\right),\quad
H=2\beta+r\alpha=n(2j+\alpha)-2p^2.}
\tag{5.2}
\]
这里 U(t)=(1,t;0,1)。所有逆都已由实际反射和角色交换提供。

令 R0 是由各倍率 g/f 及 f/g 生成的整数环。对采用 j=alpha h 的计数公式，gcd(f,g)=1：因为 gcd(p,alpha)=1、j=alpha h，(3.4) 给 f=p³ mod alpha，再用 gcd(f,n)=1。因此 R0 恰为相应 f,g 的素因子局部化。小参数证书独立核对所有 f,g 的素因子确实被这些**约分后**的倍率反演；没有假定约掉的公因子免费可逆。

各 T 共轭 U 将根参数乘 f/g。由共轭、求逆、根参数相加和整数 Bezout，得到
\[
U(\delta nR_0),\qquad\delta=\gcd\{H\}.
\tag{5.3}
\]
大 p 公式中，相邻 h 的 H 相差2alpha n，而两个 alpha 互素。故 delta|2n；又 H=-2p² mod n，delta 没有奇素因子。n 奇时有奇 alpha 给奇 H，所以 delta=1；n 偶时一条偶 alpha 排除额外的4，故 delta=2。

解释横向根时无需把换基自身当成可执行操作。对任一反射 J，设
\[
P=(e_1,Je_1)=\begin{pmatrix}1&\beta\\0&-\alpha\end{pmatrix}.
\]
精确有
\[
P^{-1}U(t)P=U(-\alpha t),\qquad
P^{-1}J U(t)J^{-1}P=L(\alpha t/\det J).
\tag{5.4}
\]
置 h*=delta n，第二式取 t=(det J)h*x，清去分母；于是 P 基下已有 U(alpha h* R0)、L(alpha h* R0)。深同余引理给 Gamma(alpha² h*²,R0)。换回原基，因 alpha P^-1 和 P 都整于 R0，有
\[
\Gamma(\alpha^3h_*^2,R_0)\text{ 正向可执行}.
\tag{5.5}
\]
不同 alpha 的 gcd 为1时，这些群生成包含 Gamma(h*²,R0) 的群。理由是先模各 level 的公倍数：各素数幂下的主同余条件是嵌套的，CRT 和 SL2 的有限环满射使它们的乘积给 gcd level，再接已知深层。这一步不要求任何 alpha 是 R0 单位。

故大 p 一律已有 Gamma(n²,R0) 或 Gamma(4n²,R0)。小参数证书除一个补充外给 gcd(alpha)=1、delta 属于{1,2,4}，且 delta 的素数都整除 n，故同样得到仅支持于 n 的控制层。例外 $(11,3)$ 由守恒输出交换构造处理。

下文统一使用更深但方便的
\[
\mathfrak M=\begin{cases}n^4,&n\text{ 奇},\\64n^4,&n\text{ 偶}.
\end{cases}
\tag{5.6}
\]
上述控制层均包含 Gamma(mathfrak M,R0)。
