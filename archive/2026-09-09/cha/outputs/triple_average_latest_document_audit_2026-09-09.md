# 三平均项目最新文档严格审计

审计截止：2026-09-10（Asia/Shanghai）。对象为
`C:\Users\19226\Documents\Codex\2026-09-07\3-3-triple-average-research-note` 当前版本。

## 当前判断

上一轮指出的数学和验证工程问题已基本修复。当前没有发现新的数学反例；二十五元已经补为独立完整判据，奇数合数闭包因此从“至多一个5”升级为“任意五幂”。当前最小尚未闭合维数为20，下一个未解素数为29；一般任意 n 仍未解决。

## 本次复核：为什么历史公式可取 epsilon=1

旧交接稿中的
\[
n=3^a5^\varepsilon\prod_{p\in P}p^{e_p},\qquad \varepsilon\in\{0,1\}
\]
不是一个未解释的数论限制，而是二十五元尚未完成时的归纳边界。因子桥遇到商大小5时不能调用错误的A(5)；归并后得到的是若干份同一个合法五元商。对任意至少两份，复制数可写为
\[
a=2x+3y,
\]
两份调用A(10)，三份调用A(15)，所以一次因子5可以收尾，这就是epsilon=1的依据。

这并不自动处理25，因为归纳会遇到A(25)本身。2026-09-10的二十五元完整证书已经通过 `n25-complete`，并且奇数闭包通过 `odd-composite-factor-closure`；因此当前正式结论应写成
\[
n=3^a5^b\prod_{p\in P}p^{e_p},\qquad b\ge0,
\]
而不是继续把epsilon in {0,1}当作最终边界。A(5)仍未被假定或证明；被补齐的是A(25)及其后的强归纳接口。

已确认的修复只简记如下：

- p=2 合法性改为直接检查 u-v 的奇偶性；S-高度加入规范化代表和二处参数格尺度。
- 固定分层的非奇异返回群与分层间奇异对应已分开；复杂度条件补充了宏展开长度和中间位长。
- B12 实验覆盖完整合法域的 62 类；标准接口、非法证书和 Python 优化模式均有清单核验。
- n12-complete 已登记进 smoke/core/full，不再依赖 B12 有界 BFS。
- n18-via-twelve-complete 已登记进 smoke/core/full；十八元使用十二元已证子程序和偶重数配对，不依赖 B18 自身的返回群。

## 复核结果

- `smoke`：10/10 通过。
- `core`：15/15 通过（此前 14/14 的记录对应十八元登记前的清单版本）。
- n18-via-twelve-complete：十二元证书重跑通过，7460 个局部子问题和 24 个物理三进网络尾段通过。
- n12-complete：四个真实宏、正向逆元、12 个陪集、独立模 8 标签、唯一合法 cusp 和六步终端全部通过。其数学结论是 n=12 及 n=12*3^k 的 G=3^a 充要性。
- B12 高度 8 深度 4：62/62；B15 两个缺口深度 5：2/2；B21 高度 8 深度 5：79/79。
- B12 六步分支、返回前沿 503 条目、theta/二次型结构、标准接口 229 个样本和搜索契约均通过。
- `n25-complete`：18 个通用模板、30 个模25陪集、唯一合法宽度25 cusp、858 个显式输送和446个安全核心桥全部通过。
- `odd-composite-factor-closure`：奇数边界5项、8整除边界2项、4404个奇数因子计划、1654个8整除因子计划、943个多例外接口和2210个35元桥全部通过。

十二元证明的关键逻辑已经闭合：高维安全下降进入
B_12(u,v)，四个真实宏及其正向逆元生成一个包含共轭 Gamma_0(8) 的指数 12 子群；模 8 陪集只有一个合法 cusp，代表 (1,0) 有六步真实终端。脚本核验的是有限群证书和宏账本，安全下降与任意列补全的全称部分仍由证明文档承担，这个证据边界标注是正确的。

## 仍需同步的文档

这些是过时表述，不是新的数学漏洞：

1. `outputs/triple_average_general_n_synthesis.md` 仍使用不含 12 的旧基维数集合和旧算法范围。
2. `outputs/triple_average_arbitrary_n_outlook.md` 仍列 `{7,8,10,11}`，没有加入 12。
3. `outputs/triple_average_arithmetic_geometry_view.md` 及部分早期综合稿仍使用十二元完成前的维数列表。
4. `outputs/triple_average_b12_kernel_experiment.md` 仍有“下一步建立 B12 控制器”的旧句子；现在应改为 B15/B18 或一般接口研究。
5. `outputs/triple_average_carry_repair_and_arithmetic_interface.md` 开头的“不声称 n=12 已解决”与后文“B12 已闭合”容易表面矛盾，应改成“本文自身的宏族分析不承担 n=12 定理”。
6. `README.md` 仍把 B12 链接描述为“首个二维核实验”，最好同时标出已完成的十二元完整判据；有限实验只作为辅助回归。
7. `outputs/triple_average_twelve_arithmetic_complete.md` 第 1 节仍把 18 列为“其他尚未解决的情形”；十八元归约已经完成，应改为“发现阶段旧描述”。
8. `outputs/triple_average_carry_repair_and_arithmetic_interface.md` 第 3、5 行仍把 B18 列在开放问题中；正文后面已有十八元更新，应统一改为 B15 和一般多块问题开放。
9. `outputs/triple_average_kernel_interface_and_automorphic_route.md` 与 `outputs/triple_average_q_average_arithmetic_geometry.md` 仍把 B18 写成待处理的独立二维控制器；现在应注明 B18 已通过十二元子程序解决，但 B15 和一般接口仍开放。

`b12-complete-bounded-domain` 在清单中仍标为有限实验、不是 n=12 定理，这是正确的，因为该条目只验证高度 8 的有限域；不要把它改成 theorem-certificate。

## 总结

当前应以 README、最新交接稿、研究勘误、n12-complete/n18-via-twelve-complete 清单条目和本文档为准。核心数学状态是：已解决基维数为 7、8、10、11、12、13、18，以及它们的三进塔；开放部分从 14 开始，并集中在 B15、一般多块终止约化、链间耦合、正向 Hecke/算术控制和三份复制消去。
