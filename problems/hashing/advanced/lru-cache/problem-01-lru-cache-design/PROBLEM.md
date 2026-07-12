# LRU Cache

**Difficulty:** Medium

**Source:** LeetCode 146 — LRU Cache

## Description

Design a data structure for an LRU cache with a positive `capacity`. `get(key)` returns the value if present (and marks it most recently used) or `-1`. `put(key, value)` inserts or updates the key (marking it most recently used); if this exceeds capacity, evict the least-recently-used key. Both operations must be O(1).

## Examples

### Example 1

```
Input:  capacity 2; put(1,1),put(2,2),get(1)
Output: 1
```

**Explanation:** 1 is present and becomes most-recently-used.

### Example 2

```
Input:  put(3,3) then get(2)
Output: -1
```

**Explanation:** Inserting 3 evicts the LRU key 2.

## Hint

Hash map + doubly linked list, or an OrderedDict: touch on access, pop the oldest on overflow.
