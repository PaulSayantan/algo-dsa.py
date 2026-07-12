# Longest Subarray With At Most K Distinct Integers

**Difficulty:** Medium

**Source:** Classic — longest at-most-K-distinct window

## Description

Given an integer array `nums` and an integer `k`, return the length of the longest contiguous subarray containing at most `k` distinct integers. `k = 0` returns `0`.

## Examples

### Example 1

```
Input:  nums = [1,2,1,2,3], k = 2
Output: 4
```

**Explanation:** [1,2,1,2] has 2 distinct values and length 4.

## Hint

Grow the right edge; shrink left while distinct count > k; track the max width.
