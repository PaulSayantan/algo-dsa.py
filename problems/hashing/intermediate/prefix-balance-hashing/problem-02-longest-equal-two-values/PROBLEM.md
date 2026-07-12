# Longest Subarray With Equal Counts of Two Values

**Difficulty:** Medium

**Source:** Classic — equal counts of two chosen values (balance hashing)

## Description

Given an integer array `nums` and two distinct target values `a` and `b`, return the length of the longest contiguous subarray containing an equal number of `a`s and `b`s. Values other than `a` and `b` do not affect the balance. Map `a` to `+1`, `b` to `-1`, all others to `0`, then hash the earliest index of each running balance.

## Examples

### Example 1

```
Input:  nums = [1,2,1,2,3], a = 1, b = 2
Output: 5
```

**Explanation:** The whole array has two 1s and two 2s.

### Example 2

```
Input:  nums = [5,5,5], a = 1, b = 2
Output: 3
```

**Explanation:** Neither value appears, so all counts (0 and 0) are equal.

## Hint

Same +/-1 balance idea as Contiguous Array, but only a and b move the balance; other values are neutral.
