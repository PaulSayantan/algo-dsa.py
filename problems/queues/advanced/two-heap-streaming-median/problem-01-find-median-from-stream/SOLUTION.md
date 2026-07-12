# Find Median from Data Stream — Solution

## Optimal Approach

### Reference implementation

```python
class MedianFinder:
    def __init__(self):
        self._low = []   # max-heap (negated)
        self._high = []  # min-heap

    def addNum(self, num):
        heapq.heappush(self._low, -num)
        heapq.heappush(self._high, -heapq.heappop(self._low))
        if len(self._high) > len(self._low):
            heapq.heappush(self._low, -heapq.heappop(self._high))

    def findMedian(self):
        if len(self._low) > len(self._high):
            return float(-self._low[0])
        return (-self._low[0] + self._high[0]) / 2
```
