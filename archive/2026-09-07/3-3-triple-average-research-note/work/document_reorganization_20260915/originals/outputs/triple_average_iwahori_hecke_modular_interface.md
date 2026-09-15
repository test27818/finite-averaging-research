# Hecke 代数恒等式与尚未建立的模形式接口

更新：2026-09-11。最新结论见[最后检验](triple_average_final_hecke_audit.md)。
当前保留的是有限Hecke代数和矩阵恒等式，**没有构造出能够调用Ihara或
自守谱理论的全局接口**。此前过强的解释已撤回，完整原稿保存在
[审计前存档](history/triple_average_hecke_interface_before_final_audit.md)。

## 1. 有效的有限代数识别

几何链相邻权重比为 $s=3^k$，真实宏的非平凡块为
\[
\sigma_i=\begin{pmatrix}(s-1)/s&1/s\\1&0\end{pmatrix}.
\]
由已有Burau关系，$T_i=s\sigma_i$满足
\[
(T_i-sI)(T_i+I)=0,\qquad
T_iT_{i+1}T_i=T_{i+1}T_iT_{i+1},
\]
以及远交换关系。这确实定义有限型Hecke代数的表示，但不自动定义仿射
Hecke代数的酉表示或经典模形式。

标准 $B_p$ 宏在 $(x,y)=(u,v-u)$ 坐标中为
\[
A=\begin{pmatrix}1&0\\-p/3&-1/3\end{pmatrix},\qquad H=3A.
\]
它也满足参数3二次关系。能量矩阵
\[
G_p=\begin{pmatrix}p(p-1)&3p\\3p&12\end{pmatrix}
\]
满足 $A^TG_p=G_pA$ 及
\[
G_p-A^TG_pA=\frac23\binom p4(p,4).
\]
这是一种有限维星结构，尚未识别为Petersson内积。

## 2. 单生成元不能解释全部 level

令 $R=\left(\begin{smallmatrix}0&3\\1&2\end{smallmatrix}\right)$。
旧换基 $P_p=\left(\begin{smallmatrix}1&3\\0&-p\end{smallmatrix}\right)$
确实满足 $HP_p=P_pR$、$|\det P_p|=p$。但对任意奇数 $p$，取
$\epsilon=\pm1\equiv p\pmod4$、$b=(\epsilon-p)/4$，则
\[
Q_p=\begin{pmatrix}1&3\\b&-p-b\end{pmatrix},\qquad
HQ_p=Q_pR,\quad\det Q_p=\pm1.
\]
因此指数 $p$ 只是旧换基的一种选择，并非单生成元的内在level。
$\Gamma_0(p)$ 的正确来源仍是独立已证的合法模 $p$ 圆盘稳定子。

另有精确矩阵分解
\[
H\operatorname{diag}(1,-1)
=\operatorname{diag}(3,1)\begin{pmatrix}1&0\\-p&1\end{pmatrix}.
\]
它给出双陪集成员关系；附加反射没有被证明正向可实现，这也没有把 $H$
识别为整个经典Hecke卷积算子。

## 3. 第二算子族与停止边界

取
\[
B_c=\begin{pmatrix}-1&0\\cp&3\end{pmatrix},\qquad
A^{H}=\begin{pmatrix}-3&0\\p&1\end{pmatrix}=-H.
\]
二者满足
\[
B_cA^H=3L(p(1-c)),\qquad A^HB_c=3L(p(c-1)/3),
\quad L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix}.
\]
$c=1$没有非平凡根。$c\ne1$给出一侧根资源；原基矩阵为
$CB_cC^{-1}=\left(\begin{smallmatrix}-1&0\\cp-4&3\end{smallmatrix}\right)$。
41元已有的额外返回对应 $c=2/3$。

对 $c\in\mathbb Z[1/3]$，取足够小的
$\delta=(p-1)/3^k$，其中 $3^k\equiv1\pmod p$，这些目标有严格正的
三进类型运输，源／目标容量为 $(p-4,3,1)$；副本实现不等于原位置实现。

本次新增两个一般障碍：

- 所有这些矩阵及其逆下三角，任意有限词都把 $u$ 变为非零倍数的 $u$，
  所以不能从 $u\ne0$ 直接进入 $u=0$ 终端。
- 若要求 $H$ 与 $B_c$ 为同一正定内积下的自伴算子，必有
  $4g_{12}=pg_{22}=cpg_{22}$。$c\ne1$时内积退化，因而不能把这对指定
  矩阵当成同一酉Hecke表示中的两个自伴简单生成元。

这排除了原定的直接酉谱接口，不排除非酉、非线性或带额外变量的其他构造。

## 4. 投影名称的修正

\[
E_+=\frac{3A+I}{4}=\begin{pmatrix}1&0\\-p/4&0\end{pmatrix},
\quad
E_-=\frac{3(I-A)}4=\begin{pmatrix}0&0\\p/4&1\end{pmatrix}
\]
是正确的代数投影，其像分别为非法方向 $(4,-p)$ 和终端方向 $(0,1)$。
它们只是有限二次代数的两个特征空间，没有被证明对应全局Eisenstein／
Steinberg自守分量。非负系数多项式 $F(A)$满足 $F(1)>0$，无法消去第一
特征线；这个正锥障碍不依赖任何模形式定理。

## 5. 数字与删点模型的真实范围

循环标签上的数字矩阵确实有 $K=P_0+P_1+P_2$，其中
$(P_df)(i)=f(3i+d)$。这是有限置换表示中的和，尚未与 $U_3$ 或 $T_3$
在模形式／模符号空间上的作用交织。不能再写“复制已经实现整个 $T_3$”。

原 $p$ 位置的punctured置换不是Möbius变换；平移与它生成的是 $A_p$，见
[交错群影子](triple_average_nonsplit_alternating_shadow.md)。相应Reynolds
角代数应在这个物理置换模型中研究。$p+1$点的非分裂环面是另一个对象，
把它降到 $p$ 个位置的接口仍未证明。

## 6. Manin 最后检验

到平凡系数普通模符号的自然线性等变映射被中心 $-I$ 排除：它在参数向量上
是负号，在有理端点上是恒等，所以等变线性映射只能为零。非线性射影映射
可以避开该障碍，但目前没有构造。

全部合法有理方向属于同一 $\Gamma_0(p)$ cusp轨道，因此只看cusp标签
不能形成严格下降高度；必须增加代表、路径或局部格信息。模符号的反向和
三角关系也没有提供保持原位置重数的正向路径。

强群包含仍是充分条件；弱的输入相关终端覆盖仍是开放目标。严格下降高度
是可能的充分证书，不应成为所有成功路线的必要要求。没有额外分支提升定理时，
把弱目标称作“Hecke覆盖”或“Ihara饱和”只是改名。

## 7. 已有计算与证据边界

| 检验 | 结果 | 效力 |
|---|---|---|
| 有限Hecke、能量和根公式 | 精确核验通过 | 恒等式，不是自守接口 |
| 旧返回库2084个矩阵 | 9个满足二次谱型；41元多一个 | 仅指定库 |
| 17个非分裂素数至149 | 一／两层chart、三层回基准均无新返回 | 仅指定平移语法 |
| 9个素数至71的原子词 | 深度5无非标准二次谱型返回 | 不排除长词或直接终端 |
| $B_{71}(1,v),\ |v|\le100$ | 198个合法整数参数在至多6步准备后有零和三元组 | 非任意有理参数定理 |
| 同一深度5的大窗口 | 1251/19720 | 不能据稀疏性推断Manin递归 |

六步准备后如要制造三个零，还需一次平均。有限词各自产生线性终端方程，
所以有限深度终端斜率稀疏本就是线性系统的一般性质。

保留核验入口 `iwahori-hecke-modular-interface` 的历史ID，其数学效力已
收窄为有限代数恒等式；新增 `final-hecke-manin-audit`核验上述一般障碍。
详细证明、条件范围和旧说法的逐项纠正见[最后检验](triple_average_final_hecke_audit.md)。
