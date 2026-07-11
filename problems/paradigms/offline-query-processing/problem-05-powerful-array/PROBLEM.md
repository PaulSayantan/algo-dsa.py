# Powerful Array

**Difficulty:** Hard

**Source:** Codeforces 86D (Powerful Array) — the canonical Mo's-algorithm problem

## Description

For an array `a` of positive integers, define the **power** of a subarray
`a[l..r]` (1-indexed, inclusive) as:

```
power(l, r) = sum over all distinct values v of  (count_v)^2 * v
```

where `count_v` is the number of times value `v` appears within `a[l..r]`.

You are given the array and `q` queries, each a pair `(l, r)`. For each query,
output `power(l, r)`. All queries are known in advance and there are no updates.
Return the answers in the order the queries are given.

## Constraints

- `1 <= n, q <= 2 * 10^5`
- `1 <= a[p] <= 10^6`
- `1 <= l <= r <= n`
- Answers can be large; use 64-bit integers (Python integers are unbounded).

## Examples

### Example 1

```
Input:  a = [1, 2, 1]
        queries = [(1, 2), (1, 3)]
Output: [3, 6]
```

Explanation:
- `(1, 2)`: subarray `[1, 2]`; each value appears once →
  `1^2*1 + 1^2*2 = 1 + 2 = 3`.
- `(1, 3)`: subarray `[1, 2, 1]`; value `1` appears twice, value `2` once →
  `2^2*1 + 1^2*2 = 4 + 2 = 6`.

### Example 2

```
Input:  a = [1, 1, 2, 2, 1, 3, 1, 1]
        queries = [(2, 7), (1, 6)]
Output: [20, 20]
```

Explanation:
- `(2, 7)`: subarray `[1, 2, 2, 1, 3, 1]`; value `1` appears 3 times,
  value `2` twice, value `3` once →
  `3^2*1 + 2^2*2 + 1^2*3 = 9 + 8 + 3 = 20`.
- `(1, 6)`: subarray `[1, 1, 2, 2, 1, 3]`; value `1` appears 3 times,
  value `2` twice, value `3` once →
  `9 + 8 + 3 = 20`.

## Hint

Each query depends on the exact multiset of a contiguous range, and adding or
removing one element at an endpoint changes the answer by an amount you can update
in `O(1)`. This is the signature of **Offline Query Processing** via **Mo's
algorithm**: sort the queries by `(l // block, r)` and slide two pointers between
consecutive queries so the total pointer movement is `O((n + q) * sqrt(n))`.
