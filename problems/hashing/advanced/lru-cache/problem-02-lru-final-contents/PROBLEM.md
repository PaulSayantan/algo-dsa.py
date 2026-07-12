# LRU Cache — Final Contents

**Difficulty:** Medium

**Source:** Classic — LRU op-sequence, final resident keys

## Description

Run a sequence of LRU operations on a cache of the given capacity, then report which keys remain resident (as a sorted list). `get(key)` still refreshes recency and returns the value or `-1`; `put` inserts and evicts the least-recently-used key on overflow. `keys_sorted()` returns the current keys in ascending order (a deterministic answer independent of internal recency order).

## Examples

### Example 1

```
Input:  cap 3; put 1,2,3; keys_sorted()
Output: [1, 2, 3]
```

**Explanation:** All three fit.

### Example 2

```
Input:  put(4) then keys_sorted()
Output: [2, 3, 4]
```

**Explanation:** 1 was least-recently-used, so it is evicted.

## Hint

Same LRU; expose the resident key set sorted so the answer is order-independent.
