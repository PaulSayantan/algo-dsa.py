# Intersection of Two Arrays

**Difficulty:** Easy

**Source:** LeetCode 349 — Intersection of Two Arrays

## Description

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be **unique**, and you may return it in any order. Here the reference returns the result **sorted ascending** so the oracle is deterministic.

## Examples

### Example 1

```
Input:  nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

### Example 2

```
Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

## Hint

Intersect the two sets: set(nums1) & set(nums2). Sort the result before returning.
