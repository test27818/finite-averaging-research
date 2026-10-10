# 有限步平均研究

更新：2026-09-15。当前工作是**整理和改进素数平均证明**；合数研究保留原进展，本轮暂停推进。

对奇素数 p，最优最终阈值已证明为 N(p)=2p+1；二平均 N(2)=4。n 在阈值以上时，非全等有理输入经原位置 p 平均可达全等，当且仅当中心化、本原化后的差分 gcd 是 p 的幂。只有 p 不整除 n 时才能简写成 G=1。

## 从这里开始

| 需要 | 入口 |
|---|---|
| 新 AI 接手／理解当前定理 | [素数证明入口](outputs/prime_arity/README.md) |
| 完整证明链与各维数覆盖 | [总证明](outputs/prime_arity/proof.md) |
| 统一代数工具与真正的几何结构 | [通用引理](outputs/prime_arity/arithmetic_toolkit.md) · [模曲线与标记格](outputs/prime_arity/geometry.md) |
| 阅读记录、证明证据、独立审核 | [本轮核验说明](outputs/prime_arity/verification.md) |
| 合数的现有成果与 GRH 条件 | [合数交接](outputs/general_k_three_tasks_progress_20260915.md) |
| 三平均直接证明、算法和其他主题 | [成果索引](outputs/README.md) |
| 查询曾试过什么 | [历史路线账本](outputs/research_routes_history_20260915.md) · [原根进展日志](HISTORY.md) |

素数证明无条件，但引用已审核的 Morris/Serre 定理，且九偏移部分含完整有限参数证书。尚未证明可变 p、n 下的统一多项式操作长度，也未解决一般合数元数的最优最终阈值。旧历史文稿的“未解”不覆盖当前已完成结论。

## 核验入口

在项目根目录执行：

```text
python work/run_verifications.py --profile prime-proof
```

这是素数主线的选定核验集，包含最终独立证书检查；PASS 的证明范围以[注册清单](work/verification_manifest.json)为准，不能代替正文的一般量词或外部定理。其他脚本见 [work 索引](work/README.md)。

## 文档维护

当前定理和阅读顺序集中维护，技术附录保留原位置不改名；历史过程归档，不再向两个 README 逐条追加进展。新结果必须区分“完整定理／有限证书／公式核验／探索”，并更新相关依赖与证据边界。
