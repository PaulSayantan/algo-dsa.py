# Trapping Rain Water (Stack)

Water is trapped between a taller left bar and a taller right bar. A monotonically decreasing stack of indices captures this: when a taller bar arrives, pop the shorter bars it 'closes off', and for each add the water held between the popped bar's neighbors, level by level, in O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Trapping Rain Water](problem-01-trapping-rain-water/PROBLEM.md) | Layered trapping | Hard |
| 2 | [Daily Temperatures](problem-02-daily-temperatures/PROBLEM.md) | Decreasing stack of indices, index-gap resolution | Medium |
| 3 | [Sum of Subarray Minimums](problem-03-sum-of-subarray-minimums/PROBLEM.md) | Left/right span counting via monotonic stack | Medium |
| 4 | [Online Stock Span](problem-04-online-stock-span/PROBLEM.md) | Decreasing (price, span) stack, span folding | Medium |
| 5 | [Next Greater Element II](problem-05-next-greater-element-ii/PROBLEM.md) | Circular decreasing stack of indices | Medium |
