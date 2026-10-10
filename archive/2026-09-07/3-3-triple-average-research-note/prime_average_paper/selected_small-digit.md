

# C17.1 已有的对称坐标揭示一个乘法群

九偏移核心写作
\[
\mathcal K(a,z)=
\bigl(a^p,(rz-a)^p,(-pz)^r\bigr),
\qquad r=p+s,\ n=2p+r=3p+s.
\]
令
\[
y=a+pz,\qquad \eta=y-\frac n2z=a-\frac r2z.
\tag{1.1}
\]
η是两个等大p块数值之差的一半。z记录它们共同的均值方向，η记录差方向。换块使η变号而不改z。

旧两个互补p平均给
\[
F_q:
(a,z)\longmapsto
\left(\frac qp\,a+\frac{r(p-q)}{2p}z,\ z\right),
\qquad q\text{奇},\quad1\le q\le p.
\]
在(z,η)坐标中，它恰为diag(1,q/p)。在已有根和深核之后，F₁及安全F_q的正向逆已由旧夹乘定理取得，所以
\[
C_q=F_qF_1^{-1}
\]
给diag(1,q)。以一个共同非零尺度选择射影矩阵代表，令D_q=q⁻¹C_q，于是
\[
\boxed{
D_q=\begin{pmatrix}
q^{-1}&0\\
\frac n2(q^{-1}-1)&1
\end{pmatrix}
\quad\text{在}(z,y)\text{基中};
\qquad
(z,\eta)\mapsto(q^{-1}z,\eta).
}
\tag{1.2}
\]
D_q不需要执行一次额外的q⁻¹数乘；实际词为C_q，D_q只是同一射影作用的代表。

当n偶、q奇时，n(q⁻¹−1)/2属于nR。因此
\[
\boxed{D_q:\quad z\mapsto q^{-1}z,\quad y\mapsto y\pmod n.}
\tag{1.3}
\]
全部分母来自已真实反演的小数字q。换块的负代表
\[
D_{-1}=-S=\begin{pmatrix}-1&0\\-n&1\end{pmatrix}
\]
也在这一乘法族中。

这就是此处“分裂环面”的具体含义：两个自然特征方向中的一个缩放，另一个保持。它已存在于原平均操作中，不是引入新的抽象可执行性假设。

# C17.2 所需的小数字总存在：一个一般计数引理

**引理。** 设p≥11为整数，n为偶数且n<4p。则存在奇整数q满足
\[
1<q\le p,\qquad q\equiv3\text{或}5\pmod8,\qquad\gcd(q,n)=1.
\tag{2.1}
\]

证明先检查3、5、11、13。p=11或12时，若3、5、11都不与n互素，n被165整除，与n<4p≤48矛盾。所以此时已有合适q。

设p≥13。如果四个数字都不与n互素，则3·5·11·13整除n。记n的不同奇素因子数为d≥4，令
\[
\rho=\prod_{\ell\mid n,\ \ell\text{奇}}(1-\ell^{-1}).
\]
考察q=3+8t、1≤q≤p组成的等差数列，项数L≥(p−4)/8。每个奇平方自由除数在该数列中的计数与L除以该除数相差小于1。容斥故给与n互素的项数至少
\[
L\rho-2^d.
\]
因p>n/4且ρ≤1，
\[
L\rho>\frac{n\rho}{32}-\frac12.
\]
而
\[
n\rho\ge2\prod_{\ell\mid n,\ \ell\text{奇}}(\ell-1)
\ge1920\cdot6^{d-4}.
\]
前四个因子来自3、5、11、13；每增加一个不同奇素数，其ℓ−1至少为6。因此
\[
L\rho>60\cdot6^{d-4}-\frac12>2^d.
\]
至少一个q符合要求。证毕。

这个引理不假设p或n为素数，也不要求分解所有候选q。算法可先检查四个小数，必要时沿3 mod8的数列计算gcd。有限测试不是该存在性证明的依据。

# C17.3 同一个二进单位规则

若q≡3或5 mod8，则
\[
v_2(q^2-1)=3.
\]
因此q²的幂在模2^L下生成全部1 mod8的单位，−1和q再覆盖模8的四个奇类，得到
\[
\boxed{\langle-1,q\rangle=(\mathbb Z/2^L\mathbb Z)^\times
\qquad(L\ge3).}
\tag{3.1}
\]
这是逐次平方的初等推论：若u=1+8c、c奇，则u^{2^j}−1的二进赋值为3+j。先选符号及q的指数奇偶匹配模8，再逐位选择q^{2^{j+1}}的有无，就能匹配任意奇单位，不需要离散对数黑箱或有限群轨道表。

(3.1)只主张这些已可用整数单位的二进像足够，不主张它们单独生成所有奇数模数的单位。后者仍由旧基础单位模n满射承担。

# C17.4 方向只从原根反射生成

沿用[两根列提升](two_root_column_completion.md)：每条根反射J的计数差α=i−j给
\[
T_\alpha=S\widehat J
\equiv\begin{pmatrix}1&-\alpha/p^2\\0&1\end{pmatrix}\pmod n.
\]
旧根供应已要求gcd α_i=1；整数Bezout给c_i满足Σc_iα_i=1。设
\[
\boxed{V=\prod_iT_{\alpha_i}^{c_i}
\equiv\begin{pmatrix}1&-p^{-2}\\0&1\end{pmatrix}\pmod n.}
\tag{4.1}
\]
本构造不再对tr V模4提任何条件。

**环与本原性的账本。** R取旧根对约分倍率实际生成的环，再加入p及所有安全小数字的素因子。旧根供应的核验检查了每条所用根反射的平方系数均为R单位，因此\(\widehat J\)、其逆及S都在GL₂(R)，故V也在GL₂(R)。这比上一轮使用任意独立direction反射时的前提强，但这里直接由已有根供应得到，不需要新增局部化。

对于 $(p,s)=(11,3)$，使用守恒输出交换构造所列的 $\alpha=2,3$ 反射及其深核。整数等式 $-2+3=1$ 给出同一粗略平移；不需要辅助13的局部群计算。

因此所有后续矩阵都在同一个GL₂(R)中。当前R本原列经它们作用仍R本原；共同有理尺度只作分析代表，不额外平均或扩增位置。**无需每次重新取整数本原代表，也无需Smith准备。**

# C17.5 共同前提与目标

令δ=1（n奇）或δ∈{2,4}（n偶），h=δn，Q=h²。旧root_pairs、基础小数字和Morris／Serre给
\[
L(hR),\quad\Gamma(Q,R),\quad
R^\times\twoheadrightarrow(\mathbb Z/n\mathbb Z)^\times.
\]
全输入入口和零触发尾部沿用旧证明。它们均先于本构造终端过程，不需要direction或binary_unit。

显式终端仍为
\[
t_j=(1,p^2-nj),\qquad0\le j<\delta.
\]
选j+1份A、j份B、p−1−2j份C就恰好零和。p≥11、r=p+s保证非负容量；t_j第一坐标为1，自动本原。

从任意合法R本原列(z,y)出发，先以V的非负幂把它变为
\[
p^2z\equiv y\pmod n.
\]
再取ε∈R×使ε≡z modn，得到
\[
(z,y)\equiv\epsilon(1,p^2)\pmod n.
\tag{5.1}
\]
此时z、y在二进处均为单位（n偶时）；全程保持R本原性。

# C17.6 偶数n的首坐标：先用乘法自由度完成

写n=2ᵃm，m奇，a≥1；记h=2ᵇm、v=2ᵇ、M=v²，则Q=Mm²且b≥2。

按第2节取q，利用(3.1)求
\[
(-1)^e q^t\equiv z/\epsilon\pmod M,
\qquad e\in\{0,1\},\ t\ge0.
\]
执行D_{-1}^eD_q^t。由(1.2)—(1.3)得到
\[
z'\equiv\epsilon\pmod M,\qquad y'\equiv\epsilon p^2\pmod n.
\tag{6.1}
\]
这一步可能改变z的奇数模m分量，下面用原V修正，但冻结整个二进分量。

由于V mod2是非平凡上平移，V²≡I mod2，逐次平方得
\[
\boxed{V^M\equiv I\pmod M.}
\tag{6.2}
\]
这个结论对任何这样的V成立，无需tr V≡2 mod4。M是2幂，故模m可逆。取
\[
k=M\left[p^2(z'-\epsilon)(y')^{-1}M^{-1}\right]_m.
\]
执行V^k，得到
\[
\boxed{z''\equiv\epsilon\pmod M,\quad
z''\equiv\epsilon\pmod m,\quad
y''\equiv\epsilon p^2\pmod n.}
\tag{6.3}
\]
因M被v整除，第一坐标已经匹配模h，而且二进最终精度一次到位。

这里没有使用V在二进方向上形成长循环。V只负责奇数处加法，乘法D_q负责二进处缩放，两者用指数的互素性隔离。

n奇时δ=1，(5.1)已是模h目标，跳过本节。

# C17.7 终端选择、两根消元、一次下根

选择
\[
j\equiv\epsilon^{-1}\frac{\epsilon p^2-y''}{n}\pmod\delta,
\quad0\le j<\delta.
\]
于是当前列w和目标w_T=εt_j相符模h。

令E=E₂₁、X=VEV⁻¹。在模m目标列上，
\[
\det(Ew_T,Xw_T)=2\epsilon^2/p^2
\]
为单位。清除X的分母后，按[上一轮两根消元](two_root_column_completion.md)解一次二维线性方程；根参数通过CRT选为在二进部分恒等，得到w′≡w_T modm²。由于本构造V∈GL₂(R)，X本来就在M₂(R)，清分母仅便于用整数系数计算，不扩大环。

n奇时Q=m²，已全部完成。

n偶时第一坐标保持ε modM；最后用一个已有L(hr)修正第二坐标模M，并选r≡0 modm保持m²部分。这就是上轮第7节的最后一个线性同余式，不再需要规范化循环。得到
\[
w_{\rm out}\equiv w_T\pmod Q.
\]
两列都R本原，由旧Γ(Q,R)精确纤维真实到达w_T；随后零和组平均产生p个零，接旧尾部完整归零。
