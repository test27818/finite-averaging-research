# 从二平均到任意平均元数：当前全貌与临界猜想

**最新合数主线：** [四项新结果](general_k_three_tasks_progress_20260915.md)包含GRH下全部2、3幂的最早临界点、任意元数2k+1端点、奇素数幂的全部奇数中间维数，以及M(10)=16的固定六步网络。下文相应旧“未证”状态保留为历史；一般合数最终阈值仍未解决。

**2026-09-15最新总结果：** [九偏移共同完成](../prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)接此前下半带及3p+10以上的证明，给出全部奇素数p的N(p)=2p+1；N(2)=4。判据始终为rad(G)|p，不能在p|n时一律写G=1。素数部分已无未覆盖维数；一般合数元数的最优阈值仍开放。下文是2026-09-12及早期追加的历史快照，其中五平均14元、素数元平均一般阈值“未解”等表述均已过期，最新状态以[当前索引](../README.md)为准。

2026-09-15完整更新：[三单点交换子与无条件入口](../prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)删除下半带全部素因子数和密度入口条件。任意奇p>=3的2p+1端点、任意素数p>=5的全部奇数2p<n<3p均已全输入完成；全部偶余量也已进入合法核心，但一般核内终止和最终阈值仍未解决。统一坐标及后续两轮修复见[统一文稿](../prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)。

2026-09-15偶数后续：[内部偶余量完整证明](../prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md)已完成所有4<=r<=p-3的偶数核心方向、尺度和终端输送。偶数下半带剩余一般边界为r=2和r=p-1；最终阈值仍未降低。

2026-09-14的[合数端点同余闭合](../prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md)先完成任意合法核心；2026-09-15新入口使原六素因子或Theta限制全部删除。一般后续偶数维数仍须处理；本页各小元数最终阈值并未因此降低。

2026-09-14上半带完整族：[与6互素的上半带定理](../prime_arity/proofs/upper_band/prime_arity_upper_band_coprime_six_complete.md)证明所有素数p>=13、3p+10<=n<=4p-3且gcd(n,6)=1的全输入G=1充要判据，不限制n的素因子个数。一般最终阈值与未覆盖的2、3局部情形、两端短区间仍开放。

日期：2026-09-12。记 \(q\) 为每次平均的元数，\(n\) 为总位置数。对有理输入减去总体均值、清分母并本原化为
\[
X\in\mathbb Z^n,\quad \sum_iX_i=0,\quad \gcd_iX_i=1,\qquad
G(X)=\gcd_{i<j}|X_i-X_j|.
\]

## 1. 统一必要条件与量词

对任意 \(q,n\)，可达必然满足
\[
\boxed{\operatorname{rad}(G)\mid q,\qquad G\mid n.}
\]
第一条来自禁止素数的共同非零余类不变量；第二条来自零和与本原性。

定义 \(\mathcal P(q,n)\) 为“对所有有理输入，可达当且仅当 \(\operatorname{rad}(G)\mid q\)”。定义
\[
N(q)=\min\{N:\mathcal P(q,n)\text{ 对所有 }n\ge N\},
\]
\[
H(q)=\min\{n>q:\operatorname{rad}(n)\nmid q,\ \mathcal P(q,n)\}.
\]
\(H\) 是 \(G\) 真正筛选输入的非自动边缘；\(N\) 是最终阈值。自动维数满足 \(\operatorname{rad}(n)\mid q\)，此时G条件本身不筛选输入。

另有普遍小维数定理：\(n=q+1\) 时，可达当且仅当某个初始坐标已经等于总体均值。它不是一般G判据。

## 2. 已证的素数和小元数结果

### \(q=2\)

\[
n=3\Longleftrightarrow\text{三数成等差},\qquad
n\ge4:\quad \mathcal P(2,n).
\]
因此 \(N(2)=4\)。四元是自动G维数，非自动边缘 \(H(2)=5\) 已证。

### \(q=3\)

\[
\boxed{\mathcal P(3,n)\quad(n\ge7)}
\]
即 \(G\) 为三幂当且仅当可达；\(N(3)=H(3)=7\)。

### \(q=4\)

已证
\[
\mathcal P(4,7),\qquad \mathcal P(4,9),
\]
以及全部偶数 \(n\ge8\) 的完整判据。六元有 \(G=1\) 不可达例
\[
(-1,-1,-1,-1,0,4).
\]
所以 \(H(4)=7\)，但整体仍只有
\[
7\le N(4)\le16,
\]
\(n=11,13,15\) 未解决。

### \(q=5\)

已证 \(n=11,12,13\) 及全部 \(n\ge15\) 的完整判据。十二元由[统一文稿第11节的直接整数下降](../prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)补齐，十三元由[主同余群证明](../prime_arity/examples/five_average_thirteen_congruence_complete.md)承担。故
\[
H(5)=11,\qquad N(5)\in\{11,15\}.
\]
只有\(n=14\)仍未解决。若它满足完整判据，则N(5)=11；若存在合法反例，则N(5)=15。

### \(q=6\)

八元有 \(G=1\) 不可达例
\[
(-1^6,0,6).
\]
九元有固定四步网络，但G自动成立，只是辅助结果。十元已证
\[
\boxed{\mathcal P(6,10):\quad G\in\{1,2\}\Longleftrightarrow\text{可达}.}
\]
因为十元 \(G\mid10\)，这正是 \(G=2^a3^b\) 的简化；所以 \(H(6)=10\)。此外全部 \(3\mid n,\ n\ge6\) 及全部 \(n\ge24\) 已证。当前
\[
9\le N(6)\le24,
\]
未解决的非自动维数为 \(11,13,14,16,17,19,20,22,23\)。

### \(q=7\)

全部n>=15现已证明
\[
\boxed{\mathcal P(7,n)\quad(n\ge15),\qquad N(7)=H(7)=15.}
\]
最新[最优阈值证明](../prime_arity/examples/seven_average_sharp_threshold_complete.md)用原位置标量闭路、深主同余和完整方向—尺度有限证书补齐20、22元；接已证15—19、21及全部n>=23。十四元有已证G=1不可达族，故阈值15最优。一般p的最优阈值与五平均12、14仍开放。

### \(q=8\)

九至十二元有临界赋值反例；十三元已证
\[
\boxed{\mathcal P(8,13):\quad G=1\Longleftrightarrow\text{可达}},
\]
故 \(H(8)=13\)。最终 \(N(8)\) 未定。

### \(q=9,10,12\)

九平均十三元已由[平方元数统一控制器](square_arity_uniform_controller_and_nine_thirteen.md)完整证明M(9)=H(9)=13。十平均十七元、十二平均十七元两项也已证：
\[
\boxed{H(10)=H(12)=17,\qquad \mathcal P(10,17),\ \mathcal P(12,17).}
\]
N(9)仍未确定。十、十二平均十六元的G条件自动成立，不能代替十七元结论；十二平均十六元有固定四步网络，十平均十六元现也有固定六步网络，故M(10)=M(12)=16。

## 3. 任意平均元数的大维数定理

对任意整数 \(q\ge3\)，令
\[
d_q(n)=\#\{\ell:\ell\mid n,\ \ell\nmid q\}.
\]
已证明
\[
\boxed{n\ge4q-1+d_q(n)\Longrightarrow\mathcal P(q,n).}
\]
因此每个固定 \(q\) 都有最终阈值，且
\[
\boxed{N(q)\le4q+\lceil\log_2q\rceil+1\le5q.}
\]
证明不需要q为素数：非单位差分用 \(q/\gcd(\delta,q)\) 与其余份数的两值配比直接构造整数平均；中点碰撞、一般EGZ、保护池和整数能量下降随后完成闭包。

这是一条统一充分上界，不是最优临界线。

## 4. 原 \(B(q)\) 与精确临界线猜想

定义
\[
S(q)=\max_{p^a\parallel q}p^{\lceil a/2\rceil},
\]
并令
\[
B(q)=q+S(q)+
\begin{cases}
0,&\operatorname{rad}(q+S(q))\mid q,\\
1,&\operatorname{rad}(q+S(q))\nmid q.
\end{cases}
\]
赋值间隙不变量已证明：\(q<n<q+S(q)\) 存在 \(G=1\) 反例；边界 \(q+S(q)\) 在不自动的情形也存在反例。因此 \(M(q),N(q)\ge B(q)\)，其中 \(M\) 是排除平凡 \(n=q\) 后的最早完整G维数。

按当前“只关心G真正筛选输入”的标准，精确候选应为
\[
\boxed{C(q)=\min\{n\ge B(q):\operatorname{rad}(n)\nmid q\}.}
\]
已有下界给出 \(H(q)\ge C(q)\)。最自然的两条猜想是
\[
\boxed{H(q)=C(q)}
\]
以及更强的
\[
\boxed{M(q)=B(q),\qquad N(q)=M(q).}
\]
前者是非自动算术猜想；后者还要求自动点和后续维数没有空档。

代表性数值：
\[
\begin{array}{c|cccccccccccc}
q&2&3&4&5&6&7&8&9&10&12&14&15\\
\hline
B(q)&4&7&7&11&9&15&13&13&16&16&22&21\\
C(q)&5&7&7&11&10&15&13&13&17&17&22&21\\
\text{H状态}&已证&已证&已证&已证&已证&已证&已证&已证&已证&已证&未证&未证
\end{array}
\]

其中 \(q=10,12\) 的 \(B=16\) 是自动G点，必须跳到17；这正是“加一后仍可能自动”的情形。

## 5. \(B(q)\) 中自动G点的完整列表（\(q\le200\)）

\[
\begin{array}{c|c@{\qquad}c|c@{\qquad}c|c}
q&B(q)&q&B(q)&q&B(q)\\ \hline
2&4&6&9&10&16\\
12&16&20&25&30&36\\
42&49&54&64&56&64\\
75&81&90&96&110&121\\
120&125&132&144&138&162\\
156&169&182&196&&
\end{array}
\]
自动的精确定义始终是 \(\operatorname{rad}(B(q))\mid q\)；表格只是 \(q\le200\) 的枚举。

## 6. 奇端点 \(n=2q+1\) 的合数推广

端点的两部分必须分开：

- 若 \(2q+1\) 至多含两个不同素因子，已有统一三步入口；结合完整CRT陪集证书可证明全输入 \(G=1\) 判据。
- 统一CRT流程已核验36个指定合数level的32112条回路，其中28个两素因子level得到全输入结论，8个三、四素因子level的核心证书先行完成，后来四素因子入口定理已补齐，因此这36个列明端点均已完成全输入判据。
- 结合素数幂端点定理，在有限范围内所有奇 \(3\le q\le109\) 的 \(2q+1\) 端点均已解决。

一般合数level仍未有全称群包含定理；三个以上危险素因子的任意输入入口也曾是独立缺口。有限证书不能外推到任意level。

## 7. 自动网络与G等价的区别

自动G维数不应与非自动算术边缘混为一谈。例如：

- 二平均四元、六平均九元、以及 \(q=m(m-1), n=m^2\) 的固定四步网络族，都是无条件网络；
- 这些点说明存在一个固定全输入平均词，不说明相邻非自动维数；
- \(q=6,n=9\) 是无条件成功，真正的G筛选点是 \(n=10\)；
- \(q=10,12,n=16\) 的G自动，真正已证筛选点是 \(n=17\)。

## 8. 当前可复核入口

主要证明证书：

~~~text
python work/run_verifications.py --id six-average-ten-complete
python work/run_verifications.py --id seven-average-fifteen-complete
python work/run_verifications.py --id ten-twelve-seventeen-complete
python work/run_verifications.py --id four-average-seven-complete
python work/run_verifications.py --id eight-average-thirteen-complete
python work/run_verifications.py --id composite-endpoint-transfer
python work/run_verifications.py --id arbitrary-arity-linear-threshold
~~~

对应文档分别覆盖 \(H(6)=10\)、\(H(7)=15\)、\(H(10)=H(12)=17\)、\(H(4)=7\)、\(H(8)=13\)、合数端点有限推广以及任意q的大维数充分定理。各程序都区分定理证书、有限核验与探索性搜索，不把超时或有界搜索失败当成不可达证明。
