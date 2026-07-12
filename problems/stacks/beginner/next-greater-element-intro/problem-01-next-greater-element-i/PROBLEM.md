# Next Greater Element I

**Difficulty:** Easy

**Source:** LeetCode 496 — Next Greater Element I

## Description

You are given two distinct-integer arrays `nums1` (a subset of `nums2`) and `nums2`. For each `nums1[i]`, find the next greater element to its right in `nums2`; if none exists, use `-1`. Return the answers in `nums1` order.

## Examples

### Example 1

```
Input:  nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
```

## Hint

Precompute next-greater for every value in nums2 with a decreasing stack, then look up.
