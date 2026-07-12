# Online Stock Span — Solution

## Optimal Approach

Maintain a monotonic decreasing stack of `(price, span)` pairs. When a new
`price` arrives, its span starts at `1`; then, while the stack's top price is
less than or equal to the new price, pop it and fold its span into the current
one. Each price is pushed once and popped at most once, so the amortized cost
per `next` call is O(1) and total work is O(n) across `n` calls.

### Reference implementation

```python
class StockSpanner:
    def __init__(self):
        self.stack = []  # (price, span), monotonically decreasing by price

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
```
