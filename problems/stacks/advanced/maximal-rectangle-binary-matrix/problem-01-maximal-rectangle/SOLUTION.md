# Maximal Rectangle — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        best = 0

        def largest(hs):
            stack = []
            area = 0
            for i, h in enumerate(hs + [0]):
                while stack and hs[stack[-1]] >= h:
                    top = stack.pop()
                    width = i if not stack else i - stack[-1] - 1
                    area = max(area, hs[top] * width)
                stack.append(i)
            return area

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] else 0
            best = max(best, largest(heights))
        return best
```
