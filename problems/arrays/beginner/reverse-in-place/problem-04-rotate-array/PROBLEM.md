# Rotate Array

**Difficulty:** Medium

**Source:** LeetCode 189 — Rotate Array

## Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is
non-negative.

Rotating right by one step moves the last element to the front and shifts everyone else
one position right. You must rotate by `k` steps in total. Try to solve it **in place**
with `O(1)` extra space.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Examples

### Example 1

```
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

Explanation: The last `k = 3` elements `[5,6,7]` wrap around to the front, and the
first four `[1,2,3,4]` shift to the back. Equivalently: rotate right once ->
`[7,1,2,3,4,5,6]`, twice -> `[6,7,1,2,3,4,5]`, three times -> `[5,6,7,1,2,3,4]`.

### Example 2

```
Input:  nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

Explanation: With `k = 2`, the last two elements `[3,99]` move to the front and the
first two `[-1,-100]` move to the back, giving `[3,99,-1,-100]`.

## Hint

Use **Reverse In-Place**: reverse the whole array, then reverse the first `k` elements
and reverse the remaining `n - k` elements. (Remember to take `k mod n` first.)
