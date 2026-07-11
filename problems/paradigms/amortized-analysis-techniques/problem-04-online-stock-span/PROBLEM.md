# Online Stock Span

**Difficulty:** Medium

**Source:** LeetCode 901 — Online Stock Span

## Description

Design an algorithm that collects daily price quotes for some stock and returns the
**span** of that stock's price for the current day.

The **span** of the stock's price on the current day is defined as the maximum number
of consecutive days (starting from the current day and going backward) for which the
price of the stock was **less than or equal to** the price of the current day.

Concretely, the span counts today plus all immediately-preceding consecutive days whose
price is ≤ today's price, stopping at the first earlier day with a strictly larger price.
For example, if the prices seen so far (in order) are `[7, 34, 1, 2]` and today's price
is `8`, the span is `3` — the qualifying days are `[1, 2, 8]`, because the `34` two days
earlier is greater than `8` and stops the backward run.

Implement the `StockSpanner` class:

- `StockSpanner()` — Initializes the object of the class.
- `int next(int price)` — Returns the span of the stock's price given that today's
  price is `price`.

## Constraints

- `1 <= price <= 10^5`
- At most `10^4` calls will be made to `next`.

## Examples

### Example 1

```
Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output:
[null, 1, 1, 1, 2, 1, 4, 6]
```

Explanation:
```
StockSpanner ss = new StockSpanner();
ss.next(100);  // span 1: [100]
ss.next(80);   // span 1: 80 < 100, only today qualifies
ss.next(60);   // span 1: 60 < 80
ss.next(70);   // span 2: [60, 70]  (60 <= 70, then 80 > 70 stops)
ss.next(60);   // span 1: 60 < 70
ss.next(75);   // span 4: [60, 70, 60, 75]  (80 > 75 stops)
ss.next(85);   // span 6: [80, 60, 70, 60, 75, 85]  (100 > 85 stops)
```

### Example 2

```
Input:
["StockSpanner", "next", "next", "next"]
[[], [31], [41], [48]]

Output:
[null, 1, 2, 3]
```

Explanation: Prices are non-decreasing (`31 <= 41 <= 48`), so each new day extends the
run all the way back: spans are `1`, `2`, `3`.

## Hint

Use **Amortized Analysis Techniques** with a **monotonic decreasing stack** of
`(price, span)` pairs. When a new price is at least as large as the top of the stack,
pop it and absorb its accumulated span. Each daily entry is pushed once and popped once
over the object's lifetime, so `next` is O(1) amortized despite an occasional long pop
chain.
