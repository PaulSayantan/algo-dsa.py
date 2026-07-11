# Solution — Interpolation Search Basics

## Brute Force

Scan the array left to right and compare each element with `x`.

```python
def linear_search(arr, x):
    for i, v in enumerate(arr):
        if v == x:
            return i
    return -1
```

- **Time:** O(n) — every element may be inspected.
- **Space:** O(1).

This ignores the sortedness of the data entirely. Binary search improves it to O(log n), but on
uniformly distributed data we can do even better.

## Optimal Approach (Interpolation Search)

Interpolation search keeps a window `[lo, hi]` and, instead of probing the midpoint, estimates the
probe index by assuming the values increase linearly with the index:

```
pos = lo + ((x - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])
```

`(x - arr[lo]) / (arr[hi] - arr[lo])` is the fractional position of `x` between the endpoint
values; multiplying by the window length `(hi - lo)` maps that fraction onto an index.

### Reference implementation

```python
def interpolation_search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi and arr[lo] <= x <= arr[hi]:
        if arr[lo] == arr[hi]:          # single value left in window
            return lo if arr[lo] == x else -1
        pos = lo + ((x - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1
```

### Why it is correct

- **Loop guard `arr[lo] <= x <= arr[hi]`.** If `x` is outside the endpoint values it cannot be in
  the window, so the loop stops immediately and returns `-1`. Inside the window this guarantees
  `lo <= pos <= hi`, so `pos` is always a valid index.
- **Progress.** On every iteration where we do not return, we either move `lo` strictly past `pos`
  or `hi` strictly before `pos`, so the window shrinks and the loop terminates.
- **Distinct + sorted** means at most one index holds `x`, so returning the first match is correct.

### Step-by-step (Example 1: `arr = [10..100]`, `x = 70`)

1. `lo = 0`, `hi = 9`, `arr[lo] = 10`, `arr[hi] = 100`.
2. `pos = 0 + ((70 - 10) * 9) // (100 - 10) = (60 * 9)//90 = 540//90 = 6`.
3. `arr[6] == 70` → return `6`. One probe, because the data is perfectly uniform.

### Complexity

- **Time:** O(log log n) average on uniformly distributed data; O(n) worst case if the data is
  heavily skewed (the probe repeatedly lands one step from the boundary).
- **Space:** O(1).

## Key Insights & Edge Cases

- **Division by zero:** when `arr[lo] == arr[hi]` the denominator is 0. With distinct values this
  only happens once the window has collapsed to a single index, so handle it explicitly (compare
  and return). This guard is essential even here for `lo == hi` windows.
- **Single-element array:** `lo == hi == 0`; the `arr[lo] == arr[hi]` branch returns `0` or `-1`.
- **Target absent but in range** (Example 2, `x = 5`): probes narrow the window until either the
  guard `arr[lo] <= x <= arr[hi]` fails or the collapsed window mismatches → `-1`.
- **Integer arithmetic:** multiply *before* dividing to avoid truncating the fraction to 0.
  Python's arbitrary-precision integers avoid overflow; in C/Java use a wider type or reorder.
- **Not uniform?** The algorithm is still *correct* on any sorted array, only the speed guarantee
  is lost. When the distribution is unknown, binary search's O(log n) worst case is safer.
