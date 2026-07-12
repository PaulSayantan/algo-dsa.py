# Ternary Expression Parser

**Difficulty:** Medium

**Source:** LeetCode 439 — Ternary Expression Parser

## Description

Given a string `expression` representing a nested ternary expression, evaluate
it and return the resulting single-character token as a string.

The expression contains only digits `0-9`, the letters `T` and `F`, and the
characters `?` and `:`. It groups right-to-left, so `a?b:c` means "if `a` is `T`
then `b` else `c`", where `b` and `c` may themselves be ternary expressions. The
input is always valid; `T` and `F` appear only as conditions, and every result
is a single character (`0-9`, `T`, or `F`).

## Examples

### Example 1

```
Input:  expression = "F?1:T?4:5"
Output: "4"
```

**Explanation:** Right-associative, so this is `F ? 1 : (T ? 4 : 5)`. The outer `F` picks the else branch `T?4:5`, whose `T` picks `4`.

## Hint

Scan right-to-left pushing chars on a stack; when the top is `?`, pop condition, `?`, true-token, `:`, false-token and push the chosen branch — a stack fold over nested groups.
