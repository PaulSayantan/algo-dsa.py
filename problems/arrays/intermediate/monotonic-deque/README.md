# Monotonic Deque

A **monotonic deque** is a double-ended queue (`collections.deque` in Python)
whose contents you deliberately keep in sorted order — either non-increasing or
non-decreasing from front to back. Unlike a monotonic *stack*, you can push and
pop at **both** ends, which is exactly what you need to slide a fixed- or
variable-width window across an array and query its maximum or minimum in
amortized `O(1)`.

## The core idea

Suppose you are sweeping a window `[l, r]` from left to right and want the
window maximum at every step. Two facts drive the technique:

1. **A smaller element that arrives later dominates.** If a new value `nums[r]`
   is greater than the value at the back of the deque, that older, smaller value
   can never again be the maximum of any window containing `r`, so pop it. This
   keeps the deque **decreasing** from front to back.
2. **The front may fall out of the window.** When the left edge advances past the
   index stored at the front, pop the front. Because the deque is decreasing, the
   front always holds the index of the current window maximum.

Store **indices**, not values, so you can test whether the front has expired
(`front <= r - k`) and still read the value via `nums[front]`.

For a window **minimum**, keep the deque **increasing** instead (pop the back
while `nums[back] >= nums[r]`).

## When to reach for it

Reach for a monotonic deque when:

- You need the **max or min of a sliding window** of fixed size `k` in `O(n)`.
- A dynamic program has the shape `dp[i] = nums[i] + max(dp[j])` (or `min`) over
  a **contiguous window** `j in [i-k, i-1]` — the deque replaces an inner
  `O(k)` scan with `O(1)` amortized lookup (Jump Game VI, Constrained
  Subsequence Sum).
- You need the shortest/longest window satisfying a **monotone prefix-sum**
  condition (Shortest Subarray with Sum at Least K).
- You need the max/min over a window but where the window boundary itself is
  driven by a second condition (Longest Subarray with Absolute Diff <= Limit,
  Max Value of Equation).

## Complexity

- **Time:** `O(n)` — each index is pushed exactly once and popped at most once,
  so the total number of deque operations is at most `2n`, despite the inner
  `while` loops.
- **Space:** `O(k)` for a fixed window of size `k` (or `O(n)` in the worst case),
  since the deque never holds more indices than can co-exist in one window.

## Deque vs. heap for sliding-window max

A max-heap also answers window-max queries, but lazily deleting expired entries
gives `O(n log n)` time and up to `O(n)` extra space. The monotonic deque is
strictly better at `O(n)` time and `O(k)` space because it *proactively* discards
dominated elements instead of leaving them in the structure.

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [Sliding Window Maximum](problem-01-sliding-window-maximum/PROBLEM.md) | Medium/Hard | The canonical problem: max of every size-`k` window in `O(n)` with a decreasing deque of indices. |
| 2 | [Longest Subarray with Absolute Diff <= Limit](problem-02-longest-subarray-absolute-diff-limit/PROBLEM.md) | Medium | Longest window whose max minus min stays within `limit`, using two deques (one for max, one for min). |
| 3 | [Jump Game VI](problem-03-jump-game-vi/PROBLEM.md) | Medium | DP where `dp[i]` adds the best `dp` in the previous `k` indices; the deque gives the window max in `O(1)`. |
| 4 | [Constrained Subsequence Sum](problem-04-constrained-subsequence-sum/PROBLEM.md) | Hard | Max subsequence sum with a gap constraint `<= k`; deque tracks the best usable `dp` in the window. |
| 5 | [Shortest Subarray with Sum at Least K](problem-05-shortest-subarray-sum-at-least-k/PROBLEM.md) | Hard | Shortest subarray summing to `>= k` (negatives allowed) via a monotonic deque over prefix sums. |
| 6 | [Max Value of Equation](problem-06-max-value-of-equation/PROBLEM.md) | Hard | Maximize `y_i + y_j + |x_i - x_j|` under `|x_i - x_j| <= k` with a decreasing deque of `y - x`. |
