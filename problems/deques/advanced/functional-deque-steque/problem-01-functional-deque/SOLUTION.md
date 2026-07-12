# Immutable Functional Deque — Solution

## Optimal Approach

### Reference implementation

```python
class FunctionalDeque:
    def __init__(self):
        # each version: (front_list, back_list) as tuples;
        # logical order = front + reversed(back)
        self._versions = [((), ())]

    def _add(self, state):
        self._versions.append(state)
        return len(self._versions) - 1

    def _elements(self, v):
        front, back = self._versions[v]
        return list(front) + list(reversed(back))

    def pushFront(self, v, x):
        front, back = self._versions[v]
        return self._add(((x,) + front, back))

    def pushBack(self, v, x):
        front, back = self._versions[v]
        return self._add((front, (x,) + back))

    def front(self, v):
        return self._elements(v)[0]

    def back(self, v):
        return self._elements(v)[-1]
```
