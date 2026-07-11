# Climbing Stairs

**Difficulty:** Easy

**Source:** LeetCode 70 (Climbing Stairs)

## Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` step or `2` steps. In how many **distinct ways** can
you climb to the top?

Each "way" is a distinct ordered sequence of `1`- and `2`-step moves whose sizes sum to
`n`. This is a counting problem: the number of ways to reach step `n` is the number of
ways to reach step `n - 1` (then take a single step) plus the number of ways to reach
step `n - 2` (then take a double step).

## Constraints

- `1 <= n <= 45`

## Examples

### Example 1

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top:
  1. 1 step + 1 step
  2. 2 steps
```

### Example 2

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top:
  1. 1 + 1 + 1
  2. 1 + 2
  3. 2 + 1
```

### Example 3

```
Input: n = 5
Output: 8
Explanation: The counts follow 1, 2, 3, 5, 8 for n = 1, 2, 3, 4, 5 — a Fibonacci-style recurrence.
```

## Hint

Use **Dynamic Programming (memoization / tabulation)**: `ways(n) = ways(n - 1) + ways(n - 2)`.
The same subproblem `ways(k)` is reached along many paths, so cache it.
