# Is a Permutation Stack-Sortable?

**Difficulty:** Medium

**Source:** Classic — Knuth's stack-sortable permutations

## Description

Given a permutation `perm` of `1..n`, determine whether it can be sorted to `1, 2, ..., n` using one auxiliary stack: you may push the next input element or pop the stack top to the output at any time. Return `True` if a valid sequence of pushes/pops produces sorted output, else `False`.

## Examples

### Example 1

```
Input:  perm = [2,3,1]
Output: false
```

**Explanation:** 231 pattern present.

## Hint

Simulate: push each element, and pop to output while the top equals the next value you still owe.
