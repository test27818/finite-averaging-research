# `work/` 使用说明

无条件端点入口核验：unrestricted-endpoint-entry，对应[完整端点及全部奇数下半带](../outputs/prime_arity_unrestricted_endpoint_and_odd_band.md)。79组有理交换子、1965组有限模正向编译、28条逐位置入口和16条完整核心归约均通过；另以压缩账本跨过七素因子覆盖例及旧r<omega(n)入口缺口。程序不搜索平均词，不展开巨大群论归零尾部；完整定理由新入口与已有核心证明连接承担。

内部偶余量核验：even-interior-completion，对应[内部偶余量完整证明](../outputs/prime_arity_even_interior_completion.md)。65组奇半核代数、110组全部内部参数、9200个单位类、520个终端输送、64类r=4二进制状态、256类r=p-3状态和48条边界输送通过。完整证明保留Morris/Serre依赖，并不覆盖r=2或r=p-1。

缺口复查核验：core-gap-four-lifts，对应[常高度乘法与有限例外](../outputs/prime_arity_core_gap_reassessment_20260915.md)。约一秒验证精确四lift判据、无限失败锥、两种逃逸、前缀约分、终端分母以及任意奇p的小分母完整算法。Furstenberg拓扑定理及其有限例外推论由文档明确引用和证明，程序不代替外部定理，也不证明一般阈值。

完整邻点算法：two-prime-neighbour-complete，对应[统一文稿第11节](../outputs/prime_arity_unified_weighted_core_theorem.md)。验证所有奇p>=5且omega(p+1)<=2时n=2p+2的严格整数下降，输出包含完整原位置归零路径；五平均12元因此完成。多奇素因子情形、其他偶余量不由本条目覆盖。

七平均最优阈值核验：seven-average-sharp-completion，对应[完整证明](../outputs/seven_average_sharp_threshold_complete.md)。固定正向循环和有限证书补齐20、22元，接旧维数得到N(7)=15；程序保留22元有限单位像的两个尺度类。证书数据为seven_average_sharp_completion_records.json，未展开任意主同余矩阵的全长平均词。

统一中间带入口核验为 uniform-two-block-entry，对应[统一证明文稿](../outputs/prime_arity_unified_weighted_core_theorem.md)及verify_uniform_two_block_entry.py。它验证不带旧周期/gcd条件的两轮入口，并检查两带公共格、返回及终端公式；不证明一般偶数核内终止。完整有限方向模型须保留R单位像，不能直接用普通有限射影线替代。

当前研究状态及已尝试路线先见 [研究索引](../outputs/README.md)。以下保留核验程序的历史说明，其中旧的未解维数、入口范围和“下一步”须结合索引及后续专题确认；不能据旧说明重开已经完成或已排除的任务。

全局数学状态见 `outputs/averaging_global_status_20260912.md`：按固定维数判据、自动G、非自动G边缘H和最终阈值N四类量词整理，避免把无条件网络点误当作G等价结果。

十平均与十二平均17元入口是 `ten-twelve-seventeen-complete`，对应 `outputs/ten_twelve_average_seventeen_complete.md` 与 `verify_ten_twelve_average_seventeen.py`；均得到G=1充要，H(10)=H(12)=17。程序保存6条完整路径及q<=200自动B表。两个17元控制器使用不同的Delta(5)/Delta(3)局部激活，不能将一种平均元数的矩阵词混用于另一种。

外部Arena三平均网页的审阅独立放在 `arena_triple_solver_review/`，对应 `outputs/arena_triple_solver_review.md`；核验ID `arena-triple-solver-review`。48个同题比较、预热计时、源码SHA256、数值尺度反例和所有成功索引均保存。快速核验只重放已有证据，不重新访问网页或运行长搜索；本任务不修改数学构造算法。

`work/` 保存研究计算的完整历史，因此仍是平铺目录。为保留旧文档引用，本次没有移动或重命名文件。新接手者不应通过文件名前缀猜测数学结论，而应从 `verification_manifest.json` 查找结论到程序的明确对应关系。

合数端点统一核验入口 `composite-endpoint-transfer` 对应 `outputs/composite_endpoint_crt_transfer.md`。`composite_endpoint_pivot_certificates.json` 存36个模数的全部32112条回路；`verify_composite_endpoint_transfer.py` 独立检查，不导入构造器或主元搜索。28个两素因子模数得到完整输入判据，另8个仅核心覆盖；结果明确保存在 `composite_endpoint_transfer_results.json`。`build_composite_endpoint_certificates.py` 和 `explore_composite_endpoint_transversals.py` 负责有限证书生成，失败不等于不可达。无限两素数入口已证明；任意level的群包含及多素数入口仍是不同问题。

最新入口 `seven-average-fifteen-complete` 对应 `outputs/seven_average_fifteen_complete.md` 与 `verify_seven_average_fifteen_complete.py`。使用已证七平均端点种子，新增两素数三步入口和模15的完整24陪集、72回路编译，严格证明G=1充要及H(7)=15。`seven_average_fifteen_witnesses.json` 保存7条完整路径与72个特殊入口输入。用户取消的六平均十一元探索文件保留但不继续推进，也不登记为完整定理；后续按平均元数增加研究，8平均13元已证，下一候选为9平均13元。

最新非自动G判据入口为 `six-average-ten-complete`，对应 `outputs/six_average_ten_complete.md` 与 `verify_six_average_ten_complete.py`。它完整覆盖G1和G2、排除G5和G10，严格给出H(6)=10。`six_average_ten_witnesses.json` 保存6条完整路径；`explore_six_average_ten_macros.py` 及其发现表只作溯源，正式核验不导入。新的两步R返回、实际尺度周期和模5交换子全部明确实现，不能把Sigma当成免费交换不等块。

当前合数临界线入口为 `composite-critical-scale` 与 `eight-average-thirteen-complete`，共同对应 `outputs/composite_critical_scale_and_conjecture.md`。前者核验局部素数幂平方根尺度的反例下界和连续整数乘积的固定四步网络；后者完成八平均13元并结合下界证明其为排除n=q后的最早成功维数。`composite_critical_scale_results.json` 保存下界表和网络，`eight_average_thirteen_witnesses.json` 保存5条完整路径。`explore_composite_minimal_core_periods.py` 仅记录短周期发现，预算未命中无不可达含义；正式核验不导入它。M最早成功与N最终阈值必须区分。

任意平均元数的充分大维数统一入口是 `arbitrary-arity-linear-threshold`，对应 `verify_arbitrary_arity_linear_threshold.py` 与同名证明文档；保存70条一般路径和24条造零收尾路径。四平均九元的完整入口是 `four-average-nine-complete`，对应 `verify_four_average_nine_complete.py` 与 `outputs/four_average_nine_complete.md`；保存6条经真实尺度重放的原位置路径。两者都没有平均词发现搜索，均由正文证明全称结论。

四平均七元的精确入口是 `four-average-seven-complete`，对应 `verify_four_average_seven_complete.py` 与 `outputs/four_average_seven_complete.md`；它用 (4,2,1) 加权核心和模7陪集控制器证明七元本身的完整判据，保存12条完整路径。

六平均九元独立入口是 `six-average-nine-fixed-network`，对应 `verify_six_average_nine_fixed_network.py`：只用标准库核对固定四步矩阵、全部756个二步后继行和160个有理输入，证明四步为固定全输入网络的最优长度。四平均七元的Sigma由真实C²B词实现，不能免费交换不等大小块；其文档明确区分实际周期尺度与射影等式。两个入口均不证明整体N(4)=7或N(6)=9。

合数平均入口是 `composite-four-six-transfer`。`verify_composite_arity_transfer.py` 对应 `outputs/composite_arity_four_six_transfer.md`，核验偶数元数半块转译、四平均偶数维数和六平均三的倍数维数；生成的 `composite_arity_transfer_witnesses.json` 保存336条原始输入与1基完整序列。商层调用已有二平均HTML，最终Fraction重放只信任原输入和操作索引。全称证明在文档；未解决维数不能据此标为不可达。

## 统一入口

从项目根目录运行：

```text
python work/run_verifications.py --list
python work/run_verifications.py --profile smoke
python work/run_verifications.py --profile core
python work/run_verifications.py --id n13-complete
```

运行器会检查清单结构、引用文件是否存在、程序退出码和预期输出标记。这里的 `PASS` 只表示该程序重现了清单声明的计算结果；它的数学效力不能超出同一条目的 `evidence_scope`。

`reynolds-hodge-structure` 核对原子Reynolds恒等式、完整生成代数及危险素数处的Hodge／Fricke边界；`contingency-layer-semigroup` 实际重放运输表层及交数秩，给出无需子问题调用的有限半群模型。其终端覆盖没有被宣称已证。

`final-hecke-manin-audit`是当前Hecke路线入口：核对整数幺模共轭、第二算子的共同正定星结构障碍、三角方向、普通Manin中心负号及两个位置／卷积模型的区别。旧`iwahori-hecke-modular-interface`的ID保留，但只核对有限代数恒等式；局部特征线并非已识别的自守分量，数字置换和也并非已实现的T_3。旧推导存档与纠正见`outputs/triple_average_final_hecke_audit.md`。

`explore_nonsplit_hecke_charts.py`检查非分裂Reynolds的一至三层B_p chart返回；`explore_bcore_atomic_hecke_walls.py`按二维系数类型和重数穷尽短原子词中的非标准Hecke墙。二者都是有界阴性诊断，不排除直接终端或带子问题的长gallery。

`explore_bcore_symbolic_terminal_cover.py`把整个B_p(1,v)参数族保留为二维整数系数，一棵状态树同时求出所有整数v终端超平面。登记的B71窗口覆盖是有限探索证据；大窗口显示固定深度语言稀疏，不能外推为统一六步定理。

2026-09-11的载体路线复盘见`outputs/triple_average_route_reassessment_2026-09-11.md`。`explore_equal_carrier_*`检查等载体有限域轨道、正向协向量、B核特殊族与固定中心收缩同步；`explore_bcore_zero_triple.py`用整数值--重数状态寻找真实零和三元组，`explore_bcore_zero_triple_greedy.py`比较局部贪心规则。这些`explore_*`文件都是有限诊断；其中一次具体等载体搜索的共同尺度错误已在脚本和复盘中明确修正，旧输出不得引用。

`n47-complete` 完成47元：固定尖点词和校正伸缩、18个Schreier回路正向消元、48陪集及独立标签、全部合法方向输送。`localized-iwahori-generation` 核对任意素数的标准根／单位生成接口和通用奇次三进尖点恒等式，实际资源的普遍正向实现仍开放。发现工具 `explore_b47_schreier_roots.py` 只负责定向找词，不是正式核验入口。

`b47-root-activation` 独立检查固定 `b47_root_activation_certificate.json`，三层46/113/2激活全部167旧宏的逆，连同种子共170节点；核验不导入发现工具 `explore_b47_root_activation.py`。另检查57模板正向共轭词及两个完整相对根群。它单独不承担47元完整判据，后续n47-complete补齐。

`b47-extra-atom-involutions` 固定三个新extra-stage模板及47Z[1/6]平移；`adjoint-return-domain-audit` 检查倒序投影是否真的满足普遍调用域。共享 `verify_bn_integer_templates.py` 的extra字段可选，旧输入沿用两阶段流程。两个搜索文件的阴性结果仅限记录的模板范围，不是不可达证明。

`projective-spectral-balance` 包含任意秩给定矩阵的精确Ad分圆算法。`b47-short-cycle-boundary`（仅full）使用NumPy整数数组作无遗漏模筛选，完整整数复核全部幸存者；`search_four_factor_cycles.py` 是单独的浮点发现工具，阴性结果没有证明效力。

`paired-carrier-two-adic-reset` 核验原维数的等值载体二进宏、两个R理想的精确共同缩放，以及受限宏库的周期障碍；构造有效不等于它已有正向逆。全部操作用真实原位置系数重放。

`n41-complete` 固定21宏、10个三因子对合和10个整数词，正式核验不运行发现搜索。`explore_integral_cycle_closure.py` 使用行列式平方类和两字母状态作有界发现；`modular-primitive-height-barrier` 则重放有限模调度中实能量下降而本原高度指数增长的精确族。

`two-carrier-modular-bridge` 核验一般n=5 mod6的正向降维接口。有限模逆由正向幂实际重放；大子问题只在明确同余域调用，并再次检查全局G。一般群论控制的存在性在正文，脚本未实现大维数任意输入的完整词求解器。

`n29-complete` 是冻结旧子问题库上的独立29元证书，不运行发现搜索。`search_bn_three_cycle.py` 用浮点提出候选并精确复核，阴性输出没有不存在证明效力。`--expanded-first` 只扩充探索用首步大小，不改变默认库。非分裂射影层的有限精确边界登记为 `nonsplit-projective-layer-boundary`。

`split-prime-gaussian-controller` 核验原位置数的高斯周期正向控制器，对应全部p=1 mod3的统一证明。`explore_gaussian_period_layers.py` 同时提供构造辅助函数，不是通过有限素数表宣称全称结论。当前solved_size包含该无限素数族的因子闭包。

新增 `one-tripling-stabilization` 对应一次三份复制、整数仿射轨道及所有三整除维数定理；包含87元接口，但不证明29元。`compile_bn_integer_templates.py` 的 `certificate_size` 保留旧证书库，`solved_size` 才使用新增维数，避免历史证书的矩阵数量随库增长而变化。

`balanced-digit-congruence-group` 核验副本数字库的完整整数同余群生成接口。`b29-current-cycle-boundary` 核验当前B29库的二因子周期排除及全部指数A^jB的精确迹方程；它不运行不断增长的词搜索。

`flat-star-formal-arithmeticity` 核验原维数形式群的显式幺幂和第一层局部接口，有限指数证明另使用已声明的标准初等同余群定理。`cyclotomic-level-entanglement` 建立旧21504容器的43008状态耦合二重覆盖；旧自动机的标签没有改号，旧终端缓存不视为新容器证书。

三档用途如下：

- `smoke`：最新关键结构和九十一元同余容器，通常少于 10 秒。
- `core`：已完成基维数证书和主要一般归约，通常约 1 至 2 分钟。
- `full`：清单中的全部项目，包括九十一元深度四、cusp 29 深度五和新增四维数核实验。长搜索集中于 cusp 29 与 B21；不保证固定总时长。

## 证据等级

- `theorem-certificate`：精确有限证书，闭合证明中明确陈述的有限子问题。一般归约仍需阅读对应证明文档。
- `symbolic-check`：用精确整数或有理数检查恒等式、真实宏和有限参数实例。
- `finite-sanity`：有限穷举或固定随机种子的有界实验，用于防止公式和实现错误，不能承担无限量词。
- `exploratory-search`：有限深度或有限高度搜索。没有找到见证不等于不可达证明。

## 历史文件前缀

- `verify_*`：作者当时用于核对某个公式或证书；强度可能属于上述任一等级。
- `check_*`：局部一次性核对，通常没有稳定输出契约。
- `search_*`、`explore_*`、`analyze_*`：搜索、数据生成或诊断，默认不能引用为完整证明。
- 其他 `.py` / `.js`：共享辅助模块、数据整理或早期实验。
- `.pickle`：历史搜索缓存，不是独立证书。
- `__pycache__/`：运行产物，可忽略。

新增或修改一项可引用的计算结论时，应同时更新：

1. 对应数学文档中的结论和证明边界；
2. `verification_manifest.json` 的命令、输出标记、证据等级和运行时间；
3. 必要时更新 `outputs/triple_average_verification_guide.md` 的人工索引。

有限搜索必须记录全部参数，例如深度、模数、输入界、覆盖数和未覆盖数。九十一元脚本默认深度 2，得到 `14/24`；深度 3 得到 `20/24`；深度 4 得到 `23/24`；定向深度 5 搜索 cusp 29 得到最后一条证书，容器内有限深度覆盖为 `24/24`。脚本默认使用全部逻辑处理器，也可用 `--jobs 1` 做串行对照。
