# Design HashMap

**Difficulty:** Easy

**Source:** LeetCode 706 — Design HashMap

## Description

Design a hash map without using any built-in hash-table library. Implement `put(key, value)` (insert or update), `get(key)` (return the value, or `-1` if the key is absent), and `remove(key)` (erase the mapping if present). Keys and values are non-negative integers.

## Examples

### Example 1

```
Input:  put(1,1); put(2,2); get(1); get(3); put(2,1); get(2); remove(2); get(2)
Output: 1, -1, 1, -1
```

## Hint

Map each integer key to a bucket via key % capacity; store [key, value] pairs and scan the bucket.
