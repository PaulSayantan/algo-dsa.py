# Maximum Bipartite Matching

**Difficulty:** Hard

**Source:** Classic — Hopcroft–Karp / Kuhn's matching

## Description

Given a bipartite graph with `left` nodes `0..left-1`, `right` nodes `0..right-1`, and an edge list `[u, v]` (u on the left, v on the right), return the size of the maximum matching.

## Hint

Repeatedly BFS-layer then DFS-augment along shortest alternating paths; count matched pairs.
