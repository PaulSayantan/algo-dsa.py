# Josephus Survivor

**Difficulty:** Medium

**Source:** Classic — Josephus problem

## Description

There are `n` people numbered `1..n` in a circle. Counting starts at person 1; every `k`-th person is eliminated, and counting resumes from the next person. Return the 1-indexed position of the last survivor, computed via circular-queue simulation.

## Examples

### Example 1

```
Input:  n = 7, k = 3
Output: 4
```

**Explanation:** Eliminations 3,6,2,7,5,1 leave 4.

## Hint

Queue of 1..n; move k-1 to the back, remove the next; the last one left survives.
