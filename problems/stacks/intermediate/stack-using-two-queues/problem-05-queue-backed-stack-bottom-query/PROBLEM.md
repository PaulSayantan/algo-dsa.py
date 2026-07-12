# Queue-Backed Stack with Bottom Query

**Difficulty:** Medium

**Source:** Classic — stack-via-queue with a bottom peek

## Description

Design a LIFO stack backed only by queue operations that, in addition to the
usual API, can report the **bottom** (oldest / first-pushed) element still in
the stack. Support `push(x)`, `pop()` (remove & return top), `top()` (peek top),
`getBottom()` (peek the bottom without removing), and `empty()`.

Use the single-queue rotate-on-push scheme: the front of the queue is the stack
top, so the **back** of the queue is the stack bottom.

## Examples

### Example 1

```
Input:  push 10,20,30; top; getBottom; pop; getBottom; top; pop; pop; empty
Output: 30, 10, 30, 10, 20, 20, 10, True
```

**Explanation:** After pushing 10,20,30 the top is 30 and the bottom is 10.
Popping removes 30; the bottom is still 10 and the new top is 20. Popping again
removes 20, then 10, leaving the stack empty.

## Hint

Rotate on push so the queue front is the top; then `getBottom` is simply the
element at the back of the queue (`q[-1]`).
