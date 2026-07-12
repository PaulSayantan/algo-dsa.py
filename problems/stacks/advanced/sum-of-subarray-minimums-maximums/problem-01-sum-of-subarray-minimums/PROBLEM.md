# Sum of Subarray Minimums

**Difficulty:** Medium

**Source:** LeetCode 907 — Sum of Subarray Minimums

## Description

Given an array `arr`, return the sum of `min(b)` over every (contiguous) subarray `b` of `arr`. Since the answer may be large, return it modulo `10**9 + 7`.

## Examples

### Example 1

```
Input:  arr = [3,1,2,4]
Output: 17
```

## Hint

For each element count subarrays where it is the min via nearest-smaller spans (strict one side to avoid double count).
