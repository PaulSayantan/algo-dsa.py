# First Unique Number

**Difficulty:** Medium

**Source:** LeetCode 1429 — First Unique Number

## Description

Design a data structure `FirstUnique(nums)` initialized from a stream of integers. Support `showFirstUnique()` — return the value of the first integer in insertion order that is still unique (appears exactly once), or `-1` if there is none — and `add(value)`, which appends a value to the stream. Both operations should be amortized O(1).

## Examples

### Example 1

```
Input:  FirstUnique([2,3,5]); showFirstUnique()
Output: 2
```

### Example 2

```
Input:  add(5); add(2); add(3); showFirstUnique()
Output: -1
```

## Hint

Count map + deque of candidates; showFirstUnique pops stale fronts lazily, add enqueues on first sight.
