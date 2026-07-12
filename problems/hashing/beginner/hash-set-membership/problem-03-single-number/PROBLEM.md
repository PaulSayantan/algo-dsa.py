# Single Number

**Difficulty:** Easy

**Source:** LeetCode 136 — Single Number

## Description

Given a non-empty array `nums` where every element appears exactly twice except for one element that appears once, return that single element.

## Examples

### Example 1

```
Input:  nums = [4,1,2,1,2]
Output: 4
```

## Hint

Toggle membership in a set: add on first sight, remove on second. The lone survivor is the answer.
