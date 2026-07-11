# Hirschberg's Algorithm

**Hirschberg's algorithm** (Dan Hirschberg, 1975) computes an optimal alignment
between two sequences — most famously the **Longest Common Subsequence (LCS)** and
**global sequence alignment (Needleman–Wunsch)** — in the *same* `O(n·m)` time as the
classic dynamic-programming table, but using only **`O(min(n, m))` space** instead of
`O(n·m)`.

## The core idea

The classic DP fills an `(n+1) × (m+1)` table and then *backtracks* through it to
recover the actual alignment. The backtrack is why you seem to need the whole table.
Hirschberg removes that need with **divide and conquer**:

1. Computing only the **length/score** of an optimal alignment needs a single rolling
   row — `O(min(n, m))` space (this is the "NW score" or "Needleman–Wunsch score" pass).
2. Split the first string `X` at its midpoint row `i = n/2`.
3. Run the score pass **forward** on `X[:i]` vs `Y`, and **backward** (on reversed
   strings) on `X[i:]` vs `Y`. Each produces one length-`(m+1)` vector.
4. Add the two vectors element-wise. The column `k` that maximises the sum is the
   point where an optimal alignment crosses row `i`. This splits `Y` into `Y[:k]` and
   `Y[k:]`.
5. Recurse on `(X[:i], Y[:k])` and `(X[i:], Y[k:])`, concatenating the results.

Because each level of recursion does `O(n·m)` work but the problem area halves each
time, the total work is still `O(n·m)` (a geometric series `nm + nm/2 + nm/4 + … ≤ 2nm`).
Only `O(min(n, m))` extra memory is ever live, plus `O(log n)` recursion stack.

## When to reach for it

- You need the **actual** aligned sequence / subsequence / edit script, not just its
  length, **and** the strings are large enough that an `O(n·m)` table (e.g. gigabytes
  for two 100k-character genomes) will not fit in memory.
- Bioinformatics (DNA/protein alignment), `diff`-style tools, spell correction, and
  any place the quadratic-space DP would blow the memory budget.

If you only need the *length*, you don't need the full algorithm — just the rolling-row
score pass. Hirschberg's contribution is recovering the alignment itself in linear space.

## Complexity

| Metric | Full DP table | Hirschberg |
|--------|---------------|------------|
| Time   | `O(n·m)`      | `O(n·m)`   |
| Space  | `O(n·m)`      | `O(min(n, m))` (+ `O(log n)` stack) |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [LCS Length in Linear Space](problem-01-lcs-length-linear-space/PROBLEM.md) | Length of the longest common subsequence using one rolling row | Easy |
| 2 | [Reconstruct the LCS String](problem-02-reconstruct-lcs-string/PROBLEM.md) | Recover an actual LCS (not just its length) in `O(min(n,m))` space | Medium |
| 3 | [Edit Distance Operations in Linear Space](problem-03-edit-distance-operations-linear-space/PROBLEM.md) | Recover the min-cost sequence of insert/delete/replace edits in linear space | Medium |
| 4 | [Shortest Common Supersequence](problem-04-shortest-common-supersequence/PROBLEM.md) | Build the shortest string containing both inputs as subsequences | Hard |
| 5 | [Global Sequence Alignment (Needleman–Wunsch)](problem-05-global-sequence-alignment/PROBLEM.md) | Optimal scored alignment with gap/mismatch penalties in linear space | Hard |

Each folder contains `PROBLEM.md` (statement), `solution.py` (empty template to fill
in), and `SOLUTION.md` (answer key with reference implementation).
