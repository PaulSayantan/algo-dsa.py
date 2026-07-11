# Solution — Reverse Pairs

## Brute Force

Check every pair `(i, j)` with `i < j` and test `nums[i] > 2 * nums[j]`:
`O(n^2)` time, `O(1)` extra space. For `n = 5 * 10^4` that is `2.5 * 10^9`
comparisons — too slow in practice.

The standard `O(n log n)` solution is a **modified merge sort**: while merging
the two sorted halves, count pairs with `left[i] > 2 * right[j]` before merging.
A BIT/Fenwick over compressed values also works. The Wavelet Tree offers a clean
`O(n log sigma)` alternative that reuses the same range-count primitive as the
earlier problems.

## Optimal Approach (Wavelet Tree)

### Reduction

Fix `j`. The valid partners are indices `i < j` (the prefix `[0, j)`) whose value
satisfies `nums[i] > 2 * nums[j]`. So for each `j`:

```
contribution(j) = |{ i in [0, j) : nums[i] > 2 * nums[j] }|
                = j - rangeCountLeq(0, j, 2 * nums[j])
```

`rangeCountLeq(0, j, T)` counts prefix values `<= T`; subtracting from the prefix
length `j` gives the count strictly greater than `T`. Summing over all `j` yields
the answer. Since a Wavelet Tree built over the *whole* array can answer
`rangeCountLeq(0, j, ...)` for any `j`, we don't even need to insert
incrementally — the prefix window `[0, j)` is just a normal range query.

### Algorithm

1. Build a Wavelet Tree over all of `nums`: `O(n log sigma)`.
2. For `j = 0 .. n-1`, add `j - range_count_leq(0, j, 2 * nums[j])` to a running
   total.
3. Return the total.

```python
class Solution:
    def reversePairs(self, nums):
        n = len(nums)
        wt = WaveletTree(nums)                     # rangeCountLeq(l, r, x)
        total = 0
        for j in range(n):
            T = 2 * nums[j]
            total += j - wt.range_count_leq(0, j, T)   # values in [0,j) that are > T
        return total
```

### Handling the `2 * nums[j]` threshold with compression

The threshold `T = 2 * nums[j]` is generally **not** a value present in `nums`,
and with `nums[j]` up to `2^31 - 1` it may not fit the compressed alphabet. Two
robust options:

- **Compare on the raw value scale.** Store each node's true `[lo, hi]` on the
  original integer scale and compare the raw `T` against the raw `mid` inside
  `range_count_leq`. Then `T` can be any 64-bit integer with no special casing.
- **Map `T` into the compressed domain by `<=` semantics.** Compute
  `t = (number of distinct sorted values that are <= T) - 1`; then
  `rangeCountLeq(0, j, T)` on raw values equals a compressed query at index `t`.
  Use `bisect_right` on the sorted distinct values. Guard `T` below the minimum
  (result `0`) and above the maximum (result `j`).

Both give identical answers; the raw-scale comparison is easier to get right.

### Why it is correct

Every important reverse pair `(i, j)` has a unique larger index `j`, and is
counted exactly once when we process that `j`: `i` ranges over `[0, j)` and the
condition `nums[i] > 2 * nums[j]` is precisely "prefix value `> T`". Summed over
all `j`, each pair is counted once, giving the exact total. No pair is double
counted because `i < j` fixes which endpoint is the "query" index.

**Complexity:** `O(n log sigma)` time (build + `n` queries), `O(n log sigma)`
space. With compression, `O(n log n)`.

## Key Insights & Edge Cases

- **Overflow**: `2 * nums[j]` can exceed 32 bits (up to `~4.29 * 10^9`). In
  Python this is automatic; in C++/Java use 64-bit (`long long` / `long`) for
  the threshold.
- **Strict inequality**: we need `nums[i] > 2 * nums[j]`, i.e. strictly greater,
  so counting `> T` (not `>= T`) is correct — `j - rangeCountLeq(0, j, T)` does
  exactly that.
- **Negative numbers** are fine: `2 * nums[j]` may be very negative, the
  raw-scale comparison handles it; below-minimum thresholds contribute `0`
  (nothing is `<= T`, so all `j` prefix elements count as `>` — but only if `T`
  is below min... which the formula `j - 0 = j` correctly yields when *all*
  prefix values exceed `T`).
- **Prefix window `[0, j)`** is empty for `j = 0`, contributing `0`.
- Choose merge sort if you want the simplest self-contained solution; choose the
  Wavelet Tree when the same array must also answer k-th-smallest / range-count
  queries (it amortizes one build across many query types).
