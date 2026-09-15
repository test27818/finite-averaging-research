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

[临界尺度下界](composite_critical_scale_and_conjecture.md)排除了十平均11至15元以及十二平均13至15元的全称G充分性；16元G自动满足，被H的定义排除。故
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
