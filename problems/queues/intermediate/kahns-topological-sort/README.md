# Kahn's Algorithm (Topological Sort)

Kahn's algorithm topologically orders a DAG with a queue of in-degree-0 nodes: repeatedly dequeue such a node, append it to the order, and decrement its neighbors' in-degrees, enqueuing any that reach zero. If fewer than `n` nodes are emitted, the graph has a cycle.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Course Schedule](problem-01-course-schedule/PROBLEM.md) | In-degree queue | Medium |
| 2 | [Course Schedule II (Lexicographically Smallest Order)](problem-02-course-schedule-ii-lexicographic/PROBLEM.md) | Lex-smallest topo order | Medium |
| 3 | [Sequence Reconstruction](problem-03-sequence-reconstruction/PROBLEM.md) | Unique topo order | Medium |
| 4 | [Parallel Courses](problem-04-parallel-courses/PROBLEM.md) | Level-by-level Kahn BFS | Medium |
| 5 | [Course Schedule IV](problem-05-course-schedule-iv/PROBLEM.md) | Ancestor-set propagation | Medium |
