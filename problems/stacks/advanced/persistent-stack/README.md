# Persistent Stack

A persistent (immutable) stack never mutates: every push or pop returns a new version that structurally shares the untouched tail with the old one. Because a stack is just a singly linked list from the head, each operation is O(1) yet all past versions remain queryable — the essence of functional data structures.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Versioned Persistent Stack](problem-01-persistent-stack/PROBLEM.md) | Structural sharing | Hard |
