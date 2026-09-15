# Arena三平均网页审阅

来源与完整结论见 ../../outputs/arena_triple_solver_review.md。这里只保存外部网页快照、未改动的计算函数和独立审阅工具，不替换项目正式求解器。

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
