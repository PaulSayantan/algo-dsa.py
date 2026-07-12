# Binary Tree Level Order Traversal

**Difficulty:** Medium

**Source:** LeetCode 102 — Binary Tree Level Order Traversal

## Description

Given the `root` of a binary tree (built from a level-order list with `None` for missing children), return its level-order traversal: a list of levels, each a list of node values from left to right.

## Examples

### Example 1

```
Input:  root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

## Hint

Process the queue one full level at a time using its current length.
