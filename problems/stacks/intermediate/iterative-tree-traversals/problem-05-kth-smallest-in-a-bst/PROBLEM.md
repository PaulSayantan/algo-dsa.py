# Kth Smallest Element in a BST

**Difficulty:** Medium

**Source:** LeetCode 230 — Kth Smallest Element in a BST

## Description

Given the `root` of a binary search tree (built here from a level-order list with `None` for missing children) and an integer `k` (`1`-indexed), return the value of the `k`-th smallest element. It is guaranteed that `1 <= k <= n`, where `n` is the number of nodes.

Do the traversal **iteratively** with an explicit stack, and stop as soon as the `k`-th node is popped — you must not do a full recursive walk that materializes every value.

## Examples

### Example 1

```
Input:  root = [3, 1, 4, null, 2], k = 1
Output: 1
```

**Explanation:** The in-order sequence is `1, 2, 3, 4`; the 1st smallest is `1`.

### Example 2

```
Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
Output: 3
```

**Explanation:** The in-order sequence is `1, 2, 3, 4, 5, 6`; the 3rd smallest is `3`.

## Hint

Do an iterative in-order walk (push left spine, pop-visit-go-right) and return the value on the `k`-th pop.
