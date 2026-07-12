# First and Last Occurrence via Hash Map

**Difficulty:** Easy

**Source:** Classic — first/last occurrence lookup

## Description

Given an integer array `nums` and a `target`, return `[first, last]`, the first and last indices at which `target` appears. If `target` is absent, return `[-1, -1]`.

## Examples

### Example 1

```
Input:  nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2

```
Input:  nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## Hint

Build a first-seen and a last-seen index map in one pass, then read both for the target.
