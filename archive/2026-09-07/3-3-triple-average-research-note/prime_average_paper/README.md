# 素数平均的详细证明稿

阅读 [论文 PDF](prime_average.pdf)；独立 LaTeX 源文件为 [prime_average.tex](prime_average.tex)。源文件已展开全部组成部分，不需要旧项目文稿参与编译。

范围：奇素数 p、n>=2p+1 的 G 判据及锐下界，另明确引用二平均判据得到 N(2)=4。未收入五元静态分类、算术几何解释、合数或 GRH 探索。

主文重新陈述基本引理、真实返回、深同余、内容分支和有限终端。构造部分展开各区间的计数与证明，使用奇数反射铅笔、共同终端、五返回与二进列提升等简化；仍必需的有限资源没有删除。当前仍是详细证明稿，不代表已经完成一轮独立同行审稿或得到全参数无计算证明。

## 证据

- [来源与选用章节](source_map.json)：35份构造来源的原路径、选用章节和 SHA256；不是独立审稿记录。
- [剩余根资源核对](certificate_check.json)：114组参数、233对反射；检查容量、迹零、标量、根系数及约分倍率的局部化。完整计数表印在论文中。
- [独立有限核验程序](finite_checks.py)：只使用 Python 标准库，正文末尾亦完整收录；不导入原项目模块、不搜索平均词。
- [有限核验结果](finite_checks_result.json)：903个五平均线性系统、57026个七平均系统、二十二元648个辅助群元素及3872个带尺度状态。
- [十元二次覆盖数据](ten_cover_result.json)：5120个局部类、12个签名的完整二次系数与未覆盖实点；论文中亦列出。

外部引用保留 Morris 2007 Theorem 6.1(2)、Serre 的有理 S 整数强同余子群性质及其正式综述依据；没有把“有限同余核”当作“平凡同余核”。二平均引言的条件 MC 已在主文准确代入 G 判据。正文直接给有限域计数证明，因而素数 EGZ 部分不再隐藏 Chevalley--Warning 的使用。

## 编译与维护

在本目录连续运行两次 `xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape prime_average.tex`。字体使用 Windows 的 Times New Roman、SimSun 和 Microsoft YaHei；其他系统应替换为已安装的等价字体。

`front.tex`、`ending.tex` 是主文编辑源；`sections.json` 与 `build_paper.py` 管理构造选取和文内引用。重建需要 `pypandoc_binary`；仅编译现成 `prime_average.tex` 不需要 Python 或 Pandoc。`prepare_finite_checks.py` 提取纯有限证明核验，`prepare_ten_cover.py` 从既有精确验证器导出完整符号数据。

本目录放在项目根下，是论文编辑交付物，不是新的研究状态源。原2440个文件逐字节核对未变，原知识登记与冻结材料均未改写。新展开的八元安全入口及两剩余位置的平移分组写在主文中；它们补足论文阅读依赖，不扩大已有可达性范围。
