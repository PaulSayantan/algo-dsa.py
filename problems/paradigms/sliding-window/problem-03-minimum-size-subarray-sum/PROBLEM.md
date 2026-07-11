# Minimum Size Subarray Sum

**Difficulty:** Medium

**Source:** LeetCode 209 — Minimum Size Subarray Sum

## Description

Given an array of **positive** integers `nums` and a positive integer `target`,
return the **minimal length** of a **contiguous** subarray whose sum is greater than
or equal to `target`.

If there is no such subarray, return `0` instead.

## Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2
Explanation: The subarray [4, 3] has sum 7 >= 7 and length 2. No length-1 element
             reaches 7, so 2 is minimal.
```

### Example 2

```
Input:  target = 4, nums = [1, 4, 4]
Output: 1
Explanation: The single element [4] already meets the target, giving length 1.
```

### Example 3

```
Input:  target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
Output: 0
Explanation: The total sum is 8, which is less than 11, so no qualifying subarray
             exists and the answer is 0.
```

## Hint

Use the **Sliding Window** technique: grow the window on the right to accumulate sum,
and as soon as the sum reaches `target`, shrink from the left to find the shortest
window still meeting the requirement. This works because all values are positive.

## Follow-up

Can you also design an O(n log n) solution using prefix sums and binary search?
