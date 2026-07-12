# Largest Rectangle in Histogram

**Difficulty:** Hard

**Source:** LeetCode 84 — Largest Rectangle in Histogram

## Description

Given an array `heights` representing the heights of bars of width 1, return the area of the largest rectangle that fits entirely within the histogram.

## Examples

### Example 1

```
Input:  heights = [2,1,5,6,2,3]
Output: 10
```

**Explanation:** The 5,6 bars give 5*2 = 10.

## Hint

Increasing stack of indices; pop on a shorter bar and compute height*width using the new boundary.
