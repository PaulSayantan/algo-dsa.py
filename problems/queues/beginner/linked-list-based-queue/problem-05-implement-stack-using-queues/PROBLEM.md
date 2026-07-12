# Implement Stack using Queues

**Difficulty:** Easy

**Source:** LeetCode 225 — Implement Stack using Queues

## Description

Implement a LIFO stack using only a FIFO queue (backed here by a singly linked list). Support:

- `MyStack()` initializes the stack.
- `push(x)` pushes `x` onto the top of the stack.
- `pop()` removes and returns the element on top of the stack.
- `top()` returns the element on top of the stack without removing it.
- `empty()` returns `True` if the stack is empty, `False` otherwise.

Use a single linked-list queue. On `push(x)`, enqueue `x` at the tail, then rotate the queue by dequeuing and re-enqueuing every *earlier* element (`size - 1` of them) so the newest element ends up at the head. Then `pop`/`top` simply read the head, keeping LIFO order.

## Examples

### Example 1

```
Input:
  ["MyStack", "push", "push", "top", "pop", "empty"]
  [[], [1], [2], [], [], []]
Output:
  [null, null, null, 2, 2, false]
```

**Explanation:** After pushing `1` then `2`, the rotation puts `2` at the head, so `top()` returns `2`, `pop()` removes and returns `2`, and the stack is not empty (still holds `1`).

## Hint

Keep one linked-list queue; after enqueuing the new value, dequeue-then-enqueue the other elements so the newest sits at the head for O(1) LIFO reads.
