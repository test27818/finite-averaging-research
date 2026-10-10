# 本次整理的阅读、修改与核验范围

2026-09-15。本页区分本次直接阅读、沿用审核、实际重跑及未核对内容；不把文档重组称为独立重证全部数学。

## 1. 实际阅读的项目文本

以下是正文阅读，不只是文件名检索；“相关节”不表示通读整篇。

| 文档 | 本次读取范围／用途 |
|---|---|
| [最终独立审核](../prime_arity_optimal_threshold_independent_audit_20260915.md) | 全文；量词、99组额外扩环、两项特殊补充、下界、证书及审核边界 |
| [下半带外部定理审核](../prime_arity_lower_band_external_theorems_audit_20260915.md) | 主结论及§§2—5；Morris/Serre前提、任意有限环消元 |
| [3p+10审核](../prime_arity_three_p_plus_ten_audit_20260915.md) | 上端与尾部拼接、外部依赖和证据说明 |
| [九偏移共同证明](../prime_arity_nine_offsets_large_symmetric_carrier_completion.md) | 入口、四原子反射、§§4—9；容量、换基、扩环、局部方向和尺度 |
| [内部偶余量](../prime_arity_even_interior_completion.md) | §§1—6；取逆、有限循环、纤维接口及分支范围 |
| [2p+2统一证明](../prime_arity_two_p_plus_two_uniform.md) | §§1—4；统一返回、CRT与精确终端 |
| [中间维数结构](../prime_arity_middle_band_structure.md) | §§1—4；3p的三块运输与固定level |
| [逆EGZ](../prime_arity_inverse_egz_threshold.md)及[4p尾部](../prime_arity_four_p_tail_completion.md) | 各§§1—4；旧不等式与已补齐范围 |
| [全部3p+10以上](../prime_arity_all_prime_three_p_plus_ten.md) | §§8—10及相关接口；小p收口、旧九偏移状态定位 |
| [插值与均值格](../prime_arity_interpolation_and_lattice_structure.md) | §§1—3、6—7；造零、禁止免费插值、整数格指数 |
| [旧端点几何](../prime_power_endpoint_and_critical_geometry.md) | §§5—6，并回查相关两图／Schreier段；范数、theta与外部尺度障碍 |
| [Hecke最终审核](../triple_average_final_hecke_audit.md) | §§1—8；分支求和、正向实现和符号边界 |
| [无条件入口](../prime_arity_unrestricted_endpoint_and_odd_band.md) | 定理、依赖和§2块—单点交换；其余入口细节此次依照专项审核，未逐式重证 |
| [线性阈值](../prime_arity_linear_threshold.md) | 不变量与能量结论、§§8—9的2p反例和最低p进赋值论证 |
| [三平均任意维数](../triple_average_all_dimensions_double_triple_invariant.md) | 定理、适用范围与不变量；7—10基例的完整证明未在本次重跑 |
| [二平均与三平均比较](../binary_vs_ternary_averaging_followup.md) | 结论与共同算术层；2018原证明的完整源文审核沿用既有记录 |
| [合数交接](../general_k_three_tasks_progress_20260915.md) | 当前结果、GRH条件、三项剩余范围，用于保持导航正确；不推进合数证明 |

另直接读取两个原 README 的导航、结论表及历史组织，查看全项目核验注册的相关条目与运行器，并读取最终独立审核脚本及固定证书接口。[此前阅读日志](../research_reading_log_20260915.md)记录其他回合，不能混称本次全部新读。

3p−1、端点一般核心、奇余量核心及部分上半带的细节此次主要通过已读专项审核与被引用接口组织；不声称再次逐行独立审定。总证明链接这些来源，供新读者继续核对。

## 2. 外部文献实际访问层级

| 来源 | 本次访问等级 |
|---|---|
| [Milne v1.31](https://www.jmilne.org/math/CourseNotes/MF.pdf) | 下载PDF并读取相关正文：§2商曲线/cusp，Remark4.8，§5几何Hecke，§8的8.5—8.8，Lemma11.10；不是全书通读 |
| [Stein书目导航](https://wstein.org/books/modform/modform/) | 仅目录网页；另一个 modular_curves 子页404，未用作定理依据 |
| [MIT 18.783课程导航](https://math.mit.edu/classes/18.783/2025/lectures.html) | 仅课程页面，不称为已读讲义 |
| Morris 2007、Prasad–Rapinchuk正式综述、Serre 1970 | 本轮沿用并阅读项目的原文专项审核；未重新通读外部原文，Serre原始全文仍未取得 |
| Kani，二元theta与CM | 继承旧文的题录／摘要层级；未取得或声称读过全文 |

Milne缓存的SHA256：`977f06a4e838c43c77a7c9398c090789e60d67f64e013e1dcd9bcce0e0c27b8d`。[来源元数据](../../work/prime_proof_editorial_20260915/milne_modular_forms_source.json)保留URL等信息。

## 3. 本次数学修改和没有作出的声明

- 在九偏移原文§6并入全部二进补充及隔一反射倍率的扩环。以−39/29所需13为具体例子，说明新增分母必须来自真实三角共轭；原level在扩环后重新取得。
- 集中写出标量周期、深主同余、非幺模换基、Smith—CRT取逆及精确纤维引理。
- 把各附录的方向／尺度收尾写成一个有限终端提升定理，并给出 `Um₂(B)/单位像` 的精确轨道分类及缺失尺度的反例。
- 复述已有均值格和权一theta结构，解释Γ₀／Γ₁／Γ的标记层级及局部化的区别；未借模形式证明新的阈值、容量公式或效率界。

最终素数定理仍含原来的完整有限参数证书，也仍依赖已注明的Morris/Serre。本文整理不是外部同行评审或证明助手认证。

## 4. 可重跑的素数核验集

```text
python work/run_verifications.py --profile prime-proof
```

新增 profile 只选素数主证明所需的既有核验与最终独立证书检查；不包含合数GRH工作或旧失败路线的大搜索。各条 purpose、一般量词来自何处、不能证明什么，均在[注册清单](../../work/verification_manifest.json)保留。

本轮数学正文改动集中于最终九偏移扩环，因此实际重跑这两项：

```text
python work/run_verifications.py --id nine-offsets-large-symmetric-carrier --id prime-final-independent-audit
```

其余 profile 条目是复现入口，未因重写导航而全部再跑。一般量词来自所引正文；有限公式检查与完整有限参数证书的逻辑地位不同。

本轮执行结果：**PASS=2，FAIL=0，SKIP=0**。原核验器通过522组完整参数和1440组公式／局部提升检查；独立审核通过3540条实际均值记录、521组普通level检查，并识别99组额外扩环，辅助13处完整群为2184元。详见[运行记录](../../work/prime_proof_editorial_20260915/verification_run.txt)。

另以精确有理数核对16个矩阵等式实例及两个明确反例接口，记录在[通用公式复核](../../work/prime_proof_editorial_20260915/toolkit_identity_checks.json)。这是含非幺模换基的有限抽查；一般恒等式与纤维结论由正文证明，未进行符号库认证。

本目录的路径、锚点、机器依赖图、核验ID、中文编码及归档完整性检查写入[文档检查](../../work/prime_proof_editorial_20260915/document_validation.json)。新导航出现的编码问题已修正，归档中的原文内容按原SHA256保留。检查范围不含全体历史链接。

## 5. 文档迁移与维护

原根 README 全文保存在[HISTORY.md](../../HISTORY.md)，原 outputs README 及E/H/I路线表保存在[历史路线账本](../research_routes_history_20260915.md)。归档位于原文件同目录，旧相对链接保持有效。原文SHA256与24篇状态提示清单见[归档记录](../../work/prime_proof_editorial_20260915/archive_record.json)。

技术附录没有批量移动或改名。新 [proof_map.json](proof_map.json)是便于机器导航的主证明依赖图，区分接受的附录定理、外部依赖和解释性文稿；不是对所有跨文引用的自动证明核验。
