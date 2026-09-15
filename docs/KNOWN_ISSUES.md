# 已知核验问题 / Known verification issues

[中文首页](../README.zh-CN.md) · [English](../README.md) · [核验指南](VERIFICATION.md)

## 二平均零预算状态依赖时钟 / Binary zero-budget status depends on the clock

**2026-09-16首次完整review运行：FAIL。** 原二平均19项Python回归中，test_expired_deadline_is_not_proof要求零预算时status=limit，但一次运行得到status=solved。其余18项Python回归通过。原公开归档中的源代码和测试未改写，也没有通过重跑直到成功来掩盖这次结果。

**The first complete review run failed.** One of the 19 archived binary Python tests expected status=limit for a zero-time budget but received status=solved. The other 18 tests passed. The archived implementation and test are unchanged, and the failed run is retained.

已确定原因：[construct_moves](../archive/2026-09-07/new-chat-3/averaging_benchmark/src/mix_engine.py)使用time.time() > deadline，而solve把deadline_s=0设置为当前时钟值。同一时钟刻度内“严格大于”不成立，构造器可以继续；该实例能给出一条有效路径。时钟前进后则立刻返回limit。

The constructor checks time.time() > deadline. With deadline_s=0, repeated equal clock readings can allow construction to proceed; an advancing clock stops it. This makes the test's status expectation sensitive to clock resolution.

确定性复现不依赖机器快慢：

~~~sh
python -B scripts/check_binary_deadline_behavior.py
~~~

| 时钟模型 / Clock | status | certified | min_steps | 路径 / Path |
|---|---|---|---|---|
| 保持同一刻度 / frozen tick | solved | false | null | 精确验解有效 / exact replay valid |
| 每次前进 / advancing ticks | limit | false | null | 无返回路径 / none |

这说明零时间预算的边界语义不一致；本次未发现“错误路径被接受”或“预算耗尽被当成最短性证明”。诊断的PASS仅表示上述问题被准确复现，**不表示原19项回归全部通过**。

This identifies a zero-budget boundary inconsistency, not an invalid accepted path or false optimality claim in the observed case. A PASS from the diagnostic means the discrepancy was reproduced; it does not make the original regression suite pass.

未来维护可明确约定零预算行为，并在活动代码版本中修正边界比较及加入可控时钟测试；本次只增加读者导航和核验证据，不改写冻结研究。完整review命令可能因这项回归返回非零，日志应保留。具体阈值定理、原位置真逆等数学结论不由这项计时状态测试判定。

A future maintained implementation can specify zero-budget behavior and repair the comparison with controlled-clock tests. This publication update records the issue without rewriting the frozen implementation. The complete review may return nonzero for this reason. Mathematical reachability theorems are not decided by this timing-status test.

## 本次实际结果 / Results actually obtained

- 素数prime-proof：18项注册检查通过；FAIL=0，SKIP=0。
- 三平均小基例：n7-n8-complete与n10-complete通过；主体已在prime-proof中运行。
- 一般偶元数端点与最新统一二进列引理通过。
- 二平均Python：18项通过，1项上述计时状态失败。
- 二平均Node：另行运行6组全部通过。
- 三／p平均基准：另行运行，108条有效路径、1个已知负对照和7项拒绝测试通过。
- 全部1905个归档原文件哈希保持一致。

Prime-profile checks, ternary bases, the general even endpoint and the new dyadic lemma passed. Binary Python had one recorded timing failure; the separately run JavaScript and benchmark checks passed. All archived source hashes remained unchanged.

[首次review报告](../catalog/REPRODUCTION_CHECKS.json) · [首次review完整日志](../catalog/reproduction_review.txt) · [补充诊断与独立检查](../catalog/REPRODUCTION_SUPPLEMENT.json)
