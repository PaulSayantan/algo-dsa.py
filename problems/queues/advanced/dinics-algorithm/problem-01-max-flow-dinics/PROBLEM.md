# Maximum Flow (Dinic's)

**Difficulty:** Hard

**Source:** Classic — Dinic's max-flow (cf. SPOJ FASTFLOW)

## Description

Given `n` nodes, directed capacity edges `[u, v, cap]`, a source `s`, and a sink `t`, return the maximum flow from `s` to `t` using Dinic's level-graph + blocking-flow method.

## Hint

Repeat: BFS to assign levels; DFS blocking flow along edges that go to the next level. Sum the pushes.
