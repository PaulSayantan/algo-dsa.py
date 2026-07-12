# Moving Average from Data Stream — Solution

## Optimal Approach

Hold the last `size` values in a fixed ring buffer with a `head` index (the
oldest slot) and a `count`, plus a running `sum`. While the window is not yet
full, append at `(head + count) % size` and grow `count`. Once full, the slot at
`head` is the oldest: subtract it from the running sum, overwrite it with the new
value, add that in, and advance `head` modulo `size`. The average is
`sum / count`, computed in O(1).

### Reference implementation

```python
class MovingAverage:
    def __init__(self, size):
        self._size = size
        self._data = [0] * size
        self._head = 0
        self._count = 0
        self._sum = 0

    def next(self, val):
        if self._count < self._size:
            self._data[(self._head + self._count) % self._size] = val
            self._count += 1
            self._sum += val
        else:
            self._sum -= self._data[self._head]
            self._data[self._head] = val
            self._sum += val
            self._head = (self._head + 1) % self._size
        return self._sum / self._count
```
