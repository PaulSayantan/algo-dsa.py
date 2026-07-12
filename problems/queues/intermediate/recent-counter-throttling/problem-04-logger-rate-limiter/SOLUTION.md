# Logger Rate Limiter — Solution

## Optimal Approach

Because timestamps arrive non-decreasing, the messages printed in the last 10 seconds form a FIFO window: the oldest print always expires first. Keep a queue of `(timestamp, message)` pairs for everything still inside the window, plus a set of the messages currently in it (so membership is O(1)).

On each call at time `t`:

1. Evict from the front of the queue while the front timestamp is `<= t - 10`, removing each evicted message from the live set.
2. If `message` is still in the live set, it was printed within the last 10 seconds — return `False`.
3. Otherwise enqueue `(t, message)`, add it to the set, and return `True`.

Each `(timestamp, message)` entry is enqueued and dequeued once, so calls are amortized O(1).

### Reference implementation

```python
class Logger:
    def __init__(self):
        self._q = deque()
        self._live = set()

    def shouldPrintMessage(self, timestamp, message):
        while self._q and self._q[0][0] <= timestamp - 10:
            _, old = self._q.popleft()
            self._live.discard(old)
        if message in self._live:
            return False
        self._q.append((timestamp, message))
        self._live.add(message)
        return True
```
