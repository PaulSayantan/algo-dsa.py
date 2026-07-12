# Insert an Element into a Sorted Stack

**Difficulty:** Medium

**Source:** Classic — sorted insert (the core step of sort-a-stack)

## Description

You are given an **already sorted** stack (a list where the **last** element is the top, sorted non-decreasing from bottom to top) and an integer `x`. Insert `x` so the stack stays sorted, using only stack operations (pop/push) and recursion — no other data structure. Implement `sortedInsert(stack, x)` and return the resulting list (bottom to top).

This is the fundamental building block of recursive stack sorting: pop elements larger than `x` off the top, push `x`, then push the popped elements back.

Constraints: `0 <= len(stack) <= 1000`; the input stack is guaranteed sorted; values may repeat.

## Examples

### Example 1

```
Input:  stack = [1, 3, 5], x = 4
Output: [1, 3, 4, 5]
```

**Explanation:** `5` is larger than `4`, so it is lifted off, `4` is placed, then `5` goes back on top.

### Example 2

```
Input:  stack = [1, 3, 5], x = 6
Output: [1, 3, 5, 6]
```

**Explanation:** `6` is at least the current top, so it is simply pushed.

## Hint

While the top is greater than `x`, pop it aside (recursively), push `x`, then push the held elements back — exactly the inner step of sort-a-stack.
