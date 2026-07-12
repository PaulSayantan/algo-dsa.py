# Make Sum Divisible by P

**Difficulty:** Medium

**Source:** LeetCode 1590 — Make Sum Divisible by P

## Description

Given `nums`, remove the smallest possible contiguous subarray (not the whole array) so that the sum of the remaining elements is divisible by `p`. Return the length of that subarray, or -1 if impossible. Return 0 if the whole sum is already divisible by `p`.

## Examples

### Example 1

```
Input:  nums = [3,1,4,2], p = 6
Output: 1
```

## Hint

Let need = total%p. Find the shortest subarray whose sum%p == need via a remainder→index map.
