# 2026-09-07：以新算法替换原默认实现

## 1. 来源与备份

来源：上传的 `2-average-solver.html`，SHA-256：
`d71cca94ee272e06b829e4974b8a2f980f49593ae467532418238c6d0d51b76a`。
未修改 `/upload` 中的原文件。

- 完整替换前快照：`/workspace/averaging_migration_20260907/before.tar.gz`。
- 上传原件副本：`/workspace/averaging_migration_20260907/original-upload.html`。
- 目录内更早算法备份：`legacy_20260907/`（保留，不作为当前运行入口）。
- 数据升级前备份：`data_backup_20260907_122136/`。
- 用于独立回归的冻结原始小集：`tests/fixtures/original_small.jsonl`。

接手时目录中还存在一份未完成的 `mix_engine.py` / `solver_v2.py` 迁移稿；已纳入快照。
它包含未统一的 value-pair/position-pair API、重复加时间戳的 deadline 计算、前置指数分块
以及无依据的 n≤14 覆盖率宣称。最终默认入口已重写，未把这些中间状态当作成品。

## 2. 实际替换了什么

| 入口 | 原默认行为 | 当前行为 |
|---|---|---|
| `solver.html` | 旧版演示网页 | 上传工作台的离线 UI + 经回归的资源控制改动 |
| `src/solver_core.js` | Fraction-like BFS + 随机贪心 | 由 `web_*.js` 构建的新核心，保留原 Node exports |
| `solver.min_steps_sequence()` | 带分母截断的 BFS | 无分母截断的 IDA*；旧参数仍可传入 |
| `solver_v2.solve()` | A*/分块/旧决策搜索混合 | 先构造，再按剩余预算 IDA*；显式上下界和状态 |
| `construct.construct()` | 先跑精确搜索和指数分块 | 相反数/四元块/蝶形/下降/逃逸，默认先拿可行证书 |
| `prove_no.decision()` | 旧计数界、弱分支顺序 | 更强计数界、排序分支、有限失败表，保留旧 tuple API |
| `lower.lower_bound()` | κ 深度过程与指数分块 | 已证明的相反数计数界与可选连通分块界 |
| `upgrade_data.py` | 可能丢失已有认证标记、再次构造耗时 | 一次 solve，保留既有真值，完整校验后落盘和更新 manifest |

保留 `legacy_bfs.py` 供独立 Fraction 交叉验证。保留 `solver_v2.astar()` 作为可选路径，
其输出仍是 **1 基位置索引**，而不是内部的偏差值对。旧实验 SAT 脚本未删除。

## 3. 搜索和构造的实现要点

### 状态

偏差 `x_i = n*a_i - sum(a)`，整体约去 gcd、排序。一步操作等价于：

```
选中两项 -> x+y
未选中项 -> 原值×2
整体约去 gcd，再排序
```

搜索使用的是去除整体尺度的整数表示，目标全 0。分母不需要截断，但整数位长仍可能
随深度增长，不能宣称“被初始输入位长界住”。全等分支避免 gcd=0 除零。

构造使用实际符号；失败状态表可以合并整体变号对称。值对路径最后重新映射到原题
固定索引，并以独立分数运算验证。逃逸搜索和可选 A* 使用不可变父节点，防止替换
状态表记录时破坏路径的符号、父链或位置映射。

### 新下界（默认认证依赖的证明）

令 `m` 为非零项数，`c` 为可组成的不相交相反数对数，`C=ceil(m/2)`。
若一个解有 `q` 次非零相反数抵消和 `t` 次其他有效操作，则：

1. 每次抵消最多减少两个非零项，其他操作不会减少非零项，所以 `q>=C`。
2. 一次抵消使相反数对数恰减 1；其他操作最多增加两对。
3. 最后对数为 0，故 `q<=c+2t`，于是
   `q+t >= C + max(0, ceil((C-c)/2))`。

这个论证包含“把已有零重新变成非零”的操作，未排除它们。它也支配旧的
`nonzero/2`、`no-opposite-pair setup` 和 `distinct magnitudes/2` 界。

旧 κ/深度过程实现移至 `research_lower.py`，**不进入当前默认最优性证书**。
尤其其按每个位置自己的目标深度做饱和、忽略已有达标位置后续作为深链来源等行为，
需要单独证明/审查。有限样本无反例不是可采纳性的充分证据。

### 资源与状态

- DFS 表有内存条目上限，节点预算在 IDA* 各轮之间累计，不会每轮重新获得完整预算。
- 每 128 个实际搜索节点检查软时限；原子运算/一次后继生成可能超出软限。
- `proved` 只来自完整穷尽；`time/cap/depth` 都是未完成。
- 如果已验证上界等于已证下界，不需要再搜索上界那一层。
- Python 默认只在 n≤14 运行 IDA*（可配置），网页默认 n≤12；这只是资源策略。
  **n 超过门槛仍可因 LB=UB 直接认证最优**，例如 `[0,...,13]` 的 7 步。
- 限制为 19,000 步的网页构造不会因一次蝶形收尾而越过上限。
- 不隐藏内部断言失败。正常预算失败与程序错误分别处理；原网页中蝶形不变量的
  `throw` 并不是一个已证实的算法 bug，没有因为此前审阅的猜测而删除检查。

默认构造在文献通用 Invariant-(I) 算法之外仍属启发式。538/538 是本数据集覆盖率，
不意味着对每个可平均输入必定在资源预算内成功。

## 4. 数据升级结果

输入、ID、顺序、tier、traits、YES/NO 标签均保持不变。
每题预算：2 秒 / 1,000,000 节点；完整批次先校验后替换。

| split | total | YES | 原 min / 新 min | 原 sequence / 新 sequence |
|---|---:|---:|---:|---:|
| small | 224 | 98 | 78 / 92 | 98 / 98 |
| dev | 304 | 119 | 0 / 109 | 0 / 119 |
| test | 704 | 230 | 0 / 185 | 0 / 230 |
| hard | 404 | 91 | 0 / 42 | 0 / 91 |
| 总计 | 1636 | 538 | **78 / 428** | **98 / 538** |

仍有 110 个 YES 实例只有已验证上界，`min_steps=null, certified=false`，没有冒称最优。
新的认证题实测最大 n=12，不能据此声称所有 n≤12 或 n≤14 的问题均能快速认证。

`data/manifest.json` 固定本版本内容的 SHA-256、原始随机种子和本次预算统计。
随机种子可复现题面；时间预算内是否拿到证书可能随硬件改变，所以“重新跑同样
墙钟预算必然得到逐字节相同的升级结果”不是本项目的承诺。

## 5. 实测记录

权威结果文件：`results/migration_report.json`。该轮记录：

- 78 个冻结原始最优真值：全部一致；独立旧 BFS 0.105 s，新引擎 0.0065 s。
- 260 个此前保存的随机认证真值：全部一致，约 2.55 s；这批经过可认证筛选，
  **不是无偏的随机性能评估**。
- 538/538 个 YES 实例构造成功并独立验解；1636 个标签 Python/JS 一致。
- 案例 1：min=10，0.049 s；案例 2：min=11，0.643 s。
- Python 回归包括超时/节点/内存/深度中断不得输出证明、0 步、重复值、仿射变换、
  原序号映射、单例和 256 位大整数、无分母截断的独立小 BFS。
- Node 回归使用 HTML 同源脚本；另有真实 Chromium 测试求解、回放、JSON 下载、
  导入验解、内置 16 测试、批量与手机视口。没有页面 JS 错误或外部网络请求。

旧日志中的 n=10 用时约 6/52 秒仅作为历史对照；不是同一轮严控实验。
新版展开节点只统计启发式剪枝后进入搜索的节点，**不能直接与旧日志的出队数或
JS 的所有 DFS 调用数比较成节点减少倍数**。

## 6. 复现与维护

```bash
python3 -m unittest discover -s tests -v
node tests/test_web.js
python3 src/build_web.py --check
python3 src/eval_all.py

# 本工作区已安装 Playwright；不是产品依赖
NODE_PATH=/workspace/browser-lab/node_modules node tests/browser_smoke.js
```

网页维护源是 `src/web_solver.js`、`web_verifier.js`、`web_runner.js`、`web_main.js`，
兼容桥是 `web_compat.js`。运行 `python3 src/build_web.py` 同步 HTML 和 Node bundle。

网页导出与 benchmark 保持各自 schema，提供显式转换：

```bash
python3 src/import_web.py exported.json --ground data/test.jsonl --out results/imported.jsonl
python3 src/evaluate.py --ground data --split test --preds results/imported.jsonl --task construct
```

转换只按原题固定顺序匹配，重新验解；**不信任网页 JSON 中自行写的 optimal 字段**。
TXT 仍可在网页内导入验证；Python 转换器目前只接收单条/批量 JSON。

## 7. 这次没有宣称解决的事

- 最少步数一般复杂度、任意输入的高效通用构造，仍未解决。
- “无零和子集 ⇒ 唯一零和有理关系”不成立，不能按旧文档猜想直接给蝴蝶最优性打标签。
- 未重新检索所有文献，因此旧 `open_problems.md` 的世界范围开放状态不作为此次验证结果。
- 没有把工作区所有未提交内容提交进 git；仅修改本 benchmark，其他项目保持不动。
