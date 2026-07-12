# Time Based Key-Value Store — Solution

## Optimal Approach

Append-only version lists per key; binary search by timestamp.

### Reference implementation

```python
class TimeMap:
    def __init__(self):
        self._store = defaultdict(list)

    def set(self, key, value, timestamp):
        self._store[key].append((timestamp, value))

    def get(self, key, timestamp):
        arr = self._store.get(key, [])
        lo, hi = 0, len(arr) - 1
        ans = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```

### Complexity

set O(1); get O(log n).

## Key Insights & Edge Cases

get at t=0 precedes the first set → "".
