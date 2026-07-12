# Array-Based Queue

A **queue** is a FIFO (first-in, first-out) container: elements leave in the same order they arrived. The simplest concrete implementation keeps the items in a list, appending at the **rear** and removing from the **front**. It is the foundation for every queue technique that follows; note that removing from the front of a plain Python list is O(n), which later implementations (`collections.deque`, linked lists, ring buffers) fix to O(1).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design a Queue (Array-Backed)](problem-01-design-array-queue/PROBLEM.md) | Queue ADT, FIFO order | Easy |
| 2 | [Simulate Queue Operations](problem-02-simulate-queue-operations/PROBLEM.md) | Queue simulation | Easy |
| 3 | [Number of Recent Calls](problem-03-number-of-recent-calls/PROBLEM.md) | Sliding-window queue, dequeue stale front | Easy |
| 4 | [Moving Average from Data Stream](problem-04-moving-average-from-data-stream/PROBLEM.md) | Fixed-size window queue | Easy |
| 5 | [Time Needed to Buy Tickets](problem-05-time-needed-to-buy-tickets/PROBLEM.md) | FIFO line simulation | Easy |
