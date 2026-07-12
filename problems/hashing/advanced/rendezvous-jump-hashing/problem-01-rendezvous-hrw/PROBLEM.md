# Rendezvous (HRW) get_node

**Difficulty:** Medium

**Source:** Classic — Thaler & Ravishankar rendezvous hashing

## Description

Implement rendezvous / Highest-Random-Weight hashing. Support `add_node(name)` and `get_node(key)`, which returns the node that maximizes a **fixed arithmetic** `hash(node, key)` score (never the salted builtin `hash()`). Break ties deterministically. Each key is independently assigned to its highest-scoring node, so the mapping is reproducible across runs and processes.

## Hint

For each node compute an arithmetic score of (node, key) and keep the argmax. Iterating nodes in sorted order makes ties deterministic.
