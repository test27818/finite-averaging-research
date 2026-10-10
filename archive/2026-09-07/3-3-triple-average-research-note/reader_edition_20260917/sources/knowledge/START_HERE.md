# 接手入口：先定位问题，再阅读证明

这里解决“同一项目反复发现旧结果”的问题。原论文式证明和研究经过保留原位置；当前结论、真正缺口、替代关系和核验入口集中登记在 [catalog.json](catalog.json)，专题页和状态页由它生成。

先读 [当前状态](STATUS.md)，再选一个主题：

| 任务 | 入口 |
|---|---|
| 三平均全部 n≥7 的完整证明与几何解释 | [三平均与统一几何](topics/triple.md) |
| 全部素数元数的阈值，以及减少分段／证书的研究 | [素数定理与自然统一](topics/prime.md) |
| 五元、六元及 p<n≤2p | [阈值以下与五元算术](topics/subcritical.md) |
| 合数元数、M/H/N、GRH 条件 | [一般元数](topics/composite.md) |
| 计算复杂度、最短路径、求解器 | [算法与核验](topics/algorithms.md) |
| 外部定理、已排除的偷换、历史路线 | [公共工具与路线边界](topics/interfaces.md) |

理解证明全貌读 [证明链与开放接口](PROOF_ROUTES.md)。开始一个新想法前读 [避免重复研究的路线表](ROUTE_GUARDS.md)。严格核验读 [核验使用说明](VERIFICATION.md)。全部 Markdown 的文件级定位在 [文档清单](DOCUMENTS.md)，它只作发现，不自动判定正文真假。

素数研究先看[参数范围 × 启动 × 收尾 × 残留证据](topics/prime.md#当前参数覆盖启动与收尾分开看)。大型数学项目的现成工具与本项目适配建议见[Blueprint、ANTEDB及证明执行harness调查](MATH_PROJECT_HARNESSES.md)。

## 一个接手动作

在项目根目录执行：

```text
python knowledge/project_knowledge.py context "五元 小分母"
python knowledge/project_knowledge.py context "两根 列修正"
python knowledge/project_knowledge.py context "偶数部分统一了吗"
python knowledge/project_knowledge.py context "上半区三段选参是否合并"
python knowledge/project_knowledge.py search "Hecke"
python knowledge/project_knowledge.py show FIVE-TEMPLATE-ESCAPE
```

`context` 返回相关结论卡、已登记的前提、后续替代、历史核验及正文命中。它是阅读包，不是自动数学判断。进入原文以后仍须核对符号、假设和量词。

## 几条容易混淆的状态

- 三平均 n≥7 和全部奇素数平均 n≥2p+1 的可达性已有完整证明。继续研究自然统一，不意味着原定理尚缺证明。
- 五元逐输入判定及最短操作已解决；尚缺的是用户要求的一次性算术分类。固定 D 的全词逃逸仍是猜想，多块固定模板已给证明。
- 七元与 Γ₀(7) 的对应有真实正向宏支撑；一般 Hecke 分支之和、群闭包或运输存在不具备这个自动接口。
- 原素数基线证书与独立研究的剩余根资源清单属于不同版本／作用范围；当前计数直接查 PRIME-TOTAL、PRIME-FIVE-RETURNS 及覆盖表。不能仅修改一个计数便宣称整篇新证明已重审。

## 维护责任

结论状态、依赖和脚本的维护属于研究工作本身。新研究者应遵守 [AGENTS.md](../AGENTS.md)，使用 [轮次模板](SESSION_TEMPLATE.md)。用户不再负责逐次提醒“这件事以前已做过”。

本次整理属于导航、交接和证据关联审查，未重新认证全部数学证明。新研究的状态按“文稿已给证明／尚未独立审核”明确记录。
