# Daily Temperatures — Solution

## Optimal Approach

Walk left to right keeping a stack of indices whose warmer day is still unknown.
The stack stays decreasing in temperature. When day `i` is warmer than the day on
top of the stack, that top day's answer is `i - top`; pop and repeat. Each index is
pushed and popped once, so the whole scan is O(n).

### Reference implementation

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices with strictly decreasing temperatures
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer
```
