# Sqrt Decomposition on Queries (Offline) — Mo's Algorithm

**Category:** arrays / advanced

## What it is

**Mo's Algorithm** (a.k.a. *sqrt decomposition on queries* or *query square-root
decomposition*) is an **offline** technique for answering many range queries on a
static array. Instead of answering each query independently, we **read all queries
first, reorder them cleverly, and process them together**, moving two pointers
`curL` and `curR` that mark the current window `[curL, curR]`.

The core idea: if we can maintain the answer for a window while **adding or
removing one element at a time** in `O(f)` each (via `add(i)` / `remove(i)`
operations), then the total cost depends only on *how far the pointers travel*.
By sorting queries so that the pointers move as little as possible, the total
pointer movement is bounded by `O((n + q) * sqrt(n))`.

### The sorting trick

Divide the array of size `n` into blocks of size `B ≈ sqrt(n)`. Sort queries
`(l, r)` by:

1. **block of `l`** = `l / B` (ascending), then
2. **`r`** (ascending — often with even/odd block alternation to shave a constant).

With this ordering:
- The left pointer stays within a block, so across all queries in a block it
  moves `O(B)` per query → `O(q * B)` total.
- The right pointer moves monotonically within each block, so `O(n)` per block ×
  `O(n / B)` blocks → `O(n^2 / B)` total.

Choosing `B = n / sqrt(q)` (or simply `sqrt(n)`) balances these to
**`O((n + q) * sqrt(n) * f)`**, where `f` is the cost of one add/remove.

## When to reach for it

- You have a **static** array and a **large batch of range queries** given up
  front (offline is allowed — no forced online / real-time ordering).
- The query statistic is **not easily decomposable** by a segment tree or prefix
  sums (e.g. "number of distinct values", "number of pairs with XOR = k",
  "mex of occurrence counts"), **but** it *is* cheap to update when a single
  element enters or leaves the window.
- Variants extend it to **trees** (flatten with an Euler tour) and to
  **point updates** (Mo's with modifications / "Mo's on 3 dimensions").

## Complexity

| Quantity | Cost |
|---|---|
| Time (basic) | `O((n + q) * sqrt(n) * f)` where `f` = add/remove cost |
| Time (with updates) | `O(n^(2/3) * q)` typical, using block size `n^(2/3)` |
| Space | `O(n + q)` for the array, frequency table, and stored queries |

`f` is `O(1)` for most classic problems (maintaining a frequency array and a
running answer), so the practical bound is `O((n + q) * sqrt(n))`.

## Limitations

- **Offline only.** You must know all queries before answering any (unless
  combined with heavier machinery).
- Requires an **invertible / incremental** statistic: both `add` *and*
  `remove` must be supported cheaply. Some statistics (e.g. min of a sliding
  window that only shrinks) resist removal.
- Constant factor and the `sqrt(n)` term make it slower than a segment tree when
  the statistic *is* decomposable — use the right tool.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Distinct Elements in Range](problem-01-distinct-elements-in-range/PROBLEM.md) | Vanilla Mo's: count distinct values | Medium |
| 2 | [Powerful Array](problem-02-powerful-array/PROBLEM.md) | Incremental delta update of `Σ Kₛ²·s` | Medium |
| 3 | [XOR and Favorite Number](problem-03-xor-and-favorite-number/PROBLEM.md) | Prefix-XOR reformulation + counting pairs | Hard |
| 4 | [Tree and Queries](problem-04-tree-and-queries/PROBLEM.md) | Mo's on a flattened tree (Euler tour) | Hard |
| 5 | [Machine Learning (Mex of Counts)](problem-05-machine-learning-mex-of-counts/PROBLEM.md) | Mo's with point updates (3D Mo's) | Very Hard |

Work through them in order — each introduces one new twist on top of the vanilla
add/remove template.
