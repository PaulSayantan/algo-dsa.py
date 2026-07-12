# Front Middle Back Queue — Peek Operations — Solution

## Optimal Approach

The three peeks reuse the exact index rules of the pushes/pops but read instead
of remove: front is index `0`, back is index `-1`, and the front-middle is index
`(len - 1) // 2`. Guard the empty case with `-1`.

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

    def peekFront(self):
        return self._q[0] if self._q else -1

    def peekMiddle(self):
        if not self._q:
            return -1
        return self._q[(len(self._q) - 1) // 2]

    def peekBack(self):
        return self._q[-1] if self._q else -1
```
