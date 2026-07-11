# Binary Subarrays With Sum

**Difficulty:** Medium

**Source:** LeetCode 930 — Binary Subarrays With Sum

## Description

Given a binary array `nums` (each element is `0` or `1`) and an integer `goal`,
return the **number of non-empty contiguous subarrays** whose elements sum to
exactly `goal`.

Because the array is binary, every prefix sum is non-decreasing, so the count
of prefix sums equal to `current - goal` directly gives the number of valid
subarrays ending at the current index.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `nums[i]` is either `0` or `1`.
- `0 <= goal <= nums.length`

## Examples

### Example 1

```
Input: nums = [1, 0, 1, 0, 1], goal = 2
Output: 4
Explanation: The four subarrays summing to 2 are
[1,0,1]   (indices 0..2),
[1,0,1,0] (indices 0..3),
[0,1,0,1] (indices 1..4),
[1,0,1]   (indices 2..4).
```

### Example 2

```
Input: nums = [0, 0, 0, 0, 0], goal = 0
Output: 15
Explanation: Every non-empty subarray sums to 0. An array of length 5 has
5*(5+1)/2 = 15 subarrays, all of which qualify.
```

### Example 3

```
Input: nums = [1, 0, 1], goal = 1
Output: 4
Explanation: The subarrays summing to 1 are [1] (index 0), [1,0] (0..1),
[0,1] (1..2), and [1] (index 2).
```

## Hint

This is the binary special case of "count subarrays with sum k". Track a
running **prefix sum** and a **hash map** counting how many times each prefix
sum has appeared; for each position add the count of `prefix - goal`. (Note the
`goal = 0` case relies on the `{0: 1}` seed.)
