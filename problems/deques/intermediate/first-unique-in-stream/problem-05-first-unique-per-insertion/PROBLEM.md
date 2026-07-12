# First Unique Stream Tracker

**Difficulty:** Medium

**Source:** Classic — design a live first-unique tracker

## Description

Design a data structure `FirstUniqueStream()` that starts empty and tracks a stream of integers. Support three operations, each amortized O(1):

- `add(value)` — append `value` to the stream.
- `first()` — return the first value in insertion order that is still unique (appears exactly once so far), or `None` if none exists.
- `numUnique()` — return how many distinct values are currently unique (appear exactly once).

Maintain a count map plus a deque of candidate values in arrival order; `first()` lazily discards stale fronts, and `numUnique()` is kept as a running counter as counts cross the 1 -> 2 boundary.

## Examples

### Example 1

```
Input:  s = FirstUniqueStream(); s.add(4); s.add(7); s.first()
Output: 4
```

**Explanation:** Both `4` and `7` are unique; `4` arrived first.

### Example 2

```
Input:  s.add(4); s.first()
Output: 7
```

**Explanation:** After a second `4`, `4` is no longer unique, so the front advances to `7`.

## Hint

Count map + deque of candidates; bump a `numUnique` counter when a count hits 1 and decrement it when a count reaches 2, popping stale fronts lazily in `first()`.
