# Design Circular Deque

**Difficulty:** Easy

**Source:** LeetCode 641 — Design Circular Deque

## Description

Design a **fixed-capacity** double-ended queue. The constructor takes `k`, the maximum number of elements. Support:

- `insertFront(value)` — add `value` at the front; return `True`, or `False` if full.
- `insertLast(value)` — add `value` at the rear; return `True`, or `False` if full.
- `deleteFront()` — remove the front element; return `True`, or `False` if empty.
- `deleteLast()` — remove the rear element; return `True`, or `False` if empty.
- `getFront()` — return the front element, or `-1` if empty.
- `getRear()` — return the rear element, or `-1` if empty.
- `isEmpty()` / `isFull()` — return whether the deque is empty / full.

Every operation must run in O(1).

## Examples

### Example 1

```
Input:
  ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
  [[3], [1], [2], [3], [4], [], [], [], [4], []]
Output:
  [null, true, true, true, false, 2, true, true, true, 4]
```

**Explanation:** The fourth insert fails because the deque already holds 3 items; after `deleteLast` frees a slot, `insertFront(4)` succeeds and becomes the new front.

## Hint

Back the fixed-capacity deque with a doubly linked list plus a size counter: sentinel head/tail nodes make both-end splices O(1), and `size == k` is the "full" test.
