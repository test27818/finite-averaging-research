# 复现与正确性核验 / Reproduction and verification

[中文首页](../README.zh-CN.md) · [English](../README.md) · [证明路线 / Proof guide](PROOF_GUIDE.md)

## 三种不同的检查 / Three different checks

| 检查 / Check | 能说明 / Establishes | 不能说明 / Does not establish |
|---|---|---|
| 哈希与路径 / Hashes and paths | 归档文件完整，新增导航可达 / bytes intact and navigation targets present | 数学命题正确 / mathematical truth |
| 精确代码核验 / Exact computational checks | 指定恒等式、有限证书、原位置序列和回归按声明通过 / the declared identities, finite certificates and paths pass | 任意未检查参数、外部定理或完整无限量词 / untested parameters or external theorems |
| 阅读证明及依赖 / Proof and dependency review | 逻辑量词、容量、真逆、单位尺度、归纳和引用前提 / hypotheses and general logical implications | 不自动等于形式化认证 / not automatically proof-assistant certification |

只有“程序退出码为0”不够：原注册还列出expected markers。运行器可能把缺少命令记为SKIP，所以本仓库新复现入口要求所有选中任务通过且SKIP=0。

Exit code zero is insufficient: registered checks also specify expected output markers. The new reproduction entry rejects missing tools and skipped checks, even when an older runner would otherwise return zero.

## 推荐的一条命令 / Recommended command

**当前实测：** 首次review的数学检查通过，但二平均有1项零预算状态测试失败；完整日志保留。详见[已知问题及确定性诊断](KNOWN_ISSUES.md)。不要把本页的复现命令当作保证全绿的声明。

**Observed result:** the first review passed the selected mathematical checks but failed one binary zero-budget status regression. The log is retained; see the [known issue and deterministic diagnostic](KNOWN_ISSUES.md). These commands reproduce evidence, not a promise of an all-green result.

从仓库根目录，使用Python 3.11+，并安装Node.js以运行二平均JavaScript回归：

From the repository root, use Python 3.11+ and Node.js for the binary JavaScript regressions:

~~~sh
python -B scripts/check_archive.py
python -B scripts/build_check_index.py --check
python -B scripts/reproduce.py --suite review
~~~

review把archive复制到临时目录，在副本中依次运行下表任务；结束后核对原归档哈希。日志和JSON报告默认写入被Git忽略的verification_runs/，临时副本自动清理。耗时依机器而变，脚本不运行全部历史搜索。

The review suite copies the archive into a temporary directory, runs the checks there, then rechecks the original hashes. Logs and JSON reports go to the Git-ignored verification_runs/ directory; the temporary copy is removed. Runtime depends on the machine. This does not execute every historical search.

| 套件 / Suite | 内容 / Included checks |
|---|---|
| prime | 原prime-proof的18项注册检查 / the 18 registered prime-profile checks |
| ternary | n7-n8-complete、n10-complete、all-dimensions-double-triple-invariant |
| dyadic | 最新二进列统一引理的恒等式、构造与原证明接口 / new uniform dyadic column lemma |
| general | even-arity-all-endpoints，检查一般偶元数端点接口 / even-arity endpoint interfaces |
| binary | 19项Python回归及6组Node回归 / Python and JavaScript regressions |
| benchmark | 三／p平均参考路径、自检与非法证书拒绝 / reference paths and rejection checks |
| review | 上述全部；已在prime内的三平均主体不重复运行 / all of the above, without repeating the ternary main check |

例如只看最新改进： / For the latest improvement alone:

~~~sh
python -B scripts/reproduce.py --suite dyadic
~~~

一般k的套件只是一个代表性的已证接口，没有覆盖所有GRH结果或全部合数定理。可从[全部185项索引](../catalog/CHECKS.md)选择其他检查。

The general suite is a representative proved interface, not all GRH or composite-arity results. Select further checks from the [185-entry catalog](../catalog/CHECKS.md).

## 手动核验一个命题 / Inspect one claim manually

在[命题—检查索引](../catalog/CHECKS.md)中找到ID，读documents、evidence scope、does not establish、dependencies，再查看脚本和证书。索引自动读取冻结的注册，不按文件名猜测结论。

Find the ID in the catalog, then read the documents, evidence scope, exclusions and dependencies before inspecting its scripts and certificate. The index is generated from the frozen registry.

例如九偏移浅层提升：

~~~sh
cd archive/2026-09-07/3-3-triple-average-research-note
python -B work/run_verifications.py --id transverse-root-shallow-lifting
~~~

该项包含精确切向恒等式、162组小参数证书和统一公式实例检查；$`p\ge83`$的无限范围仍由容量公式正文承担，Morris／Serre由明确引用承担。

This check covers exact tangent identities, the 162-case certificate and formula instances. The unbounded range follows from the written capacity proof; the external group-theoretic input remains a cited theorem.

直接运行历史核验可能重写其JSON结果；若希望保持原始快照，用上面的临时副本入口。不能用python -O或其他禁用assert的方式运行数学核验。

Direct historical runs may rewrite their result JSON. Use the temporary-copy entry to preserve the snapshot. Do not disable Python assertions with -O.

## 文件及证据定位 / Locating evidence

- [FILES.json](../catalog/FILES.json)：1905个归档文件、来源、字节数和SHA-256 / all archived source files.
- [CHECKS.md](../catalog/CHECKS.md)：185个注册条目的正文、脚本、范围和排除声明 / claim-to-evidence map.
- [proof_map.json](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/proof_map.json)：主证明依赖导航图，不是自动提取的形式化证明 / navigation dependency graph, not a formal proof object.
- [外部定理审核](../archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md)：引用名称、前提和原文访问边界 / external assumptions and source access.
- [首次发布检查](../catalog/PUBLICATION_CHECKS.json)：归档与二平均回归 / original publication checks.
- [本次复现记录](../catalog/REPRODUCTION_CHECKS.json) · [完整日志](../catalog/reproduction_review.txt)：本次实际执行的范围 / results actually run for these guides.

## 目录清晰程度的边界 / Navigation limitations

主题入口、双语指南、全部文件索引和生成的检查索引均作路径检查；归档内旧文逐字节保留，其中部分绝对路径、旧迁移链接和历史状态仍需结合当前入口理解。详见[来源与移植](../PROVENANCE.md)。不能据新增导航检查宣称1905个历史文件中的每条链接都已修复。

The new navigation is checked. Archived documents remain byte-identical, including some historical absolute paths, migrated links and outdated status statements. The new checks do not claim to repair every link inside all 1,905 historical files.
