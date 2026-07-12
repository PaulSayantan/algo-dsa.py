# Number of Recent Calls — Solution

## Optimal Approach

Every request time is stored in FIFO order. Because each `ping` uses a strictly
increasing `t`, the newest time always goes to the rear and the stale times are
always at the front. On each `ping` we enqueue `t`, then dequeue from the front
(index 0) every time that is older than `t - 3000`. What remains is exactly the
set of requests inside `[t - 3000, t]`, so its length is the answer.

### Reference implementation

```python
class RecentCounter:
    def __init__(self):
        self._times = []

    def ping(self, t):
        self._times.append(t)
        while self._times[0] < t - 3000:
            self._times.pop(0)
        return len(self._times)
```
