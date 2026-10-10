# 端点精度路线的外部文献阅读记录

日期：2026-09-30。任务：查找能将真实p平均的精度控制推进成n=2p+1完整证明的既有方法。全文获取不等于通读；以下逐项列出实际读取范围。

## 搜索方式与边界

OpenAlex的六组初始查询涉及p进连分数、精度格、clique gossiping、低维矩阵半群和S整数除法链。部分返回429，部分长查询有明显无关结果；保存query_00—05.json，不将无关题录当作支持。Crossref四次查询超时，保存crossref_00—03.json。较短OpenAlex查询仍受限流，Semantic Scholar也返回429。

随后直接读取arXiv搜索结果及正式预印本页面，成功下载四份PDF，用PyMuPDF提取全文；文件名、URL和SHA256保存在各source.json。arXiv搜索页面共49条匹配，包含2026年周期性论文；周期性的新结果不被用作本题有限归零依据。

## 实际读取的来源

|来源|版本与实际读取范围|本项目能采用什么|不能推出什么|
|---|---|---|---|
|X. Caruso, D. Roe, T. Vaccon, *Tracking p-adic precision*|[arXiv:1402.7142v1](https://arxiv.org/abs/1402.7142)，2014-02-28；全文PDF24页。读引言、§2.2—2.3精度格、§3.1 Lemma3.4及证明和非满射讨论。正式DOI [10.1112/S1461157014000357](https://doi.org/10.1112/S1461157014000357)。|用格保留相关精度；线性映射上精度传播可精确计算。我们的历史格是前缀整性逆像，正文独立证明。|其非线性精度引理要求满射微分；不是原位置选词、有限可达或归零算法。|
|L. Capuano, N. Murru, L. Terracini, *On the finiteness of P-adic continued fractions for number fields*|[arXiv:2105.12570v2](https://arxiv.org/abs/2105.12570)，2025-11-28修订；期刊版Bull. Soc. Math. France150(2022),743—772。读引言、§3.1 floor函数定义、§4.1 Lemma4.2/Proposition4.3及证明、§4.3 Theorem4.5及证明；未通读后面的数域分类证明。|Browkin对有理数的有限终止；p进整除深度与实收缩递推的配合；nu<1的有限性判据。|不能自由挑选不在真实平均菜单中的数字/反演；不保证模n合法性，也不保证固定物理分母。|
|L. Capuano, S. Checcoli, M. Mula, L. Terracini, *On P-adic continued fractions with extraneous denominators: some explicit finiteness results*|[arXiv:2311.14034](https://arxiv.org/abs/2311.14034)，搜索页标示2026-03-12修订；PDF23页。读引言及Theorem1.1、§7.1—7.3除法链和初等矩阵关系，包括Theorem7.5的陈述及算法说明；未逐项审核§5.8数域常数证明。|明确区分floor有限性算法与短除法链；额外分母如何拓宽有限性结论。|额外形式分母不等于实际允许除数；若依赖SL2生成，仍须说明与原同余群路线的关系。|
|R. Belhadef, H.-A. Esbelin, *On the complexity of p-adic continued fractions of rational number*|[arXiv:2405.14500v2](https://arxiv.org/abs/2405.14500)，2024-05-31；PDF17页。读摘要、引言和§2 Algorithm2.3；未审核全文复杂度证明。|确认Browkin算法及长度问题已有专门文献。|不调用未审核的复杂度界；数学代入采用上列CMT的完整命题。|

另读已缓存Liu–Li–Anderson–Shi《Clique Gossiping》2017 arXiv v1的摘要与引言，用于复核固定词/全初值量词；本轮没有重审其证明或采用其整除判据。

## 直接结论

最接近独立端点证明的是CMT的“整除增长抵消实增长”机制；它不是“p进收敛就有限终止”。本轮实际端点返回有实二阶收缩公式，但没有取得与之相容的合法数字选择。

因此没有发现能直接引用来完成本题的新定理。该判断只针对本次搜索及已读来源，不是文献不存在的断言。本文献调查没有改变原素数定理的外部依赖。
