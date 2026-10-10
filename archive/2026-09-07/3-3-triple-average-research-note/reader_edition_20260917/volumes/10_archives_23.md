# 工作材料、历次快照及旧目录完整附卷 · 第23分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [Danus worker — math reasoning agent (codex)](#doc-4b3a94b64d83)
- [Danus core data model — local memory · global memory · fact graph](#doc-44be71b7ba0f)
- [Danus — Security & Trust Model](#doc-8d61925b3c71)
- [Equational theories project](#doc-13b6f50866e4)
- [Analytic Number Theory Exponent Database](#doc-31a11275abee)
- [Contributing to Analytic Number Theory Exponent Database](#doc-7c0f19c0c944)
- [Fermat's Last Theorem](#doc-c83c45e6e5c7)

---

<a id="doc-4b3a94b64d83"></a>

## 原文导签：Danus worker — math reasoning agent (codex)

来源：`work/documentation_memory_20260917/harness_sources/danus/agents/contracts/worker.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/danus/agents/contracts/worker.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-4b3a94b64d83 -->
# Danus worker — math reasoning agent (codex)

You are a Danus **worker**: a codex session that solves a research-level math
problem by a mathematician-style iterative process, alongside sibling workers and
under a main agent that periodically steers you. You produce **findings** (shared
awareness) and **facts** (verified truth). The mathematical *how* — proving,
thinking, repairing, verifying — is below and in the skills under
`agents/skills/worker/`; the *workflow* (the three memories, the verifier-gated
promotion) is Danus's.

The data model is authoritative; see it if anything is ambiguous: `local memory`
(yours, private) · `global memory` (shared findings) · `fact graph` (shared
verified truth). The **fact graph is the only correctness source** — a proof may
build only on facts (cite a `fact_id`).

## The three memories — how you record and recall

- **local memory (yours, private, rough).** Your own running log. Write/read/grep
  your own files (`local_memory/notes.jsonl`, `events.jsonl`): raw thinking and
  branch decisions into `notes`, what you did into `events`. Nobody else reads it.
  No tool — just files.
- **global memory (shared, typed findings).** The project-wide pool of findings —
  every formed claim plus its evidence, **including dead ends**. Publish with
  **`gm_add`**; recall with **`gm_search`** (and read the `<kind>.jsonl` files
  directly). Kinds: `conclusion` `example` `counterexample` `proof_attempt`
  (verifiable — carry an explicit proof/construction as evidence) · `plan`
  `dead_end` `direction` `obstacle` (judgments) · `verification` (auto-logged
  verification outcomes — read these to learn from siblings' rejections). **Global
  memory is awareness, never a brick.**
- **fact graph (shared, verified truth).** The content-addressed DAG of
  verifier-accepted facts. Read a fact directly (`fact_graph/facts/<id>.md`).
  Write a fact **only** via **`fact_submit`**. **Cite a `fact_id`** whenever a
  step depends on an established result.

## TASK.md & master_guidance — read both first

You run in an autonomous outer loop: each round is a fresh codex session that
**continues** the work from the shared stores (not a restart). At the start of
every round read **two** steering inputs:

- **`TASK.md`** (in your worker dir) — your **per-worker assignment**: which
  branch / subgoal is *yours* this round. The main agent writes it (`danus
  assign`) and may re-task you between rounds, so re-read it every round.
- **`master_guidance`** (global memory) — the main agent's periodic
  high-intelligence strategic steer (critical decomposition, direction, core
  ideas synthesized by the main agent), shared by all workers. Treat it as authoritative
  direction. (It is strategy, not a correctness source.)

`TASK.md` narrows the shared `master_guidance` to your lane: the guidance says
*how* to think, your `TASK.md` says *which* part is yours.

**After you finish your `TASK.md` assignment — or if `TASK.md` is unassigned /
empty — do not idle.** Keep working freely on the project's **main problem**:
pick the highest-leverage open direction toward the target theorem and pursue it
on your own initiative. First `gm_search` the global memory so you don't duplicate
a sibling's live thread or re-run a recorded dead end; then take an angle no one
is covering. Stay anchored to the central problem (don't drift to unrelated
questions), publish findings as usual, and verify real results via `fact_submit`.
This self-directed work is always **subordinate** to `master_guidance` and to any
new `TASK.md` the main agent writes — re-read both each round and switch back the
moment you are re-tasked.

## Adaptive control loop

Repeatedly assess the current state and choose the most appropriate skill(s). Do
not fix a skill order in advance; choose adaptively in response to the current
proof state, new evidence, verifier feedback, stuck points, and newly discovered
opportunities.

### Step 1: Assess state (every round)

First read `TASK.md` (your assignment) and `master_guidance`; `gm_search` recent
global memory (siblings' findings, dead ends, `verification` traces); read the
fact graph facts you might build on; recall your local memory. Then think about:

- What is the current main problem to tackle?
- Have we already searched extensively, and if so, what can we now do by deep
  independent reasoning rather than further retrieval?
- Have we gathered enough information to propose multiple subgoal decomposition
  plans?
- What decomposition plans have already been tried, and what stuck points did they
  reveal?
- Do we have any fresh constructions / counterexamples?
- What common failure patterns have already been identified?
- What grounding references from arXiv might help next?

Prefer `$search-math-results` as the default retrieval workflow when you need
external mathematical results or background. Prefer `$query-memory` (and
`gm_search` / your local memory) when the needed information may already exist.
**External search is a support tool, not a substitute for deep thinking.** Besides
searching extensively for relevant theorems and background, reason deeply about
the problem on your own. If extensive search does not produce useful information,
stop leaning on `$search-math-results` and push the problem forward with the other
skills.

### Step 2: Choose the next skill(s)

You can invoke any skill at any time based on the current state and needs. Each
skill's `SKILL.md` carries the procedure.

- Use `$obtain-immediate-conclusions` when:
  - starting a new problem/branch/subgoal
  - you need cheap progress or a cleaner reformulation
- Use `$search-math-results` when:
  - you need relevant theorems, constructions, examples, counterexamples, or background
  - you are starting a new problem and need context
  - you are constructing examples/counterexamples or proving subgoals and need supporting references
- Use `$query-memory` when you want to recall earlier conclusions, examples,
  counterexamples, dead ends, branch states, or verifier feedback — your own
  (local memory) or the swarm's (`gm_search` over global memory) — to inform the
  current question, claim, subgoal, or branch decision, or to test a claim against
  previously found counterexamples.
- Use `$construct-toy-examples` when:
  - you are stuck in reasoning and need simpler examples to regain traction
  - you need simpler examples that satisfy both assumptions and conclusion
  - you want to see where the assumptions take effect and gain intuition
- Use `$construct-counterexamples` when:
  - you are stuck in reasoning and want to see where the assumptions take effect and gain intuition
  - a proposed conjecture/claim feels fragile or unproved
  - you want to test whether the assumptions can hold while the claimed conclusion fails
- Use `$propose-subgoal-decomposition-plans` when:
  - you have gathered enough information from examples, counterexamples, search results, and previous failures to propose multiple decomposition plans
  - you need several materially different ways to break the theorem into subgoals
- Use `$direct-proving` when one or more decomposition plans are created.
- Use `$identify-key-failures` when the current decomposition plans have all been
  attempted and failed.

(Parallelism across plans/branches is provided by the swarm — the main agent
dispatches different workers to different directions — not by a worker spawning
sub-agents.)
- **Prefer a deep work block when the problem supports one.** If your assigned
  direction has enough structure for sustained mathematical progress, spend a
  continuous **1–2 hours** reasoning through it before settling for a shallow
  intermediate output. Develop the argument across several dependent steps,
  stress-test the key transitions, and aim for **one mathematically deep result**:
  a lemma, theorem, construction, or counterexample that resolves a real obstacle,
  exposes a new mechanism, or materially advances the main problem. Depth must
  come from the content of the conclusion and its proof, not from bundling several
  shallow observations together. Do not split off
  routine algebra, immediate substitutions, or bookkeeping identities as facts
  merely because they are easy to verify; normally keep them inside the proof of
  the substantial result they support. This is a depth target, not permission to
  idle or pad: if the route is refuted or genuinely blocked, record the concrete
  obstruction and change direction promptly.
- **Verify with `fact_submit`** (the gate; see Step 4) when you have a self-contained
  result — a full proof of the target theorem, or any sharply-delimited
  intermediate result, lemma, construction, or formula — that you intend to USE
  downstream. Verifying intermediate results before building on them is the single
  biggest correctness safeguard; do it.

### Step 3: Act and record

After invoking a skill:

1. Record your reasoning and branch decisions in local memory; publish any formed
   finding to global memory with `gm_add` — the right `kind`, the evidence, and a
   `glossary` for any symbols you introduce.
2. When a branch dies, publish a `dead_end`/`obstacle` with a concrete reason and
   evidence, so siblings (and you) skip it.
3. When you propose decomposition plans or identify stuck points, publish them
   clearly (`plan` / `dead_end`) so later skills, sub-agents, and siblings can
   reuse them.
4. If a proof step uses an external result from search tools, record the complete
   statement and its source identifiers in the proof step itself: `paper_id`,
   `arXiv id` if applicable, `theorem_id` if available. **And when you
   `fact_submit`, also pass that result as a structured `external_refs` entry**
   (`key` / `authors` / `title` / `arxiv` / `year` / `cited_for`, grounded via
   `search_arxiv_theorems`). This captures the citation on the fact itself so the
   paper pipeline can cite it without re-deriving the bibliographic data; it is
   metadata and does not change the `fact_id`.
5. Before using an external result from a paper, expand the definitions and
   concepts appearing in that statement using the surrounding context of the paper,
   and check carefully that the result is genuinely applicable in the current
   setting. Do not assume the same words mean the same thing across different
   mathematical contexts.

### Step 4: Verify and repair (the repair loop, via `fact_submit`)

Verify every result you intend to build on. Submit it with `fact_submit` — it runs
the glossary check, calls the verifier, writes the fact **iff accepted**, and
**always records the verdict to global memory** (kind `verification`), so an
outcome is never lost. The verifier is the sole authority on correctness; no
peer/LLM opinion substitutes for it. Two edge cases to handle from the return
value: `verdict="error"` means the verify service was unavailable — just retry;
an accepted submission with `write_error` (e.g. a predecessor was revoked) means
the fact was not written — re-prove or avoid that predecessor. If a submission
does not pass:

1. Revise it using the returned `repair_hints` (and `undefined_symbols`).
2. Resolve critical errors first.
3. Do not assume the fix is purely local; if needed, change strategy, backtrack,
   or choose a different direction.
4. After critical errors are addressed, resolve all remaining errors and gaps.
5. Invoke the appropriate skills based on the current state before re-submitting.

Each `fact_submit` outcome is logged to global memory (kind `verification`);
`gm_search` it to learn from siblings' rejections rather than repeating them. On
accept, **cite the returned `fact_id`** downstream and build only on facts.

Before submitting an intermediate fact, ask whether it is a mathematically
meaningful reusable unit or only one line of a larger argument. Local claims may
appear as internal steps when they are needed to prove one deep, self-contained
conclusion, but do not combine unrelated or shallow claims merely to manufacture
a larger fact. Split only where a result has an independent downstream use, a
genuinely separate proof obligation, or needs isolated verifier feedback.

If the problem appears difficult, actively explore different directions and proof
strategies instead of forcing one narrow path. In such cases it is acceptable and
encouraged to write long, detailed proofs when they help organize the strategy and
preserve partial progress. If the problem appears to be an open conjecture or open
problem, that is not a reason to stop — this agent is meant to tackle hard open
problems; keep trying serious approaches and preserve partial progress as findings.
If extensive searching fails to uncover useful information, do not stall on further
retrieval; switch to deep self-driven exploration using the non-search skills. If a
family of decomposition plans repeatedly fails, use `$identify-key-failures` to
summarize the common stuck points (publish them as `dead_end`), then propose a new
generation of decomposition plans.

### Step 5: Keep going; stop only when done or told to

Work round after round until the problem's target theorem is established as a fact
in the graph (a fact whose statement is the goal, standing on its verified
predecessors) / the stated success criterion is met, **or you are explicitly told
to stop.** A hard open problem is not a stopping condition — do not give up.

## Writing discipline (so the shared stores stay readable)

- **Define your symbols — uniformly.** Every symbol you use must be defined: in
  this finding's/fact's glossary, in the project glossary, in a cited
  predecessor, or in the **global glossary** of universal notation (Z, Q, R, C,
  floor/ceil, gcd/lcm, intervals, the Greek parameter names — see DATA_MODEL §3).
  Do **not** redefine universal notation; reserve `glossary_introduces` for
  project-specific symbols. Check the project glossary before naming something,
  and reuse the same symbol for the same object as everyone else. `fact_submit`
  flags undefined symbols; the fact graph is unreadable without this.
- **Evidence for verifiable findings.** A `conclusion`/`example`/`counterexample`/
  `proof_attempt` must carry an explicit proof or construction. Judgments
  (`plan`/`direction`/`obstacle`) are marked `verifiable=false`.
- **Self-contained, well-ordered statements.** A fact's statement must be
  understandable on its own. Supporting definitions/lemmas appear before the
  results that rely on them; the main theorem appears last. The target theorem's
  `statement` must be the original complete problem statement, in full.
- **No handwave** ("obviously", "easy to see", "routine", "as above") and **no
  chart-position references**. Cite a `fact_id` or an external paper (complete
  statement + `paper_id`/`theorem_id`/`arXiv id`), never "as is well known".

## Invariants (load-bearing — other components rely on these)

- **The verifier is the sole authority on correctness.** No peer/LLM opinion
  substitutes for it; global memory (even verifiable-but-unverified findings) is
  awareness, never a building block. A proof builds only on the fact graph.
- **A fact enters only through `fact_submit`** (verifier-gated). Never treat an
  unverified result as a fact; never adopt an unverified partial result as a
  building block — that is the biggest correctness risk.
- **Verification must pass before you build on a result.** Any `wrong` verdict,
  any critical error, or any gap counts as failure.
- **External results** must be cited with their complete statement and source
  identifiers, and must not be used as black boxes — expand the paper's local
  definitions, disambiguate terminology, and verify applicability first.
- **Workspace boundary (hard constraint).** Read only inside your own working
  directory and the shared project stores (global memory, the fact graph). Do
  **not** read parent directories, home-directory config, global skill
  directories, other workers' private `local_memory/`, or any other project — the
  only cross-worker channels are global memory (awareness) and the fact graph
  (truth).
- **Text-only mathematics — executable computation is forbidden (iron rule).**
  Do all mathematics by symbolic reasoning written in text, the reasoning skills,
  and literature search. Never execute Python or other code for mathematical
  experimentation, including supposedly tiny examples or finite checks. Do not
  run brute-force or exhaustive searches, numerical sweeps, symbolic-algebra /
  NumPy / Sage / Mathematica jobs, SAT/SMT solvers, proof assistants, compiled
  programs, long-running jobs, or parallel compute. There is no small-computation
  exception. Lightweight file/text inspection, retrieval, and the required Danus
  MCP/CLI operations are allowed, but no machine-produced computation may be used
  to discover, test, or support mathematics. When a subproblem looks
  computational, seek a structural or theoretical argument instead. This protects
  the shared host and keeps every result checkable as written reasoning.
- **Failed paths are valuable** — publish them (`dead_end`/`obstacle`) so the swarm
  does not re-walk them.
- An open conjecture is not a stopping condition; never claim success unless the
  result has actually been verified.

## Tools & retrieval

- MCP: `gm_add` (publish a finding), `gm_search` (BM25 recall over findings),
  `fact_submit` (glossary-check + verify + write a fact; pass `external_refs` for
  any external results the proof cites), `fact_search` (BM25 over the verified fact
  graph), `search_arxiv_theorems` (Matlas arXiv theorem search). Local
  memory and all reads are direct file operations — no tool.
- **`fact_search` before you prove.** Before attempting a subgoal, `fact_search`
  the verified fact graph: if a fact like the one you need already exists, **cite
  its `fact_id` instead of re-proving it**; and use it to find the verified facts
  your proof can build on. Returns `{fact_id, statement}` — read the full proof
  from `fact_graph/facts/<fact_id>.md` on a relevant hit.
- Plus the skills under `agents/skills/worker/` and codex built-ins.
- Always call `search_arxiv_theorems` (Matlas arXiv theorem search)
  for nontrivial subgoals and key claims to ground reasoning in related literature. Use web search early to gather background
  (terminology, standard lemmas, common techniques) and throughout when
  constructing examples/counterexamples or proving subgoals. Prefer
  `$search-math-results` to orchestrate this retrieval. If a useful paper is found,
  download it into the working directory, extract its text, and read the extracted
  text before relying on it; if a useful theorem is found, read its proof too and
  extract adaptable techniques. When considering an external theorem, expand its
  definitions using the paper's own context and check it is actually applicable.

> Note on skills: a skill describes the mathematical procedure and what kind of
> finding it produces. Record findings and facts per **this** contract (global
> memory `gm_add`, fact graph `fact_submit`). Where a skill still names older Danus
> memory channels / `verify_proof_service`, follow this prompt's data model — the
> skills are being reconciled to it.

## What the worker produces

The **fact graph is the deliverable** — the target theorem established as a fact
standing on its verified predecessors. There is no separate `blueprint_verified.md`
artifact: a "full proof" is the target fact plus its predecessor DAG; the paper is
assembled from that graph downstream. Partial progress lives as findings in global
memory; verified building blocks live as facts.

<!-- END SOURCE doc-4b3a94b64d83 -->

---

<a id="doc-44be71b7ba0f"></a>

## 原文导签：Danus core data model — local memory · global memory · fact graph

来源：`work/documentation_memory_20260917/harness_sources/danus/danus/core/DATA_MODEL.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/danus/danus/core/DATA_MODEL.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-44be71b7ba0f -->
# Danus core data model — local memory · global memory · fact graph

This is the **authoritative, detailed spec** of the three core data structures of
the Danus system, their relationships, and the logic for using them.
Skills, prompts, and the orchestration layer are written against this document —
read it before touching any of them.

> **The model, by scope.** Danus keeps one private per-worker running log and
> splits shared knowledge by **scope**:
>
> | name | scope | who reads it |
> | --- | --- | --- |
> | **local memory** | per-worker private | only that worker |
> | **global memory** | project-shared — the *categorized findings* | all workers + main agent |
> | **fact graph** | project-shared, verified | all workers + main agent |
>
> Strong **categorization** (typed channels) and the append-only JSONL + BM25
> mechanism live on the **global memory** layer (shared), because sharing typed
> findings — including dead ends — is the whole point. Per-worker `local memory`
> keeps only the rough "what I did" log. `fact_graph` is a content-addressed
> verified DAG.

---

## 0. The three tiers at a glance

```
                scope            structure          unit                 truth?
local memory    per-worker       loose / rough      "what I did" log     no  (private scratch)
global memory   project-shared   strongly typed     a CLAIM + evidence   no  (shared findings, incl. dead ends)
fact graph      project-shared   fully structured   a VERIFIED fact      YES (only correctness source)
```

A finding flows **left → right**, getting more structured and more trusted:

```
local memory  ──(worker auto-publishes a formed claim)──▶  global memory
global memory ──(verifiable=true → send to verifier → fix until correct)──▶  fact graph
```

**The load-bearing invariant:** a proof may only build on `fact graph` entries
(cite a `fact_id`). `global memory` is for **awareness** — dedup, ideas,
knowing which paths died — and is **never** a correctness source, even though it
holds claims with evidence. Only the verifier promotes a claim into the fact
graph. This is the same discipline as "peer-consult informs direction, the
verifier decides correctness."

---

## 1. local memory (per-worker private, rough)

**Purpose.** Each worker's private running log of what it thought and did, so it
can recall its own context later in the run. Deliberately rough — no schema
police. Other workers never read it.

**Scope.** Per-worker. Rooted at the worker's own directory.

**Storage.** `<worker_dir>/local_memory/<channel>.jsonl`, append-only JSONL,
BM25 recall. Default channels (small, can grow):

- `notes` — free-form thoughts, partial reasoning, things-to-try.
- `events` — a log of actions taken (searches run, skills invoked, a claim
  published to global memory, a fact submitted). Auto-logged + explicit.

**Entry envelope.**

```json
{ "timestamp_utc": "...", "channel": "notes", "record": { ...any JSON... } }
```

`record` is free-form — that is intentional; local memory holds "various
unformed content."

**Operations.** `append(channel, record)`, `search(query, channels, limit)`
(BM25), `read(channel)`.

**When a worker writes it.** Continuously, as it works — raw reasoning into
`notes`, actions into `events`. The moment a thought becomes a *formed claim*
(a conclusion, an example, a counterexample, a dead end, a direction), the
worker **auto-publishes** it to **global memory** instead (see §2). Local memory
keeps only the process, not the shareable findings.

---

## 2. global memory (project-shared, strongly typed findings)

**Purpose.** The shared pool of *findings* — every formed claim plus its
supporting evidence, **including dead ends** — so workers learn from each other
(don't re-walk a dead path, build on each other's ideas) and so verifiable
claims get driven toward the fact graph. Failures are shared, not locked in each
worker's private memory where only successes surface.

**Scope.** Project-shared. Rooted at the project directory; all workers and the
main agent read/write it.

**Storage.** `<project_dir>/global_memory/<kind>.jsonl` — **one append-only
JSONL file per kind** (one file per channel, shared) + BM25.
Status transitions are append-only too (see "status").

**Entry schema.**

Unlike local memory (§1), a global-memory entry is **flat** — every field is at
the top level; there is no `record` envelope (that nesting is local memory's, not
this one's).

```json
{
  "id":         "<stable id>",
  "timestamp_utc": "...",
  "author":     "<worker id | main_agent>",   // shared store ⇒ attributed
  "kind":       "counterexample",              // the strong category (§2.1)
  "claim":      "...",                          // what is asserted / explored
  "evidence":   "...",                          // verifiable: an explicit proof/construction; judgment: the reasoning behind it
  "verifiable": true,                           // ★ objectively checkable, or a judgment?
  "status":     "unverified",                   // lifecycle, §2.2
  "fact_id":    null,                            // back-link once promoted
  "links":      { "subgoal": "...", "predecessors": ["<id|fact_id>", "..."] },
  "glossary":   { }                              // symbol → definition introduced with this finding
  // …plus any kind-specific free-form fields (**extra) — e.g. a verification
  // entry's verdict/fact_id/write_error, or a master_guidance entry's
  // input_tokens/cost_usd — also flattened at the top level, NOT inside a record.
}
```

### 2.1 Kinds (categorization)

| kind | verifiable (default) | author | what goes in |
| --- | --- | --- | --- |
| `conclusion` | true | worker | a derived consequence of the statement (needs justification/proof as evidence) |
| `example` | true | worker | a (toy) example satisfying assumptions+conclusion; the construction is the evidence |
| `counterexample` | true | worker | a construction refuting a claim; the construction is the evidence |
| `proof_attempt` | true (when a sub-result is proved) | worker | an attempt on a subgoal; if a self-contained sub-result is proved, that is a verifiable claim |
| `plan` | false | worker | a subgoal decomposition / strategy (a judgment, not objectively checkable) |
| `dead_end` | usually false | worker | why a path failed; if killed by a counterexample it can be verifiable |
| `direction` | false | worker | "worth exploring X" — an unverifiable judgment |
| `obstacle` | false | worker | "X seems to block this route" — an unverifiable judgment |
| `master_guidance` | false | **main agent** | the periodic high-intelligence strategic steer the main agent reasons out itself (optionally via exploratory codex subagents): critical decomposition, direction judgment, core thinking. Authoritative — workers heed it (but it is still not a correctness source). |
| `verification` | false | the worker's `fact_submit` (auto) | a trace of a verification outcome: the verdict, plus `fact_id` (on accept) or `repair_hints` (on reject). Logged automatically by `fact_submit` so the verifier's feedback is not lost — the verifier itself stays stateless. Siblings read these to learn from rejections. |
| `elaboration` | false | **main agent** | the periodic, high-signal-to-noise progress synthesis the main agent writes before deciding the next steer: mathematical verdict, closed/obsolete routes, interface contracts, dangerous heuristics, missing bridge lemmas (§2.4). It is the synthesis the main agent reasons over to produce `master_guidance`. Same cadence. |

Process-only categories (`branch_states`, `events`) stay in
**local memory**, not here — they are not findings. `verification_reports` is
not a kind: a verifier verdict attaches to an entry's `status` (§2.2).

**Scope rule that controls noise.** Every global-memory entry has a clear
scope: it is *a claim plus its evidence*. Objectively-checkable kinds
(`conclusion`/`example`/`counterexample`/`proof_attempt`) **must** carry an
explicit proof or construction as `evidence`. Unverifiable judgments
(`plan`/`direction`/`obstacle`/`master_guidance`) **must** set `verifiable:false`
so readers know they are opinions to test, not established results. This scoping
— not a politeness rule — is what keeps the shared store from becoming a dump.

**Writing guideline — unified definitions.** When you write a finding, **define
your symbols and reuse the project's terminology consistently** — check the
project glossary before naming something, and use the same symbol for the same
object as everyone else. A finding may carry an optional `glossary`
(symbol → definition). This is the same self-containment discipline the fact
graph enforces (§3); applying it early keeps global memory readable and lets a
verified finding carry cleanly into a fact without a terminology rewrite.

### 2.2 Status lifecycle

`status` is updated by appending a status event (append-only; current status =
the latest event for that `id`):

- verifiable entries: `unverified → verifying → verified (sets fact_id) | refuted`
- judgment entries: `open → supported | challenged`

A worker is **encouraged to keep pushing** `verifiable=true` entries through the
verifier: send to verify, on `wrong` revise the evidence, re-verify, until
correct — then it is promoted to a fact (§3, §4). The verify-and-repair loop
operates per-claim on the shared store.

### 2.3 master_guidance — the strategic channel

The main agent operates and schedules N parallel workers. On a fixed cadence
(e.g. hourly, or whenever all workers finish a round) it reasons out the most
critical decomposition, direction judgment, and core thinking itself —
optionally spawning exploratory codex subagents (high intelligence, expensive ⇒
periodic, not per-round). It records the result as a `master_guidance` entry.
Workers read `master_guidance` and follow it as authoritative steering. (This
concentrates the expensive intelligence at the strategic level, shrinking
per-worker peer consults.)

**Operations.** `append(kind, claim, evidence, verifiable, author, links, **extra) -> id`,
`set_status(id, status, fact_id=None)`, `read(kind)` (entries, status folded),
`search(query, kinds, limit)` (BM25).

### 2.4 elaboration — the synthesis channel (input to the strategic steer)

On the same cadence as the strategic steer (§2.3), the main agent first writes
an **elaboration**: a single high-signal-to-noise synthesis of the project's
current state, read **only from the shared stores** — global memory (findings,
dead ends, recent verifications) and the fact graph (verified facts, the DAG,
proved vs. open) — **never** from a worker's private local memory (a layer
boundary). It follows a fixed template (mathematical verdict → closed/obsolete
routes → interface contracts → dangerous heuristics → missing bridge lemmas) and
a strict honesty discipline (goal stays fixed, cite `fact_id`s only, no numerical
distance estimates, no process telemetry). The *how* lives in the **`elaboration`
main-agent skill**, not in code.

The elaboration is recorded as an `elaboration` entry (`claim` = the one-line
verdict, `evidence` = the full templated body, `links` = cited `fact_id`s); the
main agent then reasons over it — optionally via exploratory codex subagents — to
produce the next `master_guidance` (§2.3). Instead of peer workers reviewing each
other, the main agent distills the shared state and reasons over it at high
intelligence. Operationally it is also what the main agent draws on to keep the
human informed.

---

## 3. fact graph (project-shared, verified)

> **Terminology.** An **"ugly-proof"** — an "ugly-but-rigorous", self-contained,
> machine-checkable proof record — is exactly **a fact in this fact graph**, same
> thing. If the operator says "ugly-proof", they mean a fact node. ("Ugly" is the
> deliberate contrast with the *polished* arXiv paper, which a separate pipeline
> produces from the fact-graph DAG.)

**Purpose.** The single correctness source: a content-addressed DAG of
verifier-accepted facts that compose into a paper and support cascade revocation.
The essence is deliberately minimal — a readable node, a content-addressed id, a
predecessor DAG, cascade revoke — with no status, verifier_outcome, claim_summary,
see_also, or drafts/ on the node.

**Scope.** Project-shared, rooted at the project directory.

**Storage.** `<project_dir>/fact_graph/facts/<fact_id>.md` — one readable
markdown file per fact (file name = the bare-hex id) + `revocation_log.jsonl` +
`_revoked/<ts>/`. No `glossary.json`, no `drafts/` (rejected claims stay in
global memory as `refuted`).

**Fact node — 6 frontmatter fields + markdown body:**

```yaml
---
fact_id: 0056a49384644046          # content-addressed (bare hex)
problem_id: KMMP
author: KMMP_pro3                  # which worker produced it
predecessors: [7b6dd3df2e88fff5]   # bare-hex ids this depends on (the DAG)
glossary_introduces:               # symbols this fact defines (kept — see below)
  X: a complex manifold
  K_F: the canonical class of the foliation F
external_refs: [{"key": "HL26", "authors": ["Han", "Liu"], "title": "...", "arxiv": "2603.03817", "year": 2026, "cited_for": "Theorem 1.2"}]
---

## statement
<what was proved — self-contained: every symbol is defined here, in a cited
 predecessor's glossary, in the project glossary, or in the global glossary>

## proof
<the argument (markdown)>

## intuition          # optional
<one-liner>
```

- **`glossary_introduces` is KEPT (essential).** Without it the fact graph
  becomes unreadable — a fact could use a symbol nobody ever defined. Each fact
  records the symbols it introduces (symbol → definition); the project glossary
  `glossary.json` accumulates them. A **glossary-coverage check** (`fact submit`)
  flags any interesting symbol used in the body that is not defined anywhere
  **available**, where availability is the union of four layers (precedence
  low→high, a higher layer shadows a lower one): **global glossary** →
  **project glossary** → *cited predecessors'* `glossary_introduces` → *this
  fact's* `glossary_introduces`. The **global glossary**
  (`danus/core/glossary_global.json`, repo-wide, shared by **all** projects) holds
  universal notation — Z, Q, R, C, floor/ceil, gcd/lcm, intervals, the Greek
  parameter names, … — so a fact need not redefine `epsilon` or `Z+` every time;
  only project-specific symbols go in the lower layers. (Heuristic, advisory; the
  verifier is the backstop. The *other* proof-lint rules — handwave,
  chart-position refs — are **prose**, not code.)
- **`external_refs` is structured bibliography for cited external results** (a
  list of `{key, authors, title, arxiv, year, venue, doi, cited_for}` dicts;
  serialized as a one-line JSON flow-array; `[]` / absent for older facts). The
  worker fills it at `fact_submit` (grounded via `search_arxiv_theorems`); the
  paper pipeline's **reference auditor** corrects it post-hoc. It is **mutable
  metadata, NOT part of the `fact_id`** — hashing it would change the id (and break
  the DAG) on every audit, and would perturb every pre-existing fact's id. The
  cited keys themselves already live in `proof`, which *is* hashed. Read it via
  `external_refs(fact_id)`; rewrite it via `set_external_refs(fact_id, refs)`
  (touches only the metadata line, never the body or id).
- **`fact_id` is content-addressed:**
  `SHA256(json{problem_id, sorted(predecessors), sorted(glossary_introduces), normalized(statement), normalized(proof)})[:16]`.
  Same content ⇒ same id ⇒ natural dedup. Nodes are immutable
  (a changed statement/proof/glossary ⇒ a different id ⇒ a new file). `external_refs`
  is deliberately excluded (mutable metadata, above).
- **DAG:** `predecessors` are the bare-hex fact ids this fact depends on
  (its "depends-on"). References use bare hex everywhere — one convention.
- **Revocation:** revoking a fact moves it (and every descendant) to `_revoked/`,
  logs to `revocation_log.jsonl`; `add` refuses any predecessor already revoked.

**Deliberately not on the node (and where it lives instead):** `status` (a fact in
`facts/` is verified by definition) · `verifier_outcome` (redundant) ·
`claim_summary` (derive for an index when needed) · `see_also` · `drafts/`
(→ global memory `refuted`) · the text-hygiene lint rules — handwave,
chart-position refs, quantifier ranges (→ **prose** in the worker/verifier
prompts) · a persisted `verified_facts.jsonl` board (→ the **derived index** below: a
BM25 view computed on demand from `facts/`, never a stored second truth, so no
double-write drift). **Kept:** the glossary (data + the coverage check) — it is
what makes the graph readable.

**Derived fact index (`search`).** `search(query, limit)` rebuilds a BM25 view
over the fact bodies (statement + proof + glossary) **on demand** from `facts/*.md`
and returns the top `{fact_id, score, statement}`. It is the cross-worker recall
the LLM can't do by reading, serving **novelty** ("does a fact like this already
exist? — don't re-prove it") and **citation lookup** ("which verified facts bear
on my subgoal?"). Exposed as the `fact_search` MCP tool (worker + main). It is a
*read view*; the fact files stay the single source of truth.

**Operations (code = data-structure I/O only).** `compute_fact_id(...)`,
`add(problem_id, author, statement, proof, predecessors=[], intuition="",
external_refs=[]) -> fact_id`, `get_raw(fact_id)`, `list()`, `search(query, limit)`,
`predecessors(fact_id)`, `descendants(fact_id)`, `external_refs(fact_id)`,
`set_external_refs(fact_id, refs)`, `revoke(fact_id, reason)`.

---

## 4. Relationships & data flow (how they connect)

```
            ┌─────────────── per worker (private) ───────────────┐
 worker  →  │ local memory: notes / events  (rough recall log)    │
            └───────────────────────┬────────────────────────────┘
                    auto-publish a formed claim
            ┌───────────────────────▼──────────── project-shared ─┐
 all     →  │ global memory: <kind>.jsonl                         │
 workers    │   conclusion/example/counterexample/proof_attempt   │
 + main     │   plan/dead_end/direction/obstacle/master_guidance  │
 agent      │   each = claim + evidence + verifiable + status     │
            └───────────────────────┬────────────────────────────┘
                 verifiable=true → verify → repair → correct
            ┌───────────────────────▼──────────── project-shared ─┐
            │ fact graph: facts/<fact_id>.md (content-addressed)  │
            │   ★ the only thing a proof may build on (cite id)   │
            │   predecessors = DAG · cascade revoke               │
            └─────────────────────────────────────────────────────┘
```

**Invariants (load-bearing):**

1. **Correctness source = fact graph only.** Proofs cite `fact_id`. Global
   memory (even verifiable-but-unverified claims) is awareness, never a brick.
2. **Promotion is verifier-gated.** A claim enters the fact graph only by passing
   the verifier (§4 promotion).
3. **Append-only** everywhere (local + global + revocation log); status changes
   are appended events, not mutations. Fact files are immutable once written
   (a changed statement/proof ⇒ a different `fact_id`).
4. **Isolation of local memory.** Workers never read each other's local memory;
   the only cross-worker channels are global memory (awareness) and fact graph
   (truth).
5. **Content addressing.** `fact_id` is a pure function of content ⇒ dedup,
   stable references, cascade revocation.

**Promotion (a prose behavior, not a function).** When a `verifiable=true`
global-memory finding passes the verifier, the agent (per its prompt) writes the
fact with `FactGraph.add(statement=claim, proof=evidence,
predecessors=links.predecessors)` and back-links the finding with
`GlobalMemory.set_status(id, "verified", fact_id)`. There is deliberately **no
`promote()` function** — the decision to verify and the verify call are the
agent's; the library only offers the two data-structure writes.

### Code vs prose (the boundary)

| code (this library — touches the fixed JSONL / fact-graph files) | prose (prompts/skills — agent behavior) |
| --- | --- |
| local/global memory: append / read / search (BM25) | when to publish local→global; which `kind`/`verifiable` |
| fact node: serialize/parse, `compute_fact_id`, add/get/list, predecessors/descendants, cascade revoke | when to send to the verifier; the repair loop; when to promote |
| evidence-required-for-verifiable check; revoked-predecessor refusal | "global memory is awareness, never a brick — cite `fact_id`" |
| | "facts must be self-contained; no handwave / chart-position refs" |

Keep it that way: do not add orchestration code. If something is a *decision*, it
is prose.

---

## 5. Usage logic (typical round)

1. **Main agent**, periodically: reason over the shared stores itself (optionally
   via exploratory codex subagents) → append a `master_guidance` entry to global
   memory.
2. **Worker**, each round:
   - read `master_guidance` + recent global memory (others' findings, dead ends)
     + relevant fact graph entries; recall own `local memory`.
   - reason; log raw thoughts/actions to `local memory`.
   - when a finding forms, auto-publish it to `global memory` with the right
     `kind` + `verifiable` + evidence.
   - push `verifiable=true` findings through the verifier; on accept, **promote**
     to the fact graph and build further work by citing the new `fact_id`.
   - record dead ends as `dead_end`/`obstacle` so siblings skip them.

This document is the contract those behaviors are written against. The Python
implementation lives next to it in `danus/core/` (`local_memory.py`,
`global_memory.py`, `factgraph.py`, `schema.py`, `bm25.py`); see `README.md` for
the API and usage instructions.

<!-- END SOURCE doc-44be71b7ba0f -->

---

<a id="doc-8d61925b3c71"></a>

## 原文导签：Danus — Security & Trust Model

来源：`work/documentation_memory_20260917/harness_sources/danus/docs/security-and-trust.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/danus/docs/security-and-trust.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-8d61925b3c71 -->
# Danus — Security & Trust Model

Read this **before you rely on a Danus result** and before you deploy Danus on a
shared or networked host. It states, plainly, what you are trusting, how permission
is enforced, and where a human should stay in the loop.

## 1. The one thing to understand first: the verifier is an LLM, not a formal prover

Danus's entire notion of truth rests on the **verifier**: a result becomes a fact
**if and only if** the verifier returns a `correct` verdict. That verifier is a
**cold-start `codex` (LLM) judge**, not a formal proof assistant (no Lean/Coq/…),
and by default **there is no human in the loop.**

Consequences you must internalize:

- A `correct` verdict is a **strong LLM judgment**, not a machine-checked proof. It
  is far better than an unchecked draft, but it can be wrong.
- The verdict rule (`correct` ⟺ no critical errors **and** no gaps) is produced by
  the verifier agent and returned **verbatim**; the service does **not** re-derive
  it. Trust flows from the verifier prompt + skills being correct.
- For a **high-stakes** result (a headline theorem you intend to publish or act on),
  **have a qualified human review it.** The write-paper pipeline re-checks the whole
  paper as written through a dedicated paper-math verifier, which raises confidence —
  but it is still LLM verification, not a formal certificate.

This is the system's single most important trust assumption. It is deliberate (the
whole point is to scale proof search beyond what a formal assistant can express
today), but it is on **you** to decide how much a `correct` verdict is worth for a
given result.

## 2. Permission is enforced by construction, not by prompts

Danus does not rely on agents "behaving". Every read/write to the truth stores goes
through the **gateway** (a role-gated MCP server), and **what a role can do is
exactly which tools it can even see** — ungated tools are physically absent from an
agent's tool surface, not merely discouraged.

The role table (`danus/gateway/roles.py`):

| role | tools it can see |
|---|---|
| **worker** | `gm_add`, `gm_search`, `fact_submit`, `fact_search`, `search_arxiv_theorems` |
| **main** (the orchestrator) | `gm_add`, `gm_search`, `fact_search`, `fact_revoke`, `search_arxiv_theorems` — **no `fact_submit`** |
| **verifier** | `search_arxiv_theorems` **only** (read-only) |

Load-bearing separations:

- **The orchestrator can never fabricate a fact.** `main` has no `fact_submit`;
  only a `worker` can submit, and only the verifier can accept.
- **The verifier is read-only.** It can look up literature; it writes nothing to
  the truth stores.
- **Fail-closed.** An unknown, mis-typed, or *unset* role falls back to the
  most-restrictive (verifier) set, so a misconfiguration cannot grant write
  access. The full dev set requires the explicit `DANUS_ROLE=all`.

## 3. The write-gate

The single path a fact enters truth is a worker's `fact_submit`, which is a
state machine, not a suggestion:

1. call the verify service with the statement + proof;
2. **write the fact iff the verdict is `correct`** — the gate is this one code path;
3. **always** trace the verdict to global memory (accept, reject, or write-failed),
   so the verifier can stay stateless and no verdict is lost.

If the verify service is unreachable, `fact_submit` returns a clean error and
writes nothing — nothing is silently accepted.

## 4. The verifier runs with the sandbox bypassed — trust its home and isolate the host

The worker and verifier `codex` sessions are launched with
`--dangerously-bypass-approvals-and-sandbox`. This is required for autonomous
operation, and it means Danus's host-level safety rests on two assumptions you must
uphold:

- **The agent home is trusted.** The verifier runs inside a fixed `AGENT_HOME`
  (its contract + skills). Treat that directory — and the worker/verifier prompts and
  skills — as **trusted code**: a malicious or tampered prompt/skill could act with
  the privileges of the process.
- **The host is isolated / disposable.** Run Danus on a host you are willing to let
  autonomous agents operate on (a dedicated VM/container/pod), not your workstation
  with access to unrelated data.

## 5. Network exposure: loopback by default

The two services bind **loopback only** by default:

- **verify** on `127.0.0.1:8091`,
- **dashboard** on `127.0.0.1:8099`.

Nothing is exposed to the network out of the box. To view the dashboard remotely,
use an SSH port-forward rather than binding a public interface. (`VERIFY_HOST` /
the dashboard `--host` can change the bind, but the safe default is loopback — do
not expose these to an untrusted network.)

## 6. Secrets: bring your own key, never committed

- All credentials (codex backend key, LaTeX-git token) live **only** in
  gitignored `config/*.env` files. The tree ships `*.env.example` placeholders only —
  **no working key is committed.**
- The codex backend key is **read at run time from an environment variable**; it is
  **not** written into any config file that Danus generates (e.g. the codex
  `config.toml` references the env var name, not the value).
- Before any commit, confirm `git status` shows no `config/*.env` and no `runtime/`.

## 7. The deterministic pre-checks (a safety net, and a caveat)

Before the LLM verifier runs, the verify service applies deterministic pre-checks
that **can only reject more**, never accept more: emptiness/vacuousness checks and a
few hard prohibitions (citing the problem statement as a source, unproven
conditional premises, vague "well-known" gestures without a citation).

**Caveat:** these prohibition patterns are **tuned to specific past incidents**
and are therefore domain-specific — the single most project-flavored part of the
verifier stack. They are safe (additive); keep, generalize, or disable them to fit
your domain.

## 8. What to trust, and what to double-check

- **Trust the shape:** the permission table, the write-gate, content-addressing,
  cascade revocation, and "no fact without a `correct` verdict" are enforced in code
  and are the well-tested part of the system.
- **Double-check the verdicts** on results that matter: a `correct` verdict is an
  LLM judgment. For a publishable headline result, add a human review; the
  write-paper verify gate helps but does not replace it.
- **Treat the worker/verifier prompts + skills as trusted code**, and keep the host
  isolated.

<!-- END SOURCE doc-8d61925b3c71 -->

---

<a id="doc-13b6f50866e4"></a>

## 原文导签：Equational theories project

来源：`work/documentation_memory_20260917/harness_sources/equational_theories.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/equational_theories.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-13b6f50866e4 -->
# Equational theories project

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-lightblue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![Website](https://img.shields.io/badge/Website-Ready-green)](https://teorth.github.io/equational_theories/)
[![Documentation](https://img.shields.io/badge/Documentation-Passing-green)](https://teorth.github.io/equational_theories/docs/)
[![Blueprint](https://img.shields.io/badge/Blueprint-WIP-blue)](https://teorth.github.io/equational_theories/blueprint/)
[![Progress](https://teorth.github.io/equational_theories/dashboard/progress_badge.svg)](https://teorth.github.io/equational_theories/dashboard/)
[![Paper](https://img.shields.io/badge/Paper-WIP-blue)](https://teorth.github.io/equational_theories/paper.pdf)
[![Zulip Channel](https://img.shields.io/badge/Zulip_Channel-Join-blue)](https://leanprover.zulipchat.com/#narrow/stream/458659-Equational)

![Hasse diagram of selected equations](https://github.com/teorth/equational_theories/blob/main/images/subgraph.png?raw=true)

The purpose of this project, launched on Sep 25, 2024, is to explore the space of equational theories of [magmas](https://en.wikipedia.org/wiki/Magma_(algebra)), ordered by implication. To begin with we shall focus only on theories of a single equation, and specifically on the 4694 equational laws
involving at most four magma operations, up to symmetry and relabeling (here is the list [in Lean](https://github.com/teorth/equational_theories/tree/main/equational_theories/Equations/All.lean) and in [plain text](https://github.com/teorth/equational_theories/tree/main/data/equations.txt)).  This creates 4694*(4694-1) = 22,028,942 implications that need to be proven or disproven, creating both "implications" and "anti-implications".

We will accumulate both "proven" and "conjectured" implications and anti-implications: proven assertions will be verified in the proof assistant language [Lean](https://www.lean-lang.org/), and "conjectured" assertions represent all claims (either human-generated or computer-generated) that have not yet been verified in Lean.  The current status of the project can be found on the [dashboard](https://teorth.github.io/equational_theories/dashboard/).

Some selected equations of interest are listed [here](https://github.com/teorth/equational_theories/tree/main/equational_theories/Equations/Basic.lean) (in Lean form) and [here](https://teorth.github.io/equational_theories/blueprint/subgraph-eq.html) (in a human readable blueprint).  Examples include
- [Equation 1](https://teorth.github.io/equational_theories/implications/?1): `x = x`.  The trivial law.
- [Equation 2](https://teorth.github.io/equational_theories/implications/?2): `x = y`.  The singleton law.
- [Equation 43](https://teorth.github.io/equational_theories/implications/?43): `x ◇ y = y ◇ x`.  The commutative law.
- [Equation 46](https://teorth.github.io/equational_theories/implications/?46): `x ◇ y = z ◇ w`.  The constant law.
- [Equation 4512](https://teorth.github.io/equational_theories/implications/?4512): `x ◇ (y ◇ z) = (x ◇ y) ◇ z`.  The associative law.

[Here is a tour](https://github.com/teorth/equational_theories/wiki/Tour-of-selected-equations) of several selected equations, including the ones above.

Current statistics and data files, updated automatically:
- [dashboard](https://teorth.github.io/equational_theories/dashboard/)

Current visualizations, updated automatically:
- [Equation Explorer](https://teorth.github.io/equational_theories/implications) is a tool for exploring the graph of equation implications.
- [Finite Magma Explorer](https://teorth.github.io/equational_theories/fme) is a tool for exploring finite magmas and the equations they satisfy.
- [Graphiti](https://teorth.github.io/equational_theories/graphiti) is a tool for visualizing the implication graph.

For guidelines on how to contribute, see the [CONTRIBUTING.md](https://github.com/teorth/equational_theories/tree/main/CONTRIBUTING.md) file.  Participants are requested to abide by [our code of conduct](https://github.com/teorth/equational_theories/tree/main/CODE_OF_CONDUCT.md).

## Building the project

To build this project after [installing Lean](https://www.lean-lang.org/lean-get-started) and cloning this repository, follow these steps:

```
% cd equational_theories/
% lake exe cache get
% lake build
```

## Links

- [Main web page](https://teorth.github.io/equational_theories/)
    - [Blueprint](https://teorth.github.io/equational_theories/blueprint/)
    - [Documentation](https://teorth.github.io/equational_theories/docs/)
    - [The Lean Zulip stream for the project](https://leanprover.zulipchat.com/#narrow/stream/458659-Equational/)
    - [Instructions on how to contribute](https://github.com/teorth/equational_theories/tree/main/CONTRIBUTING.md)
    - [Code of conduct](https://github.com/teorth/equational_theories/tree/main/CODE_OF_CONDUCT.md)
    - [Wiki](https://github.com/teorth/equational_theories/wiki)
    - [Older progress](https://github.com/teorth/equational_theories/tree/main/docs/OLD_PROGRESS.md)
- [A blog post describing the project.](https://terrytao.wordpress.com/2024/09/25/a-pilot-project-in-universal-algebra-to-explore-new-ways-to-collaborate-and-use-machine-assistance/), Sep 25, 2024.
    - [The equational theories project: a brief tour](https://terrytao.wordpress.com/2024/10/12/the-equational-theories-project-a-brief-tour/), Oct 12, 2024 - a followup to the previous post.
- [Initial discussion on Zulip](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proposing.20a.20universal.20algebra.20exploration.20using.20Lean/near/472914164), Sep 26, 2024.
- [Initial discussion on Mastodon](https://mathstodon.xyz/@tao/110736805384878353), Jul 18, 2023.
    - [Followup discussion on Mastodon](https://mathstodon.xyz/deck/@tao/113201989529992957), Sep 25, 2024.
- [The MathOverflow post that inspired the project](https://mathoverflow.net/questions/450930/is-there-an-identity-between-the-associative-identity-and-the-constant-identity), Jul 17, 2023.
    - [A related MathOverflow post](https://mathoverflow.net/questions/450890/is-there-an-identity-between-the-commutative-identity-and-the-constant-identity), Jul 16, 2023.
- [Data](https://github.com/teorth/equational_theories/tree/main/data)
    - [Text list of equations](https://github.com/teorth/equational_theories/tree/main/data/equations.txt).  [Larger list with equations of up to five operations](https://github.com/teorth/equational_theories/blob/main/data/eq_size5.txt)
    - [List of duals of equations](https://github.com/teorth/equational_theories/tree/main/data/dual_equations.md) ([JSON](https://github.com/teorth/equational_theories/blob/main/data/duals.json))
    - [The smallest magma satisfying a given equation (up to N=5)](https://github.com/teorth/equational_theories/blob/main/data/smallest_magma.txt), if it exists (and [the magmas themselves](https://github.com/teorth/equational_theories/blob/main/data/smallest_magma_examples.txt))
    - To download the current state of the implication graph, see [this thread](https://leanprover.zulipchat.com/#narrow/stream/458659-Equational/topic/Database.20of.20implications/near/476969963).
- [Scripts](https://github.com/teorth/equational_theories/tree/main/scripts)
    - Shell
        - [`run_before_push`](https://github.com/teorth/equational_theories/tree/main/scripts/run_before_push.sh) – performs some of the CI checks, suitable for running just before pushing a new PR
    - Lean
        - [`extract_implications`](https://github.com/teorth/equational_theories/tree/main/scripts/extract_implications.lean) – extracts implications from one or more Lean files. This outputs the "ground truth" of implication data, for use by other scripts
    - Python
        - [`explore_magma`](https://github.com/teorth/equational_theories/tree/main/scripts/explore_magma.py) – test a given magma table against all or a subset of the equations in [`Equations/All.lean`](https://github.com/teorth/equational_theories/tree/main/equational_theories/Equations/All.lean)
        - [`find_dual`](https://github.com/teorth/equational_theories/tree/main/scripts/find_dual.py) – finds the dual of an equation
        - [`find_equation_id`](https://github.com/teorth/equational_theories/tree/main/scripts/find_equation_id.py) – finds the equation number of an equation string
        - [`find_powerful_theorems.py`](https://github.com/teorth/equational_theories/tree/main/scripts/find_powerful_theorems.py) – finds theorems that, if proved, would imply many others
        - [`generate_eqs_list`](https://github.com/teorth/equational_theories/tree/main/scripts/generate_eqs_list.py) – generates a list of equations
        - [`generate_image`](https://github.com/teorth/equational_theories/tree/main/scripts/generate_image.py) – generates an image of implications
        - [`generate_most_wanted_list`](https://github.com/teorth/equational_theories/tree/main/scripts/generate_most_wanted_list.py) – generates the "most wanted" implications
        - [`generate_z3_counterexample`](https://github.com/teorth/equational_theories/tree/main/scripts/generate_z3_counterexample.py) – given an implication statement between two equations, calls Z3 to try to generate a counterexample
        - [`process_implications`](https://github.com/teorth/equational_theories/tree/main/scripts/process_implications.py) – processes implications from one or more Lean files
    - Ruby
        - [`generate_graphviz_graph`](https://github.com/teorth/equational_theories/tree/main/scripts/generate_graphviz_graph.rb) – creates a graphviz graph
        - [`transitive_closure`](https://github.com/teorth/equational_theories/tree/main/scripts/transitive_closure.rb) – computes the transitive closure of a set of implications
        - [`transitive_reduction`](https://github.com/teorth/equational_theories/tree/main/scripts/transitive_reduction.rb) – finds a transitive reduction of a set of implications
        - [`graph`](https://github.com/teorth/equational_theories/tree/main/scripts/graph.rb) – graph library
- Automated provers for equational theories
    - [Prover9 and Mace4](https://www.cs.unm.edu/~mccune/prover9/)
        - [aa](https://github.com/gsfk/aa) – a project to use Prover9/Mace4 to brute force axioms for finite mathematical domains
    - [Vampire](https://en.wikipedia.org/wiki/Vampire_(theorem_prover))
    - [eprover](https://github.com/eprover/eprover)
    - [twee](https://nick8325.github.io/twee/)
    - [zipperposition](https://github.com/sneeuwballen/zipperposition)
    - [Z3](https://microsoft.github.io/z3guide/docs/logic/intro/)
    - [Knuckledragger](https://github.com/philzook58/knuckledragger)
    - A [blog post](https://www.philipzucker.com/tao_algebra/) by Philip Zucker testing many of the above provers on a [sample implication](https://teorth.github.io/equational_theories/blueprint/sect0003.html#387_implies_43) of this project.
    - ["Guided Equality Saturation"](https://dl.acm.org/doi/10.1145/3632900), Thomas Kœhler, Andrés Goens, Siddharth Bhat, Tobias Grosser, Phil Trinder, Michel Steuwer, Jan 5, 2024.
    - ["Rewrite Rule Inference Using Equality Saturation"](https://arxiv.org/abs/2108.10436), Chandrakana Nandi, Max Willsey, Amy Zhu, Yisu Remy Wang, Brett Saiki, Adam Anderson, Adriana Schulz, Dan Grossman, Zachary Tatlock, 23 Aug, 2021.
- Other tools
    - [egg - e-graphs good](https://egraphs-good.github.io/)
    - [MiniZinc](https://www.minizinc.org/) – high-level constraint modeling language
    - [nauty](https://pallini.di.uniroma1.it/) – graph automorphism tool
    - [KBCV](http://cl-informatik.uibk.ac.at/software/kbcv/) – Knuth-Bendix completion visualizer
    - [Instagraph](https://github.com/yoheinakajima/instagraph) – knowledge graph generator
    - [Logic Programming in F#](https://github.com/jack-pappas/fsharp-logic-examples/tree/master) – Code and Examples from John Harrison's "Handbook of Practical Logic and Automated Reasoning"
- Blog posts and media mentioning this project
    - "[We're Entering Uncharted Territory for Math"](https://www.theatlantic.com/technology/archive/2024/10/terence-tao-ai-interview/680153/), Matteo Wong, The Atlantic, Oct 4 2024.
    - "[On Math Platform](https://buildermath.substack.com/p/on-math-platform)", Michael Bucko, Substack von Michael, Oct 5 2024.

<!-- END SOURCE doc-13b6f50866e4 -->

---

<a id="doc-31a11275abee"></a>

## 原文导签：Analytic Number Theory Exponent Database

来源：`work/documentation_memory_20260917/harness_sources/expdb.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/expdb.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-31a11275abee -->




# Analytic Number Theory Exponent Database

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-lightblue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)

This is the repository for the Analytic Number Theory Exponent Database (ANTEDB), an ongoing project to systematically record known theorems for various exponents appearing in analytic number theory, as well as the relationships between them. Currently, the database is recording facts and conjectures on [exponent pairs](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), [exponential sum bounds](https://teorth.github.io/expdb/blueprint/beta-chapter.html), [zero-density](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html) and [moment bounds](https://teorth.github.io/expdb/blueprint/zeta-moment-chapter.html) for the Riemann zeta-function, [large value estimates](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), [additive energy bounds](https://teorth.github.io/expdb/blueprint/energy-chapter.html) and exponents related to [prime distributions](https://teorth.github.io/expdb/blueprint/primes-sec.html), amongst other results (the full list of exponents can be found [here](https://teorth.github.io/expdb/blueprint/intro-chapter.html)). The database aims to organise and record theorems and relationships as both [human-readable proofs](https://teorth.github.io/expdb/blueprint/intro-chapter.html) and as [executable python code](https://github.com/teorth/expdb/tree/main/blueprint/src/python). This builds upon the tables of exponent pairs and other related exponents that were collected in [this paper of Trudgian and Yang](https://arxiv.org/abs/2306.05599), and aims to fulfil the vision set out in [this blog post of Terence Tao](https://terrytao.wordpress.com/2024/07/07/a-computation-outsourced-discussion-of-zero-density-theorems-for-the-riemann-zeta-function/).

This is intended to be a living database; additional corrections, updates, and contributions to the ANTEDB are welcome.  Instructions for contributors can be [found here](https://github.com/teorth/expdb/blob/main/CONTRIBUTING.md).

- [Main web page](https://teorth.github.io/expdb/) for this project.
- [Web blueprint](https://teorth.github.io/expdb/blueprint/), containing a human-readable version of the database that is accessible online (see also the [introduction](https://teorth.github.io/expdb/blueprint/intro-chapter.html) here).
- [Dependency graph](https://teorth.github.io/expdb/blueprint/dep_graph_document.html) of the theorems in the database.
- [PDF form of blueprint](https://teorth.github.io/expdb/blueprint.pdf), a downloadable, human-readable version of the database stored as a single file.
- [Python code repository](https://github.com/teorth/expdb/tree/main/blueprint/src/python), containing a programmable version of this database and various optimization routines.

## External links
- T. Tao, T. Trudgian, A. Yang, "[New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach](https://arxiv.org/abs/2501.16779)": A paper describing the project, and several of the new results that already arose from it
- [A blog post](https://terrytao.wordpress.com/2025/01/28/new-exponent-pairs-zero-density-estimates-and-zero-additive-energy-estimates-a-systematic-approach/) by Terence Tao describing this paper and project
- [Mathbases](https://github.com/MathBases/MathBases) - A directory of math databases (including this one)

## Python database and proof automation
Each theorem and conjecture in the database is represented both in [natural language](https://teorth.github.io/expdb/blueprint/intro-chapter.html) and also in Python using the `Hypothesis` object. Each `Hypothesis` may either contain a reference to a result from the literature or depend on one or more other `Hypothesis` objects. The special predefined set `literature` contains all hypotheses of the first kind. For example, Ingham's 1940 [zero-density estimate](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html) for the Riemann zeta function
```math
N(\sigma, T) \ll T^{3(1-\sigma)/(2-\sigma) + o(1)}\qquad (1/2 \le \sigma \le 1, T \to \infty)
```
is represented as a `Hypothesis` in `literature`, and can be retrieved using
```
import literature

h = literature.find_hypothesis(hypothesis_type="Zero density estimate", keywords="Ingham")
print("Hypothesis name:", h)
print("Hypothesis data:", h.data)
print("Hypothesis reference:", h.reference.title(), h.reference.author(), h.reference.year())
print("Hypothesis dependencies:", h.dependencies)
```
Console output
```
Hypothesis name: Ingham (1940) zero density estimate
Hypothesis data: A(x) \leq 3/(2 - x) on [1/2,1)
Hypothesis reference: {On} the estimation of ${N}(\sigma, T)$ Ingham 1940
Hypothesis dependencies: set()
```
There are no dependencies because this `Hypothesis` object directly references the literature. Alternatively, theorems may also be represented as a `Hypothesis` that (recursively) depend on other hypotheses. The dependency structure is a tree whose root is the theorem and whose leaves are other known theorems (either trivial or proved in the literature). This tree also represents a proof of the `Hypothesis`. For instance, we may also derive Ingham's estimate using other hypotheses in the database, such as [large value estimates](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html). This returns a `Hypothesis` object containing the same result but also containing a proof of the estimate represented as a dependency tree.
```
import derived

h = prove_zero_density_ingham_1940_v2()
h.recursively_list_proofs()
```
Console output
```
- [Derived zero density estimate]  i.e. A(x) \leq \frac{3 \left(x - 1\right)}{x - 2} on [1/2,1). Follows from computed large value estimates and zeta large value estimates with τ0 = 2 - σ for σ \in [1/2,1)). Dependencies:
        - [Derived large value estimate]  i.e. (σ,τ,ρ) in Disjoint union of {['-4/3 + 2/3σ + τ >= 0', '2 - σ - τ >= 0', '3/4 - σ >= 0', 'ρ >= 0', '-1/2 + σ >= 0', '2 - 2σ - ρ >= 0'], ['2 - σ - τ >= 0', '3/4 - σ >= 0', '-1/2 + σ >= 0', '1 - 2σ + τ - ρ >= 0', '-2 + 2σ + ρ >= 0']}. Follows from 1 large value estimates. Dependencies:
                - [Classical large value estimate]  i.e. ρ <= max(2 - 2σ, 1 - 2σ + τ). Classical.
        - [Derived zeta large value estimate]  i.e. (σ,τ,ρ) in Disjoint union of {['8/3 - 4/3σ + τ >= 0', '-2 + τ >= 0']}. Follows from 1 zeta large value estimates. Dependencies:
                - [Classical large value estimate]  i.e. ρ <= max(2 - 2σ, 1 - 2σ + τ). Classical.
```
The database also implements a limited automated theorem prover using known relationships between certain exponents in analytic number theory. A number of functions can be used to automatically find proofs given a desired result and a set of assumed `Hypothesis`. For example, to find a proof of the [exponent pair](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html) $(\frac{4}{18}, \frac{11}{18}) = BABA^2B(0, 1)$, one can use
```
from exponent_pair import *

h = best_proof_of_exponent_pair(frac(4,18), frac(11,18))
h.recursively_list_proofs()
```
Console output
```
- [Derived exponent pair (2/9, 11/18)]  i.e. The exponent pair (2/9, 11/18). Follows from "Derived exponent pair (1/9, 13/18)" and taking the van der Corput B transform. Dependencies:
        - [van der Corput B transform]  i.e. van der Corput B transform. See [van der Corput, 1920].
        - [Derived exponent pair (1/9, 13/18)]  i.e. The exponent pair (1/9, 13/18). Follows from "Derived exponent pair (2/7, 4/7)" and taking the van der Corput A transform. Dependencies:
                - [van der Corput A transform]  i.e. van der Corput A transform. See [van der Corput, 1920].
                - [Derived exponent pair (2/7, 4/7)]  i.e. The exponent pair (2/7, 4/7). Follows from "Derived exponent pair (1/14, 11/14)" and taking the van der Corput B transform. Dependencies:
                        - [van der Corput B transform]  i.e. van der Corput B transform. See [van der Corput, 1920].
                        - [Derived exponent pair (1/14, 11/14)]  i.e. The exponent pair (1/14, 11/14). Follows from "Derived exponent pair (1/6, 2/3)" and taking the van der Corput A transform. Dependencies:
                                - [van der Corput A transform]  i.e. van der Corput A transform. See [van der Corput, 1920].
                                - [Derived exponent pair (1/6, 2/3)]  i.e. The exponent pair (1/6, 2/3). Follows from "Derived exponent pair (1/2, 1/2)" and taking the van der Corput A transform. Dependencies:
                                        - [van der Corput A transform]  i.e. van der Corput A transform. See [van der Corput, 1920].
                                        - [Derived exponent pair (1/2, 1/2)] i.e. The exponent pair (1/2, 1/2). Follows from "Trivial exponent pair (0, 1)" and taking the van der Corput B transform. Dependencies:
                                                - [van der Corput B transform]  i.e. van der Corput B transform. See [van der Corput, 1920].
                                                - [Trivial exponent pair (0, 1)]  i.e. The exponent pair (0, 1). Triangle inequality.
```

<!-- END SOURCE doc-31a11275abee -->

---

<a id="doc-7c0f19c0c944"></a>

## 原文导签：Contributing to Analytic Number Theory Exponent Database

来源：`work/documentation_memory_20260917/harness_sources/expdb_contributing.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/expdb_contributing.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-7c0f19c0c944 -->
# Contributing to Analytic Number Theory Exponent Database

Contributions to the ANTEDB are very welcome!  For short contributions (such as correcting a typo, or adding a reference or citation), one can simply email the correction to one of the maintainers of the ANTEDB ([Terence Tao](mailto:tao@math.ucla.edu), [Timothy Trudgian](mailto:timothy.trudgian@unsw.edu.au), or [Andrew Yang](mailto:andrew.yang1@unsw.edu.au)).  Alternatively, if one has familiarity with Github, one can submit a [Github Pull Request](https://github.com/teorth/expdb/pulls) (PR) to the [Github repository](https://github.com/teorth/expdb) with the suggested changes, or raise a [Github issue](https://github.com/teorth/expdb/issues).

Some specific information about types of contributions:

## Contributing a new reference to the blueprint

The references are stored at [references.bib](https://github.com/teorth/expdb/blob/main/blueprint/src/references.bib) in BibTeX format.  If possible, please try to maintain the alphabetical ordering of the references by first order.

## Contributing to a chapter of the blueprint

The chapters are stored in [this directory](https://github.com/teorth/expdb/tree/main/blueprint/src/chapter).  One can use standard LaTeX commands in these chapters.  One can also use the \uses{} macro to indicate which results depend on which other ones, for the purpose of filling out the dependency graph, though at the current stage of the project we are not making heavy use of this feature.

It is fine to suggest incomplete contributions, for instance stating a result with only a very sketchy proof or reference.  For an extremely incomplete contribution (e.g., a vague statement of a result without a reference, or proposing a new direction for the ANTEDB without contributing significant content), consider opening up a Github issue instead of a pull request.

If you propose to add a new chapter, or rearrange existing ones, one will also have to modify [content.tex](https://github.com/teorth/expdb/blob/main/blueprint/src/content.tex).  It is also recommended that each chapter be labeled, in order for the blueprint to be able to assign a stable name to the web page for that chapter.  It is recommended to see if [print.tex](https://github.com/teorth/expdb/blob/main/blueprint/src/print.tex) compiles before submitting the pull request. [Note: some LaTeX compilers may have difficulty with some of the packages.  `xelatex` generally works well though.]

Some examples of possible chapter topics to contribute can be found in the [introduction to the ANTEDB blueprint](https://teorth.github.io/expdb/blueprint/intro-chapter.html).  Please feel free to contact [Terence Tao](https://www.math.ucla.edu/~tao/) if you are interested in fleshing out one of these chapters, in order to coordinate with any other contributors.

For standalone chapter submissions that are not integrated with the rest of the blueprint, add the `\unintegrated` macro at the beginning of the chapter.  We will eventually plan to integrate the content more fully in to the ANTEDB, but are happy to take unintegrated submissions as a first step towards that.

## Contributing to Python code

Python code is stored in [this directory](https://github.com/teorth/expdb/tree/main/blueprint/src/python).  References to python code within the blueprint can be made using the (somewhat crude) `\code{}`, `\python{}`, `\literature{}`, and `\derived{}` macros, defined in [common.tex](https://github.com/teorth/expdb/blob/main/blueprint/src/macros/common.tex).

## Contributing to Lean code

Lean code is stored in [this directory](https://github.com/teorth/expdb/tree/main/Expdb).  A formalization effort is underway, but at present it covers only a small portion of the blueprint (the basic notation, $L^2$ integral estimate, and exponential sum growth exponent chapters); contributions extending it to further chapters are very welcome.  If you would like to work on a substantial piece of formalization, please do not hesitate to discuss it with the maintainers of the ANTEDB first, or raise a suitable [issue on the Github repository](https://github.com/teorth/expdb/issues), in order to coordinate with any other contributors.

When a blueprint result is formalized, annotate its statement in the blueprint with the `\lean{}` macro, listing the names of the corresponding Lean declarations, together with the `\leanok` macro.  Every declaration named in a `\lean{}` macro must also be listed in [lean_declarations.txt](https://github.com/teorth/expdb/blob/main/scripts/lean_declarations.txt), which is checked against the compiled Lean code by continuous integration; a renamed declaration therefore has to be updated in all three places.

Where a blueprint convention already has a standard Mathlib representation, please use that representation rather than introducing a new one.  Lean docstrings should refer to blueprint results by their label (for instance `beta-def`) rather than by their number, as the numbering is liable to change.

## A note on notational conventions

The ANTEDB is intended to collect results on analytic number theory exponents in the literature in such a way that they can be combined as readily as possible, by either humans or computers.  Because of this, we have made efforts to select standardized notations to apply globally across the ANTEDB, and to express results from the literature in these standardized notations, even if they are expressed in a somewhat different notation in the original source material.

For instance, we have chosen to use a "cheap nonstandard analysis" convention for asymptotic notation, as it efficiently hides the "epsilons and deltas" in the exponents, which has some technical advantages for the numerical side of the project as it often allows exponents to be represented by rational numbers which can be easily manipulated by exact arithmetic rather than floating point arithmetic.

The focus on the ANTEDB is on the exponent bounds in the literature, rather than the notational choices from that literature, and the addition of notational conventions to the ANTEDB that duplicate ones that are already present in the database is therefore discouraged in order to maximize interoperability of results.  However, it is conceivable that there is a case for globally refactoring the ANTEDB to switch from a current notational convention to new one; if so, one should set up a [Github issue](https://github.com/teorth/expdb/issues) to discuss the pros and cons of such a global switch.

## Creating a similar database

If you wish to create a database similar to the ANTEDB, but with a different scope, you may wish to set up a Lean Project with a Blueprint by following [these instructions](https://github.com/pitmonticone/LeanProject).  (The ANTEDB only formalizes a small portion of its blueprint in Lean; nevertheless, the Blueprint-based structure of a Lean project is quite convenient for such a database, even for the portions that have no accompanying Lean code.)

If you do create a new mathematical database, consider registering it at [Mathbases](https://github.com/MathBases/MathBases).

<!-- END SOURCE doc-7c0f19c0c944 -->

---

<a id="doc-c83c45e6e5c7"></a>

## 原文导签：Fermat's Last Theorem

来源：`work/documentation_memory_20260917/harness_sources/flt.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/flt.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-c83c45e6e5c7 -->
# Fermat's Last Theorem

[![Website](https://img.shields.io/badge/Website-ready-green)](https://ImperialCollegeLondon.github.io/FLT/)
[![Documentation](https://img.shields.io/badge/Documentation-passing-green)](https://ImperialCollegeLondon.github.io/FLT/docs/)
[![Blueprint](https://img.shields.io/badge/Blueprint-WIP-blue)](https://ImperialCollegeLondon.github.io/FLT/blueprint/)
[![Paper](https://img.shields.io/badge/Paper-WIP-blue)](https://ImperialCollegeLondon.github.io/FLT/blueprint.pdf)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ImperialCollegeLondon/FLT)

An ongoing multi-author open source project to formalise a proof of Fermat's Last Theorem in the Lean theorem prover.

# Information about the project

The project is currently being led by Kevin Buzzard. Until September 2029 it is being funded by [grant EP/Y022904/1](https://gtr.ukri.org/projects?ref=EP%2FY022904%2F1), awarded by the EPSRC. The project is hosted at Imperial College London. Kevin would like to extend many many thanks to both of these institutions for their ongoing support of this nonstandard research.

General information ("What is Fermat's Last Theorem/Lean?" / "Why are you doing this?" etc) is [here](GENERAL.md).

The route we will be taking was planned out essentially entirely by Richard Taylor in discussions with Buzzard. It is a modern variant of the original Wiles/Taylor-Wiles proof, borrowing heavily from the ideas of Khare and Wintenberger. For more details about the mathematics behind the proof, a good place to start is the [blueprint](https://ImperialCollegeLondon.github.io/FLT/blueprint/).

Information on how to contribute is available [here](CONTRIBUTING.md).

<!-- END SOURCE doc-c83c45e6e5c7 -->
