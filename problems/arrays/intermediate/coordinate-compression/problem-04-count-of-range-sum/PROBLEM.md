# Count of Range Sum

**Difficulty:** Hard

**Source:** LeetCode 327 — Count of Range Sum

## Description

Given an integer array `nums` and two integers `lower` and `upper`, return the number of
range sums that lie in `[lower, upper]` inclusive.

A **range sum** `S(i, j)` is the sum of the elements of `nums` between indices `i` and `j`
(inclusive), where `i <= j`.

The standard trick is to work with prefix sums `P[k] = nums[0] + ... + nums[k-1]`, so that
`S(i, j) = P[j+1] - P[i]`. A range sum lies in `[lower, upper]` exactly when, for some
`i < k`, `lower <= P[k] - P[i] <= upper`, i.e. `P[k] - upper <= P[i] <= P[k] - lower`.
Counting, for each `k`, how many earlier prefix sums fall in that window is a
count-in-range query that a Fenwick tree answers in `O(log n)` — but prefix sums range over
roughly `-10^14 .. 10^14`, so we must compress them first.

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

**Explanation:** The range sums that fall in `[-2, 2]` are `S(0,0) = -2`, `S(2,2) = -1`, and
`S(0,2) = -2 + 5 - 1 = 2`. That is 3 ranges.

### Example 2

```
Input:  nums = [0], lower = 0, upper = 0
Output: 1
```

**Explanation:** The only range is `S(0,0) = 0`, which lies in `[0, 0]`.

### Example 3

```
Input:  nums = [1, -1, 1], lower = 0, upper = 1
Output: 5
```

**Explanation:** The range sums are `S(0,0)=1`, `S(1,1)=-1`, `S(2,2)=1`, `S(0,1)=0`,
`S(1,2)=0`, `S(0,2)=1`. Those within `[0, 1]` are `1, 1, 0, 0, 1` — five of the six ranges
(only `S(1,1) = -1` is excluded).

## Hint

Use **Coordinate Compression** on the prefix sums, then a Fenwick tree (BIT) to count, for
each prefix sum, how many earlier prefix sums land in the required window.
