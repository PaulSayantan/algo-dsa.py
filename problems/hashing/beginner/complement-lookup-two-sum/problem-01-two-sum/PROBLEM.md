# Two Sum

**Difficulty:** Easy

**Source:** LeetCode 1 — Two Sum

## Description

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Exactly one valid answer exists, and you may not use the same element twice. Return the indices in increasing order.

## Examples

### Example 1

```
Input:  nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Explanation:** nums[0] + nums[1] == 9.

### Example 2

```
Input:  nums = [3,2,4], target = 6
Output: [1,2]
```

## Hint

Keep a value -> index map. For each x, check if (target - x) is already in the map.
