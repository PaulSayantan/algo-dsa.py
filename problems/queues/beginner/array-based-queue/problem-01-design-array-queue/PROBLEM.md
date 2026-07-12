# Design a Queue (Array-Backed)

**Difficulty:** Easy

**Source:** Classic — array-backed queue ADT

## Description

Implement a first-in-first-out (FIFO) queue using a list. Support `enqueue(x)` (add at the rear), `dequeue()` (remove & return the front), `front()` (peek at the front), and `empty()`. Return the value produced by each query operation.

## Hint

Append to the end for enqueue; the element at index 0 is the front — pop(0) to dequeue.
