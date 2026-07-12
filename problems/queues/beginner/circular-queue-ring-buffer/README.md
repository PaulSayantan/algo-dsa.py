# Circular Queue / Ring Buffer

A **circular queue** (ring buffer) stores elements in a fixed-size array and wraps the front and rear indices around modulo the capacity, so no shifting is ever needed — every operation is O(1). Tracking a `head` index plus a live `count` (rather than a separate tail) cleanly distinguishes the empty state from the full state. Ring buffers underpin bounded producer/consumer queues, streaming windows, and hardware I/O buffers.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design Circular Queue](problem-01-design-circular-queue/PROBLEM.md) | Fixed-capacity ring, modulo wrap | Medium |
| 2 | [Ring Buffer with Overwrite](problem-02-ring-buffer-overwrite/PROBLEM.md) | Overwrite-oldest ring | Medium |
| 3 | [Moving Average from Data Stream](problem-03-moving-average-stream/PROBLEM.md) | Fixed-window sum over a ring | Easy |
| 4 | [Round-Robin Task Scheduler](problem-04-round-robin-scheduler/PROBLEM.md) | Modulo-wrapping head cursor | Easy |
| 5 | [Fixed-Delay Line](problem-05-fixed-delay-line/PROBLEM.md) | Fixed-lag ring buffer, modulo head | Easy |
