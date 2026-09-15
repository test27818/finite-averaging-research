# 完美可混合性与有限步平均 · Perfect Mixability and Finite Averaging

**中文 · [English](README.en.md) · [证明路线 / Proof guide](docs/PROOF_GUIDE.md) · [核验指南 / Verification](docs/VERIFICATION.md) · [中英术语 / Terminology](docs/TERMINOLOGY.md)**

研究一组有理数能否通过有限次操作变得**精确全等**：每次选恰好 $k$ 个不同位置，把这些位置的值全部替换为其算术平均。位置数固定，不增加副本、不丢弃输出。

本仓库覆盖**完美可混合性／完全可混合性（perfect mixability）、混合图（mixing graphs）、有限步平均（finite-step averaging）、二平均／两数平均（binary/pairwise averaging）、三平均／三数平均（ternary/triple averaging）、素数 $p$ 平均（prime-arity averaging）和一般 $k$ 平均（k-ary averaging）**。

**English overview.** Proofs, exact rational verifiers, finite certificates and algorithms for perfect mixability and finite-step averaging on fixed positions. Includes binary, ternary, prime and composite arities, mixing graphs, congruence obstructions, and state-dependent finite equalization. See the [English README](README.en.md) for the model, theorem scope, proof strategy and reproduction commands.

二平均直接来源为 Coviello Gonzalez–Chrobak 的 *Towards a Theory of Mixing Graphs: A Characterization of Perfect Mixability*（[arXiv:1806.08875v4](https://arxiv.org/abs/1806.08875v4)，[期刊DOI](https://doi.org/10.1016/j.tcs.2020.09.007)）。相关的有限时间共识（finite-time consensus）与团八卦算法（clique gossiping）可能使用不同量词，见[术语与模型区别](docs/TERMINOLOGY.md)。

## 首次阅读：从命题到核验

**研究来源与当前方向。** 本项目的新研究成果主要基于 **GPT-6 Astra（gpt6-astra）** 与用户的持续协作形成。已完成证明经过多轮内部审核、交叉复核与针对性的精确核验，审核记录、纠错和已知问题均予以保留。目前仍在寻找**更自然、更易读、结构更统一的证明**，以减少零散构造和计算证书依赖。这里的内部审核不等于外部同行评审或形式化认证；引用的既有文献成果仍归原作者。详见[研究来源与审核范围](PROVENANCE.md)。

1. [问题定义与术语](docs/TERMINOLOGY.md)：操作、Condition (MC)、差分gcd，以及“对每个输入找路径”和“固定网络处理全部输入”的区别。
2. [证明路线与审核地图](docs/PROOF_GUIDE.md)：二／三平均的重复值—能量法，素数临界范围的安全核心—真实返回—同余纤维法。
3. [185项命题—核验索引](catalog/CHECKS.md)：按结论查正文、脚本、证书、引用前提及证据边界。
4. [复现指南](docs/VERIFICATION.md)：在临时副本中执行检查，保留原归档；明确FAIL、SKIP和PASS的含义。


**公开快照：2026-09-16。** 本仓库收录四个相关研究工作区的 **1905 个原始文件**，包括 590 篇 Markdown、479 个 Python 脚本、42 份 PDF、22 份 LaTeX 源文件，以及证书、网页求解器、JavaScript、Prolog 和测试数据。原始文件逐字节保留；运行缓存和 LaTeX 编译辅助文件未收入。

## 按主题阅读

| 主题 | 入口 | 内容 |
|---|---|---|
| 二平均 | [二平均导航](topics/binary/README.md) | Perfect Mixability 文献复核、Python／网页／Prolog 求解器、1636 个基准实例 |
| 三平均 | [三平均导航](topics/ternary/README.md) | 直接证明、7—10 元基例、论文 PDF／LaTeX、旧算术路线 |
| 素数 $p$ 平均 | [素数平均导航](topics/prime/README.md) | 最优最终阈值、完整证明依赖、原位置返回、同余群、有限证书 |
| 一般 $k$ 平均 | [一般元数导航](topics/general/README.md) | 合数与素数幂、统一端点、固定网络、GRH 条件性结果和未解范围 |
| 最新结构改进 | [独立 p 进研究](archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/README.md) | 二进列提升、整格、载体、根与证明简化 |
| 算法测试 | [二平均基准](archive/2026-09-07/new-chat-3/averaging_benchmark/README.md) · [三／p 平均基准](archive/2026-09-10/new-chat/outputs/averaging_algorithm_benchmark/README.md) | 判定、路径构造、验解、复杂度与失败样本 |
| 完整目录 | [文件清单](catalog/FILES.md) · [机器清单](catalog/FILES.json) | 全部文档、脚本、数据及来源路径和 SHA-256 |

## 数学状态与阅读约定

按项目当前证明，奇素数平均的最优最终阈值为 $N(p)=2p+1$，二平均为 $N(2)=4$。阈值以上的有理输入经中心化、清分母、本原化后，可平均当且仅当差分公因子 $G$ 是 $p$ 的幂；仅在 $p\nmid n$ 时简写为 $G=1$。三平均另有独立的直接证明。

一般合数元数已有宽尾部、所有 $2k+1$ 端点、若干区间和小维数结论；平方族及部分素数幂结果明确带 GRH 条件。**这里没有宣称一般 $k$ 的最优最终阈值已完全解决。**

2026-09-16 的独立改进以同一个二进列提升引理替代内部偶余量的 64／256 类轨道表；原完成证明文件保留历史版本。九偏移的 162 组位置／根理想证书及其它依赖仍保留。参见[一般证明及核验](archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/structural_reassessment_and_uniform_dyadic_orbits.md)。

旧稿会出现已经过时的“未解”“当前最小例”等表述。请先读各主题导航和最新状态，再把旧稿用于研究溯源。证明、条件定理、有限证书、公式检查、探索搜索各自的量词不同；程序 PASS 不替代无限参数论证或引用的外部定理。

## 目录结构

~~~text
topics/                         二、三、p、k 平均导航
docs/                           中英术语、证明路线和复现指南
archive/
  2026-09-07/
    3-3-triple-average-research-note/
      outputs/                  按主题组织的主证明、历史、算法与文献综述
      research/prime_arity_padic/ 最新独立证明改进
      work/                     核验脚本、证书、原始资料、旧版本
    new-chat-3/
      averaging_benchmark/      二平均求解器和基准库
      outputs/                  早期三平均研究文稿
      work/                     早期探索脚本
  2026-09-09/cha/outputs/        历史文档审阅
  2026-09-10/new-chat/
    outputs/                    三平均论文、算法测试集、补充文档
    work/                       配套脚本与论文打包资料
catalog/                        全部文件与校验值
scripts/                        仓库完整性检查
~~~

保留工作区层级是为了维持已有相对路径和 Python 模块导入。没有将共同核验器按文件名前缀拆散；跨元数脚本的数学用途由原[核验注册](archive/2026-09-07/3-3-triple-average-research-note/work/verification_manifest.json)说明。

## 下载与运行

需要 Python 3.11 或更新版本。核心精确核验通常只用标准库；部分符号计算、线性规划及文献抓取另用 SymPy、NumPy、SciPy、Requests，可按需安装 [requirements.txt](requirements.txt)。

~~~sh
git clone https://github.com/test27818/finite-averaging-research.git
cd finite-averaging-research
python -B scripts/check_archive.py
python -B scripts/build_check_index.py --check
python -B scripts/reproduce.py --suite review
~~~

最后一条命令在临时副本中运行所选研究核验，需要Python 3.11+及Node.js；不会改写归档。它不是全项目数学审稿。下面是可选的原始入口命令，直接运行可能重写结果JSON。

**已知核验问题：** 本次数学检查通过，二平均Python回归有1项零预算状态测试失败；原因和确定性诊断见[已知问题](docs/KNOWN_ISSUES.md)，[失败日志](catalog/reproduction_review.txt)照实保留。没有将这次review标成全部通过。

素数证明注册与核验（以下从仓库根目录开始）：

~~~sh
cd archive/2026-09-07/3-3-triple-average-research-note
python -B work/run_verifications.py --list
python -B work/run_verifications.py --profile prime-proof
python -B research/prime_arity_padic/verify_uniform_dyadic_column_lifting.py
~~~

二平均求解器（另开终端，从仓库根目录开始）：

~~~sh
cd archive/2026-09-07/new-chat-3/averaging_benchmark
python -B src/construct.py '[38,-23,-14,16,-11,4,63,80,14,38]'
python -B -m unittest discover -s tests -v
~~~

直接打开二平均的 [solver.html](archive/2026-09-07/new-chat-3/averaging_benchmark/solver.html) 可离线使用。Node.js 用于 JavaScript 核验，SWI-Prolog 用于 Prolog 程序；浏览器测试另需原测试说明所列依赖。GitHub 普通文件页面不执行 HTML，下载后打开即可。

部分核验会重写原来的结果 JSON，届时归档哈希检查会报告变化；这表示工作副本已不同于初始快照。历史脚本可能包含旧电脑的绝对路径，需按本机路径调整，参见[移植与来源说明](PROVENANCE.md)。

## 来源与历史

本次公开整理保留用户与 AI 协作研究的完成稿、探索稿、纠错和失败路线；并非重新完成了一次全项目数学审稿。第三方论文、源码、网页抓取和题录保留各自来源与权利，见[资料来源与权利说明](THIRD_PARTY.md)。本仓库没有为第三方材料另行授予统一许可证。

[发布核对记录](catalog/PUBLICATION_CHECKS.json) · [源文件 SHA-256](catalog/SHA256SUMS.txt) · [原历史路线账本](archive/2026-09-07/3-3-triple-average-research-note/outputs/history/research_routes_history_20260915.md)
