# Jump Game VI

Reaching the end by hopping 1..k with maximum accumulated score is a windowed DP: `dp[i] = nums[i] + max(dp[i-k..i-1])`. A monotonic deque keeps the window's best `dp` at its front, so each index is processed in amortized O(1).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Jump Game VI](problem-01-jump-game-vi/PROBLEM.md) | Max-reachable DP | Medium |
