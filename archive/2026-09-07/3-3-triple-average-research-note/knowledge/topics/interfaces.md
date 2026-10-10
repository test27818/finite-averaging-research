# 公共工具与路线边界

[总状态](../STATUS.md) · [接手入口](../START_HERE.md)

跨主题先读这些共同工具和反例边界。历史文中方法的限制可以仍有效，原可达性目标却可能已经由其他路线完成。


| ID | 结论 | 状态 |
|---|---|---|
| G-OBSTRUCTION | G的障碍模、Smith余核与目标饱和 | 本地文稿已给证明，未独立重审 |
| STABILIZATION | 正双随机运输与3幂复制稳定化 | 原证明已完成 |
| EXTERNAL-ARITH | Morris／Serre外部定理的审核与边界 | 原证明已完成 |
| OLD-HECKE-AUDIT | 旧Ihara–Hecke／Manin接入的修正 | 修正／撤回过强表述 |
| WINDOW-MEAN | 局部窗口的均值与相对尺度障碍 | 原证明已完成 |
| OLD-TRACE-RETURN | 统一／双／混合迹零返回的历史接口 | 部分结果／明确范围 |
| BURAU-REASSESS | Burau路线的现有资源与临界带容量边界 | 解释／综述，非新可达性证明 |
| AFFINE-IDEAL | 仿射交换子理想：可逆宏已有后根参数可完整计算 | 原证明已完成 |
| PARAMETRIC-RIGIDITY | 固定参数词的有限射影周期刚性 | 原证明已完成 |
| N91-CONTAINER-CORRECTION | 九十一元21504容器等式已经被反驳 | 修正／撤回过强表述 |

### G-OBSTRUCTION · G的障碍模、Smith余核与目标饱和

**状态：** 本地文稿已给证明，未独立重审。O_p(X)=坐标R理想/差分R理想；其阶为G非p部分，沿操作有逆向满射。复制稳定条件对所有n成立。

**边界：** G不是保持不变的动态量；新障碍可以产生。目标可达性不能扩大成任意运输矩阵分解。

**原文：** [G_as_obstruction_group_and_stable_threshold_20260916.md](../../research/prime_arity_padic/G_as_obstruction_group_and_stable_threshold_20260916.md)

**还应读：** STABILIZATION, GEOMETRY-ALL-N

**核验：** `python knowledge/project_knowledge.py verify G-OBSTRUCTION` 只展示已登记命令及边界，不自动启动计算。

### STABILIZATION · 正双随机运输与3幂复制稳定化

**状态：** 原证明已完成。任意n：G为3幂 ⇔ 存在严格正三进双随机P消去X ⇔ 某个3幂复制后真实可达。

**边界：** 原位置分解不随运输存在自动成立；五、六元有复制后成功而原态失败。n≥7复制消去可由已证总定理推出，不是独立新证明。

**原文：** [triple_average_stabilization_theorem.md](../../outputs/triple_average/history/triple_average_stabilization_theorem.md)

**核验：** `python knowledge/project_knowledge.py verify STABILIZATION` 只展示已登记命令及边界，不自动启动计算。

### EXTERNAL-ARITH · Morris／Serre外部定理的审核与边界

**状态：** 原证明已完成。原素数证明所需有限指数、强同余性质及无限单位前提的明确引用接口。

**边界：** 已读来源与未取得原文须按审查文稿保留；有限模像满不推出全群包含。

**原文：** [prime_arity_lower_band_external_theorems_audit_20260915.md](../../outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md) · [prime_arity_endpoint_congruence_completion.md](../../outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md)

**核验：** `python knowledge/project_knowledge.py verify EXTERNAL-ARITH` 只展示已登记命令及边界，不自动启动计算。

### OLD-HECKE-AUDIT · 旧Ihara–Hecke／Manin接入的修正

**状态：** 修正／撤回过强表述。保存原Hecke关系、星结构、中心符号及物理分支提升的审计；旧直接闭合推断不可作为定理使用。

**边界：** 不否定全部自守方法；七元实群、五元Aka–Shapira接口必须按各自已证前提使用。

**原文：** [triple_average_final_hecke_audit.md](../../outputs/triple_average/history/triple_average_final_hecke_audit.md)

**还应读：** SEVEN-GEOMETRY, FIVE-HECKE

**核验：** `python knowledge/project_knowledge.py verify OLD-HECKE-AUDIT` 只展示已登记命令及边界，不自动启动计算。

### WINDOW-MEAN · 局部窗口的均值与相对尺度障碍

**状态：** 原证明已完成。子块差分缩放只围绕子块自身均值，外部位置不跟随；不能当作整系统射影逆。

**边界：** 重写仿射矩阵或换称标记格不会自动提供窗口拼接定理。

**原文：** [prime_arity_middle_band_relative_scale.md](../../outputs/prime_arity/structure/prime_arity_middle_band_relative_scale.md)

**还应读：** GEOMETRY-ALL-N

**核验：** `python knowledge/project_knowledge.py verify WINDOW-MEAN` 只展示已登记命令及边界，不自动启动计算。

### OLD-TRACE-RETURN · 统一／双／混合迹零返回的历史接口

**状态：** 部分结果／明确范围。参数化周期和部分根公式成立；指定返回的原位置分解是更强目标，旧单返回充分性曾过强。

**边界：** 原可达性已由别的路线完成；运输／复制证书不是这些指定矩阵的原位置分解。

**原文：** [triple_average_universal_trace_zero_target.md](../../outputs/triple_average/history/triple_average_universal_trace_zero_target.md) · [triple_average_two_trace_zero_returns.md](../../outputs/triple_average/history/triple_average_two_trace_zero_returns.md) · [triple_average_mixed_singleton_controller.md](../../outputs/triple_average/history/triple_average_mixed_singleton_controller.md)

**还应读：** STABILIZATION, OLD-HECKE-AUDIT, AFFINE-IDEAL, PARAMETRIC-RIGIDITY

**核验：** `python knowledge/project_knowledge.py verify OLD-TRACE-RETURN` 只展示已登记命令及边界，不自动启动计算。

### BURAU-REASSESS · Burau路线的现有资源与临界带容量边界

**状态：** 解释／综述，非新可达性证明。正向中心、几何链及非零均值修正有效；三幂链最短容量与2p—4p临界带不匹配。

**边界：** Zariski稠密不等于算术指数／终端覆盖；不能因三平均就假设B₃。

**原文：** [burau_route_reassessment.md](../../research/prime_arity_padic/burau_route_reassessment.md)

**核验：** `python knowledge/project_knowledge.py verify BURAU-REASSESS` 只展示已登记命令及边界，不自动启动计算。

### AFFINE-IDEAL · 仿射交换子理想：可逆宏已有后根参数可完整计算

**状态：** 原证明已完成。可执行仿射生成元的导群参数理想由交换子与倍率局部化精确生成；无需逐参数搜根。

**边界：** 必须先有真实正向逆；非零理想不等于本原理想，导群也不必是全部平移核。

**原文：** [triple_average_affine_commutator_ideal.md](../../outputs/triple_average/history/triple_average_affine_commutator_ideal.md)

**还应读：** OLD-TRACE-RETURN

**核验：** `python knowledge/project_knowledge.py verify AFFINE-IDEAL` 只展示已登记命令及边界，不自动启动计算。

### PARAMETRIC-RIGIDITY · 固定参数词的有限射影周期刚性

**状态：** 原证明已完成。固定有理函数矩阵词若非恒等满足分圆迹关系，仅有限参数有有限射影阶；无限族须有恒等关系或变化词形。

**边界：** 不排除随参数无界增长的词，也不否定后来的统一正向种子。

**原文：** [triple_average_parametric_cycle_rigidity.md](../../outputs/triple_average/history/triple_average_parametric_cycle_rigidity.md)

**还应读：** OLD-TRACE-RETURN

**核验：** `python knowledge/project_knowledge.py verify PARAMETRIC-RIGIDITY` 只展示已登记命令及边界，不自动启动计算。

### N91-CONTAINER-CORRECTION · 九十一元21504容器等式已经被反驳

**状态：** 修正／撤回过强表述。模8和模91的尺度字符耦合，证明特定宏群不等于旧21504容器；必要容器修正为43008。

**边界：** 43008仍只是必要容器，未证明等于实际宏群；九十一元可达性已有独立归约，不能混为未解。

**原文：** [triple_average_permutation_shadow_entanglement.md](../../outputs/triple_average/history/triple_average_permutation_shadow_entanglement.md)

**还应读：** OLD-HECKE-AUDIT

**核验：** `python knowledge/project_knowledge.py verify N91-CONTAINER-CORRECTION` 只展示已登记命令及边界，不自动启动计算。
