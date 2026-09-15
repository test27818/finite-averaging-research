# Perfect Mixability and Finite Averaging

**[中文](README.md) · English · [Proof guide](docs/PROOF_GUIDE.md) · [Verification](docs/VERIFICATION.md) · [Terminology](docs/TERMINOLOGY.md)**

**When can rational numbers on fixed positions be made exactly equal by finitely many averaging operations?** Each operation selects exactly $`k`$ distinct positions and replaces all their values by their arithmetic mean. No additional copies or discarded outputs are allowed. This repository studies **perfect mixability**, **mixing graphs**, binary, ternary, prime-arity and general k-ary averaging.

> **Highlights: an independent direct proof for ternary averaging; the optimal final threshold for every prime arity; a precise composite-arity threshold conjecture with a proved universal lower bound and several completed families. Work continues toward more natural, readable and structurally unified proofs, and the remaining composite-arity cases.**

The project's new results were developed primarily through sustained collaboration between the user and **GPT-6 Astra (gpt6-astra)**. Completed proofs have undergone repeated internal review, cross-checking and targeted exact verification. Corrections, withdrawals, source assumptions and known issues are retained. The prior binary theorem remains attributed to its original authors; see [provenance](PROVENANCE.md).

## Main achievements

For a nonconstant rational input, center it, clear denominators, and divide out the coordinate gcd to obtain a primitive integer zero-sum vector $`X`$. Set

```math
G(X)=\gcd_{i\lt j}|X_i-X_j|.
```

Here $`\mathrm{rad}(m)`$ is the product of the distinct primes dividing $`m`$. General $`k`$-averaging requires $`\mathrm{rad}(G)\mid k`$; the table specifies ranges where sufficiency has been established. Constant input always takes zero steps.

| Achievement | Precise scope and significance | Proof source |
|---|---|---|
| **Complete binary classification: literature foundation** | **Every four-entry input is unconditionally mixable with four fixed operations.** Other powers-of-two sizes are also unconditional. For remaining $`n\ge5`$, the criterion is that $`G`$ is a power of 2; at $`n=3`$, the input must be an arithmetic progression | [Classification and four-operation proof](docs/BINARY_CLASSIFICATION.md) |
| **Independent direct ternary proof** | For every $`n\ge7`$, mixability iff $`G`$ is a power of 3. A two-triple invariant handles all $`n\ge11`$, with separate bases at 7, 8, 9 and 10; no general prime/composite dimension reduction is needed | [Direct proof](archive/2026-09-07/3-3-triple-average-research-note/outputs/triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md) |
| **Optimal final threshold for every odd prime** | $`\boxed{N(p)=2p+1}`$ for every odd prime $`p`$. At all $`n\ge2p+1`$, the criterion is $`G=p^e`$, with $`e`$ a nonnegative integer. Eligible but unreachable inputs at $`n=2p`$ establish sharpness | [Full proof and dimension coverage](archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/proof.md) |
| **Common endpoint and linear tail for arbitrary arity** | Every $`k\ge2`$ has the complete $`G=1`$ criterion at $`n=2k+1`$; every $`k\ge3`$ satisfies $`N(k)\le4k+\lceil\log_2k\rceil+1\le5k`$ | [Endpoints and status](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_three_tasks_progress_20260915.md) · [Linear tail](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/arbitrary_arity_linear_threshold.md) |
| **Families of dimensions and block-mean transfer** | Complete arithmetic criteria for all $`n=jk`$, $`j\ge3`$, at any arity $`k\ge2`$; also every odd $`2k\lt n\lt 3k`$ for odd prime-power arity $`k=p^a`$ | [Block-mean transfer](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/averaging_proof_strategy_and_composite_frontier_20260915.md) · [Odd middle band](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/odd_composite_coprime_middle_band_completion.md) |
| **Unconditional fixed-network families** | Four operations for $`k=m(m-1)`$ on $`n=m^2`$ positions, integer $`m\ge2`$; $`2b+2`$ operations for $`k=2(4^b-1)/3`$ on $`n=4^b`$, integer $`b\ge1`$, including a fixed six-operation network for ten-averaging on sixteen positions | [Four-operation family](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/composite_critical_scale_and_conjecture.md) · [Ten-averaging and recurrence](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/ten_average_sixteen_and_dyadic_network_family.md) |
| **GRH square family and selected optimal critical points** | Every $`k=t^2`$, integer $`t\ge2`$, has a complete criterion at $`n=t^2+t+1`$. All prime powers with even exponent and all powers of 2 and 3 attain their respective earliest critical lower bounds under GRH. **These are not final-threshold results for every later dimension** | [Square family](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md) · [Odd powers of 2 and 3](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/two_three_odd_power_critical_grh_completion.md) |
| **Uniform dyadic column lifting** | Squares, commutators and lifting of three existing physical returns replace two interior orbit tables with 64 and 256 parameter classes, retaining both direction and scale | [Independent 2026-09-16 improvement](archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/structural_reassessment_and_uniform_dyadic_orbits.md) |

**Algorithms:** binary tools include Python, a JavaScript webpage, Prolog and 1,636 benchmark instances with 538 verified paths. Ternary/prime-arity work includes difficult instances, exact position-based path checkers, a PDF/LaTeX paper and construction scripts. Decision, construction and certified shortest paths are separate tasks; exhausted search budgets do not prove unreachability.

## The methods that make the proofs work

**1. Repeated values protect arithmetic witnesses; discrete energy proves termination.** The binary source preserves two distinct repeated values, while the direct ternary proof preserves two distinct triply repeated values. Surviving copies keep nonconstant residue witnesses at dangerous primes. Reserving one extra precision digit permits safe nontrivial operations on an integer lattice, with strictly decreasing $`\sum_iX_i^2`$, until an explicit terminal configuration is reached. This is how the direct ternary proof avoids the old seed-search approach. Four-entry binary averaging and other powers-of-two sizes use a fixed network directly.

**2. Critical dimensions use controlled cores and genuinely positive inverses.** Safe grouping reduces an input to a few equal-value blocks on its original positions. Explicit nonnegative counts produce returns $`J`$ with $`J^2=cI`$, $`c\ne0`$, on the entire core, providing executable projective inverses. Quotients and commutators of neighboring count constructions yield shear roots. Their parameter ideals and actual multipliers determine the localization ring. An abstract inverse matrix is never substituted for an executable averaging operation.

**3. The integral mean lattice explains congruences; exact fibers reach rational terminals.** Gluing the constant direction to the integer zero-sum lattice supplies natural congruence markings. Actual roots, together with the cited Morris/Serre tools, give deep congruence control. Finite adjustments must preserve **both direction and allowed unit scale**; exact congruence fibers then reach a genuine zero-sum terminal. The new dyadic column lemma replaces some orbit tables by one linear error-correction rule.

**4. Composite arity combines block means, fixed networks and local valuations.** Quotient operations are realized by averaging unions of original blocks; unselected blocks need not be equalized first. Valuation traps at allowed primes give critical lower bounds. Square cores and mixed-arity networks supply actual positive constructions. In the conditional results, GRH supplies small-unit generation at the arithmetic endpoint; it cannot supply missing positions, positive inverses or termination.

[Proof guide and dependency diagram](docs/PROOF_GUIDE.md) · [Common arithmetic toolkit](archive/2026-09-07/3-3-triple-average-research-note/outputs/prime_arity/arithmetic_toolkit.md) · [Independent structural improvements](archive/2026-09-07/3-3-triple-average-research-note/research/prime_arity_padic/README.md)

## The precise general-k threshold conjecture

Let $`\mathcal P(k,n)`$ mean that every rational input in that dimension obeys the complete characterization: mixability iff $`\mathrm{rad}(G)\mid k`$, treating constant input separately. Three quantities matter:

| Quantity | Definition | Example |
|---|---|---|
| $`M(k)`$ | The first dimension $`n\gt k`$ satisfying $`\mathcal P(k,n)`$; the trivial point $`n=k`$ is excluded | $`M(6)=9`$, via an unconditional network |
| $`H(k)`$ | The first such dimension with $`\mathrm{rad}(n)\nmid k`$, where the gcd condition actually excludes some inputs | $`H(6)=10`$; binary $`M(2)=4`$ but $`H(2)=5`$ |
| $`N(k)`$ | The smallest starting dimension above $`k`$ such that **every subsequent dimension** satisfies $`\mathcal P(k,n)`$ | $`N(3)=7`$; general composite final thresholds remain open |

Write $`k=\prod_p p^{a_p}`$ and define the local critical scale

```math
S(k)=\max_{p\mid k}p^{\lceil a_p/2\rceil},
```

and

```math
B(k)=k+S(k)+
\begin{cases}
0,&\mathrm{rad}(k+S(k))\mid k,\\
1,&\mathrm{rad}(k+S(k))\nmid k.
\end{cases}
```

**Proved lower bounds: $`M(k)\ge B(k)`$ and $`N(k)\ge B(k)`$. The main conjecture has two parts:**

```math
\boxed{M(k)=B(k)}
\qquad\text{and}\qquad
\boxed{N(k)=M(k)}.
```

Together they predict $`\boxed{N(k)=B(k)}`$. The first asks whether the lower bound is attainable; the second asks whether any gaps remain after the first success. **Neither follows from finitely many successful examples.** The corresponding conjecture for the first nonautomatic arithmetic dimension is

```math
H(k)=C(k),\qquad
C(k)=\min\{n\gt k+S(k):\mathrm{rad}(n)\nmid k\}.
```

**Why this formula is structural:** for each $`p^a\parallel k`$, fewer than $`p^{\lceil a/2\rceil}`$ remaining positions cannot break a minimal-valuation $`k`$-fold block: every nontrivial averaging recreates the trap. Taking the worst local scale gives $`S(k)`$. At the boundary, escaping the valuation trap can introduce a forbidden common residue, explaining the possible extra 1 in $`B(k)`$. This accounts for the odd-prime threshold $`2p+1`$, four-averaging at seven positions and eight-averaging at thirteen positions in the same framework.

| Arity $`k`$ | Predicted critical point $`B(k)`$ | Proved earliest-point result | Final threshold $`N(k)`$ |
|---|---:|---|---|
| 2 | 4 | $`M=4,\ H=5`$; four entries unconditional | **Proved: 4** |
| Odd prime $`p`$ | $`2p+1`$ | $`M=H=2p+1`$ | **Proved for every odd prime: $`2p+1`$** |
| 4, 8, 9 | 7, 13, 13 | Respectively $`M=H=7,13,13`$, unconditionally proved | Not determined |
| 6 | 9 | $`M=9,\ H=10`$ | Not determined |
| 10, 12 | 16, 16 | Both have $`M=16,\ H=17`$, unconditionally proved | Not determined |
| $`p^{2a}`$, $`a\ge1`$ | $`p^{2a}+p^a+1`$ | $`M=H=B`$ under GRH; some small cases also unconditionally proved | Not determined in general |
| $`p^{2a+1}`$, $`a\ge1`$, $`p=2,3`$ | $`p^{2a+1}+p^{a+1}+1`$ | $`M=H=B`$ under GRH | Not determined in general |
| 14, 15, 18 | 22, 21, 22 | Lower bounds proved; sufficiency at the critical point remains open | Not determined |

For squares with mixed prime factors, the square-family theorem need not attain $`B(k)`$: for $`k=36`$, it gives $`n=43`$ under GRH, while $`B(36)=40`$. Also, $`\mathrm{rad}(n)\mid k`$ makes the gcd condition automatic but **does not by itself provide a mixing network**: an eligible unreachable input is known for $`k=24,n=27`$.

[Original critical lower bounds and conjectures](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/composite_critical_scale_and_conjecture.md) · [Latest established scope and remaining tasks](archive/2026-09-07/3-3-triple-average-research-note/outputs/general_arity/general_k_three_tasks_progress_20260915.md)

## Current research priorities and limits

- **Unifying the proof:** extract common count constructions, root ideals and column-lifting mechanisms from the completed prime proof. The 162 nine-offset physical/root-ideal certificates and other finite evidence remain; the entire proof is not yet certificate-free.
- **Composite critical points:** handle high odd powers of primes $`p\ge5`$ and mixed arities such as 14, 15 and 18. Local carry mechanisms at different allowed primes must coexist along one actual path.
- **Propagation through dimensions:** extend from $`M(k)`$ or the $`2k+1`$ endpoint to every later dimension. Odd bands, divisibility transfers and the wide tail do not yet give general $`N(k)=B(k)`$.
- **Constructive efficiency:** extract shorter executable averaging sequences from existence proofs. No uniform polynomial operation-length or shortest-path algorithm is established for all varying $`k,n`$.

The prime result is unconditional but uses the cited Morris/Serre theorems. Composite GRH assumptions are explicitly labeled. Repeated internal review is not external peer review or proof-assistant certification. Each program's PASS has its stated scope, and failed approaches, historical claims and software issues remain visible.

## Reading routes and repository structure

| Reader goal | Entry |
|---|---|
| Binary classification, unconditional small dimensions and solvers | [Binary topic](topics/binary/README.md) |
| Direct ternary proof, small bases and PDF/LaTeX paper | [Ternary topic](topics/ternary/README.md) |
| Prime theorem, every dimension range and dependencies | [Prime topic](topics/prime/README.md) |
| Composite arity, GRH and open questions | [General topic](topics/general/README.md) |
| Find the proof and code for a claim | [185-entry claim-to-check index](catalog/CHECKS.md) |
| All original files and research history | [Complete catalog](catalog/FILES.md) · [Historical route ledger](archive/2026-09-07/3-3-triple-average-research-note/outputs/history/research_routes_history_20260915.md) |
| Algorithm benchmarks | [Binary 1,636-instance benchmark](archive/2026-09-07/new-chat-3/averaging_benchmark/README.md) · [Difficult ternary/prime cases](archive/2026-09-10/new-chat/outputs/averaging_algorithm_benchmark/README.md) |

~~~text
topics/              Binary, ternary, prime and general-arity entries
docs/                Bilingual definitions, proof and verification guides, known issues
catalog/             File and verification indexes, hashes and execution records
scripts/             Archive checks and temporary-copy reproduction
archive/
  2026-09-07/
    3-3-triple-average-research-note/
      outputs/       Organized proofs, literature and research history
      research/      Independent structural improvements
      work/          Original verifiers, certificates, exploration and sources
    new-chat-3/      Binary solver and benchmark
  2026-09-09/cha/    Historical document review
  2026-09-10/new-chat/ Paper, algorithm challenges and supplements
~~~

**Snapshot: 2026-09-16.** The archive preserves 1,905 source files, including 590 Markdown documents, 479 Python scripts, 42 PDFs and 22 LaTeX sources. Dated paths preserve original imports and cross-workspace references; topic pages give current reading routes. Original research is mainly in Chinese; these English guides are not translations of every proof. Historical notes may contain outdated status or paths; see [provenance and portability](PROVENANCE.md). The archived sources are unchanged by editorial updates.

## Verify the evidence

Use Python 3.11+ and Node.js for the binary JavaScript regressions. The review suite works in a temporary copy, preserving the archive:

~~~sh
git clone https://github.com/test27818/finite-averaging-research.git
cd finite-averaging-research
python -B scripts/check_archive.py
python -B scripts/build_check_index.py --check
python -B scripts/reproduce.py --suite review
~~~

The [verification guide](docs/VERIFICATION.md) explains commands, scope and dependencies. The [complete review log](catalog/reproduction_review.txt) records actual results. **The latest full review passed the selected mathematical checks but failed one binary Python zero-budget timing-status test.** Its cause and deterministic diagnostic are disclosed in [known issues](docs/KNOWN_ISSUES.md); the run is not labeled all-green.

The binary [offline webpage](archive/2026-09-07/new-chat-3/averaging_benchmark/solver.html) can be downloaded and opened directly. Some additional scripts require [optional dependencies](requirements.txt). Archive integrity, exact finite verification and general mathematical proof are different levels of evidence.

## Original problem and literature

A central binary source is Miguel Coviello Gonzalez and Marek Chrobak, *Towards a Theory of Mixing Graphs: A Characterization of Perfect Mixability*, [arXiv:1806.08875v4](https://arxiv.org/abs/1806.08875v4), [journal DOI](https://doi.org/10.1016/j.tcs.2020.09.007). The [source reassessment](archive/2026-09-07/3-3-triple-average-research-note/outputs/literature/triple_average_binary_source_reassessment_2026-09-11.md) explains Condition (MC), repeated-value methods and their transfer limits.

**Search vocabulary:** perfect mixability, mixing graphs, finite-step averaging, pairwise/binary averaging, ternary/triple averaging, prime-arity averaging, general k-ary averaging; 完美可混合性、完全可混合性、混合图、有限步平均、两数平均、三数平均、素数平均、合数平均。Finite-time consensus and clique gossiping are related subjects, but universal fixed networks and state-dependent reachability have different quantifiers; see the [bilingual terminology guide](docs/TERMINOLOGY.md).

Third-party sources retain their original attribution and rights: [THIRD_PARTY.md](THIRD_PARTY.md). [Research provenance and review history](PROVENANCE.md) · [Source hashes](catalog/SHA256SUMS.txt)
