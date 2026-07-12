# Sliding-Window Aggregate with Two Monotonic Deques

When a variable-size window must satisfy a constraint on both its maximum and its minimum, run **two** monotonic deques in lock-step: a decreasing one tracking the window max and an increasing one tracking the window min. Expand the right edge each step; whenever `max - min` violates the limit, advance the left edge and evict any deque front that falls out of the window. The invariant makes each element enter and leave both deques once, so the whole sweep is O(n) whether you want the longest valid window or a count of all valid subarrays.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](problem-01-longest-subarray-abs-diff-limit/PROBLEM.md) | Two deques, longest window | Medium |
| 2 | [Count Subarrays With Bounded Range](problem-02-count-bounded-range-subarrays/PROBLEM.md) | Two deques, subarray count | Medium |
| 3 | [Shortest Subarray With Range At Least K](problem-03-shortest-subarray-range-at-least-k/PROBLEM.md) | Two deques, shortest window | Medium |
| 4 | [Jump Game VI — Maximum Score](problem-04-jump-game-vi-max-score/PROBLEM.md) | Deque-optimized windowed DP max | Medium |
| 5 | [Maximum Sum of a Bounded-Range Subarray](problem-05-max-sum-bounded-range-subarray/PROBLEM.md) | Two deques, max window sum | Medium |
