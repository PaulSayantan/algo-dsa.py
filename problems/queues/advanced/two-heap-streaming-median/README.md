# Two-Heap Streaming Median

Maintaining the median of a growing stream uses two priority queues: a max-heap for the lower half and a min-heap for the upper half, kept balanced in size. The median is then the top of one heap (odd count) or the average of both tops (even). Each insert is O(log n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Find Median from Data Stream](problem-01-find-median-from-stream/PROBLEM.md) | Balanced two heaps | Hard |
