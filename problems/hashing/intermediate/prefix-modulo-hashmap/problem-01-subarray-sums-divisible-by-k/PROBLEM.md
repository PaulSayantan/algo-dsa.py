# Subarray Sums Divisible by K

**Difficulty:** Medium

**Source:** LeetCode 974 — Subarray Sums Divisible by K

## Description

Given an integer array `nums` and an integer `k`, return the number of non-empty contiguous subarrays whose sum is divisible by `k`. The array may contain negatives; keep remainders in `[0, k)`.

## Examples

### Example 1

```
Input:  nums = [4,5,0,-2,-3,1], k = 5
Output: 7
```

## Hint

Count pairs of equal prefix remainders: count += freq[cur%k]; then freq[cur%k]+=1.
