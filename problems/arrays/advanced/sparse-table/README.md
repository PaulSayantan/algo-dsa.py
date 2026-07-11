# Sparse Table

A **Sparse Table** is a static data structure that answers **range queries** on an
**immutable** array in **O(1)** time after an **O(n log n)** preprocessing step.

The core idea: precompute the answer for every subarray whose length is a power of
two. Concretely, define

```
sparse[j][i] = f( a[i], a[i+1], ..., a[i + 2^j - 1] )
```

i.e. the "combine" of the block of length `2^j` that starts at index `i`. Each level
`j` is built from the previous level in O(1) per entry:

```
sparse[j][i] = combine( sparse[j-1][i], sparse[j-1][i + 2^(j-1)] )
```

To answer a query on `[l, r]`, pick the largest power `2^k` with `2^k <= (r - l + 1)`
and combine the block that starts at `l` with the block that **ends** at `r`:

```
answer = combine( sparse[k][l], sparse[k][r - 2^k + 1] )
```

## When to reach for it

Use a Sparse Table when **all** of these hold:

- The array (or cost function over indices) is **static** — no updates between queries.
  If you need point/range updates, use a Segment Tree or Fenwick Tree instead.
- The combine operation is **idempotent**, meaning `combine(x, x) = x`. This is what
  lets the two query blocks **overlap** without double-counting. Idempotent operations
  include **min, max, gcd, bitwise AND, bitwise OR**.
- You have **many** queries (offline or online) and need each to be fast.

> Sum is **not** idempotent, so the O(1) two-block trick does not work directly. A
> Sparse Table can still do sum in O(log n) per query using **disjoint** blocks — but
> for sum a prefix-sum array is simpler and O(1).

## Complexity

| Operation                     | Time         | Space        |
|-------------------------------|--------------|--------------|
| Build                         | O(n log n)   | O(n log n)   |
| Query (idempotent op)         | O(1)         | —            |
| Query (non-idempotent, e.g. sum) | O(log n)  | —            |
| Update                        | Not supported (rebuild = O(n log n)) | — |

A tiny helper `log2[i] = floor(log2(i))` (precomputed in O(n)) lets you find the block
exponent `k` in O(1) per query.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Static Range Minimum Query](problem-01-static-range-minimum-query/PROBLEM.md) | Answer many `min(a[l..r])` queries on a fixed array | Easy |
| 2 | [Range GCD Queries](problem-02-range-gcd-queries/PROBLEM.md) | Answer many `gcd(a[l..r])` queries on a fixed array | Medium |
| 3 | [Longest Subarray with Abs Diff ≤ Limit](problem-03-longest-subarray-abs-diff-limit/PROBLEM.md) | Longest window where `max - min <= limit` (LeetCode 1438) | Medium |
| 4 | [Smallest Subarrays With Maximum Bitwise OR](problem-04-smallest-subarrays-max-or/PROBLEM.md) | For each `i`, shortest subarray from `i` reaching the max OR (LeetCode 2411) | Medium |
| 5 | [GCD of Whole Array via Cyclic Windows](problem-05-min-length-window-full-gcd/PROBLEM.md) | Smallest cyclic window whose GCD equals the array GCD (Codeforces 1547F flavor) | Hard |
