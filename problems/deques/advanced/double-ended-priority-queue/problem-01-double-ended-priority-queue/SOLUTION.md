# Double-Ended Priority Queue — Solution

## Optimal Approach

### Reference implementation

```python
class DEPQ:
    def __init__(self):
        self._min = []  # (value, id)
        self._max = []  # (-value, id)
        self._alive = {}
        self._next_id = 0

    def push(self, x):
        i = self._next_id
        self._next_id += 1
        self._alive[i] = True
        heapq.heappush(self._min, (x, i))
        heapq.heappush(self._max, (-x, i))

    def _clean(self, heap):
        while heap and not self._alive.get(heap[0][1]):
            heapq.heappop(heap)

    def popMin(self):
        self._clean(self._min)
        x, i = heapq.heappop(self._min)
        self._alive[i] = False
        return x

    def popMax(self):
        self._clean(self._max)
        nx, i = heapq.heappop(self._max)
        self._alive[i] = False
        return -nx
```
