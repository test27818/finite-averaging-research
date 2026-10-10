# 有限步平均研究

**统一接手入口：[knowledge/START_HERE.md](knowledge/START_HERE.md)。** 当前结论、证明链、开放问题、旧路线与核验入口已经集中整理；请从这里进入，不凭某篇旧文的“尚未解决”决定新任务。

| 要做什么 | 入口 |
|---|---|
| 五分钟了解数学状态 | [当前状态](knowledge/STATUS.md) |
| 看完整证明依赖与剩余接口 | [证明链](knowledge/PROOF_ROUTES.md) |
| 查相近思路以前做到哪里 | [路线边界](knowledge/ROUTE_GUARDS.md) · [结论卡登记](knowledge/catalog.json) |
| 找某个结论对应的程序 | [核验说明](knowledge/VERIFICATION.md) |
| 按文件查文献和历史材料 | [文档清单](knowledge/DOCUMENTS.md) · [旧成果目录](outputs/README.md) |

三平均 n≥7、全部奇素数平均 n≥2p+1 的 G 判据已有完整证明。自然统一、路径复杂度、五元静态分类与合数最优阈值是不同研究任务，范围和条件见当前状态。

在根目录检索：

```text
python knowledge/project_knowledge.py context "五元 小分母"
python knowledge/project_knowledge.py context "两根 列修正"
python knowledge/project_knowledge.py verify SEVEN-GEOMETRY
python knowledge/project_knowledge.py check
```

原证明在 `outputs/`，后续独立研究在 `research/`，计算材料在 `work/`。本次保留全部原文、脚本、证书和路径；导航原件存于[整理快照](work/documentation_memory_20260917/snapshots.json)。数学状态以准确的结论卡和原证明为准，散列／PASS 都不是数学认证。

研究者先读 [AGENTS.md](AGENTS.md)。新成果应更新已有结论卡、来源、后续替代和核验范围，不再把 README 写成时间线。完整维护与审查边界见[整理报告](knowledge/ORGANIZATION_AUDIT_20260917.md)。
