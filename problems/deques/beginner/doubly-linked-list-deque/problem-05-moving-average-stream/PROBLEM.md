# Moving Average from Data Stream

**Difficulty:** Easy

**Source:** LeetCode 346 — Moving Average from Data Stream

## Description

Design a class `MovingAverage` initialized with a window `size`. Implement `next(val)`, which appends `val` to the stream and returns the average of the **last `size` values** (or of all values seen so far, if fewer than `size` have arrived).

Maintain a running `sum` so each `next` is O(1): append the new value at the back, and once the window overflows, drop the value at the front.

## Examples

### Example 1

```
Input:
  ["MovingAverage", "next", "next", "next", "next"]
  [[3], [1], [10], [3], [5]]
Output:
  [null, 1.0, 5.5, 4.666666666666667, 6.0]
```

**Explanation:** With `size = 3`: `next(1)` averages `[1]` → 1.0; `next(10)` averages `[1,10]` → 5.5; `next(3)` averages `[1,10,3]` → 4.6667; `next(5)` drops the oldest `1`, averaging `[10,3,5]` → 6.0.

## Hint

Keep the window in a doubly-linked-list deque: `pushBack` the new value, and when the deque exceeds `size`, `popFront` the oldest — adjust a running sum on each push/pop so the average is `sum / len` in O(1).
