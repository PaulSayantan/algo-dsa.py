# Design Hit Counter — Solution

## Optimal Approach

Hits arrive in non-decreasing time order, so their timestamps form a natural FIFO stream: the oldest hit always expires first. Store the timestamps in a queue. On `hit`, enqueue the timestamp. On `getHits`, expire stale hits by dequeuing from the front while the front timestamp is `<= timestamp - 300`; the remaining queue length is the number of hits still inside the trailing 300-second window. Every timestamp is enqueued and dequeued at most once, giving amortized O(1) per operation.

### Reference implementation

```python
class HitCounter:
    def __init__(self):
        self._q = deque()

    def hit(self, timestamp):
        self._q.append(timestamp)

    def getHits(self, timestamp):
        while self._q and self._q[0] <= timestamp - 300:
            self._q.popleft()
        return len(self._q)
```
