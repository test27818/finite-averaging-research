# 三元平均论文与补充材料

版本日期：2026-09-11。

## 阅读

- `triple_average_paper.pdf`：论文正文与附录。
- `triple_average_paper.tex`：可独立编译的 UTF-8 LaTeX 源文件。
- `supplement/`：精确有限证书、构造核验和源码数据核对程序。

正文直接证明全部 n>=11，不依赖素数、合数归约，也不调用其他维数。七、八、十元单独处理，九元使用固定网络。七元和十元的精确有限代数验证是证明的一部分；全维数的数值重放只是实现审计。

## 编译

需要包含 ctex、Fandol 字体和 TeX Gyre 字体的 TeX Live，以及 XeLaTeX。已在 TeX Live 2024 上编译。

在本目录运行两遍；若提示目录或引用变动，再运行一遍：

```text
xelatex -interaction=nonstopmode -halt-on-error triple_average_paper.tex
xelatex -interaction=nonstopmode -halt-on-error triple_average_paper.tex
```

参考文献已直接包含在源码中，无需 BibTeX、外部图片或联网下载数据。

## 核验

需要 Python 3.10 或更新版本，仅使用标准库。在本目录运行：

```text
python supplement/run_checks.py
```

不得使用 `-O` 或设置 `PYTHONOPTIMIZE`。预期结束标记为 `ALL PAPER CHECKS PASS: 7`。完整输出写入 `supplement/verification_results.txt`。

`verify_paper_data.py` 会直接读取本目录 LaTeX 源文件，比较七元矩阵、十八个词、五种赋值签名、十元七个矩阵、实际尺度和十二种局部签名，检查是否存在重复或未定义的交叉引用。

`explore_ten_descent.py` 与 `symbolic_two_parameter_macros.py` 保留来源文件名；验证过程只使用它们的精确算术和形式值辅助函数，不执行发现搜索。无需缓存文件、旧项目目录、第三方 Python 库或在线服务。

## 结论边界

对非恒定有理输入，n>=7 的判据为：本原中心化差分 gcd 是三幂。全等输入直接可达。

n>=11 的一位额外精度结论针对整数零和输入；一般有理输入先统一中心化、清分母。七、八、十元的一位额外精度界没有在本文中证明。判定具有位长多项式复杂度；构造长度只给出数值高度界，没有宣称位长多项式长度。
