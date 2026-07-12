# Persistent Deque

A fully persistent deque keeps every version queryable and mutable. Modeling each version's contents immutably (sharing an underlying tuple) lets you branch history: push onto an old version to create a new one without disturbing others — the deque analogue of Library Checker's persistent_queue.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Fully-Persistent Deque](problem-01-persistent-deque/PROBLEM.md) | Branching version history | Hard |
