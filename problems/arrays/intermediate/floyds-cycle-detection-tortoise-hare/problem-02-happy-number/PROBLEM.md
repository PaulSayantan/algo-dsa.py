# Happy Number

**Difficulty:** Easy

**Source:** LeetCode 202 — Happy Number

## Description

Write an algorithm to determine if a number `n` is *happy*.

A **happy number** is defined by the following process:

- Starting with any positive integer, replace the number by the sum of the
  squares of its digits.
- Repeat the process until the number equals `1` (where it will stay), or it
  **loops endlessly in a cycle** that never includes `1`.
- Those numbers for which this process **ends in 1** are happy.

Return `true` if `n` is a happy number, and `false` if not.

The key observation is that the "next number" operation is a deterministic
function of the current number, so the sequence of numbers you generate is
exactly the kind of implicit sequence Floyd's algorithm was designed for: it
either reaches `1` or falls into a repeating cycle.

## Constraints

- `1 <= n <= 2^31 - 1`

## Examples

### Example 1

```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
The process reaches 1, so 19 is happy.
```

### Example 2

```
Input: n = 2
Output: false
Explanation:
2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> ...
The sequence returns to 4 and loops forever without ever reaching 1, so 2 is
not happy.
```

### Example 3

```
Input: n = 1
Output: true
Explanation: 1 is already 1, so the process ends immediately and 1 is happy.
```

## Hint

The digit-square-sum operation defines a single "next" value for every number,
so the sequence must eventually repeat. Apply **Floyd's Cycle Detection
(Tortoise & Hare)** with a slow pointer (one step) and a fast pointer (two
steps): if they meet at `1`, the number is happy; if they meet at any other
value, there is a non-`1` cycle.
