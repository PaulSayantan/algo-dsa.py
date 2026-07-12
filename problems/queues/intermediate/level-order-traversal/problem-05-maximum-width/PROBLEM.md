# Maximum Width of Binary Tree

**Difficulty:** Medium

**Source:** LeetCode 662 — Maximum Width of Binary Tree

## Description

Given the `root` of a binary tree (built from a level-order list with `None` for missing children), return the maximum width of the tree. The width of a level is the number of positions between its leftmost and rightmost non-null nodes (inclusive), counting the `null` slots that would sit between them as if the tree were a complete binary tree. The answer is the largest width over all levels.

## Examples

### Example 1

```
Input:  root = [1,3,2,5,3,null,9]
Output: 4
```

**Explanation:** The bottom level occupies positions `0,1,_,3` (values `5,3,null,9`), so its width is `3 - 0 + 1 = 4`.

### Example 2

```
Input:  root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
```

**Explanation:** The bottom level's leftmost node `6` sits at position `0` and rightmost `7` at position `6`, giving width `7`.

## Hint

Run a level-order BFS carrying each node's positional index (`2*i` for the left child, `2*i+1` for the right); each level's width is `last_index - first_index + 1`.
