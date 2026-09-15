# Perfect Mixability and Finite Averaging

**[中文首页](README.md) · English · [Proof guide](docs/PROOF_GUIDE.md) · [Verification guide](docs/VERIFICATION.md) · [Terminology](docs/TERMINOLOGY.md)**

When can a finite collection of rational numbers be made **exactly equal in finitely many averaging operations**? An operation chooses exactly $k$ distinct positions and replaces all their values by their arithmetic mean. The positions and their number remain fixed; no extra copies or discarded outputs are allowed.

This repository studies **perfect mixability**, **mixing graphs**, **finite-step averaging**, **binary/pairwise averaging**, **ternary/triple averaging**, **prime-arity averaging**, and **general k-ary averaging**. It contains mathematical proofs, exact rational verifiers, finite certificates, constructive algorithms, benchmarks, literature reviews, and unsuccessful research routes with corrections.

**Chinese search terms:** 完美可混合性、完全可混合性、可混合性、混合图、有限步平均、有限次平均、二平均、两数平均、三平均、三数平均、p平均、k平均、素数平均、合数平均、有限步精确共识。

## Mathematical problem

**Research provenance and ongoing direction.** The project's new research results were developed primarily through sustained collaboration between the user and **GPT-6 Astra (gpt6-astra)**. The completed proofs have undergone multiple rounds of internal review, cross-checking and targeted exact verification, with audit records, corrections and known issues retained. Work continues toward **more natural, readable and structurally unified proofs**, reducing isolated constructions and reliance on computational certificates. Internal review is not external peer review or formal certification; cited prior results remain attributed to their original authors. See [research provenance and review scope](PROVENANCE.md).

For $x\in\mathbb Q^n$, choose $S\subseteq\{1,\dots,n\}$ with $|S|=k$. Replace $x_i$ by $\sum_{j\in S}x_j/k$ for each $i\in S$, leaving the other entries unchanged. The target is the original mean $\bar x$ in every position.

For a nonconstant input, center it, clear denominators, and divide by the gcd of all coordinates to obtain a primitive integer zero-sum vector $X$. Define

$$G(X)=\gcd_{i<j}|X_i-X_j|.$$

The project's prime-arity theorem gives, for every odd prime $p$ and $n\ge2p+1$, finite reachability exactly when $G(X)=p^e$ for some $e\ge0$. The final threshold $2p+1$ is optimal; binary averaging has final threshold $N(2)=4$. Only when $p\nmid n$ may the criterion be shortened to $G=1$.

The binary literature uses **Condition (MC)** and waste-free **mixing graphs**. The project develops ternary and higher-arity extensions. A state-dependent path for each eligible rational input is different from a single fixed averaging network that works for all real inputs; results about finite-time consensus or clique gossiping must respect that distinction.

## Start by topic

| Topic | Main entry | What to read |
|---|---|---|
| Binary / pairwise averaging | [Binary topic](topics/binary/README.md) | Perfect Mixability source review; Python, JavaScript and Prolog tools; 1,636 benchmark instances |
| Ternary / triple averaging | [Ternary topic](topics/ternary/README.md) | Direct repeated-value proof, dimensions 7–10, LaTeX/PDF, algorithm benchmarks |
| Prime arity $p$ | [Prime topic](topics/prime/README.md) | Full dimension coverage, positive realizations, congruence subgroups, exact fibers, finite certificates |
| General arity $k$ | [General topic](topics/general/README.md) | Composite arities, prime powers, fixed networks, unconditional and GRH-conditional results |
| Proof simplification | [Independent local-arithmetic research](archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/README.md) | Marked lattices, dyadic column lifting, root ideals and carrier updates |
| What each check establishes | [Claim-to-check index](catalog/CHECKS.md) | All 185 registered checks with documents, scripts, scope and exclusions |

Most original research documents are in Chinese. This English entry and the bilingual guides explain the model, current scope, proof architecture and reproduction commands; they do not claim that every archived proof has been translated.

## Proof architecture and status

The [bilingual proof guide](docs/PROOF_GUIDE.md) explains two successful mechanisms. Binary and direct ternary proofs preserve repeated values and arithmetic witnesses while a discrete integer energy decreases. The prime-arity proof also uses safe reduction to weighted cores, **genuinely executable positive returns and inverses**, elementary root operations, deep congruence fibers, and finite direction-and-scale corrections before a zero-sum terminal step.

The prime proof cites Morris's finite-index theorem and the stated strong congruence subgroup property for rational S-integer $\mathrm{SL}_2$. Finite certificates remain part of the archived proof. The 2026-09-16 dyadic column lemma uniformly replaces two interior orbit tables with 64 and 256 parameter classes; it does not remove the 162 nine-offset physical/root-ideal certificates or all other finite evidence.

General composite arity is **not completely solved**. Every $2k+1$ endpoint has an unconditional result, but this does not imply a final threshold of $2k+1$. Square-arity and some prime-power critical results explicitly assume GRH. See the [current general-arity handoff](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_three_tasks_progress_20260915.md).

These are the project's recorded proof claims, with audit trails. This repository is not a proof-assistant formalization or a claim of completed external peer review. Exact finite verification does not establish an unbounded theorem by itself.

## Reproduce without changing the archive

Python 3.11+ is required. The review suite also uses Node.js for the binary JavaScript tests. The selected Python checks use the standard library; optional research dependencies are listed in [requirements.txt](requirements.txt).

~~~sh
git clone https://github.com/test27818/finite-averaging-research.git
cd finite-averaging-research
python -B scripts/check_archive.py
python -B scripts/build_check_index.py --check
python -B scripts/reproduce.py --suite review
~~~

The last command runs the documented checks in a temporary copy, preserving the 1,905 archived files. It reports failures, missing tools, and skipped checks explicitly. Read the [verification guide](docs/VERIFICATION.md) for individual suites, expected results, dependency boundaries and interpretation of PASS. The review suite is selected evidence across all four themes, not every historical search or all general-$k$ results.

**Known verification issue:** the first review passed the selected mathematical checks but failed one binary Python zero-budget status test. A controlled-clock diagnostic reproduces the discrepancy; returned paths remain exactly verified and are not claimed optimal. See [KNOWN_ISSUES.md](docs/KNOWN_ISSUES.md) and the preserved [run report](catalog/REPRODUCTION_CHECKS.json). The frozen source is unchanged.

## Repository layout

| Location | Role |
|---|---|
| [topics/](topics/) | Four thematic entry points |
| [docs/](docs/README.md) | Bilingual definitions, proof strategy and reviewer instructions |
| [catalog/](catalog/) | Full file list, hashes, check index and recorded publication/reproduction results |
| [archive/2026-09-07/3-3-triple-average-research-note/](archive/2026-09-07/3-3-triple-average-research-note/) | Main organized research: outputs, exact verifiers, historical notes and independent improvements |
| [archive/2026-09-07/new-chat-3/averaging_benchmark/](archive/2026-09-07/new-chat-3/averaging_benchmark/) | Binary solver, data, tests and earlier versions |
| [archive/2026-09-10/new-chat/](archive/2026-09-10/new-chat/) | Ternary paper, algorithm challenges and supplemental work |

The 2026-09-16 snapshot preserves **1,905 original files** byte-for-byte, including 590 Markdown documents, 479 Python scripts, 42 PDFs and 22 LaTeX sources. Dated workspace paths preserve existing imports and cross-workspace references. The thematic front pages avoid requiring readers to navigate by date. Historical absolute paths and migrated links may need manual translation; see [provenance and portability](PROVENANCE.md) and the [complete file catalog](catalog/FILES.md).

## Literature and attribution

A central binary source is Miguel Coviello Gonzalez and Marek Chrobak, *Towards a Theory of Mixing Graphs: A Characterization of Perfect Mixability*, [arXiv:1806.08875v4](https://arxiv.org/abs/1806.08875v4), [journal DOI](https://doi.org/10.1016/j.tcs.2020.09.007). The [source reassessment](archive/2026-09-07/3-3-triple-average-research-note/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md) states which claims and constructions transfer.

Research notes record human–AI collaboration, including failed approaches and corrections. Third-party papers, source archives and captured pages retain their original attribution and rights; see [THIRD_PARTY.md](THIRD_PARTY.md).
