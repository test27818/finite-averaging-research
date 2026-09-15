# 文献与检索注意事项

## 核心文献

1. **Miguel Coviello Gonzalez, Marek Chrobak.**
   *Towards a theory of mixing graphs: A characterization of perfect mixability.*
   - arXiv: **1806.08875**（v4, 2019-05-18）
   - 期刊版：**Theoretical Computer Science** 845 (2020) 98–121，doi:10.1016/j.tcs.2020.09.007
   - 模型：微流控 lab-on-chip 的"混合图"，每个微混合器双入双出，输出 $\frac{a+b}{2}$。
   - 内容：PerfectMixability（= 本问题）的完整刻画（Condition (MC)）、多项式判定与构造、
     多项式大小的混合图、常数深度 MixReachability 的 NP-hard、Dinh 算法反例。
   - 术语：$b$-congruent（多重集所有元素模 $b$ 同余）、near-final（可划分为均值相同、
     大小为 $2$ 的幂的分块）、precision（精度 = 分母 $2^d$ 的位数，与 depth 深度不同）。

2. **MathOverflow 421671** "Make $n$ numbers equal using pairwise averages"（2022）。
   - 独立提出同一问题；当时仅有部分结果（$n=3$ 等差、$n=4$ 恒可、$n\ge5$ 开放），
     未给出完整判据（判据在文献 1 中）。

## 相关文献（不是同一问题）

- **Chatterjee, Diaconis, Sly, Zhang.** *A phase transition for repeated averages.*
  Ann. Probab. 50(1), 2022, arXiv:2101.xxxx。研究**随机**选对平均的**收敛速率**（Bourgain 问题），
  不是"有限步精确相等"的判定。
- **Couëtoux, Gastaldi, Naves.** *The steady-states of splitter networks.* arXiv:2404.05472 (2024)。
  研究 Factorio 分流网络的稳态/负载均衡（流量版"完美混合"），引用文献 1。
- 微流控工程的稀释/混合启发式算法（Thies 的 Min-Mix、Roy 的 DMRW、Huang、Chiang、
  Dinh 的 ILP 等）——目标是最小浪费/最小试剂，不是判定理论。

## 检索注意事项（重要）

本问题在**纯数学/组合数学文献里没有独立名字**。用 `average`, `equalize`, `averaging game`
等数学关键词基本搜不到；正确入口是微流控理论术语：

- `perfect mixability`
- `mixing graphs` / `mix-reachability`
- `droplet microfluidics` + `dilution`
- 作者线索：Marek Chrobak（UC Riverside）、Coviello Gonzalez

因此，评测 AI 时**不应**把它当作"有现成答案的竞赛题"——文献答案存在但极难被普通检索命中，
这正好可以测 AI 是"独立推出判据"还是"检索到判据"（以及是否诚实说明来源）。
