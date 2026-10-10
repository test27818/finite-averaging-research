

# C20.2 保留自由参数，容量成为一个完整整数区间

继续用原反射计数与矩阵。给定正整数 α,h，令
\[
\begin{aligned}
j&=\alpha h,& i&=\alpha(h+1),& k&=p-2\alpha h-\alpha,\\
v&=sh,&x&=\alpha h-e,&y&=k-e,\\
u&=(\alpha-s)h+\alpha+2e.
\end{aligned}
\tag{2.1}
\]
组成和为 p，迹零条件 p(x−y)+αv=β 恒成立。旧公式仅用 e=0,1,2,3；现在允许这四个连续整数从任意合法起点开始。

写 p=3αh+t。输出非负及上界精确要求
\[
L\le e\le U,
\quad
L=\max\left(0,2\alpha-t,
\left\lceil\frac{(s-\alpha)h-\alpha}{2}\right\rceil\right),
\]
\[
U=\min\left(\alpha h,\ \alpha h+t-\alpha,
\left\lfloor\frac{sh+\alpha+s-t}{2}\right\rfloor\right).
\tag{2.2}
\]
另须满足来源容量 2i≤p、2k≤p+s 和 v≤p−s；2j≤p 由2i≤p得到。

因此“连续四个反射”恰可取 e=L,L+1,L+2,L+3，只须证明 L≤U−3。取整没有额外格空洞：e 的可行集合就是闭区间内的全部整数。
