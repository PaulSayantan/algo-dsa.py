# Count of Range Sum

**Difficulty:** Hard

**Source:** LeetCode 327 — Count of Range Sum

## Description

Given an integer array `nums` and two integers `lower` and `upper`, return the number
of range sums that lie in `[lower, upper]` **inclusive**.

A *range sum* `S(i, j)` is defined as the sum of the elements of `nums` between
indices `i` and `j` inclusive, with `i <= j`. Count every pair `(i, j)` such that
`lower <= S(i, j) <= upper`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `-10^5 <= lower <= upper <= 10^5`
- The answer is guaranteed to fit in a 32-bit integer.

## Examples

### Example 1

```
Input:  nums = [-2, 5, -1], lower = -2, upper = 2
Output: 3
```

**Explanation:** Enumerate all range sums and keep those in `[-2, 2]`:
- `S(0,0) = -2`   in range
- `S(0,1) = 3`    out
- `S(0,2) = 2`    in range
- `S(1,1) = 5`    out
- `S(1,2) = 4`    out
- `S(2,2) = -1`   in range

The three in-range sums are `-2`, `2`, and `-1`, so the answer is `3`.

### Example 2

```
Input:  nums = [2, -1, 1], lower = 1, upper = 2
Output: 4
```

**Explanation:** Enumerate all range sums:
- `S(0,0) = 2`    in range
- `S(0,1) = 1`    in range
- `S(0,2) = 2`    in range
- `S(1,1) = -1`   out
- `S(1,2) = 0`    out
- `S(2,2) = 1`    in range

Four range sums lie in `[1, 2]`, so the answer is `4`.

## Hint

Work with **prefix sums** `P[k] = nums[0] + ... + nums[k-1]`. Then
`S(i, j) = P[j+1] - P[i]`, and the condition becomes
`lower <= P[j+1] - P[i] <= upper`. Sweep the prefix sums while maintaining a
**Segment Tree over the compressed prefix-sum values**, counting for each new prefix
how many earlier prefixes fall in the required value window.
