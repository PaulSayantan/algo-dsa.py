# K-Concatenation Maximum Sum

**Difficulty:** Hard

**Source:** LeetCode 1191 — K-Concatenation Maximum Sum

## Description

Given an integer array `arr` and an integer `k`, modify the array by repeating
it `k` times. For example, if `arr = [1, 2]` and `k = 3`, then the modified
array is `[1, 2, 1, 2, 1, 2]`.

Return the maximum sub-array sum in the modified array. Note that the length of
the sub-array can be `0` and its sum in that case is `0` (so the answer is never
negative).

As the answer can be very large, return the answer **modulo `10^9 + 7`**.

Because `k` can be up to `10^5` and each copy up to `10^5` long, you cannot
build the repeated array explicitly — you must reason about at most **two**
copies plus the repeated interior.

## Constraints

- `1 <= arr.length <= 10^5`
- `1 <= k <= 10^5`
- `-10^4 <= arr[i] <= 10^4`

## Examples

### Example 1

```
Input:  arr = [1, 2], k = 3
Output: 9
Explanation: The repeated array is [1, 2, 1, 2, 1, 2]. Its total sum is 9, and
             since every element is positive the whole thing is the best subarray.
```

### Example 2

```
Input:  arr = [1, -2, 1], k = 5
Output: 2
Explanation: One copy sums to 0, so extra copies add nothing. The best subarray
             spans a seam: the trailing 1 of one copy plus the leading 1 of the
             next gives 1 + 1 = 2.
```

### Example 3

```
Input:  arr = [-1, -2], k = 7
Output: 0
Explanation: Every element is negative, so the best choice is the empty subarray
             with sum 0.
```

## Constraints on the answer

- The answer is `max(0, ...)` — empty subarray is allowed.
- Apply `% (10^9 + 7)` to the final result.

## Hint

The optimal subarray never needs more than two copies of `arr` at its ends; any
full copies in the middle only matter if one copy's total is positive. Use
**Kadane's Algorithm** on one copy and on two copies, then add `(k - 2)` times
the array sum when that sum is positive.
