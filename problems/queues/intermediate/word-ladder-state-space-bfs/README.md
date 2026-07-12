# Word Ladder / State-Space BFS

BFS isn't limited to explicit graphs — it explores any *state space* where states connect by a legal move. In Word Ladder, states are words and edges are single-letter changes; BFS finds the fewest transformations. The queue holds states; a visited set prevents revisits.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Word Ladder](problem-01-word-ladder/PROBLEM.md) | State-space BFS | Hard |
| 2 | [Open the Lock](problem-02-open-the-lock/PROBLEM.md) | BFS over 4-digit lock states | Medium |
| 3 | [Minimum Genetic Mutation](problem-03-minimum-genetic-mutation/PROBLEM.md) | BFS over gene strings (ACGT) | Medium |
| 4 | [Snakes and Ladders](problem-04-snakes-and-ladders/PROBLEM.md) | BFS over board squares | Medium |
| 5 | [Perfect Squares (BFS)](problem-05-perfect-squares-bfs/PROBLEM.md) | BFS over remaining amounts | Medium |
