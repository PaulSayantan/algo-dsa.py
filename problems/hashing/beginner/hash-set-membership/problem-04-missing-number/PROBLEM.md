# Missing Number

**Difficulty:** Easy

**Source:** LeetCode 268 — Missing Number

## Description

Given an array `nums` of `n` distinct integers taken from the range `[0, n]`, exactly one number in that range is missing. Return the missing number.

## Examples

### Example 1

```
Input:  nums = [3,0,1]
Output: 2
```

**Explanation:** n = 3, so 0..3 should be present; 2 is absent.

## Hint

Put every value in a set, then scan 0..n for the first index absent from the set.
