# Push–Relabel (FIFO)

Push–relabel takes a different tack from augmenting paths: it maintains a preflow and node 'heights', repeatedly pushing excess toward the sink and relabeling stuck nodes. The FIFO variant processes a queue of active (excess-bearing) nodes, achieving O(V³).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Maximum Flow (FIFO Push–Relabel)](problem-01-max-flow-push-relabel/PROBLEM.md) | Preflow + active queue | Hard |
