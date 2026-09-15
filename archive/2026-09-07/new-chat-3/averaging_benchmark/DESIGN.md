# Benchmark 设计与当前实现

> 当前默认算法已于 2026-09-07 替换为 projective-ida-v3。变更记录见 `MIGRATION.md`。
> 旧设计全过程保存在替换前的完整备份，不应继续按“只有 n≤6 的 BFS”理解当前能力。

## 1. 三个可自动评分的任务

| task | 提交 JSONL | 判分方式 |
|---|---|---|
| judge | `{"id":"test_000001","answer":"YES"}` | 与 G 判据标签比较 |
| construct | `{"id":"test_000001","steps":[[1,2],[3,4]]}` | 从原输入独立精确模拟，索引 1-based |
| min_steps | `{"id":"small_000001","answer":4}` | 仅在认证的 min_steps 非 null 时比较 |

Task 4/5 为证明/开放推广，仍需人工评审。不把模型声称“最优”当作机器认证。

## 2. 真值可信性

- 判定来自已知充要条件；n=3、全等、约去 gcd 的边界独立测试。
- 冻结旧数据与新数据分开：`tests/fixtures/original_small.jsonl` 保存原 78 个最优真值。
- `legacy_bfs.py` 保留精确分数搜索作为不同表示的交叉检查，不与新引擎共享剪枝。
- 新最优真值必须由完整有界搜索或已证明下界与已验证上界相等获得。
- 每条序列由 `solver.verify_sequence()` 验证；浏览器另用独立 BigInt 分数验证器。
- 不把截止时限、状态预算、搜索失败解释为不可平均或最优性证明。
- 旧 κ/深度下界保留研究接口，但不用于当前默认认证。

## 3. 数据

固定随机种子 `20260907`；原始 1636 个输入、ID、YES/NO、标签不变。

| split | 总数 | YES | 认证 min | 已验证 sequence |
|---|---:|---:|---:|---:|
| small | 224 | 98 | 92 | 98 |
| dev | 304 | 119 | 109 | 119 |
| test | 704 | 230 | 185 | 230 |
| hard | 404 | 91 | 42 | 91 |

记录保留 `label/min_steps/sequence/traits/tier`，新增认证记录含
`certified/lb/ub/min_steps_source`。`min_steps` 与 `certified` 不混用：有序列只证明上界。

`manifest.json` 含行数、SHA-256、标签分布、升级预算与统计。`upgrade_data.py` 默认输出
新目录，只有明确 `--in-place` 才备份后替换。已知最小值、最短证书不因新一次超时而降级。

## 4. 指标与解释

判定需要同时看 accuracy、balanced accuracy、YES precision/recall/F1、per-tier/per-trait。
因为 test 中 NO 为 474/704，always_NO 也有 67.33% accuracy，不能只看准确率。

构造需要报告验证成功率、步数和与已认证最优值的比值。最小步数需要报告 exact-match、
误差和覆盖率。使用 `evaluate.py` 的报告时注意评分分母：未提交/无法解析的预测与成功
预测不能混成“全数据集已完成”。当前算法基线输出全部 ID，并保留 limit 状态。

`baselines/trivial.py` 保留 trivial/oracle 作诊断锚点；`baselines/current.py` 只把 `a/id`
传给新算法，不读取 label/min_steps/sequence 当答案。oracle 100% 不说明一个 AI 模型能做到。

## 5. 网页和 Python 不共用浮点值

- 网页：BigInt 投影整数求解，独立约分分数验解，浮点仅用于耗时/显示坐标。
- Python：int 求解，Fraction 验解；所有外部操作都是原始位置上的 1 基索引对。
- 浏览器随机生成使用 crypto 拒绝采样，仅按可平均判据筛选，未附带逆推答案。
- 导出转换：`src/import_web.py` 接收浏览器 JSON，按原输入顺序匹配 ID 并重新验解。

## 6. 可复现命令

```bash
python3 -m unittest discover -s tests -v
node tests/test_web.js
python3 src/build_web.py --check
python3 src/generate.py --selfcheck
python3 src/eval_all.py
python3 baselines/current.py data/test.jsonl results/current_test.jsonl --task construct
python3 src/evaluate.py --ground data --split test --preds results/current_test.jsonl --task construct
```

重建题面建议写到 `data_generated`，不要覆盖已经升级的 `data`。硬件/墙钟预算会影响
认证覆盖，不承诺重新计时产生逐字节相同的升级数据；本次发行由 manifest 固定。

## 7. 尚待完成

通用 Invariant-(I) 构造、困难实例的更强已证明下界、开放题自动诚实性评分仍未完成。
随机题面能减轻逐题记忆，但不能排除对已知判据的训练污染，也不能仅凭检索难度
判断模型是在独立发现定理。
