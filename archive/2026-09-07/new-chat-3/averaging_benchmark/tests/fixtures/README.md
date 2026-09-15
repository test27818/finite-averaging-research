# Frozen independent regression inputs

- `original_small.jsonl`: pre-migration small split, 224 records; 78 non-null minima.
- `pre_migration_260.json`: 260 additional instances certified in the previous comparison session, copied from `/workspace/upload_solver/random_truth.json` before this migration. Their source is an earlier solver, not the new data release. They were selected for certifiability, so they are NOT an unbiased scalability sample.

Never regenerate these fixtures from the current solver to make a failing test pass.
The new `data/` and its 428 minima are tested for witness validity and manifest hashes,
not treated as an independent proof of this implementation's own optimality.
