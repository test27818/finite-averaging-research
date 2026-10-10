# 计算材料与核验入口

这里保留全部原核验器、证书、搜索脚本和历史缓存。文件名 `verify_` 本身不决定数学证据强度；请按结论检索。

```text
python knowledge/project_knowledge.py verify TRIPLE-ALL
python knowledge/project_knowledge.py verify PRIME-ODD-PENCIL
python knowledge/project_knowledge.py verify FIVE-TEMPLATE-ESCAPE
```

这些命令只展示对应脚本、记录与证明边界，不启动计算。新的独立研究脚本在 `research/prime_arity_padic/`，现在同样可以从这个入口找到。

原完成项目的执行器和185项登记保持原样：

```text
python work/run_verifications.py --list
python work/run_verifications.py --id seven-endpoint-structure
python work/run_verifications.py --profile prime-proof
```

`prime-proof` 仍对应原冻结证明版本，不假装已经执行后续所有独立简化。[原注册](verification_manifest.json)记录每项检查的 `evidence_scope` 和 `does_not_establish`；[统一核验说明](../knowledge/VERIFICATION.md)解释两套登记如何衔接。

搜索器的阴性输出不证明不可达，有限样本不承担无穷量词，JSON结果的存在也不等于本轮已重跑。接手先读[当前数学状态](../knowledge/STATUS.md)，不要据旧文的阶段性“未解”重开已完成任务。

旧版长核验日志完整保存在[原导航快照](documentation_memory_20260917/originals/work/README.md)，用于溯源和恢复；具体脚本和证书没有移动。源码与正文的当前关联见[文档清单](../knowledge/DOCUMENTS.md)。
