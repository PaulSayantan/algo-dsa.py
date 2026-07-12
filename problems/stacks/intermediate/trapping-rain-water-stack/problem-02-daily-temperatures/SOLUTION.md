# Daily Temperatures — Solution

## Optimal Approach

Maintain a decreasing stack of indices. When the current temperature is warmer
than the temperature at the stack's top, that top day has found its answer: pop
it and record `i - j` (the day gap). Each index is pushed and popped once, so
the pass is O(n) time and O(n) space.

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
