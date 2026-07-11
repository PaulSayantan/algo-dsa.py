# Online Stock Span — Solution

## Brute Force

Store every price in a list. On each `next(price)`, walk backwards counting days
while the price is `<=` today's.

```python
class BruteStockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 0
        i = len(self.prices) - 1
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1
        return span
```

- **Time:** `O(n)` per `next` call, `O(n^2)` across `n` calls.
- **Space:** `O(n)` to store all prices.

## Optimal Approach (Monotonic Stack)

Key observation: once a day is "absorbed" into the span of a later, higher-or-equal
priced day, we never need its individual price again — we only need the *total
span* it contributed. So we can collapse consecutive lower days into a single
`(price, span)` entry.

Maintain a stack of `(price, span)` pairs, kept **strictly decreasing by price**
from bottom to top. On `next(price)`:

1. Start `span = 1` (today itself).
2. While the stack is non-empty and the top price is `<= price`, pop it and add
   its stored span to `span` (those days are all `<=` today, and they were
   consecutive).
3. Push `(price, span)` and return `span`.

```python
class StockSpanner:
    def __init__(self):
        self.stack = []  # list of (price, span), strictly decreasing by price

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
```

### Why it is correct

The stack, read top to bottom, represents the sequence of "price plateaus" to the
left, each with the number of days it summarizes. Because the prices are strictly
decreasing on the stack, everything popped for today is a contiguous block of days
all `<=` today's price, and the first remaining stack entry (strictly greater than
today) is exactly the day that stops the span. Summing the absorbed spans plus
today gives the correct consecutive count. Pushing the combined `(price, span)`
preserves the invariant for future queries.

### Step-by-step on `[100, 80, 60, 70, 60, 75, 85]`

| price | pops (price,span) absorbed | span returned | stack after (bottom->top)      |
|-------|----------------------------|---------------|--------------------------------|
| 100   | —                          | 1             | [(100,1)]                      |
| 80    | —                          | 1             | [(100,1),(80,1)]               |
| 60    | —                          | 1             | [(100,1),(80,1),(60,1)]        |
| 70    | (60,1)                     | 2             | [(100,1),(80,1),(70,2)]        |
| 60    | —                          | 1             | [(100,1),(80,1),(70,2),(60,1)] |
| 75    | (60,1),(70,2)              | 4             | [(100,1),(80,1),(75,4)]        |
| 85    | (75,4),(80,1)              | 6             | [(100,1),(85,6)]               |

Returned spans: `[1, 1, 1, 2, 1, 4, 6]`.

- **Time:** amortized `O(1)` per `next`; `O(n)` total — each price is pushed once
  and popped at most once across all calls.
- **Space:** `O(n)` for the stack.

## Key Insights & Edge Cases

- The comparison is `<=` (loose), because the span counts days with price **less
  than or equal to** today's. This is the classic "previous strictly greater
  element" boundary.
- Collapsing popped entries into a single running `span` is what keeps it `O(1)`
  amortized — do not re-scan individual days.
- The very first call always returns `1`.
- Strictly increasing prices give `1, 2, 3, ...` (each call empties the stack).
- Strictly decreasing prices give all `1`s (nothing is ever absorbed).
