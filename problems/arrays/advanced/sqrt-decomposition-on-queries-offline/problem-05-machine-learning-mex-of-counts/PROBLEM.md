# Machine Learning (Mex of Occurrence Counts)

**Difficulty:** Very Hard

**Source:** Codeforces 940F — "Machine Learning".

## Description

You are given an array `a` of `n` integers. You must process `q` operations of
two kinds:

- **Type 1 — `(1, l, r)`:** Consider the subarray `a[l..r]` (**1-indexed**,
  inclusive). For every distinct value in that subarray, compute how many times
  it occurs. Output the **mex** of the multiset of these occurrence counts — that
  is, the **smallest positive integer that is not equal to the occurrence count
  of any value** in `a[l..r]`.
- **Type 2 — `(2, p, x)`:** A **point update** — set `a[p] = x` (1-indexed
  position). This affects all later queries.

Because updates are interleaved with queries, this is **not** a pure static-array
problem: it needs Mo's algorithm extended with a *time* (update) dimension.

### Why the answer is small (key fact)

Let `occ[t]` be the number of distinct values that occur exactly `t` times in the
current window. If the answer (mex) were `M`, then each of `1, 2, ..., M-1` is the
occurrence count of some value, so the subarray must contain at least
`1 + 2 + ... + (M-1) = M(M-1)/2` elements. Hence `M = O(sqrt(len))`, so you can
find the mex by scanning `t = 1, 2, 3, ...` until `occ[t] == 0` — only
`O(sqrt(len))` steps.

## Constraints

- `1 <= n, q <= 10^5`
- `1 <= a[i], x <= 10^9` (coordinate-compress values, including update values)
- `1 <= l <= r <= n`, `1 <= p <= n`
- Mixed queries: updates and type-1 queries may appear in any order.

## Examples

### Example 1

```
Input:
  n = 6
  a = [1, 2, 3, 3, 3, 2]        (1-indexed)
  ops = [(1, 1, 3),             # query subarray a[1..3]
         (2, 2, 3),             # update: a[2] = 3
         (1, 1, 3)]             # query subarray a[1..3] again
Output:
  [2, 3]
```

Explanation:
- `(1,1,3)`: `a[1..3] = [1,2,3]`; each value occurs once → occurrence counts
  present = {1}. Smallest positive integer absent = **2**.
- `(2,2,3)`: sets `a[2] = 3`, so `a = [1,3,3,3,3,2]`.
- `(1,1,3)`: `a[1..3] = [1,3,3]`; value 1 occurs once, value 3 occurs twice →
  occurrence counts present = {1, 2}. Smallest positive absent = **3**.

### Example 2

```
Input:
  n = 3
  a = [2, 3, 2]                 (1-indexed)
  ops = [(1, 1, 3),
         (1, 2, 3)]
Output:
  [3, 2]
```

Explanation:
- `(1,1,3)`: `a[1..3] = [2,3,2]`; value 2 occurs twice, value 3 occurs once →
  counts present = {1, 2}. Smallest positive absent = **3**.
- `(1,2,3)`: `a[2..3] = [3,2]`; each occurs once → counts present = {1}. Smallest
  positive absent = **2**.

## Hint

The presence of point updates rules out plain Mo's. Use **Sqrt Decomposition on
Queries (offline)** extended with a third *time* coordinate ("Mo's with
updates" / 3D Mo's): sort queries by `(block of l, block of r, timestamp)` with
block size `~ n^(2/3)`, and roll updates forward/backward as you move between
queries while maintaining occurrence-count histograms.
