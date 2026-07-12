# Design a Linked-List Queue

**Difficulty:** Easy

**Source:** Classic — linked-list queue ADT

## Description

Implement a FIFO queue using a singly linked list with `head` and `tail` pointers so that `enqueue`, `dequeue`, `front`, `size`, and `empty` are all O(1) worst-case. Enqueue links a node after the tail; dequeue unlinks the head.

## Hint

Enqueue at the tail, dequeue at the head; keep a size counter and reset tail to None when it empties.
