# Design a Doubly-Linked Deque

**Difficulty:** Easy

**Source:** Classic — doubly-linked-list deque ADT

## Description

Implement a double-ended queue using a doubly linked list. Support `pushFront(v)`, `pushBack(v)`, `popFront()`, `popBack()` (each O(1); `pop*` return the removed value or `-1` if empty), and `isEmpty()`.

## Hint

Keep head and tail sentinel nodes. To push, splice a node next to the sentinel; to pop, unlink the sentinel's neighbor.
