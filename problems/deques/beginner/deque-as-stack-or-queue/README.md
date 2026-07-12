# Deque as Stack or Queue

A deque generalizes both a stack and a queue, so a single `deque` can impersonate either. Use **one end** for both push and pop and you get LIFO (stack) behavior; push at one end and pop from the **opposite** end and you get FIFO (queue) behavior. Comparing the two on the same input makes the difference concrete: the stack output is the reverse of the queue output. This is why `collections.deque` is the recommended structure for both.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Deque as Stack vs Queue (Right End)](problem-01-stack-vs-queue-right-end/PROBLEM.md) | LIFO vs FIFO ends | Easy |
| 2 | [Deque as Stack vs Queue (Left End)](problem-02-stack-vs-queue-left-end/PROBLEM.md) | Same duality, left end | Easy |
| 3 | [Baseball Game (Deque as a Stack)](problem-03-baseball-game-stack/PROBLEM.md) | Deque as a LIFO stack | Easy |
| 4 | [Moving Average from Data Stream (Deque as a Queue)](problem-04-moving-average-queue/PROBLEM.md) | Deque as a bounded FIFO queue | Easy |
| 5 | [Number of Recent Calls (Deque as a Queue)](problem-05-recent-calls-queue/PROBLEM.md) | Deque as a sliding-window FIFO queue | Easy |
