# Sort a Stack Using Recursion

**Difficulty:** Medium

**Source:** Classic — sort a stack using recursion

## Description

You are given a stack represented as a list, where the **last** element is the top. Sort it in ascending order (largest element on top, i.e. non-decreasing from bottom to top) **using recursion only** — no explicit auxiliary stack or other container is allowed; the call stack itself is your temporary storage. Implement `sortStack(stack)` and return the sorted list (bottom to top).

The idea: recursively pop the whole stack, then insert each popped value back into the now-sorted stack at its correct position (a recursive `sortedInsert`).

Constraints: `0 <= len(stack) <= 1000`, values may be negative and may repeat.

## Examples

### Example 1

```
Input:  stack = [34, 3, 31, 98, 92, 23]
Output: [3, 23, 31, 34, 92, 98]
```

**Explanation:** Sorted bottom-to-top, so the largest value (`98`) sits on top.

### Example 2

```
Input:  stack = [-2, -5, -1, 0]
Output: [-5, -2, -1, 0]
```

**Explanation:** Negatives sort just like any other integers.

## Hint

Pop everything via recursion, then use a recursive `sortedInsert` to drop each value back into place — the call stack replaces the auxiliary stack.
