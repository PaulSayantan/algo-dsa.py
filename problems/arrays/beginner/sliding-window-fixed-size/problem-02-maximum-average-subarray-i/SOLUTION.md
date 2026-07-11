# Solution — Maximum Average Subarray I

## Brute Force

Try every start index `i`, sum the `k` elements of that window, divide by `k`, and
keep the largest average.

```python
best = float("-inf")
for i in range(len(nums) - k + 1):
    best = max(best, sum(nums[i:i + k]) / k)
return best
```

- **Time:** O(n·k) — each of ~`n` windows re-sums `k` elements.
- **Space:** O(1)

For `n = 10^5` and large `k` this is too slow.

## Optimal Approach (Sliding Window, Fixed Size)

Because `k` is constant, `average = sum / k`, so the window with the maximum sum also
has the maximum average. We therefore track only the running **sum** and divide once at
the end.

1. `window_sum = sum(nums[0..k-1])`; set `best_sum = window_sum`.
2. Slide: for `right` from `k` to `n - 1`, do
   `window_sum += nums[right] - nums[right - k]` and
   `best_sum = max(best_sum, window_sum)`.
3. Return `best_sum / k`.

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best_sum = window_sum
        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[right - k]
            best_sum = max(best_sum, window_sum)
        return best_sum / k
```

**Why it is correct:** Dividing by the *fixed* constant `k` is a monotonic
transformation, so `argmax(sum) == argmax(sum / k)`. The sliding sum visits every
length-`k` window exactly once (the running sum after step `right` equals
`sum(nums[right-k+1 .. right])`), so `best_sum` is the global maximum window sum and
`best_sum / k` is the maximum average.

**Step by step** on `nums = [1, 12, -5, -6, 50, 3], k = 4`:

1. First window `[1,12,-5,-6]` → `window_sum = 2`, `best_sum = 2`.
2. `right=4`: `+50 -1` → `2 + 50 - 1 = 51` (window `[12,-5,-6,50]`), `best_sum = 51`.
3. `right=5`: `+3 -12` → `51 + 3 - 12 = 42` (window `[-5,-6,50,3]`), `best_sum = 51`.

Answer: `51 / 4 = 12.75`.

## Key Insights & Edge Cases

- **Divide only once, at the end.** Maximizing the integer sum avoids repeated
  floating-point division inside the loop and keeps the comparison exact.
- **Seed with the first window sum, not `0`** — arrays can be entirely negative, so
  `0` is not a safe lower bound.
- **`k == n`:** a single window (the whole array); the loop does not run and the answer
  is `sum(nums) / n`.
- **Return a float:** in Python, `best_sum / k` already produces a float even when the
  division is exact.
