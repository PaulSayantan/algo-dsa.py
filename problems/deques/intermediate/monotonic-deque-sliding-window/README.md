# Monotonic Deque — Sliding Window Max/Min

A **monotonic deque** keeps window candidates ordered so the extreme of the current window is always at the front. For a max query, before pushing the new index you pop from the back every index whose value is `<=` the new value (they can never beat it while it stays in the window); the front is then the window maximum. Evict the front once it slides out of the `[i-k+1, i]` range. Each index is pushed and popped once, so a full left-to-right pass is O(n) — beating the naive O(nk).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Sliding Window Maximum](problem-01-sliding-window-maximum/PROBLEM.md) | Decreasing deque, window max | Hard |
| 2 | [Sliding Window Minimum](problem-02-sliding-window-minimum/PROBLEM.md) | Increasing deque, window min | Medium |
| 3 | [Longest Continuous Subarray With Absolute Diff <= Limit](problem-03-longest-subarray-absolute-diff-limit/PROBLEM.md) | Dual deques (max+min), shrinking window | Medium |
| 4 | [Jump Game VI](problem-04-jump-game-vi/PROBLEM.md) | DP + decreasing deque for window max | Medium |
| 5 | [Continuous Subarrays](problem-05-continuous-subarrays/PROBLEM.md) | Dual deques (max+min), count windows | Medium |
