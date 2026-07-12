# Binary Tree Right Side View

**Difficulty:** Medium

**Source:** LeetCode 199 — Binary Tree Right Side View

## Description

Given the `root` of a binary tree (built from a level-order list with `None` for missing children), imagine standing on the right side of the tree. Return the values of the nodes you can see, ordered from top to bottom — i.e. the last node of each level.

## Examples

### Example 1

```
Input:  root = [1,2,3,null,5,null,4]
Output: [1, 3, 4]
```

**Explanation:** From the right you see `1` (level 0), `3` (level 1), then `4` (the rightmost node on level 2).

### Example 2

```
Input:  root = [1,null,3]
Output: [1, 3]
```

**Explanation:** Each level has a single visible node.

## Hint

Do a level-order BFS and keep the last value dequeued on each level.
