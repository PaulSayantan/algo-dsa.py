# Find Largest Value in Each Tree Row

**Difficulty:** Medium

**Source:** LeetCode 515 — Find Largest Value in Each Tree Row

## Description

Given the `root` of a binary tree (built from a level-order list with `None` for missing children), return a list containing the largest value in each row (level) of the tree, ordered from the top row to the bottom.

## Examples

### Example 1

```
Input:  root = [1,3,2,5,3,null,9]
Output: [1, 3, 9]
```

**Explanation:** Level 0 is `[1]`, level 1 is `[3,2]` (max `3`), level 2 is `[5,3,9]` (max `9`).

### Example 2

```
Input:  root = [1,2,3]
Output: [1, 3]
```

**Explanation:** Level 0 max is `1`; level 1 `[2,3]` max is `3`.

## Hint

Run a level-order BFS and track the maximum value seen while draining each level.
