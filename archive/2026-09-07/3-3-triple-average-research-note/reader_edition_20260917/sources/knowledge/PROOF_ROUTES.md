# 证明链与真正开放的接口

本页给阅读骨架，精确范围和证据查 [STATUS.md](STATUS.md) 及对应结论卡。这里不是所有正文的自包含替代，也不是自动生成的形式化依赖证明。

## 三平均

已经证明所有 n≥7：G为3幂当且仅当有限三平均可达。最短的主阅读链是：

1. **必要性与公共算术对象：** `G-OBSTRUCTION`。根格配对／仿射R格的障碍模；G非3部分不能沿操作消掉。
2. **全部 n≥11 的充分性：** `TRIPLE-ALL`。研究3X，至多两步建立两个不同三重值；同时保护危险素数见证；选取真实整数平均；离散能量严格下降；进入显式终端。
3. **有限边界：** `TRIPLE-BASES`、`SEVEN-STRUCTURE`。七元正向逆与尖点控制，八元Euclid，九元固定三幂网络，十元精确宏覆盖。
4. **几何理解：** `GEOMETRY-ALL-N`、`SEVEN-GEOMETRY`。前者统一根格和局部退化，后者给真实可执行的模曲线例子；两者均不能替代第2、3步的操作存在性。

已绕开的旧必经关卡：逐个素数位置数搜种子、一般合数归约、所有输入压到同一个二维核、指定迹零矩阵的原位置分解。它们的独立工具仍可用，不能再说三平均全维数证明尚依赖这些未完成目标。

真正开放：可变n的统一多项式构造长度；更简洁的统一原位置资源定理；阈值以下的静态分类。一般最短问题与此分开。

## 素数平均

完整基线由 [原总证明](../outputs/prime_arity/proof.md) 及 [原依赖图](../outputs/prime_arity/proof_map.json) 给出。原注册中的 162 组是该版本的证书。

```mermaid
flowchart LR
  A[合法输入与安全入口] --> B[带重数账本的核心]
  B --> C[实际标量周期与根资源]
  C --> D[深同余工具]
  D --> E[有限列与尺度输送]
  E --> F[零和终端及收尾]
```

独立改进不是再证明各处可达，而是替换这条链的部分环节。按接口读，避免把旧计数当最新状态：

| 接口 | 先读 | 已替代什么 | 仍需要什么 |
|---|---|---|---|
| 全输入入口／共同形状 | PRIME-MOVE-MERGE、PRIME-COMMON-SHAPE | 统一双块入口和跨3p形状 | 核内资源供应 |
| 初始正向逆 | PRIME-EVEN-INVERSE、PRIME-ODD-PENCIL | 全偶载体周期；全部奇数下半带含端点的共同反射 | 一般偶数／上半带完整资源 |
| 容量内的根 | PRIME-FIBER、PRIME-GEOMETRY | 同行列式作用格、二维整数凸包的本原根 | 退化／小库存的一般存在性 |
| 九偏移资源记录 | PRIME-CONSERVATION13、PRIME-FIVE-RETURNS | 辅助13；48组根记录由通式替代 | 此路线保留114组根资源，不能自动改写基线审计 |
| 已有资源后的终端 | PRIME-SPLIT-COLUMNS、PRIME-FINITE-TERMINAL | direction、binary_unit、反复扩环等更强要求 | 初始根与深核必须先成立 |

推进自然统一之前必读 `PRIME-NATURAL-UNIFICATION`。**“已有深核后可做”不能倒过来成为深核启动的证明。** 只需存在成功选择；不要求任意合法选择都终止。

## 五元

完整逐输入问题与算术研究要分别追踪。

```mermaid
flowchart LR
  A[SUBCRITICAL-COMPLETE: 强制递归与最短词] --> B[FIVE-NORMAL-FORM: 完整正词描述]
  B --> C[FIVE-FRACTAL: 三进紧集有理点]
  C --> D[FIVE-TORUS: 扭曲环面]
  D --> E[FIVE-UNITS-GROUP: 固定理想单位指数]
  E --> F[FIVE-ESCAPE-OPEN: 固定D全词逃逸]
  E --> G[FIVE-SPARSITY: 稀疏与周期]
  G --> H[FIVE-TEMPLATE-ESCAPE: 固定模板逃逸]
  H -. 任意变模板仍缺 .-> F
```

这个图是研究关联，不声称每一条边都是不可替换的证明前提。更细的脚本与原文从结论卡定位。

- 已解决：任意有理五元能否可达、失败能否判停、最少步数。
- 已证明的结构：部分静态范数族、完整正词／连分数／三进描述、环面及理想坐标、多块固定模板逃逸。
- 尚未解决：D=1只三个单位指数；固定D任意词只有有限成功点；像G一样的一次性完整算术判据。

固定模板可以有无界切换，但“模板固定”的量词不能删。零密度、Baker–Brumer超越性、Aka–Shapira整周期等分布都不自动填这个缺口。

## 合数与算法

合数先读 `COMPOSITE-FRONTIER`，再读 `COMPOSITE-DEFINITIONS`。GRH、单个临界维数、自动G、首个非自动G维数及最终阈值必须逐项保留。不要从全部2k+1端点已解推断全部n≥2k+1已解。

算法先读 `ALG-LENGTH`。存在性、路径长度上界、生成一条路径、该路径最短、有限计时比较，是五种不同结论。五元的专门最短算法不与一般最短路径困难性冲突。

## 快速获得阅读包

```text
python knowledge/project_knowledge.py context "固定模板 小分母"
python knowledge/project_knowledge.py context "容量 深核 退化"
python knowledge/project_knowledge.py context "七元 尖点"
python knowledge/project_knowledge.py verify PRIME-ODD-PENCIL
```

开始研究时在记录中注明选中哪条链、哪个接口、要增加哪一个量词。单纯新增矩阵记号、提高有限搜索范围、重写为几何术语，不自动构成该接口的新结果。
