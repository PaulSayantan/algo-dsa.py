# Count Nice Pairs in an Array

**Difficulty:** Medium

**Source:** LeetCode 1814 — Count Nice Pairs in an Array

## Description

Given an array `nums`, let `rev(x)` be `x` with its decimal digits reversed. A pair `(i, j)` with `i < j` is **nice** when `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`. Rearranging, this is `nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])`, so group by that key. Return the count modulo `10**9 + 7`.

## Examples

### Example 1

```
Input:  nums = [42,11,1,97]
Output: 2
```

**Explanation:** Nice pairs: (0,3) and (1,2).

### Example 2

```
Input:  nums = [13,10,35,24,76]
Output: 4
```

## Hint

Key each element by (num - rev(num)); accumulate count[key] before incrementing it.
