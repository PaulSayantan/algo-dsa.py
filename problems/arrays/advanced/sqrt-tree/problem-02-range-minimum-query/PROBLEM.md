# Range Minimum Query (RMQ)

**Difficulty:** Easy

**Source:** Classic (SPOJ RMQSQ; CSES 1647 "Static Range Minimum Queries")

## Description

Given a static integer array `nums` of length `n`, answer `q` queries. Each query gives
`l` and `r` (`0 <= l <= r < n`) and asks for the **minimum** value in the subarray
`nums[l..r]` inclusive.

Preprocess once, then answer each query in **O(1)**.

`min` is **associative** *and* **idempotent** (`min(x, x) = x`). Idempotence is exactly the
property a Sparse Table needs, so this problem is normally solved with a sparse table. We
solve it with a **Sqrt Tree** to show that Sqrt Tree handles idempotent ops too — its query
decomposition never overlaps ranges, so it does not even *rely* on idempotence. This makes
it a good bridge to the harder non-idempotent problems.

Implement `RangeMin` with a constructor and `query(l, r)` returning the minimum over
`[l, r]`.

## Constraints

- `1 <= n <= 2·10^5`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= q <= 2·10^5`
- `0 <= l <= r < n`

## Examples

### Example 1

```
Input:
  nums = [5, 2, 8, 1, 9, 3, 7]
  query(1, 4)
  query(4, 6)

Output:
  1
  3

Explanation:
  query(1, 4) -> min(2, 8, 1, 9) = 1
  query(4, 6) -> min(9, 3, 7)    = 3
```

### Example 2

```
Input:
  nums = [5, 2, 8, 1, 9, 3, 7]
  query(0, 6)
  query(2, 2)

Output:
  1
  8

Explanation:
  query(0, 6) -> min of the whole array = 1
  query(2, 2) -> single element nums[2] = 8
```

## Hint

Split into `√n` blocks, precompute per-block prefix/suffix minima and the min over every
pair of whole blocks, then answer any range with a suffix + between + prefix combine. Build
a **Sqrt Tree** with `op = min`. Note you do **not** need overlapping ranges (unlike a
sparse table), so the same structure will work for the non-idempotent problems later.
