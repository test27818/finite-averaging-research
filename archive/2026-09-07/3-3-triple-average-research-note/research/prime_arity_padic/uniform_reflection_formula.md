# 所说的“统一公式”具体是什么

2026-09-15。这里完整解释上一轮的统一公式，避免把“生成一套宏的公式”与“完整平均算法”混称。原证明文件本轮不作修改。

## 1. 精确范围和输入形状

设p≥83为素数，1≤s≤9，n=3p+s，r=p+s。公式在原n个位置上作用于核心
\[
\mathcal K(\xi,z)=\bigl(\xi^p,(rz-\xi)^p,(-pz)^r\bigr).
\]
记这三种值为A、B、C。这里的指数是位置重数；它不是幂运算。总和为0。

任意合法输入进入此核心的步骤、完整根理想和终端提升沿用既有证明；下面只给出共同的反射生成公式。

## 2. 先算三个离散参数

令
\[
a_0=\left\lfloor\frac{s}{3}\right\rfloor+1,
\qquad \alpha\in\{a_0,a_0+1\},
\]
\[
h\in\left\{
\left\lfloor\frac{p}{3\alpha}\right\rfloor-1,
\left\lfloor\frac{p}{3\alpha}\right\rfloor
\right\},\qquad \rho=p-3\alpha h.
\]
定义
\[
e_0=\max\left(
0,\ 2\alpha-\rho,
\left\lceil\frac{(s-\alpha)h-\alpha}{2}\right\rceil
\right),\qquad e=e_0,e_0+1,e_0+2.
\tag{2.1}
\]
两个α、两个h、三个e共生成12条指定返回，无需按p搜索。

## 3. 每条返回的七个位置计数

由所选α、h、e直接算
\[
\boxed{
\begin{aligned}
i&=\alpha(h+1),& j&=\alpha h,& k&=p-2\alpha h-\alpha,\\
x&=\alpha h-e,& y&=k-e,& u&=(\alpha-s)h+\alpha+2e,\\
v&=sh.
\end{aligned}}
\tag{3.1}
\]
四次实际平均如下：

1. 取i份A、j份B、k份C，平均成p份D。
2. 再取一组组成相同、位置不交的i份A、j份B、k份C，平均成另p份D。
3. 从2p份D保留r=p+s份；在剩余位置中取x份旧A、y份旧B、u份旧C、v份D，平均成第一个新p块。
4. 把其余p个位置平均成第二个新p块。

所有保留与分组均使用原n个位置。p≥83的容量证明保证七个计数非负，来源足够、输出组和补组均恰有p个位置。

## 4. 为什么这总是可逆反射

令
\[
\beta=rj-pk,\qquad Q=pry-p^2u+v\beta.
\]
在参数(ξ,z)上，四步作用的矩阵为
\[
\boxed{M_{\alpha,h,e}=\frac1{p^2}
\begin{pmatrix}\beta&Q\\-\alpha&-\beta\end{pmatrix}.}
\tag{4.1}
\]
计数公式恒等地满足
\[
p(x-y)+\alpha v=\beta,
\]
这恰使矩阵迹为0。若pf=β²−αQ，则
\[
M_{\alpha,h,e}^2=\frac f{p^3}I,\qquad pf\equiv p^4\pmod n.
\]
因此f≠0，重复同样的四步返回给真正的射影逆。无需数值试验周期。

e增加1时，(x,y,u,v)增加(−1,−1,2,0)，Q减少pn、f增加αn。连续三个e同时提供相邻倍率与隔一倍率；相邻α提供模n上的粗略平移。后续浅层提升使其无需再满足三进高阶满循环条件。

## 5. 一个具体代入

取p=83、s=1、α=1、h=26。则ρ=5、e₀=0；取e=0得到
\[
(i,j,k;x,y,u,v)=(27,26,30;26,30,1,26).
\]
前两次平均各取27份A、26份B、30份C。随后保留84份D；第三次取26份旧A、30份旧B、1份旧C、26份D；最后平均补组。

此时β=−306、Q=194315，f=−1213，故
\[
M=\frac1{83^2}\begin{pmatrix}-306&194315\\-1&306\end{pmatrix},
\qquad M^2=-\frac{1213}{83^3}I.
\]
e=1、2只需按同一整数移动修改计数，没有新增搜索。

## 6. “统一”到什么程度

这个公式覆盖的是九个偏移族n=3p+s、1≤s≤9且p≥83的反射资源；它不是全部2p到4p的单一计数式，不覆盖较小p的全部边界，也没有把任意输入的整条成功序列写成固定公式。

它的证明由可行e区间中的三个连续整数点构成。此前一般充分h下界为：α=1、2、3、4、5分别取7、12、8、4、4；p≥83时式(2.1)的两个h均满足相应下界。详见只读来源[三连参数容量证明](../../outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)第6节和[完整可行区间](../../outputs/prime_arity/structure/carrier_interval_and_unit_descent.md)第2节。

更自然的算法形式应把这段计数当作“实际可执行操作的供应器”，把局部误差修正交给同一个有限环算法；下一篇[平方零编译](square_zero_hensel_compiler.md)正是这种分离。尚未证明所有p、n都能由同一个供应器覆盖。
