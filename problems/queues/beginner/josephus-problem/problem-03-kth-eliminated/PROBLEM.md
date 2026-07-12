# Josephus K-th Eliminated

**Difficulty:** Easy

**Source:** Classic — Josephus problem

## Description

There are `n` people numbered `1..n` standing in a circle. Counting starts at person 1; every `k`-th person is eliminated, and counting resumes from the next person. Return the 1-indexed position of the `m`-th person to be eliminated (`1 <= m <= n - 1`), computed via circular-queue simulation.

## Examples

### Example 1

```
Input:  n = 7, k = 3, m = 1
Output: 3
```

**Explanation:** With `n = 7, k = 3` the elimination order is `3, 6, 2, 7, 5, 1`; the 1st removed is `3`.

## Hint

Run the rotate-`k-1`-then-dequeue loop, recording each removed person; return the `m`-th recorded value.
