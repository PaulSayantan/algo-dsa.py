# Design Circular Queue

**Difficulty:** Easy

**Source:** LeetCode 622 — Design Circular Queue

## Description

Design a circular queue (a FIFO ring buffer) with a fixed capacity `k`. Support `enQueue(v)` and `deQueue()` (each returning `True` on success and `False` if the queue is full / empty respectively), `Front()` and `Rear()` (returning the value at the front / rear, or `-1` if empty), and the predicates `isEmpty()` and `isFull()`. All operations run in O(1).

Unlike a plain array-backed queue, when the tail reaches the end of the buffer it wraps back to the front, reusing slots vacated by `deQueue`.

## Examples

### Example 1

```
Input:  MyCircularQueue(3); enQueue(1); enQueue(2); enQueue(3); enQueue(4); Rear(); isFull(); deQueue(); enQueue(4); Rear()
Output: [true, true, true, false, 3, true, true, true, 4]
```

**Explanation:** enQueue(4) fails because the queue is full; Rear is 3. After deQueue frees the front slot, enQueue(4) succeeds and the new Rear is 4.

## Hint

Keep a fixed buffer, a `head` index, and a `count`. Enqueue writes at `(head + count) % capacity`; dequeue advances `head` with `% capacity`.
