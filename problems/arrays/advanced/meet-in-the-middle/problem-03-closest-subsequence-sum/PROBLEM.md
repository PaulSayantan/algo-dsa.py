# Closest Subsequence Sum

**Difficulty:** Hard

Source: LeetCode 1755 — "Closest Subsequence Sum".

## Description

You are given an integer array `nums` and an integer `goal`.

You want to choose a **subsequence** of `nums` (any subset of indices, possibly empty)
such that the sum of its elements is as close as possible to `goal`. That is, if the sum
of the chosen subsequence is `sum`, you want to **minimize** the absolute difference
`abs(sum - goal)`.

Return the **minimum possible value** of `abs(sum - goal)`.

Note that a subsequence of an array is obtained by removing some (possibly all) elements
from it; the empty subsequence has sum `0`.

## Constraints

- `1 <= len(nums) <= 40`
- `-10^7 <= nums[i] <= 10^7`
- `-10^9 <= goal <= 10^9`

## Examples

### Example 1
```
Input:  nums = [5, -7, 3, 5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with sum = 5 - 7 + 3 + 5 = 6.
The absolute difference is abs(6 - 6) = 0.
```

### Example 2
```
Input:  nums = [7, -9, 15, -2], goal = -5
Output: 1
Explanation: Choose the subsequence {-9, -2}, with sum = -11; abs(-11 - (-5)) = 6.
Better: choose {7, -9, -2} with sum = -4; abs(-4 - (-5)) = 1. No subset reaches -5
exactly, so 1 is optimal.
```

### Example 3
```
Input:  nums = [1, 2, 3], goal = -7
Output: 7
Explanation: The smallest reachable sum is the empty subsequence with sum 0, giving
abs(0 - (-7)) = 7. Every non-empty subset only increases the sum, moving further away.
```

## Hint

`n` is at most 40, so `2^40` is too many subsequences to try, but `2^20` per half is fine.
Split the array, sort one half's subset sums, and binary-search for the best complement —
**Meet in the Middle**.
