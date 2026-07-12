# Design Hit Counter — Solution

## Optimal Approach

Maintain two fixed circular arrays of length 300: `times[i]` holds the timestamp
last written to bucket `i`, and `counts[i]` holds how many hits landed on that
exact second. A hit at time `t` maps to bucket `t % 300`. If that bucket already
records second `t`, increment its count; otherwise it holds a stale (older, now
irrelevant) second, so overwrite the timestamp and reset the count to 1 — this is
the ring-buffer recycle that keeps space bounded at 300. `getHits(t)` sums the
counts of every bucket whose stored timestamp is still inside the window
`(t - 300, t]`, i.e. `times[i] > t - 300`.

### Reference implementation

```python
class MyHitCounter:
    def __init__(self):
        self._n = 300
        self._times = [0] * self._n
        self._counts = [0] * self._n

    def hit(self, timestamp):
        idx = timestamp % self._n
        if self._times[idx] != timestamp:
            self._times[idx] = timestamp
            self._counts[idx] = 1
        else:
            self._counts[idx] += 1

    def getHits(self, timestamp):
        total = 0
        cutoff = timestamp - self._n
        for i in range(self._n):
            if self._times[i] > cutoff:
                total += self._counts[i]
        return total
```
