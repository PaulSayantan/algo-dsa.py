# Partition Array Into Two Halves to Minimize Sum Difference

**Difficulty:** Hard

**Source:** LeetCode 2035 — Partition Array Into Two Arrays to Minimize Sum
Difference

## Description

You are given an integer array `nums` of `2 * n` integers.

Partition `nums` into **two arrays of length `n` each** to minimize the
absolute difference of their sums. Every element must be placed into exactly
one of the two arrays, and each array must contain exactly `n` elements.

Return the minimum possible absolute difference
`abs(sum(firstArray) - sum(secondArray))`.

## Constraints

- `1 <= n <= 15`
- `nums.length == 2 * n`
- `-10^7 <= nums[i] <= 10^7`

## Examples

### Example 1

```
Input:  nums = [3, 9, 7, 3]
Output: 2
```

**Explanation:** Here `n = 2`. One optimal partition is `[3, 9]` and `[7, 3]`
with sums `12` and `10`; the difference is `abs(12 - 10) = 2`. No partition
into two size-2 arrays does better.

### Example 2

```
Input:  nums = [-36, 36]
Output: 72
```

**Explanation:** Here `n = 1`, so each array holds one element. The only
partition (up to swapping) is `[-36]` and `[36]`, giving
`abs(-36 - 36) = 72`.

### Example 3

```
Input:  nums = [2, -1, 0, 4, -2, -9]
Output: 0
```

**Explanation:** Here `n = 3`. The partition `[-1, 0, -2]` (sum `-3`) and
`[2, 4, -9]` (sum `-3`) has difference `abs(-3 - (-3)) = 0`, which is optimal.

## Hint

Trying all `C(2n, n)` balanced partitions is too slow for `n = 15`. Split the
array into a left half and a right half of `n` elements each and **meet in the
middle** — but now the halves must be combined *while respecting how many
elements each side contributes to the first array*. Group each half's subset
sums by their element count, then match a `k`-element choice on the left with
an `(n - k)`-element choice on the right using sorting + binary search.
