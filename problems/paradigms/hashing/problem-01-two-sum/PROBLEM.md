# Two Sum

**Difficulty:** Easy

**Source:** LeetCode 1 (Two Sum)

## Description

Given an array of integers `nums` and an integer `target`, return the **indices**
of the two numbers such that they add up to `target`.

You may assume that each input has **exactly one** solution, and you may not use
the same element twice. You can return the answer in any order.

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid answer exists.

## Examples

### Example 1

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9, so the indices are 0 and 1.
```

### Example 2

```
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] = 2 + 4 = 6. Note nums[0] = 3 is not reused,
even though 3 + 3 = 6, because the two elements must be at different indices.
```

### Example 3

```
Input:  nums = [3, 3], target = 6
Output: [0, 1]
Explanation: The two 3's live at distinct indices 0 and 1 and sum to 6.
```

## Hint

Use **Hashing**: as you scan the array, remember each value you have seen (mapped
to its index). For the current number `x`, the value you actually need is
`target - x` — check whether it is already in your map before storing `x`.
