# Next Greater Element II

**Difficulty:** Medium

**Source:** LeetCode 503 — Next Greater Element II

## Description

Given a **circular** integer array `nums` (the element after `nums[-1]` is `nums[0]`), return an array `answer` where `answer[i]` is the next greater number for `nums[i]`. The next greater number of `nums[i]` is the first number greater than it when scanning forward circularly. If it does not exist, use `-1`.

Constraints: `1 <= len(nums) <= 10^4`, `-10^9 <= nums[i] <= 10^9`.

## Examples

### Example 1

```
Input:  nums = [1,2,1]
Output: [2,-1,2]
```

**Explanation:** For the last `1` the search wraps around circularly and finds `2`.

## Hint

Walk a monotonic decreasing stack of indices over the array twice (using `i % n`) so wrap-around is handled; a taller bar arriving pops the shorter indices it "closes off" and assigns their answer — the same popping mechanic as trapping rain water.
