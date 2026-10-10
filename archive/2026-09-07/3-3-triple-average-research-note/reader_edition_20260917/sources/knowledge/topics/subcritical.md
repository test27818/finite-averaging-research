# 阈值以下与五元算术

[总状态](../STATUS.md) · [接手入口](../START_HERE.md)

先读SUBCRITICAL-COMPLETE最新一般p稿：p至2p都有统一整数补集判定，p+2为强制递归且最短可求；p+3以后一般位长多项式界未得。五元静态算术分类与固定D逃逸另列，不要把已解可判定性重开。


| ID | 结论 | 状态 |
|---|---|---|
| SUBCRITICAL-COMPLETE | p至2p统一补集判定；p+2强制递归与p进二叉结构 | 本地文稿已给证明，未独立重审 |
| SUBCRITICAL-LIMITS | 低维G加固定同余、实半代数判据的限制 | 本地文稿已给证明，未独立重审 |
| SIX-EXPLICIT | 六元三重核心G=3与唯一后继 | 本地文稿已给证明，未独立重审 |
| FIVE-SUMMARY | 五元：算法已解、静态分类仍未解 | 解释／综述，非新可达性证明 |
| FIVE-NORM-SLICE | 统一椭圆宏范数剥离、根标签耦合与−59／−971判据 | 本地文稿已给证明，未独立重审 |
| FIVE-NORMAL-FORM | 五元完整受限连分数与level15矩阵序 | 本地文稿已给证明，未独立重审 |
| FIVE-FRACTAL | 三进紧集的全部有理点与密度 | 本地文稿已给证明，未独立重审 |
| FIVE-DIGITS | 原整数同步三进非正则、精确进位与有理代数对应 | 本地文稿已给证明，未独立重审 |
| FIVE-TORUS | 统一Q(√5)范数一环面与扭曲平移 | 本地文稿已给证明，未独立重审 |
| FIVE-DENOMINATORS | 精确D、相邻互素、同理想任意近的失败点 | 本地文稿已给证明，未独立重审 |
| FIVE-UNITS-GROUP | 固定理想单位指数与三进大群闭包 | 本地文稿已给证明，未独立重审 |
| FIVE-SPARSITY | 固定D有效稀疏与固定周期有限返回 | 本地文稿已给证明，未独立重审 |
| FIVE-BOUNDED-RUNS | 有界字母切换的有效有限性 | 本地文稿已给证明，未独立重审 |
| FIVE-HECKE | 显式间隙界与同层共同Hecke二次型 | 本地文稿已给证明，未独立重审 |
| FIVE-TEMPLATE-ESCAPE | 固定多块模板统一逃离小分母 | 本地文稿已给证明，未独立重审 |
| FIVE-ESCAPE-OPEN | 固定D全词逃逸与D=1完整分类 | 开放问题 |

### SUBCRITICAL-COMPLETE · p至2p统一补集判定；p+2强制递归与p进二叉结构

**状态：** 本地文稿已给证明，未独立重审。奇p的p+2强制判定与最短词完整，环面为Q(√(p²−4))范数一曲线，固定S一步对应四穿孔P¹。p+3完整像为P²，含自同构、到直线的投影及终端直线；单例外两端坐标单位条件为两个三穿孔P¹的乘积。一般p+r有整数能量图与G公式。

**边界：** 固定S一步整点不等于全轨道静态分类；p+3五直线补集只描述一种分支，未得覆盖所有降秩分支的共同环面。一般p+r仅伪多项式算法；实际整数尺度不能随意丢掉。p=2四穿孔模型退化。

**原文：** [subcritical_complement_dynamics_20260916.md](../../research/prime_arity_padic/subcritical_complement_dynamics_20260916.md) · [subcritical_prime_uniform_arithmetic_20260917.md](../../research/prime_arity_padic/subcritical_prime_uniform_arithmetic_20260917.md)

**条件／外部依赖：** 仅固定S相邻边及开曲面整点有限性使用ESS定理1.1；算法、p进分类及一般p坐标公式不依赖ESS

**证据／文献记录：** [source.json](../../research/prime_arity_padic/five_torus_literature_20260917/source.json)

**还应读：** SUBCRITICAL-LIMITS, FIVE-FRACTAL, SIX-EXPLICIT, FIVE-TORUS

**核验：** `python knowledge/project_knowledge.py verify SUBCRITICAL-COMPLETE` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 区分曲面上的真实降秩路径与人为固定S整点条件；p+2继续静态算术压缩，p+3及一般p+r需同时控制自同构与真子集投影，不由维数猜测现成高秩群判据。

### SUBCRITICAL-LIMITS · 低维G加固定同余、实半代数判据的限制

**状态：** 本地文稿已给证明，未独立重审。对每个奇素数p、每个p+2≤n≤2p和任意固定M，都有逐项modM相同、G均为1的一可解一不可解输入；一个全r公式统一旧端点例子。有限实半代数判据也不足以刻画p+2方向。

**边界：** 只排除G加预定有限同余，以及指定实半代数表达；不排除自适应gcd或其他算术编码。没有证明简洁判据不可能。

**原文：** [five_six_intuitive_criteria_and_modular_limits_20260916.md](../../research/prime_arity_padic/five_six_intuitive_criteria_and_modular_limits_20260916.md) · [subcritical_prime_uniform_arithmetic_20260917.md](../../research/prime_arity_padic/subcritical_prime_uniform_arithmetic_20260917.md)

**核验：** `python knowledge/project_knowledge.py verify SUBCRITICAL-LIMITS` 只展示已登记命令及边界，不自动启动计算。

### SIX-EXPLICIT · 六元三重核心G=3与唯一后继

**状态：** 本地文稿已给证明，未独立重审。三重核心G=3且无四重值可解；四重值有模9条件；一般G=1失败出口后剩唯一后继。

**边界：** 一般G=1尚未压成一次性公式；不是所有六元G合法都可解。

**原文：** [six_triple_block_explicit_G3_20260916.md](../../research/prime_arity_padic/six_triple_block_explicit_G3_20260916.md)

**核验：** `python knowledge/project_knowledge.py verify SIX-EXPLICIT` 只展示已登记命令及边界，不自动启动计算。

### FIVE-SUMMARY · 五元：算法已解、静态分类仍未解

**状态：** 解释／综述，非新可达性证明。逐输入判定与最短路径完成；椭圆型真实宏的范数剥离已统一，新增−59／−971子族及跨素数根标签耦合。全五元静态判据及固定D全词逃逸仍未解。

**边界：** 本总结不是所有新证明的独立审核。有限实验、零密度、分形维数和超越性均不能证明静态简单判据不可能。

**原文：** [five_averaging_progress_summary_20260917.md](../../research/prime_arity_padic/five_averaging_progress_summary_20260917.md)

**还应读：** SUBCRITICAL-COMPLETE, FIVE-ESCAPE-OPEN, FIVE-TEMPLATE-ESCAPE, FIVE-DIGITS, FIVE-NORM-SLICE

**核验：** `python knowledge/project_knowledge.py verify FIVE-SUMMARY` 只展示已登记命令及边界，不自动启动计算。

### FIVE-NORM-SLICE · 统一椭圆宏范数剥离、根标签耦合与−59／−971判据

**状态：** 本地文稿已给证明，未独立重审。任意椭圆型真实宏T=WS^ε均由范数赋值保证原位置整块剥离；−11、−59、−971有完整静态子族。Q₁₁非三核m必为5或25 mod30，成功根标签存在跨素数耦合。保留原固定m塔及一般p+2范数子族。

**边界：** 单周期剥离已统一，任意m成功标签及不同周期选择／转换仍未统一；有限组周期范数塔不足全覆盖。m可沿成功步骤增大，不能默认下降。m不是环面D，全词逃逸未解，新证明未独立重审。

**原文：** [five_quadratic_norm_explicit_slice_20260916.md](../../research/prime_arity_padic/five_quadratic_norm_explicit_slice_20260916.md) · [five_quadratic_norm_towers_and_minus59_20260917.md](../../research/prime_arity_padic/five_quadratic_norm_towers_and_minus59_20260917.md)

**导航前提：** SUBCRITICAL-COMPLETE（不是自动抽取的完整证明DAG）

**还应读：** FIVE-NORMAL-FORM, FIVE-DENOMINATORS

**核验：** `python knowledge/project_knowledge.py verify FIVE-NORM-SLICE` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 单周期的整数实现已统一；继续须控制任意m的整体根标签、多个周期之间的转换与选择。排除独立素数筛选和单陪集模型，不排除更一般算术关系。

### FIVE-NORMAL-FORM · 五元完整受限连分数与level15矩阵序

**状态：** 本地文稿已给证明，未独立重审。任意五元通过十对线性表达式进入唯一受限连分数；整数代数为level15序，生成模为u+v≡0 mod5。

**边界：** 群轨道严格大于正词；不存在两分支共同乘法型齐次范数，不排除一般算术条件。

**原文：** [five_complete_arithmetic_normal_form_20260916.md](../../research/prime_arity_padic/five_complete_arithmetic_normal_form_20260916.md)

**导航前提：** SUBCRITICAL-COMPLETE（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-NORMAL-FORM` 只展示已登记命令及边界，不自动启动计算。

### FIVE-FRACTAL · 三进紧集的全部有理点与密度

**状态：** 本地文稿已给证明，未独立重审。有限标记=可解；无限边界有理点恰两轴有限轨道，被模5排除；维数log₂/log₃、每层2^(m+1)−1类。

**边界：** 实稠密、三进零测不等于判定不可能；五元整数盒子密度零不等于固定D有限。

**原文：** [five_padic_fractal_rational_points_20260916.md](../../research/prime_arity_padic/five_padic_fractal_rational_points_20260916.md)

**导航前提：** FIVE-NORMAL-FORM（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-FRACTAL` 只展示已登记命令及边界，不自动启动计算。

### FIVE-DIGITS · 原整数同步三进非正则、精确进位与有理代数对应

**状态：** 本地文稿已给证明，未独立重审。普通斜率及未本原化原五整数的同步三进语言均无固定有限状态判据；h剥位公因子恰gcd(q,4)，二因子总量望远镜消去。保留交换商有理对应。

**边界：** 不排除先算gcd后本原承诺域读位、无界整数寄存器或输入相关算术式；未得G式总判据。换支不是实际平均，新证明未独立重审。

**原文：** [five_digit_obstruction_and_rational_correspondence_20260916.md](../../research/prime_arity_padic/five_digit_obstruction_and_rational_correspondence_20260916.md) · [five_integer_digits_and_carry_20260917.md](../../research/prime_arity_padic/five_integer_digits_and_carry_20260917.md)

**证据／文献记录：** [rational_base_padic_2011_source.json](../../research/prime_arity_padic/five_torus_literature_20260917/rational_base_padic_2011_source.json) · [rational_base_regular_2021_source.json](../../research/prime_arity_padic/five_torus_literature_20260917/rational_base_regular_2021_source.json)

**导航前提：** FIVE-FRACTAL（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-DIGITS` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 当前优先：本原化后的数字规律或输入相关gcd／赋值式；先与完整递归核验。二进约分总量已消去，不能再把它作为独立无界障碍。

### FIVE-TORUS · 统一Q(√5)范数一环面与扭曲平移

**状态：** 本地文稿已给证明，未独立重审。两分支为J(ε^±1α)，3惰性、5分歧；四穿孔曲线及固定S内相邻单位边有限。

**边界：** J不是群同态；相邻边有限不能阻止离开后返回；辅助分母不是物理分母。

**原文：** [five_norm_one_torus_and_twisted_translation_20260917.md](../../research/prime_arity_padic/five_norm_one_torus_and_twisted_translation_20260917.md)

**条件／外部依赖：** ESS定理1.1用于固定S单位方程

**证据／文献记录：** [README.md](../../research/prime_arity_padic/five_torus_literature_20260917/README.md)

**导航前提：** FIVE-DIGITS（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-TORUS` 只展示已登记命令及边界，不自动启动计算。

### FIVE-DENOMINATORS · 精确D、相邻互素、同理想任意近的失败点

**状态：** 本地文稿已给证明，未独立重审。D=|u²+7uv+v²|/5是环面最小分母；相邻D互素，兄弟gcd只可能11；同理想固定局部精度不足。

**边界：** D不单调，不独立决定可解；辅助素数可变化。

**原文：** [five_torus_denominators_and_local_separation_20260917.md](../../research/prime_arity_padic/five_torus_denominators_and_local_separation_20260917.md)

**导航前提：** FIVE-TORUS（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-DENOMINATORS` 只展示已登记命令及边界，不自动启动计算。

### FIVE-UNITS-GROUP · 固定理想单位指数与三进大群闭包

**状态：** 本地文稿已给证明，未独立重审。固定理想候选为α₀ε^(4k)，Z₃指数与h等距；群闭包含PSL₂(Q₃)，对数偏移D=1整数、D>1超越。

**边界：** 大群不替代正半群；指数零密度不推出有限。

**原文：** [five_fixed_ideal_unit_exponents_and_padic_group_20260917.md](../../research/prime_arity_padic/five_fixed_ideal_unit_exponents_and_padic_group_20260917.md)

**条件／外部依赖：** Baker–Brumer，已读正式转述，原1967证明未取得

**导航前提：** FIVE-DENOMINATORS, FIVE-FRACTAL（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-UNITS-GROUP` 只展示已登记命令及边界，不自动启动计算。

### FIVE-SPARSITY · 固定D有效稀疏与固定周期有限返回

**状态：** 本地文稿已给证明，未独立重审。长度L指数区间成功数<4L^log₃2；固定D高度计数为对数高度分数幂；固定正词幂只有有限命中。

**边界：** 不涵盖变词全树；有限返回不自动给有效最后命中界，后续Baker只补固定混合周期。

**原文：** [five_fixed_D_effective_sparsity_and_periodic_return_20260917.md](../../research/prime_arity_padic/five_fixed_D_effective_sparsity_and_periodic_return_20260917.md)

**条件／外部依赖：** ESS；SML为替代有限性论证

**导航前提：** FIVE-UNITS-GROUP（不是自动抽取的完整证明DAG）

**后续更新：** FIVE-TEMPLATE-ESCAPE：由单周期扩为多参数固定模板，另补固定周期有效增长

**核验：** `python knowledge/project_knowledge.py verify FIVE-SPARSITY` 只展示已登记命令及边界，不自动启动计算。

### FIVE-BOUNDED-RUNS · 有界字母切换的有效有限性

**状态：** 本地文稿已给证明，未独立重审。固定D且同方向段数有界时有限并有效；D=1至多两次切换的全长度分类只留三个方向。

**边界：** 小段数应用有精确尾误差证书；任意切换仍未解决，后续有无网格界与模板推广。

**原文：** [five_bounded_switches_and_correspondence_degree_20260917.md](../../research/prime_arity_padic/five_bounded_switches_and_correspondence_degree_20260917.md)

**导航前提：** FIVE-DENOMINATORS（不是自动抽取的完整证明DAG）

**后续更新：** FIVE-HECKE：将一般有效界升级为无网格显式界；FIVE-TEMPLATE-ESCAPE：重复块可混合两字母，覆盖无界切换子族

**核验：** `python knowledge/project_knowledge.py verify FIVE-BOUNDED-RUNS` 只展示已登记命令及边界，不自动启动计算。

### FIVE-HECKE · 显式间隙界与同层共同Hecke二次型

**状态：** 本地文稿已给证明，未独立重审。有界段数给闭式字长界；所有同长度词拉回型整数等价；D=1第一段为v₃(2k+1)+v₃(2k−1)。

**边界：** Aka–Shapira只给整周期分布，不控制终端标记Ce；类信息统一不是全词逃逸。

**原文：** [five_explicit_gap_common_hecke_form_20260917.md](../../research/prime_arity_padic/five_explicit_gap_common_hecke_form_20260917.md)

**条件／外部依赖：** Aka–Shapira用于共同周期；Lucas赋值亦有自足证明

**证据／文献记录：** [switch_hecke_review_20260917.md](../../research/prime_arity_padic/five_torus_literature_20260917/switch_hecke_review_20260917.md)

**导航前提：** FIVE-BOUNDED-RUNS, FIVE-UNITS-GROUP（不是自动抽取的完整证明DAG）

**与旧结果的关系：** FIVE-BOUNDED-RUNS：将一般有效界升级为无网格显式界

**核验：** `python knowledge/project_knowledge.py verify FIVE-HECKE` 只展示已登记命令及边界，不自动启动计算。

### FIVE-TEMPLATE-ESCAPE · 固定多块模板统一逃离小分母

**状态：** 本地文稿已给证明，未独立重审。任意固定U₀V₁^a₁⋯V_r^a_rU_r内，指数独立变化仍统一逃离小D；允许混合块及无界切换。

**边界：** 模板本身变化的全部词仍未覆盖；多模板有限性未给有效截止；固定混合周期另有Baker指数下界。

**原文：** [five_bounded_templates_uniform_escape_20260917.md](../../research/prime_arity_padic/five_bounded_templates_uniform_escape_20260917.md)

**条件／外部依赖：** ESS经极小零子和化格陪集；Baker–Wüstholz正式转述只用于固定周期有效增长

**证据／文献记录：** [uniform_escape_review_20260917.md](../../research/prime_arity_padic/five_torus_literature_20260917/uniform_escape_review_20260917.md)

**导航前提：** FIVE-SPARSITY, FIVE-DENOMINATORS（不是自动抽取的完整证明DAG）

**与旧结果的关系：** FIVE-SPARSITY：由单周期扩为多参数固定模板，另补固定周期有效增长；FIVE-BOUNDED-RUNS：重复块可混合两字母，覆盖无界切换子族

**核验：** `python knowledge/project_knowledge.py verify FIVE-TEMPLATE-ESCAPE` 只展示已登记命令及边界，不自动启动计算。

### FIVE-ESCAPE-OPEN · 固定D全词逃逸与D=1完整分类

**状态：** 开放问题。猜想min_|W|=L D(We)→∞；更小猜想D=1只允许单位指数k=0,±1。

**边界：** 模板定理、零密度、群闭包、有限指数范围实验都不能替代任意词证明。没有证明简单判据不可能。

**原文：** [five_averaging_progress_summary_20260917.md](../../research/prime_arity_padic/five_averaging_progress_summary_20260917.md) · [five_bounded_templates_uniform_escape_20260917.md](../../research/prime_arity_padic/five_bounded_templates_uniform_escape_20260917.md)

**还应读：** FIVE-TEMPLATE-ESCAPE, FIVE-HECKE

**核验：** `python knowledge/project_knowledge.py verify FIVE-ESCAPE-OPEN` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 对不断变化的词模板给一致小范数控制，或构造无限反例族；不得把固定模板的无限并当有限覆盖。
