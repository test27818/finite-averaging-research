# 核验：从结论定位脚本，不从文件名前缀猜结论

有两套互补登记：原完成项目的 [185项核验清单](../work/verification_manifest.json)，以及 [catalog.json](catalog.json) 中独立研究的 `local_checks`。两者由同一查询入口联接，原清单和证书内容不因本次整理而改写。

```text
python knowledge/project_knowledge.py verify TRIPLE-ALL
python knowledge/project_knowledge.py verify FIVE-TEMPLATE-ESCAPE
python knowledge/project_knowledge.py verify PRIME-FINITE-TERMINAL
```

查询会列出命令、数据记录、证据等级与不覆盖范围；**不自动运行**。先读范围，再执行所需命令。不需要为了接手一条小支线重跑全项目长搜索。

## 原完成项目

```text
python work/run_verifications.py --list
python work/run_verifications.py --id all-dimensions-double-triple-invariant
python work/run_verifications.py --id seven-endpoint-structure
python work/run_verifications.py --profile prime-proof
```

旧运行器的输出标记只证实相应检查成功。`theorem-certificate` 只承担正文明确归约后的有限子问题；`symbolic-check` 和 `finite-sanity` 不能证明无穷量词。`exploratory-search` 失败不能当不存在证明。

## 后续独立研究

结论卡直接关联文稿、实际核验器和JSON记录。无独立脚本的综述／书面推导明确标记，不伪装成漏登的PASS。一个脚本可能核对多个结论，也可能读旧证书，须检查卡中范围和原文。

例如固定模板逃逸的正式证明依赖ESS及谱引理；脚本只检查公式与有限样本。`--return-depth 18` 的524286个词诊断与一般定理分开，不构成“只搜索到18便证明逃逸”。

## 文档与知识登记检查

```text
python knowledge/project_knowledge.py check
```

检查ID唯一性、文件与脚本存在性、关联ID、导航前提循环、来源散列变化、独立研究是否遗漏、生成页是否过期和新知识库链接。**它不会审查证明是否正确。**

现在还实际调用旧冻结兼容审查。原[256项冻结快照](../research/prime_arity_padic/existing_documents_snapshot.json)及其散列保留；[导航迁移登记](navigation_migrations.json)只允许六份明确README演进，逐项要求旧备份与原散列相符、当前版本与迁移登记相符。其余250项必须原样。不能把证明文件加入例外名单，也不能覆盖原散列消除失败。

旧调用者的 `check_frozen_files()` 仍返回核查条目总数；部分历史输出字段名含 `unchanged`，现在应按上述兼容政策解释为“冻结材料与已登记导航迁移均通过”，不代表六份当前README字节未变。新统一检查会分别报告两类数量。

有意修改来源后，先读相应结论卡并更新范围／边界，再执行：

```text
python knowledge/project_knowledge.py accept-sources FIVE-TEMPLATE-ESCAPE
python knowledge/project_knowledge.py build
python knowledge/project_knowledge.py check
```

`accept-sources` 只是记录维护者已处理的版本，不会认证新数学结果。不要为了消除警告批量确认未阅读的变更。

## 新结果的最低登记要求

固定ID、精确量词、条件（尤其GRH）、证明状态、已知边界、相关前置结果、替代的具体范围、原文路径。涉及程序结论时再加命令、输入／证书文件、结果文件、实际核验承担什么。外部定理加来源版本与实际读过的章节。

有限检查可以复用，不必给纯导航更改重跑数学程序。本次整理的自动核查与检索试验记录在 [整理报告](ORGANIZATION_AUDIT_20260917.md)。
