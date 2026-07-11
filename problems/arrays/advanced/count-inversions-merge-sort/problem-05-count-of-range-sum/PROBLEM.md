# Count of Range Sum

**Difficulty:** Hard

**Source:** LeetCode 327 — "Count of Range Sum"

## Description

Given an integer array `nums` and two integers `lower` and `upper`, return the
number of range sums that lie in `[lower, upper]` **inclusive**.

A *range sum* `S(i, j)` is the sum of the elements of `nums` between indices `i`
and `j` inclusive, where `i <= j`. You must count how many pairs `(i, j)`
satisfy `lower <= S(i, j) <= upper`.

**Prefix-sum reduction.** Let `P[0] = 0` and `P[k] = nums[0] + ... + nums[k-1]`.
Then `S(i, j) = P[j + 1] - P[i]`. Counting subarrays with sum in `[lower, upper]`
becomes counting pairs of prefix indices `a < b` (with `a, b` in `0..n`) such
that:

```
lower <= P[b] - P[a] <= upper
```

That is a two-sided "cross-pair" count over the prefix-sum array — a direct
generalization of inversion counting.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `-10^5 <= lower <= upper <= 10^5`
- The prefix sums can overflow 32-bit range, so accumulate them in 64-bit
  (Python integers are unbounded).

## Examples

### Example 1

```
Input:  nums = [-2, 5, -1], lower = -2, upper = 2
Output: 3
Explanation: Prefix sums P = [0, -2, 3, 2]. The subarrays whose sum lies in
[-2, 2] are:
  [-2]        sum = -2   (valid)
  [-2, 5, -1] sum =  2   (valid)
  [-1]        sum = -1   (valid)
The other three subarrays ([-2,5]=3, [5]=5, [5,-1]=4) fall outside [-2, 2].
```

### Example 2

```
Input:  nums = [0], lower = 0, upper = 0
Output: 1
Explanation: Prefix sums P = [0, 0]. The only subarray is [0] with sum 0,
which lies in [0, 0]. So exactly 1 range sum qualifies.
```

## Hint

Build the prefix-sum array `P` of length `n + 1`, then use **Count Inversions
(merge sort)** on `P`. During each merge (both halves sorted), for every left
index `a` count the right indices `b` with `P[b] - P[a]` in `[lower, upper]`
using two monotone pointers that mark the window `[P[a] + lower, P[a] + upper]`.
Then merge to keep `P` sorted for the parent call.
