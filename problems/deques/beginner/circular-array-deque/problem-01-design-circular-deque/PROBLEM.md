# Design Circular Deque

**Difficulty:** Medium

**Source:** LeetCode 641 — Design Circular Deque

## Description

Design your implementation of a circular double-ended queue with a fixed capacity `k`. Support `insertFront(v)`, `insertLast(v)`, `deleteFront()`, `deleteLast()` (each returning `True` on success and `False` if the operation cannot be performed), `getFront()` and `getRear()` (returning the value or `-1` if empty), and the predicates `isEmpty()` and `isFull()`. All operations run in O(1).

## Examples

### Example 1

```
Input:  MyCircularDeque(3); insertLast(1); insertLast(2); insertFront(3); insertFront(4); getRear(); isFull(); deleteLast(); insertFront(4); getFront()
Output: [true, true, true, false, 2, true, true, true, 4]
```

**Explanation:** insertFront(4) fails because the deque is full; getRear is 2.

## Hint

Store a fixed buffer, a head index, and a count. Wrap indices with % capacity; insertFront moves head back one slot.
