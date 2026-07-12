# Design HashSet — Solution

## Optimal Approach

Same chaining scheme as HashMap but storing keys only.

### Reference implementation

```python
class MyHashSet:
    def __init__(self):
        self._buckets = [[] for _ in range(769)]

    def _idx(self, key):
        return key % 769

    def add(self, key):
        b = self._buckets[self._idx(key)]
        if key not in b:
            b.append(key)

    def contains(self, key):
        return key in self._buckets[self._idx(key)]

    def remove(self, key):
        b = self._buckets[self._idx(key)]
        if key in b:
            b.remove(key)
```

### Complexity

Expected O(1) per op.

## Key Insights & Edge Cases

Adding 2 twice is idempotent; remove(2) clears membership.
