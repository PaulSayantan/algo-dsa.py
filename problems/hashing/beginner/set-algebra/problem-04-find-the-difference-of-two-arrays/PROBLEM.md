# Find the Difference of Two Arrays

**Difficulty:** Easy

**Source:** LeetCode 2215 — Find the Difference of Two Arrays

## Description

Given integer arrays `nums1` and `nums2`, return a list `answer` of size 2 where `answer[0]` is a list of the **distinct** integers in `nums1` that are not in `nums2`, and `answer[1]` is a list of the distinct integers in `nums2` that are not in `nums1`. The reference returns each list **sorted** so the oracle is deterministic.

## Examples

### Example 1

```
Input:  nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
```

## Hint

Take set differences s1 - s2 and s2 - s1; sort each and return the pair.
