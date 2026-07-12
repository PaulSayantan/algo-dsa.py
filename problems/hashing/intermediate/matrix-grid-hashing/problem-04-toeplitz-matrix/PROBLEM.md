# Toeplitz Matrix

**Difficulty:** Easy

**Source:** LeetCode 766 — Toeplitz Matrix

## Description

A matrix is Toeplitz if every top-left-to-bottom-right diagonal has the same value. Return whether the given matrix is Toeplitz.

## Examples

### Example 1

```
Input:  [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
```

## Hint

Group cells by the key r - c; every cell on a diagonal must equal the first seen.
