# Queue Using Two Stacks

A FIFO queue can be built from two LIFO stacks: an 'in' stack receives pushes, and an 'out' stack serves pops. When 'out' is empty, pour all of 'in' into it, reversing the order so the oldest element surfaces. Each element moves between stacks at most once, giving amortized O(1) operations.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Implement Queue using Stacks](problem-01-implement-queue-using-stacks/PROBLEM.md) | Amortized FIFO via 2 stacks | Easy |
| 2 | [Max Value in a Queue](problem-02-max-value-in-queue/PROBLEM.md) | Two-stack queue with running max per frame | Medium |
| 3 | [Design Hit Counter](problem-03-design-hit-counter/PROBLEM.md) | Two-stack FIFO sliding-window over timestamps | Medium |
| 4 | [Dota2 Senate](problem-04-dota2-senate/PROBLEM.md) | Per-party two-stack queues, re-enqueue winners | Medium |
| 5 | [Reveal Cards in Increasing Order](problem-05-reveal-cards-in-increasing-order/PROBLEM.md) | Simulate reveal on a two-stack queue of slots | Medium |
