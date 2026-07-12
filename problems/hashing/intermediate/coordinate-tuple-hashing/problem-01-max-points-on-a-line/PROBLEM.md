# Max Points on a Line

**Difficulty:** Hard

**Source:** LeetCode 149 — Max Points on a Line

## Description

Given `points` on a 2D plane, return the maximum number of points that lie on the same straight line.

## Examples

### Example 1

```
Input:  points = [[1,1],[2,2],[3,3]]
Output: 3
```

## Hint

For each anchor, hash GCD+sign-normalized (dx,dy) slope keys; take the max bucket + 1.
