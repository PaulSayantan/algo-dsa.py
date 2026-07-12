# Max Stack Backed by a Queue

**Difficulty:** Medium

**Source:** Classic — stack-via-queue with a max query

## Description

Design a LIFO stack, backed only by queue operations, that also supports a
`peekMax()` query returning the maximum element currently in the stack (without
removing it). Support `push(x)`, `pop()` (remove & return top), `top()` (peek),
and `peekMax()`.

Use the single-queue, rotate-on-push scheme so the newest element is always at
the queue's front (the stack top). `peekMax` scans the queue for the maximum.

## Examples

### Example 1

```
Input:  push 5,1,5; top; peekMax; pop; peekMax; pop; peekMax; top
Output: 5, 5, 5, 5, 1, 5, 5
```

**Explanation:** After pushing 5,1,5 the top is 5 and the max is 5. Popping the
top 5 leaves [1,5] (bottom→top), whose max is still 5. Popping 1 leaves [5],
whose max and top are both 5.

## Hint

Rotate on push so the front of the queue is the stack top; `peekMax` is a linear
scan (`max`) over the queue's contents.
