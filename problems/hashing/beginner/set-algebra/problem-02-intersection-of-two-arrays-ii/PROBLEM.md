# Intersection of Two Arrays II

**Difficulty:** Easy

**Source:** LeetCode 350 — Intersection of Two Arrays II

## Description

Given two integer arrays `nums1` and `nums2`, return their intersection **with multiplicity**: each element appears as many times as it shows in both arrays. The result may be in any order; the reference returns it **sorted** for a deterministic oracle.

## Examples

### Example 1

```
Input:  nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

### Example 2

```
Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

## Hint

Count one array with a Counter; for each element of the other, emit it while its remaining count is positive.
