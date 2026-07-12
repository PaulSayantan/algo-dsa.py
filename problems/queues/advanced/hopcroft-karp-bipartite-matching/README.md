# Hopcroft–Karp (Bipartite Matching)

Hopcroft–Karp finds a maximum bipartite matching in O(E·√V) by alternating phases: a BFS layers the graph by augmenting-path distance, then DFS finds a maximal set of vertex-disjoint shortest augmenting paths at once. The matching size is unique.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Maximum Bipartite Matching](problem-01-maximum-bipartite-matching/PROBLEM.md) | BFS-layer + DFS-augment | Hard |
