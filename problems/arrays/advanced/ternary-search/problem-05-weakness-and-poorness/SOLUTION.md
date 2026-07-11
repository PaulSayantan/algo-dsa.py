# Solution — Weakness and Poorness

## Brute Force

Try many candidate values of `x` on a fine grid; for each, compute `weakness(x)` by
examining subarrays.

- **Naive weakness:** enumerating all `O(n^2)` subarrays per `x` is `O(G · n^2)` — far
  too slow for `n = 2·10^5`.
- Even with an `O(n)` weakness evaluator (below), a blind grid over `x` still needs a
  huge number of points to reach `1e-6` and remains only approximate.

The key structural fact — that `weakness(x)` is convex in `x` — turns this into a clean
ternary search.

## Optimal Approach (Ternary Search on `x` + Kadane inside)

### Evaluating `weakness(x)` in O(n)

Fix `x` and set `b_i = a_i - x`. The poorness of subarray `[l, r]` is
`|sum_{i in [l,r]} b_i|`. The maximum absolute subarray sum is

```
weakness(x) = max( maxSubarraySum(b), -minSubarraySum(b) )
```

Both `maxSubarraySum` (largest contiguous sum) and `minSubarraySum` (smallest
contiguous sum) come from **Kadane's algorithm** in a single `O(n)` pass each. Taking
`-minSubarraySum` captures the most-negative subarray as a positive magnitude, so the
`max` of the two is the largest **absolute** subarray sum.

### Why `weakness(x)` is unimodal in `x`

A subarray `[l, r]` of length `k` has sum `S_{l,r} - k·x`, where `S_{l,r}` is its sum in
the original array. Its poorness `|S_{l,r} - k·x|` is a **V-shaped (convex)** function of
`x`. `weakness(x)` is the **pointwise maximum** over all subarrays of these convex
functions, and a pointwise max of convex functions is **convex**. A convex function on
an interval is **unimodal** — one minimum, no spurious local minima. Ternary search
finds it.

### The search

Search `x` on an interval that safely brackets the optimum. Since `|a_i| <= 10^4`, the
optimal `x` lies within `[-10^4, 10^4]`. Standard minimization step:

```
m1 = lo + (hi - lo) / 3
m2 = hi - (hi - lo) / 3
if weakness(m1) < weakness(m2):  hi = m2
else:                            lo = m1
```

Run ~200-300 iterations (each an `O(n)` weakness evaluation), then report
`weakness((lo + hi) / 2)`.

### Reference implementation

```python
from typing import List


def weakness(a: List[int], x: float) -> float:
    # Kadane for max subarray sum and min subarray sum of (a_i - x).
    max_end = max_so = a[0] - x
    min_end = min_so = a[0] - x
    for i in range(1, len(a)):
        v = a[i] - x
        max_end = max(v, max_end + v)
        max_so = max(max_so, max_end)
        min_end = min(v, min_end + v)
        min_so = min(min_so, min_end)
    return max(max_so, -min_so)


def min_weakness(a: List[int]) -> float:
    lo, hi = -1e4, 1e4
    for _ in range(300):
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0
        if weakness(a, m1) < weakness(a, m2):
            hi = m2
        else:
            lo = m1
    return weakness(a, (lo + hi) / 2.0)
```

- **Time:** O(n · log_{3/2}(range / eps)) — ~300 iterations, each an `O(n)` Kadane pass.
  For `n = 2·10^5` that is ~`6·10^7` operations.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Two nested ideas.** The *outer* problem (choose `x`) is a unimodal optimization →
  ternary search. The *inner* evaluation (weakness of a fixed `x`) is a max-absolute
  subarray problem → Kadane. Recognizing that the outer function is convex is what makes
  the whole thing efficient.
- **Max of convex is convex** is the general reason a great many "minimize the worst
  case over a parameter" problems are unimodal and ternary-searchable.
- **`weakness` combines max- and min-subarray.** Forgetting the `-minSubarraySum` term
  misses the most-negative subarray and undercounts the true weakness.
- **Precision:** iterate a fixed number of times; do not compare floats for equality.
  ~200-300 iterations of the `2/3` shrink over a width-`2·10^4` interval reach well
  below `1e-6`.
- **`n == 1`:** the only subarray is `[a_0]`; picking `x = a_0` makes weakness `0`, and
  the search converges there.
- **Bracketing interval** must contain the optimum. `[-max|a_i|, max|a_i|]` is safe
  because pushing `x` outside the data range only increases every subarray's poorness.
