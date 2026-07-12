# Find K Pairs with Smallest Sums

**Difficulty:** Medium

**Source:** LeetCode 373 — Find K Pairs with Smallest Sums

## Description

Given two ascending arrays `nums1` and `nums2` and an integer `k`, return the `k` pairs `[a, b]` (a from `nums1`, b from `nums2`) with the smallest sums, in non-decreasing sum order.

## Examples

### Example 1

```
Input:  nums1=[1,7,11], nums2=[2,4,6], k=3
Output: [[1,2],[1,4],[1,6]]
```

## Hint

Min-heap seeded with (nums1[i]+nums2[0], i, 0); on pop, push the next j for that i.
