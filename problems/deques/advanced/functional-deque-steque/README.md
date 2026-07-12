# Functional Deque (Steque)

A purely functional deque never mutates: each operation returns a new version. A two-list representation (front list + reversed back list) gives amortized O(1) `pushFront`/`pushBack`/`popFront`/`popBack`, rebalancing by splitting the non-empty list when one side empties. Old versions stay valid.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Immutable Functional Deque](problem-01-functional-deque/PROBLEM.md) | Two-list persistence | Hard |
