# Moving Average from Data Stream

**Difficulty:** Easy

**Source:** LeetCode 346 — Moving Average from Data Stream

## Description

Given a stream of integers and a window size, implement `MovingAverage` to calculate the moving average of all integers in the sliding window.

- `MovingAverage(size)` initializes the object with the window size `size`.
- `next(val)` appends `val` to the stream and returns the average of the last `size` values (or of all values so far if fewer than `size` have arrived).

Constraints: `1 <= size <= 1000`, and `next` is called with integer values.

## Examples

### Example 1

```
Input:
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output:
[null, 1.0, 5.5, 4.666666666666667, 6.0]
```

**Explanation:** With `size = 3`: `next(1)` averages `[1]` -> `1.0`; `next(10)` averages `[1, 10]` -> `5.5`; `next(3)` averages `[1, 10, 3]` -> `14/3`; `next(5)` drops `1`, averaging `[10, 3, 5]` -> `6.0`.

## Hint

Keep the window values in a list: enqueue `val` at the rear, and once the list exceeds `size`, dequeue the oldest from the front (index 0). The answer is `sum(window) / len(window)`.
