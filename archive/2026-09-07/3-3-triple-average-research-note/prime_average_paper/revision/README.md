# 素数平均论文：原生 LaTeX 修订版

阅读 `prime_average_revised.pdf`，单文件源为 `prime_average_revised.tex`。上一版128页稿及原研究材料不变。

本版九节主文依次为：主定理、障碍与下界、返回与同余输送、安全整数下降、等块及含零收尾、安全压缩、临界带控制器、宽维数、完整覆盖。四个附录分别展开偶数下半带、上半带计数、小元数基例、有限证书。Python程序独立作为补充材料。

各命题使用统一 theorem/lemma/proposition/corollary 编号；方程自动编号；引用通过 ref/eqref。没有 Pandoc、ensuremath、texorpdfstring、addcontentsline、手写公式tag或C编号。`build.py`仅拼接手写LaTeX并写入有限整数表，不解释或猜测数学表达式。

## 数学与编写边界

这是按现有证明重写的论文版本。外部群论依赖和有限证书仍保留，没有得到整个临界带无分情形、无计算的统一证明。参考文献仅列实际引用的四项；有限域计数与零和逆边界在文中给出证明，没有为了增加文献数而列未使用的来源。

本轮明确整理了两项较短衔接：偶数内部取得2n根后直接接共同有限终端；共同上半带计数在s>=10时的实际容量覆盖全部p>=11。这两项一般不等式与坐标计算在正文和附录写出，另有精确检查；它们属于本次编辑者复核，尚未经过独立审稿。

`structure_check.json`只检查源文件结构、标签与引用存在性，不认证数学正确性。`DEPENDENCIES.md`记录被引用结果如何提供前提，以便逐条审核。`revision_checks.json`是计数和坐标恒等式核对；`finite_checks_result.json`是完整有限分类结果。

## 复核

运行 `python build.py` 重建单文件。连续运行 XeLaTeX 至交叉引用稳定。字体依赖 Windows 的 Times New Roman 和 SimSun。

`python -B verify_revision.py` 核对114组根表、共同上半带计数与标准偶反射；`python -B finite_checks.py`独立复核有限碰撞系统及二十二元轨道。两程序均不搜索平均词。
