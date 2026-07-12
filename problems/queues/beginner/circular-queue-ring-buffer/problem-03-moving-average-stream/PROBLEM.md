# Moving Average from Data Stream

**Difficulty:** Easy

**Source:** LeetCode 346 — Moving Average from Data Stream

## Description

Design a class `MovingAverage` that computes the moving average of the last `size` values from a stream of integers. The constructor takes the window `size`. Each call to `next(val)` pushes `val` into the stream and returns the average (as a float) of the at-most-`size` most recent values seen so far. Before the window fills, average over however many values have arrived.

Constraints: `1 <= size <= 1000`, and each `val` fits in a standard integer.

## Examples

### Example 1

```
Input:  MovingAverage(3); next(1), next(10), next(3), next(5)
Output: 1.0, 5.5, 4.666666666666667, 6.0
```

**Explanation:** The window holds at most 3 values. After `next(3)` it is `[1, 10, 3]` (avg `14/3`); `next(5)` evicts the oldest `1`, leaving `[10, 3, 5]` (avg `18/3 = 6.0`).

## Hint

Keep a fixed-size ring buffer plus a running sum: each `next` overwrites the slot at the head, subtracting the value it evicts and adding the new one, so every update is O(1).
