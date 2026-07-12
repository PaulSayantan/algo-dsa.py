# Largest Rectangle in Histogram — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # indices, increasing heights
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                top = stack.pop()
                height = heights[top]
                width = i if not stack else i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)
        return best
```
