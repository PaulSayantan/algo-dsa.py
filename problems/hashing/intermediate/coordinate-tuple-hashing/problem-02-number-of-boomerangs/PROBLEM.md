# Number of Boomerangs

**Difficulty:** Medium

**Source:** LeetCode 447 — Number of Boomerangs

## Description

A boomerang is a tuple of points `(i, j, k)` such that the distance from `i` to `j` equals the distance from `i` to `k` (order matters). Return the number of boomerangs.

## Examples

### Example 1

```
Input:  points = [[0,0],[1,0],[2,0]]
Output: 2
```

## Hint

Per anchor, hash squared distances; a group of size c contributes c*(c-1) ordered pairs.
