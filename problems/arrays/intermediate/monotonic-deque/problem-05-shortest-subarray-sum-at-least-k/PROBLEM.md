# Shortest Subarray with Sum at Least K

**Difficulty:** Hard

**Source:** LeetCode 862 — Shortest Subarray with Sum at Least K

## Description

Given an integer array `nums` and an integer `k`, return the **length of the
shortest non-empty contiguous subarray** of `nums` with a sum of **at least**
`k`. If there is no such subarray, return `-1`.

Note that `nums` may contain **negative** numbers, which is what makes the simple
two-pointer sliding window insufficient and forces a monotonic-deque approach
over prefix sums.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

## Examples

### Example 1

```
Input:  nums = [1], k = 1
Output: 1
```

**Explanation:** The single-element subarray `[1]` has sum `1 >= 1`, length `1`.

### Example 2

```
Input:  nums = [1, 2], k = 4
Output: -1
```

**Explanation:** The largest possible sum is `1 + 2 = 3 < 4`, so no subarray
qualifies.

### Example 3

```
Input:  nums = [2, -1, 2], k = 3
Output: 3
```

**Explanation:** The only subarray whose sum reaches `3` is the whole array
`[2, -1, 2]` (sum `3`), length `3`. Shorter subarrays (`[2]`, `[2,-1]`,
`[-1,2]`, ...) all sum to less than `3`.

### Example 4

```
Input:  nums = [84, -37, 32, 40, 95], k = 167
Output: 3
```

**Explanation:** The subarray `[32, 40, 95]` sums to `167 >= 167` with length
`3`; no shorter subarray reaches `167`.

## Hint

Work with **prefix sums** `P`, where a subarray `(i, j]` has sum `P[j] - P[i]`.
For each `j` you want the largest `i < j` with `P[i] <= P[j] - k`, minimizing
`j - i`. Maintain a **Monotonic Deque** of prefix-sum indices that is increasing
in `P`, popping from both ends.
