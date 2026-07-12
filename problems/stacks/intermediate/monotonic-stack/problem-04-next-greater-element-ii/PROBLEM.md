# Next Greater Element II

**Difficulty:** Medium

**Source:** LeetCode 503 — Next Greater Element II

## Description

Given a **circular** integer array `nums` (the element after `nums[-1]` is `nums[0]`), return an array `answer` where `answer[i]` is the next greater number for `nums[i]`. The *next greater number* of `x` is the first strictly greater value encountered when scanning forward, wrapping around the end of the array. If no such value exists, `answer[i] == -1`.

Constraints: `1 <= len(nums) <= 10^4`; values may repeat and be negative.

## Examples

### Example 1

```
Input:  nums = [1,2,1]
Output: [2,-1,2]
```

**Explanation:** The first `1` sees `2` next; the `2` never finds anything larger; the last `1` wraps around to the leading `2`.

## Hint

Walk the indices twice (`2n`) over a decreasing stack; when a strictly greater value arrives it resolves everything popped, and the wrap-around pass fills the tail.
