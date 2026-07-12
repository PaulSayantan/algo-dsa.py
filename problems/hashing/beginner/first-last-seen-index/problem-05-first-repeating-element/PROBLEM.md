# First Repeating Element

**Difficulty:** Easy

**Source:** Classic — first repeating element

## Description

Given an integer array `nums`, return the index of the first element that appears more than once — that is, the smallest index `i` such that `nums[i]` occurs at least twice in the array. Return `-1` if every element is unique.

## Examples

### Example 1

```
Input:  nums = [10,5,3,4,3,5,6]
Output: 1
```

**Explanation:** 5 (index 1) is the first value that repeats.

## Hint

Count occurrences first; then scan left to right and return the first index whose value has count > 1.
