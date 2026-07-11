# Minimum Operations to Make the Array K-Increasing

**Difficulty:** Hard

**Source:** LeetCode 2111 — Minimum Operations to Make the Array K-Increasing

## Description

You are given a 0-indexed array `arr` consisting of `n` positive integers, and
a positive integer `k`.

The array `arr` is called **K-increasing** if
`arr[i - k] <= arr[i]` holds for **every** index `i` where `k <= i <= n - 1`.

- For example, `arr = [4, 1, 5, 2, 6, 2]` is K-increasing for `k = 2` because:
  - `arr[0] <= arr[2]` (`4 <= 5`)
  - `arr[1] <= arr[3]` (`1 <= 2`)
  - `arr[2] <= arr[4]` (`5 <= 6`)
  - `arr[3] <= arr[5]` (`2 <= 2`)
- However, the same `arr` is **not** K-increasing for `k = 1` (because
  `arr[0] > arr[1]`) or `k = 3` (because `arr[0] > arr[3]`).

In one **operation**, you can choose an index `i` and change `arr[i]` to
**any** positive integer. Return the minimum number of operations required to
make `arr` K-increasing for the given `k`.

## Constraints

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^5`
- `1 <= k <= arr.length`

## Examples

### Example 1

```
Input:  arr = [5, 4, 3, 2, 1], k = 1
Output: 4
Explanation: For k = 1 the whole array must be non-decreasing.
             One optimal fix is [5, 5, 5, 5, 5] (or [1,1,1,1,1]),
             changing 4 of the 5 elements. Fewer than 4 changes cannot work.
```

### Example 2

```
Input:  arr = [4, 1, 5, 2, 6, 2], k = 2
Output: 0
Explanation: The array is already K-increasing for k = 2 (all four
             arr[i-2] <= arr[i] checks hold), so no operations are needed.
```

### Example 3

```
Input:  arr = [4, 1, 5, 2, 6, 2], k = 3
Output: 2
Explanation: Split into k = 3 chains by index mod 3:
             indices {0,3} -> [4, 2], indices {1,4} -> [1, 6],
             indices {2,5} -> [5, 2].
             Chains [4,2] and [5,2] each need 1 change to become
             non-decreasing; [1,6] needs 0. Total = 2.
```

## Hint

The constraint only links indices that are `k` apart, so the array decomposes
into `k` independent chains (index `mod k`). Each chain must become
**non-decreasing** with the fewest changes — and "minimum changes to make a
sequence non-decreasing" is `length - LNDS`, where LNDS is found with the
Longest Increasing Subsequence (patience / binary search) technique.
