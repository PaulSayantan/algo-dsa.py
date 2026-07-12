# Next Greater Element II (Circular)

**Difficulty:** Medium

**Source:** LeetCode 503 — Next Greater Element II

## Description

Given a **circular** integer array `nums`, return the next greater number for every element. The next greater number of `nums[i]` is the first greater value moving forward, wrapping around; if none exists, use `-1`.

## Examples

### Example 1

```
Input:  nums = [1,2,1]
Output: [2,-1,2]
```

## Hint

Iterate 2n indices modulo n over a decreasing stack of indices to handle the wrap-around.
