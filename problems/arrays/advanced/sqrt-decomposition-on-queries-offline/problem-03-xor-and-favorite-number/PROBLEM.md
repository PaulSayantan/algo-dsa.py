# XOR and Favorite Number

**Difficulty:** Hard

**Source:** Codeforces 617E — "XOR and Favorite Number".

## Description

You are given a static array `a` of `n` non-negative integers and a fixed
favorite number `k`. You must answer `q` queries. Each query gives `l` and `r`
(**1-indexed**, inclusive) and asks:

> How many pairs `(i, j)` with `l <= i <= j <= r` satisfy
> `a[i] XOR a[i+1] XOR ... XOR a[j] = k`?

(`XOR` is the bitwise exclusive-or.) All queries are known in advance and the
array is never modified.

### The prefix-XOR reformulation (the crux)

Define prefix XOR `pre[0] = 0` and `pre[t] = a[1] XOR ... XOR a[t]`. Then the XOR
of the subarray `a[i..j]` equals `pre[j] XOR pre[i-1]`. So the subarray condition
`= k` becomes: count pairs of **prefix indices** `(x, y)` with
`l-1 <= x < y <= r` such that `pre[x] XOR pre[y] = k`, i.e. `pre[y] = pre[x] XOR k`.

That turns a "count subarrays" query on `a[l..r]` into a "count value pairs"
query on the prefix array over the index window `[l-1, r]` — exactly the shape
Mo's algorithm loves. When a prefix value `pv` enters the window you add
`cnt[pv XOR k]` to the running answer, then increment `cnt[pv]`.

## Constraints

- `1 <= n, q <= 10^5`
- `0 <= a[i], k <= 10^6` (so every prefix XOR is `< 2^20`)
- `1 <= l <= r <= n`
- The answer can exceed 32 bits — use 64-bit integers.

## Examples

### Example 1

```
Input:
  n = 6, q = 2, k = 3
  a = [1, 2, 1, 1, 0, 3]     (1-indexed)
  queries = [(1, 6), (3, 5)]
Output:
  [7, 0]
```

Explanation:
- Prefix XOR array: `pre = [0, 1, 3, 2, 3, 3, 0]` (indices 0..6).
- Query `(1,6)` counts prefix-index pairs `(x, y)`, `0 <= x < y <= 6`, with
  `pre[x] XOR pre[y] = 3`. Value 0 sits at indices {0,6} and value 3 at {2,4,5}
  (`0 XOR 3 = 3` → 2·3 = 6 pairs), plus value 1 at {1} with value 2 at {3}
  (`1 XOR 2 = 3` → 1 pair). Total = **7**.
- Query `(3,5)` uses prefix window `[2,5]` with values `3,2,3,3`. No pair XORs to
  3, so **0**.

### Example 2

```
Input:
  n = 5, q = 3, k = 0
  a = [1, 1, 2, 2, 1]        (1-indexed)
  queries = [(1, 2), (1, 4), (2, 5)]
Output:
  [1, 3, 2]
```

Explanation (with `k = 0`, we count subarrays whose XOR is 0, i.e. equal prefix
values `pre[x] == pre[y]`):
- `pre = [0, 1, 0, 2, 0, 1]` (indices 0..5).
- `(1,2)` → prefix window `[0,2]`, values `0,1,0`: the single equal pair
  (indices 0 and 2, both 0) → subarray `a[1..2] = [1,1]` → **1**.
- `(1,4)` → prefix window `[0,4]`, values `0,1,0,2,0`: value 0 sits at indices
  {0,2,4} giving C(3,2) = 3 equal pairs — `(0,2)`, `(0,4)`, `(2,4)` → subarrays
  `a[1..2]`, `a[1..4]`, `a[3..4]`, each XOR 0 → **3**.
- `(2,5)` → prefix window `[1,5]`, values `1,0,2,0,1`: value 1 at {1,5} → 1 pair
  (subarray `a[2..5]`), value 0 at {2,4} → 1 pair (subarray `a[3..4]`) → **2**.

## Hint

Rewrite subarray-XOR as a difference of prefix XORs, reducing each query to
"count value pairs in an index window". Then answer everything **offline** with
**Sqrt Decomposition on Queries (offline)**, maintaining a count table over
prefix values and adding `cnt[pv XOR k]` on each insertion.
