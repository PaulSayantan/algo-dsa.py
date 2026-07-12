# Implement Queue using Stacks

**Difficulty:** Easy

**Source:** LeetCode 232 — Implement Queue using Stacks

## Description

Implement a first-in-first-out (FIFO) queue using only two stacks. Support `push(x)` (enqueue), `pop()` (dequeue & return front), `peek()` (front), and `empty()`. Use only standard stack operations.

## Examples

### Example 1

```
Input:  push 1,2; peek; pop; empty
Output: 1, 1, false
```

## Hint

Push to the 'in' stack; when serving, if 'out' is empty, pour 'in' into 'out' first.
