# 工作材料、历次快照及旧目录完整附卷 · 第3分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [素数定理与自然统一](#doc-66296cf1c816)
- [阈值以下与五元算术](#doc-533f52f161f3)
- [三平均全维数与几何](#doc-6646d5da9f32)
- [成果与研究索引](#doc-24a8b54a7709)
- [算法、复杂度与测试集](#doc-5a9f1981beef)
- [一般元数与合数研究](#doc-f00c7dd4ea77)
- [合数元数实例](#doc-0284ea9ce528)
- [素数平均：当前证明入口](#doc-87b7960b8383)
- [小素数实例与历史证据](#doc-7e8635e35480)
- [素数主证明技术附录](#doc-59c3b8d08b76)
- [2p到3p：全输入入口与完成证明](#doc-f07df728cbbe)
- [尾部上界与最优性下界](#doc-194ac5f2a052)
- [3p以上：核心、反射与完成证明](#doc-afc8ff23d0fd)
- [素数证明的结构与简化](#doc-7bd774674840)
- [已使用的核心与均值格工具](#doc-6a9fda16e26c)
- [三平均：直接证明与原算术路线](#doc-57cbdfec5f0e)
- [三平均旧算术实例](#doc-3ff251530145)
- [三平均直接证明与小基例](#doc-6512624ce2ea)
- [独立研究入口](#doc-1f00cb7484b5)
- [五元环面研究的外部定理记录](#doc-4444d71b4138)
- [七元算术几何：实际阅读、外部接口与自足证明](#doc-292e4ad8ae5c)
- [计算材料与核验入口](#doc-c244d247ecef)
- [Arena三平均网页审阅](#doc-ef29dd2e6627)

---

<a id="doc-66296cf1c816"></a>

## 原文导签：素数定理与自然统一

来源：`knowledge/topics/prime.md` · [逐字节原样副本](../sources/knowledge/topics/prime.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-66296cf1c816 -->
# 素数定理与自然统一

[总状态](../sources/knowledge/STATUS.md) · [接手入口](../sources/knowledge/START_HERE.md)

原可达性定理已经完成。先看参数覆盖表，区分共同形状、共同收尾、统一启动和已独立审核；表内大参数替代行可与基线行重叠，不是新的互斥证明划分。全参数资源供应可走纤维比较、改变来源或状态相关准备，退化出口不是唯一关卡。

## 当前参数覆盖：启动与收尾分开看

记 n=2p+r。以下同时展示完整基线和明确范围的改进；重叠行是替代关系，不能据一行的共同收尾推断启动也统一。

| 参数范围 | 初始构造 | 收尾 | 残留证据／统一边界 | 来源卡 |
|---|---|---|---|---|
| 奇p≥3；奇数1≤r<p；n=2p+r | 同一边界反射铅笔，包含r=1；启动无83界 | 已证根／深核＋有限对应共同终端 | 此整族不再逐小p启动；原Morris/Serre依赖保留 | [PRIME-ODD-PENCIL](../sources/research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md) |
| p≥5；r=2；n=2p+2 | 可逆缩放＋三步重叠反射；对当前列选两次CRT数字返回 | 指定载体坐标后接精确同余纤维 | 全小素数有效，无omega(p+1)限制；仍与内部不同启动 | [PRIME-2P2](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md) |
| p≥7；偶数4≤r≤p−3 | 原相邻载体对合与实际逆／根资源 | 原深核与终端；二进表可用PRIME-DYADIC统一替代 | 全参数已证；尚非与r=2、p−1共用一个资源公式 | [PRIME-EVEN-INTERIOR](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md) |
| p≥5；r=p−1；n=3p−1 | 重叠反射族；p=5接明确夹乘，p≥7通式 | 方向、单位与主同余纤维 | 完整解析证明；没有因此消除边界与内部启动差别 | [PRIME-3PM1](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md) |
| p≥83；3≤r<p（覆盖上述偶数内部及r=p−1） | r<r₀用旧载体桥；r≥r₀用共同新载体公式 | 同一根／单位／移动终端；已有深核后可用有限对应 | 共同收尾已合并，启动仍分旧／新载体；r=2不包含 | [PRIME-RETAINED-BRIDGE](../sources/research/prime_arity_padic/retained_carrier_bridge_and_endpoint_lessons.md) |
| n=3p | 三个等大块，控制level为3 | 真实正运输与零触发 | 独立机制；判据为G的p幂，不能写G=1 | [PRIME-3P](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md) |
| p≥83；r=p+s，1≤s≤9 | §3.3旧三连参数计数，使用前两个输出 | 统一反射、根与终端接口 | 此范围不用小参数表；三段选参尚未合成单一公式 | [PRIME-CRITICAL-CONTROLLER](../sources/research/prime_arity_padic/critical_band_common_controller.md) |
| p≥83；r=p+s，10≤s≤⌊p/2⌋ | §3.2平衡来源＋相邻输出 | 与紧邻3p及上端相同 | 已合并控制与收尾，来源计数仍不同 | [PRIME-CRITICAL-CONTROLLER](../sources/research/prime_arity_padic/critical_band_common_controller.md) |
| p≥83；3p/2<r<2p | §3.1按剩余载体选择q=2来源 | 与另外两段相同 | 上半带全覆盖；并非三段启动选参已完全合并 | [PRIME-CRITICAL-CONTROLLER](../sources/research/prime_arity_padic/critical_band_common_controller.md) |
| 11≤p<83；n=3p+s，1≤s≤9 | 冻结基线162组；独立五返回通式替代其中48组 | direction/binary_unit及特殊辅助已由后续接口替代 | 独立路线仍列114组根资源；不等于已改写并重审基线 | [PRIME-FIVE-RETURNS](../sources/research/prime_arity_padic/conservation_capacity_and_five_return_supply.md) |
| 5≤p<83其他上半带；p=3单独 | 原完整区间证明；p=5、7用锐界；p=3用三平均直接链 | 按原覆盖表的各已证终端 | 可达性全证；新共同p≥83公式未全参数替代这些分支 | [PRIME-TOTAL](../sources/outputs/prime_arity/proof.md) |
| n≥4p | 已有整数见证下降；容量不足时接既有算术核心 | 原尾部全参数完成 | 备用改进，不再视为当前可达性缺口 | [PRIME-TAIL-BACKUP](../sources/research/prime_arity_padic/four_p_tail_optimization.md) |

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

**原文：** [endpoint_discriminant_orders_and_G_orbits_20260917.md](../sources/research/prime_arity_padic/endpoint_discriminant_orders_and_G_orbits_20260917.md)

**条件／外部依赖：** 继承端点统一正向控制器及整数Gamma0包含；一般level使用已核对Morris／Serre，不新增GRH或ESS

**导航前提：** PRIME-TOTAL, G-OBSTRUCTION, EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** SEVEN-GEOMETRY, GEOMETRY-ALL-N, PRIME-NATURAL-UNIFICATION

**与旧结果的关系：** SEVEN-GEOMETRY：将七元的精确宏群与G轨道扩到全部奇2p+1端点；保留七元专属theta/Eisenstein计数，不外推其类数一结论

**核验：** `python knowledge/project_knowledge.py verify PRIME-ENDPOINT-GEOMETRY` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 研究G轨道内真实词的有效提取与尺度／长度界，或把判别式交环接到更多核心的资源供应；不能仅以theta或理想类替代实际宏。

### PRIME-TOTAL · 所有奇素数平均的最优最终阈值

**状态：** 原证明已完成。所有奇素数p：N(p)=2p+1，阈值以上G为p幂充要；N(2)=4。原主证明覆盖表完整。

**边界：** 已完成存在性不等于新统一无证书证明或通用高效群词提取。162组是冻结基线，后续独立简化不自动重写它。

**原文：** [proof.md](../sources/outputs/prime_arity/proof.md) · [arithmetic_toolkit.md](../sources/outputs/prime_arity/arithmetic_toolkit.md) · [verification.md](../sources/outputs/prime_arity/verification.md)

**条件／外部依赖：** Morris有限指数与有理S整数SL₂强同余子群性质；原小参数有限资源证书

**证据／文献记录：** [proof_map.json](../sources/outputs/prime_arity/proof_map.json)

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-ODD-PENCIL, PRIME-FINITE-TERMINAL, PRIME-ENDPOINT-GEOMETRY

**核验：** `python knowledge/project_knowledge.py verify PRIME-TOTAL` 只展示已登记命令及边界，不自动启动计算。

### PRIME-NATURAL-UNIFICATION · 自然统一的主目标：全参数原位置资源供应

**状态：** 开放问题。原阈值已证。目标是统一2p<n<4p的初始物理资源供应；纤维比较、改变来源、状态相关准备是并列候选策略。奇数下半带已有共同反射。

**边界：** 退化出口不是唯一必经关卡；先有独立真实资源才可使用深核。共同收尾、共同形状与同一选参公式是不同强度。

**原文：** [unified_stable_range_saturation_candidate_20260916.md](../sources/research/prime_arity_padic/unified_stable_range_saturation_candidate_20260916.md) · [small_parameters_lattice_defects_and_closure_target.md](../sources/research/prime_arity_padic/small_parameters_lattice_defects_and_closure_target.md)

**还应读：** PRIME-ODD-PENCIL, PRIME-FINITE-TERMINAL, PRIME-FIBER, PRIME-GEOMETRY, PRIME-2P2, PRIME-EVEN-INTERIOR, PRIME-3PM1, PRIME-3P, PRIME-CRITICAL-CONTROLLER

**核验：** `python knowledge/project_knowledge.py verify PRIME-NATURAL-UNIFICATION` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 证明全参数库存内足够的真实作用：可比较计数纤维、改变来源或按状态准备；须接可控终端，不要求所有出口序列终止。

### PRIME-MOVE-MERGE · 任意元数的移动见证—双块入口

**状态：** 本地文稿已给证明，未独立重审。k≥2、n≥2k+1，完整危险素数见证可保留到两个k重块加剩余单点。

**边界：** 入口完整不等于核心内终止；单载体格障碍仍需不同资源。

**原文：** [move_witnesses_then_merge.md](../sources/research/prime_arity_padic/move_witnesses_then_merge.md)

**还应读：** PRIME-CARRIER-OBSTRUCTION

**核验：** `python knowledge/project_knowledge.py verify PRIME-MOVE-MERGE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-CARRIER-OBSTRUCTION · 单载体正词的p进Smith形障碍

**状态：** 本地文稿已给证明，未独立重审。m≥2差分空间中任意k步单载体词的Smith形为diag(p^−k,1,…,1)，排除全空间非空标量周期。

**边界：** 不排除更小输入像的返回或多载体宏；有限模逆不等于真实有理逆。

**原文：** [carrier_balance_and_uniform_mechanism.md](../sources/research/prime_arity_padic/carrier_balance_and_uniform_mechanism.md)

**核验：** `python knowledge/project_knowledge.py verify PRIME-CARRIER-OBSTRUCTION` 只展示已登记命令及边界，不自动启动计算。

### PRIME-BALANCE · 对称尺度配平与载体更新正常形

**状态：** 部分结果／明确范围。已有成功分支可提取全系统配平及四步返回正常形；单独对称对角资源不足以给横向控制。

**边界：** 早期4|t缺口已由全偶载体定理补齐；不将本卡旧范围作为当前缺口。

**原文：** [local_proofs_to_global_balance.md](../sources/research/prime_arity_padic/local_proofs_to_global_balance.md) · [carrier_refresh_normal_form.md](../sources/research/prime_arity_padic/carrier_refresh_normal_form.md)

**还应读：** PRIME-EVEN-INVERSE

**后续更新：** PRIME-EVEN-INVERSE：补齐原4整除t分支，替代仅部分偶载体的取逆范围

**核验：** `python knowledge/project_knowledge.py verify PRIME-BALANCE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-EVEN-INVERSE · 全部偶载体的一致正向逆

**状态：** 本地文稿已给证明，未独立重审。所有奇素数p、1≤t<p的(p,p,2t)核心都有同一十二步非零标量闭路。

**边界：** 可逆资源不等于完整根群、入口和终端统一。

**原文：** [uniform_even_carrier_inverse.md](../sources/research/prime_arity_padic/uniform_even_carrier_inverse.md)

**与旧结果的关系：** PRIME-BALANCE：补齐原4整除t分支，替代仅部分偶载体的取逆范围

**核验：** `python knowledge/project_knowledge.py verify PRIME-EVEN-INVERSE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-OUTPUT-ROOT · 固定来源交换输出产生真实剪切

**状态：** 本地文稿已给证明，未独立重审。从已有可逆返回的输出差获得明确非零根，记录模板容量边界。

**边界：** 两矩阵不交换不自动有根；一个根不自动有本原根理想或完整轨道。

**原文：** [output_exchange_produces_roots.md](../sources/research/prime_arity_padic/output_exchange_produces_roots.md)

**导航前提：** PRIME-EVEN-INVERSE（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify PRIME-OUTPUT-ROOT` 只展示已登记命令及边界，不自动启动计算。

### PRIME-SQUARE-ZERO · 已有深核后的平方零一次同余编译

**状态：** 本地文稿已给证明，未独立重审。在整族根与精确深核已真实存在前提下，把模h²修正压成模h的一项标量同余。

**边界：** 不制造初始根族，不证明资源存在；不得循环依赖深核。

**原文：** [square_zero_hensel_compiler.md](../sources/research/prime_arity_padic/square_zero_hensel_compiler.md)

**证据／文献记录：** [frozen_compat.py](../sources/knowledge/frozen_compat.py) · [navigation_migrations.json](../sources/knowledge/navigation_migrations.json)

**核验：** `python knowledge/project_knowledge.py verify PRIME-SQUARE-ZERO` 只展示已登记命令及边界，不自动启动计算。

### PRIME-CERTIFICATE-ANATOMY · 旧九偏移证书与p≥83公式的解剖

**状态：** 历史方案／已被更宽接口覆盖。解释原162=18×9参数记录的物理计数、根理想、方向与单位字段，以及旧p≥83范围。

**边界：** 最新研究已经删除多项字段；本卡解释冻结基线，不能当最新剩余清单。

**原文：** [certificate_anatomy_and_odd_offsets.md](../sources/research/prime_arity_padic/certificate_anatomy_and_odd_offsets.md) · [uniform_reflection_formula.md](../sources/research/prime_arity_padic/uniform_reflection_formula.md)

**还应读：** PRIME-FIVE-RETURNS, PRIME-SPLIT-COLUMNS

**后续更新：** PRIME-TERMINAL-FAN：取消binary_unit字段及97/13特例的终端用途；PRIME-SPLIT-COLUMNS：全部独立direction字段不再需要；PRIME-FIVE-RETURNS：以通式替代48组root资源；162→114仅就此资源清单

**核验：** `python knowledge/project_knowledge.py verify PRIME-CERTIFICATE-ANATOMY` 只展示已登记命令及边界，不自动启动计算。

### PRIME-DYADIC · 以统一列提升替代旧二进轨道表

**状态：** 本地文稿已给证明，未独立重审。旧内部偶余量64、256类表由同一个手写二进列提升引理替代；区分终端控制与物理资源。

**边界：** 当时162组根／方向记录的未替代范围须按后续卡更新。

**原文：** [structural_reassessment_and_uniform_dyadic_orbits.md](../sources/research/prime_arity_padic/structural_reassessment_and_uniform_dyadic_orbits.md)

**还应读：** PRIME-TWO-ROOTS, PRIME-SPLIT-COLUMNS

**后续更新：** PRIME-TWO-ROOTS：终端改为只修当前列，无需原三共轭浅核

**核验：** `python knowledge/project_knowledge.py verify PRIME-DYADIC` 只展示已登记命令及边界，不自动启动计算。

### PRIME-TERMINAL-FAN · 移动终端替代额外单位补充

**状态：** 本地文稿已给证明，未独立重审。两个／四个终端代替单一目标，删除45组binary_unit及(13,3)的97/13补充用途。

**边界：** 本阶段仍保留root_pairs、direction和(11,3)辅助13，后两者有后续替代。

**原文：** [terminal_fan_replaces_dyadic_units.md](../sources/research/prime_arity_padic/terminal_fan_replaces_dyadic_units.md)

**与旧结果的关系：** PRIME-CERTIFICATE-ANATOMY：取消binary_unit字段及97/13特例的终端用途

**核验：** `python knowledge/project_knowledge.py verify PRIME-TERMINAL-FAN` 只展示已登记命令及边界，不自动启动计算。

### PRIME-TWO-ROOTS · 两根直接修正列，避免提升整个群

**状态：** 本地文稿已给证明，未独立重审。把sl₂三方向目标降为当前列二维作用；116组direction可由旧根生成，46组当时保留二进条件。

**边界：** 不移除初始根资源与深核；46组后由分裂乘法完成。

**原文：** [two_root_column_completion.md](../sources/research/prime_arity_padic/two_root_column_completion.md)

**导航前提：** PRIME-TERMINAL-FAN（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-DYADIC：终端改为只修当前列，无需原三共轭浅核

**后续更新：** PRIME-SPLIT-COLUMNS：补齐剩余46组方向；取消其迹条件与Smith本原准备

**核验：** `python knowledge/project_knowledge.py verify PRIME-TWO-ROOTS` 只展示已登记命令及边界，不自动启动计算。

### PRIME-SPLIT-COLUMNS · 分裂乘法完成全部方向与二进修补

**状态：** 本地文稿已给证明，未独立重审。旧等块互补混合的对角乘法完成162组列输送，不再需要direction、binary_unit或二进迹条件。

**边界：** 根反射、深核和物理供应仍须独立存在；(11,3)辅助13由下一卡处理。

**原文：** [split_torus_completes_all_directions.md](../sources/research/prime_arity_padic/split_torus_completes_all_directions.md)

**导航前提：** PRIME-TWO-ROOTS（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-TWO-ROOTS：补齐剩余46组方向；取消其迹条件与Smith本原准备；PRIME-CERTIFICATE-ANATOMY：全部独立direction字段不再需要

**后续更新：** PRIME-CONSERVATION13：补去仍保留的(11,3)辅助13

**核验：** `python knowledge/project_knowledge.py verify PRIME-SPLIT-COLUMNS` 只展示已登记命令及边界，不自动启动计算。

### PRIME-CONSERVATION13 · 守恒交换替代(11,3)辅助13

**状态：** 本地文稿已给证明，未独立重审。同来源输出守恒关系直接给U(−36)，接横向反射与终端，删除辅助13特殊群计算。

**边界：** 局部修复不等于全部根表移除。

**原文：** [conservation_exchange_removes_auxiliary13.md](../sources/research/prime_arity_padic/conservation_exchange_removes_auxiliary13.md)

**导航前提：** PRIME-SPLIT-COLUMNS（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-SPLIT-COLUMNS：补去仍保留的(11,3)辅助13

**核验：** `python knowledge/project_knowledge.py verify PRIME-CONSERVATION13` 只展示已登记命令及边界，不自动启动计算。

### PRIME-FIVE-RETURNS · 五返回公式替代48组根资源，保留114组

**状态：** 本地文稿已给证明，未独立重审。一般容量公式与守恒n根供应两组横向系数；对原九偏移资源表替代48组，列出114组剩余。

**边界：** 114是本独立改进对物理根资源的剩余，不是重写冻结主证明后的完整独立审计计数；s>p/2该模板有障碍。

**原文：** [conservation_capacity_and_five_return_supply.md](../sources/research/prime_arity_padic/conservation_capacity_and_five_return_supply.md)

**导航前提：** PRIME-CONSERVATION13（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-CERTIFICATE-ANATOMY：以通式替代48组root资源；162→114仅就此资源清单

**核验：** `python knowledge/project_knowledge.py verify PRIME-FIVE-RETURNS` 只展示已登记命令及边界，不自动启动计算。

### PRIME-COMMON-SHAPE · 临界带共同(p,p,r)形状与整数关系格

**状态：** 本地文稿已给证明，未独立重审。整个2p<n<4p可进入共同形状；固定来源的迹零输出关系格及有效方向可显式算出。

**边界：** 无界关系格的像不保证容量内可用移动；共同形状不等于全参数终止。

**原文：** [common_shape_integer_relations_and_mainstream_structure.md](../sources/research/prime_arity_padic/common_shape_integer_relations_and_mainstream_structure.md)

**核验：** `python knowledge/project_knowledge.py verify PRIME-COMMON-SHAPE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-CRITICAL-CONTROLLER · 跨3p的共同控制器

**状态：** 本地文稿已给证明，未独立重审。p≥83、新载体r≥r₀(p)的上下半带接同一根、单位及移动终端接口。

**边界：** 本页r₀是新载体自身范围；小r已由旧载体桥接，不可再列整条立方根缺口。

**原文：** [critical_band_common_controller.md](../sources/research/prime_arity_padic/critical_band_common_controller.md)

**导航前提：** PRIME-COMMON-SHAPE, PRIME-SPLIT-COLUMNS（不是自动抽取的完整证明DAG）

**后续更新：** PRIME-RETAINED-BRIDGE：补齐其r<r₀条带，不再把立方根宽度看作当前缺口

**核验：** `python knowledge/project_knowledge.py verify PRIME-CRITICAL-CONTROLLER` 只展示已登记命令及边界，不自动启动计算。

### PRIME-RETAINED-BRIDGE · 旧载体桥接补齐小余量

**状态：** 本地文稿已给证明，未独立重审。p≥83、3≤r<2p、r≠p均可接同一收尾；r=1接旧端点，r=2保留CRT，r=p接等块。

**边界：** 未消除小p全部物理供应；r=1的统一启动又有后续奇数铅笔。

**原文：** [retained_carrier_bridge_and_endpoint_lessons.md](../sources/research/prime_arity_padic/retained_carrier_bridge_and_endpoint_lessons.md)

**导航前提：** PRIME-CRITICAL-CONTROLLER（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-CRITICAL-CONTROLLER：补齐其r<r₀条带，不再把立方根宽度看作当前缺口

**后续更新：** PRIME-FINITE-TERMINAL：统一已有深核后的终端接口，取消逐数字取逆／扩环要求；PRIME-ODD-PENCIL：奇数下半带包括端点改为统一启动，不再依赖83

**核验：** `python knowledge/project_knowledge.py verify PRIME-RETAINED-BRIDGE` 只展示已登记命令及边界，不自动启动计算。

### PRIME-ADELIC · 本原直线的内容余循环与共同CRT

**状态：** 本地文稿已给证明，未独立重审。把本原化的局部内容、均值标记及两端点CRT准备接到共同格描述。

**边界：** 阿代尔语言不会供应尚缺的物理返回；旧r=1启动差异按奇数铅笔更新。

**原文：** [adelic_primitive_lines_and_common_endpoint_preparation.md](../sources/research/prime_arity_padic/adelic_primitive_lines_and_common_endpoint_preparation.md)

**后续更新：** PRIME-ODD-PENCIL：端点与奇数内部的资源启动差异已由共同反射替代

**核验：** `python knowledge/project_knowledge.py verify PRIME-ADELIC` 只展示已登记命令及边界，不自动启动计算。

### PRIME-FIBER · 同行列式纤维与有限精度对应

**状态：** 本地文稿已给证明，未独立重审。有效作用格(n/g)Z；偶4≤r≤2p/5、奇5≤r≤p/5有直接根；Q|det A|精度记录本原输出。

**边界：** 深核必须先真实实现；有限对应图存在不等于其终端全覆盖。

**原文：** [determinant_fibers_and_finite_lattice_correspondences.md](../sources/research/prime_arity_padic/determinant_fibers_and_finite_lattice_correspondences.md)

**导航前提：** PRIME-COMMON-SHAPE（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify PRIME-FIBER` 只展示已登记命令及边界，不自动启动计算。

### PRIME-GEOMETRY · 有界纤维整数凸包、根本原性与内容对偶

**状态：** 本地文稿已给证明，未独立重审。固定非零行列式纤维的整数凸包维数控制可生成根格；二维得到本原步长；内容与伴随对偶。

**边界：** 实多边形大不等于任意小库存有资源；未完成全参数无证书存在性。

**原文：** [global_structure_and_bounded_fiber_geometry_20260916.md](../sources/research/prime_arity_padic/global_structure_and_bounded_fiber_geometry_20260916.md)

**证据／文献记录：** [source_index.md](../sources/research/prime_arity_padic/global_structure_investigation_20260916/source_index.md)

**导航前提：** PRIME-FIBER（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify PRIME-GEOMETRY` 只展示已登记命令及边界，不自动启动计算。

### PRIME-FINITE-TERMINAL · 深核只建一次：有限对应群化与共同终端

**状态：** 本地文稿已给证明，未独立重审。已有真实深核，行列式与控制模数互素时，有限正向对应轨道等于明确有限群轨道；终端无需反复扩环。

**边界：** 不供应初始根与深核；共享坏因子的行列式不自动覆盖。

**原文：** [finite_orbit_completion_without_ring_extension.md](../sources/research/prime_arity_padic/finite_orbit_completion_without_ring_extension.md)

**导航前提：** PRIME-GEOMETRY, PRIME-SPLIT-COLUMNS（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-RETAINED-BRIDGE：统一已有深核后的终端接口，取消逐数字取逆／扩环要求

**核验：** `python knowledge/project_knowledge.py verify PRIME-FINITE-TERMINAL` 只展示已登记命令及边界，不自动启动计算。

### PRIME-ODD-PENCIL · 奇数下半区共同边界反射铅笔

**状态：** 本地文稿已给证明，未独立重审。所有奇素数p≥3、全部奇数1≤r<p，用同一两组三步反射及两步反射取得根、深核与终端。包含r=1，无83界。

**边界：** 偶数余量、3p及上半带没有因此统一；Morris/Serre等原依赖仍保留。

**原文：** [odd_lower_band_boundary_reflection_pencil_20260916.md](../sources/research/prime_arity_padic/odd_lower_band_boundary_reflection_pencil_20260916.md)

**导航前提：** PRIME-FINITE-TERMINAL, EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**与旧结果的关系：** PRIME-RETAINED-BRIDGE：奇数下半带包括端点改为统一启动，不再依赖83；PRIME-ADELIC：端点与奇数内部的资源启动差异已由共同反射替代

**核验：** `python knowledge/project_knowledge.py verify PRIME-ODD-PENCIL` 只展示已登记命令及边界，不自动启动计算。

### PRIME-TAIL-BACKUP · 4p尾部整数化：备用改进及固定池障碍

**状态：** 部分结果／明确范围。原n≥4p已全证；本稿分析见证预算、双重值恢复与固定双块池策略的不可能范围。

**边界：** 不构成2p附近统一突破；没有发现必须重做原尾部正确性的理由。

**原文：** [four_p_tail_optimization.md](../sources/research/prime_arity_padic/four_p_tail_optimization.md)

**还应读：** PRIME-NATURAL-UNIFICATION

**核验：** `python knowledge/project_knowledge.py verify PRIME-TAIL-BACKUP` 只展示已登记命令及边界，不自动启动计算。

### PRIME-2P2 · 偶数下边界 n=2p+2：状态相关的两次CRT返回

**状态：** 原证明已完成。全部素数p≥5、n=2p+2的完整G=1判据；无需omega(p+1)限制。

**边界：** 原文的“上方九偏移仍未解”是历史状态；本边界已完整，但不等于内部偶数启动已经同构。

**原文：** [prime_arity_two_p_plus_two_uniform.md](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md)

**条件／外部依赖：** 原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-RETAINED-BRIDGE

**核验：** `python knowledge/project_knowledge.py verify PRIME-2P2` 只展示已登记命令及边界，不自动启动计算。

### PRIME-EVEN-INTERIOR · 偶数下半带内部 4≤r≤p−3 的完整证明

**状态：** 原证明已完成。全部p≥7、偶数4≤r≤p−3，n=2p+r全输入G=1充要。

**边界：** 不承担r=2及r=p−1；这两条边界有独立完整卡。旧二进表可由PRIME-DYADIC替代，不等于启动全部统一。

**原文：** [prime_arity_even_interior_completion.md](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md)

**条件／外部依赖：** 原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-RETAINED-BRIDGE

**核验：** `python knowledge/project_knowledge.py verify PRIME-EVEN-INTERIOR` 只展示已登记命令及边界，不自动启动计算。

### PRIME-3PM1 · 偶数上边界 n=3p−1：重叠反射完整证明

**状态：** 原证明已完成。全部素数p≥5、n=3p−1的完整G=1判据；p≥7通式，p=5有显式夹乘。

**边界：** 两条偶数边界均已完成；本卡并未宣称与r=2及内部是同一资源公式。

**原文：** [prime_arity_three_p_minus_one_completion.md](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md)

**条件／外部依赖：** 原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-RETAINED-BRIDGE

**核验：** `python knowledge/project_knowledge.py verify PRIME-3PM1` 只展示已登记命令及边界，不自动启动计算。

### PRIME-3P · n=3p：三个等大块运输

**状态：** 原证明已完成。n=3p的完整判据允许G为p幂；等大三块具有独立的真实运输／终端机制。

**边界：** 此处不可简写G=1；本原重数改变，未由r≠p的共同控制器替代。

**原文：** [prime_arity_middle_band_structure.md](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md)

**条件／外部依赖：** 原文保留的入口、Morris／Serre及零触发前提；有限检查不代替一般量词

**导航前提：** EXTERNAL-ARITH（不是自动抽取的完整证明DAG）

**还应读：** PRIME-NATURAL-UNIFICATION, PRIME-RETAINED-BRIDGE

**核验：** `python knowledge/project_knowledge.py verify PRIME-3P` 只展示已登记命令及边界，不自动启动计算。

<!-- END SOURCE doc-66296cf1c816 -->

---

<a id="doc-533f52f161f3"></a>

## 原文导签：阈值以下与五元算术

来源：`knowledge/topics/subcritical.md` · [逐字节原样副本](../sources/knowledge/topics/subcritical.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-533f52f161f3 -->
# 阈值以下与五元算术

[总状态](../sources/knowledge/STATUS.md) · [接手入口](../sources/knowledge/START_HERE.md)

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

**原文：** [subcritical_complement_dynamics_20260916.md](../sources/research/prime_arity_padic/subcritical_complement_dynamics_20260916.md) · [subcritical_prime_uniform_arithmetic_20260917.md](../sources/research/prime_arity_padic/subcritical_prime_uniform_arithmetic_20260917.md)

**条件／外部依赖：** 仅固定S相邻边及开曲面整点有限性使用ESS定理1.1；算法、p进分类及一般p坐标公式不依赖ESS

**证据／文献记录：** [source.json](../sources/research/prime_arity_padic/five_torus_literature_20260917/source.json)

**还应读：** SUBCRITICAL-LIMITS, FIVE-FRACTAL, SIX-EXPLICIT, FIVE-TORUS

**核验：** `python knowledge/project_knowledge.py verify SUBCRITICAL-COMPLETE` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 区分曲面上的真实降秩路径与人为固定S整点条件；p+2继续静态算术压缩，p+3及一般p+r需同时控制自同构与真子集投影，不由维数猜测现成高秩群判据。

### SUBCRITICAL-LIMITS · 低维G加固定同余、实半代数判据的限制

**状态：** 本地文稿已给证明，未独立重审。对每个奇素数p、每个p+2≤n≤2p和任意固定M，都有逐项modM相同、G均为1的一可解一不可解输入；一个全r公式统一旧端点例子。有限实半代数判据也不足以刻画p+2方向。

**边界：** 只排除G加预定有限同余，以及指定实半代数表达；不排除自适应gcd或其他算术编码。没有证明简洁判据不可能。

**原文：** [five_six_intuitive_criteria_and_modular_limits_20260916.md](../sources/research/prime_arity_padic/five_six_intuitive_criteria_and_modular_limits_20260916.md) · [subcritical_prime_uniform_arithmetic_20260917.md](../sources/research/prime_arity_padic/subcritical_prime_uniform_arithmetic_20260917.md)

**核验：** `python knowledge/project_knowledge.py verify SUBCRITICAL-LIMITS` 只展示已登记命令及边界，不自动启动计算。

### SIX-EXPLICIT · 六元三重核心G=3与唯一后继

**状态：** 本地文稿已给证明，未独立重审。三重核心G=3且无四重值可解；四重值有模9条件；一般G=1失败出口后剩唯一后继。

**边界：** 一般G=1尚未压成一次性公式；不是所有六元G合法都可解。

**原文：** [six_triple_block_explicit_G3_20260916.md](../sources/research/prime_arity_padic/six_triple_block_explicit_G3_20260916.md)

**核验：** `python knowledge/project_knowledge.py verify SIX-EXPLICIT` 只展示已登记命令及边界，不自动启动计算。

### FIVE-SUMMARY · 五元：算法已解、静态分类仍未解

**状态：** 解释／综述，非新可达性证明。逐输入判定与最短路径完成；椭圆型真实宏的范数剥离已统一，新增−59／−971子族及跨素数根标签耦合。全五元静态判据及固定D全词逃逸仍未解。

**边界：** 本总结不是所有新证明的独立审核。有限实验、零密度、分形维数和超越性均不能证明静态简单判据不可能。

**原文：** [five_averaging_progress_summary_20260917.md](../sources/research/prime_arity_padic/five_averaging_progress_summary_20260917.md)

**还应读：** SUBCRITICAL-COMPLETE, FIVE-ESCAPE-OPEN, FIVE-TEMPLATE-ESCAPE, FIVE-DIGITS, FIVE-NORM-SLICE

**核验：** `python knowledge/project_knowledge.py verify FIVE-SUMMARY` 只展示已登记命令及边界，不自动启动计算。

### FIVE-NORM-SLICE · 统一椭圆宏范数剥离、根标签耦合与−59／−971判据

**状态：** 本地文稿已给证明，未独立重审。任意椭圆型真实宏T=WS^ε均由范数赋值保证原位置整块剥离；−11、−59、−971有完整静态子族。Q₁₁非三核m必为5或25 mod30，成功根标签存在跨素数耦合。保留原固定m塔及一般p+2范数子族。

**边界：** 单周期剥离已统一，任意m成功标签及不同周期选择／转换仍未统一；有限组周期范数塔不足全覆盖。m可沿成功步骤增大，不能默认下降。m不是环面D，全词逃逸未解，新证明未独立重审。

**原文：** [five_quadratic_norm_explicit_slice_20260916.md](../sources/research/prime_arity_padic/five_quadratic_norm_explicit_slice_20260916.md) · [five_quadratic_norm_towers_and_minus59_20260917.md](../sources/research/prime_arity_padic/five_quadratic_norm_towers_and_minus59_20260917.md)

**导航前提：** SUBCRITICAL-COMPLETE（不是自动抽取的完整证明DAG）

**还应读：** FIVE-NORMAL-FORM, FIVE-DENOMINATORS

**核验：** `python knowledge/project_knowledge.py verify FIVE-NORM-SLICE` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 单周期的整数实现已统一；继续须控制任意m的整体根标签、多个周期之间的转换与选择。排除独立素数筛选和单陪集模型，不排除更一般算术关系。

### FIVE-NORMAL-FORM · 五元完整受限连分数与level15矩阵序

**状态：** 本地文稿已给证明，未独立重审。任意五元通过十对线性表达式进入唯一受限连分数；整数代数为level15序，生成模为u+v≡0 mod5。

**边界：** 群轨道严格大于正词；不存在两分支共同乘法型齐次范数，不排除一般算术条件。

**原文：** [five_complete_arithmetic_normal_form_20260916.md](../sources/research/prime_arity_padic/five_complete_arithmetic_normal_form_20260916.md)

**导航前提：** SUBCRITICAL-COMPLETE（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-NORMAL-FORM` 只展示已登记命令及边界，不自动启动计算。

### FIVE-FRACTAL · 三进紧集的全部有理点与密度

**状态：** 本地文稿已给证明，未独立重审。有限标记=可解；无限边界有理点恰两轴有限轨道，被模5排除；维数log₂/log₃、每层2^(m+1)−1类。

**边界：** 实稠密、三进零测不等于判定不可能；五元整数盒子密度零不等于固定D有限。

**原文：** [five_padic_fractal_rational_points_20260916.md](../sources/research/prime_arity_padic/five_padic_fractal_rational_points_20260916.md)

**导航前提：** FIVE-NORMAL-FORM（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-FRACTAL` 只展示已登记命令及边界，不自动启动计算。

### FIVE-DIGITS · 原整数同步三进非正则、精确进位与有理代数对应

**状态：** 本地文稿已给证明，未独立重审。普通斜率及未本原化原五整数的同步三进语言均无固定有限状态判据；h剥位公因子恰gcd(q,4)，二因子总量望远镜消去。保留交换商有理对应。

**边界：** 不排除先算gcd后本原承诺域读位、无界整数寄存器或输入相关算术式；未得G式总判据。换支不是实际平均，新证明未独立重审。

**原文：** [five_digit_obstruction_and_rational_correspondence_20260916.md](../sources/research/prime_arity_padic/five_digit_obstruction_and_rational_correspondence_20260916.md) · [five_integer_digits_and_carry_20260917.md](../sources/research/prime_arity_padic/five_integer_digits_and_carry_20260917.md)

**证据／文献记录：** [rational_base_padic_2011_source.json](../sources/research/prime_arity_padic/five_torus_literature_20260917/rational_base_padic_2011_source.json) · [rational_base_regular_2021_source.json](../sources/research/prime_arity_padic/five_torus_literature_20260917/rational_base_regular_2021_source.json)

**导航前提：** FIVE-FRACTAL（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-DIGITS` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 当前优先：本原化后的数字规律或输入相关gcd／赋值式；先与完整递归核验。二进约分总量已消去，不能再把它作为独立无界障碍。

### FIVE-TORUS · 统一Q(√5)范数一环面与扭曲平移

**状态：** 本地文稿已给证明，未独立重审。两分支为J(ε^±1α)，3惰性、5分歧；四穿孔曲线及固定S内相邻单位边有限。

**边界：** J不是群同态；相邻边有限不能阻止离开后返回；辅助分母不是物理分母。

**原文：** [five_norm_one_torus_and_twisted_translation_20260917.md](../sources/research/prime_arity_padic/five_norm_one_torus_and_twisted_translation_20260917.md)

**条件／外部依赖：** ESS定理1.1用于固定S单位方程

**证据／文献记录：** [README.md](../sources/research/prime_arity_padic/five_torus_literature_20260917/README.md)

**导航前提：** FIVE-DIGITS（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-TORUS` 只展示已登记命令及边界，不自动启动计算。

### FIVE-DENOMINATORS · 精确D、相邻互素、同理想任意近的失败点

**状态：** 本地文稿已给证明，未独立重审。D=|u²+7uv+v²|/5是环面最小分母；相邻D互素，兄弟gcd只可能11；同理想固定局部精度不足。

**边界：** D不单调，不独立决定可解；辅助素数可变化。

**原文：** [five_torus_denominators_and_local_separation_20260917.md](../sources/research/prime_arity_padic/five_torus_denominators_and_local_separation_20260917.md)

**导航前提：** FIVE-TORUS（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-DENOMINATORS` 只展示已登记命令及边界，不自动启动计算。

### FIVE-UNITS-GROUP · 固定理想单位指数与三进大群闭包

**状态：** 本地文稿已给证明，未独立重审。固定理想候选为α₀ε^(4k)，Z₃指数与h等距；群闭包含PSL₂(Q₃)，对数偏移D=1整数、D>1超越。

**边界：** 大群不替代正半群；指数零密度不推出有限。

**原文：** [five_fixed_ideal_unit_exponents_and_padic_group_20260917.md](../sources/research/prime_arity_padic/five_fixed_ideal_unit_exponents_and_padic_group_20260917.md)

**条件／外部依赖：** Baker–Brumer，已读正式转述，原1967证明未取得

**导航前提：** FIVE-DENOMINATORS, FIVE-FRACTAL（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify FIVE-UNITS-GROUP` 只展示已登记命令及边界，不自动启动计算。

### FIVE-SPARSITY · 固定D有效稀疏与固定周期有限返回

**状态：** 本地文稿已给证明，未独立重审。长度L指数区间成功数<4L^log₃2；固定D高度计数为对数高度分数幂；固定正词幂只有有限命中。

**边界：** 不涵盖变词全树；有限返回不自动给有效最后命中界，后续Baker只补固定混合周期。

**原文：** [five_fixed_D_effective_sparsity_and_periodic_return_20260917.md](../sources/research/prime_arity_padic/five_fixed_D_effective_sparsity_and_periodic_return_20260917.md)

**条件／外部依赖：** ESS；SML为替代有限性论证

**导航前提：** FIVE-UNITS-GROUP（不是自动抽取的完整证明DAG）

**后续更新：** FIVE-TEMPLATE-ESCAPE：由单周期扩为多参数固定模板，另补固定周期有效增长

**核验：** `python knowledge/project_knowledge.py verify FIVE-SPARSITY` 只展示已登记命令及边界，不自动启动计算。

### FIVE-BOUNDED-RUNS · 有界字母切换的有效有限性

**状态：** 本地文稿已给证明，未独立重审。固定D且同方向段数有界时有限并有效；D=1至多两次切换的全长度分类只留三个方向。

**边界：** 小段数应用有精确尾误差证书；任意切换仍未解决，后续有无网格界与模板推广。

**原文：** [five_bounded_switches_and_correspondence_degree_20260917.md](../sources/research/prime_arity_padic/five_bounded_switches_and_correspondence_degree_20260917.md)

**导航前提：** FIVE-DENOMINATORS（不是自动抽取的完整证明DAG）

**后续更新：** FIVE-HECKE：将一般有效界升级为无网格显式界；FIVE-TEMPLATE-ESCAPE：重复块可混合两字母，覆盖无界切换子族

**核验：** `python knowledge/project_knowledge.py verify FIVE-BOUNDED-RUNS` 只展示已登记命令及边界，不自动启动计算。

### FIVE-HECKE · 显式间隙界与同层共同Hecke二次型

**状态：** 本地文稿已给证明，未独立重审。有界段数给闭式字长界；所有同长度词拉回型整数等价；D=1第一段为v₃(2k+1)+v₃(2k−1)。

**边界：** Aka–Shapira只给整周期分布，不控制终端标记Ce；类信息统一不是全词逃逸。

**原文：** [five_explicit_gap_common_hecke_form_20260917.md](../sources/research/prime_arity_padic/five_explicit_gap_common_hecke_form_20260917.md)

**条件／外部依赖：** Aka–Shapira用于共同周期；Lucas赋值亦有自足证明

**证据／文献记录：** [switch_hecke_review_20260917.md](../sources/research/prime_arity_padic/five_torus_literature_20260917/switch_hecke_review_20260917.md)

**导航前提：** FIVE-BOUNDED-RUNS, FIVE-UNITS-GROUP（不是自动抽取的完整证明DAG）

**与旧结果的关系：** FIVE-BOUNDED-RUNS：将一般有效界升级为无网格显式界

**核验：** `python knowledge/project_knowledge.py verify FIVE-HECKE` 只展示已登记命令及边界，不自动启动计算。

### FIVE-TEMPLATE-ESCAPE · 固定多块模板统一逃离小分母

**状态：** 本地文稿已给证明，未独立重审。任意固定U₀V₁^a₁⋯V_r^a_rU_r内，指数独立变化仍统一逃离小D；允许混合块及无界切换。

**边界：** 模板本身变化的全部词仍未覆盖；多模板有限性未给有效截止；固定混合周期另有Baker指数下界。

**原文：** [five_bounded_templates_uniform_escape_20260917.md](../sources/research/prime_arity_padic/five_bounded_templates_uniform_escape_20260917.md)

**条件／外部依赖：** ESS经极小零子和化格陪集；Baker–Wüstholz正式转述只用于固定周期有效增长

**证据／文献记录：** [uniform_escape_review_20260917.md](../sources/research/prime_arity_padic/five_torus_literature_20260917/uniform_escape_review_20260917.md)

**导航前提：** FIVE-SPARSITY, FIVE-DENOMINATORS（不是自动抽取的完整证明DAG）

**与旧结果的关系：** FIVE-SPARSITY：由单周期扩为多参数固定模板，另补固定周期有效增长；FIVE-BOUNDED-RUNS：重复块可混合两字母，覆盖无界切换子族

**核验：** `python knowledge/project_knowledge.py verify FIVE-TEMPLATE-ESCAPE` 只展示已登记命令及边界，不自动启动计算。

### FIVE-ESCAPE-OPEN · 固定D全词逃逸与D=1完整分类

**状态：** 开放问题。猜想min_|W|=L D(We)→∞；更小猜想D=1只允许单位指数k=0,±1。

**边界：** 模板定理、零密度、群闭包、有限指数范围实验都不能替代任意词证明。没有证明简单判据不可能。

**原文：** [five_averaging_progress_summary_20260917.md](../sources/research/prime_arity_padic/five_averaging_progress_summary_20260917.md) · [five_bounded_templates_uniform_escape_20260917.md](../sources/research/prime_arity_padic/five_bounded_templates_uniform_escape_20260917.md)

**还应读：** FIVE-TEMPLATE-ESCAPE, FIVE-HECKE

**核验：** `python knowledge/project_knowledge.py verify FIVE-ESCAPE-OPEN` 只展示已登记命令及边界，不自动启动计算。

**继续须新增：** 对不断变化的词模板给一致小范数控制，或构造无限反例族；不得把固定模板的无限并当有限覆盖。

<!-- END SOURCE doc-533f52f161f3 -->

---

<a id="doc-6646d5da9f32"></a>

## 原文导签：三平均全维数与几何

来源：`knowledge/topics/triple.md` · [逐字节原样副本](../sources/knowledge/topics/triple.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-6646d5da9f32 -->
# 三平均全维数与几何

[总状态](../sources/knowledge/STATUS.md) · [接手入口](../sources/knowledge/START_HERE.md)

先读TRIPLE-ALL完整直接链，再读SEVEN-GEOMETRY与GEOMETRY-ALL-N。统一解释不是另一份已经完成的纯模曲线证明。


| ID | 结论 | 状态 |
|---|---|---|
| TRIPLE-ALL | 三平均 n≥7 的完整G判据 | 原证明已完成 |
| TRIPLE-BASES | 三平均7、8、9、10基例与适用范围 | 原证明已完成 |
| SEVEN-STRUCTURE | 七元：真实正向逆与完整 Γ₀(7) 控制 | 原证明已完成 |
| GEOMETRY-ALL-N | 全部n的根格、局部根基与零目标饱和 | 解释／综述，非新可达性证明 |
| SEVEN-GEOMETRY | 七元G、分歧范数、尖点与Eisenstein的完整对接 | 本地文稿已给证明，未独立重审 |

### TRIPLE-ALL · 三平均 n≥7 的完整G判据

**状态：** 原证明已完成。非全等输入中心化、本原化后，可达全等 ⇔ G为3幂。n≥11同一双三重直接证明，接7—10基例。

**边界：** 判定已解决；不等于最短路径或可变n统一多项式构造长度已解决。

**原文：** [triple_average_all_dimensions_double_triple_invariant.md](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md)

**导航前提：** TRIPLE-BASES, G-OBSTRUCTION（不是自动抽取的完整证明DAG）

**还应读：** GEOMETRY-ALL-N, ALG-LENGTH

**核验：** `python knowledge/project_knowledge.py verify TRIPLE-ALL` 只展示已登记命令及边界，不自动启动计算。

### TRIPLE-BASES · 三平均7、8、9、10基例与适用范围

**状态：** 原证明已完成。7元已有无十八词覆盖的结构证明；8元Euclid下降；9元三幂网络；10元精确局部—实宏覆盖。

**边界：** 不能将10元有限证书说成全凭几何；七元新版不依赖旧十八词搜索。

**原文：** [triple_average_seven_eight_complete.md](../sources/outputs/triple_average/proofs/triple_average_seven_eight_complete.md) · [triple_average_ten_complete.md](../sources/outputs/triple_average/proofs/triple_average_ten_complete.md)

**还应读：** SEVEN-STRUCTURE

**核验：** `python knowledge/project_knowledge.py verify TRIPLE-BASES` 只展示已登记命令及边界，不自动启动计算。

### SEVEN-STRUCTURE · 七元：真实正向逆与完整 Γ₀(7) 控制

**状态：** 原证明已完成。两步安全入口、三种实际返回的标量周期、根群与八陪集改写、合法单尖点轨道和四步尾部。

**边界：** 七元作为全系统才共享目标均值；嵌入较大系统不可免费当作全局射影逆。

**原文：** [seven_exact_threshold_structure.md](../sources/outputs/prime_arity/examples/seven_exact_threshold_structure.md)

**还应读：** SEVEN-GEOMETRY, WINDOW-MEAN

**核验：** `python knowledge/project_knowledge.py verify SEVEN-STRUCTURE` 只展示已登记命令及边界，不自动启动计算。

### GEOMETRY-ALL-N · 全部n的根格、局部根基与零目标饱和

**状态：** 解释／综述，非新可达性证明。G是A_(n−1)中本原向量的配对理想；危险素位为对角根基；A₂投影及实际见证下降统一解释已有定理。

**边界：** 不是新纯同余群证明。一般G合法不等于范数为单位；n=11有能量22、G=1的可解例子。

**原文：** [triple_all_n_root_lattice_and_target_saturation_20260917.md](../sources/research/prime_arity_padic/triple_all_n_root_lattice_and_target_saturation_20260917.md)

**导航前提：** TRIPLE-ALL, SEVEN-GEOMETRY（不是自动抽取的完整证明DAG）

**核验：** `python knowledge/project_knowledge.py verify GEOMETRY-ALL-N` 只展示已登记命令及边界，不自动启动计算。

### SEVEN-GEOMETRY · 七元G、分歧范数、尖点与Eisenstein的完整对接

**状态：** 本地文稿已给证明，未独立重审。指定宏群恰为PGL₂(Z[1/6])模7上三角子群；G=1等价合法尖点及Q(√−7)分歧单位，theta与本原能量层有显式计数。

**边界：** 七元可达性是已有结果；theta计数和类数一不能替代真实正向宏。非全局窗口不能直接推广。

**原文：** [seven_averaging_cusps_norm_and_eisenstein_20260917.md](../sources/research/prime_arity_padic/seven_averaging_cusps_norm_and_eisenstein_20260917.md)

**条件／外部依赖：** theta模性引用已读Stein Theorem5.8；轨道与范数恒等式在正文证明

**证据／文献记录：** [README.md](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/README.md)

**导航前提：** SEVEN-STRUCTURE, G-OBSTRUCTION（不是自动抽取的完整证明DAG）

**后续更新：** PRIME-ENDPOINT-GEOMETRY：将七元的精确宏群与G轨道扩到全部奇2p+1端点；保留七元专属theta/Eisenstein计数，不外推其类数一结论

**核验：** `python knowledge/project_knowledge.py verify SEVEN-GEOMETRY` 只展示已登记命令及边界，不自动启动计算。

<!-- END SOURCE doc-6646d5da9f32 -->

---

<a id="doc-24a8b54a7709"></a>

## 原文导签：成果与研究索引

来源：`outputs/README.md` · [逐字节原样副本](../sources/outputs/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-24a8b54a7709 -->
# 成果与研究索引

> **2026-09-17导航更新：** 新接手者先读[统一状态与主题入口](../sources/knowledge/START_HERE.md)。下文保留2026-09-15完成项目的基线索引；“最新简化”指该版本。其后的独立研究、字段替代和真正开放任务统一登记在[素数主题](../sources/knowledge/topics/prime.md)，不要据下文旧阶段重开任务。原技术证明与注册未改动。

2026-09-15整理。当前任务：素数平均证明的整合和改进。先按主题选择入口；旧研究过程已移入同目录的[历史路线账本](../sources/outputs/history/research_routes_history_20260915.md)，技术附录已实际移入主题文件夹，链接与核验注册同步更新。

## 文件夹地图

```text
outputs/
├─ prime_arity/          素数定理入口、总证明、通用引理
│  ├─ proofs/           lower_band / upper_band / tail_and_lower_bound
│  ├─ tools/            入口、核心与均值格原始工具
│  ├─ structure/        当前证明简化与结构研究
│  ├─ audits/           专项及独立审核
│  ├─ examples/         小素数实例
│  └─ history/          素数研究历史
├─ triple_average/      proofs / arithmetic_cases / history
├─ general_arity/       一般元数、合数与条件性结果
├─ algorithms/          序列、复杂度和测试集
├─ literature/          文献调查
└─ history/             路线账本与阅读日志
```

[素数](../sources/outputs/prime_arity/README.md) · [三平均](../sources/outputs/triple_average/README.md) · [一般元数](../sources/outputs/general_arity/README.md) · [算法](../sources/outputs/algorithms/README.md) · [文献](../sources/outputs/literature/README.md) · [历史](../sources/outputs/history/README.md)。

迁移了220篇文档，旧路径对应新路径可查[完整迁移表](../sources/work/document_reorganization_20260915/path_map.json)。技术脚本和证书仍在work，避免破坏模块导入。没有在outputs根目录留下220个跳转占位文件。

## 素数平均：完整最终阈值

最新证明简化：[三个共轭根与浅层提升](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)。九偏移的奇数n已删除高阶方向／尺度轨道，偶数n只剩至多8个二进修正类；p≥83用统一三连参数公式，保留162组物理计数证书与原两项局部补充。

[主入口](../sources/outputs/prime_arity/README.md) → [总证明与覆盖表](../sources/outputs/prime_arity/proof.md) → [通用算术引理](../sources/outputs/prime_arity/arithmetic_toolkit.md) → [几何解释](../sources/outputs/prime_arity/geometry.md)。

全部奇素数 p 有 N(p)=2p+1，N(2)=4；阈值以上判据为中心化、本原化后的 G 是 p 幂。两条偶数边界、九个低偏移和全部旧 dₚ 尾部缺口均已完成。不要据旧专题中的阶段状态重新开启这些定理。

最新整理把二进补充所用倍率的扩环正式并入[九偏移第6节](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)。无条件结论仍使用 Morris/Serre，有限参数证书仍是证明的一部分。[本轮阅读、核验与维护记录](../sources/outputs/prime_arity/verification.md)说明实际核对范围。

## 三平均：独立直接证明和算法

- [双三重值任意维数直接证明](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md)：n≥11 的初等主证明，接7、8、9、10元基例得 n≥7；不依赖上述一般算术群证明。
- [二平均原文复核](../sources/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md)：直接方法的来源、实际读过的原文和误用边界。
- [序列长度研究](../sources/outputs/algorithms/triple_average_sequence_length_analysis.md)：区分数值能量界、固定 n 的位长界和未证的可变 n 统一界。
- [算法测试集](../sources/outputs/algorithms/averaging_algorithm_benchmark.md)：已知可达但可能难于提取路径的输入；搜索失败不代表反例。

旧“17到59的种子／非分裂／仿射／Hecke”研究按[历史路线表](../sources/outputs/history/research_routes_history_20260915.md)查找。其方法障碍可能仍有意义，素数平均可达性定理本身已不再开放。

## 合数元数：成果保留，另有未解范围

当前交接为[三项任务的完成范围和剩余](../sources/outputs/general_arity/general_k_three_tasks_progress_20260915.md)。本轮不推进这些任务，不改变用户此前允许采用 GRH 的决定。

| 已有结果 | 条件与入口 |
|---|---|
| 所有平方元数 t² 在 t²+t+1 元完整成立 | [GRH阶段定理](../sources/outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md)；充分大参数另有无条件结果 |
| 2、3的全部幂达到最早临界点 | GRH 下；见上述最新交接，不能称为全部后续维数的最终阈值 |
| 任意整数 k≥2 的 2k+1 端点 | [偶元数补齐](../sources/outputs/general_arity/even_arity_all_endpoints_completion.md)，接已证奇元数结果；无条件 |
| 奇素数幂的全部奇数 2k<n<3k | [奇合数区间与块均值转译](../sources/outputs/general_arity/odd_composite_coprime_middle_band_completion.md)；无条件 |
| 十平均十六元固定六步网络及推广族 | [固定网络](../sources/outputs/general_arity/ten_average_sixteen_and_dyadic_network_family.md)；无条件 |
| 任意元数的已知宽尾部 | [一般线性阈值](../sources/outputs/general_arity/arbitrary_arity_linear_threshold.md)，不等于最优阈值 |

定义 M、H、N 及原猜想的历史来源见[全局状态](../sources/outputs/general_arity/averaging_global_status_20260912.md)和[合数临界猜想](../sources/outputs/general_arity/composite_critical_scale_and_conjecture.md)。两篇日期较早，以新交接判断其开放范围。

## 证据与历史

[素数核验说明](../sources/outputs/prime_arity/verification.md) · [机器依赖图](../sources/outputs/prime_arity/proof_map.json) · [全项目核验注册](../sources/work/verification_manifest.json) · [此前阅读日志](../sources/outputs/history/research_reading_log_20260915.md) · [原根 README 历史](../sources/HISTORY.md)。

符号：当前 p 是平均元数，n 是位置数。很多旧 triple_average 文件的 p 是位置数，引用公式前必须检查。

<!-- END SOURCE doc-24a8b54a7709 -->

---

<a id="doc-5a9f1981beef"></a>

## 原文导签：算法、复杂度与测试集

来源：`outputs/algorithms/README.md` · [逐字节原样副本](../sources/outputs/algorithms/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-5a9f1981beef -->
# 算法、复杂度与测试集

区分可达性存在、构造长度、最短路径及有限搜索。

[回到成果索引](../sources/outputs/README.md)

- [Arena三平均网页算法审阅与同题对比](../sources/outputs/algorithms/arena_triple_solver_review.md)
- [原位置 p 平均算法测试集](../sources/outputs/algorithms/averaging_algorithm_benchmark.md)
- [二平均求解器复核、三平均优化与最短性](../sources/outputs/algorithms/pair_triple_solver_comparison_and_optimality.md)
- [三平均计算的性能审计与搜索优化](../sources/outputs/algorithms/triple_average_computation_performance_audit.md)
- [三平均搜索优化建议复核（2026-09-09）](../sources/outputs/algorithms/triple_average_search_optimization_review_2026-09-09.md)
- [双三重值算法的操作序列长度](../sources/outputs/algorithms/triple_average_sequence_length_analysis.md)
- [三平均研究的计算核验指南](../sources/outputs/algorithms/triple_average_verification_guide.md)

<!-- END SOURCE doc-5a9f1981beef -->

---

<a id="doc-f00c7dd4ea77"></a>

## 原文导签：一般元数与合数研究

来源：`outputs/general_arity/README.md` · [逐字节原样副本](../sources/outputs/general_arity/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-f00c7dd4ea77 -->
# 一般元数与合数研究

新接手先读[统一一般元数主题](../sources/knowledge/topics/composite.md)。精确区分M、H、N与GRH条件；下文的“本轮”描述原交接时点，不自动决定后来用户任务。

当前交接为general_k_three_tasks_progress_20260915。保留GRH条件与开放范围；本轮只整理，不推进这些定理。

[回到成果索引](../sources/outputs/README.md)

[当前合数交接](../sources/outputs/general_arity/general_k_three_tasks_progress_20260915.md)

- [任意平均元数的线性阈值：非单位差分也是可执行资源](../sources/outputs/general_arity/arbitrary_arity_linear_threshold.md)
- [从二平均到任意平均元数：当前全貌与临界猜想](../sources/outputs/general_arity/averaging_global_status_20260912.md)
- [从素数完整证明到合数临界问题：策略、可迁移定理与真实困难](../sources/outputs/general_arity/averaging_proof_strategy_and_composite_frontier_20260915.md)
- [合数平均：四平均、六平均与原位置副本转译](../sources/outputs/general_arity/composite_arity_four_six_transfer.md)
- [合数平均的临界尺度：最早成立、最终阈值与无条件网络](../sources/outputs/general_arity/composite_critical_scale_and_conjecture.md)
- [从十五元推广到合数端点：统一CRT证书与两素数完整入口](../sources/outputs/general_arity/composite_endpoint_crt_transfer.md)
- [全部偶数元数的2k+1端点：旧种子与统一取逆](../sources/outputs/general_arity/even_arity_all_endpoints_completion.md)
- [examples/](../sources/outputs/general_arity/examples/README.md)
- [一般k平均的证明计划：先完成核心，再接成全部维数](../sources/outputs/general_arity/general_k_averaging_proof_plan_20260915.md)
- [接受GRH后的完整平方族定理与剩余证明任务](../sources/outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md)
- [一般k平均规划评议：平方族入口可直接补齐，尺度任务可以数论化](../sources/outputs/general_arity/general_k_plan_review_and_square_entry_20260915.md)
- [对一般k规划建议的复核与采纳](../sources/outputs/general_arity/general_k_review_response_20260915.md)
- [GRH主线三项任务：本轮完成范围与当前剩余](../sources/outputs/general_arity/general_k_three_tasks_progress_20260915.md)
- [H_t文献调查：已有小生成元理论、无条件充分大结论与全范围边界](../sources/outputs/general_arity/ht_literature_and_eventual_square_completion_20260915.md)
- [逆零和定理的原位置转译：碰撞修复与 2p+4 元七步族](../sources/outputs/general_arity/inverse_zero_sum_averaging_progress.md)
- [较大素数高奇次幂：两种统一三步正向反射](../sources/outputs/general_arity/large_prime_high_odd_power_three_step_reflections.md)
- [奇合数元数的奇余量区间：按真实互素条件迁移旧证明](../sources/outputs/general_arity/odd_composite_coprime_middle_band_completion.md)
- [平方元数的统一正向控制器与九平均十三元](../sources/outputs/general_arity/square_arity_uniform_controller_and_nine_thirteen.md)
- [十平均十六元与一族确定性三块网络](../sources/outputs/general_arity/ten_average_sixteen_and_dyadic_network_family.md)
- [十平均与十二平均17元完整G判据，以及原B公式中的自动维数](../sources/outputs/general_arity/ten_twelve_average_seventeen_complete.md)
- [q-平均的根格、\(S\)-算术与控制器猜想](../sources/outputs/general_arity/triple_average_q_average_arithmetic_geometry.md)
- [统一四／六阶控制器完成2、3奇次幂临界点](../sources/outputs/general_arity/two_three_odd_power_critical_grh_completion.md)

<!-- END SOURCE doc-f00c7dd4ea77 -->

---

<a id="doc-0284ea9ce528"></a>

## 原文导签：合数元数实例

来源：`outputs/general_arity/examples/README.md` · [逐字节原样副本](../sources/outputs/general_arity/examples/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-0284ea9ce528 -->
# 合数元数实例

各文件分别标注固定网络、完整判据和使用条件。

[回到成果索引](../sources/outputs/README.md)

- [四平均九元完整判据：一个四步周期与模9控制器](../sources/outputs/general_arity/examples/four_average_nine_complete.md)
- [四平均七元完整判据：\((4,2,1)\) 核与模7控制器](../sources/outputs/general_arity/examples/four_average_seven_complete.md)
- [六平均九元：所有输入固定四步完成](../sources/outputs/general_arity/examples/six_average_nine_fixed_network.md)
- [六平均十元完整G判据：第一个非自动的算术成功维数](../sources/outputs/general_arity/examples/six_average_ten_complete.md)

<!-- END SOURCE doc-0284ea9ce528 -->

---

<a id="doc-87b7960b8383"></a>

## 原文导签：素数平均：当前证明入口

来源：`outputs/prime_arity/README.md` · [逐字节原样副本](../sources/outputs/prime_arity/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-87b7960b8383 -->
# 素数平均：当前证明入口

> **2026-09-17导航更新：** 本页记录已完成证明的冻结基线。后续“两根列修正—分裂乘法—有限对应—奇数边界反射”的当前接口与替代范围，先读[统一素数主题](../sources/knowledge/topics/prime.md)和[证明链](../sources/knowledge/PROOF_ROUTES.md)。原162组注册仍属于本基线；独立研究的114组剩余根资源不自动替换完整审计。

整理日期：2026-09-15。本目录是素数平均的主入口；本目录下的proofs、tools、structure、audits、examples和history分别保存技术证明、工具、结构、审核、实例与历史。本次整理没有把旧文全部重新独立审核，也没有去掉既有外部定理依赖。

## 1. 已证明的准确结论

一次 **p 平均**是在原 n 个位置中选 p 个，将其值同时替换为均值。设有理输入不全等：减去总均值、清分母、除坐标公因子，得到本原整数零和向量 X。记
\[
G(X)=\gcd_{i<j}|X_i-X_j|.
\]
对每个奇素数 p、每个 n≥2p+1，有限步 p 平均可达全等，当且仅当 G(X) 是 p 的非负整数次幂。最优最终阈值为
\[
N(p)=2p+1\quad(p\ge3),\qquad N(2)=4.
\]
只有 p 不整除 n 时，判据才能简写为 G=1。全等输入无需操作。这里的 N 是“此后所有维数均满足判据”的阈值，不是单个自动全平均网络的最小维数。

**证据边界：**素数定理无条件，引用 Morris 的有限指数定理与有理 S 整数 SL₂ 的强同余子群性质；九个低偏移现只需162组有限反射证书；p≥83由统一三连参数公式承担，入口及基础单位生成已改为书面证明。原522组、180组版本保留作历史对照。一般群词存在已证明，但未给出对可变 p、n 的统一多项式操作长度或通用高效词提取算法。没有对所有低于阈值的输入作完整分类。

## 冻结基线的简化（2026-09-15）

[三个共轭根与浅层提升](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)把奇数n控制层降到Γ(n,R)，偶数n降到Γ(2δn,R)、δ∈{2,4}。奇数n不再需要高阶轨道，偶数n模n以上只需至多8个二进方向／尺度类；统一公式达到p≥83，剩162组及原两项补充。[此前区间构造](../sources/outputs/prime_arity/structure/carrier_interval_and_unit_descent.md)的入口、容量与基础单位下降继续使用。

[整格拼接与正运输](../sources/outputs/prime_arity/structure/integral_gluing_and_positive_transport.md)进一步解释同余群和真实逆的来源，给出一般权重整提升判据及等块有限菜单的正运输定理。两个命题有直接证明，未改变当前阈值或剩余证书数。

[局部二次群与轨道缺陷](../sources/outputs/prime_arity/structure/padic_quadratic_group_and_orbit_defect.md)把旧高层方向循环统一成形式群的首层检验；[Kneser边界](../sources/outputs/prime_arity/structure/padic_leading_symbols_and_kneser_boundary.md)说明2p+1也是p进首位不交选择图的连通性阈值。二者独立保留结构意义；当前证书数按上面的浅层提升版为准。

[证明附录](../sources/outputs/prime_arity/proofs/README.md) · [结构研究](../sources/outputs/prime_arity/structure/README.md) · [审核](../sources/outputs/prime_arity/audits/README.md) · [实例](../sources/outputs/prime_arity/examples/README.md) · [历史](../sources/outputs/prime_arity/history/README.md)。

## 2. 按目的阅读

| 目的 | 阅读顺序 |
|---|---|
| 新 AI 快速接手 | 本页 → [总证明](../sources/outputs/prime_arity/proof.md)的覆盖表 → [阅读与核验记录](../sources/outputs/prime_arity/verification.md) |
| 理解证明为何成功 | [总证明](../sources/outputs/prime_arity/proof.md) → [通用算术引理](../sources/outputs/prime_arity/arithmetic_toolkit.md) → [几何解释](../sources/outputs/prime_arity/geometry.md) |
| 严格逐项审核 | 先读通用引理，再按总证明表逐篇读技术附录，最后读三份独立／专项审核 |
| 找可改进之处 | [几何解释第7节](../sources/outputs/prime_arity/geometry.md#7-整理后真正值得改进的部分)；先确认没有重复已否定的推广 |
| 核对脚本支持什么 | [核验说明](../sources/outputs/prime_arity/verification.md)及[机器依赖图](../sources/outputs/prime_arity/proof_map.json)；不要把 PASS 当成全量词证明 |
| 继续合数研究 | [合数交接](../sources/outputs/general_arity/general_k_three_tasks_progress_20260915.md)，与本素数定理分开；其中部分结论依赖 GRH |

## 3. 一条完整证明链

\[
\text{合法原输入}
\longrightarrow\text{带位置账本的少块核心}
\longrightarrow\text{真实标量周期与根}
\longrightarrow\text{深主同余群}
\longrightarrow\text{有限方向和单位尺度}
\longrightarrow\text{精确终端}.
\]

这是临界及中间区间的共同结构。远端还可直接用整数安全平均和离散能量下降。两种方法在造零终端处连接，不要求全程使用同一个能量，也不要求整个 SL₂ 都能实现。

必须区分三层：实际平均词、二维有理矩阵、有限模像。每次从后一层返回前一层都需要已证接口。角色可以更换，但位置总数不能增加；换基用于证明，不自动成为操作；共同尺度必须作用于整个核心。

## 4. 防止重复走弯路

- 端点现在不再受六素因子限制；旧文中的入口限制已被三单点交换子替代。
- 偶余量、2p+2、3p−1、3p 之后九个偏移及旧 dₚ 尾部缺口均已有完成证明，见总证明覆盖表。
- 不能从两个已解维数自动插值，也不能把子系统的射影逆当成全系统的逆。
- 模方向满像不等于尺度匹配；最终环必须包括所有实际使用的倍率，包括二进补充。
- Hecke 分支之和、形式逆、双随机运输和复制实现，都不能单独替代原位置正向词。

旧路线及其适用范围保存在[历史路线账本](../sources/outputs/history/research_routes_history_20260915.md)。历史“未解”是当时状态，不是当前待办。

## 5. 维护规则

新的独立研究先更新[统一结论登记](../sources/knowledge/catalog.json)及相关证据关联，不把进展逐条堆到本页。只有明确纳入完整基线时，才同步修改本目录总证明、依赖图与原核验注册。数学结论、有限证书、公式核验和探索搜索分别标明。本目录采用“总证明＋可定位技术附录”的结构，尚非一篇不依赖链接的自包含论文。

<!-- END SOURCE doc-87b7960b8383 -->

---

<a id="doc-7e8635e35480"></a>

## 原文导签：小素数实例与历史证据

来源：`outputs/prime_arity/examples/README.md` · [逐字节原样副本](../sources/outputs/prime_arity/examples/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-7e8635e35480 -->
# 小素数实例与历史证据

完整定理、数值实验和不可达边界都在文件标题及正文标注；不能因同处此目录就视为相同证据等级。

[回到成果索引](../sources/outputs/README.md)

- [五平均十一元的完整判据：两步返回、正向周期与 Γ₀(11)](../sources/outputs/prime_arity/examples/five_average_eleven_complete.md)
- [五平均 (n=10) 的不可解比例实验](../sources/outputs/prime_arity/examples/five_average_n10_unsolvable_ratio.md)
- [五平均十一元临界实验](../sources/outputs/prime_arity/examples/five_average_n11_random_experiment.md)
- [五平均十三元：已有对合接同余子群定理](../sources/outputs/prime_arity/examples/five_average_thirteen_congruence_complete.md)
- [五平均达到 3p：最小同余见证与碰撞总和证书](../sources/outputs/prime_arity/examples/five_average_three_p_threshold.md)
- [(p=13) 临界对照：(n=26) 与 (n=27)](../sources/outputs/prime_arity/examples/p13_boundary_n26_n27_comparison.md)
- [七平均十五元完整G判据：两素数入口与二进 \(\Gamma_0(15)\) 覆盖](../sources/outputs/prime_arity/examples/seven_average_fifteen_complete.md)
- [七平均 (n=14) 与 (n=15) 对照实验](../sources/outputs/prime_arity/examples/seven_average_n14_vs_n15_comparison.md)
- [七平均 (n=15) 数值证据](../sources/outputs/prime_arity/examples/seven_average_n15_numerical_evidence.md)
- [七平均的最优最终阈值：二十元、二十二元与 N(7)=15](../sources/outputs/prime_arity/examples/seven_average_sharp_threshold_complete.md)
- [七平均达到 3p+2：对称碰撞总和的完整证书](../sources/outputs/prime_arity/examples/seven_average_three_p_plus_two_threshold.md)
- [为什么三平均的精确阈值是七：资源边界、有限周期与合法单轨道](../sources/outputs/prime_arity/examples/seven_exact_threshold_structure.md)

<!-- END SOURCE doc-7e8635e35480 -->

---

<a id="doc-59c3b8d08b76"></a>

## 原文导签：素数主证明技术附录

来源：`outputs/prime_arity/proofs/README.md` · [逐字节原样副本](../sources/outputs/prime_arity/proofs/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-59c3b8d08b76 -->
# 素数主证明技术附录

按下半带、上半带、尾部与下界分组。各篇是总证明的技术来源；历史状态以素数总入口为准。

[回到成果索引](../sources/outputs/README.md)

- [lower_band/](../sources/outputs/prime_arity/proofs/lower_band/README.md)
- [tail_and_lower_bound/](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/README.md)
- [upper_band/](../sources/outputs/prime_arity/proofs/upper_band/README.md)

<!-- END SOURCE doc-59c3b8d08b76 -->

---

<a id="doc-f07df728cbbe"></a>

## 原文导签：2p到3p：全输入入口与完成证明

来源：`outputs/prime_arity/proofs/lower_band/README.md` · [逐字节原样副本](../sources/outputs/prime_arity/proofs/lower_band/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-f07df728cbbe -->
# 2p到3p：全输入入口与完成证明

依次读无条件入口、端点／奇余量／内部偶余量、两条边界，最后读3p。

[回到成果索引](../sources/outputs/README.md)

- [合数端点核心的统一闭合：有限指数、同余子群与二进根](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md)
- [全部内部偶余量的完整证明：有限逆提升、局部循环与尺度](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md)
- [2p 与 4p 之间：三块运输解掉 3p，并缩小双重值障碍](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_middle_band_structure.md)
- [全部 3p-1 的统一完成与五平均最优阈值](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_three_p_minus_one_completion.md)
- [全部 2p+2：可逆缩放、三步反射与两次 CRT 返回](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_two_p_plus_two_uniform.md)
- [任意素数的奇余量中间核：两个对合、主同余控制与小代表](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_uniform_odd_middle_cores.md)
- [无条件端点与全部奇数中间维数：三单点交换子补齐入口](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)

<!-- END SOURCE doc-f07df728cbbe -->

---

<a id="doc-194ac5f2a052"></a>

## 原文导签：尾部上界与最优性下界

来源：`outputs/prime_arity/proofs/tail_and_lower_bound/README.md` · [逐字节原样副本](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-194ac5f2a052 -->
# 尾部上界与最优性下界

线性阈值第8节给2p反例；逆EGZ及尾部文稿闭合所有较大维数。

[回到成果索引](../sources/outputs/README.md)

- [素数元平均的充分大维数定理](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_averaging_large_dimension.md)
- [统一补齐 4p 上方的 d_p 尾部：N(p)<=3p+10](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_four_p_tail_completion.md)
- [逆 EGZ 真正降低阈值：4p-2+d，以及向 7p/2 推进的具体接口](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_inverse_egz_threshold.md)
- [素数元平均的线性阈值与 2p 边界](../sources/outputs/prime_arity/proofs/tail_and_lower_bound/prime_arity_linear_threshold.md)

<!-- END SOURCE doc-194ac5f2a052 -->

---

<a id="doc-afc8ff23d0fd"></a>

## 原文导签：3p以上：核心、反射与完成证明

来源：`outputs/prime_arity/proofs/upper_band/README.md` · [逐字节原样副本](../sources/outputs/prime_arity/proofs/upper_band/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-afc8ff23d0fd -->
# 3p以上：核心、反射与完成证明

九偏移主文仍保留旧522组版本以便追查；当前精简版先读结构目录的反射区间与单位下降。

[回到成果索引](../sources/outputs/README.md)

- [容量、单位密度与局部提升：全部素数的 3p+10 阈值](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_all_prime_three_p_plus_ten.md)
- [九个低偏移的共同完成：改用大载体与两个等大块](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)
- [上半带与 6 互素维数的完整证明](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_coprime_six_complete.md)
- [上半带四返回：统一双向根与深主同余控制](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_four_return_congruence.md)
- [一次重叠替换载体：统一补齐靠近 4p 的两条边界](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_overlap_completion.md)
- [3p 到 4p：任意素因子数的原位置三值归约](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_three_value_reduction.md)
- [上半带内部区间的无条件完整证明](../sources/outputs/prime_arity/proofs/upper_band/prime_arity_upper_band_unrestricted_completion.md)

<!-- END SOURCE doc-afc8ff23d0fd -->

---

<a id="doc-7bd774674840"></a>

## 原文导签：素数证明的结构与简化

来源：`outputs/prime_arity/structure/README.md` · [逐字节原样副本](../sources/outputs/prime_arity/structure/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-7bd774674840 -->
# 素数证明的结构与简化

当前先读[三个共轭根与浅层提升](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)：奇数n的全部高阶方向／尺度轨道已从九偏移证明中删除，偶数n只保留至多8个二进修正类；统一公式降到p≥83，有限反射证书缩至162组。原180组区间证明保留为前一阶段技术来源。

若先理解构造为何自然出现，读[整格拼接与正运输](../sources/outputs/prime_arity/structure/integral_gluing_and_positive_transport.md)：典范标记决定同余容器；均匀运输表的有限整数扰动统一产生真实逆。它不宣称已消除剩余180组边界证书。

[p进翻译与典范分支](../sources/outputs/prime_arity/structure/padic_places_and_canonical_branches.md)区分平均元数p处和危险ℓ处，证明原子秩一退化、端点合法／非法方向的p进稠密性，以及局部循环与加一机的共轭。另核对典范子群、U_p与特征簇文献；尚未得到可直接用于平均的模形式接口。

后续两项更精确的结构：

- [二次群律、形式对数与轨道缺陷](../sources/outputs/prime_arity/structure/padic_quadratic_group_and_orbit_defect.md)：局部返回是二次代数中的平移，首层缺陷决定所有高层轨道数，统一解释原2／3进条件。已核对180组证书的364个地方。
- [首位乘积与Kneser边界](../sources/outputs/prime_arity/structure/padic_leading_symbols_and_kneser_boundary.md)：任意词首位由交数乘积给出，2p+1恰是不交图首次连通及两步压缩像从一维变二维的阈值；其下一层首位秩同步从1增至2。带全部算术标记的路径提升仍需证明。

[回到成果索引](../sources/outputs/README.md)

- [反射容量的一维整数区间与最小缺失单位：削减九偏移证书](../sources/outputs/prime_arity/structure/carrier_interval_and_unit_descent.md)
- [三个共轭根替代高阶轨道：浅同余层与固定二进修正](../sources/outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)
- [二类型碰撞的整数格证明：同余单类闭包与 3p+1 的三重值分支](../sources/outputs/prime_arity/structure/prime_arity_binary_collision_lattice.md)
- [全碰撞单位分支的统一补回：载体、重叠与整数配比](../sources/outputs/prime_arity/structure/prime_arity_complete_unit_collision_recovery.md)
- [素数元平均在临界维数附近的多种结构](../sources/outputs/prime_arity/structure/prime_arity_critical_structures.md)
- [从统一能量到整数方向下降：2p+2 的一族完整证明](../sources/outputs/prime_arity/structure/prime_arity_energy_and_dyadic_neighbour.md)
- [能量唯一性之后：可改进的不变量与上半带整数出口](../sources/outputs/prime_arity/structure/prime_arity_invariant_improvements_and_core_exit.md)
- [2p+1 与 3p 之间的相对尺度接口](../sources/outputs/prime_arity/structure/prime_arity_middle_band_relative_scale.md)
- [来源关系、动态见证与整数返回阶段：三条改进的证明及边界](../sources/outputs/prime_arity/structure/prime_arity_provenance_dynamic_and_integer_stages.md)
- [允许块形状变化的整数检查点势](../sources/outputs/prime_arity/structure/prime_arity_shape_changing_integer_potential.md)
- [形状变化势：已核对的零和文献与实际适用范围](../sources/outputs/prime_arity/structure/prime_arity_shape_potential_literature_interface.md)
- [重数弱化的锐障碍与一位额外精度的必要性](../sources/outputs/prime_arity/structure/prime_arity_sharp_repetition_and_precision_barriers.md)
- [单值零和：旧猜想撤回与正确结构](../sources/outputs/prime_arity/structure/prime_arity_single_value_zero_sum_conjecture.md)
- [任意素数的碰撞结构：两组相加、总和窗口与高重数分类](../sources/outputs/prime_arity/structure/prime_arity_uniform_collision_structure.md)

<!-- END SOURCE doc-7bd774674840 -->

---

<a id="doc-6a9fda16e26c"></a>

## 原文导签：已使用的核心与均值格工具

来源：`outputs/prime_arity/tools/README.md` · [逐字节原样副本](../sources/outputs/prime_arity/tools/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-6a9fda16e26c -->
# 已使用的核心与均值格工具

这里是历史技术来源；集中后的通用算术引理位于素数目录根部。

[回到成果索引](../sources/outputs/README.md)

- [已解维数怎样组合：统一造零收尾与同余群背后的均值格](../sources/outputs/prime_arity/tools/prime_arity_interpolation_and_lattice_structure.md)
- [中间带的统一整数格、终端族与原位置入口](../sources/outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)
- [临界双块的局部几何、素数幂完整证明与 theta 联系](../sources/outputs/prime_arity/tools/prime_power_endpoint_and_critical_geometry.md)
- [临界双块系统的统一正向控制器：不再搜索种子周期](../sources/outputs/prime_arity/tools/uniform_endpoint_positive_controller.md)

<!-- END SOURCE doc-6a9fda16e26c -->

---

<a id="doc-57cbdfec5f0e"></a>

## 原文导签：三平均：直接证明与原算术路线

来源：`outputs/triple_average/README.md` · [逐字节原样副本](../sources/outputs/triple_average/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-57cbdfec5f0e -->
# 三平均：直接证明与原算术路线

新接手先读[统一三平均主题](../sources/knowledge/topics/triple.md)与[完整证明链](../sources/knowledge/PROOF_ROUTES.md)。后续五元静态分类和七元几何在独立研究目录，已接入[低维主题](../sources/knowledge/topics/subcritical.md)，不要把本目录的历史状态当作当前缺口。

proofs为当前直接证明及基例；arithmetic_cases保留旧逐维数算术成果；history为探索、纠错和未完成的更强结构。

[回到成果索引](../sources/outputs/README.md)

- [arithmetic_cases/](../sources/outputs/triple_average/arithmetic_cases/README.md)
- [history/](../sources/outputs/triple_average/history/README.md)
- [proofs/](../sources/outputs/triple_average/proofs/README.md)

<!-- END SOURCE doc-57cbdfec5f0e -->

---

<a id="doc-3ff251530145"></a>

## 原文导签：三平均旧算术实例

来源：`outputs/triple_average/arithmetic_cases/README.md` · [逐字节原样副本](../sources/outputs/triple_average/arithmetic_cases/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-3ff251530145 -->
# 三平均旧算术实例

这些完整实例保留其独立价值；一般三平均证明已不再依赖逐素数种子。

[回到成果索引](../sources/outputs/README.md)

- [十八元及其三进塔：调用十二元定理的配对归约](../sources/outputs/triple_average/arithmetic_cases/triple_average_eighteen_via_twelve_complete.md)
- [三平均的十一元完整判据](../sources/outputs/triple_average/arithmetic_cases/triple_average_eleven_complete.md)
- [十五元完整判据：模八轮转与可解子块](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifteen_via_subblocks_complete.md)
- [59元完整判据与跨维数结构](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifty_nine_arithmetic_complete.md)
- [53元完整判据：三进根与完整主元同余](../sources/outputs/triple_average/arithmetic_cases/triple_average_fifty_three_arithmetic_complete.md)
- [四十一元完整判据：三因子对合与级41同余证书](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_one_arithmetic_complete.md)
- [四十七元完整判据：尖点平移与局部化根群消元](../sources/outputs/triple_average/arithmetic_cases/triple_average_forty_seven_arithmetic_complete.md)
- [十四元完整判据：图论核心与512类余数桥](../sources/outputs/triple_average/arithmetic_cases/triple_average_fourteen_complete.md)
- [十九元完整判据：通用十五元调用与级19同余子群](../sources/outputs/triple_average/arithmetic_cases/triple_average_nineteen_arithmetic_complete.md)
- [十七元完整判据：正向逆元、级17同余子群与唯一合法尖点](../sources/outputs/triple_average/arithmetic_cases/triple_average_seventeen_arithmetic_complete.md)
- [十三元完整判据：可逆宏、同余子群与有限尖点法](../sources/outputs/triple_average/arithmetic_cases/triple_average_thirteen_arithmetic_complete.md)
- [十二元完整判据：正向宏与指数 12 的模群子群](../sources/outputs/triple_average/arithmetic_cases/triple_average_twelve_arithmetic_complete.md)
- [二十五元完整判据：级25子群与奇数归约的最后小基例](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_five_arithmetic_complete.md)
- [二十九元完整判据：三因子正向周期与级29同余群](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_nine_arithmetic_complete.md)
- [二十三元完整判据：含2因子的正向周期与级23同余子群](../sources/outputs/triple_average/arithmetic_cases/triple_average_twenty_three_arithmetic_complete.md)

<!-- END SOURCE doc-3ff251530145 -->

---

<a id="doc-6512624ce2ea"></a>

## 原文导签：三平均直接证明与小基例

来源：`outputs/triple_average/proofs/README.md` · [逐字节原样副本](../sources/outputs/triple_average/proofs/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-6512624ce2ea -->
# 三平均直接证明与小基例

先读all_dimensions_double_triple_invariant；它覆盖n≥11，另接7、8、9、10元基例。

[回到成果索引](../sources/outputs/README.md)

- [双三重值不变量的任意维数直接证明](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md)
- [任意维数严格归约到素数：低二进重数的最后接口](../sources/outputs/triple_average/proofs/triple_average_all_dimensions_to_primes.md)
- [素数维数的双三重值不变量：一位额外三进精度证明](../sources/outputs/triple_average/proofs/triple_average_prime_double_triple_invariant.md)
- [三平均的新突破：七元与八元的完整判据](../sources/outputs/triple_average/proofs/triple_average_seven_eight_complete.md)
- [三平均的十元完整判据](../sources/outputs/triple_average/proofs/triple_average_ten_complete.md)
- [全部二三光滑维数的完整判据](../sources/outputs/triple_average/proofs/triple_average_two_three_smooth_complete.md)

<!-- END SOURCE doc-6512624ce2ea -->

---

<a id="doc-1f00cb7484b5"></a>

## 原文导签：独立研究入口

来源：`research/prime_arity_padic/README.md` · [逐字节原样副本](../sources/research/prime_arity_padic/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-1f00cb7484b5 -->
# 独立研究入口

这里保存原完成证明之后的改进，以及五元、六元、七元的算术研究。技术稿和原位置验证文件均保留；本入口不再追加“最新进展”时间线。

**先读[统一接手页](../sources/knowledge/START_HERE.md)及[当前状态](../sources/knowledge/STATUS.md)。** 本目录全部技术文稿已经关联结论卡、后续替代与核验命令。

| 主题 | 当前入口 |
|---|---|
| 素数证明：从三共轭根到列修正、有限对应和共同反射 | [素数主题](../sources/knowledge/topics/prime.md) |
| 五元完整算法与尚未完成的静态算术分类 | [低维主题](../sources/knowledge/topics/subcritical.md) |
| 七元范数、尖点与全维数根格解释 | [三平均主题](../sources/knowledge/topics/triple.md) |
| 外部定理、旧Hecke路线与复制／窗口限制 | [公共接口](../sources/knowledge/topics/interfaces.md) |
| 结论到程序的对应 | [核验说明](../sources/knowledge/VERIFICATION.md) |
| 按文件追溯全部历史 | [文件清单](../sources/knowledge/DOCUMENTS.md) |

本目录的“已证明”默认是文稿已有一般论证，不表示全部新结论均已独立审稿或纳入冻结主证明。原阈值定理已经完整；保留114组根资源、统一奇数下半带等属于具体改进范围，不能与旧基线162组计数混用。

继续研究前：

```text
python knowledge/project_knowledge.py context "对应关键词"
```

原先累计入口已完整保存在[整理快照](../sources/work/documentation_memory_20260917/originals/research/prime_arity_padic/README.md)中，仅作原始版本恢复。数学稿与证书未搬动。新的阅读顺序与状态统一在 `knowledge/catalog.json` 维护。

<!-- END SOURCE doc-1f00cb7484b5 -->

---

<a id="doc-4444d71b4138"></a>

## 原文导签：五元环面研究的外部定理记录

来源：`research/prime_arity_padic/five_torus_literature_20260917/README.md` · [逐字节原样副本](../sources/research/prime_arity_padic/five_torus_literature_20260917/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-4444d71b4138 -->
# 五元环面研究的外部定理记录

2026-09-17。本目录保存实际使用的外部来源，以及后续定向查询和适用性核对记录。新增调查先读[六份全文与相关问答的适用性审查](../sources/research/prime_arity_padic/five_torus_literature_20260917/targeted_review_20260917.md)；其中不适用的定理没有被引作证明。

**后续连分数／Hecke调查：** [Lucas赋值与共同Hecke周期](../sources/research/prime_arity_padic/five_torus_literature_20260917/switch_hecke_review_20260917.md)。Aka–Shapira的不分裂素数情形确实适用于本题零方向的拉回，给普通连分数周期等分布；Murru–Sanna赋值公式给D=1族第一段长度。两项均不直接解决任意切换的固定D有限性。记录了实际稿件版本、期刊年份纠正和不能引用的公式提取缺失。

**统一逃逸方向：** [ESS多参数归约与Baker有效增长](../sources/research/prime_arity_padic/five_torus_literature_20260917/uniform_escape_review_20260917.md)。ESS此次通过极小零子和把固定多块模板的指数解集化成有限个格陪集，再由本题实能量／三进谱排除恒值非负射线。固定混合周期另用正式转述的Baker–Wüstholz推论给有效指数增长。分形逼近资料虽相关，未直接适用，不作为全词逃逸的证明。

**来源：** J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics **155 (2002), 807–836**。arXiv上传日期2004不是正式出版年份。

- [arXiv作者稿PDF](https://arxiv.org/pdf/math/0409604)
- [本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/evertse_schlickewei_schmidt_2002.pdf)
- [提取文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/evertse_schlickewei_schmidt_2002.txt)
- [访问URL、字节数及SHA256](../sources/research/prime_arity_padic/five_torus_literature_20260917/source.json)

实际读取：第807页摘要／定义，第808页定理1.1，第809页两变量先前界，第810—811页关于S单位及有限生成群的适用说明。没有声称重审全部证明。

**所用结论：** 特征0域中有限秩乘法群Γ⊂(K^×)^n，方程Σa_i x_i=1的非退化解有限。原定理还给仅依n及秩的显式上界；最初相邻S单位研究只用有限性，后续固定周期返回定理使用其参数一致上界，不将巨大上界用作实际搜索截止。

**本题代入：** F=Q(√5)，S有限且含所有无穷位与2、3上方素位，Γ=(O_(F,S)^×)²，n=2，a_1=a_2=1。群为有限秩，非零两项的和为1自动无零真子和，因此所有相关解均非退化。先由J(γ)=−(2γ+1)/(γ+2)及2(γ+2)−(2γ+1)=3，证明γ、Jγ均为S单位迫使2γ+1也是S单位；然后应用定理，不能省略这段归约。

**结论边界：** 只证明固定S内相邻环面点对有限，不枚举它们、不宣称高效可计算界、不把这条有限性当成平均可解判据。原位置数值的分母仍只含3；这里的辅助素数由环面有理坐标引入。

前期宽泛题录查询含无关结果，未用作证明。下载后的Python PDF解析库不可用，实际以本机pdftotext提取成功；原PDF保存并校验文件头，不因最初文本提取失败而重复声称阅读。

## Baker--Brumer定理的正式转述

Adel Betina, Mladen Dimitrov, *Geometry of the eigencurve at CM points and trivial zeros of Katz p-adic L-functions*, Advances in Mathematics **384 (2021),107724**，DOI [10.1016/j.aim.2021.107724](https://doi.org/10.1016/j.aim.2021.107724)。取得arXiv:1907.09422v3作者稿：

- [公开PDF](https://arxiv.org/pdf/1907.09422)
- [本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/eigencurve_cm_baker_brumer_2021.pdf)、[文本](../sources/research/prime_arity_padic/five_torus_literature_20260917/eigencurve_cm_baker_brumer_2021.txt)
- [访问与SHA256记录](../sources/research/prime_arity_padic/five_torus_literature_20260917/eigencurve_cm_source.json)
- [已目视核对的第8页](../sources/research/prime_arity_padic/five_torus_literature_20260917/baker_brumer_statement_page8.png)

实际阅读：摘要／标题信息，§1.5定理1.6及相关定义，引用表中[7]。定理1.6说明相应p进对数在Q上线性独立可提升到Qbar上线性独立；文本提取会把两种Q都显示为Q，所以已渲染原页并目视核对横线。

原始来源为A. Brumer, *On the units of algebraic number fields*, Mathematika **14 (1967),121–124**，本轮只取得题录而未取得原全文。因此本项目引用的是正式论文中的标准定理转述，没有声称重新证明／全文审查Brumer定理。

**本题代入：** α∈Q(√5)的范数1主单位、ρ=ε⁴。若α的最小整环分母D>1，则其某个素位赋值非零、而ρ处处单位，故α与ρ乘法独立。3进log在该主单位群上单射，得到两个对数Q线性独立；定理推出它们Qbar线性独立，因而log_3α/log_3ρ超越。没有使用文中强四指数猜想、六指数定理、eigencurve几何或p进L函数结论。

## Skolem–Mahler–Lech零点定理的标准转述

Jason P. Bell, Jeffrey C. Lagarias, *A Skolem–Mahler–Lech theorem for iterated automorphisms of K-algebras*, Canadian J. Math.67(2) (2015),286–314，DOI[10.4153/CJM-2013-048-3](https://doi.org/10.4153/CJM-2013-048-3)。

- [作者稿](https://arxiv.org/pdf/1312.5305)、[本地PDF](../sources/research/prime_arity_padic/five_torus_literature_20260917/bell_lagarias_skolem_mahler_lech_2013.pdf)、[来源与阅读范围](../sources/research/prime_arity_padic/five_torus_literature_20260917/skolem_mahler_lech_source.json)。
- 实际读：作者稿前三页，引言§1.1的经典递推零点定理1.3；未调用较强的K代数自同构结果。
- 只应用于固定M时Q_5(M^nx)−c的线性递推。配合不同特征根比不是单位根，零点有限；不由此宣称有效截止，更不应用于任意变化的平均词。

后续[固定周期返回文稿](../sources/research/prime_arity_padic/five_fixed_D_effective_sparsity_and_periodic_return_20260917.md)以ESS给统一有限次数，SML为另一有限性证明。最新[有界切换文稿](../sources/research/prime_arity_padic/five_bounded_switches_and_correspondence_degree_20260917.md)独立使用初等紧致性，不需要以上深定理。

<!-- END SOURCE doc-4444d71b4138 -->

---

<a id="doc-292e4ad8ae5c"></a>

## 原文导签：七元算术几何：实际阅读、外部接口与自足证明

来源：`research/prime_arity_padic/seven_geometry_literature_20260917/README.md` · [逐字节原样副本](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-292e4ad8ae5c -->
# 七元算术几何：实际阅读、外部接口与自足证明

2026-09-17。本轮以已有七元结构证明为主要数学来源，并核对尖点／模形式标准资料。没有向外发送消息。宽泛题录搜索部分429或无关，原始结果保存在query_*.json；不据其断言文献不存在。

## 1. 项目内直接读取并重核的基础

- [七元端点结构证明](../sources/outputs/prime_arity/examples/seven_exact_threshold_structure.md)：第1—5节，包括两步入口、三宏周期、全部Γ₀(7)陪集回路及终端。第6节一般p的历史“未解”状态按文首后续说明理解。
- [原七／八元证明](../sources/outputs/triple_average/proofs/triple_average_seven_eight_complete.md)：七元范数与宏部分。原十八词覆盖不是本轮充分性证明的依赖。
- [统一端点控制器](../sources/outputs/prime_arity/tools/uniform_endpoint_positive_controller.md)：原位置返回、正向逆与局部化根的公式；七元只用既有短周期特例。
- [G障碍模](../sources/research/prime_arity_padic/G_as_obstruction_group_and_stable_threshold_20260916.md)：G的仿射格、余核、操作满射及目标饱和的量词。
- [早期算术几何整理](../sources/outputs/triple_average/history/triple_average_arithmetic_geometry_view.md)：能量型、判别式以及“类数不能自动决定可达性”的边界。

已重跑原七元结构核验器，不修改原文件。新增核验进一步将一般Bezout矩阵作Euclid／Schreier改写并重放实际位置操作。

本目录向outputs的相对路径需经过research/prime_arity_padic/子目录；以上链接在提交前按实际文件位置核对。

## 2. Sage官方文档：尖点与亏格的标准交叉核对

- [Γ₀(N)文档](https://doc.sagemath.org/html/en/reference/arithgroup/sage/modular/arithgroup/congroup_gamma0.html)：实际读ncusps条目，素数level均有两个尖点；[本地页面](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/sage_gamma0.html)、[来源](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/sage_gamma0_source.json)。
- [Arithmetic subgroup文档](https://doc.sagemath.org/html/en/reference/arithgroup/sage/modular/arithgroup/arithgroup_generic.html)：实际读cusp_width和genus条目。前者示例显示Γ₀(11)的∞宽1、0宽11；后者Γ₀(n)表确认n=7亏格0。[本地页面](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/sage_arithmetic.html)、[来源](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/sage_arithmetic_source.json)。

七元两个轨道与宽度1、7在新文稿中用Bezout和矩阵直接证明，不依赖运行Sage。亏格0仅作模曲线背景，不用于G充分性推理。没有在当前Python环境假装安装或执行Sage。

## 3. Stein书：实际读取的Eisenstein模性定理

William Stein, *Modular Forms, a Computational Approach*，在线章节[Eisenstein Series and Bernoulli Numbers](https://wstein.org/books/modform/modform/eisenstein.html)。

- [保存页面](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/stein_eisenstein.html)、[带公式的可读文本](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/stein_eisenstein_readable.txt)、[来源散列](../sources/research/prime_arity_padic/seven_geometry_literature_20260917/stein_eisenstein_source.json)。
- 实际读“Explicit Basis for the Eisenstein Subspace”，公式(4)、Theorem5.8及附近的定义和常数项。该页公式使用图片alt文本，已将alt恢复入可读文本；不把丢失公式的普通HTML去标签结果当成完整陈述。
- 定理5.8：原始Dirichlet特征χ、ψ满足χ(−1)ψ(−1)=(−1)^k时，除weight2平凡特征例外，所定义E_(k,χ,ψ)(q^t)属于对应level和特征的模形式空间。
- 本题k=1、χ=1、ψ=χ₋₇、t=1，故theta计数恒等式识别出的2E_(1,1,χ₋₇)为level7、weight1、特征χ₋₇的模形式。

本页一般模性引用Stein对Miyake第7章结论的整理；没有取得并重审Miyake原章证明。系数恒等式、Euclidean环、理想范数计数在研究正文中自足证明。未引用该章其它basis/eigenform断言作为额外必要依赖。

另读取[dimension formulas章节](https://wstein.org/books/modform/modform/dimension_formulas.html)的权重适用范围；未将k≥2的公式用于本题weight1。保存页面和来源仅用于记录这次适用性检查。

## 4. 取得但不作为数学来源的材料

LMFDB尝试页面返回HTTP200但只有650字节、无可用曲线数据，故不引用；记录见lmfdb_7_source.json。最初猜测的Stein章节URL404，后从书目录定位到实际Eisenstein章节，错误访问保留在stein_modular_source.json。

取得Sage二元二次型页面，但本文没有借其算法或输出证明类数；Q(√−7)范数Euclidean性有11/16覆盖界的直接证明。因此不把下载文件视为已引用的定理。

## 5. 本轮结论的来源边界

- 七元可平均当且仅当G=1：已有项目定理，本轮用结构版重新接通。
- 指定宏菜单恰生成𝔅₇(Z[1/6])：由既有根与整数群包含新增R点补齐证明。
- 分歧素理想单位条件、两个尖点轨道、能量层本原表示公式：正文直接证明。
- theta级数的模性：引用已读Stein Theorem5.8；不是可达性证明前提。

因此本轮不是借“模曲线／自守形式”替代真实操作，而是标明它们与真实操作已经能够严格对接的七元实例。

<!-- END SOURCE doc-292e4ad8ae5c -->

---

<a id="doc-c244d247ecef"></a>

## 原文导签：计算材料与核验入口

来源：`work/README.md` · [逐字节原样副本](../sources/work/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-c244d247ecef -->
# 计算材料与核验入口

这里保留全部原核验器、证书、搜索脚本和历史缓存。文件名 `verify_` 本身不决定数学证据强度；请按结论检索。

```text
python knowledge/project_knowledge.py verify TRIPLE-ALL
python knowledge/project_knowledge.py verify PRIME-ODD-PENCIL
python knowledge/project_knowledge.py verify FIVE-TEMPLATE-ESCAPE
```

这些命令只展示对应脚本、记录与证明边界，不启动计算。新的独立研究脚本在 `research/prime_arity_padic/`，现在同样可以从这个入口找到。

原完成项目的执行器和185项登记保持原样：

```text
python work/run_verifications.py --list
python work/run_verifications.py --id seven-endpoint-structure
python work/run_verifications.py --profile prime-proof
```

`prime-proof` 仍对应原冻结证明版本，不假装已经执行后续所有独立简化。[原注册](../sources/work/verification_manifest.json)记录每项检查的 `evidence_scope` 和 `does_not_establish`；[统一核验说明](../sources/knowledge/VERIFICATION.md)解释两套登记如何衔接。

搜索器的阴性输出不证明不可达，有限样本不承担无穷量词，JSON结果的存在也不等于本轮已重跑。接手先读[当前数学状态](../sources/knowledge/STATUS.md)，不要据旧文的阶段性“未解”重开已完成任务。

旧版长核验日志完整保存在[原导航快照](../sources/work/documentation_memory_20260917/originals/work/README.md)，用于溯源和恢复；具体脚本和证书没有移动。源码与正文的当前关联见[文档清单](../sources/knowledge/DOCUMENTS.md)。

<!-- END SOURCE doc-c244d247ecef -->

---

<a id="doc-ef29dd2e6627"></a>

## 原文导签：Arena三平均网页审阅

来源：`work/arena_triple_solver_review/README.md` · [逐字节原样副本](../sources/work/arena_triple_solver_review/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

旧核验ID：`arena-triple-solver-review`

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-ef29dd2e6627 -->
# Arena三平均网页审阅

来源与完整结论见 ../../outputs/algorithms/arena_triple_solver_review.md。这里只保存外部网页快照、未改动的计算函数和独立审阅工具，不替换项目正式求解器。

快速核验（不访问网络、不重新计时）：

~~~text
python work/arena_triple_solver_review/verify_saved_review.py
~~~

重新做同题基准，必须串行执行以下步骤，避免计时相互干扰：

~~~text
python work/arena_triple_solver_review/benchmark_arena.py --output comparison_single.json
python work/arena_triple_solver_review/remeasure_baseline.py
python work/arena_triple_solver_review/check_structure.py
python work/arena_triple_solver_review/check_warm_and_macros.py
python work/arena_triple_solver_review/verify_saved_review.py
~~~

完整网页束搜索复测约需数分钟；每题有独立16秒外部保护，超时不表示不可达。原网页单题预算9000ms、批量预算1500ms不是同一配置，主报告使用单题默认配置。benchmark_arena.py 的 --batch 选项仅用于另行诊断。

frame1.html 是实际浏览器iframe渲染后的快照；arena_solver.js 是其中计算部分的原文，统一LF换行，并由 provenance.json 的SHA256绑定。page.html 和 frame0.html 是Arena外壳，不包含被审阅的求解算法。

run_arena.cjs 只运行已经读取检查的计算段，放在Node VM Worker中，不执行原页面网络脚本或DOM事件。外部Worker是审阅隔离工具；原网页本身没有把求解放进Worker。

comparison_single.json：48个历史同题和4个额外示例；baseline_current.json：旧算法同机串行复测；warm_small.json：同一个JS上下文的24题预热复测；structure_checks.json：缩放和预算问题；macro_basis_checks.json：33个独立宏基重放；summary.json：从记录重新计算的统计。

读取大整数原题请使用Python整数或无损JSON工具，避免将JSON数值直接转成JavaScript Number。提供给网页算法的所有输入都通过十进制字符串转BigInt。

审阅结论属于有限性能和实现检查，不是新的平均可达性数学定理。历史数学项目和其他AI同时进行的研究不受这组文件影响。

<!-- END SOURCE doc-ef29dd2e6627 -->
