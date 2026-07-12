# Moving Average from Data Stream

**Difficulty:** Easy

**Source:** LeetCode 346 — Moving Average from Data Stream

## Description

Given a stream of integers and a fixed window `size`, design a class that returns the moving average of the last `size` values seen so far. Implement:

- `MovingAverage(size)` — initialize with the window `size`.
- `next(val)` — append `val` to the stream and return the average (a float) of the most recent `size` values (or of all values seen so far, if fewer than `size` have arrived).

Each `next` call must run in O(1) time and O(size) space — do not rescan the whole stream.

## Examples

### Example 1

```
Input:  MovingAverage(3); next(1); next(10); next(3); next(5)
Output: [1.0, 5.5, 4.666666666666667, 6.0]
```

**Explanation:** After `next(5)` the window holds the last 3 values `[10, 3, 5]`, whose average is `18 / 3 = 6.0`; the oldest value `1` has been evicted.

## Hint

Keep a fixed-capacity ring buffer of the last `size` values plus a running sum and a head index. When the buffer is full, subtract the value being overwritten before adding the new one, then advance the head with `% size`.
