# Hash Maps for Graphs & Trees

Hash maps are the glue of graph algorithms: an adjacency map represents the graph, an original→clone map deep-copies it, a visited set bounds DFS/BFS, indegree/outdegree maps drive judge/topological reasoning, and a weighted adjacency map turns division queries into path products. Returning a deterministic summary (counts, sorted edges, query results) keeps the oracle exact.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Clone Graph](problem-01-clone-graph/PROBLEM.md) | original->clone map | Medium |
| 2 | [Accounts Merge](problem-02-accounts-merge/PROBLEM.md) | Email union-find + owner map | Medium |
| 3 | [Evaluate Division](problem-03-evaluate-division/PROBLEM.md) | Weighted adjacency + DFS | Medium |
| 4 | [Number of Provinces](problem-04-number-of-provinces/PROBLEM.md) | Visited-set components | Medium |
| 5 | [Find the Town Judge](problem-05-find-the-town-judge/PROBLEM.md) | Indegree/outdegree maps | Easy |
