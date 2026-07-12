# Reverse First K Elements of a Queue

**Difficulty:** Medium

**Source:** Classic — reverse first k of a queue

## Description

Given a queue as a list (front = index 0) and an integer `k` (0 ≤ k ≤ len), reverse the order of the **first k** elements while leaving the remaining elements in their original order, and return the resulting list.

## Examples

### Example 1

```
Input:  q = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
```

## Hint

Stack the first k and pop them back to reverse that prefix; then append the untouched tail.
