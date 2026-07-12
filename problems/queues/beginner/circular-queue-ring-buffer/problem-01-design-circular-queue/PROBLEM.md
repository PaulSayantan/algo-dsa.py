# Design Circular Queue

**Difficulty:** Medium

**Source:** LeetCode 622 — Design Circular Queue

## Description

Design a circular queue of fixed capacity `k`. Implement `enQueue(value)`, `deQueue()`, `Front()`, `Rear()`, `isEmpty()`, and `isFull()`. `enQueue`/`deQueue` return `True` on success and `False` when the operation is not possible (full/empty). `Front`/`Rear` return the element or `-1` if the queue is empty.

## Examples

### Example 1

```
Input:  MyCircularQueue(3); enQueue(1),enQueue(2),enQueue(3),enQueue(4),Rear(),isFull(),deQueue(),enQueue(4),Rear()
Output: true, true, true, false, 3, true, true, true, 4
```

## Hint

Store head + count over a size-k array; index the rear as (head + count - 1) % k. Wrap with modulo.
