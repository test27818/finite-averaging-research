# 素数定理与自然统一

[总状态](../STATUS.md) · [接手入口](../START_HERE.md)

原可达性定理已经完成。先看参数覆盖表，区分共同形状、共同收尾、统一启动和已独立审核；表内大参数替代行可与基线行重叠，不是新的互斥证明划分。全参数资源供应可走纤维比较、改变来源或状态相关准备，退化出口不是唯一关卡。

## 当前参数覆盖：启动与收尾分开看

记 n=2p+r。以下同时展示完整基线和明确范围的改进；重叠行是替代关系，不能据一行的共同收尾推断启动也统一。

| 参数范围 | 初始构造 | 收尾 | 残留证据／统一边界 | 来源卡 |
|---|---|---|---|---|
| 奇p≥3；奇数1≤r<p；n=2p+r | 同一边界反射铅笔，包含r=1；启动无83界 | 已证根／深核＋有限对应共同终端 | 此整族不再逐小p启动；原Morris/Serre依赖保留 | [PRIME-ODD-PENCIL](../../research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md) |
| p≥5；r=2；n=2p+2 | 可逆缩放＋三步重叠反射；对当前列选两次CRT数字返回 | 指定载体坐标后接精确同余纤维 | 全小素数有效，无omega(p+1)限制；仍与内部不同启动 | [PRIME-2P2](../../outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md) |
| p≥7；偶数4≤r≤p−3 | 原相邻载体对合与实际逆／根资源 | 原深核与终端；二进表可用PRIME-DYADIC统一替代 | 全参数已证；尚非与r=2、p−1共用一个资源公式 | [PRIME-EVEN-INTERIOR](../../outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md) |
| p≥5；r=p−1；n=3p−1 | 重叠反射族；p=5接明确夹乘，p≥7通式 | 方向、单位与主同余纤维 | 完整解析证明；没有因此消除边界与内部启动差别 | [PRIME-3PM1](../../outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md) |
| p≥83；3≤r<p（覆盖上述偶数内部及r=p−1） | r<r₀用旧载体桥；r≥r₀用共同新载体公式 | 同一根／单位／移动终端；已有深核后可用有限对应 | 共同收尾已合并，启动仍分旧／新载体；r=2不包含 | [PRIME-RETAINED-BRIDGE](../../research/prime_arity_padic/retained_carrier_bridge_and_endpoint_lessons.md) |
| n=3p | 三个等大块，控制level为3 | 真实正运输与零触发 | 独立机制；判据为G的p幂，不能写G=1 | [PRIME-3P](../../outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md) |
| p≥83；r=p+s，1≤s≤9 | §3.3旧三连参数计数，使用前两个输出 | 统一反射、根与终端接口 | 此范围不用小参数表；三段选参尚未合成单一公式 | [PRIME-CRITICAL-CONTROLLER](../../research/prime_arity_padic/critical_band_common_controller.md) |
| p≥83；r=p+s，10≤s≤⌊p/2⌋ | §3.2平衡来源＋相邻输出 | 与紧邻3p及上端相同 | 已合并控制与收尾，来源计数仍不同 | [PRIME-CRITICAL-CONTROLLER](../../research/prime_arity_padic/critical_band_common_controller.md) |
| p≥83；3p/2<r<2p | §3.1按剩余载体选择q=2来源 | 与另外两段相同 | 上半带全覆盖；并非三段启动选参已完全合并 | [PRIME-CRITICAL-CONTROLLER](../../research/prime_arity_padic/critical_band_common_controller.md) |
| 11≤p<83；n=3p+s，1≤s≤9 | 冻结基线162组；独立五返回通式替代其中48组 | direction/binary_unit及特殊辅助已由后续接口替代 | 独立路线仍列114组根资源；不等于已改写并重审基线 | [PRIME-FIVE-RETURNS](../../research/prime_arity_padic/conservation_capacity_and_five_return_supply.md) |
| 5≤p<83其他上半带；p=3单独 | 原完整区间证明；p=5、7用锐界；p=3用三平均直接链 | 按原覆盖表的各已证终端 | 可达性全证；新共同p≥83公式未全参数替代这些分支 | [PRIME-TOTAL](../../outputs/prime_arity/proof.md) |
| n≥4p | 已有整数见证下降；容量不足时接既有算术核心 | 原尾部全参数完成 | 备用改进，不再视为当前可达性缺口 | [PRIME-TAIL-BACKUP](../../research/prime_arity_padic/four_p_tail_optimization.md) |

| ID | 结论 | 状态 |
|---|---|---|
| PRIME-ENDPOINT-GEOMETRY | 2p+1端点：G判别式交环与全部可逆射影轨道 | 本地文稿已给证明，未独立重审 |
| PRIME-TOTAL | 所有奇素数平均的最优最终阈值 | 原证明已完成 |
| PRIME-NATURAL-UNIFICATION | 自然统一的主目标：全参数原位置资源供应 | 开放问题 |
| PRIME-MOVE-MERGE | 任意元数的移动见证—双块入口 | 本地文稿已给证明，未独立重审 |
| PRIME-CARRIER-OBSTRUCTION | 单载体正词的p进Smith形障碍 | 本地文稿已给证明，未独立重审 |
| PRIME-BALANCE | 对称尺度配平与载体更新正常形 | 部分结果／明确范围 |
| PRIME-EVEN-INVERSE | 全部偶载体的一致正向逆 | 本地文稿已给证明，未独立重审 |
| PRIME-OUTPUT-ROOT | 固定来源交换输出产生真实剪切 | 本地文稿已给证明，未独立重审 |
| PRIME-SQUARE-ZERO | 已有深核后的平方零一次同余编译 | 本地文稿已给证明，未独立重审 |
| PRIME-CERTIFICATE-ANATOMY | 旧九偏移证书与p≥83公式的解剖 | 历史方案／已被更宽接口覆盖 |
| PRIME-DYADIC | 以统一列提升替代旧二进轨道表 | 本地文稿已给证明，未独立重审 |
| PRIME-TERMINAL-FAN | 移动终端替代额外单位补充 | 本地文稿已给证明，未独立重审 |
| PRIME-TWO-ROOTS | 两根直接修正列，避免提升整个群 | 本地文稿已给证明，未独立重审 |
| PRIME-SPLIT-COLUMNS | 分裂乘法完成全部方向与二进修补 | 本地文稿已给证明，未独立重审 |
| PRIME-CONSERVATION13 | 守恒交换替代(11,3)辅助13 | 本地文稿已给证明，未独立重审 |
| PRIME-FIVE-RETURNS | 五返回公式替代48组根资源，保留114组 | 本地文稿已给证明，未独立重审 |
| PRIME-COMMON-SHAPE | 临界带共同(p,p,r)形状与整数关系格 | 本地文稿已给证明，未独立重审 |
| PRIME-CRITICAL-CONTROLLER | 跨3p的共同控制器 | 本地文稿已给证明，未独立重审 |
| PRIME-RETAINED-BRIDGE | 旧载体桥接补齐小余量 | 本地文稿已给证明，未独立重审 |
| PRIME-ADELIC | 本原直线的内容余循环与共同CRT | 本地文稿已给证明，未独立重审 |
| PRIME-FIBER | 同行列式纤维与有限精度对应 | 本地文稿已给证明，未独立重审 |
| PRIME-GEOMETRY | 有界纤维整数凸包、根本原性与内容对偶 | 本地文稿已给证明，未独立重审 |
| PRIME-FINITE-TERMINAL | 深核只建一次：有限对应群化与共同终端 | 本地文稿已给证明，未独立重审 |
| PRIME-ODD-PENCIL | 奇数下半区共同边界反射铅笔 | 本地文稿已给证明，未独立重审 |
| PRIME-TAIL-BACKUP | 4p尾部整数化：备用改进及固定池障碍 | 部分结果／明确范围 |
| PRIME-2P2 | 偶数下边界 n=2p+2：状态相关的两次CRT返回 | 原证明已完成 |
| PRIME-EVEN-INTERIOR | 偶数下半带内部 4≤r≤p−3 的完整证明 | 原证明已完成 |
| PRIME-3PM1 | 偶数上边界 n=3p−1：重叠反射完整证明 | 原证明已完成 |
| PRIME-3P | n=3p：三个等大块运输 | 原证明已完成 |

### PRIME-ENDPOINT-GEOMETRY · 2p+1端点：G判别式交环与全部可逆射影轨道

**状态：** 本地文稿已给证明，未独立重审。端点核心G=div_L(v)，且O_(−n)/(sqrt(−n),eta)=Z/G；能量范数局部单位恰G=1。已实现宏群等于PGL₂(R)的模n上三角逆像，全部方向轨道恰按d|n分类；经典尖点可被真实单位倍率合并，各G层在平均p处均稠密。

**边界：** 核心方向按共同尺度分类，不是实际数值上的可逆循环；复用既有Morris／Serre与原位置宏。不能把导子素数都称分歧素数，不能用一般原输入能量判定。不是新阈值、最短路径或全参数高效词提取证明；未独立重审。

**原文：** [endpoint_discriminant_orders_and_G_orbits_20260917.md](../../research/prime_arity_padic/endpoint_discriminant_orders_and_G_orbits_20260917.md)

**条件／外部依赖：** 继承端点统一正向控制器及整数Gamma0包含；一般level使用已核对Morris／Serre，不新增GRH或ESS

**导航前提：** PRIME-TOTAL, G-OBSTRUCTION, EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** SEVEN-GEOMETRY, GEOMETRY-ALL-N, PRIME-NATURAL-UNIFICATION

**与旧结果的关系：** SEVEN-GEOMETRY：将七元的精确宏群与G轨道扩到全部奇2p+1端点；保留七元专属theta/Eisenstein计数，不外推其类数一结论

**核验：** `python knowledge/project_knowledge.py verify PRIME-ENDPOINT-GEOMETRY` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 研究G轨道内真实词的有效提取与尺度／长度界，或把判别式交环接到更多核心的资源供应；不能仅以theta或理想类替代实际宏。

### PRIME-TOTAL · 所有奇素数平均的最优最终阈值

**状态：** 原证明已完成。所有奇素数p：N(p)=2p+1，阈值以上G为p幂充要；N(2)=4。原主证明覆盖表完整。

**边界：** 已完成存在性不等于新统一无证书证明或通用高效群词提取。162组是冻结基线，后续独立简化不自动重写它。

**原文：** [proof.md](../../outputs/prime_arity/proof.md) · [arithmetic_toolkit.md](../../outputs/prime_arity/arithmetic_toolkit.md) · [verification.md](../../outputs/prime_arity/verification.md)

**条件／外部依赖：** Morris有限指数与有理S整数SL₂强同余子群性质；原小参数有限资源证书

**证据／文献记录：** [proof_map.json](../../outputs/prime_arity/proof_map.json)

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-ODD-PENCIL, PRIME-FINITE-TERMINAL, PRIME-ENDPOINT-GEOMETRY

**核验：** `python knowledge/project_knowledge.py verify PRIME-TOTAL` 只展示已登记命令及边界，不自动启动计算。

### PRIME-NATURAL-UNIFICATION · 自然统一的主目标：全参数原位置资源供应

**状态：** 开放问题。原阈值已证。目标是统一2p<n<4p的初始物理资源供应；纤维比较、改变来源、状态相关准备是并列候选策略。奇数下半带已有共同反射。

**边界：** 退化出口不是唯一必经关卡；先有独立真实资源才可使用深核。共同收尾、共同形状与同一选参公式是不同强度。

**原文：** [unified_stable_range_saturation_candidate_20260916.md](../../research/prime_arity_padic/unified_stable_range_saturation_candidate_20260916.md) · [small_parameters_lattice_defects_and_closure_target.md](../../research/prime_arity_padic/small_parameters_lattice_defects_and_closure_target.md)

**还应读：** PRIME-ODD-PENCIL, PRIME-FINITE-TERMINAL, PRIME-FIBER, PRIME-GEOMETRY, PRIME-2P2, PRIME-EVEN-INTERIOR, PRIME-3PM1, PRIME-3P, PRIME-CRITICAL-CONTROLLER

**核验：** `python knowledge/project_knowledge.py verify PRIME-NATURAL-UNIFICATION` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 证明全参数库存内足够的真实作用：可比较计数纤维、改变来源或按状态准备；须接可控终端，不要求所有出口序列终止。

### PRIME-MOVE-MERGE · 任意元数的移动见证—双块入口

**状态：** 本地文稿已给证明，未独立重审。k≥2、n≥2k+1，完整危险素数见证可保留到两个k重块加剩余单点。

**边界：** 入口完整不等于核心内终止；单载体格障碍仍需不同资源。

**原文：** [move_witnesses_then_merge.md](../../research/prime_arity_padic/move_witnesses_then_merge.md)

**还应读：** PRIME-CARRIER-OBSTRUCTION

**核验：** `python knowledge/project_knowledge.py verify PRIME-MOVE-MERGE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-CARRIER-OBSTRUCTION · 单载体正词的p进Smith形障碍

**状态：** 本地文稿已给证明，未独立重审。m≥2差分空间中任意k步单载体词的Smith形为diag(p^−k,1,…,1)，排除全空间非空标量周期。

**边界：** 不排除更小输入像的返回或多载体宏；有限模逆不等于真实有理逆。

**原文：** [carrier_balance_and_uniform_mechanism.md](../../research/prime_arity_padic/carrier_balance_and_uniform_mechanism.md)

**核验：** `python knowledge/project_knowledge.py verify PRIME-CARRIER-OBSTRUCTION` 只展示已登记命令及边界，不自动启动计算。

### PRIME-BALANCE · 对称尺度配平与载体更新正常形

**状态：** 部分结果／明确范围。已有成功分支可提取全系统配平及四步返回正常形；单独对称对角资源不足以给横向控制。

**边界：** 早期4|t缺口已由全偶载体定理补齐；不将本卡旧范围作为当前缺口。

**原文：** [local_proofs_to_global_balance.md](../../research/prime_arity_padic/local_proofs_to_global_balance.md) · [carrier_refresh_normal_form.md](../../research/prime_arity_padic/carrier_refresh_normal_form.md)

**还应读：** PRIME-EVEN-INVERSE

**后续更新：** PRIME-EVEN-INVERSE：补齐原4整除t分支，替代仅部分偶载体的取逆范围

**核验：** `python knowledge/project_knowledge.py verify PRIME-BALANCE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-EVEN-INVERSE · 全部偶载体的一致正向逆

**状态：** 本地文稿已给证明，未独立重审。所有奇素数p、1≤t<p的(p,p,2t)核心都有同一十二步非零标量闭路。

**边界：** 可逆资源不等于完整根群、入口和终端统一。

**原文：** [uniform_even_carrier_inverse.md](../../research/prime_arity_padic/uniform_even_carrier_inverse.md)

**与旧结果的关系：** PRIME-BALANCE：补齐原4整除t分支，替代仅部分偶载体的取逆范围

**核验：** `python knowledge/project_knowledge.py verify PRIME-EVEN-INVERSE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-OUTPUT-ROOT · 固定来源交换输出产生真实剪切

**状态：** 本地文稿已给证明，未独立重审。从已有可逆返回的输出差获得明确非零根，记录模板容量边界。

**边界：** 两矩阵不交换不自动有根；一个根不自动有本原根理想或完整轨道。

**原文：** [output_exchange_produces_roots.md](../../research/prime_arity_padic/output_exchange_produces_roots.md)

**导航前提：** PRIME-EVEN-INVERSE（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify PRIME-OUTPUT-ROOT` 只展示已登记命令及边界，不自动启动计算。

### PRIME-SQUARE-ZERO · 已有深核后的平方零一次同余编译

**状态：** 本地文稿已给证明，未独立重审。在整族根与精确深核已真实存在前提下，把模h²修正压成模h的一项标量同余。

**边界：** 不制造初始根族，不证明资源存在；不得循环依赖深核。

**原文：** [square_zero_hensel_compiler.md](../../research/prime_arity_padic/square_zero_hensel_compiler.md)

**证据／文献记录：** [frozen_compat.py](../../knowledge/frozen_compat.py) · [navigation_migrations.json](../../knowledge/navigation_migrations.json)

**核验：** `python knowledge/project_knowledge.py verify PRIME-SQUARE-ZERO` 只展示已登记命令及边界，不自动启动计算。

### PRIME-CERTIFICATE-ANATOMY · 旧九偏移证书与p≥83公式的解剖

**状态：** 历史方案／已被更宽接口覆盖。解释原162=18×9参数记录的物理计数、根理想、方向与单位字段，以及旧p≥83范围。

**边界：** 最新研究已经删除多项字段；本卡解释冻结基线，不能当最新剩余清单。

**原文：** [certificate_anatomy_and_odd_offsets.md](../../research/prime_arity_padic/certificate_anatomy_and_odd_offsets.md) · [uniform_reflection_formula.md](../../research/prime_arity_padic/uniform_reflection_formula.md)

**还应读：** PRIME-FIVE-RETURNS, PRIME-SPLIT-COLUMNS

**后续更新：** PRIME-TERMINAL-FAN：取消binary_unit字段及97/13特例的终端用途；PRIME-SPLIT-COLUMNS：全部独立direction字段不再需要；PRIME-FIVE-RETURNS：以通式替代48组root资源；162→114仅就此资源清单

**核验：** `python knowledge/project_knowledge.py verify PRIME-CERTIFICATE-ANATOMY` 只展示已登记命令及边界，不自动启动计算。

### PRIME-DYADIC · 以统一列提升替代旧二进轨道表

**状态：** 本地文稿已给证明，未独立重审。旧内部偶余量64、256类表由同一个手写二进列提升引理替代；区分终端控制与物理资源。

**边界：** 当时162组根／方向记录的未替代范围须按后续卡更新。

**原文：** [structural_reassessment_and_uniform_dyadic_orbits.md](../../research/prime_arity_padic/structural_reassessment_and_uniform_dyadic_orbits.md)

**还应读：** PRIME-TWO-ROOTS, PRIME-SPLIT-COLUMNS

**后续更新：** PRIME-TWO-ROOTS：终端改为只修当前列，无需原三共轭浅核

**核验：** `python knowledge/project_knowledge.py verify PRIME-DYADIC` 只展示已登记命令及边界，不自动启动计算。

### PRIME-TERMINAL-FAN · 移动终端替代额外单位补充

**状态：** 本地文稿已给证明，未独立重审。两个／四个终端代替单一目标，删除45组binary_unit及(13,3)的97/13补充用途。

**边界：** 本阶段仍保留root_pairs、direction和(11,3)辅助13，后两者有后续替代。

**原文：** [terminal_fan_replaces_dyadic_units.md](../../research/prime_arity_padic/terminal_fan_replaces_dyadic_units.md)

**与旧结果的关系：** PRIME-CERTIFICATE-ANATOMY：取消binary_unit字段及97/13特例的终端用途

**核验：** `python knowledge/project_knowledge.py verify PRIME-TERMINAL-FAN` 只展示已登记命令及边界，不自动启动计算。

### PRIME-TWO-ROOTS · 两根直接修正列，避免提升整个群

**状态：** 本地文稿已给证明，未独立重审。把sl₂三方向目标降为当前列二维作用；116组direction可由旧根生成，46组当时保留二进条件。

**边界：** 不移除初始根资源与深核；46组后由分裂乘法完成。

**原文：** [two_root_column_completion.md](../../research/prime_arity_padic/two_root_column_completion.md)

**导航前提：** PRIME-TERMINAL-FAN（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-DYADIC：终端改为只修当前列，无需原三共轭浅核

**后续更新：** PRIME-SPLIT-COLUMNS：补齐剩余46组方向；取消其迹条件与Smith本原准备

**核验：** `python knowledge/project_knowledge.py verify PRIME-TWO-ROOTS` 只展示已登记命令及边界，不自动启动计算。

### PRIME-SPLIT-COLUMNS · 分裂乘法完成全部方向与二进修补

**状态：** 本地文稿已给证明，未独立重审。旧等块互补混合的对角乘法完成162组列输送，不再需要direction、binary_unit或二进迹条件。

**边界：** 根反射、深核和物理供应仍须独立存在；(11,3)辅助13由下一卡处理。

**原文：** [split_torus_completes_all_directions.md](../../research/prime_arity_padic/split_torus_completes_all_directions.md)

**导航前提：** PRIME-TWO-ROOTS（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-TWO-ROOTS：补齐剩余46组方向；取消其迹条件与Smith本原准备；PRIME-CERTIFICATE-ANATOMY：全部独立direction字段不再需要

**后续更新：** PRIME-CONSERVATION13：补去仍保留的(11,3)辅助13

**核验：** `python knowledge/project_knowledge.py verify PRIME-SPLIT-COLUMNS` 只展示已登记命令及边界，不自动启动计算。

### PRIME-CONSERVATION13 · 守恒交换替代(11,3)辅助13

**状态：** 本地文稿已给证明，未独立重审。同来源输出守恒关系直接给U(−36)，接横向反射与终端，删除辅助13特殊群计算。

**边界：** 局部修复不等于全部根表移除。

**原文：** [conservation_exchange_removes_auxiliary13.md](../../research/prime_arity_padic/conservation_exchange_removes_auxiliary13.md)

**导航前提：** PRIME-SPLIT-COLUMNS（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-SPLIT-COLUMNS：补去仍保留的(11,3)辅助13

**核验：** `python knowledge/project_knowledge.py verify PRIME-CONSERVATION13` 只展示已登记命令及边界，不自动启动计算。

### PRIME-FIVE-RETURNS · 五返回公式替代48组根资源，保留114组

**状态：** 本地文稿已给证明，未独立重审。一般容量公式与守恒n根供应两组横向系数；对原九偏移资源表替代48组，列出114组剩余。

**边界：** 114是本独立改进对物理根资源的剩余，不是重写冻结主证明后的完整独立审计计数；s>p/2该模板有障碍。

**原文：** [conservation_capacity_and_five_return_supply.md](../../research/prime_arity_padic/conservation_capacity_and_five_return_supply.md)

**导航前提：** PRIME-CONSERVATION13（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-CERTIFICATE-ANATOMY：以通式替代48组root资源；162→114仅就此资源清单

**核验：** `python knowledge/project_knowledge.py verify PRIME-FIVE-RETURNS` 只展示已登记命令及边界，不自动启动计算。

### PRIME-COMMON-SHAPE · 临界带共同(p,p,r)形状与整数关系格

**状态：** 本地文稿已给证明，未独立重审。整个2p<n<4p可进入共同形状；固定来源的迹零输出关系格及有效方向可显式算出。

**边界：** 无界关系格的像不保证容量内可用移动；共同形状不等于全参数终止。

**原文：** [common_shape_integer_relations_and_mainstream_structure.md](../../research/prime_arity_padic/common_shape_integer_relations_and_mainstream_structure.md)

**核验：** `python knowledge/project_knowledge.py verify PRIME-COMMON-SHAPE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-CRITICAL-CONTROLLER · 跨3p的共同控制器

**状态：** 本地文稿已给证明，未独立重审。p≥83、新载体r≥r₀(p)的上下半带接同一根、单位及移动终端接口。

**边界：** 本页r₀是新载体自身范围；小r已由旧载体桥接，不可再列整条立方根缺口。

**原文：** [critical_band_common_controller.md](../../research/prime_arity_padic/critical_band_common_controller.md)

**导航前提：** PRIME-COMMON-SHAPE, PRIME-SPLIT-COLUMNS（不是自动抽取的完整证明DAG）

**后续更新：** PRIME-RETAINED-BRIDGE：补齐其r<r₀条带，不再把立方根宽度看作当前缺口

**核验：** `python knowledge/project_knowledge.py verify PRIME-CRITICAL-CONTROLLER` 只展示已登记命令及边界，不自动启动计算。

### PRIME-RETAINED-BRIDGE · 旧载体桥接补齐小余量

**状态：** 本地文稿已给证明，未独立重审。p≥83、3≤r<2p、r≠p均可接同一收尾；r=1接旧端点，r=2保留CRT，r=p接等块。

**边界：** 未消除小p全部物理供应；r=1的统一启动又有后续奇数铅笔。

**原文：** [retained_carrier_bridge_and_endpoint_lessons.md](../../research/prime_arity_padic/retained_carrier_bridge_and_endpoint_lessons.md)

**导航前提：** PRIME-CRITICAL-CONTROLLER（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-CRITICAL-CONTROLLER：补齐其r<r₀条带，不再把立方根宽度看作当前缺口

**后续更新：** PRIME-FINITE-TERMINAL：统一已有深核后的终端接口，取消逐数字取逆／扩环要求；PRIME-ODD-PENCIL：奇数下半带包括端点改为统一启动，不再依赖83

**核验：** `python knowledge/project_knowledge.py verify PRIME-RETAINED-BRIDGE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-ADELIC · 本原直线的内容余循环与共同CRT

**状态：** 本地文稿已给证明，未独立重审。把本原化的局部内容、均值标记及两端点CRT准备接到共同格描述。

**边界：** 阿代尔语言不会供应尚缺的物理返回；旧r=1启动差异按奇数铅笔更新。

**原文：** [adelic_primitive_lines_and_common_endpoint_preparation.md](../../research/prime_arity_padic/adelic_primitive_lines_and_common_endpoint_preparation.md)

**后续更新：** PRIME-ODD-PENCIL：端点与奇数内部的资源启动差异已由共同反射替代

**核验：** `python knowledge/project_knowledge.py verify PRIME-ADELIC` 只展示已登记命令及边界，不自动启动计算。

### PRIME-FIBER · 同行列式纤维与有限精度对应

**状态：** 本地文稿已给证明，未独立重审。有效作用格(n/g)Z；偶4≤r≤2p/5、奇5≤r≤p/5有直接根；Q|det A|精度记录本原输出。

**边界：** 深核必须先真实实现；有限对应图存在不等于其终端全覆盖。

**原文：** [determinant_fibers_and_finite_lattice_correspondences.md](../../research/prime_arity_padic/determinant_fibers_and_finite_lattice_correspondences.md)

**导航前提：** PRIME-COMMON-SHAPE（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify PRIME-FIBER` 只展示已登记命令及边界，不自动启动计算。

### PRIME-GEOMETRY · 有界纤维整数凸包、根本原性与内容对偶

**状态：** 本地文稿已给证明，未独立重审。固定非零行列式纤维的整数凸包维数控制可生成根格；二维得到本原步长；内容与伴随对偶。

**边界：** 实多边形大不等于任意小库存有资源；未完成全参数无证书存在性。

**原文：** [global_structure_and_bounded_fiber_geometry_20260916.md](../../research/prime_arity_padic/global_structure_and_bounded_fiber_geometry_20260916.md)

**证据／文献记录：** [source_index.md](../../research/prime_arity_padic/global_structure_investigation_20260916/source_index.md)

**导航前提：** PRIME-FIBER（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify PRIME-GEOMETRY` 只展示已登记命令及边界，不自动启动计算。

### PRIME-FINITE-TERMINAL · 深核只建一次：有限对应群化与共同终端

**状态：** 本地文稿已给证明，未独立重审。已有真实深核，行列式与控制模数互素时，有限正向对应轨道等于明确有限群轨道；终端无需反复扩环。

**边界：** 不供应初始根与深核；共享坏因子的行列式不自动覆盖。

**原文：** [finite_orbit_completion_without_ring_extension.md](../../research/prime_arity_padic/finite_orbit_completion_without_ring_extension.md)

**导航前提：** PRIME-GEOMETRY, PRIME-SPLIT-COLUMNS（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-RETAINED-BRIDGE：统一已有深核后的终端接口，取消逐数字取逆／扩环要求

**核验：** `python knowledge/project_knowledge.py verify PRIME-FINITE-TERMINAL` 只展示已登记命令及边界，不自动启动计算。

### PRIME-ODD-PENCIL · 奇数下半区共同边界反射铅笔

**状态：** 本地文稿已给证明，未独立重审。所有奇素数p≥3、全部奇数1≤r<p，用同一两组三步反射及两步反射取得根、深核与终端。包含r=1，无83界。

**边界：** 偶数余量、3p及上半带没有因此统一；Morris/Serre等原依赖仍保留。

**原文：** [odd_lower_band_boundary_reflection_pencil_20260916.md](../../research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md)

**导航前提：** PRIME-FINITE-TERMINAL, EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-RETAINED-BRIDGE：奇数下半带包括端点改为统一启动，不再依赖83；PRIME-ADELIC：端点与奇数内部的资源启动差异已由共同反射替代

**核验：** `python knowledge/project_knowledge.py verify PRIME-ODD-PENCIL` 只展示已登记命令及边界，不自动启动计算。

### PRIME-TAIL-BACKUP · 4p尾部整数化：备用改进及固定池障碍

**状态：** 部分结果／明确范围。原n≥4p已全证；本稿分析见证预算、双重值恢复与固定双块池策略的不可能范围。

**边界：** 不构成2p附近统一突破；没有发现必须重做原尾部正确性的理由。

**原文：** [four_p_tail_optimization.md](../../research/prime_arity_padic/four_p_tail_optimization.md)

**还应读：** PRIME-NATURAL-UNIFICATION

**核验：** `python knowledge/project_knowledge.py verify PRIME-TAIL-BACKUP` 只展示已登记命令及边界，不自动启动计算。

### PRIME-2P2 · 偶数下边界 n=2p+2：状态相关的两次CRT返回

**状态：** 原证明已完成。全部素数p≥5、n=2p+2的完整G=1判据；无需omega(p+1)限制。

**边界：** 原文的“上方九偏移仍未解”是历史状态；本边界已完整，但不等于内部偶数启动已经同构。

**原文：** [prime_arity_two_p_plus_two_uniform.md](../../outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md)

**条件／外部依赖：** 原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-RETAINED-BRIDGE

**核验：** `python knowledge/project_knowledge.py verify PRIME-2P2` 只展示已登记命令及边界，不自动启动计算。

### PRIME-EVEN-INTERIOR · 偶数下半带内部 4≤r≤p−3 的完整证明

**状态：** 原证明已完成。全部p≥7、偶数4≤r≤p−3，n=2p+r全输入G=1充要。

**边界：** 不承担r=2及r=p−1；这两条边界有独立完整卡。旧二进表可由PRIME-DYADIC替代，不等于启动全部统一。

**原文：** [prime_arity_even_interior_completion.md](../../outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md)

**条件／外部依赖：** 原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-RETAINED-BRIDGE

**核验：** `python knowledge/project_knowledge.py verify PRIME-EVEN-INTERIOR` 只展示已登记命令及边界，不自动启动计算。

### PRIME-3PM1 · 偶数上边界 n=3p−1：重叠反射完整证明

**状态：** 原证明已完成。全部素数p≥5、n=3p−1的完整G=1判据；p≥7通式，p=5有显式夹乘。

**边界：** 两条偶数边界均已完成；本卡并未宣称与r=2及内部是同一资源公式。

**原文：** [prime_arity_three_p_minus_one_completion.md](../../outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md)

**条件／外部依赖：** 原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-RETAINED-BRIDGE

**核验：** `python knowledge/project_knowledge.py verify PRIME-3PM1` 只展示已登记命令及边界，不自动启动计算。

### PRIME-3P · n=3p：三个等大块运输

**状态：** 原证明已完成。n=3p的完整判据允许G为p幂；等大三块具有独立的真实运输／终端机制。

**边界：** 此处不可简写G=1；本原重数改变，未由r≠p的共同控制器替代。

**原文：** [prime_arity_middle_band_structure.md](../../outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md)

**条件／外部依赖：** 原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-RETAINED-BRIDGE

**核验：** `python knowledge/project_knowledge.py verify PRIME-3P` 只展示已登记命令及边界，不自动启动计算。
