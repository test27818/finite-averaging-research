

# C21.1 三条返回承担三个不同的任务

设p≥2、1≤s<p、r=p+s、n=3p+s。核心为
\[
(A^p,B^p,C^r),\qquad A=a,\ B=rz-a,\ C=-pz.
\]

对一个来源参数α，以下三条返回分别承担：

1. J：迹零，重复一次就提供真实正向射影逆；
2. G：同来源的相邻迹零输出，J⁻¹G提供可逆三角倍率；
3. M：由J的输出加守恒移动，直接满足M=U(−n)J。

因为新根U(−n)已经有准确参数，第二个横向参数只需两条相邻反射。它不必再完成一遍守恒交换。这个任务划分正是五条返回而非六条或十二条的原因。

# C21.2 固定α的显式计数

设α≥1、1≤s≤2α，写
\[
p=3\alpha d+\rho,\qquad 0\le\rho<3\alpha.
\]
来源取
\[
j=\alpha d,\qquad i=j+\alpha,\qquad
k=\alpha d+\rho-\alpha.
\tag{2.1}
\]
输出取
\[
o_e=(x,y,u,v)=
\bigl(\alpha d-e,\ k-e,\ (\alpha-s)d+\alpha+2e,\ sd\bigr).
\tag{2.2}
\]
这个参数化恒满足来源与输出总数p、迹零方程。因此每条容量合法的o_e都给一个实际迹零返回J_e。

守恒移动为
\[
\Delta_3=(3\alpha-\rho,-\rho,2\rho-3\alpha-s,s).
\]
所以改变后的输出为
\[
o_e+\Delta_3=
\bigl(\alpha d+3\alpha-\rho-e,\ \alpha d-\alpha-e,\
(\alpha-s)d-2\alpha+2\rho-s+2e,\ s(d+1)\bigr).
\tag{2.3}
\]

我们同时需要o_e、o_{e+1}及(2.3)可行。它们各自四个位置容量为
\[
p-2i,\quad p-2j,\quad r-2k,\quad p-s.
\tag{2.4}
\]

**精确区间。** 来源容量与固定v容量成立时，这三条输出的所有约束等价于整数e满足
\[
L\le e\le U,
\]
其中
\[
\boxed{
L=\max\left(
0,\ 5\alpha-2\rho,\
\left\lceil\frac{(s-\alpha)d-\alpha}{2}\right\rceil,\
\left\lceil\frac{(s-\alpha)d+2\alpha+s-2\rho}{2}\right\rceil
\right),
}
\tag{2.5}
\]
\[
\boxed{
U=\min\left(
\alpha d-\alpha-\mathbf1_{\rho=0},\
\left\lfloor\frac{sd+\alpha+s-\rho-2}{2}\right\rfloor,\
\left\lfloor\frac{sd+4\alpha+2s-3\rho}{2}\right\rfloor
\right).
}
\tag{2.6}
\]

证明是逐项把(2.2)、(2.3)及e+1的非负和库存上界移项。这里s≤2α用于删去被更强条件蕴含的界；例如输出o_e与o_{e+1}的u上界合并为式(C21.2.6)第二项。

# C21.3 不用参数扫描的一般容量充分条件

**容量定理。** 若
\[
\boxed{
d\ge7,\qquad sd\ge9\alpha+2-s,\qquad
(3\alpha-s)d\ge4\alpha+s+2,
}
\tag{3.1}
\]
则来源及全部输出容量均成立，且L≤U。故可以直接选e=L。

**证明。** 由s≤2α，
\[
p-2i=\alpha d+\rho-2\alpha\ge0,
\]
\[
r-2k=\alpha d-\rho+2\alpha+s
\ge\alpha d-\alpha+s+1>0.
\]
固定D输出的最强上界是s(d+1)≤p−s，等价于
\[
(3\alpha-s)d+\rho\ge2s,
\]
由第三条充分条件及4α+s+2≥2s得到。其余来源及固定输出容量更弱。

为证明L≤U，记
\[
A=(s-\alpha)d-\alpha,\quad
B=(s-\alpha)d+2\alpha+s-2\rho,
\]
\[
C=sd+\alpha+s-\rho-2,\quad
D=sd+4\alpha+2s-3\rho,\quad
U_1=\alpha d-\alpha-\mathbf1_{\rho=0}.
\]
比较四个下界与三个上界。对整数下界l，l≤floor(C/2)等价于2l≤C；对ceil(A/2)，与整数U₁比较只需A≤2U₁，与floor(C/2)比较用充分条件A+1≤C。

十二个比较中最紧的三个分别归结为
\[
5\alpha\le\alpha d-\alpha-1,
\]
\[
10\alpha\le sd+\alpha+s-2,
\]
\[
(s-\alpha)d+2\alpha+s\le2(\alpha d-\alpha-1).
\]
它们分别由(3.1)三条保证。其余比较的余量可以直接写出：

\[
C-2(5\alpha-2\rho)=sd-9\alpha+s+3\rho-2\ge0,
\]
\[
D-2(5\alpha-2\rho)=sd-6\alpha+2s+\rho>0,
\]
\[
2U_1-A=(3\alpha-s)d-\alpha-2\mathbf1_{\rho=0}\ge0,
\]
\[
C-A=\alpha d+2\alpha+s-\rho-2\ge1,
\]
\[
D-A=\alpha d+5\alpha+2s-3\rho\ge1,
\]
\[
2U_1-B=(3\alpha-s)d-4\alpha-s+2\rho-2\mathbf1_{\rho=0}\ge0,
\]
\[
C-B=\alpha d-\alpha+\rho-2\ge1,\qquad
D-B=\alpha d+2\alpha+s-\rho\ge1.
\]
零下界的比较由同样三条立即成立。每个使用ρ的下界只取0≤ρ≤3α−1，因此量词覆盖全部余数，不是从有限p试验外推。证毕。

定义
\[
H(s,\alpha)=\max\left(
7,\left\lceil\frac{9\alpha+2-s}{s}\right\rceil,
\left\lceil\frac{4\alpha+s+2}{3\alpha-s}\right\rceil
\right).
\tag{3.2}
\]
只要p≥3αH(s,α)，上述三个实际返回就由一个闭式规则取得。

# C21.4 第二个横向参数只需两条反射

对第二个α，同样取(2.1)—(2.2)，但只要求o_e和o_{e+1}，不要求守恒平移输出。此时可取
\[
L_{\rm pair}=\max\left(
0,2\alpha-\rho,\left\lceil\frac{(s-\alpha)d-\alpha}{2}\right\rceil
\right),
\]
\[
U_{\rm pair}=\min\left(
\alpha d-1,\ \alpha d+\rho-\alpha-1,\
\left\lfloor\frac{sd+\alpha+s-\rho}{2}\right\rfloor-1
\right).
\tag{4.1}
\]
以下两个条件足够：
\[
\boxed{d\ge4,\qquad sd\ge3\alpha+2-s.}
\tag{4.2}
\]
来源容量及v≤p−s由s≤2α、d≥4成立。对0与2α−ρ，逐项比较显然，唯一紧式是
\[
sd-3\alpha+s+\rho-2\ge0.
\]
对A=(s−α)d−α，两个整数上界比较由(3α−s)d−α−2≥0保证；半整数比较由
\[
sd+\alpha+s-\rho-2-A
=\alpha d+2\alpha+s-\rho-2\ge1
\]
保证。故L_pair≤U_pair。

令
\[
H_{\rm pair}(s,\alpha)=
\max\left(4,\left\lceil\frac{3\alpha+2-s}{s}\right\rceil\right).
\]

现在统一选
\[
\boxed{a=\lceil s/2\rceil,\qquad \alpha=a,\ a+1,}
\tag{4.3}
\]
对a使用三返回，对a+1只使用两反射。总充分界为
\[
\boxed{p\ge T_s:=
\max\bigl(3aH(s,a),\ 3(a+1)H_{\rm pair}(s,a+1)\bigr).}
\tag{4.4}
\]
这是对任意s≥1的容量公式；p的素数性只在下一节的算术资源中使用。

# C21.5 五条返回已经接出完整根与方向接口

设p为奇素数、p>s并满足(4.4)，n=3p+s。两个α均小于p，所以gcd(p,αn)=1。

对固定α，令J=J_e、G=J_{e+1}，平方系数分别为pf、pg。原恒等式给
\[
g-f=\alpha n,\quad
f\equiv p^3\pmod\alpha,\quad
pf\equiv p^4\pmod n.
\]
所以
\[
\gcd(f,g)=\gcd(f,n)=\gcd(g,n)=1.
\]
J、G均非零且由重复四步提供真逆。J⁻¹G的三角倍率g/f及其逆，将f、g全部素因子局部化。

对第一组α=a，守恒返回M满足M=U(−n)J，所以U(±n)真实可执行。用两组相邻反射的倍率共轭扩环，得到
\[
U(nR_0).
\]
注意只需第一组供应这个n根，第二组的倍率也能共轭同一根，不必再次构造守恒输出。

两组横向反射的左下系数为−a、−(a+1)。由旧横向根、Morris／Serre及换基level引理，先得
\[
\Gamma(a^3n^2,R_0),\quad
\Gamma((a+1)^3n^2,R_0),
\]
再由gcd(a,a+1)=1合并为
\[
\boxed{\Gamma(n^2,R_0).}
\tag{5.1}
\]

旧安全行列式夹乘激活p与小数字，再在扩大的R上重建同样根和深核。两个反射乘换块，由−a+(a+1)=1直接给模n单位步长V；不使用任何独立direction或迹条件。所有参与返回在最终GL₂(R)中，故接[分裂乘法和终端族](split_torus_completes_all_directions.md)即可完成核心到零和终端。

在1≤s≤9时，基础单位模n满射、全输入入口和零触发尾部均已有一般证明，因此得到旧完整定理的一条新统一构造证明。对更大的可变s，(4.4)和根供应仍成立，但全输入结论必须另核对相应入口、基础单位和尾部，不能直接宣称全部区间已被同一方法覆盖。

# C21.6 九偏移的实际替代范围

将s=1,…,9代入(4.4)：

|s|a|H(s,a)|H_pair(s,a+1)|T_s|
|---:|---:|---:|---:|---:|
|1|1|10|7|42|
|2|1|8|4|24|
|3|2|7|4|42|
|4|2|7|4|42|
|5|3|7|4|63|
|6|3|7|4|63|
|7|4|7|4|84|
|8|4|7|4|84|
|9|5|7|4|105|

- 所有p≥83继续允许使用旧已证根供应公式；
- p<83时，只要p≥T_s，直接用本构造全参数五返回公式；
- 其他小参数保留原根记录，(11,3)按上一轮守恒修补完成。

旧162组中恰有48组满足新增条件，故需保留的逐参数根记录为114组。按s计数，新增替代数为
\[
(8,12,8,8,6,6,0,0,0).
\]
48组的替代不是从它们的试验成功归纳：它们只是一般定理范围中的有限成员。完整映射和剩余根记录保存在[剩余清单](conservation_remaining_root_cases.json)。该清单不是独立的全部证明，必须连同一般公式、(11,3)修补及已证算术收尾阅读。
