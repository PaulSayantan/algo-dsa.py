# 4Sum II

**Difficulty:** Medium

**Source:** LeetCode 454 — 4Sum II

## Description

Given four integer arrays `nums1`, `nums2`, `nums3`, `nums4` of equal length `n`, return the number of index tuples `(i, j, k, l)` such that `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`. Hash every pair sum from the first two arrays, then for each pair sum of the last two look up its negation.

## Examples

### Example 1

```
Input:  nums1=[1,2], nums2=[-2,-1], nums3=[-1,2], nums4=[0,2]
Output: 2
```

**Explanation:** Two tuples sum to zero: (0,0,0,1) and (1,1,0,0).

### Example 2

```
Input:  nums1=[0], nums2=[0], nums3=[0], nums4=[0]
Output: 1
```

## Hint

Counter over all a+b; answer is sum of ab[-(c+d)] across the other two arrays.
