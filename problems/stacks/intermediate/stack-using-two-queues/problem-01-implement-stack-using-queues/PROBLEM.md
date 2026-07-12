# Implement Stack using Queues

**Difficulty:** Easy

**Source:** LeetCode 225 — Implement Stack using Queues

## Description

Implement a last-in-first-out (LIFO) stack using only queue operations. Support `push(x)`, `pop()` (remove & return top), `top()`, and `empty()`.

## Examples

### Example 1

```
Input:  push 1,2; top; pop; top
Output: 2, 2, 1
```

## Hint

On push, enqueue then rotate the queue so the new element sits at the front.
