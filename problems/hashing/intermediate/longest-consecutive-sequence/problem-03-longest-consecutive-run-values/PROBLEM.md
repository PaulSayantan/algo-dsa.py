# Longest Consecutive Run (Return the Values)

**Difficulty:** Medium

**Source:** Classic — longest run of consecutive integers (returned)

## Description

Given an integer array `nums`, return the longest run of consecutive integers as an ascending list of its values. If several runs share the maximum length, return the one with the smallest starting value. Return an empty list for empty input.

## Examples

### Example 1

```
Input:  nums = [100,4,200,1,3,2]
Output: [1, 2, 3, 4]
```

### Example 2

```
Input:  nums = [3,1,2,8,9]
Output: [1, 2, 3]
```

**Explanation:** {1,2,3} (length 3) beats {8,9} (length 2).

## Hint

Iterate run-starts in sorted order and keep the first run that achieves the max length.
