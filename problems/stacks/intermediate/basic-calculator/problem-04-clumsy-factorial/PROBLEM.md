# Clumsy Factorial

**Difficulty:** Medium

**Source:** LeetCode 1006 — Clumsy Factorial

## Description

The *clumsy factorial* of a positive integer `n` takes the numbers `n, n-1, ..., 1` and inserts a fixed rotation of operators between them: multiply, divide, add, subtract, repeating in that order. So `clumsy(n) = n * (n-1) / (n-2) + (n-3) - (n-4) * (n-5) / (n-6) + ...`.

Evaluate the expression using normal operator precedence (`*` and `/` bind tighter than `+` and `-`) and left-to-right association for `*`/`/`. Integer division truncates toward zero. Return the resulting value.

Given `n`, return `clumsy(n)`.

## Examples

### Example 1

```
Input:  n = 4
Output: 7
```

**Explanation:** `4 * 3 / 2 + 1 = 6 + 1 = 7`.

### Example 2

```
Input:  n = 10
Output: 12
```

**Explanation:** `10 * 9 / 2 + 8 - 7 * 6 / 5 + 4 - 3 * 2 / 1 = 45 + 8 - 8 + 4 - 6 = 12`.

## Hint

It is the same term stack as Basic Calculator II: push `+`/`-` terms, but fold `*`/`/` into the last pushed term right away, then sum the stack.
