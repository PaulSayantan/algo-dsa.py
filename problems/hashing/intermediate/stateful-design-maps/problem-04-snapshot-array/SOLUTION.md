# Snapshot Array — Solution

## Optimal Approach

Sparse histories keyed by index; binary search by snap id; default 0.

### Reference implementation

```python
class SnapshotArray:
    def __init__(self, length):
        self._snap = 0
        self._hist = defaultdict(list)

    def set(self, index, val):
        self._hist[index].append((self._snap, val))

    def snap(self):
        self._snap += 1
        return self._snap - 1

    def get(self, index, snap_id):
        arr = self._hist.get(index, [])
        lo, hi = 0, len(arr) - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= snap_id:
                ans = arr[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
```

### Complexity

set/snap O(1); get O(log versions).

## Key Insights & Edge Cases

get(0,0)=5 (value at snap 0); index 1 was never set → 0; after snap 1, get(0,1)=6.
