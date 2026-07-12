# Moving Average from Data Stream

**Difficulty:** Easy

**Source:** LeetCode 346 — Moving Average from Data Stream

## Description

Given a stream of integers and a fixed window `size`, compute the moving average of all integers in the sliding window.

Implement `MovingAverage`:

- `MovingAverage(size)` initializes the object with the window `size`.
- `next(val)` appends `val` to the stream and returns the average of the last `size` values (or of all values seen so far if fewer than `size` have arrived).

Back the window with a singly linked list queue and keep a running sum: `enqueue` each new value at the tail and add it to the sum; once the queue holds more than `size` values, `dequeue` the head and subtract it. The average is `sum / current_count`.

## Examples

### Example 1

```
Input:
  ["MovingAverage", "next", "next", "next", "next"]
  [[3], [1], [10], [3], [5]]
Output:
  [null, 1.0, 5.5, 4.666666666666667, 6.0]
```

**Explanation:** With window size `3`: `next(3)` fills the window to `[1, 10, 3]` averaging `14/3`; `next(5)` evicts the head `1` from the queue, leaving `[10, 3, 5]` averaging `18/3 = 6.0`.

## Hint

Enqueue each value at the tail with a running sum; when the queue exceeds `size`, dequeue the head and subtract it, then divide the sum by the queue size.
