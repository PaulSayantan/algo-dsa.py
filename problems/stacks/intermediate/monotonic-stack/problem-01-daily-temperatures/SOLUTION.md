# Daily Temperatures — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []  # indices, decreasing temps
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
```
