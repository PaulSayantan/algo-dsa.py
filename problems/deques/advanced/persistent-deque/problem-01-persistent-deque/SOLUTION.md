# Fully-Persistent Deque — Solution

## Optimal Approach

### Reference implementation

```python
class PersistentDeque:
    def __init__(self):
        self._versions = [()]  # each version is an immutable tuple

    def _add(self, contents):
        self._versions.append(contents)
        return len(self._versions) - 1

    def pushBack(self, v, x):
        return self._add(self._versions[v] + (x,))

    def pushFront(self, v, x):
        return self._add((x,) + self._versions[v])

    def popFront(self, v):
        return self._add(self._versions[v][1:])

    def front(self, v):
        return self._versions[v][0]

    def back(self, v):
        return self._versions[v][-1]
```
