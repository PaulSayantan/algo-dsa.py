# Gabow's SCC (Two Stacks)

Gabow's path-based algorithm finds SCCs with two stacks instead of explicit low-link numbers: one holds the current DFS path of vertices, the other the 'boundaries' of not-yet-closed components. A back edge into an open vertex collapses boundary entries; when the top boundary equals the current vertex, an SCC pops off. Linear O(V+E).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Strongly Connected Components (Gabow)](problem-01-gabow-scc/PROBLEM.md) | Path + boundary stacks | Hard |
