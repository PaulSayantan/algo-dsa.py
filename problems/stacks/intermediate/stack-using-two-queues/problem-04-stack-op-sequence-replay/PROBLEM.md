# Replay Stack Operations Using a Queue

**Difficulty:** Medium

**Source:** Classic — simulate a stack with a queue

## Description

You are given a list of operations `ops` to run against a stack that must be
implemented using only queue operations. Each operation is a tuple:

- `("push", x)` — push integer `x`
- `("pop",)` — remove the top and record it
- `("top",)` — record the current top (without removing)
- `("empty",)` — record whether the stack is currently empty (`True`/`False`)

Return the list of recorded results, in order, for every `pop`, `top`, and
`empty` operation. `push` produces no output. Assume `pop`/`top` are only
issued when the stack is non-empty.

## Examples

### Example 1

```
Input:  [("push",1),("push",2),("top",),("pop",),("top",),("empty",),("pop",),("empty",)]
Output: [2, 2, 1, False, 1, True]
```

**Explanation:** After pushing 1,2 the top is 2; pop removes 2; top is now 1;
not empty; pop removes 1; now empty.

## Hint

Back the stack with one queue and rotate on push so the front is always the
top; then dispatch on each op tuple, appending outputs for `pop`/`top`/`empty`.
