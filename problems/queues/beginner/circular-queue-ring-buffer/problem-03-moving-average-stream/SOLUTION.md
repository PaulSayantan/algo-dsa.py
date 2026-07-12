# Moving Average from Data Stream — Solution

## Optimal Approach

Hold a fixed-size ring buffer of the last `size` values plus a running `sum`. On
each `next(val)`, if the window has not yet filled just append and grow the count;
once full, subtract the value in the head slot (the oldest), overwrite it with
`val`, and advance the head. Return `sum / count`. Every update is O(1) time and
O(size) space — no re-summing the window.

### Reference implementation

```python
class MovingAverage:
    def __init__(self, size):
        self._buf = [0] * size
        self._size = size
        self._head = 0
        self._count = 0
        self._sum = 0

    def next(self, val):
        if self._count < self._size:
            self._buf[(self._head + self._count) % self._size] = val
            self._count += 1
            self._sum += val
        else:
            self._sum -= self._buf[self._head]
            self._buf[self._head] = val
            self._head = (self._head + 1) % self._size
            self._sum += val
        return self._sum / self._count
```
