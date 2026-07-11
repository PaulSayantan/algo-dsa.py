# Partition Array Into Two Arrays to Minimize Sum Difference

**Difficulty:** Hard

Source: LeetCode 2035 — "Partition Array Into Two Arrays to Minimize Sum Difference".

## Description

You are given an integer array `nums` of `2 * n` integers. You need to partition `nums`
into **two arrays of length `n`** to **minimize the absolute difference** of the sums of
the two arrays. To partition `nums`, put each element of `nums` into **one of the two
arrays**, and each array must hold **exactly `n`** elements.

Return the **minimum possible absolute difference** between the two arrays' sums.

The equal-size constraint is what makes this harder than plain subset-sum: you cannot pick
any subset, only subsets of size exactly `n`.

## Constraints

- `1 <= n <= 15`
- `nums.length == 2 * n`
- `-10^7 <= nums[i] <= 10^7`

## Examples

### Example 1
```
Input:  nums = [3, 9, 7, 3]
Output: 2
Explanation: n = 2. One optimal partition is [3, 9] and [7, 3], with sums 12 and 10.
The absolute difference is abs(12 - 10) = 2.
```

### Example 2
```
Input:  nums = [-36, 36]
Output: 72
Explanation: n = 1. The only partition is [-36] and [36] (up to swapping).
The absolute difference is abs(-36 - 36) = 72.
```

### Example 3
```
Input:  nums = [2, -1, 0, 4, -2, -9]
Output: 0
Explanation: n = 3. The total is -6. Partition into [2, 4, -9] (sum -3) and
[-1, 0, -2] (sum -3). The absolute difference is 0.
```

## Hint

There are `2n` elements with `n` up to 15, so `2^(2n)` can reach `2^30` — too many. Split
into two halves of `n` elements each and enumerate each half's subsets **grouped by how
many elements they take**, then combine with binary search. This is **Meet in the Middle**.
