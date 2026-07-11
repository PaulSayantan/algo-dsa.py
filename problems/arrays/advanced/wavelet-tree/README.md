# Wavelet Tree

A **Wavelet Tree** is a static, comparison-based data structure built over a
sequence of values drawn from an alphabet `[lo, hi]`. It recursively partitions
the alphabet in half (like a segment tree, but over *values* instead of
*positions*) and, at each node, stores a **bitmap** that records, for every
element currently held by that node, whether it belongs to the lower half
(`0`/left) or the upper half (`1`/right) of the value range.

By pre-computing a prefix-sum of that bitmap at each node, you can "route" any
positional range `[l, r)` down the tree in O(1) per level. This unlocks a family
of powerful queries on **static** arrays:

- **rank(c, i)** – how many times value `c` appears in the prefix `arr[0..i)`.
- **select(c, j)** – the index of the `j`-th occurrence of value `c`.
- **rangeCountLeq(l, r, x)** – how many elements in `arr[l..r)` are `<= x`
  (and, by subtraction, `< x`, `= x`, `in [a, b]`, etc.).
- **kthSmallest(l, r, k)** – the `k`-th smallest element of subarray `arr[l..r)`
  (a range order-statistic / range-quantile query).

## When to reach for it

Reach for a Wavelet Tree when you have a **static** array and must answer many
**range order-statistic / range-frequency** queries offline or online — problems
that a plain Fenwick/segment tree cannot answer directly, and that a merge-sort
tree answers only in `O(log^2 n)`. The Wavelet Tree answers each such query in
`O(log σ)` where `σ` is the size of the value alphabet.

If your array is *dynamic* (frequent point updates), a Wavelet Tree is usually
the wrong tool — prefer a merge-sort tree with fractional cascading, a
persistent segment tree, or sqrt-decomposition depending on the update pattern.

## Complexity

| Operation                         | Time        | Notes                                  |
|-----------------------------------|-------------|----------------------------------------|
| Build                             | `O(n log σ)`| `σ` = number of distinct values / range|
| `rank`, `select`, `rangeCountLeq` | `O(log σ)`  | O(1) work per level via prefix sums    |
| `kthSmallest` in a range          | `O(log σ)`  | one root-to-leaf descent               |
| Space                             | `O(n log σ)`| bitmaps + prefix sums per level        |

Coordinate-compress the values first so `σ <= n`, giving `O(log n)` per query.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Rank & Select over a Sequence](problem-01-rank-select-sequence/PROBLEM.md) | Build the tree; implement `rank`/`select` (the core primitives) | Easy |
| 2 | [Count Values ≤ K in a Range](problem-02-count-values-leq-k-in-range/PROBLEM.md) | Route a range down the tree to count `<= x` | Easy–Medium |
| 3 | [Range K-th Smallest (MKTHNUM)](problem-03-range-kth-smallest/PROBLEM.md) | The signature query: order statistic in a subrange | Medium |
| 4 | [Count of Smaller Numbers After Self](problem-04-count-smaller-after-self/PROBLEM.md) | LeetCode 315 via suffix range-count | Hard |
| 5 | [Reverse Pairs](problem-05-reverse-pairs/PROBLEM.md) | LeetCode 493 via prefix range-count with a scaled threshold | Hard |
| 6 | [Online Majority in Subarray Queries](problem-06-online-majority-in-subarray/PROBLEM.md) | LeetCode 1157: median candidate (`kthSmallest`) + `rank` verification | Hard |
