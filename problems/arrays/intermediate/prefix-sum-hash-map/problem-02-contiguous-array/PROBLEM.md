# Contiguous Array

**Difficulty:** Medium

**Source:** LeetCode 525 — Contiguous Array

## Description

Given a binary array `nums` (each element is `0` or `1`), return the **maximum
length** of a contiguous subarray that contains an **equal number of `0`s and
`1`s**.

If no such subarray exists, return `0`.

The trick is to notice that "equal count of 0s and 1s" is the same as "the sum
is zero" once you treat each `0` as `-1` and each `1` as `+1`. Then the problem
becomes: find the longest contiguous subarray whose (remapped) sum is `0`.

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Examples

### Example 1

```
Input: nums = [0, 1]
Output: 2
Explanation: [0, 1] has one 0 and one 1, so the whole array of length 2 is
the longest balanced subarray.
```

### Example 2

```
Input: nums = [0, 1, 0]
Output: 2
Explanation: [0, 1] (indices 0..1) or [1, 0] (indices 1..2) are the longest
balanced subarrays, each of length 2. The full array has two 0s and one 1,
so it is not balanced.
```

### Example 3

```
Input: nums = [0, 0, 1, 0, 0, 0, 1, 1]
Output: 6
Explanation: The subarray nums[2..7] = [1, 0, 0, 0, 1, 1] has three 0s and
three 1s, giving length 6.
```

## Hint

Remap `0 -> -1` and `1 -> +1`, then a balanced subarray is one whose sum is
`0`. Use a running **prefix sum** and a **hash map** that stores the *earliest*
index at which each prefix-sum value appeared.
