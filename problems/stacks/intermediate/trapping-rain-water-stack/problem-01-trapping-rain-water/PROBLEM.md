# Trapping Rain Water

**Difficulty:** Hard

**Source:** LeetCode 42 — Trapping Rain Water

## Description

Given `height` representing an elevation map where each bar has width 1, compute how much water it can trap after raining.

## Examples

### Example 1

```
Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

## Hint

Decreasing stack of indices; on a taller bar, pop and add water = width * (min(sides) - popped height).
