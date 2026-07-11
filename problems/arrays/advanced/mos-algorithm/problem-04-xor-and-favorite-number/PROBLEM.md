# XOR and Favorite Number

**Difficulty:** Hard

**Source:** Codeforces 617E — "XOR and Favorite Number"

## Description

You are given a static array `a` of `n` non-negative integers, a favorite number
`k`, and `q` queries. For each query `(l, r)` with `1 <= l <= r <= n`, count the
number of pairs `(i, j)` with `l <= i <= j <= r` such that the XOR of the subarray
equals `k`:

> `a[i] XOR a[i+1] XOR ... XOR a[j] = k`

In other words, count the sub-subarrays of `a[l..r]` whose bitwise-XOR is exactly
`k`. The array is static and all queries can be read up front (**offline**). Return
the answer for each query in the original order.

## Constraints

- `1 <= n, q <= 10^5`
- `0 <= k, a[i] <= 10^6` (so all prefix XORs also fit within `< 2^20`)
- `1 <= l <= r <= n`
- Answers can be large — use 64-bit integers (Python ints are unbounded).

## Examples

### Example 1

```
Input:
  a = [1, 2, 1, 1, 0, 3]        # 1-indexed a[1..6]
  k = 3
  queries = [(1, 6), (3, 5)]
Output:
  [7, 0]
```

**Explanation:** For `(1,6)` the subarrays of `a[1..6]` whose XOR equals `3` number
`7` (e.g. `[1,2]`, `[3]` at index 6, `[1,2,1,1,0,3]` reduces to check each — the
brute count is 7). For `(3,5)` = `[1, 1, 0]`, no sub-subarray XORs to `3`, so `0`.

### Example 2

```
Input:
  a = [1, 1, 1]                 # 1-indexed a[1..3]
  k = 0
  queries = [(1, 3), (2, 3)]
Output:
  [2, 1]
```

**Explanation:** With `k = 0` we count subarrays whose XOR is `0`.
- `(1,3)` = `[1,1,1]`: `[1,1]` (indices 1–2) and `[1,1]` (indices 2–3) both XOR to
  `0` → `2`.
- `(2,3)` = `[1,1]`: only `[1,1]` itself → `1`.

## Hint

Subarray XOR is a *difference* of prefix XORs: `xor(i..j) = P[i-1] XOR P[j]`, so it
equals `k` exactly when `P[j] = P[i-1] XOR k`. Counting subarrays with XOR `k` inside
`[l, r]` becomes counting **pairs of prefix values with XOR = k** among
`P[l-1..r]` — a frequency problem ideal for **Mo's Algorithm**.
