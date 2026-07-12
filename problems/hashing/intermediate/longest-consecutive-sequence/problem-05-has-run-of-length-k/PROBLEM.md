# Consecutive Run of Length At Least K

**Difficulty:** Easy

**Source:** Classic — existence of a length-k band of consecutive numbers

## Description

Given an integer array `nums` and an integer `k`, return `True` if the array contains a run of at least `k` consecutive integers, otherwise `False`. `k <= 0` is trivially satisfiable.

## Examples

### Example 1

```
Input:  nums = [1,2,3,4], k = 3
Output: true
```

**Explanation:** The run [1,2,3,4] has length 4 >= 3.

### Example 2

```
Input:  nums = [10,20,30], k = 2
Output: false
```

**Explanation:** No two values are consecutive.

## Hint

Expand each run-start; short-circuit True the moment a run reaches length k.
