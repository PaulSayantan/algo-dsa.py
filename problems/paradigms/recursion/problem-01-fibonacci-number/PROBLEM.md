# Fibonacci Number

**Difficulty:** Easy

**Source:** LeetCode 509 (Fibonacci Number)

## Description

The **Fibonacci numbers**, commonly denoted `F(n)`, form a sequence in which each
number is the sum of the two preceding ones, starting from `0` and `1`. That is:

```
F(0) = 0,  F(1) = 1
F(n) = F(n - 1) + F(n - 2),  for n > 1
```

Given an integer `n`, return `F(n)`.

This is the canonical first recursion problem: the definition of `F(n)` is *itself*
recursive, with two base cases (`F(0)` and `F(1)`) and a recursive case that expresses
`F(n)` in terms of two strictly smaller subproblems.

## Constraints

- `0 <= n <= 30`

## Examples

### Example 1

```
Input:  n = 2
Output: 1
```

Explanation: `F(2) = F(1) + F(0) = 1 + 0 = 1`.

### Example 2

```
Input:  n = 3
Output: 2
```

Explanation: `F(3) = F(2) + F(1) = 1 + 1 = 2`.

### Example 3

```
Input:  n = 4
Output: 3
```

Explanation: `F(4) = F(3) + F(2) = 2 + 1 = 3`.

## Hint

Use **Recursion**: define the two base cases (`F(0) = 0`, `F(1) = 1`) and, for larger
`n`, return the sum of the recursive calls on `n - 1` and `n - 2`. Each call reduces
the problem toward the base cases.
