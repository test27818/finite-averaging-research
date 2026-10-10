# 大型数学证明项目的现成经验与适合本项目的 harness

调查日期2026-09-17。实际读取官方项目文档和下面列出的部分实现；没有安装、运行或独立安全审计这些项目。本页是工具选择调查，不是新的平均问题数学结论。

**用户补充后的重要修正：** [Danus](https://github.com/frenzymath/Danus)直接针对非形式化数学的长期多代理研究、事实图记忆与审核准入，比下述多数单项工具更贴近当前协调需求。初轮漏检，不能将此前工具清单当作完整调查。已对其固定提交做针对性源码阅读和两个离线函数检查，详见第8节；未部署代理群或验证其论文案例。

## 1. 最贴近当前阶段：ANTEDB

[Analytic Number Theory Exponent Database](https://github.com/teorth/expdb) 系统记录解析数论中的定理、猜想和可推导关系，同时提供人类可读的Blueprint与可执行Python。它的 `Hypothesis` 对象包含数学数据、证明／引用与依赖；可以递归列出推导来源。贡献指南明确说明：只有一小部分已经Lean形式化，没有Lean代码的部分也可使用Blueprint结构。

这与本项目的“自然语言证明＋精确Python＋外部定理＋未解决接口”相当接近。实际读了README、CONTRIBUTING及 `blueprint/src/python/hypotheses.py` 前155行，确认上述用途，不把Python对象称为形式化证明内核。

适合借鉴：统一符号和前提；将一个可复用结论表示为对象而非一篇孤立文章；已发表输入、猜想和派生结果分开；查询返回依赖链；把尚未接入主证明的内容明确标记为未整合。

目前结论卡可逐步向这种“有类型的命题＋有前提的推导规则”发展，但不要让登记程序自行推断两个自然语言命题等价。比如“已有深核”必须是规则的输入，不能在导航中被省略。

## 2. 大证明蓝图：Lean Blueprint / plasTeX dependency graphs

[Lean Blueprint](https://github.com/PatrickMassot/leanblueprint) 把LaTeX里的定理、定义、证明及 `\uses` 依赖变成可导航的图，并用 `\lean` 链接Lean声明。`\leanok` 是作者标记；`checkdecls` 检查引用的Lean声明是否存在，不能把该检查等同于全部声明不含sorry或依赖已审。

其底层 [plastexdepgraph](https://github.com/PatrickMassot/plastexdepgraph) 本身不要求Lean，能用于普通LaTeX证明的依赖图。Lean Blueprint的默认创建流程则预期已有Lake工程，偏向GitHub及Pages。这意味着不需要为“先看清证明全貌”立刻全项目形式化或发布。

[Tao的PFR Blueprint实践说明](https://terrytao.wordpress.com/2023/11/18/formalizing-the-proof-of-pfr-in-lean4-using-blueprint-a-short-tour/)展示了按节点追踪定义、陈述、证明及前置依赖的做法。[FLT项目](https://github.com/ImperialCollegeLondon/FLT)也把Blueprint作为数学路线入口；README明确称其为进行中的多人形式化项目，不应说已完成全部FLT形式化。

适合借鉴：未来把主证明整理成一份带稳定标签的连续LaTeX正文；区分“陈述已准确”“纸面证明已有”“已独立审查”“已形式化”四个字段。当前 `depends_on` 仍是导航前提，不可直接改名为机器认证的逻辑依赖图。

## 3. 长期数学知识库：Stacks Project

[Stacks的tag制度](https://stacks.math.columbia.edu/tags)为定理、定义和其他数学对象提供永久标识，条目移动或编号变化不改变tag。[About](https://stacks.math.columbia.edu/about)强调在线超链接、可追溯依赖和维护者接纳修改的机制。

适合借鉴：结论ID保持稳定；“相关”“依赖”“加强”“反例”“修正”是不同关系；移动文件不改变结论身份。Stacks主要是数学编辑与引用体系，不是自动证明工具，不能指望tags自行判定重复或正确性。

## 4. 搜索与验证分开：Equational Theories Project

[Equational Theories](https://github.com/teorth/equational_theories)同时整理蕴含、反蕴含、计算搜索和仪表盘。该项目的README明确把Lean已验证断言与尚未Lean验证的人类／机器断言分开，提供从Lean提取已证蕴含的脚本，再生成进度与查询图。

适合借鉴：搜索器给候选，独立核验器检查证书，已验证数据再驱动仪表盘；不从搜索日志直接生成“定理已证”状态。这个模式适合本项目的有限反射表和实际原位置词证书。

限制：它的主要任务是规格清晰的等式蕴含，不是接入任意Markdown长证明的通用解决器。我们的“已给书面证明”不应照搬其“Lean verified”的术语。

## 5. 真正的AI证明执行 harness：Pantograph / LeanDojo-v2

[Pantograph](https://github.com/lenianiva/Pantograph)是Lean 4的机器对机器接口。官方README展示启动目标、运行tactic、查询符号环境、返回JSON状态；可据Lean反馈控制AI证明搜索。

[LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2)提供Lean库追踪、定理与依赖数据、检索、训练及Pantograph上的证明执行。原[LeanDojo仓库](https://github.com/lean-dojo/LeanDojo)当前README明确提示旧库已弃用、新项目用v2；不建议按旧说明直接搭环境。

适合未来的一个小型试点：形式化平均原子、均值守恒、平方能量下降、G必要性，或七元精确宏恒等式。这样AI产出的Lean片段可以被内核检查。逐步扩展时还要检查声明类型是否忠实于原命题、是否含sorry／额外公理。

不适合立即用来替换全部现有研究：需把问题、数据结构与所引定理转换成Lean；Morris／Serre、ESS等接口的形式化可能很重。LeanDojo-v2的训练栈还包含GPU与大型依赖，本轮没有安装，也没有必要只为文档检索引入。

## 6. 对本项目的选择

**当前采用ANTEDB的命题对象与来源思路、Blueprint的依赖和进度分层、Stacks的稳定ID。保留现有轻量登记，修补实际兼容与检索。** 不再另建一套知识管理框架。

本轮已经落实的具体修补：

- 冻结数学材料与明确允许演进的导航分开，保留原散列和原版备份；新检查实际调用旧冻结兼容审查。
- 素数主题顶部按参数范围列启动、收尾与残留证据；视图只引用结论卡内的事实。
- `overview`只保留结论ID，生成器不再硬写某个证书计数；增加真实中文问题路由及回归测试。
- “全参数原位置资源供应”作为主目标；纤维比较、改变来源与状态相关准备并列，退化出口只是候选策略。

再往前最有价值的两步，不需要马上执行全面迁移：第一，将主定理所必需的结论卡细化成准确陈述和证明依赖，逐条人工审核；第二，选一个小接口做Lean试点。只有前提稳定后，证明执行harness才会给出可靠反馈，而不是把翻译错误固化下来。

此次调查没有找到一个经实际验证、可直接替代自然语言大项目全部协调与数学审核的现成万能harness。以上分别解决组织、依赖、证书和形式证明执行的不同层，不能相互冒充。

用户补充Danus后，这个推荐应细化：ANTEDB／Blueprint仍值得借鉴知识结构；Danus则成为实际研究编排的优先试点候选。没有任何一个LLM审核框架因此变成数学正确性的形式保证。

## 7. 来源与实际读取范围

原始网页／README、URL和SHA256保存在[本地来源目录索引](../work/documentation_memory_20260917/harness_sources/source_index.json)。取得的是访问时版本；散列用于精确保存阅读对象，不声称对应某个已锁定Git提交。

| 来源 | 实际读取 |
|---|---|
| leanblueprint | README的启动、编辑宏、checkdecls和项目实例 |
| plastexdepgraph | README选项与最小LaTeX示例 |
| PFR实践文章 | 正文中依赖图、状态颜色及节点展开说明 |
| FLT | README的项目状态、Blueprint入口；未审数学源码 |
| expdb | README、CONTRIBUTING、Hypothesis类的字段和依赖遍历实现 |
| Stacks | About与Tags explained；未审其网站实现 |
| Equational Theories | README的状态语义、数据提取与仪表盘脚本职责 |
| Pantograph | README的JSON REPL、goal/tactic及环境要求；未执行 |
| LeanDojo / v2 | README的弃用提示、架构与环境要求；未安装、训练或跑证明 |

## 8. Danus：最贴近调度痛点，但需要适配我们的证据体系

来源：[frenzymath/Danus](https://github.com/frenzymath/Danus)，本次读取默认`codex`分支固定提交
`6d92e8d415933ca2ef52fd1a4da73fdfcd418f1c`。作者同时保留使用Claude Code主编排的`main`分支；本文只评估所读取的版本，不混用分支。Apache-2.0，pyproject标记0.1.0／Alpha、POSIX Linux。

### 8.1 它直接针对哪些问题

- 本地工作记忆、全局发现／失败路线记忆、经过审核的事实图分层；研究计划不自动成为证明前提。
- 工作代理一次提交一个准确命题与证明；独立新启动的审核代理返回接受／修补意见。
- MCP入口区分编排者、工作者和审核者的可见工具；`fact_submit`返回`correct`后才写入事实图。
- 事实的内容ID绑定陈述、证明、术语及前置ID；撤销事实时递归撤销登记的后继，避免已知错误继续被当作基础。
- 由事实图抽取最终定理的依赖闭包，产生报告／论文，再有整篇文字审核。

这比我们当前的导航登记多出了实际研究循环、审核准入和撤销传播。若目标是减少用户亲自分配注意力、提醒历史成果，Danus明显比单独增加索引更直接。

### 8.2 源码核对出的五个适配点

**1. “verified”是LLM接受，不是形式证明。** 官方`docs/security-and-trust.md`明确说明审核者不是Lean/Coq。`gateway/server.py`以返回的`verdict == "correct"`作为准入，不在代码中重新推导报告中无critical_errors／gaps。新启动能减少对探索过程的依赖，但不保证作者与审核者没有相同数学盲点。本项目仍应保留“文稿证明、独立AI复核、有限证书、形式核验”等不同证据等级，不能把全部输入都升级为同一种数学事实。

**2. 默认审核者不运行计算证书。** `agents/contracts/verifier.md`的Resource safety明确禁止运行Python、符号代数、求解器或证明助手，要求不能重建成完整书面论证的计算依赖记为缺口。这是外部软件角色约定，不是本会话的新指令。对本项目需另接现有独立核验器：提供脚本／输入证书／结果散列和核验范围，再由审核者检查一般归约。不能让LLM文本裁决替代原185项核验和后续补充登记。

**3. 当前纯中文检索会漏失。** `danus/core/bm25.py`的分词正则是`[A-Za-z0-9_]+`；`FactGraph.search`与记忆检索使用它。本地加载该纯函数检查：`偶数部分统一了吗`与`上半带 九偏移`分词都是空列表、BM25分数全0。我们已有中文词表、公式归一化和真实问题回归用例，迁移时必须接入或补齐。该结论仅针对固定提交，未推测所有分支或未来版本。

**4. 内容去重不是数学语义去重。** `compute_fact_id`归一化空白，但包含statement、proof等内容。离线检查同文空白改变ID不变、同义英文陈述改写ID不同。适合同时保留两层身份：本项目稳定的结论ID用于“这是同一研究问题／数学主张”；Danus内容ID用于“这是哪一版陈述和证明”。不能单靠哈希消除换名后的重复研究。其原始`predecessors`也需要从我们的导航关系人工细化成真正证明前提，不能直接把`related`或阶段替代边当逻辑依赖。

**5. 运行边界与旧材料导入需设计。** 项目默认工作／审核代理经shell启动，官方说明绕过沙箱；MCP角色表不等于操作系统隔离。当前运行脚本以Linux/Bash与symlink为主，Windows本机应先在隔离的WSL／副本里试点。外部引用`external_refs`不计入内容哈希，而我们的证明依赖精确外部定理版本与计算文件，因此应额外绑定这些来源／证书的版本。不要把63张导航卡批量灌成其“已验证事实”，也不要把冻结目录交给自动代理自由改写。

### 8.3 建议的最小试点（尚未启动）

先以已有且可复现的一条七元链作导入／审核测试：G必要性、实际返回周期、整数Γ₀(7)轨道及原位置终端。将对应证据与少量旧错误接口一起提供，检查它能否：找回现有结果、拒绝“局部窗口逆就是全局逆”、拒绝“有限模像就是全群”、区分G1存在性和最短词。

验收重点是**是否减少重复和错误准入**，不是产生多少facts。通过后再将范围有限的开放资源命题交给研究循环，并设置明确预算和停止条件。新数据先留在独立试点目录；合并回本项目继续走明确版本和人工／独立复核流程。

这一方案不要求先把项目全部Lean化，也不要求废弃现有登记。若将来需要形式核验，可选局部命题再接Pantograph等；搜索到的`Danus_with_lean_verification`等分叉本轮未审，不因名字就认为原版已有形式验证。

### 8.4 阅读、检查与未验证范围

读取README、ARCHITECTURE、security-and-trust、DATA_MODEL相关字段，及schema、factgraph的写入／搜索／撤销、BM25、gateway准入和角色表、verify服务与launcher、审核合同、pyproject。下载其他合同仅作定位，未声称逐条审计其全部提示词。

仅执行两个无网络、无模型调用的离线函数检查：中文分词／BM25、内容ID。没有安装Danus、没有运行服务或代理群、没有核验README中的研究案例或其“已解决YTD”宣称，不把作者案例报告当作本轮认证。

固定提交与来源清单见[仓库记录](../work/documentation_memory_20260917/harness_sources/danus/repository.json)、[源码来源散列](../work/documentation_memory_20260917/harness_sources/danus/code_sources.json)；[检查脚本](../work/documentation_memory_20260917/inspect_danus.py)与[实际结果](../work/documentation_memory_20260917/harness_sources/danus/focused_checks.json)可复现上述两个具体限制。
