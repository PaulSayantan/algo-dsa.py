# Maximal Rectangle

**Difficulty:** Medium

**Source:** LeetCode 85 — Maximal Rectangle

## Description

Given a `matrix` of `0`s and `1`s (a list of equal-length rows), return the area of the largest rectangle containing only `1`s.

Constraints: `0 <= rows, cols`; every entry is `0` or `1`. An empty matrix (or a matrix with empty rows) has area `0`.

## Examples

### Example 1

```
Input:  matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
Output: 6
```

**Explanation:** The `1`s spanning columns 2-4 of the bottom two full rows form a 2x3 block, area 6.

### Example 2

```
Input:  matrix = [[1,1],[1,1]]
Output: 4
```

**Explanation:** The whole 2x2 block is all `1`s.

## Hint

Treat each row as the base of a histogram whose bar heights are the counts of consecutive `1`s reaching up; run largest-rectangle-in-histogram on every row and keep the max.
