# Snapshot Array

**Difficulty:** Medium

**Source:** LeetCode 1146 — Snapshot Array

## Description

Implement an array of `length` with `set(index, val)`, `snap()` (returns the snapshot id, incrementing a counter), and `get(index, snap_id)` returning the value at that index at the time the given snapshot was taken. Unset entries are 0.

## Examples

### Example 1

```
Input:  set(0,5); snap()->0; set(0,6); get(0,0)
Output: 5
```

## Hint

Per index keep (snap_id, val) history; get binary-searches the largest snap <= snap_id.
