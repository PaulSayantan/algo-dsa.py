# Sum of Absolute Differences in a Sorted Array

**Difficulty:** Medium

**Source:** LeetCode 1685 — Sum of Absolute Differences in a Sorted Array

## Description

You are given an integer array `nums` sorted in **non-decreasing** order.

Build and return an integer array `result` with the same length as `nums` such
that `result[i]` is equal to the summation of absolute differences between
`nums[i]` and all the other elements in the array.

In other words,

```
result[i] = sum over all j (0 <= j < nums.length) of |nums[i] - nums[j]|
```

## Constraints

- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= nums[i + 1] <= 10^4` (the array is sorted non-decreasing)

## Examples

### Example 1

```
Input:  nums = [2, 3, 5]
Output: [4, 3, 5]

Explanation:
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5
```

### Example 2

```
Input:  nums = [1, 4, 6, 8, 10]
Output: [24, 15, 13, 15, 21]

Explanation:
result[0] = 0 + 3 + 5 + 7 + 9  = 24
result[1] = 3 + 0 + 2 + 4 + 6  = 15
result[2] = 5 + 2 + 0 + 2 + 4  = 13
result[3] = 7 + 4 + 2 + 0 + 2  = 15
result[4] = 9 + 6 + 4 + 2 + 0  = 21
```

## Hint

Because the array is sorted, for a fixed `i` every element to the left is `<=
nums[i]` and every element to the right is `>= nums[i]`. Split the sum into a
left part and a right part and use a **prefix sum** and a **Suffix Sum** so each
`result[i]` drops to O(1).
