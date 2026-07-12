# Design Hit Counter — Solution

## Optimal Approach

Hits arrive in non-decreasing time order, so the timestamps form a natural FIFO stream: the oldest hit expires first. Store them in a queue built from two stacks — `hit` enqueues onto the `in` stack, and a query expires stale hits by dequeuing from the front (pouring `in` into `out` when needed) while the front timestamp is `<= timestamp - 300`. The remaining queue size is the number of hits in the trailing 300-second window, and every timestamp is pushed and popped at most once, giving amortized O(1) per operation.

### Reference implementation

```python
class _TwoStackQueue:
    def __init__(self):
        self._in = []
        self._out = []

    def push(self, x):
        self._in.append(x)

    def _shift(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def peek(self):
        self._shift()
        return self._out[-1]

    def pop(self):
        self._shift()
        return self._out.pop()

    def empty(self):
        return not self._in and not self._out

    def __len__(self):
        return len(self._in) + len(self._out)


class HitCounter:
    def __init__(self):
        self._q = _TwoStackQueue()

    def hit(self, timestamp):
        self._q.push(timestamp)

    def getHits(self, timestamp):
        while not self._q.empty() and self._q.peek() <= timestamp - 300:
            self._q.pop()
        return len(self._q)
```
