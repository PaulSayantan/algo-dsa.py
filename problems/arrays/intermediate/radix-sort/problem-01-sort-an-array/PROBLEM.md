# Sort an Array

**Difficulty:** Medium

**Source:** LeetCode 912 — Sort an Array

## Description

Given an array of integers `nums`, sort the array in ascending order and return
it.

You must solve the problem **without using any built-in sorting function**, and
your solution should run in the best time complexity possible. The array may
contain negative numbers, duplicates, and zeros.

Because the values are ordinary machine integers (bounded magnitude), this is a
natural fit for a digit-by-digit, non-comparison sort rather than an
`O(n log n)` comparison sort.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
Explanation: After sorting, the values appear in non-decreasing order.
```

### Example 2

```
Input:  nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
Explanation: Duplicates (the two 1s and the two 0s) are all kept and placed
next to each other in order.
```

### Example 3

```
Input:  nums = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
Output: [-7, -5, -4, -1, -1, 0, 0, 4, 7, 9]
Explanation: Negative numbers must sort correctly relative to zeros and
positives.
```

## Hint

Use **Radix Sort**: sort the numbers one digit at a time (least significant
digit first) with a stable counting-sort subroutine. Handle negatives by
sorting on magnitude and splitting/reversing, or by offsetting every value so it
becomes non-negative.
