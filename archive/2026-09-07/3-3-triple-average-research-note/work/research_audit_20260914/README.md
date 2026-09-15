# 2026-09-14研究审查材料

## 2026-09-15 强CSP专项补核

新增取得Prasad--Rapinchuk正式出版综述 *Developments on the congruence subgroup problem after the work of Bass, Milnor and Serre*, Collected Papers of John Milnor, Vol.V, AMS,2010,307-325。

- [19页重印PDF](prasad_rapinchuk_milnor_survey_2010.pdf)、[提取文本](prasad_rapinchuk_milnor_survey_2010.txt)、[第309页图像](prasad_rapinchuk_survey_page309.png)。已读取第2.1至2.3节、命题1、第4节定理3的相关陈述及参考文献[49]，并查看第309页原图。
- [作者题录](https://uva.theopenscholar.com/andrei-rapinchuk/publications/developments-congruence-subgroup-problem-after-work-bass-milnor-and)直接链接[重印文件](https://uva.theopenscholar.com/files/ixqrlw/files/milnor_survey_8.pdf)。实际下载为application/pdf，571108字节；SHA256：`CA19042C85BDF4E7E3E62F7ED66BD81E6CEC33456F65902715E472E7C9B140A1`。
- 第309页第2.3节明确给出SL2在|S|>1且S含非复数处时同余核平凡；同页命题1和第308页经典CSP定义给出每个有限指数子群包含主同余子群。第324页[49]对应Serre 1970。
- 对R=Z[1/q]、q>1，S包括实无穷处与至少一个有限素数处，因而适用。此来源同时支持奇素数局部化环，不局限于Z[1/2]。
- Serre 1970原文仍未全文取得：Annals官方题录页仅提供DOI，JSTOR请求返回HTML；arXiv访问连接重置。未将这些失败请求计作论文全文。成功取得的是上述作者提供的正式综述。

适用性与区间证明的完整审核见[专项报告](../../outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md)。下面保留9月14日原始访问范围，勿将旧的“仅二进交叉支持”当作补核后的全部证据。

本次先复查双锚点碰撞、不同值归约、单位补回、精度反例、端点主元与CRT证书。实质推进发生在端点受限群生成：找到Morris 2007的有限指数子群内部生成定理，与Serre同余子群性质及显式有限环消元接通。证明见[合数端点核心闭合](../../outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md)。

## 实际使用的来源

| 材料 | 核对内容 | 证据边界 |
|---|---|---|
| [Morris 2007 PDF](morris_muni.pdf)、[提取文本](morris_2007.txt) | 定义、定理6.1(2)、5.13、引理6.9及推论6.10；秩二及无限单位条件 | 已读相关原文；没有重新证明Carter-Keller-Paige的深结果 |
| Serre 1970，DOI 10.2307/1970630 | 所用标准特例：SL2(Z[1/2])有限指数子群包含主同余子群 | 原文全文下载未成功；[专家答复原始记录](serre_special_case_crosscheck.json)交叉确认特例；正式证明明确以Serre定理为外部依赖 |
| [Mennicke 2000 PDF](mennicke_2000.pdf)、[文本](mennicke_2000.txt) | 区分直接初等生成与正规闭包，及定理中的阶数>=3前提 | 未把该高阶结果套用于SL2 |
| 原有Morgan-Rapinchuk-Sury 2018缓存 | 整个SL2的9因子定理及参考文献 | 该定理本身不解决本题受限根群；它的参考文献帮助定位Morris原文 |

Morris来源：https://emis.muni.cz/journals/NYJM/j/2007/13-17.pdf 。作者出版列表确认刊名、年份、页码。Morris PDF SHA256：F690AD629791A30284E3E7FF7EDE152B874314D218138CB2A41CEFB24FAB902E。

Mennicke来源：https://journals.msp.org/mscand/article/download/916/915 。PDF SHA256：E2DD023379F87B82DA56BE88F74042FCB1C16EEB5D538CD60B14AF4A7003AC57。

## 检索与未使用材料

通过OpenAlex题录、作者出版页、期刊/EMIS镜像定向查询relative elementary groups、congruence subgroup generators、Mennicke symbols、Farey symbols、Carter-Keller-Paige及相关零和结构。题录命中只作线索，不作为定理证明。

Morris《Introduction to Arithmetic Groups》下载后仅检索了同余与S算术相关部分，未用于新增证明。Milne的AG.pdf实际为《Algebraic Geometry》，已按实际标题更名且未使用。若干所谓PDF地址返回的是HTML跳转页，已改名为redirect.html，不能当作已下载论文。首页、错误跳转和目录页保留为访问记录。

## 核验范围

[核验程序](../verify_endpoint_congruence_completion.py)及[结果](../endpoint_congruence_completion_records.json)只核查任意商分解公式、平衡单位、陪集归约与既有正向编译接口。完整一般量词由专题证明及其明确外部定理承担。没有平均词发现搜索，没有新增高效任意核心分解算法。
