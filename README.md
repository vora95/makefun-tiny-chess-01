# Tiny Chess — v_prune1

A 4 KB Python chess engine: alpha-beta (PVS/NegaScout) + transposition table,
null-move pruning, late-move reductions, MVV-LVA captures, killer + history
move ordering, and a hand-tuned piece-square evaluation. Searches to a fixed
node budget (never a clock), so trials replay deterministically.

Entry: `main.py` (3,690 bytes) — LZMA-compressed payload, standard library
only. See `LICENSE` (MIT).
