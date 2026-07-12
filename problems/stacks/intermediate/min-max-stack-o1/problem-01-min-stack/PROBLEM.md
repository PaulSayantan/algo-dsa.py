# Min Stack

**Difficulty:** Medium

**Source:** LeetCode 155 — Min Stack

## Description

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element `getMin`, all in O(1) time.

## Examples

### Example 1

```
Input:  push -2,0,-3; getMin; pop; top; getMin
Output: -3, 0, -2
```

## Hint

Store (value, min-so-far) pairs; getMin reads the top's second field.
