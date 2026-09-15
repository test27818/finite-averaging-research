# 二平均 · Binary and Pairwise Averaging

English: **perfect mixability**, **binary averaging**, **pairwise averaging**, **mixing graphs**, and **Condition (MC)**. This topic contains the literature-based decision criterion, constructive solvers, exact path verification and the 1,636-instance benchmark. Start with the [English overview](../../README.en.md) and [bilingual proof guide](../../docs/PROOF_GUIDE.md).

[返回仓库首页](../../README.md)

二平均将选中的两个数都替换为其平均值，要求有限步精确全等。请区分可达性判定、构造一条路径和认证最短路径。

- [问题定义、判据、特殊维数](../../archive/2026-09-07/new-chat-3/averaging_benchmark/problem.md)。
- [完整求解器与1636题基准](../../archive/2026-09-07/new-chat-3/averaging_benchmark/README.md)：Python、网页、Prolog、测试与已核验路径。
- [Python 源码](../../archive/2026-09-07/new-chat-3/averaging_benchmark/src/) · [测试](../../archive/2026-09-07/new-chat-3/averaging_benchmark/tests/) · [网页](../../archive/2026-09-07/new-chat-3/averaging_benchmark/solver.html)。
- [Perfect Mixability 原文复核及向三平均迁移](../../archive/2026-09-07/3-3-triple-average-research-note/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)。
- [arXiv:1806.08875v4 源码资料](../../archive/2026-09-07/3-3-triple-average-research-note/work/literature_20260911/mixability_v4/)；作者与出版信息以原文为准。
- [主项目原网页求解器](../../archive/2026-09-07/3-3-triple-average-research-note/2-average-solver.html)。

求解器有时间、内存或搜索预算限制。没有找到路径不等于证明不可达；返回路径的验解和最短性认证分别记录。

本次复现记录了一个零预算状态的计时边界问题，见[已知问题 / Known issue](../../docs/KNOWN_ISSUES.md)。原代码与失败证据均保留，未宣称本次Python回归全绿。
