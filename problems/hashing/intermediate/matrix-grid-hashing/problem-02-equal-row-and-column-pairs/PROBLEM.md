# Equal Row and Column Pairs

**Difficulty:** Medium

**Source:** LeetCode 2352 — Equal Row and Column Pairs

## Description

Given an `n x n` integer matrix `grid`, return the number of pairs `(Ri, Cj)` such that row `Ri` and column `Cj` are equal as ordered sequences.

## Examples

### Example 1

```
Input:  grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
```

## Hint

Hash each row as a tuple with its multiplicity; for each column tuple add the row count.
