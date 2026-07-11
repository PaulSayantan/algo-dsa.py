# Squares of a Sorted Array

**Difficulty:** Easy

**Source:** LeetCode 977 — Squares of a Sorted Array

## Description

Given an integer array `nums` sorted in **non-decreasing** order, return an array of the
**squares of each number**, also sorted in non-decreasing order.

The challenge is to do it in `O(n)` time. A sorted array of possibly-negative numbers,
once squared, is no longer sorted: the largest squares come from the two ends (the most
negative and the most positive values), while the smallest squares are somewhere in the
middle.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## Examples

### Example 1

```
Input:  nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: Squaring gives [16,1,0,9,100]; sorted non-decreasing it is
             [0,1,9,16,100].
```

### Example 2

```
Input:  nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
Explanation: Squaring gives [49,9,4,9,121]; sorted it is [4,9,9,49,121].
```

### Example 3

```
Input:  nums = [-5,-3,-2,-1]
Output: [1,4,9,25]
Explanation: All values are negative. Squaring gives [25,9,4,1]; reversing yields the
             sorted result [1,4,9,25].
```

## Hint

Think of the array as two already-sorted sequences meeting in the middle: the negatives
(whose squares *decrease* as you move right) and the non-negatives (whose squares
*increase*). Use the **Two-Pointer Merge** technique with one pointer at each end,
comparing absolute values and filling the output from the largest square down.
