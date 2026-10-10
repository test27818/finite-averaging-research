"""One-time, human-curated migration record. Do not rerun over later catalog edits."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[2]
RESEARCH='research/prime_arity_padic/'
cards=[]

def card(key,title,topic,status,scope,boundary,docs,*,deps=(),related=(),updates=(),old=(),
         check=None,records=(),assumptions=(),next_step='',aliases=(),sources=()):
    docs=[d if '/' in d else RESEARCH+d+'.md' for d in docs]
    local=[]
    if check:
        argv=['python',RESEARCH+check]
        if key=='FIVE-TEMPLATE-ESCAPE':argv+=['--return-depth','18']
        local=[{'argv':argv,'level':'symbolic-check / finite-sanity',
                'scope':'核对本文恒等式、接口或有限实例；一般量词由书面证明及注明的外部定理承担。不是独立审稿。',
                'records':[RESEARCH+p for p in records]}]
    c={'id':key,'title':title,'topic':topic,'status':status,'scope':scope,'boundary':boundary,
       'documents':docs,'depends_on':list(deps),'related':list(related),
       'updates':[{'id':i,'scope':s} for i,s in updates],'verification_ids':list(old),
       'local_checks':local,'assumptions':list(assumptions),'next_step':next_step,
       'aliases':list(aliases),'source_records':list(sources),
       'source_hashes':{d:hashlib.sha256((ROOT/d).read_bytes()).hexdigest() for d in docs}}
    cards.append(c)

card('TRIPLE-ALL','三平均 n≥7 的完整G判据','triple','proved-source',
     '非全等输入中心化、本原化后，可达全等 ⇔ G为3幂。n≥11同一双三重直接证明，接7—10基例。',
     '判定已解决；不等于最短路径或可变n统一多项式构造长度已解决。',
     ['outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md'],
     deps=['TRIPLE-BASES','G-OBSTRUCTION'],old=['all-dimensions-double-triple-invariant'],
     related=['GEOMETRY-ALL-N','ALG-LENGTH'],aliases=['三平均 任意n 已证明','一位额外三进精度 双三重','direct double triple'])
card('TRIPLE-BASES','三平均7、8、9、10基例与适用范围','triple','proved-source',
     '7元已有无十八词覆盖的结构证明；8元Euclid下降；9元三幂网络；10元精确局部—实宏覆盖。',
     '不能将10元有限证书说成全凭几何；七元新版不依赖旧十八词搜索。',
     ['outputs/triple_average/proofs/triple_average_seven_eight_complete.md','outputs/triple_average/proofs/triple_average_ten_complete.md'],
     related=['SEVEN-STRUCTURE'],aliases=['七元 八元 九元 十元 基例'],
     old=[])
card('SEVEN-STRUCTURE','七元：真实正向逆与完整 Γ₀(7) 控制','triple','proved-source',
     '两步安全入口、三种实际返回的标量周期、根群与八陪集改写、合法单尖点轨道和四步尾部。',
     '七元作为全系统才共享目标均值；嵌入较大系统不可免费当作全局射影逆。',
     ['outputs/prime_arity/examples/seven_exact_threshold_structure.md'],
     old=['seven-endpoint-structure'],related=['SEVEN-GEOMETRY','WINDOW-MEAN'],
     aliases=['3平均7元 Gamma0(7) 正向周期 18词'])
card('G-OBSTRUCTION','G的障碍模、Smith余核与目标饱和','interfaces','proved-local',
     'O_p(X)=坐标R理想/差分R理想；其阶为G非p部分，沿操作有逆向满射。复制稳定条件对所有n成立。',
     'G不是保持不变的动态量；新障碍可以产生。目标可达性不能扩大成任意运输矩阵分解。',
     ['G_as_obstruction_group_and_stable_threshold_20260916'],
     check='verify_G_obstruction_group.py',records=['G_obstruction_group_verification.json'],
     related=['STABILIZATION','GEOMETRY-ALL-N'],aliases=['G条件 仿射格 obstruction Smith 判别群'])
card('STABILIZATION','正双随机运输与3幂复制稳定化','interfaces','proved-source',
     '任意n：G为3幂 ⇔ 存在严格正三进双随机P消去X ⇔ 某个3幂复制后真实可达。',
     '原位置分解不随运输存在自动成立；五、六元有复制后成功而原态失败。n≥7复制消去可由已证总定理推出，不是独立新证明。',
     ['outputs/triple_average/history/triple_average_stabilization_theorem.md'],old=['stabilization-theorem'],
     aliases=['3-copy cancellation 复制消去 正运输 doubly stochastic'])
card('GEOMETRY-ALL-N','全部n的根格、局部根基与零目标饱和','triple','synthesis',
     'G是A_(n−1)中本原向量的配对理想；危险素位为对角根基；A₂投影及实际见证下降统一解释已有定理。',
     '不是新纯同余群证明。一般G合法不等于范数为单位；n=11有能量22、G=1的可解例子。',
     ['triple_all_n_root_lattice_and_target_saturation_20260917'],deps=['TRIPLE-ALL','SEVEN-GEOMETRY'],
     check='verify_triple_all_n_geometric_synthesis.py',records=['triple_all_n_geometric_synthesis_verification.json'],
     aliases=['全维数 算术几何 root lattice radical 2p+1 统一'])
card('SEVEN-GEOMETRY','七元G、分歧范数、尖点与Eisenstein的完整对接','triple','proved-local',
     '指定宏群恰为PGL₂(Z[1/6])模7上三角子群；G=1等价合法尖点及Q(√−7)分歧单位，theta与本原能量层有显式计数。',
     '七元可达性是已有结果；theta计数和类数一不能替代真实正向宏。非全局窗口不能直接推广。',
     ['seven_averaging_cusps_norm_and_eisenstein_20260917'],deps=['SEVEN-STRUCTURE','G-OBSTRUCTION'],
     check='verify_seven_arithmetic_geometry.py',records=['seven_arithmetic_geometry_verification.json'],
     sources=[RESEARCH+'seven_geometry_literature_20260917/README.md'],
     assumptions=['theta模性引用已读Stein Theorem5.8；轨道与范数恒等式在正文证明'],
     aliases=['七元 模曲线 cusp Iwahori 虚二次 Eisenstein theta'])
card('PRIME-TOTAL','所有奇素数平均的最优最终阈值','prime','proved-source',
     '所有奇素数p：N(p)=2p+1，阈值以上G为p幂充要；N(2)=4。原主证明覆盖表完整。',
     '已完成存在性不等于新统一无证书证明或通用高效群词提取。162组是冻结基线，后续独立简化不自动重写它。',
     ['outputs/prime_arity/proof.md','outputs/prime_arity/arithmetic_toolkit.md','outputs/prime_arity/verification.md'],
     deps=['EXTERNAL-ARITH'],old=['prime-final-independent-audit','transverse-root-shallow-lifting'],
     related=['PRIME-NATURAL-UNIFICATION','PRIME-ODD-PENCIL','PRIME-FINITE-TERMINAL'],
     assumptions=['Morris有限指数与有理S整数SL₂强同余子群性质','原小参数有限资源证书'],
     sources=['outputs/prime_arity/proof_map.json'],aliases=['p平均 完全证明 2p+1 3p+10 4p 162 522 180'])
card('PRIME-NATURAL-UNIFICATION','自然统一的当前缺口：初始物理资源与退化出口','prime','open',
     '原阈值已证。独立研究的目标是统一2p<n<4p资源供应并替代小参数根记录；奇数下半带已有共同反射。',
     '不能再把根／尖点／种子逐素数寻找当作原可达性缺口；也不能先借深核证明其自身资源。',
     ['unified_stable_range_saturation_candidate_20260916','small_parameters_lattice_defects_and_closure_target'],
     related=['PRIME-ODD-PENCIL','PRIME-FINITE-TERMINAL','PRIME-FIBER','PRIME-GEOMETRY'],
     check='verify_small_parameter_resource_scope.py',records=['small_parameter_resource_scope.json'],
     next_step='容量内有效作用与安全跨格准备的一般存在性，且与深核启动无循环依赖；不要求每条出口路径都终止。',
     aliases=['整体关联 自然统一 四色定理 83 小p 小参数 退化出口'])
card('EXTERNAL-ARITH','Morris／Serre外部定理的审核与边界','interfaces','proved-source',
     '原素数证明所需有限指数、强同余性质及无限单位前提的明确引用接口。',
     '已读来源与未取得原文须按审查文稿保留；有限模像满不推出全群包含。',
     ['outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md',
      'outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md'],
     old=['endpoint-congruence-completion'],aliases=['Morris Serre CSP 外部定理 同余子群 有限指数'])
card('OLD-HECKE-AUDIT','旧Ihara–Hecke／Manin接入的修正','interfaces','corrected',
     '保存原Hecke关系、星结构、中心符号及物理分支提升的审计；旧直接闭合推断不可作为定理使用。',
     '不否定全部自守方法；七元实群、五元Aka–Shapira接口必须按各自已证前提使用。',
     ['outputs/triple_average/history/triple_average_final_hecke_audit.md'],
     old=['final-hecke-manin-audit'],related=['SEVEN-GEOMETRY','FIVE-HECKE'],
     aliases=['Ihara Hecke 饱和 Manin 分支之和 星结构 modular form'])
card('WINDOW-MEAN','局部窗口的均值与相对尺度障碍','interfaces','proved-source',
     '子块差分缩放只围绕子块自身均值，外部位置不跟随；不能当作整系统射影逆。',
     '重写仿射矩阵或换称标记格不会自动提供窗口拼接定理。',
     ['outputs/prime_arity/structure/prime_arity_middle_band_relative_scale.md'],
     related=['GEOMETRY-ALL-N'],aliases=['窗口 嵌入 局部均值 相对尺度 外部总和'])
card('OLD-TRACE-RETURN','统一／双／混合迹零返回的历史接口','interfaces','partial',
     '参数化周期和部分根公式成立；指定返回的原位置分解是更强目标，旧单返回充分性曾过强。',
     '原可达性已由别的路线完成；运输／复制证书不是这些指定矩阵的原位置分解。',
     ['outputs/triple_average/history/triple_average_universal_trace_zero_target.md',
      'outputs/triple_average/history/triple_average_two_trace_zero_returns.md',
      'outputs/triple_average/history/triple_average_mixed_singleton_controller.md'],
     related=['STABILIZATION','OLD-HECKE-AUDIT'],aliases=['迹零 返回 种子 非分裂 原位置分解'])
card('ALG-LENGTH','构造长度与最短路径的不同状态','algorithms','partial',
     '三平均直接算法有数值界和固定n位长多项式界；原求解器、精确IDA*和最短路径困难分别登记。',
     '可变n统一多项式构造长度未证；最短性NP困难不否定非最优多项式路径可能性。',
     ['outputs/algorithms/triple_average_sequence_length_analysis.md','outputs/algorithms/pair_triple_solver_comparison_and_optimality.md'],
     old=['double-triple-sequence-length','pair-triple-solver-optimality'],
     aliases=['操作数 最短 长度 polynomial NP complete IDA* 复杂度'])
card('ALG-WEB','网页求解器与效率比较的证据范围','algorithms','partial',
     '保存Arena源码审阅、同题精确重放、批量计时及二平均HTML比较。',
     '有限随机速度优势不证明最坏复杂度；预算搜索失败不是数学反例。',
     ['outputs/algorithms/arena_triple_solver_review.md','outputs/algorithms/averaging_algorithm_benchmark.md'],
     old=['arena-triple-solver-review'],aliases=['网页 求解器 Arena 性能 2-average-solver'])
card('COMPOSITE-FRONTIER','一般元数三项主任务与GRH范围','composite','partial',
     '无条件全部k的2k+1端点；奇素数幂奇数中间维数；GRH下平方族与2、3幂临界点。',
     '不等于一般N(k)=B(k)。p≥5高奇次幂临界、混合素因子临界及整段接续仍未全闭合。',
     ['outputs/general_arity/general_k_three_tasks_progress_20260915.md','outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md'],
     assumptions=['部分临界结果依赖Dirichlet L函数GRH，不能删条件'],
     related=['COMPOSITE-DEFINITIONS'],aliases=['合数 k平均 GRH 平方 高奇次幂 临界'])
card('COMPOSITE-DEFINITIONS','M、H、N与自动G维数不能混用','composite','synthesis',
     'M最早成功、H首个非自动G成功、N此后全部成立，是不同量词；六平均九元自动成功，十元是非自动G点。',
     '历史全局表中的开放范围以COMPOSITE-FRONTIER更新；未将候选临界线推广成已证最终阈值。',
     ['outputs/general_arity/averaging_global_status_20260912.md','outputs/general_arity/composite_critical_scale_and_conjecture.md'],
     old=['composite-critical-scale'],aliases=['q+S(q) Bq M H N 自动G 6平均9 6平均10'])

# Every independent top-level research note is assigned a curated card below.
card('PRIME-MOVE-MERGE','任意元数的移动见证—双块入口','prime','proved-local',
     'k≥2、n≥2k+1，完整危险素数见证可保留到两个k重块加剩余单点。',
     '入口完整不等于核心内终止；单载体格障碍仍需不同资源。',
     ['move_witnesses_then_merge'],check='verify_carrier_balance.py',records=['carrier_balance_verification.json'],
     related=['PRIME-CARRIER-OBSTRUCTION'],aliases=['入口 move witnesses merge 两个p块'])
card('PRIME-CARRIER-OBSTRUCTION','单载体正词的p进Smith形障碍','prime','proved-local',
     'm≥2差分空间中任意k步单载体词的Smith形为diag(p^−k,1,…,1)，排除全空间非空标量周期。',
     '不排除更小输入像的返回或多载体宏；有限模逆不等于真实有理逆。',
     ['carrier_balance_and_uniform_mechanism'],check='verify_carrier_balance.py',records=['carrier_balance_verification.json'],
     aliases=['单载体 Smith 不能取逆'])
card('PRIME-BALANCE','对称尺度配平与载体更新正常形','prime','partial',
     '已有成功分支可提取全系统配平及四步返回正常形；单独对称对角资源不足以给横向控制。',
     '早期4|t缺口已由全偶载体定理补齐；不将本卡旧范围作为当前缺口。',
     ['local_proofs_to_global_balance','carrier_refresh_normal_form'],
     check='verify_symmetric_rebuild.py',records=['symmetric_rebuild_verification.json'],
     related=['PRIME-EVEN-INVERSE'],aliases=['配平 载体更新 refresh symmetric'])
card('PRIME-EVEN-INVERSE','全部偶载体的一致正向逆','prime','proved-local',
     '所有奇素数p、1≤t<p的(p,p,2t)核心都有同一十二步非零标量闭路。',
     '可逆资源不等于完整根群、入口和终端统一。',
     ['uniform_even_carrier_inverse'],check='verify_uniform_even_carrier_inverse.py',records=['uniform_even_carrier_inverse_verification.json'],
     updates=[('PRIME-BALANCE','补齐原4整除t分支，替代仅部分偶载体的取逆范围')],aliases=['偶载体 十二步 统一取逆'])
card('PRIME-OUTPUT-ROOT','固定来源交换输出产生真实剪切','prime','proved-local',
     '从已有可逆返回的输出差获得明确非零根，记录模板容量边界。',
     '两矩阵不交换不自动有根；一个根不自动有本原根理想或完整轨道。',
     ['output_exchange_produces_roots'],deps=['PRIME-EVEN-INVERSE'],
     check='verify_output_exchange_roots.py',records=['output_exchange_roots_verification.json'],aliases=['输出交换 根 剪切 非交换'])
card('PRIME-SQUARE-ZERO','已有深核后的平方零一次同余编译','prime','proved-local',
     '在整族根与精确深核已真实存在前提下，把模h²修正压成模h的一项标量同余。',
     '不制造初始根族，不证明资源存在；不得循环依赖深核。',
     ['square_zero_hensel_compiler'],check='verify_square_zero_compiler.py',records=['verification_results.json'],
     aliases=['平方零 Hensel 编译 深核'])
card('PRIME-CERTIFICATE-ANATOMY','旧九偏移证书与p≥83公式的解剖','prime','historical',
     '解释原162=18×9参数记录的物理计数、根理想、方向与单位字段，以及旧p≥83范围。',
     '最新研究已经删除多项字段；本卡解释冻结基线，不能当最新剩余清单。',
     ['certificate_anatomy_and_odd_offsets','uniform_reflection_formula'],related=['PRIME-FIVE-RETURNS','PRIME-SPLIT-COLUMNS'],
     aliases=['162 83 九偏移 证书 anatomy 统一公式'])
card('PRIME-DYADIC','以统一列提升替代旧二进轨道表','prime','proved-local',
     '旧内部偶余量64、256类表由同一个手写二进列提升引理替代；区分终端控制与物理资源。',
     '当时162组根／方向记录的未替代范围须按后续卡更新。',
     ['structural_reassessment_and_uniform_dyadic_orbits'],check='verify_uniform_dyadic_column_lifting.py',
     records=['uniform_dyadic_column_lifting_verification.json'],related=['PRIME-TWO-ROOTS','PRIME-SPLIT-COLUMNS'],
     aliases=['二进 64 256 轨道表 dyadic'])
card('PRIME-TERMINAL-FAN','移动终端替代额外单位补充','prime','proved-local',
     '两个／四个终端代替单一目标，删除45组binary_unit及(13,3)的97/13补充用途。',
     '本阶段仍保留root_pairs、direction和(11,3)辅助13，后两者有后续替代。',
     ['terminal_fan_replaces_dyadic_units'],check='verify_terminal_fan.py',records=['terminal_fan_verification.json'],
     updates=[('PRIME-CERTIFICATE-ANATOMY','取消binary_unit字段及97/13特例的终端用途')],aliases=['终端扇 binary_unit 97/13'])
card('PRIME-TWO-ROOTS','两根直接修正列，避免提升整个群','prime','proved-local',
     '把sl₂三方向目标降为当前列二维作用；116组direction可由旧根生成，46组当时保留二进条件。',
     '不移除初始根资源与深核；46组后由分裂乘法完成。',
     ['two_root_column_completion'],deps=['PRIME-TERMINAL-FAN'],check='verify_two_root_column_completion.py',
     records=['two_root_column_completion_verification.json'],updates=[('PRIME-DYADIC','终端改为只修当前列，无需原三共轭浅核')],
     aliases=['两根 列修正 116 46 三共轭 column'])
card('PRIME-SPLIT-COLUMNS','分裂乘法完成全部方向与二进修补','prime','proved-local',
     '旧等块互补混合的对角乘法完成162组列输送，不再需要direction、binary_unit或二进迹条件。',
     '根反射、深核和物理供应仍须独立存在；(11,3)辅助13由下一卡处理。',
     ['split_torus_completes_all_directions'],deps=['PRIME-TWO-ROOTS'],check='verify_split_torus_column.py',records=['split_torus_column_verification.json'],
     updates=[('PRIME-TWO-ROOTS','补齐剩余46组方向；取消其迹条件与Smith本原准备'),('PRIME-CERTIFICATE-ANATOMY','全部独立direction字段不再需要')],
     aliases=['分裂环面 split torus 方向 162 46'])
card('PRIME-CONSERVATION13','守恒交换替代(11,3)辅助13','prime','proved-local',
     '同来源输出守恒关系直接给U(−36)，接横向反射与终端，删除辅助13特殊群计算。',
     '局部修复不等于全部根表移除。',
     ['conservation_exchange_removes_auxiliary13'],deps=['PRIME-SPLIT-COLUMNS'],check='verify_equal_determinant_root_repair.py',records=['equal_determinant_root_repair_verification.json'],
     updates=[('PRIME-SPLIT-COLUMNS','补去仍保留的(11,3)辅助13')],aliases=['辅助13 11,3 守恒 n根'])
card('PRIME-FIVE-RETURNS','五返回公式替代48组根资源，保留114组','prime','proved-local',
     '一般容量公式与守恒n根供应两组横向系数；对原九偏移资源表替代48组，列出114组剩余。',
     '114是本独立改进对物理根资源的剩余，不是重写冻结主证明后的完整独立审计计数；s>p/2该模板有障碍。',
     ['conservation_capacity_and_five_return_supply'],deps=['PRIME-CONSERVATION13'],check='verify_conservation_capacity.py',
     records=['conservation_capacity_verification.json','conservation_remaining_root_cases.json'],
     updates=[('PRIME-CERTIFICATE-ANATOMY','以通式替代48组root资源；162→114仅就此资源清单')],aliases=['五返回 48 114 容量'])
card('PRIME-COMMON-SHAPE','临界带共同(p,p,r)形状与整数关系格','prime','proved-local',
     '整个2p<n<4p可进入共同形状；固定来源的迹零输出关系格及有效方向可显式算出。',
     '无界关系格的像不保证容量内可用移动；共同形状不等于全参数终止。',
     ['common_shape_integer_relations_and_mainstream_structure'],check='verify_common_shape_and_relation_lattice.py',records=['common_shape_relation_lattice_verification.json'],
     aliases=['共同形状 p,p,r 整数关系 格像'])
card('PRIME-CRITICAL-CONTROLLER','跨3p的共同控制器','prime','proved-local',
     'p≥83、新载体r≥r₀(p)的上下半带接同一根、单位及移动终端接口。',
     '本页r₀是新载体自身范围；小r已由旧载体桥接，不可再列整条立方根缺口。',
     ['critical_band_common_controller'],deps=['PRIME-COMMON-SHAPE','PRIME-SPLIT-COLUMNS'],check='verify_critical_band_common_controller.py',records=['critical_band_common_controller_verification.json'],aliases=['跨3p r0 立方根 条带'])
card('PRIME-RETAINED-BRIDGE','旧载体桥接补齐小余量','prime','proved-local',
     'p≥83、3≤r<2p、r≠p均可接同一收尾；r=1接旧端点，r=2保留CRT，r=p接等块。',
     '未消除小p全部物理供应；r=1的统一启动又有后续奇数铅笔。',
     ['retained_carrier_bridge_and_endpoint_lessons'],deps=['PRIME-CRITICAL-CONTROLLER'],check='verify_retained_carrier_bridge.py',records=['retained_carrier_bridge_verification.json'],
     updates=[('PRIME-CRITICAL-CONTROLLER','补齐其r<r₀条带，不再把立方根宽度看作当前缺口')],aliases=['保留旧载体 小余量 83'])
card('PRIME-ADELIC','本原直线的内容余循环与共同CRT','prime','proved-local',
     '把本原化的局部内容、均值标记及两端点CRT准备接到共同格描述。',
     '阿代尔语言不会供应尚缺的物理返回；旧r=1启动差异按奇数铅笔更新。',
     ['adelic_primitive_lines_and_common_endpoint_preparation'],check='verify_adelic_primitive_line_and_two_crt.py',records=['adelic_primitive_line_two_crt_verification.json'],aliases=['adelic 阿代尔 内容 CRT 格对应'])
card('PRIME-FIBER','同行列式纤维与有限精度对应','prime','proved-local',
     '有效作用格(n/g)Z；偶4≤r≤2p/5、奇5≤r≤p/5有直接根；Q|det A|精度记录本原输出。',
     '深核必须先真实实现；有限对应图存在不等于其终端全覆盖。',
     ['determinant_fibers_and_finite_lattice_correspondences'],deps=['PRIME-COMMON-SHAPE'],check='verify_equal_determinant_and_finite_correspondence.py',records=['equal_determinant_finite_correspondence_verification.json'],aliases=['同行列式 计数纤维 finite lattice Qdet 原位置库存'])
card('PRIME-GEOMETRY','有界纤维整数凸包、根本原性与内容对偶','prime','proved-local',
     '固定非零行列式纤维的整数凸包维数控制可生成根格；二维得到本原步长；内容与伴随对偶。',
     '实多边形大不等于任意小库存有资源；未完成全参数无证书存在性。',
     ['global_structure_and_bounded_fiber_geometry_20260916'],deps=['PRIME-FIBER'],
     check='global_structure_investigation_20260916/verify_geometry_and_content.py',records=['global_structure_investigation_20260916/verification.json'],
     sources=[RESEARCH+'global_structure_investigation_20260916/source_index.md'],aliases=['整数凸包 flatness 内容对偶 Graver Kneser'])
card('PRIME-FINITE-TERMINAL','深核只建一次：有限对应群化与共同终端','prime','proved-local',
     '已有真实深核，行列式与控制模数互素时，有限正向对应轨道等于明确有限群轨道；终端无需反复扩环。',
     '不供应初始根与深核；共享坏因子的行列式不自动覆盖。',
     ['finite_orbit_completion_without_ring_extension'],deps=['PRIME-GEOMETRY','PRIME-SPLIT-COLUMNS'],
     check='verify_finite_orbit_completion_without_ring_extension.py',records=['finite_orbit_completion_without_ring_extension_verification.json'],
     updates=[('PRIME-RETAINED-BRIDGE','统一已有深核后的终端接口，取消逐数字取逆／扩环要求')],aliases=['深核一次 不扩环 finite correspondence terminal'])
card('PRIME-ODD-PENCIL','奇数下半区共同边界反射铅笔','prime','proved-local',
     '所有奇素数p≥3、全部奇数1≤r<p，用同一两组三步反射及两步反射取得根、深核与终端。包含r=1，无83界。',
     '偶数余量、3p及上半带没有因此统一；Morris/Serre等原依赖仍保留。',
     ['odd_lower_band_boundary_reflection_pencil_20260916'],deps=['PRIME-FINITE-TERMINAL','EXTERNAL-ARITH'],
     check='verify_boundary_reflection_pencil.py',records=['boundary_reflection_pencil_verification.json'],
     updates=[('PRIME-RETAINED-BRIDGE','奇数下半带包括端点改为统一启动，不再依赖83'),('PRIME-ADELIC','端点与奇数内部的资源启动差异已由共同反射替代')],aliases=['奇数 r=1 下半带 反射铅笔 odd pencil'])
card('PRIME-TAIL-BACKUP','4p尾部整数化：备用改进及固定池障碍','prime','partial',
     '原n≥4p已全证；本稿分析见证预算、双重值恢复与固定双块池策略的不可能范围。',
     '不构成2p附近统一突破；没有发现必须重做原尾部正确性的理由。',
     ['four_p_tail_optimization'],related=['PRIME-NATURAL-UNIFICATION'],aliases=['4p 尾部 见证预算 双重值恢复'])
card('BURAU-REASSESS','Burau路线的现有资源与临界带容量边界','interfaces','synthesis',
     '正向中心、几何链及非零均值修正有效；三幂链最短容量与2p—4p临界带不匹配。',
     'Zariski稠密不等于算术指数／终端覆盖；不能因三平均就假设B₃。',
     ['burau_route_reassessment'],check='verify_burau_reassessment.py',records=['burau_reassessment_verification.json'],aliases=['Burau 辫子 braid 高秩'])

card('SUBCRITICAL-COMPLETE','p<n≤2p补集动力学；p+2完整判定与最短词','subcritical','proved-local',
     'p+2核心只有唯一可能成功的除p后继，位长多项式判定；枚举初选补集给精确最短词。一般p<n≤2p有整数能量完整搜索。',
     'p+3以后不能直接沿用二维唯一分支；一般伪多项式界不等于位长多项式。',
     ['subcritical_complement_dynamics_20260916'],check='verify_subcritical_complement_dynamics.py',records=['subcritical_complement_dynamics_verification.json'],aliases=['五元 5元 p+2 补集 最短 BFS forced'])
card('SUBCRITICAL-LIMITS','低维G加固定同余、实半代数判据的限制','subcritical','proved-local',
     '存在模任意固定M相同、G同合法而可解性相反的输入；五元方向不能用有限实半代数条件刻画。',
     '不排除输入相关gcd公式或其他算术编码；不能宣称不存在简单判据。',
     ['five_six_intuitive_criteria_and_modular_limits_20260916'],check='verify_five_six_modular_limits.py',records=['five_six_modular_limits_verification.json'],aliases=['固定同余 简单条件 不可能 半代数'])
card('SIX-EXPLICIT','六元三重核心G=3与唯一后继','subcritical','proved-local',
     '三重核心G=3且无四重值可解；四重值有模9条件；一般G=1失败出口后剩唯一后继。',
     '一般G=1尚未压成一次性公式；不是所有六元G合法都可解。',
     ['six_triple_block_explicit_G3_20260916'],check='verify_six_triple_block_explicit.py',records=['six_triple_block_explicit_verification.json'],aliases=['六元 6元 G3 四重 模9'])
card('FIVE-SUMMARY','五元：算法已解、静态分类仍未解','subcritical','synthesis',
     '维护完整五元层次状态：逐输入判定与最短路径完成；三进几何完整；D=1及固定D全词逃逸仍猜想。',
     '本总结不是所有新证明的独立审核。有限实验、零密度、分形维数和超越性均不能证明静态简单判据不可能。',
     ['five_averaging_progress_summary_20260917'],related=['SUBCRITICAL-COMPLETE','FIVE-ESCAPE-OPEN','FIVE-TEMPLATE-ESCAPE'],aliases=['五元 总结 三个缺口 静态判据'])
card('FIVE-NORM-SLICE','判别式−11范数子族的显式充要式','subcritical','proved-local',
     '若u²−uv+3v²=5·3^k，则可解恰为5|(u+v)且k=0或3|u；最短k+1步。',
     '只覆盖指定无限范数族，不是全部五元；勿与Q₅=u²+7uv+v²混用。',
     ['five_quadratic_norm_explicit_slice_20260916'],check='verify_five_norm_slice.py',records=['five_norm_slice_verification.json'],aliases=['-11 范数 5*3^k 静态子族'])
card('FIVE-NORMAL-FORM','五元完整受限连分数与level15矩阵序','subcritical','proved-local',
     '任意五元通过十对线性表达式进入唯一受限连分数；整数代数为level15序，生成模为u+v≡0 mod5。',
     '群轨道严格大于正词；不存在两分支共同乘法型齐次范数，不排除一般算术条件。',
     ['five_complete_arithmetic_normal_form_20260916'],deps=['SUBCRITICAL-COMPLETE'],check='verify_five_complete_arithmetic_normal_form.py',records=['five_complete_arithmetic_normal_form_verification.json'],aliases=['五元 continued fraction Eichler level15 群假阳性'])
card('FIVE-FRACTAL','三进紧集的全部有理点与密度','subcritical','proved-local',
     '有限标记=可解；无限边界有理点恰两轴有限轨道，被模5排除；维数log₂/log₃、每层2^(m+1)−1类。',
     '实稠密、三进零测不等于判定不可能；五元整数盒子密度零不等于固定D有限。',
     ['five_padic_fractal_rational_points_20260916'],deps=['FIVE-NORMAL-FORM'],check='verify_five_padic_fractal.py',records=['five_padic_fractal_verification.json'],aliases=['五元 p-adic fractal Cantor 有理点 rational boundary'])
card('FIVE-DIGITS','普通三进前缀非正则与有理代数对应','subcritical','proved-local',
     '普通斜率前缀无固定有限自动机；交换商w有二次对应，正规化P¹、节点分裂域Q(√5)。',
     '不是椭圆曲线；不排除同步整数编码；换支不是实际平均。',
     ['five_digit_obstruction_and_rational_correspondence_20260916'],deps=['FIVE-FRACTAL'],check='verify_five_digits_and_correspondence.py',records=['five_digits_and_correspondence_verification.json'],aliases=['finite automaton 非正则 对应 椭圆 曲线'])
card('FIVE-TORUS','统一Q(√5)范数一环面与扭曲平移','subcritical','proved-local',
     '两分支为J(ε^±1α)，3惰性、5分歧；四穿孔曲线及固定S内相邻单位边有限。',
     'J不是群同态；相邻边有限不能阻止离开后返回；辅助分母不是物理分母。',
     ['five_norm_one_torus_and_twisted_translation_20260917'],deps=['FIVE-DIGITS'],check='verify_five_torus_twist.py',records=['five_torus_twist_verification.json'],
     assumptions=['ESS定理1.1用于固定S单位方程'],sources=[RESEARCH+'five_torus_literature_20260917/README.md'],aliases=['Qsqrt5 torus J 扭曲 平移 S-unit'])
card('FIVE-DENOMINATORS','精确D、相邻互素、同理想任意近的失败点','subcritical','proved-local',
     'D=|u²+7uv+v²|/5是环面最小分母；相邻D互素，兄弟gcd只可能11；同理想固定局部精度不足。',
     'D不单调，不独立决定可解；辅助素数可变化。',
     ['five_torus_denominators_and_local_separation_20260917'],deps=['FIVE-TORUS'],check='verify_five_torus_denominators.py',records=['five_torus_denominators_verification.json'],aliases=['分母 D 相邻互素 11 Pell 同理想'])
card('FIVE-UNITS-GROUP','固定理想单位指数与三进大群闭包','subcritical','proved-local',
     '固定理想候选为α₀ε^(4k)，Z₃指数与h等距；群闭包含PSL₂(Q₃)，对数偏移D=1整数、D>1超越。',
     '大群不替代正半群；指数零密度不推出有限。',
     ['five_fixed_ideal_unit_exponents_and_padic_group_20260917'],deps=['FIVE-DENOMINATORS','FIVE-FRACTAL'],
     check='verify_five_unit_exponents_and_group.py',records=['five_unit_exponents_and_group_verification.json'],
     assumptions=['Baker–Brumer，已读正式转述，原1967证明未取得'],aliases=['单位指数 group closure Baker Brumer 超越'])
card('FIVE-SPARSITY','固定D有效稀疏与固定周期有限返回','subcritical','proved-local',
     '长度L指数区间成功数<4L^log₃2；固定D高度计数为对数高度分数幂；固定正词幂只有有限命中。',
     '不涵盖变词全树；有限返回不自动给有效最后命中界，后续Baker只补固定混合周期。',
     ['five_fixed_D_effective_sparsity_and_periodic_return_20260917'],deps=['FIVE-UNITS-GROUP'],check='verify_five_fixed_D_returns.py',records=['five_fixed_D_returns_verification.json'],assumptions=['ESS；SML为替代有限性论证'],aliases=['sparsity 周期 返回 Fibonacci Pell'])
card('FIVE-BOUNDED-RUNS','有界字母切换的有效有限性','subcritical','proved-local',
     '固定D且同方向段数有界时有限并有效；D=1至多两次切换的全长度分类只留三个方向。',
     '小段数应用有精确尾误差证书；任意切换仍未解决，后续有无网格界与模板推广。',
     ['five_bounded_switches_and_correspondence_degree_20260917'],deps=['FIVE-DENOMINATORS'],check='verify_five_bounded_runs.py',records=['five_bounded_runs_verification.json'],aliases=['切换 runs bounded 紧致化 CIP'])
card('FIVE-HECKE','显式间隙界与同层共同Hecke二次型','subcritical','proved-local',
     '有界段数给闭式字长界；所有同长度词拉回型整数等价；D=1第一段为v₃(2k+1)+v₃(2k−1)。',
     'Aka–Shapira只给整周期分布，不控制终端标记Ce；类信息统一不是全词逃逸。',
     ['five_explicit_gap_common_hecke_form_20260917'],deps=['FIVE-BOUNDED-RUNS','FIVE-UNITS-GROUP'],
     check='verify_five_explicit_gap_and_hecke.py',records=['five_explicit_gap_and_hecke_verification.json'],
     updates=[('FIVE-BOUNDED-RUNS','将一般有效界升级为无网格显式界')],assumptions=['Aka–Shapira用于共同周期；Lucas赋值亦有自足证明'],
     sources=[RESEARCH+'five_torus_literature_20260917/switch_hecke_review_20260917.md'],aliases=['Hecke Aka Shapira Ce 标记 Lucas 显式界'])
card('FIVE-TEMPLATE-ESCAPE','固定多块模板统一逃离小分母','subcritical','proved-local',
     '任意固定U₀V₁^a₁⋯V_r^a_rU_r内，指数独立变化仍统一逃离小D；允许混合块及无界切换。',
     '模板本身变化的全部词仍未覆盖；多模板有限性未给有效截止；固定混合周期另有Baker指数下界。',
     ['five_bounded_templates_uniform_escape_20260917'],deps=['FIVE-SPARSITY','FIVE-DENOMINATORS'],
     check='verify_five_bounded_templates_escape.py',records=['five_bounded_templates_escape_verification.json'],
     updates=[('FIVE-SPARSITY','由单周期扩为多参数固定模板，另补固定周期有效增长'),('FIVE-BOUNDED-RUNS','重复块可混合两字母，覆盖无界切换子族')],
     assumptions=['ESS经极小零子和化格陪集','Baker–Wüstholz正式转述只用于固定周期有效增长'],
     sources=[RESEARCH+'five_torus_literature_20260917/uniform_escape_review_20260917.md'],aliases=['全词 逃逸 模板 ESS bounded language 小分母'])
card('FIVE-ESCAPE-OPEN','固定D全词逃逸与D=1完整分类','subcritical','open',
     '猜想min_|W|=L D(We)→∞；更小猜想D=1只允许单位指数k=0,±1。',
     '模板定理、零密度、群闭包、有限指数范围实验都不能替代任意词证明。没有证明简单判据不可能。',
     ['five_averaging_progress_summary_20260917','five_bounded_templates_uniform_escape_20260917'],
     related=['FIVE-TEMPLATE-ESCAPE','FIVE-HECKE'],
     next_step='对不断变化的词模板给一致小范数控制，或构造无限反例族；不得把固定模板的无限并当有限覆盖。',
     aliases=['D=1 三个缺口 完整判定 全词逃离 统一逃逸'])

data={'schema_version':1,'updated':'2026-09-17','scope':'Curated navigation and state ledger, not a formal proof database or independent mathematical audit.',
      'legacy_manifest':'work/verification_manifest.json','source_policy':'Original proof sources retained; local research author proofs are not promoted to independently audited results.',
      'topic_notes':{
          'triple':'先读TRIPLE-ALL完整直接链，再读SEVEN-GEOMETRY与GEOMETRY-ALL-N。统一解释不是另一份已经完成的纯模曲线证明。',
          'prime':'PRIME-TOTAL是完整基线；PRIME-NATURAL-UNIFICATION是改进任务。最新实质接口优先看ODD-PENCIL、FINITE-TERMINAL和FIBER，早期资源卡用于追溯。',
          'subcritical':'先区分逐输入算法与静态算术分类。五元算法已全解；固定D全词逃逸仍开放。按依赖顺序阅读，避免重新证明已有递归。',
          'composite':'保留GRH条件，分清单个维数、首个非自动G点和最终阈值。此前会话的暂停安排不自动约束新用户任务。',
          'algorithms':'存在性、构造、最短性、计时和搜索失败必须分别报告；一条固定输入路径可以精确重放，但不承载无穷量词。',
          'interfaces':'跨主题先读这些共同工具和反例边界。历史文中方法的限制可以仍有效，原可达性目标却可能已经由其他路线完成。'},
      'overview':[
          {'area':'三平均 n≥7','state':'G为3幂充要，完整证明已存在。n≥11一份直接证明，7—10基例。','gap':'可变n统一多项式构造长度；更自然统一证明。'},
          {'area':'全部奇素数 p 平均','state':'N(p)=2p+1完整无条件；N(2)=4。','gap':'统一物理资源供应、替代剩余根记录；不是可达性仍未证。'},
          {'area':'素数证明独立简化','state':'方向／尺度终端已简化；有限对应；全部奇数下半带共同反射。','gap':'偶数／上半带及小p的一般资源存在性。'},
          {'area':'五元三平均','state':'完整判定与最短词已证；多种完整结构描述。','gap':'静态简洁算术式；D=1分类与固定D全词逃逸。'},
          {'area':'六元三平均','state':'G=3三重核心显式；一般核心有强制后继结构。','gap':'一般G=1一次性公式未得，不能只用G。'},
          {'area':'七元算术几何','state':'真实宏群、两个尖点、分歧范数与G已经严格对接。','gap':'不能免费嵌入任意n；不新增全维数纯群论证明。'},
          {'area':'合数元数','state':'全部2k+1端点无条件；平方族及部分临界族在GRH下完成。','gap':'一般最优临界与最终阈值、若干奇次幂与区间接续。'},
          {'area':'最短路径','state':'有明确困难性与独立精确重放工具；五元特例最短已解。','gap':'不能将预算IDA*说成通用高效最优求解器。'}],
      'claims':cards}

if __name__=='__main__':
    path=ROOT/'knowledge/catalog.json'
    if path.exists():raise SystemExit('Refusing to overwrite an existing catalog; edit that source directly.')
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Created',len(cards),'curated cards')
