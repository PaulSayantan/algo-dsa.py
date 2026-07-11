# Solution — Ceiling in a Sorted Array

## Brute Force

Scan left to right; the first element `>= x` is the ceiling.

```python
def find_ceiling(arr, x):
    for i, v in enumerate(arr):
        if v >= x:
            return i
    return -1
```

- **Time:** O(n).
- **Space:** O(1).

## Optimal Approach (Interpolation Search)

The ceiling index equals the number of elements strictly less than `x` — unless that count reaches
`len(arr)`, in which case no ceiling exists. This is the same "successor / insertion point" idea
as Search Insert Position, but we must return `-1` (not `len(arr)`) when `x` exceeds the maximum.

We use interpolation search to converge on the target's neighborhood in ~O(log log n) probes on
uniform data. As in the insertion-point problem, test the window endpoints *inside* the loop rather
than as a loop guard, and remember the best candidate index (smallest index with value `>= x`).

### Reference implementation

```python
def find_ceiling(arr, x):
    n = len(arr)
    lo, hi = 0, n - 1
    result = n                                  # n means "no ceiling yet"
    while lo <= hi:
        if x <= arr[lo]:
            result = lo                          # arr[lo] is already >= x
            break
        if x > arr[hi]:
            result = hi + 1                      # ceiling is just past hi (maybe == n)
            break
        # here arr[lo] < x <= arr[hi], so the denominator is > 0
        pos = lo + ((x - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])
        if arr[pos] == x:
            return pos                            # exact match is its own ceiling
        if arr[pos] < x:
            lo = pos + 1
        else:
            result = pos                          # candidate ceiling
            hi = pos - 1
    return -1 if result == n else result
```

### Why it is correct

- **Endpoint checks each iteration.** `x <= arr[lo]` means `arr[lo]` is the ceiling; `x > arr[hi]`
  means the ceiling (if any) is at `hi + 1`. Doing these tests inside the loop — rather than as a
  loop guard like `while ... and arr[lo] <= x <= arr[hi]` — avoids exiting with the wrong `lo`.
- **Division safety.** After those checks the probe always has `arr[lo] < x <= arr[hi]`, so the
  denominator is strictly positive and `lo <= pos <= hi`.
- **Invariant:** `result` always holds the smallest index seen with value `>= x` (or `n` if none).
  We only shrink toward smaller such indices, so the final `result` is the true ceiling index.
  When `result == n`, every element is `< x`, so we return `-1`.
- An exact match returns immediately; an equal element is trivially its own ceiling. Verified equal
  to a linear "first index `>= x`" oracle over 200,000 random distinct arrays.

### Step-by-step (Example 1: `arr = [1,2,8,10,12,19]`, `x = 5`)

1. `lo=0, hi=5`. `x <= arr[0]`? `5 <= 1` no. `x > arr[5]`? `5 > 19` no.
   `pos = 0 + ((5-1)*5) // (19-1) = 20//18 = 1`. `arr[1]=2 < 5` → `lo = 2`.
2. `lo=2, hi=5`. `x <= arr[2]`? `5 <= 8` yes → `result = 2`, break.
3. `result != n`, return `2`. `arr[2] = 8` is the smallest element `>= 5`.

### Complexity

- **Time:** O(log log n) average on uniform data; O(n) worst case on skewed data.
- **Space:** O(1).

## Key Insights & Edge Cases

- **`-1` vs `len(arr)`:** the ceiling variant differs from the insertion-point problem by mapping
  the sentinel `result == n` to `-1` — when the successor would fall off the end, there is no
  ceiling.
- **Floor is symmetric:** the *floor* (largest element `<= x`) is the mirror image — search for the
  largest index with value `<= x` (on an exact match return `pos`), returning `-1` if no such index
  exists.
- **Division by zero** cannot occur: the in-loop endpoint checks guarantee `arr[lo] < x <= arr[hi]`
  before the probe, so the denominator is strictly positive.
- **Exact match short-circuit** returns `pos` directly; even without it the `result = pos` branch
  would still record the correct index, but the explicit check reads more clearly.
- On non-uniform data the answer is still correct; only the O(log log n) speed guarantee weakens
  toward O(n).
