# Stack Using Two Queues

The dual construction: emulate a LIFO stack with FIFO queues. The simplest correct scheme makes `push` costly — after enqueuing the new element, rotate all earlier elements behind it so the newest is always at the front, ready to be popped in O(1).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Implement Stack using Queues](problem-01-implement-stack-using-queues/PROBLEM.md) | LIFO via rotating queue | Easy |
| 2 | [Two-Queue Stack (Push-Efficient)](problem-02-two-queue-pop-heavy-stack/PROBLEM.md) | O(1) push, drain-and-swap pop | Medium |
| 3 | [Max Stack Backed by a Queue](problem-03-max-stack-using-queues/PROBLEM.md) | Rotate-on-push + max scan | Medium |
| 4 | [Replay Stack Operations Using a Queue](problem-04-stack-op-sequence-replay/PROBLEM.md) | Op-sequence simulation | Medium |
| 5 | [Queue-Backed Stack with Bottom Query](problem-05-queue-backed-stack-bottom-query/PROBLEM.md) | Front=top, back=bottom | Medium |
