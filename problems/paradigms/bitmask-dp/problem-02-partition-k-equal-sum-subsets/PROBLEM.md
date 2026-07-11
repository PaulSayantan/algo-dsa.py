# Partition to K Equal Sum Subsets

**Difficulty:** Medium

**Source:** LeetCode 698 (Partition to K Equal Sum Subsets)

## Description

Given an integer array `nums` and an integer `k`, return `true` if it is
possible to divide **all** of the elements of `nums` into `k` non-empty subsets
whose sums are **all equal**.

Every element must be used exactly once, and each element belongs to exactly one
subset.

## Constraints

- `1 <= k <= len(nums) <= 16`
- `1 <= nums[i] <= 10^4`
- The frequency of each element is within the range `[1, 4]` (i.e. no huge
  duplicates matter for correctness; this bound just keeps the input tame).

## Examples

### Example 1

```
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: true
```

Explanation: The total sum is `20`, so each of the `4` subsets must sum to `5`.
One valid partition is `(5)`, `(1, 4)`, `(2, 3)`, and `(2, 3)`.

### Example 2

```
Input: nums = [1, 2, 3, 4], k = 3
Output: false
```

Explanation: The total sum is `10`, which is not divisible by `3`, so equal
partitioning is impossible.

### Example 3

```
Input: nums = [2, 2, 2, 2, 3, 4, 5], k = 4
Output: false
```

Explanation: The total sum is `20`, so each subset would need to sum to `5`.
The element `5` fills one subset, and `4` would need a `1` to reach `5` but no
`1` exists, so no valid partition into 4 equal groups exists.

## Hint

With `n <= 16` elements, encode the "already used" elements as a bitmask. Track
the running sum of the current bucket modulo the target as you add elements.
This is **Bitmask DP** over subsets.
