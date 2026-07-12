# Minimum Area Rectangle

**Difficulty:** Medium

**Source:** LeetCode 939 — Minimum Area Rectangle

## Description

Given points on a plane, find the minimum area of an axis-aligned rectangle formed from four of the points (sides parallel to the axes). Return 0 if no such rectangle exists.

## Examples

### Example 1

```
Input:  points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
```

## Hint

Store points in a set; for each diagonal pair (x1<x2,y1<y2) check (x1,y2) and (x2,y1).
