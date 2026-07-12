# Josephus Circle of Names

**Difficulty:** Easy

**Source:** Classic — Josephus problem

## Description

A group of players, given by a list of distinct name strings `names`, stand in a circle in the given order. Counting starts at the first player; every `k`-th player is eliminated, and counting resumes from the next player. Return the **name** of the last remaining player, computed via circular-queue simulation. Assume `names` is non-empty and `k >= 1`.

## Examples

### Example 1

```
Input:  names = ["Alice", "Bob", "Carol", "Dan"], k = 2
Output: 'Alice'
```

**Explanation:** With `k = 2` the eliminations are `Bob, Dan, Carol`, leaving `Alice`.

## Hint

Seed the queue with the names themselves; run the usual rotate-`k-1`-then-dequeue loop until one name remains.
