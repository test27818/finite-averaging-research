# Averaging-to-Equalize Benchmark

给定 n 个整数（数学问题可推广到有理数），每次选两项 x,y，**都**替换为 (x+y)/2。
目标是有限步精确全等，不是数值上逐渐接近均值。

## 当前版本：projective-ida-v3（2026-09-07）

已将上传的 `2-average-solver.html` 的算法迁入 Python 默认入口，并替换旧网页。
**不是只增加了一个新文件：原来的 solve / construct / min_steps_sequence / decision
入口都已接上新引擎。** 详细迁移记录、范围和已知局限见 [MIGRATION.md](MIGRATION.md)。

- **判定**：原来的归一化 G 判据不变；n=3 单独处理，全等直接 0 步。
- **构造**：相反数抵消 → 零和四元组 → 多策略蝶形收尾 → 保持可平均性的整数势能下降 → 有界逃逸搜索。
- **最短性**：相反数对计数下界 + IDA* 逐层搜索 + 有上限的失败状态表。
- **正确性**：无分母截断；所有返回的操作序列经独立 Fraction/BigInt 分数验解。
- **预算**：超时、节点/内存/深度耗尽不等于不可平均，也不等于已证明最优。
- **网页**：单文件离线 HTML，Worker 求解、随机拒绝采样、批量统计、回放、TXT/JSON 导出与独立验解。

### 当前数据（已落盘，不是待办）

| 分片 | 总题数 | 可平均 | 有认证最少步数 | 有已验证序列 |
|---|---:|---:|---:|---:|
| small | 224 | 98 | 92 | 98 |
| dev | 304 | 119 | 109 | 119 |
| test | 704 | 230 | 185 | 230 |
| hard | 404 | 91 | 42 | 91 |
| **合计** | **1636** | **538** | **428** | **538** |

升级前只有 78 条最少步数真值，98 条序列；现在分别为 428 / 538。
全部 ID、题面、YES/NO 标签保持不变，旧真值没有被降级，`data/manifest.json` 已更新 SHA-256。
本次批处理使用每题 2 秒、1,000,000 搜索节点的预算；覆盖率不是对任意实例的保证。

### 已实测回归

- 原版 78 条最少步数：78/78；冻结的另 260 条认证实例：260/260。
- 所有 1636 个判定标签一致；538/538 可平均实例构造成功并独立验解通过。
- 两个 n=10 案例仍为 min=10、min=11；本次报告用时约 **0.049 s / 0.643 s**。
- Python 19 项回归、Node 6 组回归及真实 Chromium 浏览器冒烟测试通过。
- 数字和计时见 `results/migration_report.json`；性能随环境变化，不能把这些样本外推为普遍可解规模。

## 运行

```bash
cd /workspace/averaging_benchmark

# 原接口：返回认证最小步数，或保留上下界/已验证序列
python3 src/solver_v2.py '[0,0,0,1,9]'
python3 src/construct.py '[38,-23,-14,16,-11,4,63,80,14,38]'
python3 src/prove_no.py --batch

# 回归与计时；不重写数据
python3 -m unittest discover -s tests -v
node tests/test_web.js
python3 src/build_web.py --check
python3 src/generate.py --selfcheck
python3 src/eval_all.py

# 不使用 ground-truth 答案的当前算法基线
python3 baselines/current.py data/test.jsonl results/current_test.jsonl --task construct
python3 src/evaluate.py --ground data --split test --preds results/current_test.jsonl --task construct

# 输出另一份升级数据；只有显式 --in-place 才覆盖 data（会先备份）
python3 src/upgrade_data.py --deadline 2 --out data_upgraded

# 从种子重建题面到独立目录，再升级；不要用生成器覆盖现有已认证真值
python3 src/generate.py --seed 20260907 --outdir data_generated
python3 src/upgrade_data.py --ground data_generated --out data_rebuilt
```

直接打开 `solver.html` 即可使用网页。编辑 `src/web_*.js` 后运行
`python3 src/build_web.py`，同步更新 HTML 内嵌脚本与 Node 的 `src/solver_core.js`。
HTML 保持零依赖；Playwright 仅用于可选浏览器测试，不是运行依赖。

## Python 接口

```python
from solver_v2 import solve
r = solve([0, 0, 0, 1, 9], deadline_s=2)
# r['sequence']: 原题固定位置上的 1 基索引对
# r['min_steps']: 只有 certified=True 时才非 null
# r['lb'], r['ub']: 已证明下界、已验证上界
# r['status']: solved / impossible / limit
```

`construct.construct()` 保留 `steps / verified / n_steps` 接口；默认只构造，不先消耗预算求最优。
`solver.min_steps_sequence()` 已由默认 BFS 改为 IDA*，返回格式仍为 `(minimum, sequence)`。
`solver_v2.astar()` 仍保留旧的**位置索引序列**格式；没有误改成内部偏差值对。

## 文件导航

| 文件 | 当前用途 |
|---|---|
| `src/mix_engine.py` | 共享整数状态、构造、下界、有界 DFS / IDA*、可选束搜索 |
| `src/solver.py` | 判定、独立验解、兼容的 min_steps_sequence |
| `src/solver_v2.py` | 当前求解入口，兼容原结果 schema |
| `src/construct.py` / `src/prove_no.py` | 原构造/决策接口的新版实现 |
| `src/lower.py` | 当前可信计数界 + 可选连通分块界 |
| `src/research_lower.py` | 旧 κ/深度下界，研究用途，不进入默认最优性认证 |
| `src/legacy_bfs.py` | 保留的独立 Fraction BFS，小规模交叉验证用途 |
| `src/web_*.js` / `src/build_web.py` | 网页维护源码、构建与同步检查 |
| `src/solver_core.js` / `solver.html` | 生成的 Node 兼容核心 / 单文件网页 |
| `src/upgrade_data.py` / `src/import_web.py` | 数据真值升级 / 网页 JSON → 评测序列转换 |
| `tests/` / `results/migration_*` | 冻结的旧真值、回归测试与实测记录 |
| `problem.md` / `literature.md` | 数学规格与参考文献（并非此次重新文献检索） |
| `MIGRATION.md` / `DESIGN.md` | 当前版本说明与评测设计 |
| `IMPROVEMENTS.md` / `case_study.md` | 历史研究过程；旧性能和旧默认入口不再代表当前实现 |

## 理论与限制

主判据来自 Coviello Gonzalez & Chrobak, *Towards a theory of mixing graphs:
A characterization of perfect mixability*, arXiv:1806.08875，TCS 845 (2020) 98–121。
$n\ge4$ 时，均值归零、约去公因子后，两两差的 gcd 为 2 的幂等价于可平均。

最少步数的一般复杂度未由本项目解决。此版本也**没有实现文献的完整 Invariant-(I)
多项式构造**，而是大幅提高了实用构造覆盖率；测试全通过不构成通用终止性证明。
投影整数的位长仍可能随搜索深度增长，商掉缩放不等于状态空间有限。
