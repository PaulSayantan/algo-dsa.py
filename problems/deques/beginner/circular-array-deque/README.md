# Circular-Array Deque

A **deque** (double-ended queue) supports insertion and removal at both ends in O(1). Backing it with a fixed-size **circular array** avoids shifting elements: you keep a `head` index and a `count`, and every position is taken modulo the capacity so the logical front and rear wrap around the physical buffer. This is the array counterpart to the linked-list deque and the structure behind ring buffers.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design Circular Deque](problem-01-design-circular-deque/PROBLEM.md) | Circular buffer, O(1) ends | Medium |
| 2 | [Circular Deque — Empty Handling and Wrap-Around](problem-02-circular-deque-empty-and-wrap/PROBLEM.md) | Empty/full edge cases | Medium |
| 3 | [Design Circular Queue](problem-03-design-circular-queue/PROBLEM.md) | FIFO ring buffer, O(1) ends | Easy |
| 4 | [Moving Average from Data Stream](problem-04-moving-average-data-stream/PROBLEM.md) | Fixed window + running sum | Easy |
| 5 | [Design Hit Counter](problem-05-design-hit-counter/PROBLEM.md) | Circular bucket recycling | Easy |
