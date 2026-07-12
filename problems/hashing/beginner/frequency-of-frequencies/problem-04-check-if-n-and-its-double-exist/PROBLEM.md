# Check If N and Its Double Exist

**Difficulty:** Easy

**Source:** LeetCode 1346 — Check If N and Its Double Exist

## Description

Given an integer array `arr`, return `true` if there exist two distinct indices `i` and `j` such that `arr[i] == 2 * arr[j]`. Otherwise return `false`. (Two zeros satisfy this because `0 = 2*0`.)

## Examples

### Example 1

```
Input:  arr = [10,2,5,3]
Output: true
```

**Explanation:** 10 = 2 * 5.

### Example 2

```
Input:  arr = [3,1,7,11]
Output: false
```

## Hint

Scan once with a set of seen values; for each x check if 2*x or x/2 (when x is even) was already seen before inserting x.
