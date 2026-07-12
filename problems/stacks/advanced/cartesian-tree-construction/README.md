# Cartesian Tree Construction (O(n))

A Cartesian tree is a binary tree that is a min-heap by value and a BST by array index. Building it left to right with a monotonic stack takes O(n): pop nodes larger than the incoming value, attach the last popped as its left child, and hang it off the new stack top. It is the bridge between RMQ and LCA.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Build a Cartesian Tree (Parent Array)](problem-01-build-cartesian-tree/PROBLEM.md) | Monotonic-stack tree build | Hard |
