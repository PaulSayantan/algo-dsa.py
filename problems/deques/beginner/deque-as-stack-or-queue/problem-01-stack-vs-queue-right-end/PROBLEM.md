# Deque as Stack vs Queue (Right End)

**Difficulty:** Easy

**Source:** Classic — deque duality

## Description

Given a list of `values`, implement `asStack(values)` — append every value then pop from the **same** (right) end, returning the pop sequence (LIFO) — and `asQueue(values)` — append every value then pop from the **opposite** (left) end, returning the pop sequence (FIFO). The stack result is the reverse of the queue result.

## Examples

### Example 1

```
Input:  values = [1, 2, 3, 4]
Output: asStack -> [4, 3, 2, 1]; asQueue -> [1, 2, 3, 4]
```

## Hint

append + pop share the right end (stack); append + popleft use opposite ends (queue).
