# Round-Robin Scheduling

Round-robin CPU scheduling cycles a queue of processes, giving each a fixed time quantum before requeuing it if unfinished. The FIFO queue guarantees fairness; simulating it yields each process's completion order and time.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Round-Robin Completion Order](problem-01-round-robin-order/PROBLEM.md) | Quantum requeue | Medium |
| 2 | [Round-Robin Waiting Times](problem-02-round-robin-waiting-times/PROBLEM.md) | Global clock + completion times | Medium |
| 3 | [Round-Robin Gantt Order](problem-03-round-robin-gantt-order/PROBLEM.md) | Quantum requeue (dispatch order) | Medium |
| 4 | [Round-Robin With Arrival Times](problem-04-round-robin-arrival-times/PROBLEM.md) | Arrival-driven enqueue order | Medium |
| 5 | [Round-Robin Load Balancer](problem-05-round-robin-load-balancer/PROBLEM.md) | Cyclic dispatch with add/remove | Medium |
