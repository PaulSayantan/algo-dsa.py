# Design HashMap

**Difficulty:** Easy

**Source:** LeetCode 706 — Design HashMap

## Description

Design a HashMap without using built-in hash-table libraries. Implement `put(key, value)`, `get(key)` (return -1 if absent), and `remove(key)`.

## Examples

### Example 1

```
Input:  put(1,1); get(1)
Output: 1
```

## Hint

Bucket array sized to a prime; index by key % size; chain collisions in a list.
