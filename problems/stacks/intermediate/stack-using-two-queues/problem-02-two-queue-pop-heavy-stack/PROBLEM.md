# Two-Queue Stack (Push-Efficient)

**Difficulty:** Medium

**Source:** Classic — LIFO via two queues, O(1) push

## Description

Implement a last-in-first-out (LIFO) stack using **two** FIFO queues, but make `push(x)` an O(1) operation and move the work into `pop`/`top`. Support `push(x)`, `pop()` (remove & return top), `top()` (peek), and `empty()`.

Unlike the single-queue rotate-on-push design, here `push` simply enqueues. `pop`/`top` drain all but the last element of the primary queue into the auxiliary queue, expose the tail, then swap the two queues.

## Examples

### Example 1

```
Input:  push 3,5,7; top; pop; top; push 9; pop; pop; pop; empty
Output: 7, 7, 5, 9, 5, 3, True
```

**Explanation:** The stack sees 7 on top after the first three pushes. Popping removes 7, then 9 (after it is pushed), then 5, then 3, leaving it empty.

## Hint

`push` just enqueues onto `q1`. For `pop`, move `len(q1)-1` elements to `q2`, take the last remaining element of `q1`, then swap `q1` and `q2`. `top` is the same but re-enqueue the exposed element.
