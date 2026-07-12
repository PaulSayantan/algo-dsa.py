# Design Underground System — Solution

## Optimal Approach

Store cumulative time and trip count per (start, end) pair.

### Reference implementation

```python
class UndergroundSystem:
    def __init__(self):
        self._checkins = {}
        self._totals = defaultdict(lambda: [0, 0])

    def checkIn(self, id, stationName, t):
        self._checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start, t0 = self._checkins.pop(id)
        rec = self._totals[(start, stationName)]
        rec[0] += t - t0
        rec[1] += 1

    def getAverageTime(self, startStation, endStation):
        total, cnt = self._totals[(startStation, endStation)]
        return total / cnt
```

### Complexity

All ops O(1).

## Key Insights & Edge Cases

Trips of 5, 5, 11 give averages 5.0, 5.0, then (5+5+11)/3 = 7.0.
