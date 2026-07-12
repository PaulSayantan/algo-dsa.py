# Double-Ended Priority Queue (Min-Max Heap)

A double-ended priority queue supports extracting BOTH the minimum and the maximum efficiently. One practical implementation pairs a min-heap and a max-heap with lazy deletion (a validity map), so `popMin` and `popMax` each run in amortized O(log n) — the min-max-heap use case.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Double-Ended Priority Queue](problem-01-double-ended-priority-queue/PROBLEM.md) | Min+max heaps, lazy delete | Hard |
