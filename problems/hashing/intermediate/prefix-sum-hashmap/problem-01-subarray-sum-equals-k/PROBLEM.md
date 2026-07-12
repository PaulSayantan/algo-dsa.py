# Subarray Sum Equals K

**Difficulty:** Medium

**Source:** LeetCode 560 — Subarray Sum Equals K

## Description

Given an integer array `nums` and an integer `k`, return the total number of contiguous subarrays whose elements sum to exactly `k`. The array may contain negatives and zeros.

## Examples

### Example 1

```
Input:  nums = [1,1,1], k = 2
Output: 2
```

## Hint

freq[0]=1; for each x: cur+=x; count+=freq[cur-k]; freq[cur]+=1.
