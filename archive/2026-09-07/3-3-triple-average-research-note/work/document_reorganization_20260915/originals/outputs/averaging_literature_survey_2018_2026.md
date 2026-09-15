# 二平均之后的文献进展：2018--2026 检索与可用工具

后续战略检索见[任意 p 路线重评估](prime_arity_strategy_reassessment_20260912.md)：44个结构查询得到148篇去重题录，并下载阅读 S-整数 SL2 有界生成、语言约束 Lyapunov、多面体 path-complete 和 Chevalley 有界生成四份全文。新增的 2026 SL2 预印本报告至多7个初等因子；这些结果仍不自动带来原位置运输。

检索日期：2026-09-12。

同日后续：[逆零和定理的实际转译](inverse_zero_sum_averaging_progress.md)已给出O(p)模运算的带副本选择、相反碰撞恢复、五平均十四元配对核的部分完整分类，以及所有奇数p>=5的2p+4元七步二参数族。安全性和碰撞不再只停留在这篇综述的候选说明中，但一般阈值仍未改善。

## 1. 本轮结论

有值得借用的后续进展，但本轮没有找到已经证明以下结论的公开文献：

- 固定原位置、每次把恰好三个或一般 p 个值同时替换为算术平均时，对任意有理输入的完整可达判据；
- 一般奇素数平均元数的最优阈值 N(p)=2p+1；
- 由端点维数直接内插整个中间区间的定理。

这是本轮检索的结果，不是“这些文献不存在”的证明，更不能单凭它认定项目结果具有发表意义上的首次性。

最值得优先借用的三类材料是：

1. **2022 年逆加权零和定理**：把“没有可用选择”转成强制的重复余数结构，最贴近当前重数与容量问题。
2. **2019 年正式发表的 Clique Gossiping**：提供真正的多点平均框架与有限步全初值网络判据，但必须区分其量词与本项目。
3. **2021--2022 年块 Kaczmarz 与 gossip 的统一分析**：可用于合法块的能量下降和速度分析，不能直接代替精确有限终止。

另找到 2022 年确定性 O(n log n) 的 EGZ 构造预印本，是改进现有实现的明确候选，但没有改善 2n-1 的一般长度门槛。

## 2. 检索范围和证据等级

实际检查了以下路线：

- 原论文的 arXiv、会议和期刊版本，分别查正向引用；
- 原作者的后续题录、2019 年博士论文，以及作者主页；
- clique gossip、finite-time consensus、block gossip、Kaczmarz；
- mixing graphs、mix-reachability、随机矩阵与幂等／可达性关键词；
- EGZ、逆零和、加权零和、构造算法；
- 2024--2026 年相关题录和主要相关论文的后续引用。

使用 Crossref、OpenAlex、Semantic Scholar 的公开接口，并回到 Dagstuhl、大学论文库、作者主页、Springer 和 Integers 期刊核对。
保存了数十份成功或返回明确错误状态的检索／页面响应记录；另下载并提取三份新增全文：2019 年博士论文、2022 年逆零和论文、2024 年 splitter networks 论文。

访问限制：本机直接连接 arXiv 多次失败，Semantic Scholar 后续请求受到限流，Google 无法连接，Bing 对稀有术语退化为无关结果，部分出版商只开放摘要。
因此下面明确区分“已读全文相关章节”和“只核对摘要、题录”。未读到全文的材料不作为已审定可直接调用的证明。

还遇到两种数据库问题：同一论文的预印本、会议和期刊记录分散；Miguel Gonzalez 的作者记录混入了同名化学作者。
直接引用图也有漏项：2024 年 splitter 论文的正文确实引用原论文，但并未出现在本次 OpenAlex 原论文引用列表中。
因此不把数据库的引用数当成研究进展的完整计数。

## 3. 原论文并非只有“2018 年版”

Miguel Coviello Gonzalez、Marek Chrobak：
**Towards a Theory of Mixing Graphs: A Characterization of Perfect Mixability**。

- 2018 年 arXiv 预印本：[arXiv:1806.08875](https://arxiv.org/abs/1806.08875)。用户提供的 v4 源码已在项目中阅读。
- 2019 年 CIAC 会议扩展摘要：[DOI 10.1007/978-3-030-17402-6_16](https://doi.org/10.1007/978-3-030-17402-6_16)。
- 2020 年正式期刊版：Theoretical Computer Science **845**, 98--121；[DOI 10.1016/j.tcs.2020.09.007](https://doi.org/10.1016/j.tcs.2020.09.007)。Crossref 给出 2020 年 12 月卷期，OpenAlex 给出 2020-09-10 的日期。

这三个记录属于同一研究成果的版本链，不能把 2020 年期刊版算成三平均推广。

原文末节提出的主要后续问题是一般 MixReachability、单滴目标的最小浪费，以及给定线性映射是否由 mixing graph 实现。
这些问题比“最终全部相等”的 perfect mixability 更宽；原文没有给出一般 p 平均定理。

## 4. 直接后续：作者论文与 2024 年网络工作

### 4.1 2019 年博士论文：补充材料比会议稿丰富

Miguel Coviello Gonzalez，**Towards a Theory of Droplet-Mixing Graphs in Microfluidics**，UC Riverside，2019 年 9 月。

[大学正式条目](https://escholarship.org/uc/item/4wb2g5z2)；
[公开全文](https://escholarship.org/content/qt4wb2g5z2/qt4wb2g5z2.pdf)。

本轮阅读了模型、贡献概述、perfect mixing 及第四章相关范围说明。
除二平均定理外，论文包含固定深度困难性、一般输入输出的 dominance 必要条件和某些特殊目标的可判定性。
它明确区别：在允许任意体积混合的 fluid 模型中，dominance 也是充分条件；固定液滴模型中则不是。

**与项目的关系：** 这与我们已经遇到的“连续运输／majorization 可行不等于原位置平均词可实现”是同一种边界。
博士论文并没有把该边界解决，也明确将研究限定在 1:1 混合模型。

### 4.2 2020 年 RPRIS：真实续作，但目标不同

Coviello Gonzalez、Chrobak，**A Waste-Efficient Algorithm for Single-Droplet Sample Preparation on Microfluidic Chips**。

2019 年预印本 [arXiv:1908.09618](https://arxiv.org/abs/1908.09618)，2020 年 ACM Journal of Experimental Algorithmics 正式版：
[DOI 10.1145/3408297](https://doi.org/10.1145/3408297)。

其 RPRIS 算法为单个目标液滴构造混合图，改善最坏情形的浪费上界和实验表现。
本轮核对了摘要、正式题录，并读到博士论文中相应问题的介绍。

**限制：** 它允许按目标制备并处理剩余液滴；不是固定 n 个值全部归零的系统，也没有证明一般 k 元平均的阈值。

### 4.3 2024 年 splitter networks：流与稳态方面的实质进展

Basile Couëtoux、Bastien Gastaldi、Guyslain Naves，
**The Steady-States of Splitter Networks**，FUN 2024。

[正式出版页和开放全文](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FUN.2024.9)。本轮已读相关全文。

主要结果：计算 splitter 网络稳态的多项式时间方法；通过带相等约束的循环流及辅助 Markov 链处理流量；构造平衡网络，并证明 Omega(n log n) 的节点下界。
它明确引用 2020 年 perfect mixability 论文。

**关键区别：** 该模型允许有向循环，研究稳态流量。正文明确指出，为任意数量的输出实现平衡，有向循环可能是必要的。
所以不能把稳态存在定理直接解释成固定个数液滴经有限次平均完成。

**可借用处：** 相等约束流、残余网络和障碍证书的组织方式，可用于研究某些具体运输方案。
它不提供一般“运输矩阵到有限正向平均词”的分解定理。

## 5. 与 p 平均最直接相邻的文献：Clique Gossiping

**2026-09-12合数平均复核更新：** 下述机构摘要的整除表述不能直接当作本项目的定理。[六平均九元的固定四步原位置网络](composite_arity_four_six_transfer.md)已对全部标准基精确重放，得到J9/9，但6不整除9。尚未取得全文，无法确定完整假设或摘要表述的差异；本项目后续结论不调用“m|n必要”。以下保留原始摘要阅读记录，不将它视为已经核验的适用判据。

Yang Liu、Bo Li、Brian D. O. Anderson、Guodong Shi，
**Clique Gossiping**，IEEE/ACM Transactions on Networking，2019。

[DOI 10.1109/TNET.2019.2952082](https://doi.org/10.1109/TNET.2019.2952082)；
[作者机构正式记录](https://hdl.handle.net/1885/307516)；
[预印本 arXiv:1706.02540](https://arxiv.org/abs/1706.02540)。

注意其预印本早于 2018 年，2019 年是正式发表时间，不宜说全部思想都在原论文之后才出现。
本轮核对了作者机构摘要、期刊题录和后续引用；机构 PDF 受限，未读到全文证明。

该文研究沿 clique 序列进行多节点线性交互，其中 clique averaging 正是把一个组的节点一起取平均。
摘要明确报告：使用相同大小 m 的 clique，存在全初值有限步共识网络的充要条件是 m|n，且 m、n 有完全相同的素因子集合。
它还研究最快的有限步构造，以及无环广义线图下的谱次序不变性。

### 为什么这不反驳我们的 p 平均研究

对 p 为素数，上述全初值网络条件给出 n 必须是 p 幂。
这种目标是寻找一个线性操作词 W，使

\[
\exists W\quad\forall x\in\mathbb R^n,
\qquad W x=\frac{\sum_i x_i}{n}\mathbf1.
\]

我们的目标则允许

\[
\forall\text{ 合法 }x\in\mathbb Q^n\quad\exists W_x.
\]

两者不能交换量词。
事实上，一个固定 p 平均词的矩阵元素都在 Z[1/p]；如果它对所有实输入精确平均，其矩阵必须是 J/n，于是 1/n 必须属于 Z[1/p]，立即要求 n 为 p 幂。

**可借用处：** 多点平均的统一矩阵框架、张量式有限网络、原子顺序的交换与谱简化。
**不能借用成：** “不是 p 幂时所有合法有理输入都不可达”，或一般 2p+1 阈值定理。

## 6. 2021--2022 年：块平均作为 Kaczmarz 投影

### 6.1 统一框架与加速

Nicolas Loizou、Peter Richtarik，
**Revisiting Randomized Gossip Algorithms: General Framework, Convergence Rates and Novel Block and Accelerated Protocols**，IEEE Transactions on Information Theory，2021。

[DOI 10.1109/TIT.2021.3113285](https://doi.org/10.1109/TIT.2021.3113285)；
[2019 年预印本](https://arxiv.org/abs/1905.08645)。

将平均共识转成特定线性系统，把迭代线性求解器解释为分布式 gossip，涵盖成对、路径和块平均，并发展加速与对偶方法。
本轮核对摘要和正式题录，未取得全文。

### 6.2 从不交铺分推广到覆盖

Jamie Haddock、Benjamin Jarman、Chen Yap，
**Paving the Way for Consensus: Convergence of Block Gossip Algorithms**，
IEEE Transactions on Information Theory **68(11)**, 7515--7527，2022。

[DOI 10.1109/TIT.2022.3202733](https://doi.org/10.1109/TIT.2022.3202733)；
[预印本 arXiv:2110.14609](https://arxiv.org/abs/2110.14609)；
[作者出版目录](https://jamiehaddock.com/publications/)。

把 clique、path、同步成对 gossip 与 block randomized Kaczmarz 联系起来。
分析允许比 paving 更一般的 block coverings，并涵盖秩亏系统，改善收敛界。
本轮核对摘要、作者研究页面、正式卷期及后续引用；未取得全文。

**对项目的实际意义：** 可以将当前允许的安全平均组看作一族投影，研究这族投影是否仍覆盖所有需要消去的方向，以及是否具有统一能量下降比例。

**不能省略的一步：** 几何速度或期望收敛不是有限步精确归零。
若 p 进分母可以无限增长，能量趋于零时仍可能永远不为零。
要把这样的估计转成有限终止，必须另有固定离散格、精度界，或精确终端机制。
论文中的加速权重、额外状态或松弛操作也必须逐项检查是否仍是允许的 p 平均。

## 7. 最贴近当前阈值缺口的新材料：逆加权零和

### 7.1 已读全文的 2022 年定理

Sukumar Das Adhikari、Shruti Hegde、Md Ibrahim Molla、Subha Sarkar，
**Inverse Problems Related to Some Weighted Zero-sum Constants for Cyclic Groups**，
Integers **22 (2022), A7**，2022-01-07 发表。

[期刊公开全文](https://math.colgate.edu/~integers/w7/w7.pdf)；
[期刊卷目录](https://math.colgate.edu/~integers/vol22.html)。本轮已读定理 1 及其证明。

对 A={1,...,r}、1<r<n，文中定理 1 给出：长度 ceil(n/r)-1 的 Z/nZ 序列没有非空 A-加权零和子序列，当且仅当它是同一个单位的重复。
文中还处理平方单位权重的某些素数幂与平方自由模数；这些分支不是当前最直接需要的部分。

这类结果比只知道“足够长时必有选择”更有用：它精确描述失败时的形状。

### 7.2 可以直接转译成真实副本选择的推论

令 p>=5 为奇素数，k=(p-1)/2。假设有 k 对带标签副本，值分别为 x_1,...,x_k，另有一个 p 重锚点 a。
若 x_i-a 的模 p 余数不是同一个非零余数的重复，则上面的定理取 r=2 给出

\[
c_i\in\{0,1,2\},\qquad
1\le s=\sum_i c_i\le p-1,
\qquad
\sum_i c_i(x_i-a)=0\pmod p.
\]

取 c_i 份真实 x_i，再用 p-s 份 a 补足 p 个位置，就得到一次整数 p 平均。
每个系数至多 2，正好由两份实际副本提供；总位置数也严格受到控制。

这可用于 n=3p-1 等维数中“剩余位置恰形成多对副本”的配置。
它没有凭空允许加权平均。

仍须另证：保留所有非 p 同余见证，避免新均值碰撞到唯一完整保留的重值，以及不能立即继续时的终止机制。
所以这是可用的局部引理来源，尚不是中间区间的完整证明。

### 7.3 其他相关的新材料

Md Ibrahim Molla，**Some inverse problems in zero-sum theory**，
Proceedings - Mathematical Sciences **132**, article 63，2022。

[DOI 10.1007/s12044-022-00712-4](https://doi.org/10.1007/s12044-022-00712-4)。
本轮读到出版商摘要和引用列表，全文受限。
它继续研究若干加权零和常数的极值序列分类；不能在未检查具体权重集与位置容量前直接调用。

## 8. 2022 年 EGZ 的确定性近线性构造

Seok-Hwan Choi、Hanpil Kang、Dongjae Lim，
**Simple deterministic O(n log n) algorithm finding a solution of Erdős-Ginzburg-Ziv theorem**，2022-08-16 预印本。

[arXiv:2208.07728](https://arxiv.org/abs/2208.07728)。

作者给出从任意 2n-1 个整数中构造 n 个和被 n 整除的元素的确定性 O(n log n) 算法。
本轮核对了预印本题录和摘要，未取得全文，也未确认后续正式期刊版本。

**可用价值：** 项目已证明的保护池步骤仍可先排除少量禁选位置，再调用更快的 EGZ 构造。
这比继续使用通用固定基数模 p 动态规划更值得作为实现优化候选。

**严格限制：** 它不把一般长度门槛从 2n-1 降低。
输入任意大整数的读取、取模及位运算成本还需按原文计算模型核对，不能直接把摘要的 O(n log n) 写成无条件的位复杂度界。
本轮没有把尚未阅读全文的算法替换进正式证明核验器。

## 9. 2024--2026 的命中中，哪些不能当作突破

- **Constructing Stochastic Matrices for Weighted Averaging in Gossip Networks**，Erkan Bayram、Mohamed-Ali Belabbas，IFAC-PapersOnLine，2025；[DOI 10.1016/j.ifacol.2025.07.049](https://doi.org/10.1016/j.ifacol.2025.07.049)。摘要明确研究无限乘积及有限极限集，并允许设计随机矩阵，不是固定 p 个位置全等化的有限词分解。
- **Privacy-Preserving Distributed Average Consensus in Finite Time using Random Gossip**，2022；[DOI 10.23919/ECC55457.2022.9838457](https://doi.org/10.23919/ECC55457.2022.9838457)。虽然题名含 finite time，摘要明确说 approximate average consensus，因此不是精确归零定理。
- **Block Matrix and Tensor Randomized Kaczmarz Methods for Linear Feasibility Problems**，2025；[DOI 10.1007/s44007-025-00163-z](https://doi.org/10.1007/s44007-025-00163-z)。摘要结论是期望意义的线性收敛。
- **Finite-field consensus networks with multi-communication channels and time-delays**，2026 年题录；[DOI 10.1016/j.ffa.2026.102814](https://doi.org/10.1016/j.ffa.2026.102814)。本轮只取得题录，不把有限域共识外推成有理数精确平均结论。

大量含 mixing、gossip 的检索命中实际研究图神经网络、信息传播、概率分布的 joint mixability 或连续流体。
这些不属于原平均操作模型，未列入可用定理。

另一个 OpenAlex 命中为 Zakharov 的 **Convex geometry and the Erdős-Ginzburg-Ziv problem**，预印本 [arXiv:2002.09892](https://arxiv.org/abs/2002.09892)。其高维 EGZ 摘要有研究价值，但本轮数据库给出的期刊 DOI 无法解析，未把该期刊信息采纳为已核验事实；也未将高维渐近界当成一维 2p-1 门槛的改进。

## 10. 对当前项目的建议

优先读取和转译逆零和论文，将“参与次数”明确解释为真实副本数，并加入总长度、禁选位置和均值碰撞约束。
这最有机会直接处理不同余双重值与非等重数三值配置。

其次利用 block Kaczmarz 的覆盖分析研究已经合法的宏族是否有统一下降速度，同时保留精度或整数格条件。
它适合帮助完善多步下降证明，不能仅凭谱隙宣布精确终止。

实现优化方面，应在获得并审阅 2022 年 EGZ 算法全文后，独立实现和交叉核对，再决定替换现有动态规划。

本轮没有找到一个可以直接接上、立刻解决所有 p 或整个中间区间的模形式／Hecke 定理。
现有后续文献里，最贴近项目当前缺口的是带容量的零和结构和投影块覆盖，而不是再给形式群换一个描述。

本页是外部文献检索与接口分析，不是新的全维数可达性证明。
