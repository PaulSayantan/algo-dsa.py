# Solution — Peak Index in a Mountain Array

## Brute Force

Scan left to right and return the first index `i` with `arr[i] > arr[i + 1]` (the
first place the array stops increasing). Equivalently, take `argmax(arr)`.

- **Time:** O(n) — one pass.
- **Space:** O(1).

This is perfectly correct and often accepted, but it ignores the structure. Because
the array is unimodal we can do much better than a full scan.

## Optimal Approach (Ternary Search on the index domain)

### Setup

Treat the array as a function `f(index) = arr[index]` defined on the integer domain
`[0, n - 1]`. The mountain property says `f` strictly increases up to the peak and
strictly decreases after it — it is **unimodal with a single maximum**. Ternary search
finds the argmax of any unimodal function.

### Iteration

Maintain a candidate window `[lo, hi]` that is guaranteed to contain the peak (start
`lo = 0`, `hi = n - 1`). While the window has more than 2 elements, probe two interior
indices:

```
m1 = lo + (hi - lo) // 3
m2 = hi - (hi - lo) // 3          # lo <= m1 < m2 <= hi when hi - lo >= 2
```

Compare the array values:

- If `arr[m1] < arr[m2]`: we are still on the rising side at `m1` relative to `m2`, so
  the peak is strictly to the **right** of `m1`. Discard `[lo, m1]` → `lo = m1 + 1`.
- Otherwise (`arr[m1] > arr[m2]`, and they can't be equal since values are strictly
  monotone on each side and `m1 != m2`): the peak is at or to the **left** of `m2`.
  Discard `[m2, hi]` → `hi = m2 - 1`.

Using `m1 + 1` and `m2 - 1` guarantees the window strictly shrinks, so the loop always
terminates. When `hi - lo <= 2`, scan the (at most 3) remaining indices and return the
one with the largest value.

### Why it is correct

The peak `i*` is the unique maximum. Consider `arr[m1]` vs `arr[m2]` with `m1 < m2`:

- If `arr[m1] < arr[m2]`, then `m1` cannot be the peak and neither can anything left of
  it, because to the left of the peak the function is strictly increasing — if the peak
  were `<= m1`, the function would already be decreasing at `m2 > m1`, contradicting
  `arr[m1] < arr[m2]`. So `i* > m1`, and dropping `[lo, m1]` is safe.
- Symmetrically, if `arr[m1] > arr[m2]`, then `i* < m2`, so dropping `[m2, hi]` is safe.

Each step removes a full third, so the window shrinks geometrically.

### Reference implementation

```python
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while hi - lo > 2:
            m1 = lo + (hi - lo) // 3
            m2 = hi - (hi - lo) // 3
            if arr[m1] < arr[m2]:
                lo = m1 + 1
            else:
                hi = m2 - 1
        # Few candidates remain; pick the largest.
        best = lo
        for i in range(lo + 1, hi + 1):
            if arr[i] > arr[best]:
                best = i
        return best
```

- **Time:** O(log₃ₐₐ₂ n) ≈ O(log n) evaluations. **Space:** O(1).

> Note: the classic LeetCode-optimal answer uses **binary search** on the predicate
> `arr[mid] > arr[mid + 1]`, which is also O(log n) with a smaller constant. Ternary
> search is shown here because it generalizes to unimodal functions where **no such
> monotone boundary predicate exists** (e.g. real-valued objectives in later problems).

## Key Insights & Edge Cases

- **Argmax, not a target.** We want the *location* of the maximum. There is no target
  value to match, which is the tell-tale sign to reach for ternary (or peak-finding)
  rather than plain binary search for equality.
- **Strict monotonicity** on each side means `arr[m1] == arr[m2]` never happens for
  `m1 != m2`, so the two-branch comparison is exhaustive.
- **Always advance past the probe** (`m1 + 1`, `m2 - 1`). Setting `lo = m1` (without
  `+1`) can stall when `hi - lo == 2` and cause an infinite loop.
- **Small windows:** stop at `hi - lo <= 2` and scan; trying to ternary-split a
  2-element window produces `m1 == m2` and makes no progress.
- The peak is guaranteed interior (`0 < i* < n - 1`) by the mountain definition, so the
  final scan never runs off the ends.
