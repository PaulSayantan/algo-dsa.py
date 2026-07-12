# Final Prices With a Special Discount in a Shop — Solution

## Brute Force

For each `i`, scan forward for the first `j` with `prices[j] <= prices[i]` and
subtract. That is O(n^2), which is fine for `n <= 500` but the monotonic stack
below is the intended linear pattern.

## Optimal Approach

Keep a stack of indices whose discount is still unknown; the prices they hold are
strictly decreasing. When price `p` at index `i` arrives, any waiting item whose
price is `>= p` is discounted by `p` (it is the first later price that is `<=` it),
so pop and subtract. Each index is pushed and popped at most once, giving O(n).

### Reference implementation

```python
class Solution:
    def finalPrices(self, prices):
        answer = list(prices)
        stack = []  # indices with prices still awaiting a discount
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                answer[stack.pop()] -= p
            stack.append(i)
        return answer
```
