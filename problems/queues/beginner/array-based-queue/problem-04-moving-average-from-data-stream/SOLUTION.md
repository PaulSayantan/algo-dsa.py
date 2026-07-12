# Moving Average from Data Stream — Solution

## Optimal Approach

Hold the window in a list acting as a FIFO queue. Each `next(val)` appends `val`
at the rear; if the list now holds more than `size` items, the oldest item at
the front (index 0) is dequeued so the window never exceeds `size`. The moving
average is then the sum of the window divided by its current length. (Tracking a
running sum would make each call O(1), but recomputing `sum` keeps the reference
simple and is correct.)

### Reference implementation

```python
class MovingAverage:
    def __init__(self, size):
        self._size = size
        self._window = []

    def next(self, val):
        self._window.append(val)
        if len(self._window) > self._size:
            self._window.pop(0)
        return sum(self._window) / len(self._window)
```
