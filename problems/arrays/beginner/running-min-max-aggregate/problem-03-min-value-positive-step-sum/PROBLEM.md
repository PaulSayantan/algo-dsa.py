# Minimum Value to Get Positive Step-by-Step Sum

**Difficulty:** Easy

**Source:** LeetCode 1413 — Minimum Value to Get Positive Step by Step Sum

## Description

Given an array of integers `nums`, you start with an initial positive value
`startValue`.

In each iteration, you compute the step-by-step sum of `startValue` plus
elements in `nums` from left to right. That is, you add `nums[0]`, then
`nums[1]`, and so on, keeping a running total that begins at `startValue`.

Return the **minimum positive value** of `startValue` such that the step-by-step
sum is **never less than 1** at any point during the iteration.

## Constraints

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`
- The answer is guaranteed to be a positive integer (`>= 1`).

## Examples

### Example 1

```
Input:  nums = [-3, 2, -3, 4, 2]
Output: 5
Explanation: With startValue = 5 the step-by-step sums are:
  start 5 -> 5 + (-3) = 2 -> 2 + 2 = 4 -> 4 + (-3) = 1 -> 1 + 4 = 5 -> 5 + 2 = 7
The lowest point reached is 1 (>= 1). With startValue = 4 the sum would hit 0
after the third element, which is not allowed, so 5 is the minimum.
```

### Example 2

```
Input:  nums = [1, 2]
Output: 1
Explanation: The running total only increases, so the smallest allowed
positive startValue, 1, already keeps every step-by-step sum >= 1.
```

### Example 3

```
Input:  nums = [1, -2, -3]
Output: 5
Explanation: The step-by-step sums relative to startValue dip to
startValue + (1 - 2 - 3) = startValue - 4. To keep this >= 1 we need
startValue >= 5, so the minimum is 5.
```

## Hint

Track the **Running Minimum of the prefix sums** as you scan once. If the most
negative prefix sum is `m`, you need `startValue + m >= 1`, i.e.
`startValue = max(1, 1 - m)`.
