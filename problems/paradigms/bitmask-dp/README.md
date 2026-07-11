# Bitmask DP

**Bitmask DP** (dynamic programming over subsets / bitmask states) encodes a
subset of a small universe of items as the bits of an integer, then runs a DP
whose state includes that integer. If bit `i` of `mask` is set, item `i` is
"in" the set; otherwise it is "out." Because a subset of `n` items maps to an
integer in `[0, 2^n)`, you can index a DP table directly by the mask.

## What it looks like

- **State:** an integer `mask` in `[0, 2^n)` representing which items are
  used / visited / assigned, often combined with a second coordinate such as
  "which item was last used."
- **Transition:** flip one bit on (add an item) or off, using fast bit ops.
- **Answer:** usually read off the full mask `(1 << n) - 1`.

Handy bit tricks you will use constantly:

| Operation | Expression |
|---|---|
| Is item `i` in the set? | `mask & (1 << i)` |
| Add item `i` | `mask \| (1 << i)` |
| Remove item `i` | `mask & ~(1 << i)` |
| Popcount (size of set) | `bin(mask).count("1")` |
| Iterate submasks of `mask` | `s = mask; while s: ...; s = (s - 1) & mask` |
| Lowest set bit | `mask & (-mask)` |

## When to reach for it

Reach for bitmask DP when:

- The number of items is **small** (typically `n <= 20`, sometimes up to ~22),
  because the table has `2^n` entries.
- The natural state of the problem is **"which subset have I already handled"**
  and the order or identity of remaining items matters.
- Greedy or ordinary interval/subsequence DP cannot capture the combinatorial
  dependence between items.

Classic families:

- **Subset-sum / partition** — split items into groups with equal sums.
- **Permutation counting** — count valid orderings/assignments position by position.
- **TSP / Hamiltonian path** — Held-Karp: `dp[mask][last]`.
- **Assignment / matching** — assign tasks to people, hats to people, etc.
- **Profile ("broken profile") DP** — process a grid row by row, where each
  row's chosen cells form a bitmask.

## Typical complexity

- **Time:** `O(2^n * n)` for one-extra-bit transitions, `O(2^n * n^2)` for
  Held-Karp TSP, and `O(3^n)` when you enumerate all submasks of every mask.
- **Space:** `O(2^n)` or `O(2^n * n)` for the DP table (often reducible to two
  rows for row-by-row profile DP).

The exponential factor is the price of admission: bitmask DP is only practical
because `n` is tiny.

## Problems

| # | Problem | Sub-technique | Difficulty |
|---|---------|---------------|------------|
| 1 | [Beautiful Arrangement](problem-01-beautiful-arrangement/PROBLEM.md) | Permutation counting over a mask | Medium |
| 2 | [Partition to K Equal Sum Subsets](problem-02-partition-k-equal-sum-subsets/PROBLEM.md) | Subset-sum / bucket filling | Medium |
| 3 | [Traveling Salesman (Held-Karp)](problem-03-traveling-salesman/PROBLEM.md) | `dp[mask][last]` Hamiltonian cycle | Hard |
| 4 | [Number of Ways to Wear Different Hats](problem-04-different-hats/PROBLEM.md) | Assignment / matching | Hard |
| 5 | [Maximum Students Taking Exam](problem-05-maximum-students-exam/PROBLEM.md) | Row-by-row profile DP | Hard |
