# Maximum Distance Between Equal Values

**Difficulty:** Easy

**Source:** Classic — first-seen index distance

## Description

Given an integer array `nums`, return the maximum value of `j - i` over all pairs with `i < j` and `nums[i] == nums[j]`. If no value repeats, return `0`.

## Examples

### Example 1

```
Input:  nums = [1,2,3,1,2,3]
Output: 3
```

**Explanation:** Value 1 spans indices 0 and 3.

## Hint

Record only the FIRST index of each value; the farthest later occurrence maximizes the span.
