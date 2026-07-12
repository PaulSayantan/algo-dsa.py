# Sliding-Window Metrics (Range with Two Deques)

Running two monotonic deques over a **fixed-size** window gives the window max (decreasing deque) and window min (increasing deque) simultaneously, so derived per-window metrics like the range `max - min` come for free. Push each index into both deques, evict any front that has slid out of the `[i-k+1, i]` window, and once the first full window forms read both fronts. The sweep stays O(n) and supports either emitting the metric per window or counting the windows that satisfy a threshold.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Range of Each Sliding Window](problem-01-window-range-per-window/PROBLEM.md) | Two deques, per-window range | Medium |
| 2 | [Count Stable Windows](problem-02-count-stable-windows/PROBLEM.md) | Two deques, threshold count | Medium |
| 3 | [Sum of Window Max and Min](problem-03-window-max-plus-min/PROBLEM.md) | Two deques, per-window max+min | Medium |
| 4 | [Count Windows With Range Equal to Target](problem-04-count-windows-range-equals-target/PROBLEM.md) | Two deques, exact-range count | Medium |
| 5 | [Longest Bounded-Ratio Subarray](problem-05-longest-bounded-ratio-subarray/PROBLEM.md) | Two deques, variable-width window | Medium |
