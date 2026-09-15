# B12、B15、B18、B21 的统一有限比较

**后续状态：** [十二元完整判据](../arithmetic_cases/triple_average_twelve_arithmetic_complete.md)、[十五元完整归约](../arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md)与[十八元完整归约](../arithmetic_cases/triple_average_eighteen_via_twelve_complete.md) 已闭合，B21 是七元提升的已知对照。本表仍保留有限实验本身的证据范围，不能把小高度覆盖替代这些一般证明。

本记录对应 work/explore_single_prime_kernels.py。搜索的是
\[
\mathcal B_n(u,v)=(u^{n-4},v^3,-(n-4)u-3v)
\]
的本原整数参数，按全局符号取商。合法域为
\[
\gcd(u,v)=1,\quad
\gcd(u-v,n/3^{v_3(n)})=1,\quad \max(|u|,|v|)\le8.
\]
包括所有 G 为三幂的方向，不能再限制成 G=1。B21 属于已解决的 \(7\cdot3\) 塔，本实验是其二维核方法的对照，不是新的一般判据。

## 终端契约

搜索只认与 n 的三进展开对应的零和三幂块分拆：

| n | 分拆 | 归零网络的固定尾段步数 |
|---:|---|---:|
| 12 | 3+9 | 7 |
| 15 | 3+3+9 | 8 |
| 18 | 9+9 | 12 |
| 21 | 3+9+9 | 13 |

每个证书包括前缀操作词、前缀末状态及所有块的计数；父进程复核操作重数、状态、各块零和、各块大小及完整分拆。搜索深度只计前缀；完整归零长度还要加尾段。

这是充分终端条件，未找到这种分拆并不排除其他归零路线。最终全零状态显然满足这种分拆，故不影响无深度界搜索的完备性；但不能因此把有界搜索认作判定算法。

## 实测边界

| n | 合法符号类数 | 深度 3 已覆盖 | 深度 4 已覆盖 | 深度 5 补充 |
|---:|---:|---:|---:|---|
| 12 | 62 | 60 | 62 | 无需加深 |
| 15 | 73 | 50 | 71 | 两个缺口全部找到证书 |
| 18 | 62 | 46 | 62 | 无需加深 |
| 21 | 79 | 37 | 66 | 全量得到 79/79 |

因此此高度界内完整覆盖的前缀最大深度为 4、5、4、5。B15 的两个四步缺口为 (-8,3)、(-7,-6)；B21 的四步缺口共 13 个。没有把这些有限数据提升为无界定理。

复现四维数深度四：

    python work/explore_single_prime_kernels.py --bound 8 --depth 4 --jobs 8 --summary

复现两项深度五补充：

    python work/explore_single_prime_kernels.py --n 15 --bound 8 --depth 5 --jobs 2 --pair=-8,3 --pair=-7,-6 --summary
    python work/explore_single_prime_kernels.py --n 21 --bound 8 --depth 5 --jobs 8 --summary

数值搜索默认使用本原整数状态商，并在命中后精确恢复每步实际 Fraction 值；证书仍由原始轨迹重放。旧引擎可用 --engine fraction 对照。两者最短深度分布一致；[B21 性能复核](triple_average_b21_integer_search_optimization.md) 记录了等价性证明和实测加速。

## 计算改进与数学结论

只按不同数值及其重数枚举三元组；零和分拆统一清分母成整数；尾部两个计数由线性方程解出，最后一个块直接检查补集。这些优化保留全部候选分拆，用独立的位置子集枚举做了 720 项比对。

一般宏族、混合返回长度下界、实范数下降的三进障碍和 theta 格对应，见 [三进扩张修复宏与算术接口](triple_average_carry_repair_and_arithmetic_interface.md)。有限覆盖本身不证明类数决定搜索深度，也不证明固定核返回群是算术群。
