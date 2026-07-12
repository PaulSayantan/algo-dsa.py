# 132 Pattern

**Difficulty:** Medium

**Source:** LeetCode 456 — 132 Pattern

## Description

Given an array `nums`, return `True` if there is a *132 pattern*: a subsequence of indices `i < j < k` such that `nums[i] < nums[k] < nums[j]`. Otherwise return `False`.

## Examples

### Example 1

```
Input:  nums = [3,1,4,2]
Output: true
```

**Explanation:** [1,4,2] is a 132 pattern.

## Hint

Scan right-to-left; keep a decreasing stack and the max popped value as the '2'; a smaller current element wins.
