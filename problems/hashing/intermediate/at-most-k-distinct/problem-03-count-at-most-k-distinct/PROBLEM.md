# Count Subarrays With At Most K Distinct Integers

**Difficulty:** Medium

**Source:** Classic — atMost(k) sliding-window subroutine

## Description

Given an integer array `nums` and an integer `k`, return the number of contiguous subarrays that contain **at most** `k` distinct integers. This is the workhorse subroutine behind the exactly-K identity.

## Examples

### Example 1

```
Input:  nums = [1,2,1,2,3], k = 2
Output: 12
```

### Example 2

```
Input:  nums = [5,5,5], k = 1
Output: 6
```

**Explanation:** All 6 subarrays have a single distinct value.

## Hint

For each right, after shrinking to <= k distinct, add (right - left + 1) subarrays.
