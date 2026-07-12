# Count Distinct Subtrees

**Difficulty:** Medium

**Source:** Classic — subtree serialization

## Description

Given a binary tree as a level-order list, serialize the structure of every subtree and return the number of **distinct** subtree serializations (each null subtree is represented by a sentinel and is not counted as a subtree).

## Examples

### Example 1

```
Input:  root = [1,2,3]
Output: 3
```

**Explanation:** subtrees: '2', '3', and the whole tree

## Hint

Collect every subtree's serialization in a set; the answer is the set size.
