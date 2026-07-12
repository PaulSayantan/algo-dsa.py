# Binary Search Tree Iterator

**Difficulty:** Medium

**Source:** LeetCode 173 — Binary Search Tree Iterator

## Description

Design an iterator over the **in-order** traversal of a binary search tree (built here from a level-order list with `None` for missing children). Implement:

- `BSTIterator(root)` — initialize with the tree's `root`; the pointer starts before the smallest element.
- `next()` — move the pointer to the next-smallest value and return it.
- `hasNext()` — return `True` if a next-smallest value exists, else `False`.

Do **not** flatten the tree into a list up front. Use an explicit stack holding the current left spine so `next()` runs in amortized `O(1)` and the iterator uses only `O(h)` space (`h` = tree height).

## Examples

### Example 1

```
Input:
  ["BSTIterator", "next", "next", "hasNext", "next", "next", "hasNext", "next", "hasNext"]
  [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], []]
Output:
  [null, 3, 7, true, 9, 15, true, 20, false]
```

**Explanation:** The in-order sequence of the tree is `3, 7, 9, 15, 20`; the iterator yields those values one at a time and reports `hasNext()` as `False` only after the last one.

## Hint

Keep an explicit stack of the current node's left spine; on `next()`, pop a node and, if it has a right child, push that child's left spine.
