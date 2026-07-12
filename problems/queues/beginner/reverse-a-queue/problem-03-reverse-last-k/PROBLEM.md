# Reverse Last K Elements of a Queue

**Difficulty:** Easy

**Source:** Classic — reverse last k of a queue

## Description

Given a queue as a list (front = index 0) and an integer `k` (0 ≤ k ≤ len), reverse the order of the **last k** elements while leaving the first `len - k` elements in their original order, and return the resulting list.

## Examples

### Example 1

```
Input:  q = [1, 2, 3, 4, 5], k = 3
Output: [1, 2, 5, 4, 3]
```

**Explanation:** The first `5 - 3 = 2` elements `[1, 2]` stay put; the last three `[3, 4, 5]` are reversed to `[5, 4, 3]`.

## Hint

Emit the untouched front, then push the last k onto a stack and pop them out — LIFO reverses that suffix.
