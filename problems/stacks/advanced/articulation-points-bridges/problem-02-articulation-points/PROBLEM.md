# Articulation Points

**Difficulty:** Hard

**Source:** Classic — cut vertices

## Description

Given an undirected graph as `n` and an edge list `edges`, return the sorted list of articulation points (vertices whose removal increases the number of connected components).

## Hint

Root is an articulation point iff it has >1 DFS child; non-root u iff some child v has low[v] >= disc[u].
