# 四平均七元完整判据：\((4,2,1)\) 核与模7控制器

日期：2026-09-12。本文证明七元这一固定维数的完整判据，不证明所有 \(n\ge7\) 的判据。

## 1. 结论与量词

对七个有理数，四平均有限步可达，当且仅当中心化、清分母并本原化后的差分 gcd 满足
\[
\boxed{G=1.}
\]
全等输入单独由空词解决。七元的 \(G\mid7\)，所以这恰好是“\(G\) 只能含2因子”的候选条件。

结合六元反例，整体最终充分阈值仍只知
\[
7\le N(4)\le16.
\]
四平均11、13、15元尚待解决；不能从“六元有反例、七元全部合法输入可达”推出 \(N(4)=7\)。

## 2. 两次原子进入合法 \((4,2,1)\) 核

将输入写为本原整数零和 \(X\)。因 \(G=1\)，有两个模7不同的位置。选一个包含这两个位置的三元补集，平均其他四个位置，记新均值为 \(a\)，补集三项为 \(b,c,w\)，故
\[
4a+b+c+w=0.
\]
三个补集数模7不全相同，所以至少一个不等于 \(a\pmod7\)。将它选作 \(w\)。

再选四份 \(a\) 中的两份与 \(b,c\) 做一次四平均。新均值记为 \(u\)，留在外面的两份 \(a\) 记为 \(v\)。得到
\[
K(u,v)=(u^4,v^2,w),\qquad w=-4u-2v.
\tag{1}
\]
并且
\[
u-v=\frac{b+c-2a}{4}=\frac{-6a-w}{4}
\equiv\frac{a-w}{4}\ne0\pmod7.
\tag{2}
\]
此处的有理数分母只含2，因此模7运算合法。第一次操作的补集本身保留不同余见证；第二次由 (2) 保证合法。**不需要事后交换或再次修复。**

设差坐标为 \(z=(x,y)^T=(u,u-v)^T\)。若参数本原整数化，则
\[
G(K)=\gcd(u-v,-5u-2v)=\gcd(y,7)=
\begin{cases}1,&7\nmid y,\\7,&7\mid y.\end{cases}
\tag{3}
\]
理由是 \(\gcd(u,v)=1\)，且 \(-5u-2v=-7u+2y\)。因此合法参数域正好是 \(7\nmid y\)。

## 3. 三个真实的一步宏及实际尺度

每个宏从 (1) 出发，再根据剩余位置更新“四重块、二重块、单点”的标签：

| 宏 | 选取的四项 | 新四重值 \(u'\) | 新二重值 \(v'\) | 新单点 |
|---|---|---|---|---|
| \(A\) | \(u,u,v,v\) | \((u+v)/2\) | \(u\) | \(w\) |
| \(B\) | \(u,u,u,w\) | \((-u-2v)/4\) | \(v\) | \(u\) |
| \(C\) | \(u,u,v,w\) | \((-2u-v)/4\) | \(u\) | \(v\) |

它们在 \(z=(u,u-v)^T\) 上的**实际矩阵**是
\[
A=\frac12\begin{pmatrix}2&-1\\0&-1\end{pmatrix},\quad
B=\frac14\begin{pmatrix}-3&2\\-7&6\end{pmatrix},\quad
C=\frac14\begin{pmatrix}-3&1\\-7&1\end{pmatrix}.
\tag{4}
\]
各行列式分别为 \(-1/2,-1/4,1/4\)，模7均可逆；下行第一项模7为零、第二项为单位，故三个宏都保持合法域。

本文矩阵乘积按右侧先作用。所有“射影可执行”仅指实际词给出目标矩阵乘以某个非零共同标量；程序始终在原始数值上执行平均，绝不物理缩放或增添位置。

直接计算得到精确恒等式
\[
\boxed{
C^3=\frac18I,\qquad
(CA)^2=\frac18I,\qquad
C^2B=\frac18\Sigma,
\quad
\Sigma=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}.
}
\tag{5}
\]
所以 \(C^{-1}\) 的正向射影实现是 \(C^2\)，\(A^{-1}\) 的正向射影实现是 \(CAC\)。又因 \(\Sigma^2=I\)，三步词 \(C^2B\) 实现的 \(\Sigma\) 也正向可逆，因而 \(B\) 同样正向可逆。

**这里的 \(\Sigma\) 绝不是免费交换两个块的名称。** 两个块大小为4和2，不能免费互换角色。它由先执行 \(B\)、再执行两次 \(C\) 的三个真实四平均实现，并整体收缩到原目标的 \(1/8\)。这一点是本核与九元等块核的重要区别。

## 4. 完整二进根资源

定义 \(U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix}\)、\(L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix}\)、\(\Delta(t)=\operatorname{diag}(1,t)\)。

式 (4) 给
\[
\Sigma A=\Delta(1/2),
\]
因此 \(D=\Delta(2)\) 及 \(D^{-1}\) 都射影正向可执行。再由
\[
\boxed{\Sigma D\Sigma D^{-1}=U(1/2)}
\tag{6}
\]
得到 \(U(1)=U(1/2)^2\)，以及其逆。整数次幂与 \(D\) 共轭提供全部 \(U(\mathbb Z[1/2])\)。此外 \(\Sigma U(1)=\Delta(-1)\) 提供符号单位。

下根不是额外假设，而由
\[
\boxed{
U(-1)\,C\,D^2=L(-7/4),\qquad
D^2L(-7/4)D^{-2}=L(-7)
}
\tag{7}
\]
给出。左式是以实际矩阵 (4) 写成的精确恒等式；各因子均已正向可逆，所以 \(L(7)\) 及逆均可执行。继续共轭和取整数次幂，得到
\[
\boxed{
U(R),\quad L(7R),\quad\Delta(R^\times),
\qquad R=\mathbb Z[1/2].
}
\tag{8}
\]

## 5. 改选二进代表，使所有模7回路直接可编译

令 \(S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\)、\(T=U(1)\)。模7不采用通常的居中代表 \(0,\pm1,\pm2,\pm3\)，而采用
\[
J=\{0,\pm1,\pm2,\pm4\}.
\tag{9}
\]
这些数模7恰好互不相同。取 \(\Gamma_0(7)\backslash\mathrm{SL}_2(\mathbb Z)\) 的8个代表
\[
R_j=ST^j\quad(j\in J),\qquad R_\infty=I.
\]
底行给出 \(\mathbf P^1(\mathbb F_7)\) 的全部点。它们是证明用的整数矩阵，不假定本身能物理执行。

全部回路有明确公式：

- \(R_jT^\epsilon\)，\(\epsilon=\pm1\)：取 \(j'\in J\) 满足 \(j'\equiv j+\epsilon\pmod7\)，回路为
  \[
  L(-(j+\epsilon-j'))\in L(7\mathbb Z).
  \]
- \(R_jS\)，\(j\ne0\)：取 \(k\in J\) 满足 \(k\equiv-j^{-1}\pmod7\)，回路为
  \[
  \begin{pmatrix}-k&-1\\jk+1&j\end{pmatrix}.
  \tag{10}
  \]
  主元 \(-k\) 是 \(\pm1,\pm2,\pm4\)。
- \(R_0S\) 回到 \(R_\infty\)，回路为 \(-I\)。
- \(R_\infty S\) 到 \(R_0\)，回路为 \(I\)；\(R_\infty T^\epsilon\) 的回路就是 \(T^\epsilon\)。

因此每条回路的左下项被7整除，左上主元是 \(R\) 的单位。对行列式一的矩阵，
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=L(c/a)\operatorname{diag}(a,a^{-1})U(b/a),
\tag{11}
\]
中间项射影等于 \(\Delta(a^{-2})\)，三项均由 (8) 实现。

Schreier 生成定理于是给出
\[
\boxed{\Gamma_0(7)\text{ 的全部射影作用均可由三个真实宏生成。}}
\tag{12}
\]
这不是仅计算有限群像，也不宣称真实宏群恰好等于 \(\Gamma_0(7)\)。改选代表 (9) 消掉了不必要的主元3，所以无需另造倍率3的逆。

## 6. Bezout 输送与一步终端

给定本原合法参数 \((x,y)\)，有 \(\gcd(x,y)=1\)、\(7\nmid y\)。先取 \(\alpha x+\beta y=1\)，再将
\[
(\alpha,\beta)\mapsto(\alpha+ky,\beta-kx)
\]
使 \(7\mid\alpha\)。于是
\[
H=\begin{pmatrix}y&-x\\\alpha&\beta\end{pmatrix}\in\Gamma_0(7),
\qquad H(x,y)^T=(0,1)^T.
\tag{13}
\]
整数 Euclid 给出有限 \(S,T^{\pm1}\) 词，再由第5节逐回路编译为正向宏。最终到达
\[
K(0,v)=(0^4,v^2,-2v).
\]
取两个 \(v\)、一个 \(-2v\) 和一个零做一次四平均，即全零。入口、宏编译和终端全部在原七个位置上完成。

必要性：本原七元状态 \(G\mid7\)；若 \(G=7\)，所有数模7相同且非零，四平均保持此余类，因此不可达。

## 7. 七元与九元：端点成功不等于最终阈值完成

四平均七元使用不等权 \((4,2,1)\) 核；[四平均九元](four_average_nine_complete.md)使用 \((4,4,1)\) 核。两者都有明确的原位置接口、正向根和有限回路证明，但实际宏不同。本文没有给出全部更高维数的内插定理。

结合半块归约和大维数定理，四平均尚待证明 \(G\) 充分性的维数是11、13、15；整体阈值仍为 \(7\le N(4)\le16\)。同样，[六平均九元](six_average_nine_fixed_network.md)的固定四步网络解决九元本身，不能独自推出 \(N(6)=9\)。

本轮研究中曾把两个端点的成功误写成精确最终阈值；该推论已撤回，当前入口和清单均以这里的量词为准。

## 8. 核验与证据边界

统一入口：

~~~text
python work/run_verifications.py --id four-average-seven-complete
~~~

[核验脚本](../work/verify_four_average_seven_complete.py)核对实际尺度恒等式 (5)、三个宏的两个参数基输入、48个本原模7行和24条完整回路；表达式图只允许恒等、A/B/C与乘积，不包含任何免费块交换。

入口检查覆盖16806个去掉冗余平移后的模7零和模式及80个大整数输入。12个独立随机抽样后经 \(G\) 筛选的输入，完成全部实际操作并通过独立 Fraction 重放，最长527步。大整数入口只核对入口与 Bezout，并未展开巨大输入的全部路径。

~~~text
four-average n7 physical periods and dyadic Schreier cover: PASS 6 48 24
four-average n7 exact-entry residue and large-integer audits: PASS 16806 80
four-average n7 literal full paths: PASS 12 527
four-average seven-position complete criterion: PASS
~~~

[完整操作序列](../work/four_average_seven_witnesses.json)采用1基索引。一般可达性由以上证明承担；527步是一个样本的非最短构造，不是最短界、普遍上界或输入位长多项式保证。
