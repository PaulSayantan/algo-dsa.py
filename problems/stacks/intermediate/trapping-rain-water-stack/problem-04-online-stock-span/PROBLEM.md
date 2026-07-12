# Online Stock Span

**Difficulty:** Medium

**Source:** LeetCode 901 — Online Stock Span

## Description

Design a class `StockSpanner` that collects daily price quotes for a stock and returns the *span* of the stock's price for the current day. The span is the maximum number of consecutive days (ending at today, going backwards) for which the price was less than or equal to today's price.

Implement:
- `StockSpanner()` — initializes the object.
- `next(price)` — records today's `price` and returns its span.

Constraints: `1 <= price <= 10^5`, at most `10^4` calls to `next`.

## Examples

### Example 1

```
Input:  next(100), next(80), next(60), next(70), next(60), next(75), next(85)
Output: 1, 1, 1, 2, 1, 4, 6
```

**Explanation:** When the price `75` arrives, the previous days `60,70,60` are all `<= 75`, giving a span of `4`.

## Hint

Keep a monotonic decreasing stack of `(price, span)` pairs; a new price swallows every entry it is greater-or-equal to, summing their spans — the same "pop the shorter bars a taller one closes off" move as trapping rain water.
