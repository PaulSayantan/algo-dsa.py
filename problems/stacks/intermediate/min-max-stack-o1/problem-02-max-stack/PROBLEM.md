# Max Stack

**Difficulty:** Hard

**Source:** LeetCode 716 — Max Stack (simplified)

## Description

Design a stack that supports `push(x)`, `pop()` (remove & return top), `top()`, `peekMax()` (return the maximum element), and `popMax()` (remove & return the maximum). For simplicity, when several elements share the maximum, `popMax` removes the one closest to the top.

## Examples

### Example 1

```
Input:  push 5,1,5; top; popMax; top; peekMax; pop; top
Output: 5,5,1,5,1,5
```

## Hint

A simple correct version keeps a plain list; peekMax = max(list), popMax removes the topmost max.
