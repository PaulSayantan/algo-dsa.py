# Decimal to Binary

**Difficulty:** Easy

**Source:** Classic — base conversion

## Description

Given a non-negative integer `n`, return its binary representation as a string (no leading zeros; `0` maps to `"0"`). Use a stack of remainders from repeated division by 2.

## Examples

### Example 1

```
Input:  n = 10
Output: "1010"
```

## Hint

Push n%2, then n//=2, until n is 0; pop the remainders to form the string.
