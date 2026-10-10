# H_t文献来源与访问等级

检索日期：2026-09-15。研究结论见[报告](../../outputs/general_arity/ht_literature_and_eventual_square_completion_20260915.md)。*_source.json记录原URL、最终URL、时间、状态、文件长度和SHA256；失败也保留。

## 取得全文并实际阅读相关段落

1. Paul Pollack, *Bounds for the first several prime character nonresidues*, Proc. Amer. Math. Soc.145(2017),2815–2826，DOI [10.1090/proc/13432](https://doi.org/10.1090/proc/13432)。
   [作者PDF](https://www.pollack-math.net/hudson.pdf)；本地pollack_hudson.pdf／.txt。直接读第1–4页、第8页和参考文献；定理2.7页图像pollack_theorem27.png已查看。最重要来源：定理1.1覆盖所有非主字符，定理2.7覆盖所有真子群。
2. Greg Martin、Paul Pollack, *The average least character non-residue and further variations on a theme of Erdős*, J. London Math. Soc.87(2013),22–42，DOI [10.1112/jlms/jds036](https://doi.org/10.1112/jlms/jds036)。
   [作者保存的出版PDF](https://personal.math.ubc.ca/~gerg/papers/downloads/ALCNFVTE.pdf)；本地martin_pollack2013_author.pdf／.txt。直接读印刷第22–25页，特别是Bach3log²n引用、Norton界和特征群引理；没有把平均值定理用作最坏情形界。
3. Elchin Hasanalizade、Hua Lin、Greg Martin、Andradis Luna Martínez、Enrique Treviño, *Explicit Burgess inequalities for cubefree moduli*, [arXiv:2511.17778](https://arxiv.org/abs/2511.17778)，作者当前预印本。
   [作者PDF](https://personal.math.ubc.ca/~gerg/papers/downloads/EBICM.pdf)；本地cubefree2025_author.pdf／.txt。直接读第1–3页及相关证明条件、参考文献；第2页图像cubefree_page2.png已查看，确认10^1145门槛。

## 题录、摘要或经已读文献间接核对

4. Karl K. Norton, *A character-sum estimate and applications*, Acta Arith.85(1998),51–78，[DOI](https://doi.org/10.4064/aa-85-1-51-78)。期刊页norton1998_journal.html确认题录；PDF下载403。定理1.20／1.30由Pollack正文明确引用，未声称读过Norton原证明。
5. Glyn Harman, *Integers without large prime factors in short intervals and arithmetic progressions*, Acta Arith.91(1999),279–289，[DOI](https://doi.org/10.4064/aa-91-3-279-289)。Crossref题录harman_metadata.json。MathOverflow答复指向定理3；原PDF403。一次猜测式期刊URL返回期刊首页，不作为论文正文。
6. Eric Bach、Lorenz Huelsbergen, *Statistical evidence for small generating sets*, Math.Comp.61(1993),69–82，[DOI](https://doi.org/10.1090/S0025-5718-1993-1195432-5)。OpenAlex摘要oa_bach1993.json、Crossref元数据。读到的是题录和摘要，PDF403。其对数级最坏界是启发性猜想。
7. Eric Bach, *Explicit bounds for primality testing and related problems*, Math.Comp.55(1990),355–380，[DOI](https://doi.org/10.1090/S0025-5718-1990-1023756-8)。PDF403；准确GRH条件性3log²n版本在上面的Martin–Pollack出版论文第22页读到。
8. Niraek Jain-Sharma、Tanmay Khale、Mengzhen Liu, *Explicit Burgess bound for composite moduli*, IJNT17(2021),2207–2219，[DOI](https://doi.org/10.1142/S1793042121500834)。出版元数据、arXiv:2010.09530题录；原文访问失败。其精确r=2定理在2025预印本第1页Theorem A直接读到。
9. Forrest J. Francis, *An investigation into explicit versions of Burgess' bound*, JNT228(2021),87–107，[DOI](https://doi.org/10.1016/j.jnt.2021.03.018)。题录及2025论文对其素数模数范围的介绍；未读全文，不用于独立推论。

## 论坛检索线索

- [2014年小生成元问题](https://mathoverflow.net/questions/165809/)，及[Lucia答复](https://mathoverflow.net/a/165816)：完整读取，明确联系Harman定理3、光滑数和短特征和。正式证明引用Pollack全文。
- [2023年小比值表示](https://mathoverflow.net/questions/451422/)及两条回答：完整读取，抽屉原理适用于素数模数，论文报告已给自足证明；没有把论坛的素数结论扩为所有合数。

## 检索与计算边界

- research_ht_literature.py保存12个通用网页查询和20个主题题录查询；另外的oa_*、cross_*、mo_*、mse_*文件记录适应性追查。通用网页有明显不相关结果，未将这些条目当文献证据。
- 三份PDF通过文件头确认，使用pdftotext读取；关键公式另核对页面图像。
- 题录去重数是检索覆盖指标，不是阅读全文数。数学结论仅依据报告明确列出的原文段落。
- ht_through999_certificate.json是全部2<=t<1000的有限群生成证书。它不提供无条件大参数界，也不证明外部定理。
- 本次没有联系作者或发表帖子，没有以GRH为无条件前提。
