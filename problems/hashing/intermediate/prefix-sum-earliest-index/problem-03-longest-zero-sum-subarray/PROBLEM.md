# Longest Zero-Sum Subarray

**Difficulty:** Medium

**Source:** Classic (GfG) — Largest subarray with sum 0

## Description

Given an integer array `nums`, return the length of the longest contiguous subarray whose elements sum to zero.

## Examples

### Example 1

```
Input:  nums = [15,-2,2,-8,1,7,10,23]
Output: 5
```

## Hint

Equal prefix sums bound a zero-sum range; keep the earliest index of each prefix sum.
