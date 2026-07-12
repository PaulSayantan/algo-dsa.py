# Merge k Sorted Lists — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst[0], i, 0))
        res = []
        while heap:
            val, li, ei = heapq.heappop(heap)
            res.append(val)
            if ei + 1 < len(lists[li]):
                heapq.heappush(heap, (lists[li][ei + 1], li, ei + 1))
        return res
```
