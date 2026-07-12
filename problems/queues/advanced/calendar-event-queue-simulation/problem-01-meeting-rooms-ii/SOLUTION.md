# Meeting Rooms II — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort()
        heap = []  # end times
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)
```
