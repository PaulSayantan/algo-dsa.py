# Moving Average from Data Stream

**Difficulty:** Easy

**Source:** LeetCode 346 — Moving Average from Data Stream

## Description

Design a class `MovingAverage(size)` that, given a window `size`, supports `next(val)`: append `val` to the stream and return the average of the last `size` values (or of all values so far if fewer than `size` have arrived).

## Examples

### Example 1

```
Input:  size=3; next 1,10,3,5
Output: 1.0, 5.5, 4.667, 6.0
```

## Hint

Keep a fixed-size queue and a running sum; pop the oldest when the window overflows.
