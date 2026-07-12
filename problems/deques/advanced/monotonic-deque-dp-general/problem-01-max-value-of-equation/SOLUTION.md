# Max Value of Equation — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findMaxValueOfEquation(self, points, k):
        dq = deque()  # (y - x, x), decreasing by (y - x)
        best = float('-inf')
        for x, y in points:
            while dq and x - dq[0][1] > k:
                dq.popleft()
            if dq:
                best = max(best, y + x + dq[0][0])
            while dq and dq[-1][0] <= y - x:
                dq.pop()
            dq.append((y - x, x))
        return best
```
