# Solution — Kth Smallest Number in a Multiplication Table

## Brute Force

Generate all `m * n` products, sort, and index `k - 1`.

```python
vals = sorted(i * j for i in range(1, m + 1) for j in range(1, n + 1))
return vals[k - 1]
```

- **Time:** `O(m·n·log(m·n))`.
- **Space:** `O(m·n)`.

With `m, n <= 3·10^4` the table can hold `9·10^8` entries — this both times out
and runs out of memory. We must avoid materializing the table.

A min-heap over the `m` rows (each row `i` is the sorted sequence `i, 2i, …, ni`)
gives `O(k log m)`, but `k` can be as large as `9·10^8`, so it is still too slow.

## Optimal Approach — Binary Search on Value + Saddleback Count

Exactly as in Problem 4, binary-search the **answer value**, not a position. The
value range is `[1, m*n]`. For a candidate `x`, let

```
count_le(x) = number of table cells with i * j <= x
```

`count_le` is non-decreasing in `x`, and the answer is the smallest `x` with
`count_le(x) >= k`.

### Counting `<= x` — the saddleback insight in closed form

A full staircase walk over the implicit grid would, for each row, find how far the
"`<= x`" region extends. But here the grid is defined by `mat[i][j] = i * j`, so we
can collapse each row's contribution to arithmetic:

- In row `i` (1-indexed), the entries are `i, 2i, 3i, …, ni`. The ones `<= x` are
  exactly those `j` with `i * j <= x`, i.e. `j <= x // i`. There are
  `min(x // i, n)` of them.

Summing over rows gives `count_le(x) = Σ_{i=1}^{m} min(x // i, n)`. This is the
saddleback walk written in closed form: instead of stepping cell by cell along the
monotone `0/1` boundary, each row's boundary position is computed directly in
`O(1)`, so the whole count is `O(m)`.

```python
def count_le(m, n, x):
    total = 0
    for i in range(1, m + 1):
        total += min(x // i, n)   # entries in row i that are <= x
    return total
```

### Binary search driver

```python
def findKthNumber(m, n, k):
    lo, hi = 1, m * n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if count_le(m, n, mid) >= k:
            hi = mid          # enough entries <= mid; shrink toward it
        else:
            lo = mid + 1      # too few; the answer is larger
    return lo
```

### Why the result is a real table value

`lo` converges to the least `x` with `count_le(x) >= k`. If that `x` were not a
product `i*j`, then `count_le(x) == count_le(x - 1)`, so `x - 1` would also satisfy
`>= k`, contradicting minimality. Therefore `lo` is an actual entry — the k-th
smallest.

### Worked trace on Example 1 (`m = n = 3`, `k = 5`)

`lo = 1`, `hi = 9`.

- `mid = 5`: `count_le = min(5,3) + min(2,3) + min(1,3) = 3 + 2 + 1 = 6`.
  `6 >= 5` → `hi = 5`.
- `mid = 3`: `count_le = min(3,3) + min(1,3) + min(1,3) = 3 + 1 + 1 = 5`.
  `5 >= 5` → `hi = 3`.
- `mid = 2`: `count_le = min(2,3) + min(1,3) + min(0,3) = 2 + 1 + 0 = 3`.
  `3 < 5` → `lo = 3`.
- `lo = hi = 3` → return **3**. Matches the expected output.

(Sanity check for Example 2, `m=2,n=3,k=6`: `count_le(6) = min(6,3)+min(3,3) =
3+3 = 6 >= 6`, and `count_le(5) = 3 + 2 = 5 < 6`, so the answer is `6`.)

### Complexity

- **Time:** `O(m · log(m·n))`. Each `count_le` is `O(m)`; binary search runs
  `O(log(m·n))` iterations. (You can loop over `min(m, n)` and swap to keep the
  smaller dimension in the loop.)
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Implicit matrix.** The saddleback technique never needs the matrix in memory —
  it only needs `mat[i][j]` on demand, which here is `i * j`. This is what makes
  the `9·10^8`-cell table tractable.
- **Closed-form row count.** `min(x // i, n)` is the per-row staircase boundary
  computed directly; it is the same monotone frontier as Problems 2–4, evaluated
  arithmetically instead of by stepping.
- **Loop over the smaller dimension** (`min(m, n)`) and treat the other as the
  column cap `n` — this keeps each count at `O(min(m, n))`.
- **Boundary discipline:** use `hi = mid` when the count is sufficient; `lo` is the
  final answer. Off-by-one here is the classic bug.
- Edge cases: `k = 1` → answer `1`; single row (`m = 1`) reduces to `min(x, n)` and
  returns `k` directly; `k = m*n` → answer `m*n` only when it is achievable (it
  always is, at cell `(m, n)`).
