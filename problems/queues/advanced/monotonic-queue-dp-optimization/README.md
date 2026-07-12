# Monotonic-Queue DP Optimization

A DP whose transition is `dp[i] = best over a sliding window of dp + cost` would be O(nk) naively, but a monotonic deque holding the window's best candidates collapses it to O(n). Stale (out-of-window) and dominated entries are dropped as `i` advances.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Jump Game VI](problem-01-jump-game-vi/PROBLEM.md) | Windowed-max DP | Medium |
