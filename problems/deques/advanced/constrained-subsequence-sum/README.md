# Constrained Subsequence Sum

This DP — the max sum of a subsequence where consecutive chosen indices are at most `k` apart — has transition `dp[i] = nums[i] + max(0, max(dp[i-k..i-1]))`. A monotonic deque maintains that sliding-window maximum of `dp`, turning an O(nk) recurrence into O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Constrained Subsequence Sum](problem-01-constrained-subsequence-sum/PROBLEM.md) | Windowed-max DP | Hard |
