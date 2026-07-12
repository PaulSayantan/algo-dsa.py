# Shortest Subarray with Sum ≥ K

With negative numbers allowed, the sliding-window trick fails — but a monotonic deque over *prefix sums* works. Keep prefix sums increasing in the deque; pop the front while it yields a qualifying subarray (recording the length), and pop the back to preserve monotonicity. O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Shortest Subarray with Sum at Least K](problem-01-shortest-subarray-sum-at-least-k/PROBLEM.md) | Prefix-sum deque | Hard |
