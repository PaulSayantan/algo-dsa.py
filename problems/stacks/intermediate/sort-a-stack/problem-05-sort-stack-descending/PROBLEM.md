# Sort a Stack in Descending Order

**Difficulty:** Medium

**Source:** Classic — sort a stack (descending variant)

## Description

You are given a stack represented as a list, where the **last** element is the top. Sort it in **descending** order so that the **smallest** element ends up on top (non-increasing from bottom to top), using only stack operations and **one** auxiliary stack. Implement `sortStackDesc(stack)` and return the resulting list (bottom to top).

This is the mirror image of the ascending sort: instead of moving *larger* temp elements back, you move *smaller* ones back before pushing the current value.

Constraints: `0 <= len(stack) <= 1000`; values may be negative and may repeat.

## Examples

### Example 1

```
Input:  stack = [34, 3, 31, 98, 92, 23]
Output: [98, 92, 34, 31, 23, 3]
```

**Explanation:** Sorted bottom-to-top in descending order, so the smallest value (`3`) sits on top.

### Example 2

```
Input:  stack = [7, 7, 3]
Output: [7, 7, 3]
```

**Explanation:** Duplicates are kept; the smallest (`3`) ends on top.

## Hint

Same one-aux-stack insertion sort as the ascending version, but flip the comparison: before pushing the current value, move temp's *smaller* elements back to the input.
