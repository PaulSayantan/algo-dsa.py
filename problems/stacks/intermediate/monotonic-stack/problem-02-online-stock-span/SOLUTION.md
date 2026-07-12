# Online Stock Span — Solution

## Optimal Approach

### Reference implementation

```python
class StockSpanner:
    def __init__(self):
        self._stack = []  # (price, span)

    def next(self, price):
        span = 1
        while self._stack and self._stack[-1][0] <= price:
            span += self._stack.pop()[1]
        self._stack.append((price, span))
        return span
```
