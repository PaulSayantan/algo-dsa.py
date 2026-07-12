# Base 7

**Difficulty:** Easy

**Source:** LeetCode 504 — Base 7

## Description

Given an integer `num`, return its base-7 representation as a string. The input may be
negative, in which case the result starts with a `'-'` sign. `0` maps to `"0"`, and
there are no leading zeros otherwise. Use a stack of remainders from repeated division
by 7 on the absolute value.

Constraints: `-10^7 <= num <= 10^7`.

## Examples

### Example 1

```
Input:  num = 100
Output: "202"
```

**Explanation:** 100 % 7 = 2, 100 // 7 = 14; 14 % 7 = 0, 14 // 7 = 2; 2 % 7 = 2. Pop to read "202".

## Hint

Remember the sign, work on `abs(num)`: push `n % 7` and `n //= 7` onto a stack; pop the digits and prepend `'-'` if the input was negative.
