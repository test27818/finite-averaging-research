# 来源、原始布局与移植

本仓库是2026-09-16的公开研究快照，原始资料由用户与多个AI研究会话产生。

## 研究来源、审核与后续方向 / Research provenance, review and direction

本项目的新研究成果主要基于 **GPT-6 Astra（gpt6-astra）** 与用户的持续协作形成；研究历史中也保留其他AI的建议与复核。该说明描述本项目的研究过程，不改变二平均原始论文及其他引用成果的作者归属，也不表示每份历史文件都由同一模型产生。

The project's new research results were developed primarily through sustained collaboration between the user and **GPT-6 Astra (gpt6-astra)**. The history also preserves suggestions and reviews from other AI systems. This describes the research process; it neither reattributes the binary-averaging literature or other cited results nor claims that every historical file was produced by the same model.

已完成证明经过多轮内部审核、交叉复核、负例检查与针对性的精确核验，相关撤回、修正和依赖边界保留在[审核记录](archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/verification.md)和[审核文档目录](archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/audits/)。这不等于所有历史探索都成立、所有程序都无缺陷，或已取得外部同行评审／证明助手认证；本次复现发现的[已知计时问题](docs/KNOWN_ISSUES.md)也照实公开。

Completed proofs have undergone multiple rounds of internal review, cross-checking, counterexample checks and targeted exact verification. Audit records preserve withdrawals, corrections and dependency boundaries. This does not certify every historical exploration or script, and it is not external peer review or proof-assistant certification. Known reproduction issues are disclosed.

**当前研究仍在寻找更自然、更易读、更有结构且更统一的证明**：从已成立的局部论证中提取共同机制，减少孤立参数构造和有限计算证书，并使证明依赖与核验路径更容易理解。已有可达性结论和进一步简化目标须分别判断，一般合数元数的未解范围仍按各专题说明保留。

**Research continues toward more natural, readable and structurally unified proofs**: extracting common mechanisms from successful local arguments, reducing isolated constructions and finite computational certificates, and clarifying dependencies and verification. Established reachability results, proof-simplification goals and the remaining general composite-arity questions retain their separate scopes.

## 收录工作区 / Included workspaces

以下四个工作区已完整收录其文档、脚本和数据，路径均相对于本地研究工作区父目录：

| 原工作区 | 收录文件 | 用途 |
|---|---:|---|
| 2026-09-07/3-3-triple-average-research-note | 1669 | 主研究、全部平均元数、文献、历史和最新独立改进 |
| 2026-09-07/new-chat-3 | 107 | 二平均基准与早期三平均研究 |
| 2026-09-09/cha | 1 | 三平均历史文稿审阅 |
| 2026-09-10/new-chat | 128 | 论文、测试集和补充研究工作区 |

总计1905个原文件，139776624字节。以[FILES.json](catalog/FILES.json)中的SHA-256为准。保留重复历史版本，因为它们用于溯源，不合并覆盖当前正文。archive/下的源文件逐字节复制，原本地研究未被改写。

排除项共347个，均为Python运行缓存或LaTeX编译辅助文件；其相对来源和理由列在清单内。PDF、LaTeX源码、绘图、证书、原始日志性研究数据、打包ZIP和历史缓存型研究结果仍保留。与平均研究无关的图片工程、浏览器个人资料和应用认证配置未收录。

## 为什么保留日期层级

原文之间有跨工作区相对引用，Python核验器也会导入相邻脚本。保留日期和工作区名字能维持这些依赖；按主题的阅读入口放在topics/，不通过移动原核验器来制造新的路径断裂。

历史稿可能含已迁移的旧相对链接或原电脑的绝对路径。主项目的[路径迁移表](archive/2026-09-07/3-3-triple-average-research-note/work/document_reorganization_20260915/path_map.json)保留旧名对应关系。遇到失效历史路径时，优先从主题入口或完整文件目录定位同名文件。

本次未批量替换原文绝对路径，因为这会改变数学归档、代码常量或哈希基线。较新的主核验入口通常依据自身文件位置解析路径；历史探索脚本可在本机工作副本中修改其路径常量。

## 发布验证与研究验证

scripts/check_archive.py校验所有1905个原文件内容和新增导航的相对链接。发布核对另读取原核验注册，检查声明的文档与脚本存在，并运行二平均回归。

这验证公开副本的完整性与部分运行入口，不表示本次重跑了所有历史搜索、复核了每篇数学稿，或将项目形式化验证。历史已有核验结果随资料一并保存。

部分研究核验器会重写自己的JSON输出。若重跑后SHA-256改变，归档完整性检查会报告工作副本已变；可用Git查看差异，或在另一个工作副本运行。research/prime_arity_padic里的冻结文档基线也随原件保留。

[中文首页](README.zh-CN.md) · [English](README.md)
