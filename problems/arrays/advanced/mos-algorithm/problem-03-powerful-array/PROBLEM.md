# Powerful Array

**Difficulty:** Hard

**Source:** Codeforces 86D — "Powerful Array"

## Description

You are given a static array `a` of `n` positive integers and `q` queries. For a
subarray `a[l..r]`, let `cnt[x]` be the number of times value `x` occurs in it. The
**power** of the subarray is defined as:

> `power(l, r) = Σ_x  cnt[x]² · x`

(the sum is over every distinct value `x` present in `a[l..r]`). For each query
`(l, r)` with `1 <= l <= r <= n`, output `power(l, r)`. The array is static and all
queries may be read before answering (**offline**). Return answers in input order.

## Constraints

- `1 <= n, q <= 2 * 10^5`
- `1 <= a[i] <= 10^6`
- `1 <= l <= r <= n`
- Answers can be large — use 64-bit integers (Python ints are unbounded).

## Examples

### Example 1

```
Input:
  a = [1, 2, 1]                 # 1-indexed a[1..3]
  queries = [(1, 2), (1, 3), (2, 3)]
Output:
  [3, 6, 3]
```

**Explanation:**
- `(1,2)` → `{1, 2}`: `1`·1² + `2`·1² = 1 + 2 = `3`.
- `(1,3)` → `{1, 2, 1}`: value `1` occurs twice (`1·2² = 4`), value `2` once
  (`2·1² = 2`) → `4 + 2 = 6`.
- `(2,3)` → `{2, 1}`: `2·1² + 1·1² = 2 + 1 = `3`.

### Example 2

```
Input:
  a = [1, 1, 1]                 # 1-indexed a[1..3]
  queries = [(1, 3), (1, 1)]
Output:
  [9, 1]
```

**Explanation:**
- `(1,3)` → value `1` occurs `3` times: `1 · 3² = 9`.
- `(1,1)` → value `1` occurs once: `1 · 1² = 1`.

## Hint

When you add one occurrence of value `x`, its term changes from `x·cnt²` to
`x·(cnt+1)²`, a delta of `x·(2·cnt + 1)`. That means the running answer can be
maintained in `O(1)` per boundary move — perfect for **Mo's Algorithm** on the
offline queries.
