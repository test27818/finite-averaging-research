# 工作材料、历次快照及旧目录完整附卷 · 第24分册

[返回总目录](../CONTENTS.md) · [本卷连贯导读](../chapters/08_history_and_sources.md)

> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。

## 本册篇目

- [Lean blueprints](#doc-7a7d14686f7a)
- [Note: This original LeanDojo library is deprecated. Please use [LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2) for all new projects. The information below is kept for historical reference. We will soon be moving LeanDojo-v2 here.](#doc-4d6e1622231d)
- [LeanDojo-v2](#doc-d3415e63d179)
- [Pantograph](#doc-58f142c24461)
- [plasTeX dependency graphs](#doc-d050b8407693)
- [有限步平均研究](#doc-9552ec88e1c3)
- [成果与研究索引](#doc-4e5ac7f1570b)
- [一般元数与合数研究](#doc-2f4ed79ec151)
- [素数平均：当前证明入口](#doc-5c7475f6cb2b)
- [三平均：直接证明与原算术路线](#doc-e87de3743047)
- [素数平均的独立 p 进改进研究](#doc-2d3d409b320e)
- [`work/` 使用说明](#doc-887da36dd1e8)
- [H_t文献来源与访问等级](#doc-9700466383d0)
- [Literature retrieval, 2026-09-12](#doc-17e5e0f397d9)
- [2026-09-14研究审查材料](#doc-92dd4f085969)

---

<a id="doc-7a7d14686f7a"></a>

## 原文导签：Lean blueprints

来源：`work/documentation_memory_20260917/harness_sources/lean_blueprint.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/lean_blueprint.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-7a7d14686f7a -->
# Lean blueprints

This is a [plasTeX](https://github.com/plastex/plastex/) plugin allowing
to write blueprints for Lean 4 projects.
You can learn what those blueprints are about by reading
Terence Tao’s excellent [blog post about it](https://terrytao.wordpress.com/2023/11/18/formalizing-the-proof-of-pfr-in-lean4-using-blueprint-a-short-tour/).

This infrastructure was originally created in 2020 for the
[Sphere Eversion Project](https://leanprover-community.github.io/sphere-eversion/).
Since then, it has been used by many projects. The list below will give you many
examples but is not intended to be exhaustive.
It is in approximate chronological order, at least in the beginning of the list.

* [Sphere eversion project](https://leanprover-community.github.io/sphere-eversion/blueprint/index.html)
* [Liquid tensor experiment](https://leanprover-community.github.io/liquid/)
* [Unit fractions](https://b-mehta.github.io/unit-fractions/)
* [Fermat’s last theorem for regular primes](https://leanprover-community.github.io/flt-regular/blueprint/)
* [Arithmetic Progressions - Almost Periodicity](https://yaeldillies.github.io/LeanAPAP/blueprint/)
* [Polynomial Freiman-Ruzsa Conjecture](https://teorth.github.io/pfr/blueprint/)
* [Lower bounds for hypothesis testing based on information theory](https://remydegenne.github.io/testing-lower-bounds/blueprint/)
* [New Foundations is consistent](https://leanprover-community.github.io/con-nf/)
* [Prime number theorem and…](https://alexkontorovich.github.io/PrimeNumberTheoremAnd/web/)
* [Fermat's Last Theorem for 3](https://pitmonticone.github.io/FLT3/blueprint)
* [Fermat’s last theorem](https://imperialcollegelondon.github.io/FLT/blueprint/)
* [Carleson Operators on Doubling Metric Measure Spaces](http://florisvandoorn.com/carleson/)
* [Infinity Cosmos](https://github.com/emilyriehl/infinity-cosmos)
* [Analytic Number Theory Exponent Database](https://github.com/teorth/expdb)
* [Equational Theories](https://github.com/teorth/equational_theories)
* [HoTTLean](https://sinhp.github.io/groupoid_model_in_lean4/)
* [Sphere packing in Lean](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/)
* [Localic Caratheodory extensions](https://bergschaf.github.io/Localic-Caratheodory-Extensions)
* [Banach Tarski](https://bergschaf.github.io/lean-banach-tarski)
* [Bourgain extractor in Lean](https://github.com/Command-Master/lean-bourgain)
* [Semi circle Law](https://fredraj3.github.io/SemicircleLaw/)
* [Seymour](https://ivan-sergeyev.github.io/seymour/)
* [STIR verification](https://leastauthority.github.io/STIR/)
* [Central limit theorem](https://remydegenne.github.io/CLT/blueprint/)
* [Brownian motion](https://remydegenne.github.io/brownian-motion/)
* [Formally Verified Arguments of Knowledge](https://verified-zkevm.github.io/ArkLib/blueprint/)
* [Chandra Furst Lipton](https://yaeldillies.github.io/ChandraFurstLipton/)
* [Cambridge combinatorics](https://yaeldillies.github.io/LeanCamCombi/)
* [Toric varieties in Lean](https://yaeldillies.github.io/Toric/)
* [Iwasaw theory in Lean](https://acmepjz.github.io/lean-iwasawa/)
* [Irrationality of ζ(3)](https://ahhwuhu.github.io/zeta_3_irrational/blueprint/)
* [Exceptional set in the abc conjecture](https://b-mehta.github.io/ABC-Exceptions/)
* [Analysis in Bonn](https://florisvandoorn.com/BonnAnalysis/blueprint/)
* [Extreme Value Distribution Project](https://kkytola.github.io/ExtremeValueProject/)
* [Formal proofs from the book](https://firsching.ch/FormalBook/)
* [Spectral theorem](https://oliver-butterley.github.io/SpectralThm/)
* [Sphere packing](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/)
* [Radii Polynomial](https://ilpreterosso.github.io/LEANearized-RadiiPolynomial/)

## Installation

This package depends on `plastexdepgraph` which requires graphviz and its development libraries. 
If you have a user-friendly OS, it is as simple as 
`sudo apt install graphviz libgraphviz-dev`. 
See https://pygraphviz.github.io/documentation/stable/install.html otherwise.

Then, assuming you have a sane python environment, you only need to run:
```
pip install leanblueprint
```
Note this will automatically install plasTeX and the other needed python
packages.

## Upgrading

```
pip install -U leanblueprint
```

will upgrade to the latest version.

## Starting a blueprint

This package provides a command line tool `leanblueprint` that automates in
particular the creation of a blueprint for your Lean project. This tool is not
mandatory in any way. Its goal is to make it easy to create a blueprint without
worrying about choosing a file layout or a continuous integration and deployment
setup. As every one–size-fits-all tool, it is fairly opinionated. It assumes in
particular that your project repository is hosted on Github and you want to host
its blueprint on github.io.

If you don’t want to use the `leanblueprint` command line tool, you can use
this plugin as any other plasTeX plugin, using
`plastex --plugins leanblueprint my_file.tex` (not recommended).

In order to use the `leanblueprint` tool, you need to already have a Lean
project created using lake. In addition, your blueprint will be easier to
configure if you have at least one commit in the git repository of your project
and you have already configured its GitHub git remote (GitHub displays
instructions allowing to do the remote setup when you create a new repository
there). You should also tell GitHub that you want to use GitHub pages using
GitHub actions. You can do that from the GitHub page of your repository by
clicking on the Settings tab in the top menu, then the Pages link in the side
menu and selecting GitHub Actions as the source, as in the following
screenshot.

![GitHub pages settings](github_settings.png)

Assuming your project is ready and GitHub is configured, from your project
folder run 
```
leanblueprint new
```
You will then have to answer some questions to configure your blueprint. If
unsure, accept all default answers by simply hitting Enter for each question.
Only two questions will insist on having an explicit y/n answer: the question
confirming you want to create the blueprint and the one proposing to commit
to your git repository.

After running this creation script, you can push to GitHub and wait
for GitHub Actions to build your blueprint. You can monitor this task 
in the Actions tab of the GitHub page of your repository. 
When building is done, the html version of your blueprint will be deployed to 
`https://user_name.github.io/repo_name/blueprint/` (with the appropriate
user or organization name and repository name). The pdf version will be at 
`https://user_name.github.io/repo_name/blueprint.pdf`.
The API documentation will be at `https://user_name.github.io/repo_name/docs/`.

## Local compilation

Assuming you used the `leanblueprint` command line tool to create your blueprint
(or at least that you use the same file layout), you can use `leanblueprint` to
build your blueprint locally. The available commands are:

* `leanblueprint pdf` to build the pdf version (this requires a TeX installation
  of course).
* `leanblueprint web` to build the web version
* `leanblueprint checkdecls` to check that every Lean declaration name that appear
  in the blueprint exist in the project (or in a dependency of the project such
  as Mathlib). This requires a compiled Lean project, so make sure to run `lake build` beforehand.
* `leanblueprint all` to run the previous three commands.
* `leanblueprint serve` to start a local webserver showing your local blueprint
  (this sounds silly but web browsers paranoia makes it impossible to simply
  open the generated html pages without serving them). The url you should use
  in your browser will be displayed and will probably be `http://0.0.0.0:8000/`,
  unless the port 8000 is already in use.

Note: plasTeX does not call BibTeX. If you have a bibliography, you should use
`leanblueprint pdf` before `leanblueprint web` to get it to work in the web
version (and redo it when you add a reference).

## Editing the blueprint

Assuming you used the `leanblueprint` command line tool to create your blueprint
(or at least that you use the same file layout), the source of your blueprint
will be in the `blueprint/src` subfolder of your Lean project folder.

Here you will find two main TeX files: `web.tex` and `print.tex`. The first one
is intended for plasTeX while the second one is intended for a traditional TeX
compiler such as `xelatex` or `lualatex`. 
Each of them includes `macros/common.tex` for all TeX macros that make sense
for both kinds of outputs (this should be most of your macros). 
Macros that should behave differently depending on the target format should go
to either `macros/web.tex` or `macros/print.tex`. All those files already exist
and contains comments reminding you about the above explanations.

The main content of your blueprint should live in `content.tex` (or in files
imported in `content.tex` if you want to split your content).

The main TeX macros that relate your TeX code to your Lean code are:

* `\lean` that lists the Lean declaration names corresponding to the surrounding
  definition or statement (including namespaces).
* `\leanok` which claims the surrounding environment is fully formalized. Here
  an environment could be either a definition/statement or a proof.
* `\uses` that lists LaTeX labels that are used in the surrounding environment.
  This information is used to create the dependency graph. Here
  an environment could be either a definition/statement or a proof, depending on
  whether the referenced labels are necessary to state the definition/theorem
  or only in the proof.

The example below show those essential macros in action, assuming the existence of
LaTeX labels `def:immersion`, `thm:open_ample` and `lem:open_ample_immersion` and
assuming the existence of a Lean declaration `sphere_eversion`.

```latex
\begin{theorem}[Smale 1958]
  \label{thm:sphere_eversion}
  \lean{sphere_eversion}
  \leanok
  \uses{def:immersion}
  There is a homotopy of immersions of $𝕊^2$ into $ℝ^3$ from the inclusion map to
  the antipodal map $a : q ↦ -q$.
\end{theorem}
  
\begin{proof}
  \leanok
  \uses{thm:open_ample, lem:open_ample_immersion}
  This obviously follows from what we did so far.
\end{proof}
```

Note that the proof above is abbreviated in this documentation. 
Be nice to you and your collaborators and include more details in your blueprint proofs!

By default, the dependency graph will collect the environments definition,
lemma, proposition, theorem and corollary. You can change this list using the
`thms` option which expects a list of environment names separated by `+` signs. 
For instance you can write
```latex
\usepackage[thms=dfn+lem+prop+thm+cor]{blueprint}
```
if you like short environment names. See the 
[plastexdepgraph documentation](https://github.com/PatrickMassot/plastexdepgraph/blob/master/README.md) 
for other dependency graph options having nothing to do with Lean.
Note that this is giving the `depgraph` package options directly when loading
the `blueprint` package. Do not load the `depgraph` package separately.


The above macros are by far the most important, but there are a couple more.

* `\notready` which claims the surrounding environment is not ready to be formalized,
  typically because it requires more blueprint work.
* `\discussion` gives a GitHub issue number where the surrounding definition or
  statement is discussed.
* `\proves` inside a proof environment gives the LaTeX label of the LaTeX
  statement being proved. This is necessary only when the proof does not
  immediately follow the statement.
* `\mathlibok` marks nodes that were already merged into mathlib.

## Blueprint configuration

Most of the configuration is handled during the blueprint creation if you used
the `leanblueprint` client. But some of it can be changed by LaTeX macros
in the web version of LaTeX preamble (in the file `web.tex` if you use the
default layout).

* `\home{url}` defines the url of the home page of the project.
* `\github{url}` defines the url of the git repository of the project.
* `\dochome{url}` defines the url of the doc-gen API documentation of the
  project.
* `\graphcolor{node_type}{color}{description}` sets a color in the dependency
  graph and its description in the legend. The default values are
    * `stated`, `green`, `Green`
    * `can_state`, `blue`, `Blue`
    * `not_ready`, `#FFAA33`, `Orange`
    * `proved`, `#9CEC8B`, `Green`
    * `can_prove`, `#A3D6FF`, `Blue`
    * `defined`, `#B0ECA3`, `Light green`
    * `fully_proved`, `#1CAC78`, `Dark green`
    * `mathlib`, `darkgreen`, `Dark green`

    In particular you can use the above color descriptions to interpret the node
    type by comparison with the default legend.

## Acknowledgments

The continuous integration configuration template used by `leanblueprint new`
is based on the work of many people who had to write such a configuration by
hand in the past, including Yakov Pechersky, Ben Toner, Sky Wilshaw, Yaël Dillies
and Utensil Song. It also got contributions from Pietro Monticone.

<!-- END SOURCE doc-7a7d14686f7a -->

---

<a id="doc-4d6e1622231d"></a>

## 原文导签：Note: This original LeanDojo library is deprecated. Please use [LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2) for all new projects. The information below is kept for historical reference. We will soon be moving LeanDojo-v2 here.

来源：`work/documentation_memory_20260917/harness_sources/leandojo.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/leandojo.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-4d6e1622231d -->
LeanDojo: Machine Learning for Theorem Proving in Lean
======================================================

### Note: This original LeanDojo library is deprecated. Please use [LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2) for all new projects. The information below is kept for historical reference. We will soon be moving LeanDojo-v2 here.

![LeanDojo](https://github.com/lean-dojo/LeanDojo/blob/main/images/LeanDojo.jpg)

[LeanDojo](https://leandojo.org/) is a Python library for learning–based theorem provers in Lean, providing two main features:

* Extracting data (proof states, tactics, premises, etc.) from Lean repos.
* Interacting with Lean programmatically.

LeanDojo's current version is compatible with Lean 4 `v4.3.0-rc2` or later. We strongly suggest using the current version. However, you may use the [`legacy`](https://github.com/lean-dojo/LeanDojo/tree/legacy) branch if you want to work with earlier versions (including Lean 3).

[![Documentation Status](https://readthedocs.org/projects/leandojo/badge/?version=latest)](https://leandojo.readthedocs.io/en/latest/?badge=latest) [![PyPI](https://img.shields.io/pypi/v/lean-dojo)](https://pypi.org/project/lean-dojo/) [![GitHub license](https://img.shields.io/github/license/lean-dojo/LeanDojo)](https://github.com/lean-dojo/LeanDojo/blob/main/LICENSE) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

______________________________________________________________________

## Requirements

* Supported platforms: Linux, Windows WSL, and macOS
* Git >= 2.25
* 3.9 <= Python < 3.13
* wget
* [elan](https://github.com/leanprover/elan)
* Generate a [GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#personal-access-tokens-classic) and set the environment variable `GITHUB_ACCESS_TOKEN` to it


## Installation

LeanDojo is available on [PyPI](https://pypi.org/project/lean-dojo/) and can be installed via pip:
```bash
pip install lean-dojo
```

It can also be installed locally from the Git repo:
```bash
pip install .
```


## Documentation

* [Getting Started](https://leandojo.readthedocs.io/en/latest/getting-started.html)
* [Demo](https://github.com/lean-dojo/LeanDojo/blob/main/scripts/demo-lean4.ipynb)
* [Full documentation](https://leandojo.readthedocs.io/en/latest/index.html)


## Questions and Bugs

* For general questions and discussions, please use [GitHub Discussions](https://github.com/lean-dojo/LeanDojo/discussions).  
* To report a potential bug, please open an issue. In the issue, please include your OS information, the exact steps to reproduce the error on **the latest version of LeanDojo**, and complete logs in debug mode (setting the environment variable `VERBOSE` to 1). **Important: If your issue cannot be reproduced easily, it will be unlikely to receive any help.**


## Related Links

* [LeanDojo Website](https://leandojo.org/): The official website of LeanDojo.
* [LeanDojo Benchmark](https://doi.org/10.5281/zenodo.8016385) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8016385.svg)](https://doi.org/10.5281/zenodo.8016385): The dataset used in our paper, consisting of theorems and proofs extracted from [mathlib](https://github.com/leanprover-community/mathlib/commits/19c869efa56bbb8b500f2724c0b77261edbfa28c).
* [LeanDojo Benchmark 4](https://doi.org/10.5281/zenodo.8040109) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8040109.svg)](https://doi.org/10.5281/zenodo.8040109): The Lean 4 version of LeanDojo Benchmark, consisting of theorems and proofs extracted from [mathlib4](https://github.com/leanprover-community/mathlib4/commit/29dcec074de168ac2bf835a77ef68bbe069194c5) by [generate-benchmark-lean4.ipynb](./scripts/generate-benchmark-lean4.ipynb).
* [ReProver](https://github.com/lean-dojo/ReProver): The ReProver (Retrieval-Augmented Prover) model in our paper.
* [LeanDojo ChatGPT Plugin](https://github.com/lean-dojo/LeanDojoChatGPT)
* [Lean Copilot: Running language models as copilots for theorem proving in Lean](https://github.com/lean-dojo/LeanCopilot)

## Citation

[LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](https://leandojo.org/)      
Neural Information Processing Systems (NeurIPS), 2023  
[Kaiyu Yang](https://yangky11.github.io/), [Aidan Swope](https://aidanswope.com/about), [Alex Gu](https://minimario.github.io/), [Rahul Chalamala](https://rchalamala.github.io/),  
[Peiyang Song](https://peiyang-song.github.io/), [Shixing Yu](https://billysx.github.io/), [Saad Godil](https://www.linkedin.com/in/saad-godil-9728353/), [Ryan Prenger](https://www.linkedin.com/in/ryan-prenger-18797ba1/), [Anima Anandkumar](http://tensorlab.cms.caltech.edu/users/anima/)

```bibtex
@inproceedings{yang2023leandojo,
  title={{LeanDojo}: Theorem Proving with Retrieval-Augmented Language Models},
  author={Yang, Kaiyu and Swope, Aidan and Gu, Alex and Chalamala, Rahul and Song, Peiyang and Yu, Shixing and Godil, Saad and Prenger, Ryan and Anandkumar, Anima},
  booktitle={Neural Information Processing Systems (NeurIPS)},
  year={2023}
}
```

<!-- END SOURCE doc-4d6e1622231d -->

---

<a id="doc-d3415e63d179"></a>

## 原文导签：LeanDojo-v2

来源：`work/documentation_memory_20260917/harness_sources/leandojo_v2.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-d3415e63d179 -->
# LeanDojo-v2

LeanDojo-v2 is an end-to-end framework for training, evaluating, and deploying AI-assisted theorem provers for Lean 4. It combines repository tracing, lifelong dataset management, retrieval-augmented agents, Hugging Face fine-tuning, and external inference APIs into one toolkit.


## Table of Contents

1. [Overview](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#overview)
2. [Key Features](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#key-features)
3. [Repository Layout](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#repository-layout)
4. [Requirements](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#requirements)
5. [Installation](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#installation)
6. [Environment Setup](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#environment-setup)
7. [Quick Start](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#quick-start)
8. [Working with Agents and Trainers](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#working-with-agents-and-trainers)
9. [Tracing and Dataset Generation](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#tracing-and-dataset-generation)
10. [LeanProgress Step-Prediction](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#leanprogress-step-prediction)
11. [Proving Theorems](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#proving-theorems)
12. [Testing](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#testing)
13. [Troubleshooting & Tips](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#troubleshooting--tips)
14. [Contributing](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#contributing)
15. [License](../sources/work/documentation_memory_20260917/harness_sources/leandojo_v2.md#license)


## Overview

LeanDojo-v2 extends the original LeanDojo stack with the LeanAgent lifelong learning pipeline. It automates the entire loop of:

1. Cloning Lean repositories (GitHub or local) and tracing them with Lean instrumentation.
2. Storing structured theorem information in a dynamic database.
3. Training agent policies with supervised fine-tuning (SFT), GRPO-style RL, or retrieval objectives.
4. Driving Pantograph-based provers to fill in sorrys or verify solutions.
5. Using HuggingFace API for large model inference.

The codebase is modular: you can reuse the tracing pipeline without the agents, swap in custom trainers, or stand up your own inference service via the external API layer.


## Key Features

- **Unified Agent Abstractions**: `BaseAgent` orchestrates repository setup, training, and proving. Concrete implementations (`HFAgent`, `LeanAgent`, and `ExternalAgent`) tailor the workflow to Hugging Face models, retrieval-based provers, or REST-backed models.
- **Powerful Trainers**: `SFTTrainer`, `GRPOTrainer`, and `RetrievalTrainer` cover LoRA-enabled supervised fine-tuning, group-relative policy optimization, and retriever-only curriculum learning.
- **Multi-Modal Provers**: `HFProver`, `RetrievalProver`, and `ExternalProver` run on top of Pantograph’s Lean RPC server to search for tactics, generate whole proofs, or delegate to custom models.
- **Lean Tracing Pipeline**: `lean_dojo` includes the Lean 4 instrumentation (`ExtractData.lean`) and Python utilities to trace commits, normalize ASTs, and cache proof states.
- **Dynamic Repository Database**: `database` tracks repositories, theorems, curriculum difficulty, and sorry status, enabling lifelong training schedules.
- **External API**: The `external_api` folder exposes HTTP endpoints (FastAPI + uvicorn) and Lean frontend snippets so you can query LLMs from Lean editors.


## Repository Layout

| Path | Description |
|------|-------------|
| `lean_dojo_v2/agent/` | Base class plus `HFAgent`, `LeanAgent`, and helpers to manage repositories and provers. |
| `lean_dojo_v2/trainer/` | SFT, GRPO, and retrieval trainers with Hugging Face + DeepSpeed integration. |
| `lean_dojo_v2/prover/` | Pantograph-based prover implementations (HF, retrieval, external). |
| `lean_dojo_v2/lean_dojo/` | Lean tracing, dataset generation, caching, and AST utilities. |
| `lean_dojo_v2/lean_agent/` | Lifelong learning pipeline (configs, database, retrieval stack, generator). |
| `lean_dojo_v2/external_api/` | LeanCopilot code (Lean + Python server) to query external models. |
| `lean_dojo_v2/utils/` | Shared helpers for Git, filesystem operations, and constants. |
| `lean_dojo_v2/tests/` | Pytest regression suite. |

For deeper documentation on the lifelong learning component, see `lean_dojo_v2/lean_agent/README.md`.


## Requirements

- Python ≥ 3.11.
- CUDA-capable GPU for training and inference (tested with CUDA 12.6).
- Git ≥ 2.25 and `wget`.
- [elan](https://github.com/leanprover/elan) Lean toolchain to trace repositories locally.
- Adequate disk space for the `raid/` working directory (datasets, checkpoints, traces).

Python dependencies are declared in `pyproject.toml` and include PyTorch, PyTorch Lightning, Transformers, DeepSpeed, TRL, PEFT, and more.


## Installation

### Option 1: From PyPI

```sh
# Install the core package
pip install lean-dojo-v2

# Pantograph is required for Lean RPC
pip install git+https://github.com/stanford-centaur/PyPantograph

# Install a CUDA-enabled torch build (adjust the index URL for your CUDA version)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```

### Option 2: From Source (development)

```sh
git clone https://github.com/lean-dojo/LeanDojo-v2.git
cd LeanDojo-v2
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"
pip install git+https://github.com/stanford-centaur/PyPantograph
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```

> Tip: You can use [uv](https://github.com/astral-sh/uv) (`uv pip install lean-dojo-v2`) as an alternative Python package manager.


## Environment Setup

1. **GitHub Access Token (required)**  
   The tracing pipeline calls the GitHub API extensively. Create a personal access token and export it before running any agent:

   ```sh
   export GITHUB_ACCESS_TOKEN=<token>
   ```

2. **Hugging Face Token (optional but needed for gated models)**  

   ```sh
   export HF_TOKEN=<hf-token>
   ```

3. **Working directories**  
   By default all datasets, caches, and checkpoints live under `<repo>/raid`. Change the layout by editing `lean_dojo_v2/utils/constants.py` or by pointing `RAID_DIR` to faster storage.

4. **Lean toolchains**  
   Ensure `elan` is configured and Lean 4 (e.g., `leanprover/lean4:nightly`) is available on your `$PATH`. The tracing scripts look under `~/.elan/toolchains/`.


## Quick Start

```python
from lean_dojo_v2.agent.hf_agent import HFAgent
from lean_dojo_v2.trainer.sft_trainer import SFTTrainer

url = "https://github.com/durant42040/lean4-example"
commit = "3e23ab0bfdcfdbd5b11ab53c2cd8b5d16492e9c2"

trainer = SFTTrainer(
    model_name="deepseek-ai/DeepSeek-Prover-V2-7B",
    output_dir="outputs-deepseek",
    epochs_per_repo=1,
    batch_size=2,
    lr=2e-5,
)

agent = HFAgent(trainer=trainer)
agent.setup_github_repository(url=url, commit=commit)
agent.train()
agent.prove()
```

This example:

1. Downloads and traces the target Lean repository + commit.
2. Builds a supervised dataset from sorry theorems.
3. Fine-tunes the specified Hugging Face model (optionally with LoRA).
4. Launches an `HFProver` backed by Pantograph to search for proofs.

## Tracing and Dataset Generation

The `lean_dojo_v2/lean_dojo/data_extraction` package powers repository tracing:

- `lean.py` clones repositories (GitHub, remote, or local), validates Lean versions, and normalizes URLs.
- `trace.py` drives Lean with the custom `ExtractData.lean` instrumented module to capture theorem states.
- `dataset.py` converts traced files to JSONL datasets ready for trainers.
- `cache.py` memoizes repository metadata to avoid redundant downloads.
- `traced_data.py` exposes typed wrappers for traced AST nodes and sorrys.

Typical usage:

```python
from lean_dojo_v2.database import DynamicDatabase

url = "https://github.com/durant42040/lean4-example"
commit = "3e23ab0bfdcfdbd5b11ab53c2cd8b5d16492e9c2"

database = DynamicDatabase()

database.trace_repository(
    url=url,
    commit=commit,
    build_deps=False,
)
```

The `build_deps` options decides whether LeanDojo will extract the premises from the repository's external dependencies, it is set to `False` by default. However, if you are using the traced data to train LeanAgent, it must be set to `True`.  The generated artifacts flow into the `DynamicDatabase`, which keeps repositories sorted by difficulty and appends new sorrys without retracing everything.

## Working with Agents and Trainers

### Agents

Agents orchestrate the full workflow of repository setup, training, and theorem proving. Each agent pairs a trainer with a compatible prover.

#### `HFAgent`

Uses Hugging Face models fine-tuned with `SFTTrainer` or `GRPOTrainer` for theorem proving. Loads checkpoints locally and uses `HFProver` for proof search. Ideal for training custom models on your traced repositories. Does not build Lean dependencies by default.

```python
from lean_dojo_v2.agent.hf_agent import HFAgent
from lean_dojo_v2.trainer.sft_trainer import SFTTrainer

trainer = SFTTrainer(model_name="deepseek-ai/DeepSeek-Prover-V2-7B", ...)
agent = HFAgent(trainer=trainer)
agent.setup_github_repository(url, commit)
agent.train()  
agent.prove()   
```

#### `ExternalAgent`

Uses the Hugging Face Inference API to access large models like DeepSeek-Prover-V2-671B without local model loading. Pairs with `ExternalProver` for whole-proof generation or proof search. Best for quick experiments or when you don't have GPU resources for local inference.

```python
from lean_dojo_v2.agent.external_agent import ExternalAgent

agent = ExternalAgent()
agent.setup_github_repository(url, commit)
agent.prove()  
```

#### `LeanAgent`

Implements the lifelong learning pipeline with retrieval-augmented generation. Uses `RetrievalTrainer` to train premise retrievers, then pairs with `RetrievalProver` for retrieval-augmented tactic generation. Maintains repository curricula and builds Lean dependencies by default.

```python
from lean_dojo_v2.agent.lean_agent import LeanAgent

agent = LeanAgent()
agent.setup_github_repository(url, commit)
agent.train()  
agent.prove()   
```

### Trainers

#### Supervised Fine-Tuning (`SFTTrainer`)

- Accepts any Hugging Face causal LM identifier.
- Supports LoRA by passing a `peft.LoraConfig`.
- Key arguments: `epochs_per_repo`, `batch_size`, `max_seq_len`, `lr`, `warmup_steps`, `gradient_checkpointing`.
- Produces checkpoints under `output_dir` that the `HFProver` consumes.

#### GRPO Trainer (`GRPOTrainer`)

- Implements Group Relative Policy Optimization for reinforcement-style refinement.
- Accepts `reference_model`, `reward_weights`, and `kl_beta` settings.
- Useful for improving search policies on curated theorem batches.

#### Retrieval Trainer (`RetrievalTrainer`)

- Trains the dense retriever that scores prior proofs from the corpus.
- Used by `LeanAgent` to build retrieval-augmented generation models.
- Requires indexed corpus and generator checkpoints.

Each agent inherits `BaseAgent`, so you can implement your own by overriding `_get_build_deps()` and `_setup_prover()` to register new trainer/prover pairs.

## LeanProgress Step-Prediction

- Generate a JSONL dataset with remaining-step targets (or replace it with your own LeanProgress export):

  ```sh
  python -m lean_dojo_v2.lean_progress.create_sample_dataset --output raid/data/sample_leanprogress_dataset.jsonl
  ```

- Fine-tune a regression head that predicts `steps_remaining`:

  ```python
  from pathlib import Path

  from lean_dojo_v2.trainer.progress_trainer import ProgressTrainer

  sample_dataset_path = Path("raid/data/sample_leanprogress_dataset.jsonl")

  trainer = ProgressTrainer(
      model_name="bert-base-uncased",
      data_path=str(sample_dataset_path),
      output_dir="outputs-progress",
  )

  trainer.train()
  ```

## Proving Theorems

LeanDojo-v2 provides three prover implementations, each for different use cases:

### `HFProver`

Loads a fine-tuned Hugging Face model from a local checkpoint (supports full models and LoRA adapters) and generates tactics directly, used for locally trained Hugging Face model (e.g. with `SFTTrainer` and `GRPOTrainer`).

### `ExternalProver`

Performs inference with the Hugging Face Inference API to access large models without local GPU resources. Defaults to DeepSeek-Prover-V2-671B. Supports both proof search and whole-proof generation.

### `RetrievalProver`

Used directly with LeanAgent.

### Proof Methods

LeanDojo-v2 supports two methods for theorem proving:

- **Whole-proof generation**: generate complete proof in one forward pass of the prover.

  ```python
  from lean_dojo_v2.prover import ExternalProver

  theorem = "theorem my_and_comm : ∀ {p q : Prop}, And p q → And q p := by"
  prover = ExternalProver()
  proof = prover.generate_whole_proof(theorem)
  ```

- **Proof search**: generate tactics sequentially and update the goal state through interaction with Pantograph until the proof is complete.

  ```python
  from pantograph.server import Server
  from lean_dojo_v2.prover import HFProver

  server = Server()
  prover = HFProver(ckpt_path="outputs-deepseek")

  result, used_tactics = prover.search(
      server=server, goal="∀ {p q : Prop}, p ∧ q → q ∧ p", verbose=False
  )
  ```

## Testing

We use `pytest` for regression coverage.

```sh
pip install -e .[dev]          # make sure dev extras like pytest/trl are present
export GITHUB_ACCESS_TOKEN=<token>
export HF_TOKEN=<hf-token>     # only required for tests touching HF APIs
pytest -v
```

## Troubleshooting & Tips

- **401 Bad Credentials / rate limits**: Ensure `GITHUB_ACCESS_TOKEN` is exported and has `repo` + `read:org` scopes.
- **Lean tracing failures**: Confirm that the repo’s Lean version exists locally (`elan toolchain install <version>`).
- **Missing CUDA libraries**: Install the PyTorch wheel that matches your driver and CUDA version.
- **Dataset location**: The default `raid/` directory can grow large. Point it to high-throughput storage or use symlinks.
- **Pantograph errors**: Reinstall Pantograph from source (`pip install git+https://github.com/stanford-centaur/PyPantograph`) whenever Lean upstream changes.


## Contributing

Issues and pull requests are welcome! Please:

1. Open an issue describing the bug or feature.
2. Run formatters (`black`, `isort`) and `pytest` before submitting.
3. Mention if your change touches Lean tracing files so reviewers can re-generate artifacts.

## License

LeanDojo-v2 is released under the MIT License. See `LICENSE` for details.

<!-- END SOURCE doc-d3415e63d179 -->

---

<a id="doc-58f142c24461"></a>

## 原文导签：Pantograph

来源：`work/documentation_memory_20260917/harness_sources/pantograph.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/pantograph.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-58f142c24461 -->
# Pantograph

A Machine-to-Machine interaction system for Lean 4.

![Pantograph](doc/icon.svg)

Pantograph provides interfaces to execute proofs, construct expressions, and
examine the symbol list of a Lean project for machine learning.

See [documentations](doc/rationale.md) for design rationale and references.

## Installation

For Nix users, run
``` sh
nix build .#{sharedLib,executable}
```
to build either the shared library or executable.

Install `lake` and `lean` fixed to the version of the `lean-toolchain` file, and
run

``` sh
lake build
```
This builds the executable in `.lake/build/bin/pantograph-repl`.

## Executable Usage

``` sh
pantograph-repl MODULES|LEAN_OPTIONS
```

The `pantograph-repl` executable must be run with a list of modules to import.
It can also accept lean options of the form `--key=value` e.g. `--pp.raw=true`.

The REPL loop accepts commands as single-line JSON inputs and outputs either an
`Error:` (indicating malformed command) or a JSON return value indicating the
result of a command execution.  The command can be passed in one of two formats
```
command { ... }
{ "cmd": command, "payload": ... }
```
The list of available commands can be found in `Pantograph/Protocol.lean` and below. An
empty command aborts the REPL.


Example: (~5k symbols)
```
$ pantograph Init
env.catalog
env.inspect {"name": "Nat.le_add_left"}
```
Example with `mathlib4` (~90k symbols, may stack overflow, see troubleshooting)
```
$ pantograph Mathlib.Analysis.Seminorm
env.catalog
```
Example proving a theorem: (alternatively use `goal.start {"copyFrom": "Nat.add_comm"}`) to prime the proof
```
$ pantograph Init
goal.start {"expr": "∀ (n m : Nat), n + m = m + n"}
goal.tactic {"stateId": 0, "goalId": 0, "tactic": "intro n m"}
goal.tactic {"stateId": 1, "goalId": 0, "tactic": "assumption"}
goal.delete {"stateIds": [0]}
stat {}
goal.tactic {"stateId": 1, "goalId": 0, "tactic": "rw [Nat.add_comm]"}
stat
```
where the application of `assumption` should lead to a failure.

For a list of commands, see [REPL Documentation](doc/repl.md).

### Project Environment

To use Pantograph in a project environment, setup the `LEAN_PATH` environment
variable so it contains the library path of lean libraries. The libraries must
be built in advance. For example, if `mathlib4` is stored at `../lib/mathlib4`,
the environment might be setup like this:

``` sh
LIB="../lib"
LIB_MATHLIB="$LIB/mathlib4/.lake"
export LEAN_PATH="$LIB/mathlib4/build/lib:$LIB_MATHLIB/aesop/build/lib:$LIB_MATHLIB/Qq/build/lib:$LIB_MATHLIB/std/build/lib"

LEAN_PATH=$LEAN_PATH build/bin/pantograph $@
```
The `$LEAN_PATH` executable of any project can be extracted by
``` sh
lake env printenv LEAN_PATH
```

### Troubleshooting

If lean encounters stack overflow problems when printing catalog, execute this before running lean:
```sh
ulimit -s unlimited
```

## Library Usage

`Pantograph/Library.lean` exposes a series of interfaces which allow FFI call
with `Pantograph` which mirrors the REPL commands above. It is recommended to
call Pantograph via this FFI since it provides a tremendous speed up.

The executable can be used as-is, but linking against the shared library
requires the presence of `lean-all`. Note that there isn't a 1-1 correspondence
between executable (REPL) commands and library functions.

Inject any project path via the `pantograph_init_search` function.

## Developing

A Lean development shell is provided in the Nix flake.

### Testing

The tests are based on `LSpec`. To run tests, use either
``` sh
nix flake check
```
or
``` sh
lake test
```
You can run an individual test by specifying a prefix

``` sh
lake test -- "Tactic/No Confuse"
```

<!-- END SOURCE doc-58f142c24461 -->

---

<a id="doc-d050b8407693"></a>

## 原文导签：plasTeX dependency graphs

来源：`work/documentation_memory_20260917/harness_sources/plastexdepgraph.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/harness_sources/plastexdepgraph.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-d050b8407693 -->
# plasTeX dependency graphs

This is a [plasTeX](https://github.com/plastex/plastex/) plugin allowing
to build dependency graphs.

Needs graphviz and its dev libraries. If you have a user-friendly OS, it is
as simple as `sudo apt install graphviz libgraphviz-dev`. See https://pygraphviz.github.io/documentation/stable/install.html otherwise.

You can use this package with plasTeX using `\usepackage{depgraph}`.
Do not forget to tell plasTeX to use this plugin. From the command line, this
would mean running `plastex --plugins=plastexdepgraph test.tex` for instance.
Note that the
[Lean blueprint package](https://github.com/PatrickMassot/leanblueprint)
automatically loads this packages and transmit options.

## Options

When loading the package inside the tex file, you can give the following
arguments:
* title: the title of the dependency graph.
        The default value is Dependencies.
* dep_by: optional level for dependency graph generation, for instance chapter
        or part.
        The default value is to generate one graph for the whole document
* thms: optional list of theorem types to include into the report,
        separated by +.
        The default value is: definition+lemma+proposition+theorem+corollary
* nonreducedgraph: keep all edges in the dependency, even transitively
        redundant ones.
* tpl: template file for dependency graph, relative to the current
  directory

For instance you could write 
```latex
\usepackage[thms=dfn+lem+prop+thm+cor]{depgraph}
```
if you like short environment names.

This package will also consider optional information contained in the document
userdata dictionary. Such information could be added by other packages who
want to influence the dependency graph. For instance the 
[Lean blueprint plugin](https://github.com/PatrickMassot/leanblueprint)
does that.

* `document.userdata['dep_graph']['shapes']` can be a dictionary whose keys are node
  kinds as strings and whose values are strings descripting graphviz shapes
  (see https://graphviz.org/doc/info/shapes.html).
  By default, everything uses an ellipse except definition which uses a box.

* `document.userdata['dep_graph']['colorizer']` can be a function taking as input
  a plasTeX node and outputting a CSS color for the boundary of graph nodes.

* `document.userdata['dep_graph']['fillcolorizer']` can be a function taking as
  input a plasTeX node and outputting a CSS color for the interior of graph
  nodes.

* `document.userdata['dep_graph']['stylerizer']` can be a function taking as input
  a plasTeX node and outputting a graphviz style
  (see https://graphviz.org/docs/attr-types/style/).

* `document.userdata['dep_graph']['legend']` can be a list whose entries are pairs
  made of a visual description and an explanation.
  The default value is:
  [('Boxes', 'definitions'), ('Ellipses', 'theorems and lemmas')]
  Additional entries can also refer to colors.

* `document.userdata['dep_graph']['extra_modal_links']` can be a list of Jinja2
  templates used to render extra links at the bottom of the modal appearing
  when clicking on graph nodes.
  The default value is an empty list.

## Minimal example

The procedure to create a minimal example of using this plugin is:

* Install the required graphviz packages (say using  `sudo apt install graphviz libgraphviz-dev`)
* Install this python package (say using `pip install plastexdepgraph` which
will also install the main platex program).
* Create a TeX file `test.tex` with content

  ```latex
  \documentclass{article}
  \usepackage{depgraph}

  \newtheorem{definition}{Definition}

  \begin{document}
  \section{Test}
    
  \begin{definition}
    \label{def:one} My first definition.
  \end{definition}

  \begin{definition}
    \uses{def:one}
    \label{def:two} My second definition.
  \end{definition}
  \end{document}
  ```
* Run `plastex --plugins=plastexdepgraph test.tex`
* Serve the content of the newly created `test` folder, say with `python -m
http.server` ran from that folder (simply opening the html files as local files without going through a web server won’t work).

Note the `\section` is here to ensure there will be some table of contents. Otherwise the dependency graph will be generated but you won’t see any link.
<!-- END SOURCE doc-d050b8407693 -->

---

<a id="doc-9552ec88e1c3"></a>

## 原文导签：有限步平均研究

来源：`work/documentation_memory_20260917/originals/README.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/originals/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-9552ec88e1c3 -->
# 有限步平均研究

更新：2026-09-15。当前工作是**整理和改进素数平均证明**；合数研究保留原进展，本轮暂停推进。

对奇素数 p，最优最终阈值已证明为 N(p)=2p+1；二平均 N(2)=4。n 在阈值以上时，非全等有理输入经原位置 p 平均可达全等，当且仅当中心化、本原化后的差分 gcd 是 p 的幂。只有 p 不整除 n 时才能简写成 G=1。

[文件夹地图](../sources/work/documentation_memory_20260917/originals/outputs/README.md)展示主题目录；[最新简化](outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)用三个共轭根降低同余层，删除奇数n的高阶轨道，统一反射公式覆盖p≥83。

## 从这里开始

| 需要 | 入口 |
|---|---|
| 新 AI 接手／理解当前定理 | [素数证明入口](../sources/work/documentation_memory_20260917/originals/outputs/prime_arity/README.md) |
| 完整证明链与各维数覆盖 | [总证明](outputs/prime_arity/proof.md) |
| 统一代数工具与真正的几何结构 | [通用引理](outputs/prime_arity/arithmetic_toolkit.md) · [模曲线与标记格](outputs/prime_arity/geometry.md) |
| 阅读记录、证明证据、独立审核 | [本轮核验说明](outputs/prime_arity/verification.md) |
| 合数的现有成果与 GRH 条件 | [合数交接](outputs/general_arity/general_k_three_tasks_progress_20260915.md) |
| 三平均直接证明、算法和其他主题 | [成果索引](../sources/work/documentation_memory_20260917/originals/outputs/README.md) |
| 查询曾试过什么 | [历史路线账本](outputs/history/research_routes_history_20260915.md) · [原根进展日志](HISTORY.md) |

素数证明无条件，但引用已审核的 Morris/Serre 定理，且九偏移部分保留162组有限反射证书（已从522组缩减）。尚未证明可变 p、n 下的统一多项式操作长度，也未解决一般合数元数的最优最终阈值。旧历史文稿的“未解”不覆盖当前已完成结论。

## 核验入口

在项目根目录执行：

```text
python work/run_verifications.py --profile prime-proof
```

这是素数主线的选定核验集，现采用162组精简证书及浅层提升核验；旧180／522组核验仍可按ID单独运行。PASS 的证明范围以[注册清单](work/verification_manifest.json)为准，不能代替正文的一般量词或外部定理。其他脚本见 [work 索引](../sources/work/documentation_memory_20260917/originals/work/README.md)。

## 文档维护

当前定理和阅读顺序集中维护，技术附录已按主题移入文件夹，旧文件名保持不变；历史过程归档，不再向两个 README 逐条追加进展。新结果必须区分“完整定理／有限证书／公式核验／探索”，并更新相关依赖与证据边界。

<!-- END SOURCE doc-9552ec88e1c3 -->

---

<a id="doc-4e5ac7f1570b"></a>

## 原文导签：成果与研究索引

来源：`work/documentation_memory_20260917/originals/outputs/README.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/originals/outputs/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-4e5ac7f1570b -->
# 成果与研究索引

2026-09-15整理。当前任务：素数平均证明的整合和改进。先按主题选择入口；旧研究过程已移入同目录的[历史路线账本](history/research_routes_history_20260915.md)，技术附录已实际移入主题文件夹，链接与核验注册同步更新。

## 文件夹地图

```text
outputs/
├─ prime_arity/          素数定理入口、总证明、通用引理
│  ├─ proofs/           lower_band / upper_band / tail_and_lower_bound
│  ├─ tools/            入口、核心与均值格原始工具
│  ├─ structure/        当前证明简化与结构研究
│  ├─ audits/           专项及独立审核
│  ├─ examples/         小素数实例
│  └─ history/          素数研究历史
├─ triple_average/      proofs / arithmetic_cases / history
├─ general_arity/       一般元数、合数与条件性结果
├─ algorithms/          序列、复杂度和测试集
├─ literature/          文献调查
└─ history/             路线账本与阅读日志
```

[素数](../sources/work/documentation_memory_20260917/originals/outputs/prime_arity/README.md) · [三平均](../sources/work/documentation_memory_20260917/originals/outputs/triple_average/README.md) · [一般元数](../sources/work/documentation_memory_20260917/originals/outputs/general_arity/README.md) · [算法](algorithms/README.md) · [文献](literature/README.md) · [历史](history/README.md)。

迁移了220篇文档，旧路径对应新路径可查[完整迁移表](../work/document_reorganization_20260915/path_map.json)。技术脚本和证书仍在work，避免破坏模块导入。没有在outputs根目录留下220个跳转占位文件。

## 素数平均：完整最终阈值

最新证明简化：[三个共轭根与浅层提升](prime_arity/structure/transverse_root_lifting_without_long_orbits.md)。九偏移的奇数n已删除高阶方向／尺度轨道，偶数n只剩至多8个二进修正类；p≥83用统一三连参数公式，保留162组物理计数证书与原两项局部补充。

[主入口](../sources/work/documentation_memory_20260917/originals/outputs/prime_arity/README.md) → [总证明与覆盖表](prime_arity/proof.md) → [通用算术引理](prime_arity/arithmetic_toolkit.md) → [几何解释](prime_arity/geometry.md)。

全部奇素数 p 有 N(p)=2p+1，N(2)=4；阈值以上判据为中心化、本原化后的 G 是 p 幂。两条偶数边界、九个低偏移和全部旧 dₚ 尾部缺口均已完成。不要据旧专题中的阶段状态重新开启这些定理。

最新整理把二进补充所用倍率的扩环正式并入[九偏移第6节](prime_arity/proofs/upper_band/prime_arity_nine_offsets_large_symmetric_carrier_completion.md)。无条件结论仍使用 Morris/Serre，有限参数证书仍是证明的一部分。[本轮阅读、核验与维护记录](prime_arity/verification.md)说明实际核对范围。

## 三平均：独立直接证明和算法

- [双三重值任意维数直接证明](triple_average/proofs/triple_average_all_dimensions_double_triple_invariant.md)：n≥11 的初等主证明，接7、8、9、10元基例得 n≥7；不依赖上述一般算术群证明。
- [二平均原文复核](literature/triple_average_binary_source_reassessment_2026-09-11.md)：直接方法的来源、实际读过的原文和误用边界。
- [序列长度研究](algorithms/triple_average_sequence_length_analysis.md)：区分数值能量界、固定 n 的位长界和未证的可变 n 统一界。
- [算法测试集](algorithms/averaging_algorithm_benchmark.md)：已知可达但可能难于提取路径的输入；搜索失败不代表反例。

旧“17到59的种子／非分裂／仿射／Hecke”研究按[历史路线表](history/research_routes_history_20260915.md)查找。其方法障碍可能仍有意义，素数平均可达性定理本身已不再开放。

## 合数元数：成果保留，另有未解范围

当前交接为[三项任务的完成范围和剩余](general_arity/general_k_three_tasks_progress_20260915.md)。本轮不推进这些任务，不改变用户此前允许采用 GRH 的决定。

| 已有结果 | 条件与入口 |
|---|---|
| 所有平方元数 t² 在 t²+t+1 元完整成立 | [GRH阶段定理](general_arity/general_k_grh_stage_and_remaining_tasks_20260915.md)；充分大参数另有无条件结果 |
| 2、3的全部幂达到最早临界点 | GRH 下；见上述最新交接，不能称为全部后续维数的最终阈值 |
| 任意整数 k≥2 的 2k+1 端点 | [偶元数补齐](general_arity/even_arity_all_endpoints_completion.md)，接已证奇元数结果；无条件 |
| 奇素数幂的全部奇数 2k<n<3k | [奇合数区间与块均值转译](general_arity/odd_composite_coprime_middle_band_completion.md)；无条件 |
| 十平均十六元固定六步网络及推广族 | [固定网络](general_arity/ten_average_sixteen_and_dyadic_network_family.md)；无条件 |
| 任意元数的已知宽尾部 | [一般线性阈值](general_arity/arbitrary_arity_linear_threshold.md)，不等于最优阈值 |

定义 M、H、N 及原猜想的历史来源见[全局状态](general_arity/averaging_global_status_20260912.md)和[合数临界猜想](general_arity/composite_critical_scale_and_conjecture.md)。两篇日期较早，以新交接判断其开放范围。

## 证据与历史

[素数核验说明](prime_arity/verification.md) · [机器依赖图](prime_arity/proof_map.json) · [全项目核验注册](../work/verification_manifest.json) · [此前阅读日志](history/research_reading_log_20260915.md) · [原根 README 历史](../HISTORY.md)。

符号：当前 p 是平均元数，n 是位置数。很多旧 triple_average 文件的 p 是位置数，引用公式前必须检查。

<!-- END SOURCE doc-4e5ac7f1570b -->

---

<a id="doc-2f4ed79ec151"></a>

## 原文导签：一般元数与合数研究

来源：`work/documentation_memory_20260917/originals/outputs/general_arity/README.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/originals/outputs/general_arity/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-2f4ed79ec151 -->
# 一般元数与合数研究

当前交接为general_k_three_tasks_progress_20260915。保留GRH条件与开放范围；本轮只整理，不推进这些定理。

[回到成果索引](../sources/work/documentation_memory_20260917/originals/outputs/README.md)

[当前合数交接](general_k_three_tasks_progress_20260915.md)

- [任意平均元数的线性阈值：非单位差分也是可执行资源](arbitrary_arity_linear_threshold.md)
- [从二平均到任意平均元数：当前全貌与临界猜想](averaging_global_status_20260912.md)
- [从素数完整证明到合数临界问题：策略、可迁移定理与真实困难](averaging_proof_strategy_and_composite_frontier_20260915.md)
- [合数平均：四平均、六平均与原位置副本转译](composite_arity_four_six_transfer.md)
- [合数平均的临界尺度：最早成立、最终阈值与无条件网络](composite_critical_scale_and_conjecture.md)
- [从十五元推广到合数端点：统一CRT证书与两素数完整入口](composite_endpoint_crt_transfer.md)
- [全部偶数元数的2k+1端点：旧种子与统一取逆](even_arity_all_endpoints_completion.md)
- [examples/](examples/README.md)
- [一般k平均的证明计划：先完成核心，再接成全部维数](general_k_averaging_proof_plan_20260915.md)
- [接受GRH后的完整平方族定理与剩余证明任务](general_k_grh_stage_and_remaining_tasks_20260915.md)
- [一般k平均规划评议：平方族入口可直接补齐，尺度任务可以数论化](general_k_plan_review_and_square_entry_20260915.md)
- [对一般k规划建议的复核与采纳](general_k_review_response_20260915.md)
- [GRH主线三项任务：本轮完成范围与当前剩余](general_k_three_tasks_progress_20260915.md)
- [H_t文献调查：已有小生成元理论、无条件充分大结论与全范围边界](ht_literature_and_eventual_square_completion_20260915.md)
- [逆零和定理的原位置转译：碰撞修复与 2p+4 元七步族](inverse_zero_sum_averaging_progress.md)
- [较大素数高奇次幂：两种统一三步正向反射](large_prime_high_odd_power_three_step_reflections.md)
- [奇合数元数的奇余量区间：按真实互素条件迁移旧证明](odd_composite_coprime_middle_band_completion.md)
- [平方元数的统一正向控制器与九平均十三元](square_arity_uniform_controller_and_nine_thirteen.md)
- [十平均十六元与一族确定性三块网络](ten_average_sixteen_and_dyadic_network_family.md)
- [十平均与十二平均17元完整G判据，以及原B公式中的自动维数](ten_twelve_average_seventeen_complete.md)
- [q-平均的根格、\(S\)-算术与控制器猜想](triple_average_q_average_arithmetic_geometry.md)
- [统一四／六阶控制器完成2、3奇次幂临界点](two_three_odd_power_critical_grh_completion.md)

<!-- END SOURCE doc-2f4ed79ec151 -->

---

<a id="doc-5c7475f6cb2b"></a>

## 原文导签：素数平均：当前证明入口

来源：`work/documentation_memory_20260917/originals/outputs/prime_arity/README.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/originals/outputs/prime_arity/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-5c7475f6cb2b -->
# 素数平均：当前证明入口

整理日期：2026-09-15。本目录是素数平均的主入口；本目录下的proofs、tools、structure、audits、examples和history分别保存技术证明、工具、结构、审核、实例与历史。本次整理没有把旧文全部重新独立审核，也没有去掉既有外部定理依赖。

## 1. 已证明的准确结论

一次 **p 平均**是在原 n 个位置中选 p 个，将其值同时替换为均值。设有理输入不全等：减去总均值、清分母、除坐标公因子，得到本原整数零和向量 X。记
\[
G(X)=\gcd_{i<j}|X_i-X_j|.
\]
对每个奇素数 p、每个 n≥2p+1，有限步 p 平均可达全等，当且仅当 G(X) 是 p 的非负整数次幂。最优最终阈值为
\[
N(p)=2p+1\quad(p\ge3),\qquad N(2)=4.
\]
只有 p 不整除 n 时，判据才能简写为 G=1。全等输入无需操作。这里的 N 是“此后所有维数均满足判据”的阈值，不是单个自动全平均网络的最小维数。

**证据边界：**素数定理无条件，引用 Morris 的有限指数定理与有理 S 整数 SL₂ 的强同余子群性质；九个低偏移现只需162组有限反射证书；p≥83由统一三连参数公式承担，入口及基础单位生成已改为书面证明。原522组、180组版本保留作历史对照。一般群词存在已证明，但未给出对可变 p、n 的统一多项式操作长度或通用高效词提取算法。没有对所有低于阈值的输入作完整分类。

## 当前简化

[三个共轭根与浅层提升](structure/transverse_root_lifting_without_long_orbits.md)把奇数n控制层降到Γ(n,R)，偶数n降到Γ(2δn,R)、δ∈{2,4}。奇数n不再需要高阶轨道，偶数n模n以上只需至多8个二进方向／尺度类；统一公式达到p≥83，剩162组及原两项补充。[此前区间构造](structure/carrier_interval_and_unit_descent.md)的入口、容量与基础单位下降继续使用。

[整格拼接与正运输](structure/integral_gluing_and_positive_transport.md)进一步解释同余群和真实逆的来源，给出一般权重整提升判据及等块有限菜单的正运输定理。两个命题有直接证明，未改变当前阈值或剩余证书数。

[局部二次群与轨道缺陷](structure/padic_quadratic_group_and_orbit_defect.md)把旧高层方向循环统一成形式群的首层检验；[Kneser边界](structure/padic_leading_symbols_and_kneser_boundary.md)说明2p+1也是p进首位不交选择图的连通性阈值。二者独立保留结构意义；当前证书数按上面的浅层提升版为准。

[证明附录](proofs/README.md) · [结构研究](structure/README.md) · [审核](audits/README.md) · [实例](examples/README.md) · [历史](history/README.md)。

## 2. 按目的阅读

| 目的 | 阅读顺序 |
|---|---|
| 新 AI 快速接手 | 本页 → [总证明](proof.md)的覆盖表 → [阅读与核验记录](verification.md) |
| 理解证明为何成功 | [总证明](proof.md) → [通用算术引理](arithmetic_toolkit.md) → [几何解释](geometry.md) |
| 严格逐项审核 | 先读通用引理，再按总证明表逐篇读技术附录，最后读三份独立／专项审核 |
| 找可改进之处 | [几何解释第7节](geometry.md#7-整理后真正值得改进的部分)；先确认没有重复已否定的推广 |
| 核对脚本支持什么 | [核验说明](verification.md)及[机器依赖图](proof_map.json)；不要把 PASS 当成全量词证明 |
| 继续合数研究 | [合数交接](../general_arity/general_k_three_tasks_progress_20260915.md)，与本素数定理分开；其中部分结论依赖 GRH |

## 3. 一条完整证明链

\[
\text{合法原输入}
\longrightarrow\text{带位置账本的少块核心}
\longrightarrow\text{真实标量周期与根}
\longrightarrow\text{深主同余群}
\longrightarrow\text{有限方向和单位尺度}
\longrightarrow\text{精确终端}.
\]

这是临界及中间区间的共同结构。远端还可直接用整数安全平均和离散能量下降。两种方法在造零终端处连接，不要求全程使用同一个能量，也不要求整个 SL₂ 都能实现。

必须区分三层：实际平均词、二维有理矩阵、有限模像。每次从后一层返回前一层都需要已证接口。角色可以更换，但位置总数不能增加；换基用于证明，不自动成为操作；共同尺度必须作用于整个核心。

## 4. 防止重复走弯路

- 端点现在不再受六素因子限制；旧文中的入口限制已被三单点交换子替代。
- 偶余量、2p+2、3p−1、3p 之后九个偏移及旧 dₚ 尾部缺口均已有完成证明，见总证明覆盖表。
- 不能从两个已解维数自动插值，也不能把子系统的射影逆当成全系统的逆。
- 模方向满像不等于尺度匹配；最终环必须包括所有实际使用的倍率，包括二进补充。
- Hecke 分支之和、形式逆、双随机运输和复制实现，都不能单独替代原位置正向词。

旧路线及其适用范围保存在[历史路线账本](../history/research_routes_history_20260915.md)。历史“未解”是当时状态，不是当前待办。

## 5. 维护规则

新的完整结论先更新本页与总证明，再更新依赖图和核验注册。新探索放技术附录，不把进展逐条堆到根 README。数学结论、有限证书、公式核验和探索搜索应分别标明。本目录采用“总证明＋可定位技术附录”的结构，尚非一篇不依赖链接的自包含论文。

<!-- END SOURCE doc-5c7475f6cb2b -->

---

<a id="doc-e87de3743047"></a>

## 原文导签：三平均：直接证明与原算术路线

来源：`work/documentation_memory_20260917/originals/outputs/triple_average/README.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/originals/outputs/triple_average/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-e87de3743047 -->
# 三平均：直接证明与原算术路线

proofs为当前直接证明及基例；arithmetic_cases保留旧逐维数算术成果；history为探索、纠错和未完成的更强结构。

[回到成果索引](../sources/work/documentation_memory_20260917/originals/outputs/README.md)

- [arithmetic_cases/](arithmetic_cases/README.md)
- [history/](history/README.md)
- [proofs/](proofs/README.md)

<!-- END SOURCE doc-e87de3743047 -->

---

<a id="doc-2d3d409b320e"></a>

## 原文导签：素数平均的独立 p 进改进研究

来源：`work/documentation_memory_20260917/originals/research/prime_arity_padic/README.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/originals/research/prime_arity_padic/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-2d3d409b320e -->
# 素数平均的独立 p 进改进研究

2026-09-17更新。今后的改进、算法和验证只在本目录记录。原完成证明、主索引和全项目核验注册保持冻结；本目录的阶段结果不能直接覆盖原证明。

**七元视角能否统一全部n≥7：** [根格、局部根基与零目标饱和](triple_all_n_root_lattice_and_target_saturation_20260917.md)给出精确回答。所有维数共享A_(n−1)，G是本原向量的配对理想；危险素数处的障碍恰为零和空间的对角根基。既有全部n≥11双三重直接证明是这个系统的统一正向下降，接7—10基例完成G等价，不依赖合数归约。尚无把七元单一同余群原样推广到全部n的纯群论证明；一般G也不等于能量范数处处为单位，n=11有明确G=1、能量22的可解反例。

**当前按用户要求转到三平均七元：** [G、分歧范数单位与尖点轨道](seven_averaging_cusps_norm_and_eisenstein_20260917.md)以已有七元结构证明为基础，得到完整链G=1 ⇔ Q(√−7)能量范数在7处分歧素理想下为单位 ⇔ Γ₀(7)的尖点0轨道 ⇔真实三平均归零。进一步识别指定物理宏群恰为PGL₂(Z[1/6])中模7上三角子群，证明所有三进局部方向均有可解代表；给出权一theta/Eisenstein及本原能量层的显式系数。七元可达性不是新结果，新增的是精确群识别、范数／尖点／计数的统一及实际归零编译核验。[外部阅读](seven_geometry_literature_20260917/README.md)。五元未解猜想保留，不把转向视作证明它们。

**五元当前状态先读：** [五元成果与剩余问题总结](five_averaging_progress_summary_20260917.md)。逐输入判定、操作序列和最少步数已经完整；全覆盖算术几何描述也已建立。尚未得到一次性G式总判据，D=1的三个单位指数猜想及固定D有限性均未证；分形或超越坐标不构成任意简单条件不可能的证明。总结按成果、边界、外部依赖和下一目标组织，避免把不同研究层次混为一谈。

**全词逃逸方向的新定理：任意固定多块模板统一逃逸。** [证明](five_bounded_templates_uniform_escape_20260917.md)对U₀V₁^a₁U₁⋯V_r^a_rU_r全部独立指数，证明长词D一致趋于无穷；重复块可混合两字母，允许无界切换。ESS将无限固定范数解迫成非负指数射线，实能量与三进谱排除混合增长，纯块增长由有理多项式各向异性排除。固定混合周期另由Baker下界获得有效指数逃逸。全词猜想仍未证：模板本身不断变化时缺统一控制。外部适用性与检查见[文献记录](five_torus_literature_20260917/uniform_escape_review_20260917.md)。

**五元后续：同长度词的二次型类已统一。** [显式间隙界与共同Hecke型](five_explicit_gap_common_hecke_form_20260917.md)证明Q_5∘W全部整数等价于F_f=X²+fXY−f²Y²，f=3^(L+1)；关键是黄金比单位遍历每层3幂本原直线，真实词差别留在终端标记Ce。Aka–Shapira的等分布定理确实适用共同周期，但不能自动控制该标记。另将有界切换升级为无网格的显式字长上界，并用Lucas赋值证明D=1第一段长度v₃(2k+1)+v₃(2k−1)。任意切换的D=1与固定D全分类仍未证。外部读取与版本见[补记](five_torus_literature_20260917/switch_hecke_review_20260917.md)。

**五元最新：有界切换的有效有限性与外部定理接口。** [新证明](five_bounded_switches_and_correspondence_degree_20260917.md)将任意长同方向段归一化；模5标记阻止极限投影消掉种子，Q_5各向异性和实紧致性给|Q_5(We)|≥η_R·9^字长。因此固定D且段数有界时，成功方向有限并有效；不要求词周期。D=1至多两次切换的全长度分类已认证，任意切换仍未证。[外部调查](five_torus_literature_20260917/targeted_review_20260917.md)实际核对六份全文：本题一次分支不满足常见整数点定理的次数要求，交换商对应的等次数投影也不满足多极点CIP假设；取得的Clique Gossiping v1合数必要性被已有六平均九元固定网络反驳，期刊最终版未审。

**五元固定D的定量补充：** [有效稀疏界与固定周期返回](five_fixed_D_effective_sparsity_and_periodic_return_20260917.md)给每个长度L指数区间少于4L^(log_3 2)个成功点，固定D高度≤H计数为O(2^ω(D)(1+log H)^(log_3 2))；固定正词的反复迭代命中指定D仅有限次，混合词由ESS给统一次数界。D=1剩余命题精确为Fibonacci/Pell族，既有有限指数实验与无穷同余排除均不等于全分类。

**五元固定理想与三进大群的新结论：** [单位指数分形与局部群闭包](five_fixed_ideal_unit_exponents_and_padic_group_20260917.md)证明同一完整理想的基本合法点恰为α₀ε^(4k)，其k∈Z₃参数与h∈Z₃等距；每个固定理想上的可解指数零密度，各模3^m允许类恰2^(m+1)−1。两生成元的群闭包恰为PGL₂(Q₃)中det平方类属于{1,−3}的指数二大群，正半群仍零测。核对Baker--Brumer正式转述后，证明统一对数坐标在D=1时为整数、D>1时超越。固定D有限性未证；D=1仅k=0,±1的完整分类仍是猜想，已精确诊断至|k|≤10000。

**环面如何真正约束五元可解性：** [精确分母、相邻互素与同理想局部反例](five_torus_denominators_and_local_separation_20260917.md)证明D=|u²+7uv+v²|/5是最小整环分母；相邻D互素，两兄弟分母gcd恰为gcd(u+v,11)。Pell整数坐标中的物理能量为2|C+D|/3，两个形式前驱共同分母为|2C+5D|/9，选路取决于三进主单位位置。任一成功点乘ε^(4·3^m)可构造同完整理想、任意三进接近但最终失败的点，给出了理想分解加固定精度仍不足的明确定理；不推断任意简单算术判据不可能。

**五元的共同环面与丢番图接口：** [Q(√5)范数一环面上的扭曲平移](five_norm_one_torus_and_twisted_translation_20260917.md)把全部两分支精确写成α↦J(ε^±1α)，J=−(2α+1)/(α+2)、ε=(3+√5)/2。模5合法性是分歧处+1约化；3惰性处J的不良约化产生收缩；交换商变为X²+Y²−3XY+5=0但每步须插入固定坐标对合。已读ESS定理1.1给固定S内相邻边有限，故无限反向分支必须涉及无限多个分裂辅助素数。几何接口是四穿孔有理曲线；m步真实路径恰2^(m−1)个有理分量。仍未将正向环面轨道压成一次性G式判据，亦不将J误称为环面群自同构。

**五元数字与代数对应的新结果：** [普通三进非正则性与单变量有理曲线](five_digit_obstruction_and_rational_correspondence_20260916.md)用孤立点循环节无界证明K的普通三进前缀不能由固定有限状态识别，并推广到任意有理Möbius换坐标；不排除同步整数编码或一般gcd公式。交换商的完整不变量w=(u+v)²/(uv)将两张矩阵合成固定二次对应F(w,z)=0，给有理正规化、奇点和换支范数。该曲线是P¹正规化而非椭圆曲线；Q(sqrt5)换支对称不能冒充真实正向平均。仍未将从0的有限正向轨道压成一次性算术判据。

**五元的完整算术几何分类：** [三进自相似集的有理点定理](five_padic_fractal_rational_points_20260916.md)将全五元可解性刻画为明确三进紧集K的有理点加u+v≡0 mod5；无限Cantor边界的有理点恰为两轴的有限轨道，正被模5排除。另证维数log2/log3、模3^k类数2^(k+1)−1、原始五元整数输入可解比例趋零，以及可解方向实稠密／三进零测。混合周期地址给二次无理数，−11范数族是其中一例。它是完整结构定理，不宣称已得到固定次gcd公式或任意二次点的周期性逆定理。

**奇数下半区与端点的新共同证明：** [一对边界反射统一全部奇数余量](odd_lower_band_boundary_reflection_pencil_20260916.md)对所有奇素数p≥3、全部奇数1≤r<p，用同一对三步位置表取得完整U(R)，再用一张两步反射给L(n)，接深同余与共同终端。r=1不再单独启动，也不用83界或小参数表；旧端点倍率2递推被替代。偶数下半区、3p及上半区尚未由此统一，原114组上半区资源记录未取消。

**统一框架的审计与修正：** [从候选框架到实际分支合并](unified_stable_range_saturation_candidate_20260916.md)撤回“所有退化纤维都必须退出到r=1、2、p”等无位置转换依据的说法。新结果说明改变来源的反射铅笔可以绕开固定纤维的全分类；明确分开已证奇数下半区与偶数／上半区的实际容量障碍。

**从低维结构理解G与阈值：** [有限障碍模与目标可达性](G_as_obstruction_group_and_stable_threshold_20260916.md)定义O_p=坐标R理想／差分R理想，其阶恰为G的非p部分；任意实际平均诱导O_p(新)到O_p(旧)的满射，故障碍只能按整除关系增加。结合已有正运输／复制稳定化与素数总定理，2p+1后恰是稳定算术障碍对原位置到均值完备，G也精确检测每个有限前缀是否还有成功续路。它不宣称任意运输矩阵可原位置分解、不宣称群等于半群，也不把阈值解释当作新的充分性证明。

**全五元的共同算术对象已明确：** [完整受限连分数与level15矩阵序](five_complete_arithmetic_normal_form_20260916.md)把任意输入的十对线性表达式接到唯一受限连分数，覆盖全部五元方向；两个分支的整数代数精确为一个level15 Eichler序，作用于终端的整数模恰为u+v≡0 mod5。与此同时，群轨道乃至序内行列式−3的元素都产生假阳性，且不存在任意次数的共同乘法型齐次范数。尚未把正词／数字条件压成一次性G式判据；不将连分数重写冒充该目标的完成。

**六元显式判据的新突破：** [三重块G=3、四重块赋值及全六元强制后继](six_triple_block_explicit_G3_20260916.md)给无有限证书的一般证明：本原三重核心G=3且无四重值必可解；四重值只查一项模9。三重加二重型的全输入判据恰为a=0或G=3；任意原始G=3六元只需固定20次算术检查。G=1核心的互补出口由一个gcd判定，失败后只剩唯一后继，故已取消六元的分支搜索，但尚未将一般G=1压成一次性公式。旧“六元仅有完整状态搜索”的说明据此更新，不能将本结果扩大成全部六元已获G式判据。

**五元的范数子族：** [判别式−11的显式充要条件](five_quadratic_norm_explicit_slice_20260916.md)证明：本原差值若Q=u²−uv+3v²=5·3^k，可解恰为5|(u+v)且(k=0或3|u)，最少k+1步。它由旧范数恒等式新增一般算术分类；仍不覆盖整个五元逆树。

**阈值以下的新整理与推广：** [p+1至2p的补集动力学](subcritical_complement_dynamics_20260916.md)统一写出r=n−p维的全部实际操作，结合已有不增分母定理给完整整数能量图。在p+2位置上，把旧五元递归推广到所有奇素数p：可解方向组成无碰撞的二叉逆像树，判定及最少步数均可在输入位长多项式时间求出；固定p也存在最短长度任意大的显式族。r≥3的一般范围仅有完整伪多项式算法，其中p=3、r=3现已由上方六元定理进一步取消分支搜索，尚未证明其位长多项式化。这是用户另问的阈值以下结构，不替代2p<n<4p自然统一的主目标。

**直观判据的边界：** [五元、六元与固定同余的限制](five_six_intuitive_criteria_and_modular_limits_20260916.md)给出手算式五元测试，并证明：对任意预定模数M，p+2及2p都有逐项模M相同、G均为1但可解性相反的本原输入。它排除G加固定有限同余的判据，不排除其他简洁数论条件；另说明五元核心不能由有限个实多项式不等式刻画，六元的合法整数贪心有小反例。

**新增独立结构调查：** [有界纤维的二维格几何与内容对偶](global_structure_and_bounded_fiber_geometry_20260916.md)证明：同一非零行列式纤维若已有一张真实可逆基表，其整数凸包为二维时，可行返回自动生成本原步长n/g；一维时由本原线方向精确决定根格。另给实容量宽度的充分条件、内容与伴随的对偶，以及gcd(det A,Q)=1时全部有限对应分支g⁻¹Ax（g整除|det A|）的闭式公式。已取得深核后，这些分支可供应有限单位尺度，无需先使A在全局正向可逆。仍未证明全参数的资源／退化出口存在，不删除原小参数证书；文献范围及有限诊断在报告中分别登记。

## 当前实际进展

| 层次 | 已证明内容 | 尚未完成 |
|---|---|---|
| 深核后的有限群化与不扩环收尾 | 互素行列式的有限对应轨道恰由返回矩阵和行列式素因子尺度生成；共同终端只需初始整数根／深核，后续F_q不再逐个取有理逆、扩环和重建深核 | 初始资源仍须独立证明；行列式与控制模数共享因子的退化对应未被此定理自动覆盖 |
| 同行列式纤维与有限格对应 | 有效根格精确为(n/g)Z；偶4≤r≤2p/5及奇5≤r≤p/5有直接U(n)并接共同终端；非单位返回只需Q|det A|精度，深核可逐边重置精度 | 全部小p/r的纤维资源存在与有限对应终端覆盖未证明；有限图接口不是覆盖本身 |
| 阿代尔格对应与共同端点准备 | 局部内容记录本原化并满足余循环；全1≤r≤p有同一带权数字矩阵，r=1、2接同一两次CRT引理 | 一般带权CRT的真实资源供应、83与小p例外仍未统一消除；端点启动仍引原构造 |
| 旧载体补齐小余量 | p≥83的全部3≤r<r₀用旧对合和统一二进修补接共同终端；r=1原启动也接入；立方根条带已消除 | 两类载体启动仍不同，r=2保留状态相关CRT，3p等块；p<83尚未统一替代 |
| 临界带完整分支合并 | p≥83、r₀≤n−2p<2p且n≠3p，共同反射、根理想、全区间小单位及移动终端接成全输入证明；r₀=4max(3,ceil(cuberoot(p/4))) | 2p旁O(p^(1/3))条带、p<83仍用旧证明；3p接等块运输；保留原深核与零触发 |
| 五返回的一般容量 | 一条守恒n根、两组相邻倍率及互素横向系数统一供应深核；按s的公式替代旧48组，余114组根记录 | 小容量边界仍需改变模板；s>p/2时当前四步模板有严格障碍 |
| 守恒交换直接给n根 | 固定来源、沿总和关系改输出，商自动为U(−n)；在(11,3)直接取得U(36R)，替代模13群生成／提升／分离修补 | 162组一般根计数尚未统一，仍用原深核定理 |
| 分裂乘法与根加法合并 | 全部162组方向由根反射生成；互补混合修正二进位，不用独立direction、模4迹条件、binary_unit、浅群提升或Smith本原准备 | 162组root_pairs、(11,3)辅助13、原深核与基础单位仍保留 |
| 两根直接修正列 | 九偏移不再先提升整个浅主同余群；n奇或4整除n的方向由根反射自动合成，替代116组独立direction用途 | 46组n≡2 mod4的方向条件、根对和原深核仍保留 |
| 整族终端替代尺度补充 | 用两个／四个显式零和终端、一个规范化返回幂和原有下根，替代九偏移45组binary_unit及97/13补充 | 根／方向计数与(11,3)辅助13仍保留；未统一位置供应 |
| 二进表的统一替代 | 三个旧返回的平方、交换子和列提升，统一替代内部偶余量64／256类轨道表 | 九偏移物理计数与根理想证书仍保留 |
| 全参数入口 | 任意k≥2、n≥2k+1安全进入两个k块加剩余单点 | 入口后的统一终止 |
| 偶数载体取逆 | 所有奇素数p、1≤t<p的(p,p,2t)核心具有同一规则的十二步标量闭路 | 根族、共同理想和终端 |
| 最新根构造 | t≡2 mod4时，保持来源、交换一份输出，正向实现L(qR)及两种符号 | 其它t、横向根、整体覆盖 |
| 算术编译 | 已有完整根族和深核后，一次有限环标量同余修正 | 从新宏生成这些前提及高效深核词展开 |

**尚未彻底统一。** 最新旧载体桥接已消除p≥83处的立方根宽度条带：除r=2和r=p外，整个2p<n<4p可共用终端理论；r=1保留原端点倍率启动。仍未合并的是旧／新载体资源启动、2p+2的状态相关准备、3p等块以及p<83。原小参数优化仍有效：内部偶余量64／256类表已有一般替代；九偏移无需独立direction、binary_unit、97/13、浅群提升或Smith本原准备；(11,3)辅助13由守恒n根替代；五返回公式替代162组中的48组，保留114组小参数根记录及(11,3)显式处理。Morris／Serre深核、原入口及零触发仍在。原文件冻结，表中较早阶段的“尚未完成”按后续结果理解。

## 阅读顺序

最新完整收尾简化：[深核只建一次：有限对应群化与不扩环终端](finite_orbit_completion_without_ring_extension.md)。将几何文稿的内容分支接成准确有限群轨道定理，再接全部奇偶n的移动终端。初始深核以后，不再需要普遍有理逆激活、逐数字扩环及重建深核；在p=43二维纤维例中实际接通。终端算法本身无83限制，但初始物理供应及坏行列式对应仍未全参数统一。

最新：[同行列式纤维、直接根与有限格对应](determinant_fibers_and_finite_lattice_correspondences.md)。只让基返回可逆，其他输出保持行列式即可；完整整数移动商为(n/g)Z。固定来源给偶4≤r≤2p/5及奇5≤r≤p/5的共同直接根并完成收尾，r=4无需原二进修补。另将非单位行列式纳入有限对应：本原内容整除行列式，每步由深核重置有限精度。尚未证明这个更宽接口对所有小参数自动覆盖终端。

旧路线复盘：[Burau辫子群当前是否可用](burau_route_reassessment.md)。原几何幂链的中心／正向逆定理与非零均值修正仍有效，后续已证全GL的Zariski闭包但未证算术指数／终端。p平均的最短三块幂链需p²+p+1>4p；临界带两块单载体的旧六项周期只在p=3保留，p≥5变为双曲型。建议复用中心、仿射格与低秩缺陷，不直接重启高秩算术性主线。

小参数闭合的当前判断：[格指数、退化纤维与闭合目标](small_parameters_lattice_defects_and_closure_target.md)。块和／差格指数为奇r的2r、偶r的r/2；共同危险缺陷至多在2处。相邻新载体模板在r=1、2没有所需对，r=4有强制非本原来源／根系数；有限小p诊断显示83主要是选参界，但尚未用全参数纤维结构定理替代小p证书。列出真正需要证明的跨格准备及终止接口，避免把新语言当成已完成统一。

最新结构与端点合并：[阿代尔本原直线、格对应与共同两次CRT](adelic_primitive_lines_and_common_endpoint_preparation.md)。固定可逆群遗漏了按状态改变格及本原化的自由度；局部内容κ记录这种变化并满足余循环公式。全部1≤r≤p的保旧载体返回统一为带权M_q；其参数m=(2p+r)/r在素数p时恰于r=1、2、p为整数。两端点现有资源接同一个一般CRT准备引理。对象和端点准备已合并，但83及全参数位置资源供应没有因此自动解决。

最新：[立方根缺口的来源、旧载体桥接与端点经验](retained_carrier_bridge_and_endpoint_lessons.md)。解释p^(1/3)是相邻来源模板的容量限制，并将旧对合、载体奇因子反演和一般化的迹2修补接入共同终端，完整处理全部3≤r<r₀。端点分别揭示互补倍率递推和状态相关CRT，不能强行视为同一个相邻反射模板。

最新完整合并：[跨过3p的共同控制与终端证明](critical_band_common_controller.md)。对素数p≥83，令r₀=4max(3,ceil(cuberoot(p/4)))，覆盖r₀≤r=n−2p<2p、r≠p：整个上半带和大部分下半带共用反射、根理想、全区间小单位引理与移动终端族；未统一的下端条带缩到O(p^(1/3))。来源组数为一或二，计数用四种容量选择；p<83仍保留原证明，3p接等块运输，宽尾部不重做。这次已接完整入口到归零，超出单独可逆资源或根供应。

最新跨段结果：[共同形状、整数关系与主流结构](common_shape_integer_relations_and_mainstream_structure.md)。两次安全平均将(2p,p,s)改成(p,p,p+s)的规则现已覆盖全部1≤s<p，故整个2p<n<4p可使用共同双p块形状（3p保留正确本原格）。固定来源的全部迹零输出由两个整数移动生成，其中一个作用为零，另一个使平方标量等差改变αn；给出至多两个精确容量区间，并核对Graver同号分解能处理的部分及其边界。它统一入口形状与一类返回的来源，未统一全区间核内终止。

当前研究优先级：[全局复盘第13节](structural_reassessment_and_uniform_dyadic_orbits.md#13-研究优先级修正尾部初等化不是整体统一的替代品)。保留原完整4p尾部，集中合并2p<n<4p的完整分支。尾部初等化、统一取逆或减少局部记录，均不能单独算作这个目标的完成。

备用尾部接口：[n≥4p的见证预算与双重值恢复](four_p_tail_optimization.md)。整个尾部的能量路线只剩低总重数、不同余的双重值恢复需要改进；动态预算可替换逐素数预留的粗界，但CRT构造证明固定两个完整块的余池策略确实不能覆盖旧缺口。尚未证明新的整数闭包，也没有证明它能统一2p之后的临界带。

本次全局判断先读[结构复盘第11—12节](structural_reassessment_and_uniform_dyadic_orbits.md#11-再次全局复盘不应继续围着九个偏移优化)：九偏移是旧证明拼接的遗留范围；新五返回充分界对s≥3恰为21ceil(s/2)，不能覆盖整个3p至4p。第12节进一步证明：即使把相同来源组数从两组增加到三组，同一迹零加守恒交换模板仍在整族n=(7p+1)/2上失败。下一验收应是合并完整覆盖分支，不再只缩小有限证书清单。原n≥3p的全输入定理已完成，此处讨论统一证明的缺口。

最新：[五条返回的统一根供应](conservation_capacity_and_five_return_supply.md)。对可变s给明确整数区间与容量不等式，一条直接n根即可供两种横向系数共用；九偏移的48组替代由一般定理承担。第7节证明s>p/2时当前单次守恒模板确实不可行。

最新：[守恒交换直接产生n根](conservation_exchange_removes_auxiliary13.md)。式Δ=(3i−p,3j−p,3k−r,n−3p)来自总和守恒；在(11,3)把原输出(2,5,1,3)改成(3,0,2,6)，直接得到U(−36)，接两条横向反射与统一收尾，替代辅助13整段特殊群论。

最新：[两块的分裂环面](split_torus_completes_all_directions.md)。旧互补混合在均值／块差坐标中是对角乘法，一个安全小数字覆盖二进单位；旧根反射提供所有奇数部分的加法。第2节给全参数小数字存在性，第4—7节接完整本原列输送，第9节列出依赖消减范围。

最新：[只提升当前列](two_root_column_completion.md)。根对经Bezout自动生成方向；两个根在目标列上的二维作用处理全部奇数部分，规范化循环处理二进部分，直接接原深核纤维。它替代完整九偏移终端接口，精确记录116组与46组的区别。

最新实质简化：[让终端吸收尺度](terminal_fan_replaces_dyadic_units.md)。第1节直接给零和终端，第3节处理本原化，第4—5节给统一二进加法与完整收尾；第6节精确列出可替代与仍保留的依赖。

优先读[整体结构复盘与统一二进列提升](structural_reassessment_and_uniform_dyadic_orbits.md)：区别物理资源证书与有限列覆盖；第4—5节是替代两张二进表的一般证明及其与旧证明的衔接，第7节记录核验。

第10节新增本地复杂性评估：区分已有机制、人工分支、有限证书及尚未理解的位置供应；记录162组证书的准确组成，并明确下次统一工作的验收应是替代整族证书或合并完整覆盖分支。

1. [保持来源、交换输出](output_exchange_produces_roots.md)：最新实质结果；输出差分直接产生真实剪切。含固定模板为何不能自动覆盖其它t的证明。
2. [全部偶数载体一致取逆](uniform_even_carrier_inverse.md)：根构造依赖的统一真实逆。
3. [载体更新正常形](carrier_refresh_normal_form.md)：同一来源与输出计数的完整矩阵。
4. [从局部证明提取整体主线](local_proofs_to_global_balance.md)：哪些成功构造可以复用。
5. [通用移动—合并入口](move_witnesses_then_merge.md)与[单载体格位移](carrier_balance_and_uniform_mechanism.md)：入口规则及不能只靠单载体取逆的全称障碍。
6. [平方零编译](square_zero_hensel_compiler.md)与[实现](square_zero_compiler.py)：以已有真实根和深核为前提的算术算法。
7. [统一计数公式](uniform_reflection_formula.md)与[证书解剖](certificate_anatomy_and_odd_offsets.md)：现有p≥83公式及仍未被替代的物理、理想和尺度条件。

## 本轮证据

[容量公式核验](conservation_capacity_verification.json)含五返回的位置重放、48组新公式替代及完整终端接口；[114组剩余清单](conservation_remaining_root_cases.json)保留尚未被通式覆盖的根数据，不是另行宣称独立完整证明。

[守恒交换核验](equal_determinant_root_repair_verification.json)重放正负U(36)、原来源和输出容量及标量闭路，共132个原子；含48次接终端输送。未用模13群计算，通用守恒关系与深核引用边界在正文中证明／说明。

[分裂乘法核验](split_torus_column_verification.json)在只保留p、s、root_pairs的输入上完成162组、2592次输送；43组不满足旧迹条件仍成功。另有360次大参数输送、682次原位置混合／终端平均，以及同一GL₂(R)环的分母检查。通用结论由正文证明承担。

[两根列输送核验](two_root_column_completion_verification.json)覆盖162组上的1944次输送，116组未使用direction，另46组保留；不调用浅层群提升或binary_unit。含270次大参数输送、322次原位置终端及12组本原准备，原256份冻结文件不变。

[终端族核验](terminal_fan_verification.json)检查全部90组偶数参数上的2160次输送，200次大参数公式输送、300次原位置零和终端以及规范化循环和本原准备实例。未使用binary_unit字段或97/13补充，通用结论由正文恒等式、Smith—CRT和终端证明承担。

[二进列提升核验](uniform_dyadic_column_lifting_verification.json)通过4096类模8公式、原64／256类上的3840次确定性输送，以及384次保留奇数部分尺度的混合模数输送。一般结论由恒等式和逐层归纳证明；没有搜索平均词或枚举群轨道。原256份冻结文件未改动。

[输出交换核验](output_exchange_roots_verification.json)记录66项一般根／仿射恒等式、110对参数上660条正负根的十二步原位置重放，共7920步。全参数结论由正文公式证明，有限检查不替代量词。

[全偶载体核验](uniform_even_carrier_inverse_verification.json)、[对称重建核验](symmetric_rebuild_verification.json)、[通用入口核验](carrier_balance_verification.json)和[平方零核验](verification_results.json)保留各阶段的准确范围。已冻结的256份文件按existing_documents_snapshot.json核对，未修改原证明或注册。

本轮未运行平均词或有限轨道搜索。回读了载体更新、全偶闭路、旧两类对合与相邻倍率根公式。此前把证书称为“运输半群的整数空洞／正规性”没有证明依据，已明确撤回；只使用有原位置计数的具体整数移动。

原项目入口仅作只读来源：[完成证明](../sources/work/documentation_memory_20260917/originals/outputs/prime_arity/README.md)。

<!-- END SOURCE doc-2d3d409b320e -->

---

<a id="doc-887da36dd1e8"></a>

## 原文导签：`work/` 使用说明

来源：`work/documentation_memory_20260917/originals/work/README.md` · [逐字节原样副本](../sources/work/documentation_memory_20260917/originals/work/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-887da36dd1e8 -->
# `work/` 使用说明

**当前素数证明简化：**`python work/run_verifications.py --profile prime-proof`运行18项当前核验，采用[三个共轭根与浅层提升](../outputs/prime_arity/structure/transverse_root_lifting_without_long_orbits.md)的162组反射证书。全部p≥83由三连参数公式承担；奇数n不再计算高阶方向与主单位轨道，偶数n只剩至多8个二进修正类。原180／522组证书保留作历史对照。文档已按主题迁移，见[文件夹地图](../sources/work/documentation_memory_20260917/originals/outputs/README.md)。以下为脚本历史记录，不作为当前未解列表。

无条件端点入口核验：unrestricted-endpoint-entry，对应[完整端点及全部奇数下半带](../outputs/prime_arity/proofs/lower_band/prime_arity_unrestricted_endpoint_and_odd_band.md)。79组有理交换子、1965组有限模正向编译、28条逐位置入口和16条完整核心归约均通过；另以压缩账本跨过七素因子覆盖例及旧r<omega(n)入口缺口。程序不搜索平均词，不展开巨大群论归零尾部；完整定理由新入口与已有核心证明连接承担。

内部偶余量核验：even-interior-completion，对应[内部偶余量完整证明](../outputs/prime_arity/proofs/lower_band/prime_arity_even_interior_completion.md)。65组奇半核代数、110组全部内部参数、9200个单位类、520个终端输送、64类r=4二进制状态、256类r=p-3状态和48条边界输送通过。完整证明保留Morris/Serre依赖，并不覆盖r=2或r=p-1。

缺口复查核验：core-gap-four-lifts，对应[常高度乘法与有限例外](../outputs/prime_arity/history/prime_arity_core_gap_reassessment_20260915.md)。约一秒验证精确四lift判据、无限失败锥、两种逃逸、前缀约分、终端分母以及任意奇p的小分母完整算法。Furstenberg拓扑定理及其有限例外推论由文档明确引用和证明，程序不代替外部定理，也不证明一般阈值。

完整邻点算法：two-prime-neighbour-complete，对应[统一文稿第11节](../outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)。验证所有奇p>=5且omega(p+1)<=2时n=2p+2的严格整数下降，输出包含完整原位置归零路径；五平均12元因此完成。多奇素因子情形、其他偶余量不由本条目覆盖。

七平均最优阈值核验：seven-average-sharp-completion，对应[完整证明](../outputs/prime_arity/examples/seven_average_sharp_threshold_complete.md)。固定正向循环和有限证书补齐20、22元，接旧维数得到N(7)=15；程序保留22元有限单位像的两个尺度类。证书数据为seven_average_sharp_completion_records.json，未展开任意主同余矩阵的全长平均词。

统一中间带入口核验为 uniform-two-block-entry，对应[统一证明文稿](../outputs/prime_arity/tools/prime_arity_unified_weighted_core_theorem.md)及verify_uniform_two_block_entry.py。它验证不带旧周期/gcd条件的两轮入口，并检查两带公共格、返回及终端公式；不证明一般偶数核内终止。完整有限方向模型须保留R单位像，不能直接用普通有限射影线替代。

当前研究状态及已尝试路线先见 [研究索引](../sources/work/documentation_memory_20260917/originals/outputs/README.md)。以下保留核验程序的历史说明，其中旧的未解维数、入口范围和“下一步”须结合索引及后续专题确认；不能据旧说明重开已经完成或已排除的任务。

全局数学状态见 `outputs/general_arity/averaging_global_status_20260912.md`：按固定维数判据、自动G、非自动G边缘H和最终阈值N四类量词整理，避免把无条件网络点误当作G等价结果。

十平均与十二平均17元入口是 `ten-twelve-seventeen-complete`，对应 `outputs/general_arity/ten_twelve_average_seventeen_complete.md` 与 `verify_ten_twelve_average_seventeen.py`；均得到G=1充要，H(10)=H(12)=17。程序保存6条完整路径及q<=200自动B表。两个17元控制器使用不同的Delta(5)/Delta(3)局部激活，不能将一种平均元数的矩阵词混用于另一种。

外部Arena三平均网页的审阅独立放在 `arena_triple_solver_review/`，对应 `outputs/algorithms/arena_triple_solver_review.md`；核验ID `arena-triple-solver-review`。48个同题比较、预热计时、源码SHA256、数值尺度反例和所有成功索引均保存。快速核验只重放已有证据，不重新访问网页或运行长搜索；本任务不修改数学构造算法。

`work/` 保存研究计算的完整历史，因此仍是平铺目录。为保留旧文档引用，本次没有移动或重命名文件。新接手者不应通过文件名前缀猜测数学结论，而应从 `verification_manifest.json` 查找结论到程序的明确对应关系。

合数端点统一核验入口 `composite-endpoint-transfer` 对应 `outputs/general_arity/composite_endpoint_crt_transfer.md`。`composite_endpoint_pivot_certificates.json` 存36个模数的全部32112条回路；`verify_composite_endpoint_transfer.py` 独立检查，不导入构造器或主元搜索。28个两素因子模数得到完整输入判据，另8个仅核心覆盖；结果明确保存在 `composite_endpoint_transfer_results.json`。`build_composite_endpoint_certificates.py` 和 `explore_composite_endpoint_transversals.py` 负责有限证书生成，失败不等于不可达。无限两素数入口已证明；任意level的群包含及多素数入口仍是不同问题。

最新入口 `seven-average-fifteen-complete` 对应 `outputs/prime_arity/examples/seven_average_fifteen_complete.md` 与 `verify_seven_average_fifteen_complete.py`。使用已证七平均端点种子，新增两素数三步入口和模15的完整24陪集、72回路编译，严格证明G=1充要及H(7)=15。`seven_average_fifteen_witnesses.json` 保存7条完整路径与72个特殊入口输入。用户取消的六平均十一元探索文件保留但不继续推进，也不登记为完整定理；后续按平均元数增加研究，8平均13元已证，下一候选为9平均13元。

最新非自动G判据入口为 `six-average-ten-complete`，对应 `outputs/general_arity/examples/six_average_ten_complete.md` 与 `verify_six_average_ten_complete.py`。它完整覆盖G1和G2、排除G5和G10，严格给出H(6)=10。`six_average_ten_witnesses.json` 保存6条完整路径；`explore_six_average_ten_macros.py` 及其发现表只作溯源，正式核验不导入。新的两步R返回、实际尺度周期和模5交换子全部明确实现，不能把Sigma当成免费交换不等块。

当前合数临界线入口为 `composite-critical-scale` 与 `eight-average-thirteen-complete`，共同对应 `outputs/general_arity/composite_critical_scale_and_conjecture.md`。前者核验局部素数幂平方根尺度的反例下界和连续整数乘积的固定四步网络；后者完成八平均13元并结合下界证明其为排除n=q后的最早成功维数。`composite_critical_scale_results.json` 保存下界表和网络，`eight_average_thirteen_witnesses.json` 保存5条完整路径。`explore_composite_minimal_core_periods.py` 仅记录短周期发现，预算未命中无不可达含义；正式核验不导入它。M最早成功与N最终阈值必须区分。

任意平均元数的充分大维数统一入口是 `arbitrary-arity-linear-threshold`，对应 `verify_arbitrary_arity_linear_threshold.py` 与同名证明文档；保存70条一般路径和24条造零收尾路径。四平均九元的完整入口是 `four-average-nine-complete`，对应 `verify_four_average_nine_complete.py` 与 `outputs/general_arity/examples/four_average_nine_complete.md`；保存6条经真实尺度重放的原位置路径。两者都没有平均词发现搜索，均由正文证明全称结论。

四平均七元的精确入口是 `four-average-seven-complete`，对应 `verify_four_average_seven_complete.py` 与 `outputs/general_arity/examples/four_average_seven_complete.md`；它用 (4,2,1) 加权核心和模7陪集控制器证明七元本身的完整判据，保存12条完整路径。

六平均九元独立入口是 `six-average-nine-fixed-network`，对应 `verify_six_average_nine_fixed_network.py`：只用标准库核对固定四步矩阵、全部756个二步后继行和160个有理输入，证明四步为固定全输入网络的最优长度。四平均七元的Sigma由真实C²B词实现，不能免费交换不等大小块；其文档明确区分实际周期尺度与射影等式。两个入口均不证明整体N(4)=7或N(6)=9。

合数平均入口是 `composite-four-six-transfer`。`verify_composite_arity_transfer.py` 对应 `outputs/general_arity/composite_arity_four_six_transfer.md`，核验偶数元数半块转译、四平均偶数维数和六平均三的倍数维数；生成的 `composite_arity_transfer_witnesses.json` 保存336条原始输入与1基完整序列。商层调用已有二平均HTML，最终Fraction重放只信任原输入和操作索引。全称证明在文档；未解决维数不能据此标为不可达。

## 统一入口

从项目根目录运行：

```text
python work/run_verifications.py --list
python work/run_verifications.py --profile smoke
python work/run_verifications.py --profile core
python work/run_verifications.py --id n13-complete
```

运行器会检查清单结构、引用文件是否存在、程序退出码和预期输出标记。这里的 `PASS` 只表示该程序重现了清单声明的计算结果；它的数学效力不能超出同一条目的 `evidence_scope`。

`reynolds-hodge-structure` 核对原子Reynolds恒等式、完整生成代数及危险素数处的Hodge／Fricke边界；`contingency-layer-semigroup` 实际重放运输表层及交数秩，给出无需子问题调用的有限半群模型。其终端覆盖没有被宣称已证。

`final-hecke-manin-audit`是当前Hecke路线入口：核对整数幺模共轭、第二算子的共同正定星结构障碍、三角方向、普通Manin中心负号及两个位置／卷积模型的区别。旧`iwahori-hecke-modular-interface`的ID保留，但只核对有限代数恒等式；局部特征线并非已识别的自守分量，数字置换和也并非已实现的T_3。旧推导存档与纠正见`outputs/triple_average/history/triple_average_final_hecke_audit.md`。

`explore_nonsplit_hecke_charts.py`检查非分裂Reynolds的一至三层B_p chart返回；`explore_bcore_atomic_hecke_walls.py`按二维系数类型和重数穷尽短原子词中的非标准Hecke墙。二者都是有界阴性诊断，不排除直接终端或带子问题的长gallery。

`explore_bcore_symbolic_terminal_cover.py`把整个B_p(1,v)参数族保留为二维整数系数，一棵状态树同时求出所有整数v终端超平面。登记的B71窗口覆盖是有限探索证据；大窗口显示固定深度语言稀疏，不能外推为统一六步定理。

2026-09-11的载体路线复盘见`outputs/triple_average/history/triple_average_route_reassessment_2026-09-11.md`。`explore_equal_carrier_*`检查等载体有限域轨道、正向协向量、B核特殊族与固定中心收缩同步；`explore_bcore_zero_triple.py`用整数值--重数状态寻找真实零和三元组，`explore_bcore_zero_triple_greedy.py`比较局部贪心规则。这些`explore_*`文件都是有限诊断；其中一次具体等载体搜索的共同尺度错误已在脚本和复盘中明确修正，旧输出不得引用。

`n47-complete` 完成47元：固定尖点词和校正伸缩、18个Schreier回路正向消元、48陪集及独立标签、全部合法方向输送。`localized-iwahori-generation` 核对任意素数的标准根／单位生成接口和通用奇次三进尖点恒等式，实际资源的普遍正向实现仍开放。发现工具 `explore_b47_schreier_roots.py` 只负责定向找词，不是正式核验入口。

`b47-root-activation` 独立检查固定 `b47_root_activation_certificate.json`，三层46/113/2激活全部167旧宏的逆，连同种子共170节点；核验不导入发现工具 `explore_b47_root_activation.py`。另检查57模板正向共轭词及两个完整相对根群。它单独不承担47元完整判据，后续n47-complete补齐。

`b47-extra-atom-involutions` 固定三个新extra-stage模板及47Z[1/6]平移；`adjoint-return-domain-audit` 检查倒序投影是否真的满足普遍调用域。共享 `verify_bn_integer_templates.py` 的extra字段可选，旧输入沿用两阶段流程。两个搜索文件的阴性结果仅限记录的模板范围，不是不可达证明。

`projective-spectral-balance` 包含任意秩给定矩阵的精确Ad分圆算法。`b47-short-cycle-boundary`（仅full）使用NumPy整数数组作无遗漏模筛选，完整整数复核全部幸存者；`search_four_factor_cycles.py` 是单独的浮点发现工具，阴性结果没有证明效力。

`paired-carrier-two-adic-reset` 核验原维数的等值载体二进宏、两个R理想的精确共同缩放，以及受限宏库的周期障碍；构造有效不等于它已有正向逆。全部操作用真实原位置系数重放。

`n41-complete` 固定21宏、10个三因子对合和10个整数词，正式核验不运行发现搜索。`explore_integral_cycle_closure.py` 使用行列式平方类和两字母状态作有界发现；`modular-primitive-height-barrier` 则重放有限模调度中实能量下降而本原高度指数增长的精确族。

`two-carrier-modular-bridge` 核验一般n=5 mod6的正向降维接口。有限模逆由正向幂实际重放；大子问题只在明确同余域调用，并再次检查全局G。一般群论控制的存在性在正文，脚本未实现大维数任意输入的完整词求解器。

`n29-complete` 是冻结旧子问题库上的独立29元证书，不运行发现搜索。`search_bn_three_cycle.py` 用浮点提出候选并精确复核，阴性输出没有不存在证明效力。`--expanded-first` 只扩充探索用首步大小，不改变默认库。非分裂射影层的有限精确边界登记为 `nonsplit-projective-layer-boundary`。

`split-prime-gaussian-controller` 核验原位置数的高斯周期正向控制器，对应全部p=1 mod3的统一证明。`explore_gaussian_period_layers.py` 同时提供构造辅助函数，不是通过有限素数表宣称全称结论。当前solved_size包含该无限素数族的因子闭包。

新增 `one-tripling-stabilization` 对应一次三份复制、整数仿射轨道及所有三整除维数定理；包含87元接口，但不证明29元。`compile_bn_integer_templates.py` 的 `certificate_size` 保留旧证书库，`solved_size` 才使用新增维数，避免历史证书的矩阵数量随库增长而变化。

`balanced-digit-congruence-group` 核验副本数字库的完整整数同余群生成接口。`b29-current-cycle-boundary` 核验当前B29库的二因子周期排除及全部指数A^jB的精确迹方程；它不运行不断增长的词搜索。

`flat-star-formal-arithmeticity` 核验原维数形式群的显式幺幂和第一层局部接口，有限指数证明另使用已声明的标准初等同余群定理。`cyclotomic-level-entanglement` 建立旧21504容器的43008状态耦合二重覆盖；旧自动机的标签没有改号，旧终端缓存不视为新容器证书。

三档用途如下：

- `smoke`：最新关键结构和九十一元同余容器，通常少于 10 秒。
- `core`：已完成基维数证书和主要一般归约，通常约 1 至 2 分钟。
- `full`：清单中的全部项目，包括九十一元深度四、cusp 29 深度五和新增四维数核实验。长搜索集中于 cusp 29 与 B21；不保证固定总时长。

## 证据等级

- `theorem-certificate`：精确有限证书，闭合证明中明确陈述的有限子问题。一般归约仍需阅读对应证明文档。
- `symbolic-check`：用精确整数或有理数检查恒等式、真实宏和有限参数实例。
- `finite-sanity`：有限穷举或固定随机种子的有界实验，用于防止公式和实现错误，不能承担无限量词。
- `exploratory-search`：有限深度或有限高度搜索。没有找到见证不等于不可达证明。

## 历史文件前缀

- `verify_*`：作者当时用于核对某个公式或证书；强度可能属于上述任一等级。
- `check_*`：局部一次性核对，通常没有稳定输出契约。
- `search_*`、`explore_*`、`analyze_*`：搜索、数据生成或诊断，默认不能引用为完整证明。
- 其他 `.py` / `.js`：共享辅助模块、数据整理或早期实验。
- `.pickle`：历史搜索缓存，不是独立证书。
- `__pycache__/`：运行产物，可忽略。

新增或修改一项可引用的计算结论时，应同时更新：

1. 对应数学文档中的结论和证明边界；
2. `verification_manifest.json` 的命令、输出标记、证据等级和运行时间；
3. 必要时更新 `outputs/algorithms/triple_average_verification_guide.md` 的人工索引。

有限搜索必须记录全部参数，例如深度、模数、输入界、覆盖数和未覆盖数。九十一元脚本默认深度 2，得到 `14/24`；深度 3 得到 `20/24`；深度 4 得到 `23/24`；定向深度 5 搜索 cusp 29 得到最后一条证书，容器内有限深度覆盖为 `24/24`。脚本默认使用全部逻辑处理器，也可用 `--jobs 1` 做串行对照。

<!-- END SOURCE doc-887da36dd1e8 -->

---

<a id="doc-9700466383d0"></a>

## 原文导签：H_t文献来源与访问等级

来源：`work/ht_literature_20260915/source_index.md` · [逐字节原样副本](../sources/work/ht_literature_20260915/source_index.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-9700466383d0 -->
# H_t文献来源与访问等级

检索日期：2026-09-15。研究结论见[报告](../sources/outputs/general_arity/ht_literature_and_eventual_square_completion_20260915.md)。*_source.json记录原URL、最终URL、时间、状态、文件长度和SHA256；失败也保留。

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

<!-- END SOURCE doc-9700466383d0 -->

---

<a id="doc-17e5e0f397d9"></a>

## 原文导签：Literature retrieval, 2026-09-12

来源：`work/literature_20260912/README.md` · [逐字节原样副本](../sources/work/literature_20260912/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-17e5e0f397d9 -->
# Literature retrieval, 2026-09-12

The dated survey is `../../outputs/literature/averaging_literature_survey_2018_2026.md`.
`../literature_survey_20260912.py` retrieves public metadata and pages with a
content cache. JSON filenames are hashes of request URLs and parameters; each
record preserves the final URL, HTTP status, retrieval date, and response body.
Text files with hashed names contain parsed page text.

Downloaded primary documents:

- `gonzalez_thesis_2019.pdf` / `.txt`: Miguel Coviello Gonzalez's UC Riverside dissertation, September 2019; https://escholarship.org/uc/item/4wb2g5z2
- `weighted_inverse_2022.pdf` / `.txt`: Adhikari, Hegde, Molla, Sarkar, Integers 22 (2022), A7; https://math.colgate.edu/~integers/w7/w7.pdf
- `splitter_2024.pdf` / `.txt`: Couetoux, Gastaldi, Naves, FUN 2024; https://doi.org/10.4230/LIPIcs.FUN.2024.9

The PDF text was extracted with TeX Live's pdftotext. No network execution,
messages to authors, account sign-in, or access-control changes were performed.

Limits: direct arXiv and Google connections failed; Semantic Scholar later
requests were rate-limited; several publishers exposed only abstracts. OpenAlex
author records and publication versions had merge errors. Bibliographic matches
were checked against publisher or author records where available. Citation
counts and absence of search hits do not prove that a result is absent from the
literature. The survey distinguishes primary-text reading from abstract-only
inspection and does not integrate unreviewed external algorithms into solvers.

<!-- END SOURCE doc-17e5e0f397d9 -->

---

<a id="doc-92dd4f085969"></a>

## 原文导签：2026-09-14研究审查材料

来源：`work/research_audit_20260914/README.md` · [逐字节原样副本](../sources/work/research_audit_20260914/README.md)

本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。

**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。
<!-- BEGIN SOURCE doc-92dd4f085969 -->
# 2026-09-14研究审查材料

## 2026-09-15 强CSP专项补核

新增取得Prasad--Rapinchuk正式出版综述 *Developments on the congruence subgroup problem after the work of Bass, Milnor and Serre*, Collected Papers of John Milnor, Vol.V, AMS,2010,307-325。

- [19页重印PDF](../sources/work/research_audit_20260914/prasad_rapinchuk_milnor_survey_2010.pdf)、[提取文本](../sources/work/research_audit_20260914/prasad_rapinchuk_milnor_survey_2010.txt)、[第309页图像](../sources/work/research_audit_20260914/prasad_rapinchuk_survey_page309.png)。已读取第2.1至2.3节、命题1、第4节定理3的相关陈述及参考文献[49]，并查看第309页原图。
- [作者题录](https://uva.theopenscholar.com/andrei-rapinchuk/publications/developments-congruence-subgroup-problem-after-work-bass-milnor-and)直接链接[重印文件](https://uva.theopenscholar.com/files/ixqrlw/files/milnor_survey_8.pdf)。实际下载为application/pdf，571108字节；SHA256：`CA19042C85BDF4E7E3E62F7ED66BD81E6CEC33456F65902715E472E7C9B140A1`。
- 第309页第2.3节明确给出SL2在|S|>1且S含非复数处时同余核平凡；同页命题1和第308页经典CSP定义给出每个有限指数子群包含主同余子群。第324页[49]对应Serre 1970。
- 对R=Z[1/q]、q>1，S包括实无穷处与至少一个有限素数处，因而适用。此来源同时支持奇素数局部化环，不局限于Z[1/2]。
- Serre 1970原文仍未全文取得：Annals官方题录页仅提供DOI，JSTOR请求返回HTML；arXiv访问连接重置。未将这些失败请求计作论文全文。成功取得的是上述作者提供的正式综述。

适用性与区间证明的完整审核见[专项报告](../sources/outputs/prime_arity/audits/prime_arity_lower_band_external_theorems_audit_20260915.md)。下面保留9月14日原始访问范围，勿将旧的“仅二进交叉支持”当作补核后的全部证据。

本次先复查双锚点碰撞、不同值归约、单位补回、精度反例、端点主元与CRT证书。实质推进发生在端点受限群生成：找到Morris 2007的有限指数子群内部生成定理，与Serre同余子群性质及显式有限环消元接通。证明见[合数端点核心闭合](../sources/outputs/prime_arity/proofs/lower_band/prime_arity_endpoint_congruence_completion.md)。

## 实际使用的来源

| 材料 | 核对内容 | 证据边界 |
|---|---|---|
| [Morris 2007 PDF](../sources/work/research_audit_20260914/morris_muni.pdf)、[提取文本](../sources/work/research_audit_20260914/morris_2007.txt) | 定义、定理6.1(2)、5.13、引理6.9及推论6.10；秩二及无限单位条件 | 已读相关原文；没有重新证明Carter-Keller-Paige的深结果 |
| Serre 1970，DOI 10.2307/1970630 | 所用标准特例：SL2(Z[1/2])有限指数子群包含主同余子群 | 原文全文下载未成功；[专家答复原始记录](../sources/work/research_audit_20260914/serre_special_case_crosscheck.json)交叉确认特例；正式证明明确以Serre定理为外部依赖 |
| [Mennicke 2000 PDF](../sources/work/research_audit_20260914/mennicke_2000.pdf)、[文本](../sources/work/research_audit_20260914/mennicke_2000.txt) | 区分直接初等生成与正规闭包，及定理中的阶数>=3前提 | 未把该高阶结果套用于SL2 |
| 原有Morgan-Rapinchuk-Sury 2018缓存 | 整个SL2的9因子定理及参考文献 | 该定理本身不解决本题受限根群；它的参考文献帮助定位Morris原文 |

Morris来源：https://emis.muni.cz/journals/NYJM/j/2007/13-17.pdf 。作者出版列表确认刊名、年份、页码。Morris PDF SHA256：F690AD629791A30284E3E7FF7EDE152B874314D218138CB2A41CEFB24FAB902E。

Mennicke来源：https://journals.msp.org/mscand/article/download/916/915 。PDF SHA256：E2DD023379F87B82DA56BE88F74042FCB1C16EEB5D538CD60B14AF4A7003AC57。

## 检索与未使用材料

通过OpenAlex题录、作者出版页、期刊/EMIS镜像定向查询relative elementary groups、congruence subgroup generators、Mennicke symbols、Farey symbols、Carter-Keller-Paige及相关零和结构。题录命中只作线索，不作为定理证明。

Morris《Introduction to Arithmetic Groups》下载后仅检索了同余与S算术相关部分，未用于新增证明。Milne的AG.pdf实际为《Algebraic Geometry》，已按实际标题更名且未使用。若干所谓PDF地址返回的是HTML跳转页，已改名为redirect.html，不能当作已下载论文。首页、错误跳转和目录页保留为访问记录。

## 核验范围

[核验程序](../sources/work/verify_endpoint_congruence_completion.py)及[结果](../sources/work/endpoint_congruence_completion_records.json)只核查任意商分解公式、平衡单位、陪集归约与既有正向编译接口。完整一般量词由专题证明及其明确外部定理承担。没有平均词发现搜索，没有新增高效任意核心分解算法。

<!-- END SOURCE doc-92dd4f085969 -->
