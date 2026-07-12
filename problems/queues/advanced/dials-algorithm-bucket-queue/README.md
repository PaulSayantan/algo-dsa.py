# Dial's Algorithm (Bucket Queue)

When edge weights are small integers, Dial's algorithm replaces Dijkstra's heap with an array of buckets indexed by distance. Scanning buckets in order of increasing distance gives shortest paths in O(V + E + maxDist) — no logarithmic factor.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Shortest Path with Small Integer Weights](problem-01-dials-shortest-path/PROBLEM.md) | Distance-indexed buckets | Hard |
