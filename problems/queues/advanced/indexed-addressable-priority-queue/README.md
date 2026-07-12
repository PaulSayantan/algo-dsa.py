# Indexed / Addressable Priority Queue

An indexed priority queue keeps a handle from each element to its heap position, enabling O(log n) `decrease-key`. It's the classic backing structure for Prim's MST and Dijkstra when you want to update a node's key in place rather than push duplicates.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Minimum Spanning Tree (Prim)](problem-01-prim-mst/PROBLEM.md) | Prim via min-heap | Medium |
