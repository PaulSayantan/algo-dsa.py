# Square Root Decomposition

## What it is

**Square root decomposition** (a.k.a. "sqrt decomposition" or "block
decomposition") splits an array of `n` elements into contiguous **blocks** of
size `b ≈ sqrt(n)`, giving about `sqrt(n)` blocks. For each block you precompute
and maintain a small **summary** — a sum, a minimum, a sorted copy, a compressed
jump, etc. Element `i` always lives in block `i // b`.

The payoff comes from how any range `[left, right]` decomposes:

- at most **two partial boundary blocks**, which you handle element by element
  (`< 2b` elements), and
- zero or more **whole interior blocks**, which you answer in `O(1)` each using
  their precomputed summary (`< n / b` of them).

Balancing `b` (cost of scanning a partial block) against `n / b` (number of
whole blocks) is minimized at `b = sqrt(n)`, giving the signature
`O(sqrt(n))`-per-operation cost. Point updates typically touch only the single
block that owns the changed index.

## When to reach for it

Reach for square root decomposition when you need **both** updates and range
queries on a sequence and:

- The aggregate is **associative** (sum, min, max, gcd, count) so whole blocks
  can be summarized — this is the classic range-query use.
- You want something **much simpler to implement and reason about** than a
  segment tree / Fenwick tree, and an `O(sqrt(n))` factor is acceptable
  (`n` up to a few `10^5` with up to a few `10^5` queries is comfortable).
- The query is an **order statistic** (k-th smallest, count `<= k`) that a plain
  invertible prefix cannot support — keep a **sorted copy per block** and binary
  search the whole blocks.
- You are walking a **forward pointer chain** (each index jumps to a later
  index) and want to compress it — precompute per-hole "escape this block"
  summaries and hop block-to-block.
- The problem allows **offline** reordering of queries — a close cousin,
  [Mo's algorithm](../mos-algorithm), sorts queries by block to answer them in
  `O((n + q) sqrt(n))`.

If you need the absolute best asymptotics for a standard associative range query
with point updates, a Fenwick / segment tree (`O(log n)`) beats it; sqrt
decomposition wins on simplicity and on operations trees cannot easily batch.

## Typical complexity

| Aspect | Cost |
|---|---|
| Build | `O(n)` (or `O(n log n)` if each block is sorted) |
| Point update | `O(1)` to `O(sqrt(n))` (depending on the summary maintained) |
| Range query | `O(sqrt(n))`, or `O(sqrt(n) log n)` with per-block binary search |
| Space | `O(n)` (the array plus `O(sqrt(n))` — or `O(n)` — of block summaries) |

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Range Sum Query - Mutable](problem-01-range-sum-query-mutable/PROBLEM.md) | Per-block sums; `O(1)` update, `O(sqrt(n))` sum query | Medium |
| 2 | [Range Minimum Query with Point Updates](problem-02-range-minimum-query-with-point-updates/PROBLEM.md) | Per-block minima; associative-but-not-invertible aggregate | Medium |
| 3 | [Range Add & Range Sum (Lazy Blocks)](problem-03-range-add-range-sum-lazy-blocks/PROBLEM.md) | Per-block **lazy add** tags for `O(sqrt(n))` range updates | Medium |
| 4 | [Range Count of Elements Not Exceeding K](problem-04-range-count-not-exceeding-k-with-updates/PROBLEM.md) | **Sorted copy per block** + binary search for order statistics | Hard |
| 5 | [Holes — Ball Jumping with Power Updates](problem-05-holes-ball-jumping-with-updates/PROBLEM.md) | Compress a forward jump chain into per-block escapes | Hard |

Work them top to bottom: the first three build the core block-summary and lazy
mechanics on sums and minima; the last two show the two big generalizations —
sorted blocks for order statistics, and block-jump compression for pointer
chains.
