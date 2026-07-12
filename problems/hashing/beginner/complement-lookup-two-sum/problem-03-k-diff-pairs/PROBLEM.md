# K-diff Pairs in an Array

**Difficulty:** Medium

**Source:** LeetCode 532 — K-diff Pairs in an Array

## Description

Given an integer array `nums` and an integer `k`, return the number of **unique** k-diff pairs. A k-diff pair is `(nums[i], nums[j])` with `i != j` and `|nums[i] - nums[j]| == k`. Uniqueness is by value pair, not by index.

## Examples

### Example 1

```
Input:  nums = [3,1,4,1,5], k = 2
Output: 2
```

**Explanation:** The 2-diff pairs are (1,3) and (3,5).

### Example 2

```
Input:  nums = [1,3,1,5,4], k = 0
Output: 1
```

**Explanation:** Only the value 1 appears twice.

## Hint

Deduplicate with a Counter. For k>0 check if x+k exists; for k==0 count values appearing >= 2 times.
