# Fibonacci Number

**Difficulty:** Easy

**Source:** LeetCode 509 (Fibonacci Number)

## Description

The Fibonacci numbers, commonly denoted `F(n)`, form a sequence called the *Fibonacci
sequence*, such that each number is the sum of the two preceding ones, starting from `0`
and `1`. That is:

```
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1
```

Given an integer `n`, return `F(n)`.

This is the canonical first problem for learning dynamic programming: the naive
recursion recomputes the same values exponentially many times, and caching those
repeated subproblems collapses the work to linear time.

## Constraints

- `0 <= n <= 30`

## Examples

### Example 1

```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

### Example 2

```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

### Example 3

```
Input: n = 10
Output: 55
Explanation: The sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55; the value at index 10 is 55.
```

## Hint

Use **Dynamic Programming (memoization / tabulation)**: each `F(k)` is needed by both
`F(k + 1)` and `F(k + 2)`, so compute every `F(k)` only once and reuse it.
