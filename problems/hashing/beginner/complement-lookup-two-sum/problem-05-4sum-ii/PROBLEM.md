# 4Sum II

**Difficulty:** Medium

**Source:** LeetCode 454 — 4Sum II

## Description

Given four integer arrays `nums1`, `nums2`, `nums3`, `nums4`, all of length `n`, return the number of tuples `(i, j, k, l)` such that `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`.

## Examples

### Example 1

```
Input:  nums1=[1,2], nums2=[-2,-1], nums3=[-1,2], nums4=[0,2]
Output: 2
```

## Hint

Hash every a+b sum with its multiplicity, then for each c+d look up -(c+d). Splits O(n^4) into O(n^2).
