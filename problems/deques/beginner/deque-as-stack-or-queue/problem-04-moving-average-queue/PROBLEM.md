# Moving Average from Data Stream (Deque as a Queue)

**Difficulty:** Easy

**Source:** LeetCode 346 — Moving Average from Data Stream

## Description

Design a class `MovingAverage(size)` that maintains the average of the most recent
`size` values from a stream of integers. Implement `next(val)`, which records `val`
and returns the average (as a float) of the last `size` values seen so far (or of
all values if fewer than `size` have arrived).

Back it with a deque used as a **fixed-length FIFO queue**: `append` the new value
at the right end and, once the window overflows, `popleft` the oldest value from the
left end. Keep a running sum so each `next` is O(1).

## Examples

### Example 1

```
Input:  MovingAverage(3); next(1), next(10), next(3), next(5)
Output: 1.0, 5.5, 4.666666666666667, 6.0
```

**Explanation:** window holds at most 3 values. `next(5)` drops the oldest `1`, leaving `[10, 3, 5]` whose average is `18 / 3 = 6.0`.

## Hint

`append` new values at the right; when `len(dq) > size`, `popleft` the oldest and subtract it from a running sum. Divide by `len(dq)`.
