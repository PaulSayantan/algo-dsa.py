# Min-Max Stack

**Difficulty:** Medium

**Source:** Classic — Design a stack with O(1) `getMin` and `getMax`

## Description

Design a stack that supports `push(x)`, `pop()`, `top()`, and BOTH `getMin()`
(current minimum) and `getMax()` (current maximum), each in O(1) time. All
queries assume the stack is non-empty. Values may be negative.

## Examples

### Example 1

```
Input:  push 5,1,3; getMin; getMax; pop; getMin; getMax
Output: 1, 5, 1, 5
```

**Explanation:** After pushing `5,1,3` the min is `1` and the max is `5`;
popping `3` leaves `[5,1]`, so the min stays `1` and the max stays `5`.

## Hint

Store `(value, min-so-far, max-so-far)` triples; each query reads the top triple.
