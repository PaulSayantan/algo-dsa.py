# Insert Delete GetRandom O(1) — Solution

## Optimal Approach

The value→index map lets remove swap the victim with the last slot in O(1).

### Reference implementation

```python
class RandomizedSet:
    def __init__(self):
        self._pos = {}
        self._arr = []

    def insert(self, val):
        if val in self._pos:
            return False
        self._pos[val] = len(self._arr)
        self._arr.append(val)
        return True

    def remove(self, val):
        if val not in self._pos:
            return False
        i = self._pos[val]
        last = self._arr[-1]
        self._arr[i] = last
        self._pos[last] = i
        self._arr.pop()
        del self._pos[val]
        return True

    def size(self):
        return len(self._arr)
```

### Complexity

Average O(1) per op.

## Key Insights & Edge Cases

After insert 1, insert 2, remove 1: only {2} remains → size 1.
