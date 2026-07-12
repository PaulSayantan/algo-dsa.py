# LFU Cache — Final Contents

**Difficulty:** Hard

**Source:** Classic — LFU op-sequence, final resident keys

## Description

Run a sequence of LFU operations on a cache of the given capacity and report which keys remain resident (as a sorted list). Semantics match LeetCode 460: `get` bumps frequency and returns the value or `-1`; `put` evicts the least-frequently-used key (LRU among ties) on overflow. `keys_sorted()` returns the resident keys in ascending order.

## Examples

### Example 1

```
Input:  cap 2; put 1,2; get(1); put(3)
Output: [1, 3]
```

**Explanation:** 2 (freq 1) is evicted; 1 has freq 2.

### Example 2

```
Input:  get(3); put(4)
Output: [3, 4]
```

**Explanation:** 1 and 3 tie at freq 2; 1 is older, so 1 is evicted.

## Hint

Same LFU; expose the resident key set sorted so the answer is order-independent.
