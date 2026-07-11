# Number of Ways to Split Array

**Difficulty:** Medium

**Source:** LeetCode 2270 — Number of Ways to Split Array

## Description

You are given a 0-indexed integer array `nums` of length `n`.

`nums` contains a **valid split** at index `i` if the following are true:

- The sum of the first `i + 1` elements is **greater than or equal to** the sum
  of the last `n - i - 1` elements.
- There is at least one element to the right of `i`. That is, `0 <= i < n - 1`.

Return the number of **valid splits** in `nums`.

## Constraints

- `2 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`

## Examples

### Example 1

```
Input:  nums = [10, 4, -8, 7]
Output: 2

Explanation:
There are three ways of splitting nums into two non-empty parts:
- Split at index 0: left = [10], sum 10.  right = [4, -8, 7], sum 3.  10 >= 3  -> valid.
- Split at index 1: left = [10, 4], sum 14. right = [-8, 7], sum -1. 14 >= -1 -> valid.
- Split at index 2: left = [10, 4, -8], sum 6. right = [7], sum 7. 6 >= 7 -> NOT valid.
So there are 2 valid splits.
```

### Example 2

```
Input:  nums = [2, 3, 1, 0]
Output: 2

Explanation:
- Split at index 1: left = [2, 3], sum 5.    right = [1, 0], sum 1.  5 >= 1 -> valid.
- Split at index 2: left = [2, 3, 1], sum 6. right = [0], sum 0.     6 >= 0 -> valid.
(Split at index 0: left sum 2 < right sum 4 -> not valid.)
So there are 2 valid splits.
```

## Hint

The right side of any split is a **Suffix Sum**. Precompute the total, keep a
running left (prefix) sum, and the right sum at split `i` is
`total - leftSum` — no inner loop needed.
