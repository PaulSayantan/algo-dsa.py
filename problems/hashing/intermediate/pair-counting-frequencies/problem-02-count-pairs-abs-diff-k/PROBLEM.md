# Count Pairs With Absolute Difference K

**Difficulty:** Easy

**Source:** LeetCode 2006 — Count Number of Pairs With Absolute Difference K

## Description

Given an integer array `nums` and an integer `k`, return the number of pairs `(i, j)` with `i < j` and `|nums[i] - nums[j]| == k`. Count complements on the fly with a running frequency map.

## Examples

### Example 1

```
Input:  nums = [1,2,2,1], k = 1
Output: 4
```

**Explanation:** The 4 pairs are (0,1),(0,2),(2,3),(1,3).

### Example 2

```
Input:  nums = [3,2,1,5,4], k = 2
Output: 3
```

**Explanation:** Pairs with difference 2: (3,1),(3,5),(5,... ) -> 3 in total.

## Hint

For each x, add count[x-k] + count[x+k] (values seen so far), then record x.
