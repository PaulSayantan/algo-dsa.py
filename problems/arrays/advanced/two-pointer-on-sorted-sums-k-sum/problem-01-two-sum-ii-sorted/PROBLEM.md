# Two Sum II - Input Array Is Sorted

**Difficulty:** Medium

**Source:** LeetCode 167 (Two Sum II - Input Array Is Sorted)

## Description

You are given a **1-indexed** array of integers `numbers` that is already sorted in
**non-decreasing** order. Find two numbers such that they add up to a specific
`target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]`
where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one**, as
an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You may **not**
use the same element twice. Your solution must use only **constant extra space**.

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution.

## Examples

**Example 1**

```
Input:  numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: numbers[1] + numbers[2] = 2 + 7 = 9. Return the 1-based indices [1, 2].
```

**Example 2**

```
Input:  numbers = [2, 3, 4], target = 6
Output: [1, 3]
Explanation: numbers[1] + numbers[3] = 2 + 4 = 6. Return the 1-based indices [1, 3].
```

**Example 3**

```
Input:  numbers = [-1, 0], target = -1
Output: [1, 2]
Explanation: numbers[1] + numbers[2] = -1 + 0 = -1. Return the 1-based indices [1, 2].
```

## Hint

The array is already sorted, so you do not need a hash map. Use **Two-Pointer on
Sorted Sums (k-Sum)**: place one pointer at each end and move them inward based on
whether the current pair sum is below or above the target.
