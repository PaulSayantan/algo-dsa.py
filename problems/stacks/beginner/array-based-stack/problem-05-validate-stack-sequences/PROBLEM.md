# Validate Stack Sequences

**Difficulty:** Easy

**Source:** LeetCode 946 — Validate Stack Sequences

## Description

Given two integer arrays `pushed` and `popped`, each a permutation of the same distinct values, return `True` if and only if this could have been the result of a sequence of `push` and `pop` operations on an initially empty array-based stack. Elements must be pushed in exactly the order given by `pushed`, and popped elements must come off in the order given by `popped`.

Drive a real array-backed stack (`push`/`pop`/`peek`/`isEmpty`): push values in order and, whenever the top equals the next value owed by `popped`, pop it.

## Examples

### Example 1

```
Input:  pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
```

**Explanation:** push 1,2,3,4 then pop 4, push 5 then pop 5, then pop 3, pop 2, pop 1 — the stack empties exactly.

### Example 2

```
Input:  pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
```

**Explanation:** After popping 4 the top is 3, but 5 has not been pushed yet, so 3 cannot be followed by 5 and then 1 — no valid push/pop order reproduces this.

## Hint

Push each value in order; after every push, while the stack top equals the next `popped` value, pop it and advance. The sequence is valid exactly when the stack is empty at the end.
