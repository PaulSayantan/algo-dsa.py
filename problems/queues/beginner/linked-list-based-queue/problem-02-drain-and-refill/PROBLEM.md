# Drain and Refill a Linked Queue

**Difficulty:** Easy

**Source:** Classic — tail-pointer edge case

## Description

Using the same linked-list queue, exercise the empty-then-refill path: enqueue an element, dequeue it so the queue is empty, then enqueue again. A correct implementation resets the `tail` pointer when the queue drains, so the refilled queue behaves normally.

## Hint

After the queue empties, tail must be None so the next enqueue starts a fresh single-node queue.
