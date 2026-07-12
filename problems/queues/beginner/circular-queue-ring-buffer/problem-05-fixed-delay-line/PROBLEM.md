# Fixed-Delay Line

**Difficulty:** Easy

**Source:** Classic — ring-buffer delay line

## Description

A **delay line** streams values through with a fixed lag. Implement a class `DelayLine` whose constructor takes a positive integer `delay` (and an optional `fill` value, default `0`). Each call to `push(x)` feeds the new value `x` into the line and returns the value that was pushed `delay` steps earlier; for the first `delay` pushes — before any real value has aged out — it returns `fill`.

Back the line with a **fixed-size array of length `delay`** and a single `head` index that wraps modulo `delay`. On each `push`, the slot at `head` holds the value from exactly `delay` steps ago: read it out, overwrite that slot with `x`, then advance `head = (head + 1) % delay`. No allocation or shifting happens after construction, so every `push` is O(1).

Constraints: `1 <= delay`. Values are integers.

## Examples

### Example 1

```
Input:  DelayLine(3); push(10), push(20), push(30), push(40), push(50)
Output: 0, 0, 0, 10, 20
```

**Explanation:** With `delay = 3` the first three pushes have nothing aged out yet, so they return the `fill` value `0`. The fourth push returns `10` (pushed 3 steps earlier) and the fifth returns `20`.

### Example 2

```
Input:  DelayLine(1); push(7), push(8), push(9)
Output: 0, 7, 8
```

**Explanation:** A `delay` of 1 lags each value by exactly one step: `push(7)` returns the initial `fill` `0`, `push(8)` returns `7`, and `push(9)` returns `8`.

## Hint

The buffer is exactly `delay` slots long, so the slot currently at `head` is always the value from `delay` pushes ago. Return that slot, overwrite it with the new value, then advance `head` with modulo — the array behaves as a circular queue of in-flight values.
