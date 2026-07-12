# Line Reflection

**Difficulty:** Medium

**Source:** LeetCode 356 — Line Reflection

## Description

Given `n` points, determine whether there exists a vertical line such that reflecting every point across it maps the set of points onto itself.

## Examples

### Example 1

```
Input:  points = [[1,1],[-1,1]]
Output: true
```

## Hint

The line must be x=(minX+maxX)/2; every point's mirror (sum-x, y) must be in the set.
