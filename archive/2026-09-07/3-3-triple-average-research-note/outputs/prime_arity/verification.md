# 本次整理的阅读、修改与核验范围

2026-09-15。本页按阶段保留实际阅读和核验记录；当前浅层同余提升见第10节，162组证书是最新版本。前节中的180／522组均指对应历史阶段。文档重组不等于独立重证全部数学。

## 1. 实际阅读的项目文本

以下是正文阅读，不只是文件名检索；“相关节”不表示通读整篇。

| 文档 | 本次读取范围／用途 |
|---|---|
| [最终独立审核](audits/prime_arity_optimal_threshold_independent_audit_20260915.md) | 全文；量词、99组额外扩环、两项特殊补充、下界、证书及审核边界 |
| [下半带外部定理审核](audits/prime_arity_lower_band_external_theorems_audit_20260915.md) | 主结论及§§2—5；Morris/Serre前提、任意有限环消元 |
| [3p+10审核](audits/prime_arity_three_p_plus_ten_audit_20260915.md) | 上端与尾部拼接、外部依赖和证据说明 |
| [九偏移共同证明](proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md) | 入口、四原子反射、§§4—9；容量、换基、扩环、局部方向和尺度 |
| [内部偶余量](proofs/lower_band/prime_arity_even_interior_completion.md) | §§1—6；取逆、有限循环、纤维接口及分支范围 |
| [2p+2统一证明](proofs/lower_band/prime_arity_two_p_plus_two_uniform.md) | §§1—4；统一返回、CRT与精确终端 |
| [中间维数结构](proofs/lower_band/prime_arity_middle_band_structure.md) | §§1—4；3p的三块运输与固定level |
| [逆EGZ](proofs/tail_and_lower_bound/prime_arity_inverse_egz_threshold.md)及[4p尾部](proofs/tail_and_lower_bound/prime_arity_four_p_tail_completion.md) | 各§§1—4；旧不等式与已补齐范围 |
| [全部3p+10以上](proofs/upper_band/prime_arity_all_prime_three_p_plus_ten.md) | §§8—10及相关接口；小p收口、旧九偏移状态定位 |
| [插值与均值格](tools/prime_arity_interpolation_and_lattice_structure.md) | §§1—3、6—7；造零、禁止免费插值、整数格指数 |
| [旧端点几何](tools/prime_power_endpoint_and_critical_geometry.md) | §§5—6，并回查相关两图／Schreier段；范数、theta与外部尺度障碍 |
| [Hecke最终审核](../triple_average/history/triple_average_final_hecke_audit.md) | §§1—8；分支求和、正向实现和符号边界 |
| [无条件入口](proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md) | 定理、依赖和§2块—单点交换；其余入口细节此次依照专项审核，未逐式重证 |
| [线性阈值](proofs/tail_and_lower_bound/prime_arity_linear_threshold.md) | 不变量与能量结论、§§8—9的2p反例和最低p进赋值论证 |
| [三平均任意维数](../triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md) | 定理、适用范围与不变量；7—10基例的完整证明未在本次重跑 |
| [二平均与三平均比较](../literature/binary_vs_ternary_averaging_followup.md) | 结论与共同算术层；2018原证明的完整源文审核沿用既有记录 |
| [合数交接](../general_arity/general_k_three_tasks_progress_20260915.md) | 当前结果、GRH条件、三项剩余范围，用于保持导航正确；不推进合数证明 |

另直接读取两个原 README 的导航、结论表及历史组织，查看全项目核验注册的相关条目与运行器，并读取最终独立审核脚本及固定证书接口。[此前阅读日志](../history/research_reading_log_20260915.md)记录其他回合，不能混称本次全部新读。

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

首次整理的 profile 选择素数主线与最终独立证书检查；当前按第10节改为162组浅层提升证书，不包含合数GRH或旧失败路线大搜索。各条purpose和证据边界均在[注册清单](../../work/verification_manifest.json)保留。

本轮数学正文改动集中于最终九偏移扩环，因此实际重跑这两项：

```text
python work/run_verifications.py --id nine-offsets-large-symmetric-carrier --id prime-final-independent-audit
```

其余 profile 条目是复现入口，未因重写导航而全部再跑。一般量词来自所引正文；有限公式检查与完整有限参数证书的逻辑地位不同。

本轮执行结果：**PASS=2，FAIL=0，SKIP=0**。原核验器通过522组完整参数和1440组公式／局部提升检查；独立审核通过3540条实际均值记录、521组普通level检查，并识别99组额外扩环，辅助13处完整群为2184元。详见[运行记录](../../work/prime_proof_editorial_20260915/verification_run.txt)。

另以精确有理数核对16个矩阵等式实例及两个明确反例接口，记录在[通用公式复核](../../work/prime_proof_editorial_20260915/toolkit_identity_checks.json)。这是含非幺模换基的有限抽查；一般恒等式与纤维结论由正文证明，未进行符号库认证。

本目录的路径、锚点、机器依赖图、核验ID、中文编码及归档完整性检查写入[文档检查](../../work/prime_proof_editorial_20260915/document_validation.json)。新导航出现的编码问题已修正，归档中的原文内容按原SHA256保留。检查范围不含全体历史链接。

## 5. 文档迁移与维护

首次整理将原根 README 保存在[HISTORY.md](../../HISTORY.md)，原 outputs README 及E/H/I路线表现位于[历史路线账本](../history/research_routes_history_20260915.md)。后续迁移已经修复其中的相对链接；迁移前完整字节另存于原文快照，不能再用首次整理的原文SHA256核对迁移后的链接文本。首次归档记录见[原记录](../../work/prime_proof_editorial_20260915/archive_record.json)，最新位置及快照见第6节。

首次整理未批量移动附录；后续已实际迁移220篇，文件名保持不变。[proof_map.json](proof_map.json)同步更新了技术来源与证书，不是自动形式化证明。

## 6. 当前文件夹结构与证明简化

后续直接回读九偏移全文、独立核验器的计数／方向／二进补充／辅助13、上半带三值归约与现有结构说明。推导并写出[整数区间与最小缺失单位](structure/carrier_interval_and_unit_descent.md)：

- p≥97 的所有反射来自统一闭式整数区间，替代旧 p≥307 的构造分界。
- 11≤p<97 只保留180组反射证书及原来的两项局部修补；其余342组已由一般公式承担。
- 全范围入口改为直接计数；模n基础单位生成改为最小反例下降和固定有理区间覆盖，不再枚举各参数的有限单位群。
- 18组容量不等式接口、15个四单位区间覆盖、180组完整剩余证书、342组旧参数交叉核验及45组较大参数核验均通过。一般量词由正文证明，后两组只是公式对照。

新核验ID为`carrier-interval-reduction`。当前`prime-proof`有18项，改用此项替代旧522组核验；原核验及独立审核保留为可单独执行的历史证据。因为本轮迁移修改了注册与大量引用，已执行整个当前profile：**PASS=18，FAIL=0，SKIP=0，83.39秒**，见[完整运行记录](../../work/document_reorganization_20260915/prime_profile_run.txt)。

文件夹地图见[成果索引](../README.md)。220篇文档实际迁移，各文件夹有索引；[旧新路径表](../../work/document_reorganization_20260915/path_map.json)供旧引用定位，[迁移报告](../../work/document_reorganization_20260915/migration_report.json)记录范围。原文快照在work/document_reorganization_20260915/originals。全部成果Markdown目标和核验路径检查见[迁移验证](../../work/document_reorganization_20260915/validation.json)。HISTORY中一段原有编码损坏按迁移前内容保留，没有猜写数学原文。

未新增外部深定理，未声称模形式替代容量，也未消除剩余180组或一般算法长度问题。合数研究本轮只迁移归类，条件与开放范围保持原文。

## 7. 构造原则的进一步提炼

[整格拼接与正运输](structure/integral_gluing_and_positive_transport.md)给出两项直接证明：指定常值方向的整提升条件Bη=cη modN；等大块上有限个保总和／保常值的整数自同构及其逆，在充分大平均元数下均有一层真实运输实现。它统一解释原3p构造，不声称降低任何新阈值或消去180组。

本轮直接阅读章节详列于该文第7节；特别回查旧Reynolds、有向范畴、数字同余群和根格文本，避免把旧术语当成新发现。没有运行参数搜索或重跑未修改的数学核验；两个命题以正文代数和逐位置计数证明。新增导航经过链接检查。

## 8. p进翻译与外部结构核对

[p进局部说明](structure/padic_places_and_canonical_branches.md)新增直接推导：pP_S在模p下秩一且平方为零；端点合法及非法有理方向在P¹(Qp)中各自稠密；已证的各层完整循环通过逆极限与ℓ进加一机共轭。没有改变阈值或证书数。

实际取得并阅读Buzzard《Analytic continuation of overconvergent eigenforms》的引言、典范子群定理3.3及迹／U_p命题5.1，Buzzard《Eigenvarieties》引言及§6开头，Buzzard—Gee《Slopes of modular forms》引言前3页。未通读这些全文；Katz／Lubin为前者的明确引用。准确链接、下载哈希与访问边界在专题末节及work/padic_structure_20260915。没有新外部定理作为可达性证明依赖，没有运行参数搜索。

## 9. 二次局部群与原子首位的进一步研究

[局部二次群](structure/padic_quadratic_group_and_orbit_defect.md)直接证明：合法分式线性图是群律(x+y)/(1+cxy)；深层形式对数线性化；首层倍映射的赋值d决定高层轨道长度与稳定轨道数。它重证原三进条件，并把坏类分成有限指数缺陷与真实三周期。一般二进迹条件和单位尺度的二进扭点仍分别保留。

新核验`padic-quadratic-group`通过4项符号群律恒等式、36项明确好／坏／扭点轨道实例、5项深度40的快速幂阶检查，以及全部180组保留证书的364个局部正规形，其中二进100处。不搜索平均词，不遍历深层全部状态。无限层分类由正文证明。

[Kneser边界](structure/padic_leading_symbols_and_kneser_boundary.md)从原子首位秩一乘法直接推导任意词的交数乘积，解释n=2p与2p+1不交图的连通性突变。没有把首位连通当成完整算术可达性。

同文第3.1节进一步精确计算两次不交平均：pP_TP_S=B_S+B_T+pD_R；在零和空间上的首位秩由n=2p时的1变成n≥2p+1时的2，且端点的完整有理像恰是既有双块—单点核心。这是直接矩阵恒等式，不是有限图样本外推；合法入口仍需已有见证交换。

实际读过：旧局部循环及方向、尺度证明和对应逐位核验程序；Conrad强逼近讲义§1命题1.1及证明；Buzzard主系列讲义§1和§4。Fan—Fan—Liao—Wang的2014分式线性动力系统论文只核对题录、摘要，全文多种公开地址获取失败；未引用其定理。外部来源与尝试记录见work/padic_structure_20260915。Kneser文献只查标准题录，连通性由本文两步构造证明。

当前阈值与180组证书数不变；本轮新增的是结构定理、局部缺陷诊断和首位边界解释，没有再跑未变动的整个18项主线。

## 10. 三个共轭根替代高阶轨道

当前[浅层提升定理](structure/transverse_root_lifting_without_long_orbits.md)把九偏移的控制层降到奇数n的Γ(n,R)，及偶数n的Γ(2δn,R)、δ∈{2,4}。它由三个真实共轭根的切向行列式−b³tr(T)/(det T)²、逐层线性修正和既有精确深核证明；没有用局部闭包替代真实包含。分母清除及扩环后重建均写明。

奇数n的高阶方向循环和主单位提升从证明中删除；偶数n模n以上只需至多8个二进方向和尺度类。三进好轨道条件不再需要，连续三个反射参数已够，统一公式覆盖p≥83，有限反射证书由180减到162。旧辅助13及(13,3)二进补充仍保留。

本轮实际读取：九偏移第5—9节、最新容量区间第3—6节、二次局部群全文的相关规则、原核验器的计数／方向／二进分支。新核验`transverse-root-shallow-lifting`通过符号切向行列式、36项精确逐层修正（包含一个本身为三阶周期的宏）、162组676条根反射记录、387组从83起的三连参数接口及15组单位区间覆盖。没有搜索新平均词或枚举深层轨道。

当前18项profile改用此核验；运行记录为[浅层版核验记录](../../work/document_reorganization_20260915/prime_profile_shallow_run.txt)。一般提升和无限参数由正文证明，有限接口重放不替代Morris／Serre。
