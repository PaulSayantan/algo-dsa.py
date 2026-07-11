# Powerful Array

**Difficulty:** Medium

**Source:** Codeforces 86D — "Powerful array".

## Description

For a subarray we define its **power** as follows. Let `Ks` be the number of
occurrences of value `s` inside the subarray. The power of the subarray is:

```
power = Σ  Ks^2 * s      (sum over every distinct value s in the subarray)
```

You are given a static array `a` of `n` positive integers and `q` queries. Each
query gives `l` and `r` (**1-indexed**, inclusive) and asks for the power of the
subarray `a[l..r]`.

All queries are provided up front; the array is never modified. Return the power
for each query in the original order.

The statistic is a sum over occurrence counts, so it updates in `O(1)` when a
single element enters or leaves the window: adding a value `v` whose count goes
`k → k+1` changes the power by `(2k + 1) * v`; removing it (`k → k-1`) changes it
by `-(2k - 1) * v`.

## Constraints

- `1 <= n, q <= 2 * 10^5`
- `1 <= a[i] <= 10^6`
- `1 <= l <= r <= n`
- Answers can exceed 32 bits — use 64-bit integers (Python ints are unbounded).

## Examples

### Example 1

```
Input:
  n = 3, q = 2
  a = [1, 2, 1]           (1-indexed: a[1]=1, a[2]=2, a[3]=1)
  queries = [(1, 2), (1, 3)]
Output:
  [3, 6]
```

Explanation:
- `a[1..2] = [1, 2]`: counts K₁=1, K₂=1 → `1²·1 + 1²·2 = 1 + 2 = 3`.
- `a[1..3] = [1, 2, 1]`: counts K₁=2, K₂=1 → `2²·1 + 1²·2 = 4 + 2 = 6`.

### Example 2

```
Input:
  n = 8, q = 3
  a = [1, 1, 2, 2, 1, 3, 1, 1]
  queries = [(2, 7), (1, 6), (2, 7)]
Output:
  [20, 20, 20]
```

Explanation:
- `a[2..7] = [1, 2, 2, 1, 3, 1]`: counts K₁=3, K₂=2, K₃=1 →
  `3²·1 + 2²·2 + 1²·3 = 9 + 8 + 3 = 20`.
- `a[1..6] = [1, 1, 2, 2, 1, 3]`: counts K₁=3, K₂=2, K₃=1 →
  `9 + 8 + 3 = 20`.
- The third query equals the first → 20 again.

## Hint

The power is a sum over occurrence counts that is not decomposable by a segment
tree, but it changes by a simple closed-form delta when one element joins or
leaves the window. Answer all queries **offline** with **Sqrt Decomposition on
Queries (offline)**, keeping a running power and a frequency table.
