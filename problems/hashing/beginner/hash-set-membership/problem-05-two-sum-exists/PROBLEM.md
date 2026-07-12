# Two-Sum Existence

**Difficulty:** Easy

**Source:** LeetCode 1 — Two Sum (existence variant)

## Description

Given an integer array `nums` and an integer `target`, return `true` if there exist two **distinct positions** `i != j` with `nums[i] + nums[j] == target`, and `false` otherwise. (This is the membership-set core of Two Sum, returning a boolean instead of the index pair.)

## Examples

### Example 1

```
Input:  nums = [2,7,11,15], target = 9
Output: true
```

**Explanation:** 2 + 7 = 9.

### Example 2

```
Input:  nums = [1,2,3], target = 7
Output: false
```

## Hint

For each value x, the pair partner is target - x; check whether it was already seen before adding x.
