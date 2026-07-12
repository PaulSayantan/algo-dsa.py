# Online Stock Span

**Difficulty:** Medium

**Source:** LeetCode 901 — Online Stock Span

## Description

Design a `StockSpanner` that collects daily price quotes and, for each `next(price)`, returns the *span*: the number of consecutive days (ending today, going backward) whose price was ≤ today's price.

## Examples

### Example 1

```
Input:  next: 100,80,60,70,60,75,85
Output: 1,1,1,2,1,4,6
```

## Hint

Monotonic decreasing stack of (price, span); merge spans of popped smaller prices.
