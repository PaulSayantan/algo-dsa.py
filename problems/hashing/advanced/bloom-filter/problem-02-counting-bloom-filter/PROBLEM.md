# Counting Bloom Filter with Delete

**Difficulty:** Medium

**Source:** Classic — counting Bloom filter (deletable)

## Description

A plain Bloom filter cannot delete (clearing a bit might unset a bit shared with another item). A **counting** Bloom filter replaces each bit with a small counter: `add(x)` increments the `k` counters, `remove(x)` decrements them (only if `x` currently tests present), and `contains(x)` is true iff all `k` counters are positive. Use the same `h_s(x) = (x * 2654435761 + s * 40503) mod m`.

## Examples

### Example 1

```
Input:  add 5,7; remove 5; contains(5)
Output: False
```

**Explanation:** Decrementing 5's counters clears them.

### Example 2

```
Input:  contains(7) after removing 5
Output: True
```

**Explanation:** 7's counters are untouched (no shared bits).

## Hint

Increment on add, decrement on remove (guarded by contains), contains checks all counters > 0.
