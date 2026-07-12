# Linked-List-Based Queue

Backing a queue with a singly linked list gives O(1) **worst-case** enqueue and dequeue with no array shifting or resizing. Keep two pointers: `head` (where you dequeue) and `tail` (where you enqueue). The one subtlety is that when the queue drains to empty you must reset `tail` to `None` alongside `head`, or a later enqueue will dangle off a stale node.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design a Linked-List Queue](problem-01-design-linked-queue/PROBLEM.md) | Linked queue, O(1) head/tail | Easy |
| 2 | [Drain and Refill a Linked Queue](problem-02-drain-and-refill/PROBLEM.md) | Tail reset on empty | Easy |
| 3 | [Number of Recent Calls](problem-03-number-of-recent-calls/PROBLEM.md) | Enqueue tail, dequeue stale head (sliding window) | Easy |
| 4 | [Moving Average from Data Stream](problem-04-moving-average-from-data-stream/PROBLEM.md) | Fixed-size window queue + running sum | Easy |
| 5 | [Implement Stack using Queues](problem-05-implement-stack-using-queues/PROBLEM.md) | Rotate queue on push for LIFO head | Easy |
