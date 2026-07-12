# Find Duplicate Subtrees

**Difficulty:** Medium

**Source:** LeetCode 652 — Find Duplicate Subtrees

## Description

Given the `root` of a binary tree (as a LeetCode-style level-order list where `None` marks a missing child), return the **number of distinct duplicate-subtree classes** — that is, how many distinct subtree shapes (matching in both structure and node values) occur more than once. Two subtrees are duplicates iff they have the same structure and the same node values.

## Examples

### Example 1

```
Input:  root = [1,2,3,4,null,2,4,null,null,4]
Output: 2
```

**Explanation:** the leaf 4 and the subtree rooted at 2->4 each recur

## Hint

Serialize each subtree to value+','+left+','+right; count serializations occurring >= 2 times.
