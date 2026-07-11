# Online Stock Span

**Difficulty:** Medium

**Source:** LeetCode 901 — Online Stock Span

## Description

Design an algorithm that collects daily price quotes for a stock and returns the
**span** of the stock's price for the current day.

The **span** of the stock's price on a given day is defined as the maximum number
of consecutive days (starting from that day and going **backwards**) for which
the price of the stock was **less than or equal to** the price on that day.

- For example, if the prices of the stock over the next 7 days are
  `[100, 80, 60, 70, 60, 75, 85]`, then the stock spans are
  `[1, 1, 1, 2, 1, 4, 6]`.

Implement the `StockSpanner` class:

- `StockSpanner()` initializes the object of the class.
- `int next(int price)` returns the span of the stock's price given that today's
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

**Explanation:**
- `next(100)` -> 1 (only today qualifies).
- `next(80)`  -> 1 (80 < 100, so just today).
- `next(60)`  -> 1.
- `next(70)`  -> 2 (today 70, and yesterday's 60 <= 70).
- `next(60)`  -> 1.
- `next(75)`  -> 4 (75 >= 60, 70, 60 going back, plus today = 4 days).
- `next(85)`  -> 6 (85 >= 75, 60, 70, 60, 80 going back, plus today = 6 days).

### Example 2

```
Input:
["StockSpanner", "next", "next", "next", "next"]
[[], [31], [41], [48], [59]]

Output:
[null, 1, 2, 3, 4]
```

**Explanation:** Prices are strictly increasing, so each new day's span extends
over all previous days plus itself: `1, 2, 3, 4`.

## Hint

Maintain a **Monotonic Stack** of `(price, span)` pairs kept strictly decreasing
by price. When a new price arrives, pop and absorb the spans of all earlier days
whose price is `<=` today's, giving an amortized `O(1)` answer per call.
