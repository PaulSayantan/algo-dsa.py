# Widest Full-Height Span — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxArea(self, heights):
        stack = []
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                best = max(best, heights[top] * width)
            stack.append(i)
        return best
```
