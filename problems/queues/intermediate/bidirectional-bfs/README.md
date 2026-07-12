# Bidirectional BFS

Bidirectional BFS runs two searches at once — forward from the start and backward from the goal — expanding the smaller frontier each step and stopping when they meet. This roughly square-roots the number of states explored versus one-directional BFS.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Minimum Genetic Mutation](problem-01-minimum-genetic-mutation/PROBLEM.md) | Two-frontier meet | Medium |
| 2 | [Jump Game IV](problem-02-jump-game-iv/PROBLEM.md) | Meet in the middle on an index graph | Medium |
| 3 | [Open the Lock](problem-03-open-the-lock/PROBLEM.md) | Meet-in-the-middle with deadends | Medium |
| 4 | [Minimum Knight Moves](problem-04-minimum-knight-moves/PROBLEM.md) | Two-frontier on infinite board | Medium |
| 5 | [Sliding Puzzle](problem-05-sliding-puzzle/PROBLEM.md) | Bidirectional state-space search | Medium |
