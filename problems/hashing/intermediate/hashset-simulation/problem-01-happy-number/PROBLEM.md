# Happy Number

**Difficulty:** Easy

**Source:** LeetCode 202 — Happy Number

## Description

A number is happy if repeatedly replacing it by the sum of the squares of its digits eventually reaches 1. Otherwise it loops endlessly without reaching 1. Return whether `n` is happy.

## Examples

### Example 1

```
Input:  n = 19
Output: true
```

## Hint

Iterate the transform; store seen values in a set; stop at 1 (happy) or a repeat (not).
