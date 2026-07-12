# Sliding-Window Median

Reporting the median of every length-`k` window combines a balanced structure with window bookkeeping. A simple correct approach keeps the current window in a sorted list (binary-search insert/delete); the median is then read from the middle. Larger inputs use two heaps with lazy deletion.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Sliding Window Median](problem-01-sliding-window-median/PROBLEM.md) | Ordered-window median | Hard |
