# Random Node in a Binary Tree

**Difficulty:** Medium

**Source:** Classic interview problem (a tree-shaped variant of LeetCode 382, Linked List
Random Node).

## Description

Given the `root` of a binary tree, implement `get_random()` that returns the value of a
**uniformly random node** in the tree — every node must be returned with probability
`1/n`, where `n` is the total number of nodes.

The catch: you must do it in a **single traversal** and **without precomputing** the node
count `n` (imagine the tree is huge, or nodes are produced lazily by a generator). You may
use only `O(1)` extra space beyond the recursion/traversal itself.

You can assume you have some way to iterate the tree's nodes exactly once (for example a
DFS or BFS that yields each node). The order in which nodes are visited does **not** affect
correctness, as long as each node is visited exactly once.

## Constraints

- The number of nodes `n` is in the range `[1, 10^5]`.
- `-10^4 <= Node.val <= 10^4`
- The traversal visits every node exactly once; its length `n` is not known in advance.

## Examples

Consider the tree:

```
        1
       / \
      2   3
     /
    4
```

### Example 1

```
Input:  root = [1, 2, 3, 4]  (as drawn above), then call get_random() once
Output: 3        # one possible run
```

**Explanation:** The tree has `n = 4` nodes with values `{1, 2, 3, 4}`. Each is returned
with probability `1/4`. `3` is one possible outcome; another call might return `4`.

### Example 2

```
Input:  root = [42]  (single node), then call get_random()
Output: 42
```

**Explanation:** The tree has one node, so `get_random()` always returns `42`
(probability `1`).

## Hint

Traverse the tree once, treating the visited nodes as a stream. At the i-th visited node
(1-indexed) adopt its value as the answer with probability `1/i`. This is
**Reservoir Sampling** with `k = 1` — the tree shape is irrelevant, only the visitation
order matters.
