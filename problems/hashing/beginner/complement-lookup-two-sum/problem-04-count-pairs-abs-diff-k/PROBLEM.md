# Count Number of Pairs With Absolute Difference K

**Difficulty:** Easy

**Source:** LeetCode 2006 — Count Number of Pairs With Absolute Difference K

## Description

Given an integer array `nums` and an integer `k` (k >= 1), return the number of pairs `(i, j)` with `i < j` and `|nums[i] - nums[j]| == k`. Every index pair counts (duplicates are not collapsed).

## Examples

### Example 1

```
Input:  nums = [1,2,2,1], k = 1
Output: 4
```

**Explanation:** Pairs (0,1),(0,2),(1,3),(2,3).

## Hint

One pass with a frequency map: for each x add freq[x-k] + freq[x+k] of earlier elements.
