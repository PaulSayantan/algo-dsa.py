# Count of Range Sum

**Difficulty:** Hard

**Source:** LeetCode 327 — Count of Range Sum

## Description

Given an integer array `nums` and two integers `lower` and `upper`, return the number
of range sums that lie in `[lower, upper]` inclusive.

A **range sum** `S(i, j)` is defined as the sum of the elements in `nums` between
indices `i` and `j` inclusive, where `i <= j`.

Let `P[0] = 0` and `P[t] = nums[0] + ... + nums[t-1]` be the prefix sums. Then
`S(i, j) = P[j+1] - P[i]`, so a range sum lies in `[lower, upper]` iff
`lower <= P[j+1] - P[i] <= upper`, i.e. `P[j+1] - upper <= P[i] <= P[j+1] - lower`.
Iterating the right endpoint `P[j+1]` and querying how many earlier prefix sums fall
in that window is a **range-count** query — exactly what an order-statistics tree
answers with two rank queries.

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

**Explanation:** There are three range sums in `[-2, 2]`:
- `S(0, 0) = -2`
- `S(2, 2) = -1`
- `S(0, 2) = -2 + 5 + (-1) = 2`

The other range sums are `S(1, 1) = 5`, `S(0, 1) = 3`, and `S(1, 2) = 4`, none of
which fall in `[-2, 2]`.

### Example 2

```
Input:  nums = [0], lower = 0, upper = 0
Output: 1
```

**Explanation:** The only range sum is `S(0, 0) = 0`, which lies in `[0, 0]`.

## Hint

Build prefix sums `P`. For each prefix sum `P[r]` (as the right endpoint), count how
many earlier prefix sums `P[l]` satisfy `P[r] - upper <= P[l] <= P[r] - lower`, using
an **Order-Statistics Tree** of the prefix sums seen so far. A range-count is two
rank queries: `count(<= hi) - count(< lo)`. Use 64-bit prefix sums.
