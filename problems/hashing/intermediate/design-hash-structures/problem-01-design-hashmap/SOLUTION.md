# Design HashMap — Solution

## Optimal Approach

Separate chaining over a fixed prime bucket count; update-in-place on put.

### Reference implementation

```python
class MyHashMap:
    def __init__(self):
        self._buckets = [[] for _ in range(769)]

    def _idx(self, key):
        return key % 769

    def put(self, key, value):
        b = self._buckets[self._idx(key)]
        for pair in b:
            if pair[0] == key:
                pair[1] = value
                return
        b.append([key, value])

    def get(self, key):
        b = self._buckets[self._idx(key)]
        for k, v in b:
            if k == key:
                return v
        return -1

    def remove(self, key):
        b = self._buckets[self._idx(key)]
        for i, (k, _) in enumerate(b):
            if k == key:
                b.pop(i)
                return
```

### Complexity

Expected O(1) per op.

## Key Insights & Edge Cases

put(2,1) overwrites the existing key 2; remove makes get return -1.
