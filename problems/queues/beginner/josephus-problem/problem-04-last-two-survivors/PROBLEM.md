# Josephus Last Two Survivors

**Difficulty:** Easy

**Source:** Classic — Josephus problem

## Description

There are `n` people numbered `1..n` (with `n >= 2`) standing in a circle. Counting starts at person 1; every `k`-th person is eliminated, and counting resumes from the next person. Instead of stopping at one survivor, stop when exactly **two** people remain. Return those two positions as a list sorted in ascending order, computed via circular-queue simulation.

## Examples

### Example 1

```
Input:  n = 7, k = 3
Output: [1, 4]
```

**Explanation:** Eliminations `3, 6, 2, 7, 5` leave `1` and `4`; sorted -> `[1, 4]`.

## Hint

Run the rotate-`k-1`-then-dequeue loop, but stop while `len(queue) > 2`; return the remaining two, sorted.
