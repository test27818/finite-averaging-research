# Literature retrieval, 2026-09-12

The dated survey is `../../outputs/averaging_literature_survey_2018_2026.md`.
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
