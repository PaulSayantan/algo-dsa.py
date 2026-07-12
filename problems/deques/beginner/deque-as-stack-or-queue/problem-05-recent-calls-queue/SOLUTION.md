# Number of Recent Calls (Deque as a Queue) — Solution

## Optimal Approach

Because request times arrive in strictly increasing order, once a time drops out of
the `[t - 3000, t]` window it never returns — so a FIFO queue on a deque is ideal.
`append` the new time at the right end, then `popleft` stale times (`< t - 3000`)
from the left end. Each time is enqueued and dequeued at most once, so the amortized
cost per `ping` is O(1); the answer is simply `len(dq)`.

### Reference implementation

```python
class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)                 # enqueue newest at the right end
        while self.q[0] < t - 3000:      # evict stale times from the left end
            self.q.popleft()
        return len(self.q)
```
