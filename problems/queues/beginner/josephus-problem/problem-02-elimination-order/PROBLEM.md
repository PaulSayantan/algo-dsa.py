# Josephus Elimination Order

**Difficulty:** Medium

**Source:** Classic — Josephus elimination order

## Description

For `n` people numbered `1..n` in a circle and step `k`, return the list of people in the exact order they are eliminated. Counting starts at person 1 and every `k`-th person is removed. The final survivor is **not** part of the returned list (it is the one never eliminated).

## Examples

### Example 1

```
Input:  n = 7, k = 3
Output: [3, 6, 2, 7, 5, 1]
```

**Explanation:** Survivor 4 is not listed.

## Hint

Same rotate-k-1-then-dequeue loop, but append each dequeued person to an order list.
