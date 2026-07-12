# Level-Order Traversal

Level-order traversal is BFS on a tree: a queue holds the current frontier, and processing exactly `len(queue)` nodes per outer iteration groups the output by depth. Zigzag variants simply reverse alternate levels.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Binary Tree Level Order Traversal](problem-01-level-order/PROBLEM.md) | Per-level BFS | Medium |
| 2 | [Binary Tree Zigzag Level Order Traversal](problem-02-zigzag-level-order/PROBLEM.md) | Alternating levels | Medium |
| 3 | [Binary Tree Right Side View](problem-03-right-side-view/PROBLEM.md) | Last node per level | Medium |
| 4 | [Find Largest Value in Each Tree Row](problem-04-largest-value-per-row/PROBLEM.md) | Per-level aggregation | Medium |
| 5 | [Maximum Width of Binary Tree](problem-05-maximum-width/PROBLEM.md) | Position-indexed BFS | Medium |
