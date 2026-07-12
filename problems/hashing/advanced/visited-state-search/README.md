# Visited-State Hashing (BFS/DFS State-Space)

Many shortest-path puzzles are really **BFS over an implicit state graph**: each configuration is a node and each legal move an edge. The enabling trick is to *serialize every state into a hashable key* (a string or tuple) and keep a **visited set** so each configuration is expanded at most once — without it the search re-explores states exponentially. Since BFS explores in order of distance, the first time you reach the goal gives the minimum number of moves. The path itself may not be unique, but that scalar length is, so we always return the length (deterministic), never a path.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Sliding Puzzle](problem-01-sliding-puzzle/PROBLEM.md) | BFS over board strings | Hard |
| 2 | [Open the Lock](problem-02-open-the-lock/PROBLEM.md) | BFS over lock states | Medium |
| 3 | [Word Ladder](problem-03-word-ladder/PROBLEM.md) | BFS over word states | Hard |
