# Double-Ended Priority Queue

**Difficulty:** Hard

**Source:** Classic — min-max heap / DEPQ (cf. Library Checker)

## Description

Implement a double-ended priority queue over integers supporting `push(x)`, `popMin()` (remove & return the minimum), and `popMax()` (remove & return the maximum). Assume all operations are valid (no pop from empty). Values may repeat.

## Hint

Two heaps (min and max) over (value, id) plus an alive-count map; skip stale tops lazily on each pop.
