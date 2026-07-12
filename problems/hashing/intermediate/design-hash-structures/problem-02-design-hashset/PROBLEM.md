# Design HashSet

**Difficulty:** Easy

**Source:** LeetCode 705 — Design HashSet

## Description

Design a HashSet without built-in hash-table libraries. Implement `add(key)`, `contains(key)`, and `remove(key)`.

## Examples

### Example 1

```
Input:  add(1); contains(1)
Output: true
```

## Hint

Bucket array; index by key % size; store keys in the bucket list.
