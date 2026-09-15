# 素数平均的独立 p 进改进研究

2026-09-16更新。今后的改进、算法和验证只在本目录记录。原完成证明、主索引和全项目核验注册保持冻结；本目录的阶段结果不能直接覆盖原证明。

## 当前实际进展

| 层次 | 已证明内容 | 尚未完成 |
|---|---|---|
| 二进表的统一替代 | 三个旧返回的平方、交换子和列提升，统一替代内部偶余量64／256类轨道表 | 九偏移物理计数与根理想证书仍保留 |
| 全参数入口 | 任意k≥2、n≥2k+1安全进入两个k块加剩余单点 | 入口后的统一终止 |
| 偶数载体取逆 | 所有奇素数p、1≤t<p的(p,p,2t)核心具有同一规则的十二步标量闭路 | 根族、共同理想和终端 |
| 最新根构造 | t≡2 mod4时，保持来源、交换一份输出，正向实现L(qR)及两种符号 | 其它t、横向根、整体覆盖 |
| 算术编译 | 已有完整根族和深核后，一次有限环标量同余修正 | 从新宏生成这些前提及高效深核词展开 |

**尚未彻底统一。** 新的二进列提升证明已能替代内部偶余量的64／256类表，但原文件保持冻结，未物理删除。九偏移162组及其两个补充、其它小基例仍未被替代。“第二个矩阵不交换”不等于已有根；“切向量独立”也不自动制造可执行根族。

## 阅读顺序

优先读[整体结构复盘与统一二进列提升](structural_reassessment_and_uniform_dyadic_orbits.md)：区别物理资源证书与有限列覆盖；第4—5节是替代两张二进表的一般证明及其与旧证明的衔接，第7节记录核验。

1. [保持来源、交换输出](output_exchange_produces_roots.md)：最新实质结果；输出差分直接产生真实剪切。含固定模板为何不能自动覆盖其它t的证明。
2. [全部偶数载体一致取逆](uniform_even_carrier_inverse.md)：根构造依赖的统一真实逆。
3. [载体更新正常形](carrier_refresh_normal_form.md)：同一来源与输出计数的完整矩阵。
4. [从局部证明提取整体主线](local_proofs_to_global_balance.md)：哪些成功构造可以复用。
5. [通用移动—合并入口](move_witnesses_then_merge.md)与[单载体格位移](carrier_balance_and_uniform_mechanism.md)：入口规则及不能只靠单载体取逆的全称障碍。
6. [平方零编译](square_zero_hensel_compiler.md)与[实现](square_zero_compiler.py)：以已有真实根和深核为前提的算术算法。
7. [统一计数公式](uniform_reflection_formula.md)与[证书解剖](certificate_anatomy_and_odd_offsets.md)：现有p≥83公式及仍未被替代的物理、理想和尺度条件。

## 本轮证据

[二进列提升核验](uniform_dyadic_column_lifting_verification.json)通过4096类模8公式、原64／256类上的3840次确定性输送，以及384次保留奇数部分尺度的混合模数输送。一般结论由恒等式和逐层归纳证明；没有搜索平均词或枚举群轨道。原256份冻结文件未改动。

[输出交换核验](output_exchange_roots_verification.json)记录66项一般根／仿射恒等式、110对参数上660条正负根的十二步原位置重放，共7920步。全参数结论由正文公式证明，有限检查不替代量词。

[全偶载体核验](uniform_even_carrier_inverse_verification.json)、[对称重建核验](symmetric_rebuild_verification.json)、[通用入口核验](carrier_balance_verification.json)和[平方零核验](verification_results.json)保留各阶段的准确范围。已冻结的256份文件按existing_documents_snapshot.json核对，未修改原证明或注册。

本轮未运行平均词或有限轨道搜索。回读了载体更新、全偶闭路、旧两类对合与相邻倍率根公式。此前把证书称为“运输半群的整数空洞／正规性”没有证明依据，已明确撤回；只使用有原位置计数的具体整数移动。

原项目入口仅作只读来源：[完成证明](../../outputs/prime_arity/README.md)。
