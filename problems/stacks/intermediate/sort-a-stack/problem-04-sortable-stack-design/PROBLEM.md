# Design a Self-Sorting Stack

**Difficulty:** Medium

**Source:** Classic — GeeksforGeeks "SortedStack" / design a stack that stays sorted

## Description

Design a `SortedStack` that always keeps its contents sorted so that the **smallest** element is on top. Support the following operations, using only an auxiliary stack for the reordering work during `push`:

- `push(x)` — insert `x`, keeping the smallest element on top.
- `pop()` — remove and return the top (the current minimum), or `None` if empty.
- `peek()` — return the top (the current minimum) without removing it, or `None` if empty.
- `isEmpty()` — return `True` if the stack has no elements, else `False`.

Each `push` pops elements smaller than `x` onto a temporary stack, places `x`, then restores them — the classic sort-a-stack insertion step, applied incrementally so the structure is sorted after every operation.

Constraints: values may be negative and may repeat; at most `10^4` operations.

## Examples

### Example 1

```
Input:
  ["SortedStack", "push", "push", "push", "peek", "push", "peek"]
  [[], [5], [2], [8], [], [1], []]
Output:
  [null, null, null, null, 2, null, 1]
```

**Explanation:** After pushing 5, 2, 8 the smallest (`2`) is on top; pushing `1` makes `1` the new top.

## Hint

On `push`, pop everything smaller than `x` onto a temp stack, push `x`, then push the temp elements back — the sort-a-stack insertion, done per operation so the top is always the minimum.
