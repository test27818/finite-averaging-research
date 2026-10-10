from lecture_texts import INTRO, before, after, replace, lemma, prop

INTRO['12_even']=r'''
\section{本讲的分支与共同坐标}
本讲处理 $2<r<p$ 的偶数余量，仍从已建立的核心出发。
写 $r=2t$、$m=p+t$，并令
\[
a=tu+v,\qquad z=u,
\qquad (A,B,C)=(tu+v,tu-v,-pu).
\]
这里换基是整数幺模换基，因而本原性等价于 $\gcd(u,v)=1$。
块差分的最大公因子为 $\gcd(2v,mu+v)$，由此得到
\[
\begin{cases}
\gcd(v,m)=1,&t\text{ 奇},\\
\gcd(v,m)=1,\ u+v\text{ 奇},&t\text{ 偶}.
\end{cases}
\]
奇偶分类来自这里：$t$ 偶时 $m$ 奇，模 $2$ 的信息必须另外保留。

先处理内部 $4\le r\le p-3$。标准反射有至少两个；
当 $t$ 为偶数且还有第三个反射时，用三个反射处理完整方向和尺度。
两个内部边界再增加一个迹为 $\pm2$ 的返回。
最后单独处理 $r=p-1$，其中 $p=5$ 需要一组明确矩阵。
'''
before('12_even',lemma('lem:binary-depth'),r'''
\section{一个预备步骤：把二进深度降到一}
当 $a,z$ 奇偶相反时，其中的偶数可能被很高的 $2$ 幂整除。
下面的返回把这个指数逐次减一。
它与整数平方和下降不同：每次允许重新选本原参数，下降量是 $v_2(az)$。
若某个参数已经为零，可以直接处理相应终端；深度论证只讨论 $az\ne0$。
''')
replace('12_even',r'整数输出为 $((p-2j-s)a+Dz,-a)$，',r'''
所选 $D$ 的二进赋值恰为 $1$，而当前 $4\mid a$、$z$ 为奇数。
因此第一坐标是“被 $4$ 整除的数”加“恰被 $2$ 整除的数”，其赋值必为 $1$。
整数输出为 $((p-2j-s)a+Dz,-a)$，''')
before('12_even',lemma('lem:even-core'),r'''
\section{偶数内部：从标准反射到终端}
先取得一个可能很深的同余群，再通过实际可逆倍率反演 $t$ 的奇部。
这样控制层的素因子就只剩 $n$ 的素因子，后面的局部调整才能在同一控制层内完成。
''')
replace('12_even',r'写 $r=2t,m=p+t$，',r'''
\par\noindent\textbf{第一阶段：两个标准反射给出根。}
写 $r=2t,m=p+t$，''')
replace('12_even',r'互补混合给 $F_c=',r'''
\par\noindent\textbf{第二阶段：用夹乘反演奇数倍率。}
互补混合给 $F_c=''')
replace('12_even',r'引理\ref{lem:inverse}使 $H^{-1}$ 可实现，',r'''
因为 $\det H=\det J_{s_0}=d$ 在 $R_0$ 中已经为单位，
矩阵 $HJ_{s_0}^{-1}$ 的行列式为 $1$，可以使用已有深同余群来实现它的逆。
这一步避免了直接把可能整除旧控制层的 $c$ 当作安全单位。
引理\ref{lem:inverse}使 $H^{-1}$ 可实现，''')
replace('12_even',r'若 $t$ 奇，已有',r'''
\par\noindent\textbf{第三阶段：$t$ 为奇数的情形。}
若 $t$ 奇，已有''')
replace('12_even',r'设 $t$ 偶且 $8\le r\le p-5$。',r'''
\par\noindent\textbf{第四阶段：有三个反射的偶 $t$。}
设 $t$ 偶且 $8\le r\le p-5$。''')
replace('12_even',r'比值 $(d+n)/d,(d+2n)/(d+n)$',r'''
\par\noindent\emph{先控制二进方向。}
比值 $(d+n)/d,(d+2n)/(d+n)$''')
replace('12_even',r'因此覆盖赋值一的全部模 $16$ 方向；',r'''
把 $x$ 写成 $2w$、$w$ 奇，则模 $16$ 的 $x$ 对应模 $8$ 的四个奇单位。
乘 $\kappa\equiv3\pmod8$ 和变号生成这四个类，因此覆盖赋值一的全部模 $16$ 方向；''')
replace('12_even',r'奇素数处用 $G_s=',r'''
\par\noindent\emph{再控制奇素数方向，同时固定二进方向。}
奇素数处用 $G_s=''')
replace('12_even',r'尺度模 $m$ 的变化由 $R$ 单位给出，',r'''
\par\noindent\emph{最后匹配单位尺度。}
此时方向相同，所以当前列与目标列模控制层只差一个单位。
需要证明这个有限单位来自真正的 $R$ 单位。
尺度模 $m$ 的变化由 $R$ 单位给出，''')
replace('12_even',r'逐次取素数幂并用指数 CRT 完成所有精度。',r'''
这里使用的升位事实如下。若 $\ell$ 为奇素数，$u=1+\ell^b c$、$\ell\nmid c$，
则二项式展开给
\[
v_\ell(u^\ell-1)=b+1.
\]
对 $\ell=2$，同样结论在 $b\ge2$ 时成立。
所以这样的单位的连续素数幂逐层产生整个主单位核。
各局部核的阶为对应素数的幂，用中国剩余定理选指数就能同时实现所有分量。
逐次取素数幂并用指数 CRT 完成所有精度。''')
replace('12_even',r'剩下 $r=4$，',r'''
\par\noindent\textbf{第五阶段：只有两个标准反射的内部边界。}
剩下 $r=4$，''')
replace('12_even',r'该参数属于 $nR$，二进赋值恰为 $2$。',r'''
这个新根参数的作用是减少旧根理想中过多的 $2$ 因子。
该参数属于 $nR$，二进赋值恰为 $2$。''')
before('12_even',lemma('lem:upper-boundary'),r'''
\section{上边界的重叠反射}
余量达到 $r=p-1$ 时，内部公式的部分库存已经耗尽。
本节改用重叠反射：先从第一块与载体取一个组，
保留新值中的 $p-1$ 份，再以另一组及其补组重新组成两个 $p$ 块。
两个相邻输出仍会给三角商，机制与上一节一致，但具体计数必须重新列出。
''')
replace('12_even',r'对 $p=5,n=14$，取',r'''
\par\noindent\textbf{最小边界 $p=5,n=14$。}
这里直接列出三个已有真实分组的矩阵，先得到含额外因子 $3$ 的根。
随后一次夹乘让 $3$ 成为可逆倍率，根理想便由 $84R$ 化为 $28R$。
对 $p=5,n=14$，取''')

INTRO['13_counting']=r'''
\section{把所有计数公式放进同一个模型}
上半带为 $n=3p+s$、$1\le s<p$，即 $r=p+s$。
此时载体有多于 $p$ 个位置，只平均一组不足以制造这么多相同新值，
所以通常先平均两组组成相同、位置不交的来源。
本讲把“来源—库存—输出—返回矩阵”一次讲清楚，下一讲只需填写计数。

设旧核心的三种数值为 $A=a$、$B=rz-a$、$C=-pz$。
一组来源取 $i,j,k$ 份三种值，$i+j+k=p$，产生的新值为
\[
D=\frac{iA+jB+kC}{p}
 =\frac{(i-j)a+(rj-pk)z}{p}.
\]
若做 $q_0$ 组相同组成的不交平均，就产生 $q_0p$ 个 $D$。
保留 $r$ 份作载体以后，剩余总数恰是 $2p$，可分成一个输出组及其补组。
所有自由度只剩第一输出组的四个计数。

\section{逐项读懂库存与返回公式}
'''
replace('13_counting',r"新值为 $D=(\alpha a+\beta z)/p$，新参数 $z'=-D/p$；",r'''
新载体值满足 $-pz'=D$，所以
\[
z'=-\frac{\alpha a+\beta z}{p^2}.
\]
第一输出组的均值为
\begin{align*}
a'&=\frac{xA+yB+uC+vD}{p}\\
&=\frac{p(x-y)+\alpha v}{p^2}a
 +\frac{pry-p^2u+\beta v}{p^2}z.
\end{align*}
这分别给出矩阵的第二行与第一行；''')
before('13_counting',r'\begin{corollary}\label{cor:resource}',r'''
\section{为什么相邻输出产生剪切}
输出从 $(x,y,u,v)$ 改为 $(x-1,y-1,u+2,v)$，
总项数不变，$x-y$ 也不变，所以两张表仍然迹零。
右上项的变化为 $-pr-2p^2=-pn$；这个倍数恰好让两反射的商成为三角矩阵。
随后与交换前两个块的 $\Sigma$ 作交换子，便消去对角部分，留下上剪切。

对同一个参数 $(p,r)$，如果数对 $(\alpha,H)$ 有几组，
上剪切参数可以用裴蜀等式合并，而横向系数也可以合并。
下面的推论明确说明计数表需要提供哪两个最大公因子，因而下一讲的任务成为有限整数计数。
''')
replace('13_counting',r'令 $R$ 为所有约分倍率',r'''
\par\noindent\textbf{根与控制层。}
令 $R$ 为所有约分倍率''')
replace('13_counting',r'规范反射 $J/p^2$ 模 $n$',r'''
\par\noindent\textbf{有限方向与尺度。}
规范反射 $J/p^2$ 模 $n$''')

INTRO['14_upper']=r'''
\section{本讲只负责供应上一讲的计数表}
第\ref{app:upper}讲已经证明：只要计数表产生正确的两组最大公因子，
就能接上共同终端。本讲不再重复算术输送，而按位置容量选择来源和输出。
记 $s=n-3p$、$r=p+s$，需要覆盖 $1\le s<p$。

\begin{center}
\begin{tabular}{p{.35\textwidth}p{.5\textwidth}}
\toprule 参数段 & 选择方式\\\midrule
$p\ge83,\ r>3p/2$ & 来源偏向载体，输出用一个整数 $l$ 调节\\
$p\ge83,\ 10\le s\le(p-1)/2$ & 平衡来源，输出用整数 $e$ 调节\\
$p\ge83,\ 1\le s\le9$ & 两个相邻 $\alpha$，再取两个相邻 $h$\\
$11\le p<83,\ s\ge10$ & 前两类公式的更精细边界比较\\
$11\le p<83,\ 1\le s\le9$ & 五返回公式，加上剩余的完整计数表\\
\bottomrule
\end{tabular}
\end{center}
第一列是证明范围，第二列是实际资源的来源。
有限表只承担最后一行剩余的有限参数，没有取代任何无穷范围的论证。
'''
before('14_upper',lemma('lem:upper-supply'),r'''
\section{大素数：三个范围的明确公式}
每种公式均把四个输出容量限制压缩成一个整数区间 $L\le e\le U$（或 $L\le l\le U$）。
我们需要两张相邻表，因此必须证明 $L+1\le U$。
这比只找到一张可行表更强：第二张表正是制造三角倍率和剪切的来源。
''')
replace('14_upper',r'\emph{靠近 $4p$。}',r'''\par\noindent\textbf{第一类：靠近 $4p$。}''')
replace('14_upper',r'\emph{中部。}',r'''\par\noindent\textbf{第二类：上半带中部。}''')
replace('14_upper',r'\emph{九个低偏移。}',r'''\par\noindent\textbf{第三类：紧邻 $3p$ 的九个偏移。}''')
replace('14_upper',r'由 $p/6\le\alpha\le(p+11)/6$、$s\ge10$ 逐项成立，且保证来源库存。',r'''
下面说明四个比较的余量。因为 $p/6\le\alpha\le(p+11)/6$，第一式在 $p\ge25$ 时成立；
第二式左侧至多比 $\lfloor p/2\rfloor$ 大 $6$，而 $s-1\ge9$；
第三式使用 $s\le(p-1)/2$，在 $p\ge15$ 时足够；
第四式由 $3\alpha\ge\lceil p/2\rceil$ 及 $\lfloor s/2\rfloor\ge5$ 成立。
此外 $4\alpha\le p$ 保证第一类来源不超量，$6\alpha\ge p$ 保证载体来源容量，
$s\le p/2$ 保证新值 $D$ 的库存。因此所列整数区间确实包含相邻两个输出。''')
replace('14_upper',r'三种公式均满足迹零条件。',r'''
\par\noindent\textbf{三类计数的最大公因子。}
到这里已经有真实反射，但还需把它们合成足够浅的根与同余群。
这一步只计算前一讲的 $H=n(2j+\alpha)-2p^2$。
三种公式均满足迹零条件。''')
before('14_upper',lemma('lem:upper-small'),r'''
\section{偏移至少10的小素数}
大素数界 $83$ 为三类公式提供了同一个方便界，并不表示其下所有参数都要查表。
当 $s\ge10$ 时，前两类容量不等式在更小的素数上仍成立。
下面逐一把小边界写清楚，避免把这一整片参数误交给有限证书。
''')
before('14_upper',lemma('lem:small-supply'),r'''
\section{九个低偏移：通式与剩余数表}
在最后九个偏移中，先使用已有五返回公式。
它在两张相邻输出之外增加一次沿整数守恒关系的输出交换，直接给出 $U(-n)$。
满足显式截点的参数都由该公式处理，余下参数才进入附录。
''')
replace('14_upper',r'余下的114组参数及233对相邻表完整列在',r'''
\par\noindent\textbf{有限剩余。}
余下的114组参数及233对相邻表完整列在''')
replace('14_upper',r'在此例，来源 $(4,2,5)$、',r'''
\par\noindent\textbf{唯一单列参数 $(p,s)=(11,3)$。}
此时 $n=36$，一般最大公因子接口改由两组明确矩阵完成。
在此例，来源 $(4,2,5)$、''')

INTRO['15_wide']=r'''
\section{到底还剩哪些宽维数}
第\ref{ch:descent-finish}讲已证明 $n\ge4p-2+d_p(n)$ 的充分性，
特别是所有 $n\ge4p+\lceil\log_2p\rceil$。
因此，若 $n\ge4p$ 仍未被覆盖，必在 $4p$ 上方一个很短的区间内，
而且 $n$ 必有很多不同素因子。后一个条件反而迫使 $p$ 很大，提供了充足的构造库存。

本讲继续沿用已有二维工具，换成重数为 $(2p,p,p+s)$ 的加权核心。
方法依次是：先压缩、用五步反射取得根和深层、用安全数字获得单位、
完成各局部方向，最后送到带零的 $4p$ 元子系统。
这里调用的 $4p$ 结论已经由整数下降独立证明。
'''
replace('15_wide',r'由引理\ref{lem:integer-range}，只须考虑',r'''
\par\noindent\textbf{第一步：剩余范围自动带来足够的容量。}
由引理\ref{lem:integer-range}，只须考虑''')
replace('15_wide',r'保护单点 $w$ 及见证，',r'''
\par\noindent\textbf{第二步：建立加权三块核心。}
保护单点 $w$ 及见证，''')
replace('15_wide',r'取 $\epsilon=\pm1$、',r'''
\par\noindent\textbf{第三步：五次平均组成反射。}
取 $\epsilon=\pm1$、''')
replace('15_wide',r'保留旧 $A$ 的三步反射为',r'''
\par\noindent\textbf{第四步：第二组反射与共同根理想。}
保留旧 $A$ 的三步反射为''')
replace('15_wide',r'一般保留 $A$ 的三步返回为',r'''
\par\noindent\textbf{第五步：可用数字覆盖足够多的单位。}
此时已经有深同余群，可以安全地激活与控制层互素的返回的逆。
我们从位置计数读出一个连续数字区间，证明其安全数字足以生成模 $n$ 单位群。
一般保留 $A$ 的三步返回为''')
replace('15_wide',r'在 $(z,y)=(z,a+pz)$ 中，',r'''
\par\noindent\textbf{第六步：逐素数调整方向。}
在 $(z,y)=(z,a+pz)$ 中，''')
replace('15_wide',r'单位 $d_1/d_0=1-n/d_0$',r'''
\par\noindent\textbf{第七步：匹配尺度并送到含零子系统。}
单位 $d_1/d_0=1-n/d_0$''')
