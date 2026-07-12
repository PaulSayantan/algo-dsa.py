# Versioned Persistent Stack — Solution

## Optimal Approach

### Reference implementation

```python
class PersistentStack:
    def __init__(self):
        # heads[v] = (value, parent_version) or None for empty
        self._heads = [None]

    def push(self, version, x):
        self._heads.append((x, version))
        return len(self._heads) - 1

    def pop(self, version):
        value, parent = self._heads[version]
        # the resulting stack IS the parent version; expose as new id
        self._heads.append(self._heads[parent])
        return len(self._heads) - 1

    def top(self, version):
        return self._heads[version][0]

    def empty(self, version):
        return self._heads[version] is None
```
