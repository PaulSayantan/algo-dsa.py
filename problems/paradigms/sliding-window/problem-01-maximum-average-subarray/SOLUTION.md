# Maximum Average Subarray I — Solution

## Brute Force

For every possible starting index `i` from `0` to `n - k`, sum the `k` elements
`nums[i .. i + k - 1]`, divide by `k`, and track the maximum average.

```python
best = float("-inf")
for i in range(len(nums) - k + 1):
    s = sum(nums[i:i + k])
    best = max(best, s / k)
return best
```

- **Time:** O(n · k) — each of the O(n) windows costs O(k) to re-sum.
- **Space:** O(1).

This recomputes almost the entire sum every step, which is wasteful because two
adjacent windows overlap in `k - 1` elements.

## Optimal Approach (Sliding Window)

Since the window length is **fixed** at `k`, the sum of a window and the sum of the
next window differ by exactly two elements: the one that leaves on the left and the
one that enters on the right.

1. Compute the sum of the first window `nums[0 .. k - 1]`. Call it `window_sum`.
   Initialize `best = window_sum`.
2. For each `right` from `k` to `n - 1`:
   - Add the incoming element: `window_sum += nums[right]`.
   - Subtract the outgoing element: `window_sum -= nums[right - k]`.
   - Update `best = max(best, window_sum)`.
3. Return `best / k`.

We compare sums (not averages) inside the loop because `k` is constant, so dividing
only once at the end avoids repeated floating-point division and keeps the comparison
exact on integers.

**Why it is correct:** After step 2's two updates, `window_sum` always equals the sum
of the contiguous block of exactly `k` elements ending at index `right`. Every
length-`k` window is visited exactly once, so the maximum over all of them is found.

```python
window_sum = sum(nums[:k])
best = window_sum
for right in range(k, len(nums)):
    window_sum += nums[right] - nums[right - k]
    best = max(best, window_sum)
return best / k
```

- **Time:** O(n) — one pass, O(1) work per step.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Fixed-size window:** the "add one, remove one" trick keeps the running sum in
  O(1) per slide. This is the defining move for fixed-window problems.
- **Divide once at the end.** Comparing raw sums avoids floating-point drift and is
  cheaper.
- **k == n:** there is a single window; the loop body never runs and you return the
  total sum divided by `n`.
- **k == 1:** the answer is simply the maximum element (as a float).
- **Negative numbers:** initializing `best` to the first window's sum (not `0`)
  matters — a naive `best = 0` would be wrong for all-negative arrays.
- **Integer overflow:** not a concern in Python, but in fixed-width languages the
  worst-case sum is about `10^5 · 10^4 = 10^9`, which fits in a 64-bit integer.
