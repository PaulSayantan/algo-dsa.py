# Row/Column Traversal

**Row/Column Traversal** is the most fundamental matrix technique: visit every cell
of a 2D grid by looping over the rows in the outer loop and the columns in the inner
loop (row-major order), or the reverse (column-major order). It is the matrix analog
of a simple linear scan over an array.

```text
for i in range(rows):        # rows-then-cols (row-major)
    for j in range(cols):
        process(grid[i][j])
```

You reach for this technique whenever you need to **inspect, aggregate, transform, or
count** something across all (or a structured subset of) the entries of a matrix, and
the order in which you visit cells either does not matter or maps cleanly onto the two
nested indices. Common jobs include:

- Summing / finding the max or min of each row or each column.
- Counting cells that satisfy a predicate.
- Rewriting the matrix into a new shape by walking cells in a fixed order.
- Precomputing per-row and per-column statistics, then combining them.

Because every cell is touched a constant number of times, the time complexity is
**O(m * n)** for an `m x n` matrix. The extra space is **O(1)** when you only keep
running aggregates, or **O(m + n)** when you cache per-row and per-column summaries.
This is almost always optimal, since correctly answering these questions requires
reading each cell at least once.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Richest Customer Wealth](problem-01-richest-customer-wealth/PROBLEM.md) | Sum each row, return the largest row sum | Easy |
| 2 | [Count Negatives in a Sorted Matrix](problem-02-count-negatives-in-sorted-matrix/PROBLEM.md) | Count how many cells hold a negative value | Easy |
| 3 | [Reshape the Matrix](problem-03-reshape-the-matrix/PROBLEM.md) | Re-lay the cells row by row into a new `r x c` shape | Easy |
| 4 | [Lucky Numbers in a Matrix](problem-04-lucky-numbers-in-a-matrix/PROBLEM.md) | Find values that are a row minimum and a column maximum | Easy |
| 5 | [Special Positions in a Binary Matrix](problem-05-special-positions-in-binary-matrix/PROBLEM.md) | Count 1s that are alone in their row and column | Easy/Medium |
