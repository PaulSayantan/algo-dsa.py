# Solution — Number of Sub-arrays of Size K and Average ≥ Threshold

## Brute Force

For each start index `i`, sum the window `arr[i..i+k-1]`, compute its average, and
increment a counter when the average meets `threshold`.

```python
count = 0
for i in range(len(arr) - k + 1):
    if sum(arr[i:i + k]) / k >= threshold:
        count += 1
return count
```

- **Time:** O(n·k) — every window re-sums `k` elements.
- **Space:** O(1)

## Optimal Approach (Sliding Window, Fixed Size)

Two simplifications make this clean and fast:

1. **Compare sums, not averages.** `sum / k >= threshold` is equivalent to
   `sum >= k * threshold`. Precompute `target = k * threshold` once so the whole
   algorithm stays in integer arithmetic (no floating-point error).
2. **Slide the sum** instead of recomputing it: add the entering element and subtract
   the leaving element on each step.

Steps:

1. `target = k * threshold`.
2. `window_sum = sum(arr[0..k-1])`; `count = 1 if window_sum >= target else 0`.
3. For `right` from `k` to `n - 1`:
   - `window_sum += arr[right] - arr[right - k]`.
   - If `window_sum >= target`, `count += 1`.
4. Return `count`.

```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0
        for right in range(k, len(arr)):
            window_sum += arr[right] - arr[right - k]
            if window_sum >= target:
                count += 1
        return count
```

**Why it is correct:** `sum >= k * threshold  ⇔  sum / k >= threshold` for `k > 0`, so
counting windows by sum gives the same result as counting by average — with no rounding
issues. The running sum equals the current window's sum at each step, and every
length-`k` window is examined exactly once, so the count is exact. Note the first
window (initialized before the loop) must be counted too — that is why `count` starts
at `1` or `0` based on it.

**Step by step** on `arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4`, so `target = 12`:

1. First window `[2,2,2]` → `window_sum = 6` (< 12), `count = 0`.
2. `right=3`: `6 + 2 - 2 = 6` `[2,2,2]` → `count = 0`.
3. `right=4`: `6 + 5 - 2 = 9` `[2,2,5]` → `count = 0`.
4. `right=5`: `9 + 5 - 2 = 12` `[2,5,5]` → `>= 12`, `count = 1`.
5. `right=6`: `12 + 5 - 2 = 15` `[5,5,5]` → `count = 2`.
6. `right=7`: `15 + 8 - 5 = 18` `[5,5,8]` → `count = 3`.

Answer: `3`.

## Key Insights & Edge Cases

- **Integer comparison beats float comparison.** Using `sum >= k * threshold` sidesteps
  both precision bugs and per-step division cost.
- **Do not forget the first window.** A common off-by-one bug is starting the loop at
  index `k` but never checking the initial window; initialize `count` from it.
- **`k == n`:** exactly one window (the whole array); the loop is skipped and the answer
  is `0` or `1`.
- Because all values are positive, sums only stay bounded by `n * 10^4`, well within
  native integer range.
