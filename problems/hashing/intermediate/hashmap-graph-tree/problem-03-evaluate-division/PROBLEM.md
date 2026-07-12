# Evaluate Division

**Difficulty:** Medium

**Source:** LeetCode 399 — Evaluate Division

## Description

Given equations like `a / b = 2.0`, answer queries `x / y` by multiplying edge ratios along a path in the variable graph. Return -1.0 for any query involving an unknown variable or with no path.

## Examples

### Example 1

```
Input:  a/b=2, b/c=3; query a/c
Output: 6.0
```

## Hint

Weighted adjacency map (a->b=v, b->a=1/v); DFS multiplying weights; -1.0 if unreachable.
