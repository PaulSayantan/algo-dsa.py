# Maximal Rectangle in Binary Matrix

Reduce a 2D problem to the 1D histogram: for each row, treat the column of consecutive 1s ending at that row as bar heights, then run largest-rectangle-in-histogram. Sweeping every row gives the largest all-1 rectangle in O(rows × cols).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Maximal Rectangle](problem-01-maximal-rectangle/PROBLEM.md) | Row histograms | Hard |
