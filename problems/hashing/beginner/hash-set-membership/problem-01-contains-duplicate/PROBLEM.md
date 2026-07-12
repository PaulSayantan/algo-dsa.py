# Contains Duplicate

**Difficulty:** Easy

**Source:** LeetCode 217 — Contains Duplicate

## Description

Given an integer array `nums`, return `true` if any value appears at least twice, and `false` if every element is distinct.

## Examples

### Example 1

```
Input:  nums = [1,2,3,1]
Output: true
```

### Example 2

```
Input:  nums = [1,2,3,4]
Output: false
```

## Hint

Scan once; if the current value is already in a set, it's a duplicate. Otherwise add it.
