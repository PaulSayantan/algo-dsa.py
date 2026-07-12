# Happy Number

**Difficulty:** Easy

**Source:** LeetCode 202 — Happy Number

## Description

A number is *happy* if repeatedly replacing it by the sum of the squares of its digits eventually reaches `1`. If the process instead loops endlessly in a cycle that never reaches `1`, the number is not happy. Given `n`, return `true` iff `n` is happy.

## Examples

### Example 1

```
Input:  n = 19
Output: true
```

**Explanation:** 1^2+9^2=82, 8^2+2^2=68, 6^2+8^2=100, 1^2+0+0=1.

## Hint

Iterate the digit-square-sum transform, storing each value in a set; a repeat means a cycle (not happy).
