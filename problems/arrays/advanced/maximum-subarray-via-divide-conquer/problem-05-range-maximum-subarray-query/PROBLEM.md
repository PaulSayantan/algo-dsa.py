# Range Maximum Subarray Query

**Difficulty:** Hard

**Source:** SPOJ GSS1 — "Can you answer these queries I" (classic segment-tree
maximum-subarray problem)

## Description

You are given an array `nums` of `n` integers. You must answer `q` queries. Each
query gives a range `[l, r]` (0-based, inclusive) and asks:

> Among all non-empty contiguous subarrays that lie **entirely within**
> `nums[l..r]`, what is the maximum possible sum?

Formally, for a query `(l, r)` return
`max{ nums[i] + nums[i+1] + ... + nums[j] : l <= i <= j <= r }`.

A single query is just the maximum-subarray problem restricted to a sub-range.
Running the `O(n log n)` recursion (or `O(n)` Kadane) per query would be
`O(q · n)`, which is too slow when both are large. The idiomatic solution builds a
**segment tree** whose every node stores the divide & conquer "range summary"
`(total, best_prefix, best_suffix, best)`; two children are merged with **exactly
the crossing-combine rule** from the one-shot algorithm. Each query then merges
`O(log n)` node summaries.

## Constraints

- `1 <= n <= 5 * 10^4`
- `1 <= q <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `0 <= l <= r <= n - 1`
- The queried subarray must be non-empty (guaranteed since `l <= r`).

## Examples

### Example 1

```
Input:  nums = [-1, 2, 3, -5, 4]
        queries = [(0, 4), (0, 2), (3, 4)]
Output: [5, 5, 4]
Explanation:
  (0, 4): best subarray is [2, 3] = 5 (adding -1 before or -5 after only hurts).
  (0, 2): best subarray is [2, 3] = 5, inside nums[0..2] = [-1, 2, 3].
  (3, 4): nums[3..4] = [-5, 4]; best is [4] = 4.
```

### Example 2

```
Input:  nums = [-2, -3, -1, -4]
        queries = [(0, 3), (1, 2)]
Output: [-1, -1]
Explanation:
  (0, 3): all negative, so the best single element is -1.
  (1, 2): nums[1..2] = [-3, -1]; best single element is -1.
```

### Example 3

```
Input:  nums = [1, 2, 3, 4]
        queries = [(0, 3), (2, 3)]
Output: [10, 7]
Explanation:
  (0, 3): the whole array [1, 2, 3, 4] = 10.
  (2, 3): [3, 4] = 7.
```

## Hint

Use **Maximum Subarray via Divide & Conquer** as a segment-tree node merge. Store
`(total, best_prefix, best_suffix, best)` per node. To merge a left child `L` and
right child `R`:
- `total = L.total + R.total`
- `best_prefix = max(L.best_prefix, L.total + R.best_prefix)`
- `best_suffix = max(R.best_suffix, R.total + L.best_suffix)`
- `best = max(L.best, R.best, L.best_suffix + R.best_prefix)`  ← the crossing term
Build in `O(n)`, answer each query in `O(log n)`.
