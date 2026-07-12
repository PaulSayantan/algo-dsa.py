# Contains Duplicate II

**Difficulty:** Easy

**Source:** LeetCode 219 — Contains Duplicate II

## Description

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` such that `nums[i] == nums[j]` and `|i - j| <= k`.

## Examples

### Example 1

```
Input:  nums = [1,2,3,1], k = 3
Output: true
```

### Example 2

```
Input:  nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Hint

Keep each value's most-recent index; on a repeat, check whether the gap is at most k.
