# Front Middle Back Queue — Mixed Operations — Solution

## Optimal Approach

### Reference implementation

```python
class FrontMiddleBackQueue:
    def __init__(self):
        self._q = []

    def pushFront(self, val):
        self._q.insert(0, val)

    def pushMiddle(self, val):
        self._q.insert(len(self._q) // 2, val)

    def pushBack(self, val):
        self._q.append(val)

    def popFront(self):
        if not self._q:
            return -1
        return self._q.pop(0)

    def popMiddle(self):
        if not self._q:
            return -1
        return self._q.pop((len(self._q) - 1) // 2)

    def popBack(self):
        if not self._q:
            return -1
        return self._q.pop()
```
