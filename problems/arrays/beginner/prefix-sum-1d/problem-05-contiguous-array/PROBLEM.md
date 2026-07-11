# Contiguous Array

**Difficulty:** Medium

**Source:** LeetCode 525 — Contiguous Array

## Description

Given a binary array `nums` (containing only `0`s and `1`s), return the maximum
length of a contiguous subarray that contains an **equal number of `0`s and
`1`s**.

If no such subarray exists, return `0`.

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Examples

### Example 1

```
Input:  nums = [0, 1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of
             0s and 1s (one of each).
```

### Example 2

```
Input:  nums = [0, 1, 0]
Output: 2
Explanation: [0, 1] (indices 0..1) or [1, 0] (indices 1..2) is the longest
             contiguous subarray with an equal number of 0s and 1s.
             The whole array has two 0s and one 1, so it does not qualify.
```

### Example 3

```
Input:  nums = [0, 0, 1, 0, 0, 0, 1, 1]
Output: 6
Explanation: The subarray from index 2 to index 7, [1, 0, 0, 0, 1, 1], has
             three 0s and three 1s, giving length 6.
```

## Hint

Use **Prefix Sum (1D)** on a transformed array: treat `0` as `-1` and `1` as
`+1`. A balanced subarray is then one whose transformed sum is `0`, i.e. two
positions sharing the same running sum.
