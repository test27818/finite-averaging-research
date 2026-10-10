INTRO, BEFORE, AFTER, REPLACEMENTS = {}, {}, {}, {}

def before(ch, anchor, text): BEFORE.setdefault(ch, []).append((anchor, text))
def after(ch, anchor, text): AFTER.setdefault(ch, []).append((anchor, text))
def replace(ch, old, new): REPLACEMENTS.setdefault(ch, []).append((old,new))
def lemma(key): return '\\begin{lemma}\\label{'+key+'}'
def prop(key): return '\\begin{proposition}\\label{'+key+'}'

PREAMBLE=r'''
\usepackage[xetex,top=24mm,bottom=25mm,left=27mm,right=25mm,headheight=15pt]{geometry}
\usepackage{fontspec,xeCJK}
\setmainfont{Times New Roman}
\setCJKmainfont[BoldFont=SimHei,ItalicFont=KaiTi]{SimSun}
\setCJKsansfont{Microsoft YaHei}
\setCJKmonofont{SimSun}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{booktabs,longtable,array,graphicx}
\usepackage{fancyhdr}
\usepackage[unicode,bookmarksnumbered=true,colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\usepackage{xcolor}
\newcommand{\Z}{\mathbb Z}
\newcommand{\Q}{\mathbb Q}
\newcommand{\F}{\mathbb F}
\newcommand{\R}{\mathbb R}
\newcommand{\SL}{\operatorname{SL}}
\newcommand{\GL}{\operatorname{GL}}
\newcommand{\diag}{\operatorname{diag}}
\newcommand{\rad}{\operatorname{rad}}
\newcommand{\cont}{\operatorname{cont}}
\newcommand{\Um}{\operatorname{Um}}
\newcommand{\ord}{\operatorname{ord}}
\newtheorem{theorem}{定理}[chapter]
\newtheorem{lemma}[theorem]{引理}
\newtheorem{proposition}[theorem]{命题}
\newtheorem{corollary}[theorem]{推论}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{定义}
\newtheorem{example}[theorem]{例}
\newtheorem{remark}[theorem]{说明}
\renewcommand{\proofname}{证明}
\renewcommand{\contentsname}{目录}
\renewcommand{\bibname}{参考文献}
\renewcommand{\tablename}{表}
\renewcommand{\figurename}{图}
\renewcommand{\chaptername}{讲}
\renewcommand{\appendixname}{附录}
\numberwithin{equation}{chapter}
\setcounter{tocdepth}{1}
\setcounter{secnumdepth}{2}
\setlength{\parindent}{2em}
\setlength{\parskip}{4pt plus 1pt}
\linespread{1.16}
\emergencystretch=3em
\allowdisplaybreaks[2]
\raggedbottom
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small 素数平均：有限可达性与最优阈值}
\fancyhead[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}
\makeatletter
\def\@makechapterhead#1{\vspace*{8mm}{\parindent\z@\raggedright\normalfont
 \ifnum\c@secnumdepth>\m@ne\if@mainmatter
 {\Large\sffamily\color{blue!40!black}\@chapapp\ \thechapter\par}\vskip12pt\fi\fi
 \interlinepenalty\@M\LARGE\bfseries #1\par\nobreak\vskip24pt}}
\def\@makeschapterhead#1{\vspace*{8mm}{\parindent\z@\raggedright\normalfont
 \interlinepenalty\@M\LARGE\bfseries #1\par\nobreak\vskip24pt}}
\makeatother
\hypersetup{pdftitle={素数平均：有限可达性与最优阈值},pdfsubject={中文数学讲义}}
'''

PREFACE=r'''
\chapter*{怎样阅读这份讲义}
\addcontentsline{toc}{chapter}{怎样阅读这份讲义}
把几个数替换成它们的平均值，是一个几乎不需要准备知识就能提出的操作。
然而，要求在有限步后\emph{精确}得到相同数值，会把问题带到整数同余、二维矩阵与算术群。
这份讲义围绕一条完整结论展开：对奇素数 $p$，位置数达到 $2p+1$ 以后，
有限可达性由一个最大公因子的素因子完全决定，而 $2p+1$ 不能再降低。

讲义假定读者熟悉线性代数、整除与同余、中国剩余定理，以及群、环和群作用的基本定义。
对本题另外需要的概念，例如素数赋值、局部化环、本原列、射影返回和主同余子群，
都在首次使用时说明。两个较深的算术群定理作为已发表定理引用；
这里完整讲解其假设、结论，以及它们怎样嵌入平均问题的证明。
无需预先学习算术群的一般理论。

\section*{一条主线，两种终止方式}
证明有两种主要工作方式。位置较多时，可以始终选择整数平均，
并保证平方和严格下降。平方和取非负整数值，这就把无限过程排除。
位置接近阈值时，可用于选择的位置太少，必须允许分数。
这时先把配置变为三个等值块，用两个参数描述它，再用一系列真实平均控制这两个参数。
目标是先造出一个和为零的 $p$ 元组，随后由已有的含零收尾完成。

因此，阅读矩阵构造时应始终保留下面的图景：
\[
\text{原始配置}\ \longrightarrow\ \text{三块核心}
\ \longrightarrow\ \text{零和的 }p\text{ 元组}
\ \longrightarrow\ \text{全零配置}.
\]
中间的矩阵只是记录真实操作的工具。它的两列不是额外增加的两个位置，
矩阵的逆也必须另有正向平均序列才能使用。

\section*{各部分怎样衔接}
第1--2讲建立问题和必要条件，并证明阈值的下界。
第3--5讲先独立取得整数下降、$3p$ 个位置和含零状态的解法。
这些是后面构造可以放心调用的终点。
第6讲处理任意输入到三块核心的入口。
第7--9讲集中建立矩阵和同余工具；它们解释后面所有参数构造的共同目的。

第10--14讲按 $n$ 与 $p$ 的关系给出真实返回。
此处每一张计数表都回答一个具体问题：某种矩阵作用能否用现有数量的位置完成。
第15讲补齐宽维数中整数下降的少量容量不足情形。
第16--17讲处理 $p=3,5,7$ 所必需的基例；这些例子属于总定理的证明。
第18讲将所有范围合并。

第一次阅读，建议依次读完第1--9讲，再完整读一遍第10讲的奇数余量构造。
这样便能在一个完整实例中看到“来源分组、返回矩阵、剪切、同余群、终端”的全部环节。
然后阅读其他参数段。若只想查某个具体 $(p,n)$，可先看第18讲的覆盖表，
再回到相应讲次。目录中的命题、公式及表格均有文内引用。

\section*{记号约定}
\begin{longtable}{p{.18\textwidth}p{.74\textwidth}}
\toprule 记号 & 含义\\\midrule
$p$ & 每次平均所选位置数；主体中为奇素数。\\
$n$ & 配置的总位置数，始终保留这些位置。\\
$a^m$ & 在配置记号中表示 $m$ 个值为 $a$ 的位置，不是数值幂。\\
$X$ & 减去全局均值并清分母、除公因子后得到的本原整数配置。\\
$G(X)$ & 全部坐标差的最大公因子。\\
$d_p(n)$ & $n$ 的不同素因子中不等于 $p$ 的个数。\\
$v_\ell(t)$ & 有理数 $t$ 的分子中 $\ell$ 的指数减去分母中的指数。\\
$U(t),L(t)$ & 二阶上、下三角初等剪切矩阵。\\
$R=\Z[1/D]$ & 只允许 $D$ 的素因子出现在分母中的有理数环。\\
$\Gamma(q,R)$ & $\SL_2(R)$ 中模 $qR$ 等于单位矩阵的子群。\\
$\cont(v)$ & 整数列坐标的最大公因子，称为内容。\\
\bottomrule
\end{longtable}
矩阵统一作用在列向量上，复合从右到左。描述平均序列时则按实际时间顺序叙述。
余量统一写成 $r=n-2p$；上半带另外写 $s=n-3p$，于是 $r=p+s$。
各构造中的临时计数变量只在所在小节内使用。

\section*{证明的来源与有限数据}
本讲义将已有完整证明编排为连贯课程，并恢复原稿中已有的分组说明和推导细节。
涉及小参数的有限表按原有结果收入正文及附录，所需方程、状态和生成元一并给出。
有限表的作用限于已明确列出的有限命题；无穷参数的论证由正文中的引理承担。
配套目录中的有限数据供查阅，正文不要求读者先运行程序。
本次编撰的重点是叙述、衔接和排版，沿用已有数学结果。
'''

INTRO['01_problem']=r'''
\section{从一个小实验开始}
设有七个带编号的位置，数值为
\[
(-3,0,0,0,1,1,1).
\]
每次选择三个位置，将三个数同时替换成它们的平均。
先平均 $(-3,0,0)$，便得到三个 $-1$、三个 $1$ 和一个 $0$。
接着三次选取 $(-1,0,1)$，所有位置都变成零。
这个例子体现两个基本事实：同样的数可以占据多个不同位置；
某次平均产生的零，可以在后面的步骤中继续使用。

我们研究的是：给定有理数配置，是否存在某个\emph{有限}平均序列，使所有位置精确相等。
选取位置的顺序可以依赖输入。不断接近相等还不足以回答问题，因为极限相等与有限步相等是不同的要求。

\section{形式定义与本原中心化}
'''
before('01_problem',r'若 $x$ 非恒定',r'''
总和不变直接来自所选组的总和等于其均值的 $p$ 倍。因此终点没有自由度，
只可能是原全局均值。把这个均值减去以后，目标便变为零。
再乘一个共同整数可以清除所有分母，最后除去各坐标的最大公因子。
这个过程只改变我们描述输入所用的尺度，不改变哪一串平均操作能够成功。
下一讲将把这种相容性写成正式引理。
''')
before('01_problem',r'\begin{theorem}\label{thm:prime}',r'''
\begin{example}[如何算判据]
取五平均、十一位置的配置
\[
X=(1^{10},-10).
\]
它已经零和而且本原。任意两个不同坐标的差都是 $11$，所以 $G=11$。
虽然位置数已达到 $2p+1=11$，它仍然不能归零：模 $11$ 的每个数都等于 $1$，
五平均也保持这个余数。
相比之下，$(-5,0^5,1^5)$ 同样有十一位置，且 $G=1$；
先平均 $(-5,0^4)$，便化成相反值和一个零，从而可解。
\end{example}

\section{主定理究竟断言什么}
''')
before('01_problem',r'本文采用如下约定。',r'''
这里允许 $e=0$，所以 $G=1$ 属于可解条件。
“最终阈值”要求\emph{以后的每一个}位置数都满足判据。
例如在 $n=p$ 时，一步就能把全部位置平均；这并不影响 $2p+1$ 是最优最终阈值。
阈值以下既可能存在可解配置，也可能存在满足 $G=1$ 却不可解的配置。

\section{证明路线与范围划分}
设 $p\ge5$。下表先说明每一部分在证明中承担什么工作，具体构造随后逐讲给出。
\begin{center}
\begin{tabular}{p{.26\textwidth}p{.61\textwidth}}
\toprule 范围或任务 & 主要方法\\\midrule
必要条件、$n=2p$ 的反例 & 共同余数与最低素数赋值\\
$n\ge4p-2+d_p(n)$ & 保留两个等值大块的整数能量下降\\
$n=3p$ & 三个等大块上的整数剪切\\
$2p<n<4p,\ n\ne3p$ & 一般输入压缩、二维返回、有限同余输送\\
其余 $n\ge4p$ & 加权三块核心及同余输送\\
$p=3,5,7$ 的必要小情形 & 显式平均词、下降及有限分类\\
\bottomrule
\end{tabular}
\end{center}
论证中最重要的先后关系是：\emph{先建立含零收尾，再把临界带送到含零状态。}
这样，后半部分每次“造出零和组”之后，都有已经证明的下一步可用。
''')

INTRO['02_obstruction']=r'''
上一讲给出的 $G$ 看似只是对差分取最大公因子，本讲解释它为什么抓住了所有必要的算术条件。
先固定一个素数 $\ell\ne p$，看全部数模 $\ell$ 的余数；
再在阈值下方考察分母中 $p$ 的指数。前者证明“有障碍就不能成功”，
后者用来排除反例中可能存在的分数绕路。
\section{归一化为什么不改变可达性}
'''
before('02_obstruction',lemma('lem:obstruction'),r'''
\section{共同余数不能被平均改变}
从整数输入出发，分母只会增加 $p$ 的幂。因此当 $\ell\ne p$ 时，
所有中间数都仍然有良好的模 $\ell$ 意义：把分母中的 $p$ 替换成其模逆元即可。
若所有数的余数均为 $c$，平均值的余数就是 $p^{-1}(pc)=c$。
关键是本原化保证一个共同余数不可能在某个公因子处恰好全为零。
''')
before('02_obstruction',lemma('lem:fraction'),r'''
\section{读懂最低p进赋值的论证}
对非零有理数 $x$，写 $x=p^h u/v$，其中 $p\nmid uv$，定义 $v_p(x)=h$，并令 $v_p(0)=+\infty$。
例如 $v_3(18)=2$，$v_3(2/9)=-2$。这里不需要完成化或 $p$ 进数域。
只用以下三条初等性质：
\[
v_p(xy)=v_p(x)+v_p(y),\qquad
v_p(x+y)\ge\min(v_p(x),v_p(y)),
\]
以及当两项的赋值不同时，后一不等式取等号。
最后一条可由提取较小的 $p$ 幂直接看出：一个模 $p$ 单位加上一个被 $p$ 整除的数仍是单位。

本题中特别有用的是：若 $1\le k<p$，则 $v_p(ka)=v_p(a)$。
所以一个最低值块被\emph{部分}选中时，不能靠别的更高赋值项抵消它。
所选和再除以 $p$，最低赋值还会下降一。这正是下一个引理的不变量。
''')
before('02_obstruction',prop('prop:lower'),r'''
\section{构造阈值下方的不可解输入}
现在选一个既含 $0$ 又含 $1$ 的配置，使 $G=1$ 自动成立，
同时令任何整数平均都几乎没有选择。负值 $-p$ 与 $p$ 个 $1$ 恰好平衡总和。
''')
before('02_obstruction',r'二平均使用',r'''
\section{二平均的独立结论}
二平均同样属于素数平均，但它的最终阈值为 $4$。
这里直接引用完全混合的已发表刻画，并说明与本题符号的对应。
奇素数的证明不依赖这一引用。
''')

INTRO['03_descent_tools']=r'''
\section{为什么选择整数下降}
设 $E(x)=\sum_i x_i^2$。一次平均的精确能量差是
\begin{align*}
E(x)-E(T_Sx)
 &=\sum_{i\in S}x_i^2-p\bar x_S^2\\
 &=\sum_{i\in S}(x_i-\bar x_S)^2.
\end{align*}
因此，只要所选数不全相等，能量就严格下降。
但在有理数上，严格下降的正数列仍可能无限长。
本部分的策略是让每次平均都保持整数；这样 $E$ 始终为非负整数，下降必然有限。

要使这条策略成立，还必须避免平均过程制造新的模素数障碍。
我们将同时维持四项条件：整数、零和、每个危险素数处不全同余、
至少两个不同数值各占据 $p$ 个位置。
最后一项是后续选择的储备：每次既能产生一个新的 $p$ 重值，又能留住一个旧的 $p$ 重值。
若已处于明确的相反值终端，就直接消去，不再要求维持这项储备。

\section{危险集与未选见证}
'''
before('03_descent_tools',lemma('lem:safety'),r'''
\begin{definition}[危险素数与危险集]
称 $\ell\mid n$ 且 $\ell\ne p$ 为危险素数。
若模 $\ell$ 有一个余数类包含至少 $n-p$ 个位置，称它为主类，
将其余位置构成的集合记为 $F_\ell$。
如果一次平均会使全部位置同余，那么未选的 $n-p$ 个位置已经必须同余。
因此只有这种主类存在时，才有一步制造障碍的风险。
\end{definition}
有些危险素数并无这样的主类；它们对此次整数选择没有额外限制。
有主类时，只需让一个主类外的位置留在选择之外。
而由于主类大小大于 $p$，任意选择后也会留下主类位置。
这就是“预留一个见证”的确切含义。
''')
before('03_descent_tools',lemma('lem:initialize'),r'''
\section{为什么两步就能建立储备}
初始时可以把分析代表由 $X$ 换成 $pX$。
这样所有初值都被 $p$ 整除，任意 $p$ 项的第一次平均都是整数。
我们不把乘 $p$ 作为新增操作；归一化引理说明，对 $pX$ 找到的同一平均词也适用于 $X$。
后面的所有下降都固定在这个整数尺度内进行。

初始化中经常使用一个简单的“删一”观察：
对 $p+1$ 个数 $x_1,\ldots,x_{p+1}$，删去第 $i$ 个数后的和为 $S-x_i$。
若这些 $p+1$ 个候选和都相同，则全部 $x_i$ 相同。
因而，只要池中没有某实际值的 $p$ 份副本，就能用多出的一个位置避开一个指定均值。
''')
before('03_descent_tools',r'\begin{lemma}[素数零和选择及逆边界]',r'''
\section{模p零和选择：足够的池与唯一的边界形状}
整性要求所选 $p$ 项之和为 $0\pmod p$。
接下来的零和引理告诉我们，$2p-1$ 个候选位置一定足够；
若只能拿出 $2p-2$ 个位置，失败的余数形状也完全确定。
这两种结论将分别用于宽裕的选择和最后一个容量边界。

\begin{example}[五平均的边界池]
模 $5$ 的池 $(0^4,1^4)$ 没有五项零和。
五项中必须包含 $1,2,3$ 或 $4$ 个 $1$，和都不被 $5$ 整除。
添加任意一个第九位置以后，零和引理保证出现五项零和。
逆命题说，长度为八的失败池在仿射改名后只能有这种两类各四份的形状。
\end{example}
''')
replace('03_descent_tools',r'展开后每个单项式的总次数小于',r'''这里把 $1-F_i(z)^{p-1}$ 看成一个指示函数：$F_i(z)=0$ 时它为 $1$，否则为 $0$。
对一个变量，有 $\sum_{t\in\F_p}t^k=0$，除非 $k$ 是正的 $p-1$ 倍数；当 $k=0$ 时求和也是 $p=0$。
展开后每个单项式的总次数小于''')
replace('03_descent_tools',r'非零解的支持恰有 $p$ 项，',r'''由于 $z_i^{p-1}$ 在 $z_i\ne0$ 时为 $1$，第一个方程要求非零坐标个数被 $p$ 整除。
一共只有 $2p-1$ 个变量，所以非零解的支持恰有 $p$ 项；第二个方程要求该支持对应的 $a_i$ 之和为零。
每个合格支持允许每一非零坐标任取 $p-1$ 个值，''')

INTRO['04_descent_complete']=r'''
上一讲解决了怎样安全地选择、怎样初始化，以及怎样在一个池中寻找整数平均。
本讲把这些选择按实际数值的重数组织成完整分类。
先读每种情形的目标，再看其具体配比，可以避免把多个相近公式混在一起。

\begin{center}
\begin{tabular}{p{.38\textwidth}p{.48\textwidth}}
\toprule 当前状态 & 续步的来源\\\midrule
某重值至少有 $2p-1$ 份 & 用它作背景，跨越负系数和 $p$\\
至少三个不同重值 & 保留极端值，利用实际数值顺序\\
两个不同余重值，富余份数和至少 $p-2$ & 两个重值共同承担选取消耗\\
两个不同余重值，富余更少 & 在保护池中使用逆零和边界\\
\bottomrule
\end{tabular}
\end{center}
本讲所谓“碰撞”仅指新均值恰好等于要保留的旧重值。
一次碰撞不一定使原问题不可解；它只表示当前尝试没有维持两个不同重值。
证明的办法是写出碰撞强迫的等式，再换一个选择。

\section{背景重值与系数跨越}
'''
before('04_descent_complete',lemma('lem:background'),r'''
设背景值为 $b$，另一重值为 $a=b+\Delta$。
如果 $\Delta\not\equiv0\pmod p$，给定第三值 $x$ 后，
同余式 $i\Delta+x-b\equiv0\pmod p$ 唯一确定 $0\le i<p$。
选择 $(a^i,b^{p-1-i},x)$ 就是整数平均。
如果它总是碰撞到 $b$，每个第三值都必须在一个有限等差列中。
这把任意整数配置化成了有界整数系数的计数问题。
''')
replace('04_descent_complete',r'若有 $j\ge2$，将负系数降序排列，',r'''\par\noindent\textbf{跨越构造。}
若有 $j\ge2$，将负系数降序排列，''')
replace('04_descent_complete',r'得到均值 $b-\delta$，留下',r'''这个选择的项数为
\[
s+(T-p)+(2p-s-T)=p,
\]
而相对于 $b$ 的系数总和为 $-T+(T-p)=-p$，所以均值正好是 $b-\delta$。
所有计数都非负：$T\ge p$ 与 $T+s\le2p$ 分别保证后两项。
它留下''')
before('04_descent_complete',lemma('lem:heavy'),r'''
\section{三个或更多重值：用顺序避开碰撞}
当有四个重值时，可以把最大的一个完整留住，所有参与平均的值都小于它。
因此新均值自动不同于它，不必另列同余情形。
三个重值时，储备更紧；下面的论证将最后一个困难形状隔离出来，
并用一次单中间值选择、一次双中间值选择排除连续碰撞。
''')
replace('04_descent_complete',r'只剩 $(a^p,b^{p+r},c^p)$，$r\ge2$。',r'''\par\noindent\textbf{三个值的最后形状。}
只剩 $(a^p,b^{p+r},c^p)$，$r\ge2$。''')
replace('04_descent_complete',r'最后设仅有同余重值 $a,b$。',r'''\par\noindent\textbf{两个重值模 $p$ 相同。}
最后设仅有同余重值 $a,b$。''')
before('04_descent_complete',lemma('lem:two-heavy'),r'''
\section{两个重值可以共享富余位置}
若两个重值重数分别为 $p+\alpha,p+\beta$，并不需要其中某一个单独达到 $2p-1$。
一共只消耗至多 $p-2$ 份锚点，而 $\alpha+\beta\ge p-2$ 时，
两个锚点不可能同时被消耗到 $p$ 份以下。
这项计数是下面引理比背景值情形更精细的地方。
''')
replace('04_descent_complete',r'若 $H,L<p$，右式严格介于 $0,n$，矛盾。',r'''若 $H,L<p$，则
\[
f(a)+C+H-L\ge f(a)-(p-1)>0,
\]
另一方面，$f(a)+C\le n-f(b)$ 给出
\[
f(a)+C+H-L\le n-f(b)+p-1<n.
\]
这个严格介于 $0,n$ 的整数不可能被 $n$ 整除，矛盾。''')
before('04_descent_complete',lemma('lem:integer-range'),r'''
\section{最后的双重值分支与有限终止}
最后假设两个锚点的富余总数至多为 $p-3$。
冻结各 $p$ 份锚点，再给每个危险素数至多留出一个见证，
条件 $n\ge4p-2+d_p(n)$ 仍让我们拿出 $2p-2$ 个候选位置。
这个数恰好对应上一讲的逆零和引理。

如果池中找不到整数平均，它只能有两个余数类。
接着借一份锚点进入池中；如果仍碰撞，就把这份锚点的贡献加倍。
这就是以下证明后半段“借一份、再借两份”的由来。
''')
replace('04_descent_complete',r'预留 $p$ 份 $a,b$ 及至多 $d$ 个危险见证，',r'''\par\noindent\textbf{建立边界池。}
预留 $p$ 份 $a,b$ 及至多 $d$ 个危险见证，''')
replace('04_descent_complete',r'取一份 $a$，由两池余类补足为整数平均；',r'''\par\noindent\textbf{借用锚点并排除碰撞。}
取一份 $a$，由两池余类补足为整数平均；''')
replace('04_descent_complete',r'每次非终端操作都是非恒等整数平均，',r'''\par\noindent\textbf{终止。}
以上情况已经穷尽当前状态。只要还没到相反值终端，总有下一次安全操作。
每次非终端操作都是非恒等整数平均，''')

INTRO['05_zero_tail']=r'''
后面的矩阵构造只负责造出一个零和 $p$ 元组。
本讲先证明，一旦做到这件事，确实能够完成整个配置。
为此需要独立解决 $3p$ 个位置。这个维数适合分成三个等大块，
分组矩阵的行列和都等于 $p$，于是能用非常具体的剪切处理。

\section{三个等大块上的剪切}
'''
before('05_zero_tail',prop('prop:threep'),r'''
若三个块的值为 $a,b,c$，一个 $3\times3$ 非负整数矩阵 $K$，
其每行每列的和都为 $p$，就描述一个真实分组：
第 $i$ 个新组从第 $j$ 个旧块取 $K_{ij}$ 个位置。
行和保证每组恰有 $p$ 项，列和保证每个旧位置恰好用一次。
对三个新组分别平均，新块值就是 $K(a,b,c)^T/p$。

下面的 $mJ$ 项在 $a+b+c=0$ 的平面上消失。
留下来的 $I\pm D$ 才是我们想要的剪切；添加 $mJ$ 是为了让计数全部非负。
''')
replace('05_zero_tail',r'由于 $D^2=0$，两作用互为射影逆。',r'''由于 $D^2=0$，有
\[
(I+D)(I-D)=I-D^2=I.
\]
实际三步平均仍会带上 $1/p$ 的共同尺度，但两作用在共同尺度意义下互为逆。
因此两个方向的整数次剪切都有正向平均序列。''')
replace('05_zero_tail',r'这些矩阵射影生成 $\Gamma_0(3,\Z)$。',r'''
这里 $\Gamma_0(3,\Z)$ 表示行列式为 $1$、左下项被 $3$ 整除的整数矩阵群。
为什么恰好出现 $3$？因为我们正在控制三个等大块，
其模 $3$ 的差分就是剩余的共同余数障碍。
这些矩阵射影生成 $\Gamma_0(3,\Z)$。''')
replace('05_zero_tail',r'取 $h=(p-1)/2$，连续两次平均',r'''
到了相反值配置，令 $h=(p-1)/2$。第一次选 $h$ 份 $s$、$h$ 份 $-s$ 和一个零，
得到 $p$ 个新零；第二次作同样的选择以后，每个符号只剩一份。
最后一组用这两份相反值和 $p-2$ 个零即可。
具体地，连续两次平均''')
before('05_zero_tail',lemma('lem:zero-base'),r'''
\section{一个零为什么已经有用}
在 $2p+1$ 个位置中保留一个零，其他位置正好分成两个 $p$ 组。
零和要求两个组的均值互为相反数。因此，上一个证明末尾的三步操作可以直接接上。
''')
before('05_zero_tail',lemma('lem:zero-tail'),r'''
\section{按非零支持数选择已经解决的子系统}
一个零和 $p$ 元组平均以后，至少产生 $p$ 个零，所以非零位置最多还有 $n-p$ 个。
我们只在一个包含\emph{全部}非零位置的子系统上工作；外部留下的全是零，
故子系统仍然零和，也不会有缩放尺度不同步的问题。

若一个整数配置含零，坐标差的最大公因子就等于坐标本身的最大公因子。
本原化以后它的 $G$ 必为 $1$。因此这个子系统可以直接调用已证维数的充分性。
选择子系统时只需让位置数严格大于非零支持数，确保其中也有一个零。
''')

INTRO['06_compression']=r'''
\section{压缩的目标与困难}
本讲始终保留原来的 $n$ 个位置，但逐渐减少不同数值的数目。
目标形状是
\[
(A^p,B^p,C^r),\qquad n=2p+r,
\]
并保留全部必要的同余见证。随意分组平均虽然能制造等值块，
却可能把原来可解的输入送入共同非零余数类，因此需要先安排见证的位置。

这里允许分母为 $p$ 的幂。对每个 $\ell\mid n$，因为 $p\nmid n$，
模 $\ell$ 的分母仍可逆。压缩阶段关注的是见证是否消失，不要求整数能量下降。
“块”指同值位置的集合；“单点”指暂未归入块的位置角色，其实际值允许相同。
'''
before('06_compression',lemma('lem:short-choice'),r'''
\section{同时避开若干坏配比}
将两个 $p$ 块作互补混合时，第一个新值随整数配比 $k$ 作一次变化。
在某个素数处，一个非恒定的一次式至多有一个零点。
所以问题变成：在短区间 $1,\ldots,p-1$ 中，同时避开若干素数各禁止的一个余数类。
以下引理用 $n<4p$ 对危险素因子的总数量作限制。
''')
before('06_compression',lemma('lem:concentrate'),r'''
\section{把分散的见证合并到一个差分}
说“$a-w$ 有完整支持”，是指对每个危险素数 $\ell$ 都有 $a\not\equiv w\pmod\ell$。
假设某个素数的差异还在另一个块或单点里，我们可以先把它移入当前两个块，
再用互补混合使同一个差分同时在所有已处理素数处非零。
已获得的支持不会丢掉，而每轮至少增加一个新的素数；因而这里只需有限轮。
''')
before('06_compression',lemma('lem:two-block-entry'),r'''
\section{只在有限余数上反向，仍然只做正向平均}
一次块--单点交换，把旧块中的一份位置留给新的单点角色：
\[
(a^p,c_i)\longmapsto
\left(\left(\frac{(p-1)a+c_i}{p}\right)^p,a\right).
\]
这已经说明角色为什么会移动：新的单点是某个旧块位置，
而原来的单点已经加入新块。操作不需要真正移动一个数值。

模 $\ell\mid n$，这个交换是有限集合上的可逆变换。
如果它的阶整除 $L$，重复 $L-1$ 次便具有逆的\emph{模作用}。
这不意味着有理数上的逆也能这样实现。
例如 $p=3$ 时，交换两次把 $(a,c)=(0,1)$ 送到 $(2/9,1/3)$；
形式逆送到 $(1,-2)$。模 $7$ 两者相同，实际有理数却不同。
入口只需要模见证正确，这种有限逆已经够用。
''')
replace('06_compression',r'对互异 $i,j,k$，直接相乘得到',r'''
为了说明交换子的由来，取互异 $i,j,k$，置
\[
w=e_k-e_j,\qquad h=e_j^T+\lambda e_k^T,
\qquad T=A_k^{-1}A_jA_k.
\]
秩一矩阵公式给出 $A_k^{-1}v_j=w$、$e_j^TA_k=h$，故 $T=I+wh$。
另外 $e_i^Tw=0$、$hv_i=\lambda(1+\lambda)$。
将这两个等式用于共轭，再乘 $A_i^{-1}$，得到''')
replace('06_compression',r'交换矩阵模 $\rad(n)$ 的逆可由 $L-1$ 次正向交换实现，',r'''
这里 $\rad(n)$ 是 $n$ 的全部不同素因子的乘积。
按实际时间顺序，用下面八段正向操作实现交换子的模作用：
\[
 A_i^{L-1},\ A_k,\ A_j^{L-1},\ A_k^{L-1},\
 A_i,\ A_k,\ A_j,\ A_k^{L-1}.
\]
这些段一共含 $4L$ 次块--单点交换。
交換矩阵模 $\rad(n)$ 的逆可由 $L-1$ 次正向交换实现，''')
replace('06_compression',r'其数量至多 $r$。',r'''其数量至多 $r$。
确实，若有 $r+1$ 个这样的素数，则其乘积至少为 $2^{r+1}$，又整除 $r+2$，
与 $2^{r+1}>r+2$ 矛盾。这个小计数解释了保留 $r$ 个单点为什么足够：
不能用交换子移动的素数，恰好可以逐个留一个原有见证。''')
before('06_compression',prop('prop:entry'),r'''
\section{下半带、上半带及核心参数}
下半带先制造两个 $p$ 块，再让两个块之间的差分具有全部见证。
上半带多一整块，先压成 $(2p,p,s)$ 的加权形状，再用本讲末尾的两次平均改为 $(p,p,p+s)$。
这样，后面的所有临界带都可以使用同一个核心记号。
''')
replace('06_compression',r'先设 $r<p$。',r'''\par\noindent\textbf{第一步：下半带两轮修复。} 先设 $r<p$。''')
replace('06_compression',r'若 $n=3p+s$、$1\le s<p$，',r'''\par\noindent\textbf{第二步：上半带的三块折叠。}
若 $n=3p+s$、$1\le s<p$，''')
replace('06_compression',r'对整数本原核心，由',r'''\par\noindent\textbf{第三步：把块值写成两个整数参数。}
对整数本原核心，由''')
before('06_compression',lemma('lem:shape-change'),r'''
\section{补足上半带的两次换形}
前一个证明得到 $2p$ 份 $A$、$p$ 份 $B$、$s$ 份 $C$。
这里先从三种值中取出一个 $p$ 元组，随后保留 $p+s$ 份旧 $A$，
把其余位置平均为另一个 $p$ 块。于是总重数正好成为 $p,p,p+s$。
唯一需要安排的是第一个组的计数，使所得见证仍然是模 $n$ 的单位。
''')

INTRO['07_returns']=r'''
\section{为什么只剩两个参数}
三块核心为
\[
K_{p,r}(a,z)=\bigl(a^p,(rz-a)^p,(-pz)^r\bigr).
\]
总和自动为零。若按照固定计数选择位置，每个新的块值都是 $a,z$ 的有理线性组合。
当若干次平均后重新得到相同的块重数，我们便可以用一个二阶矩阵记录新参数。
这就是返回矩阵的来源。

例如，固定第三块，将前两个 $p$ 块分别按 $p-k,k$ 的互补比例平均，
新第一块值是
\[
a'=\frac{(p-k)a+k(rz-a)}p
   =\frac{p-2k}{p}a+\frac{kr}{p}z,
\qquad z'=z.
\]
它在 $(a,z)$ 坐标中的真实矩阵为
\[
\begin{pmatrix}(p-2k)/p&kr/p\\0&1\end{pmatrix}.
\]
每组取多少份值、是否超出原块的数量，都必须在列出矩阵之前确定。
这种具体选择称为一个平均词：它只是有限多个平均操作按顺序组成的词。

\section{标签、共同尺度与射影返回}
'''
before('07_returns',r'各返回的分组将由',r'''
定义中的 $E_\pi$ 是一个展开映射：例如在某一组标记下，它把 $(a,z)^T$
展开为上式的 $n$ 个数。下标 $\pi$ 记录哪几个原位置属于哪个块。
平均结束后角色可能改变，故输出写成 $E_{\pi'}$。
只要新的块重数相同，就能把下一条构造按新的角色重放。

等式中的共同标量 $\lambda$ 作用于\emph{全部}位置。
由于任意平均词与共同缩放交换，归零问题只依赖参数列的直线方向。
这就是这里“射影”的含义。我们不把乘 $\lambda^{-1}$ 加入允许操作；
实际输出保留这个尺度，后面的归零词在任意非零共同尺度上都同样有效。

\begin{example}[两次正向返回提供逆]
若 $J=\left(\begin{smallmatrix}0&d\\-1&0\end{smallmatrix}\right)$，$d\ne0$，则 $J^2=-dI$。
假如 $J$ 有真实平均词，重复这个词就使全部参数共同乘 $-d$（另计实际词自身的共同尺度）。
所以 $J^{-1}=(-d)^{-1}J$ 在射影意义上由同一条正向词实现。
这不表示一次平均在整个 $\Q^n$ 上可逆；可逆性只发生在带相同块形状的参数空间上。
\end{example}
''')
before('07_returns',r'记 $U(t)',r'''
\section{剪切矩阵与可用分母}
上剪切把 $(x,y)$ 送到 $(x+ty,y)$；下剪切把它送到 $(x,y+tx)$。
它们的优点是参数可直接相加：
\[
U(s)U(t)=U(s+t),\qquad U(t)^{-1}=U(-t),
\]
下剪切同理。这里的“根子群”就是固定一种方向、让剪切参数遍历某个加法群所得的矩阵群。

构造中常能先实现一个整数剪切，然后用一个可逆倍率把参数不断除以某些整数。
将这些参数写成一个环比逐个列分母更方便。
\begin{definition}[整数的有限局部化]
对整数 $D>1$，
\[
\Z[1/D]=\{a/D^k:a\in\Z,\ k\ge0\}.
\]
等价地，约分后的分母只含 $D$ 的素因子。
其单位是 $\pm\prod_{\ell\mid D}\ell^{e_\ell}$，其中指数 $e_\ell$ 可正可负。
\end{definition}
例如 $\Z[1/6]$ 包含 $1/2,1/3,1/12$，不包含 $1/5$。
数 $5$ 属于这个环，但不是单位。这个区别会影响能否把某个剩余尺度提升成真实可用的共同单位。

若 $\gcd(q,D)=1$，约化映射把 $a/D^k$ 送到 $a(D^k)^{-1}\pmod q$，
从而 $R/qR$ 与 $\Z/q\Z$ 同构。
若 $q$ 含 $D$ 的素因子，先把这些单位因子删除即可。
''')
before('07_returns',lemma('lem:localize'),r'''
\section{一个倍率怎样产生完整的参数环}
声称“有 $U(hR)$”意味着对\emph{每个} $t\in hR$ 都有有限的真实平均词，
并不只是在有限模数上看到了这些矩阵。
下一个引理从已经可逆的三角返回出发，给出扩大参数环的具体办法。
''')
replace('07_returns',r'新环中每个元素是有限个 $r_i\kappa^i$ 的和。',r'''
新环中每个元素是有限个 $r_i\kappa^i$ 的和，其中 $i$ 允许为负数。
先用共轭实现每一项的剪切，再相乘把参数相加，得到所需返回。
全部求和都是有限的，因此最终仍是一条有限平均词。''')
replace('07_returns',r'裴蜀等式 $uA+vB=1$ 给出',r'''
至于新环中的分母为什么正好来自 $AB$，一方面 $A/B$、$B/A$ 显然都属于 $R[1/(AB)]$；
另一方面，裴蜀等式 $uA+vB=1$ 给出''')

INTRO['08_congruence']=r'''
\section{把无限问题集中到一个同余类内}
本讲的目标不是列出所有可实现矩阵，而是得到一个足够大的、结构明确的子群：
\[
\Gamma(q,R)=\{g\in\SL_2(R):g\equiv I\pmod{qR}\}.
\]
它称为层 $q$ 的主同余子群。层越深，要求越强；例如当 $q\mid q'$ 时，
$\Gamma(q',R)\subseteq\Gamma(q,R)$。
一个矩阵属于这个群，意味着它在模 $q$ 的有限数据上没有变化，却仍可能大幅改变实际有理参数。

为什么这恰好有用？本讲将证明：两个本原参数列只要模 $q$ 相同，
就能由这个群中的一个矩阵\emph{精确}连接。
于是，找到一个真实可实现的主同余子群以后，无穷多有理数值只留下有限的剩余类问题。

\section{本讲引用的两个算术群定理}
有限指数是指一个子群只有有限多个陪集。
这与“模某个数的像很大”是两个不同层次的陈述。
以下第一个外部定理保证完整剪切群足够大，第二个保证有限指数群包含主同余子群。
这里 $D>1$ 非常关键：它使 $\Z[1/D]$ 有无限多个单位。
'''
before('08_congruence',lemma('lem:deep'),r'''
\section{为什么可以指定层为平方}
两个外部定理起初只给出“存在某个层”。后面的构造需要知道控制模数的素因子，
所以还要做一次有限环消元，把未知层换成由根参数决定的 $h^2$。
以下证明中的模 $q$ 逆元只用来选择剪切参数的剩余类；最后会把参数提升回 $R$。
因此不会把有限环中的单位误当成 $R$ 中的单位。
''')
replace('08_congruence',r'记右侧为 $H$。定理',r'''
\par\noindent\textbf{先得到一个未知深层。}
记右侧为 $H$。将第一个外部定理用于有限指数子群 $\Gamma(h,R)$：
它包含的上下初等矩阵恰是参数在 $hR$ 中的剪切，故 $H$ 有限指数。
定理''')
replace('08_congruence',r'对 $g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma(h^2,R_D)$',r'''
\par\noindent\textbf{在有限环中找单位主元。}
对 $g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma(h^2,R_D)$''')
replace('08_congruence',r'取 $t\in hB$ 使 $ht=u-1$。',r'''
从 $g\equiv I\pmod{h^2}$ 可知 $c\in h^2B$、$b\in h^2B$，
而 $v=b+hkd\in hB$。于是上式两侧的非对角消元都已经使用 $hB$ 中的参数。
还需拆开对角矩阵。由于 $u-1\in h^2B$，取 $t\in hB$ 使 $ht=u-1$。''')
replace('08_congruence',r'提升各参数至 $hR_D$，',r'''
\par\noindent\textbf{回到真实参数。}
约化 $hR_D\to hB$ 满射，因而可把有限个剪切参数逐个提升。
提升各参数至 $hR_D$，''')
before('08_congruence',lemma('lem:transverse'),r'''
\section{只有一条根时，如何制造另一条}
若 $J$ 把第一坐标轴送到另一条直线，则共轭 $JU(t)J^{-1}$ 的固定方向也随之改变。
这叫作横向返回。把两条不同直线选作新基，两个剪切就成为标准上、下剪切。
但新基未必是 $R$ 上的幺模基；其逆矩阵可能增加分母。
因此下面的层不是直接写成 $h^2$，而要乘一个明确的 $g^3$。
''')
replace('08_congruence',r'因 $P,gP^{-1}$ 整于 $R$，该群包含 $\Gamma(g^3h^2,R)$。',r'''
因 $P,gP^{-1}$ 整于 $R$，若 $\gamma=I+g^3h^2X$，$X\in M_2(R)$，则
\[
P^{-1}\gamma P-I
=g^2h^2\,(gP^{-1})XP
\]
各项都属于 $g^2h^2R$，并且行列式仍为 $1$。
故 $P^{-1}\gamma P\in\Gamma(g^2h^2,R)$，证明该共轭群包含 $\Gamma(g^3h^2,R)$。
这个换基只用于论证群的包含关系，不需要把 $P$ 本身实现为平均词。''')
before('08_congruence',lemma('lem:fiber'),r'''
\section{本原列的精确纤维}
列 $v=(v_1,v_2)^T\in R^2$ 称为本原的，是指存在 $a,b\in R$ 使 $av_1+bv_2=1$。
在整数环上，这就是两坐标最大公因子为 $1$。
本原列可以补成行列式为 $1$ 的二阶矩阵，例如用裴蜀系数构造第二列。
下面的证明对两列采用相容的补法，因此所得运输矩阵还模 $q$ 为单位矩阵。

\begin{example}[同余相同，实际数值可以相差很大]
取 $v=(1,0)^T$、$w=(1,q)^T$，两者模 $q$ 相同。
下剪切 $L(q)$ 已经把 $v$ 精确送到 $w$。
一般本原列可能没有这么直接的一个剪切，但下一个引理保证某个 $\Gamma(q,R)$ 元素总能完成。
\end{example}
''')
replace('08_congruence',r'本原性使 $z\mapsto\det(w,z)$ 满射，',r'''
写 $w=(w_1,w_2)^T$，则 $\det(w,z)=w_1z_2-w_2z_1$。
因为 $w_1,w_2$ 生成整个 $R$，这个线性式能够取到任意环元素。
也就是说，本原性使 $z\mapsto\det(w,z)$ 满射，''')
before('08_congruence',lemma('lem:inverse'),r'''
\section{深同余群建立以后，更多逆会自动出现}
此前每个可逆返回都要专门寻找标量周期。
现在如果某个行列式一返回在有限商中的阶为 $m$，那么它的 $m$ 次幂已落入可实现的主同余群，
可以用该群中的逆来补偿。这就给出原返回的逆。
整数行列式不为 $1$ 时，下面用 Smith 标准形和中国剩余定理作同样的补偿。

Smith 标准形说：通过整数可逆的行、列变换，满秩二阶整数矩阵可以对角化。
本证明只借它找到一个乘积被行列式整除的矩阵；
这些行列变换本身无须成为平均操作。
''')

INTRO['09_terminal']=r'''
\section{方向之外，还要记住尺度}
即使已把一个参数比值送到终端比值，也未必已把本原列送进同一个同余类。
例如模 $5$ 的 $(1,1)^T$ 与 $(2,2)^T$ 方向相同，却是不同的列。
上一讲的精确纤维引理要求两个列模控制层完全相同。
本讲解释如何把必要的尺度作为有限数据一起处理。

对整数非零列 $v$，记 $\cont(v)=\gcd(|v_1|,|v_2|)$。
施加一个整数矩阵后，$Av$ 可能有新的公因子；
将它除去是选择本原分析代表，实际配置仍保留共同尺度。
不同公因子会让同一个矩阵在有限本原列集合上产生不同分支。
'''
before('09_terminal',lemma('lem:content'),r'''
\section{本原化为什么只有有限种分支}
伴随恒等式 $\operatorname{adj}(A)Av=(\det A)v$ 说明：
当 $v$ 本原时，$Av$ 的公因子一定整除 $\det A$。
所以可能的内容只来自一个固定整数的约数，与输入数值有多大无关。
更强的是：在固定的模 $q$ 输入类中，只要 $\det A$ 与 $q$ 互素，
每个约数都能通过某个本原提升实现。这正好允许我们选择输出尺度。
''')
before('09_terminal',r'\begin{corollary}\label{cor:finite-group}',r'''
\begin{example}[一个内容分支的具体样子]
令 $A=\diag(1,6)$，控制模数取 $q=5$。
对本原列 $(s,t)^T$，内容为 $\gcd(s,6)$，可能取 $1,2,3,6$。
固定任意本原模 $5$ 类，在模 $2,3$ 处分别选择 $s$ 是否为零，并取 $t$ 为单位，
就能安排这四种内容；与模 $5$ 的条件由中国剩余定理合并。
本原输出模 $5$ 因而分别是 $Ax,2^{-1}Ax,3^{-1}Ax,6^{-1}Ax$。
一般矩阵先经 Smith 标准形化为这个例子的形式。
\end{example}

\section{为什么可以在有限层面使用一个群}
我们实际可执行的是正向对应，每一次还可选择内容分支。
但一个有限集合上的置换，其逆就是某个非负次幂。
因此有限轨道可以用群来描述。这个结论发生在深同余群已经建立之后：
每次选择某个内容分支，都先在同余纤维中作真实准备，再执行该返回。
''')
before('09_terminal',lemma('lem:local-cycle'),r'''
\section{局部方向的逐层提升}
后面少数构造要在模 $\ell^b$ 的所有方向中移动。
若一个矩阵模 $\ell$ 的作用为非零平移，就已经遍历第一层 $\ell$ 个方向。
要遍历更高层，需知道取 $\ell$ 次幂恰好把步长增加一个 $\ell$ 因子，
不能增加得过多。下面把这个检查压缩为矩阵的一个平方参数 $c$。

\begin{definition}[局部整数]
$\Z_{(\ell)}$ 是分母不被 $\ell$ 整除的有理数环。
它的单位是赋值为零的元素，可同时约化到所有 $\Z/\ell^b\Z$。
当列的第二坐标是单位时，用其比值 $x=z/y$ 表示仿射方向。
矩阵 $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$ 对方向的作用为
$x\mapsto(ax+b)/(cx+d)$，只要分母为单位。
\end{definition}
''')
before('09_terminal',r'对核心\eqref{eq:core}',r'''
\section{把终点写成一族容易选择的列}
回到三块核心，改用 $(z,y)$ 坐标，其中 $y=a+pz$。
合法性就是 $y$ 模 $n$ 可逆。
选择 $j+1$ 份 $A=a$、$j$ 份 $B=rz-a$、$p-1-2j$ 份 $C=-pz$，
它们的和为
\[
(j+1)a+j(rz-a)-(p-1-2j)pz
=y-(p^2-nj)z.
\]
故只要达到 $z=1,\ y=p^2-nj$，便产生一个零和 $p$ 元组。
计数限制 $0\le p-1-2j\le r$ 正好给出下式的 $j$ 区间。
''')
before('09_terminal',lemma('lem:small-units'),r'''
\section{小数字为何足够控制单位}
两个 $p$ 块互补混合能提供一些行列式因子不超过 $p$ 的返回。
本原化的内容分支把这些因子变成有限标量。
我们因而需要一个初等数论事实：在 $2p<n<4p$ 时，
小于等于 $p$ 的安全数字已经能生成模 $n$ 的全部单位。
''')
before('09_terminal',r'\begin{theorem}\label{thm:terminal}',r'''
\section{共同终端定理}
这个定理是后面各参数构造的共同目标。它的三个输入分别是：
一条真实的整剪切和一个深同余群；模 $n$ 的一次方向平移；
足够的有限尺度或偶数处足够多的终端选择。
前两个输入处理“能去哪里”，最后一个处理“以哪个本原尺度到达”。
''')
replace('09_terminal',r'保留载体，两个 $p$ 块互补混合给',r'''
\par\noindent\textbf{第一步：获得模 $n$ 的全部有限标量。}
保留载体，两个 $p$ 块互补混合给''')
replace('09_terminal',r'对当前列，取 $k\equiv p^2zy^{-1}-1\pmod n$，',r'''
\par\noindent\textbf{第二步：先把列送对模 $n$。}
因为 $y$ 为单位，$z/y$ 有定义。
矩阵 $V\equiv U(-p^{-2})$ 把比值减去 $p^{-2}$，故可以一次指定所需平移次数。
对当前列，取 $k\equiv p^2zy^{-1}-1\pmod n$，''')
replace('09_terminal',r'$n$ 偶时写 $n=2^a m$',r'''
\par\noindent\textbf{第三步：处理额外的二进信息。}
$n$ 奇时，$h=n$，本步骤无需操作，直接进入下一步。
$n$ 偶时写 $n=2^a m$''')
replace('09_terminal',r'按 $y$ 选 $j\bmod\delta$，',r'''
\par\noindent\textbf{第四步：从浅层修正到平方层。}
按 $y$ 选 $j\bmod\delta$，''')
replace('09_terminal',r'两列的行列式 $2/p^2$ 是模 $m$ 单位。',r'''
两列的行列式 $2/p^2$ 是模 $m$ 单位。
为什么这里仅需求解\emph{线性}同余？因为 $q=h^2$，对于任意矩阵 $A,B$，
\[
(I+hA)(I+hB)\equiv I+h(A+B)\pmod{h^2}.
\]
二次交叉项消失。两个独立切向列于是能修正任意两坐标的一阶误差。
在奇数部分，$2$ 可逆，所以这两个修正方向足够。''')
replace('09_terminal',r'每条有限内容分支由引理',r'''
\par\noindent\textbf{第五步：由同余相同到实际相同。}
每条有限内容分支由引理''')

INTRO['10_odd']=r'''
\section{本讲的构造任务}
现在进入临界带，设 $n=2p+r$、$1\le r<p$ 且 $r$ 为奇数。
入口已由第\ref{sec:compression}讲解决，收尾已由第\ref{sec:blocks}讲解决。
因此只需在核心中取得第\ref{sec:controllers}讲的共同终端条件。

本讲完整展示一次典型的构造过程：先设计两组三步反射，
令它们的商成为三角矩阵，再同换块作用作交换子，产生一条完整剪切。
另一个两步反射提供横向方向。整个构造覆盖所有奇数余量，包括最紧的 $r=1$。

为了使交换两个等大块变得简单，取对称坐标
\[
u=z,\qquad v=a-\frac r2z,
\qquad A=\frac r2u+v,\quad B=\frac r2u-v,\quad C=-pu.
\]
交换 $A,B$ 的名称就是 $S=\diag(1,-1)$。
分母 $2$ 目前只是分析坐标的选择；构造本身仍由整数个位置组成。
'''
replace('10_odd',r'采用 $u=z,v=a-rz/2$。',r'''
\par\noindent\textbf{第一步：选择两组库存内的反射。}
采用 $u=z,v=a-rz/2$。''')
replace('10_odd',r'返回的实际尺度为 $p^{-2}$，',r'''
这三次操作的顺序是：先产生一个新 $p$ 块，留出其中的 $r$ 份作载体，
再平均一个输出组，最后平均其补组。补组自动有 $p$ 个位置，
因此只需逐项检查所列输出组不超过剩余库存。
返回的实际尺度为 $p^{-2}$，''')
replace('10_odd',r'平方标量模 $n$ 为 $p^4$，',r'''
\par\noindent\textbf{第二步：标量周期与参数环。}
平方标量模 $n$ 为 $p^4$，''')
replace('10_odd',r'在 $R=\Z[1/|f_0f_1|]$ 中，',r'''
相邻标量互素，故三角商的倍率 $f_1/f_0$ 约分后仍保留两者的全部素因子。
而 $f_0,f_1$ 奇偶相反、$r\mid f_0$，所以 $2$ 与 $r$ 都会成为参数环的单位。
在 $R=\Z[1/|f_0f_1|]$ 中，''')
replace('10_odd',r'保留 $r$ 份旧 $B$，',r'''
\par\noindent\textbf{第三步：取得横向剪切。}
保留 $r$ 份旧 $B$，''')
replace('10_odd',r'引理\ref{lem:deep}先给 $\Gamma(n^3,R)$。',r'''
这里换基矩阵的行列式为 $n$，必须计入一层分母损失。
引理\ref{lem:deep}先给 $\Gamma(n^3,R)$。''')
replace('10_odd',r'换到 $(z,y)$ 的矩阵',r'''
\par\noindent\textbf{第四步：接入共同终端。}
换到 $(z,y)$ 的矩阵''')
after('10_odd',r'\end{proof}',r'''
\section{一个可以手算的实例：五平均的十一位置}
取 $p=5,r=1$，则 $n=11$、$k=1,\epsilon=0$。
两组来源的 $\alpha$ 为 $-1,3$，对应
\[
J_{-1}=\begin{pmatrix}-5/2&1\\55/4&5/2\end{pmatrix},
\qquad
J_3=\begin{pmatrix}-5/2&-3\\55/4&5/2\end{pmatrix}.
\]
两者的平方分别是 $20I,-35I$，即 $f_0=4,f_1=-7$。
对第一组，先从两个五块各取 $2,3$ 份；留出一份新值后，
剩余四类库存为 $(3,2,1,4)$，输出取 $(2,1,0,2)$。
对第二组，来源改取 $4,1$ 份，库存为 $(1,4,1,4)$，输出取 $(1,2,0,2)$。
两次所选输出均为五项，且逐项不超过库存。

三角商的倍率为 $-7/4$，所以参数环为 $\Z[1/14]$。
这时根参数 $4r/(c_\epsilon f_0)=1$，完整的 $U(R)$ 随即得到。
这个例子说明：大定理中的有限局部化环，是从实际分组的标量平方里读出来的。
它并不是事先任意指定的有理系数域。
''')

INTRO['11_two']=r'''
\section{为什么把两个剩余位置单列}
本讲取 $r=2$、$n=2p+2$，使用
\[
(A^p,B^p,C^2)=((u+v)^p,(u-v)^p,(-pu)^2).
\]
令 $m=p+1$，合法性化为 $v$ 与 $m$ 互素，尤其 $v$ 为奇数。
这个最紧的偶数余量不走共同终端中生成全部有限单位的路线，
而是根据当前输入选择两次数字返回，直接把第二坐标改成 $\pm1$ 模一个明确的深层。

中国剩余定理在这里的角色很具体：第一次使第二坐标在控制层处处为单位，
第二次把它的完整余数指定为 $\pm1$。两次都同时安排本原性，
避免最后约去公因子时破坏刚设好的余数。
'''
before('11_two',lemma('lem:two-carrier'),r'''
\section{完整构造}
为了方便跟踪，以下把构造分为四个阶段：
上平移与缩放的逆、横向反射与深层、第一次数字返回、第二次数字返回。
''')
replace('11_two',r'记 $m=p+1$。',r'''
\par\noindent\textbf{第一阶段：上平移与缩放的正向逆。}
记 $m=p+1$。''')
replace('11_two',r'再平均 $(A^{(p+1)/2},B^{(p-3)/2},C)$。',r'''
\par\noindent\textbf{第二阶段：三步反射与深同余群。}
再平均 $(A^{(p+1)/2},B^{(p-3)/2},C)$。''')
replace('11_two',r'对 $2\le b\le p$，',r'''
\par\noindent\textbf{第三阶段：使第二坐标在整个控制层可逆。}
对 $2\le b\le p$，''')
replace('11_two',r'由于 $v$ 奇，先用整数上平移把 $u$ 改成 $2a-v$，',r'''
这个 $M_b$ 是可用的正向返回，但不预先假定它对所有本原输入安全或可逆。
下面每次使用它，都会先安排输入，使本原输出保持合法。
由于 $v$ 奇，先用整数上平移把 $u$ 改成 $2a-v$，''')
replace('11_two',r'执行 $M_p$ 后本原分析列为 $(-a,pv-ma)$。',r'''
直接乘矩阵可见
\[
\frac1pM_p(2a-v,v)^T=\frac2p(-a,pv-ma)^T.
\]
其中 $2/p$ 是全部核心的共同尺度，所余整数列将被安排为本原。
执行 $M_p$ 后本原分析列为 $(-a,pv-ma)$。''')
replace('11_two',r'再令 $p\nmid a$。CRT 给出',r'''
这些额外同余只在不整除 $v$ 的素数处新增，所以与 $2a\equiv u\pmod v$ 相容。
再令 $p\nmid a$；若 $p\mid v$，原来的同余已经保证这一点，否则另加 $a\equiv1\pmod p$。
由于 $\gcd(a,v)=1$，有
\[
\gcd(a,pv-ma)=\gcd(a,p)=1.
\]
这给出本原性，而对所有 $\ell\mid q$ 的选择给出第二坐标的单位性。
CRT 给出''')
replace('11_two',r'取 $v_1^{-1}\pmod m$ 的代表',r'''
\par\noindent\textbf{第四阶段：直接指定第二坐标的完整余数。}
取 $v_1^{-1}\pmod m$ 的代表''')
replace('11_two',r'前两个模数互素；',r'''
除法 $(bv_1-\epsilon)/m$ 是整数除法，因为先前已选 $bv_1\equiv\epsilon\pmod m$。
此时第二个同余恰好等价于 $bv_1-ma_1\equiv\epsilon\pmod q$。
前两个模数互素；''')
replace('11_two',r'再用上平移使第一项为零模 $q$，',r'''
因为 $\gcd(a_1,v_1)=\gcd(a_1,b)=1$，有
\[
\gcd(a_1,bv_1-ma_1)=\gcd(a_1,bv_1)=1.
\]
所以这里无须再约去任何内容，已经安排好的第二坐标余数确实保留。
再用上平移使第一项为零模 $q$，''')
