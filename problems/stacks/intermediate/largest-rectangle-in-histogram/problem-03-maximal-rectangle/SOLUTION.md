# Maximal Rectangle — Solution

## Optimal Approach

Maintain a running histogram `heights[j]` = number of consecutive `1`s ending at
column `j` in the current row (reset to 0 on a `0`). After updating the histogram
for a row, the largest all-`1`s rectangle whose bottom edge sits on that row is
exactly the largest rectangle in that histogram, which the monotonic-stack pass
computes in O(cols). Take the max over all rows. Overall O(rows * cols).

### Reference implementation

```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        best = 0
        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] else 0
            best = max(best, self._largest(heights))
        return best

    def _largest(self, heights):
        stack = []  # indices of bars in increasing height
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                best = max(best, heights[top] * width)
            stack.append(i)
        return best
```
