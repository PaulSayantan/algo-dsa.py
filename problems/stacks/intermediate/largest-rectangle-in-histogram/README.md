# Largest Rectangle in Histogram

For each bar, the widest rectangle of that bar's height extends until a strictly shorter bar on each side. A monotonic increasing stack of bar indices finds those left/right boundaries in a single O(n) pass: when a shorter bar arrives, pop taller bars and compute the area each one bounds.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Largest Rectangle in Histogram](problem-01-largest-rectangle-in-histogram/PROBLEM.md) | Left/right smaller bounds | Hard |
| 2 | [Widest Full-Height Span](problem-02-largest-rectangle-all-ones-row/PROBLEM.md) | Histogram, edge cases | Medium |
| 3 | [Maximal Rectangle](problem-03-maximal-rectangle/PROBLEM.md) | Per-row histogram of 1s | Medium |
| 4 | [Maximum Score of a Good Subarray](problem-04-maximum-score-of-a-good-subarray/PROBLEM.md) | Prev/next-smaller bounds covering k | Medium |
| 5 | [Count Submatrices With All Ones](problem-05-count-submatrices-with-all-ones/PROBLEM.md) | Histogram, sum of subarray minima | Medium |
