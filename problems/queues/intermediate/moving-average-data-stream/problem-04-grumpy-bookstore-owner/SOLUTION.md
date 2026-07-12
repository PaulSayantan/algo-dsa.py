# Grumpy Bookstore Owner — Solution

## Optimal Approach

Customers arriving during non-grumpy minutes are always satisfied, so sum them once as a fixed base. The only lever is which size-`minutes` window to make calm; the gain of a window is the customers in it during grumpy minutes. Slide a fixed-size window keeping that grumpy-minute sum as a running total (add the entering minute's grumpy customers, drop the leaving minute's) and keep the best. Answer is base + best window gain. O(n) time.

### Reference implementation

```python
class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)
        window = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        best = window
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                window += customers[i]
            if grumpy[i - minutes] == 1:
                window -= customers[i - minutes]
            if window > best:
                best = window
        return base + best
```
