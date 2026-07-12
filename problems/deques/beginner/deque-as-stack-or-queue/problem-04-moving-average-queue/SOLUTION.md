# Moving Average from Data Stream (Deque as a Queue) — Solution

## Optimal Approach

The window is a FIFO queue on a deque: `append` the newest value at the right end,
and when the window grows past `size`, `popleft` the oldest from the left. A running
sum makes each `next` O(1) instead of re-summing the window. The average is
`running_sum / len(window)`, which naturally handles the warm-up phase (fewer than
`size` values seen).

### Reference implementation

```python
class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.window = deque()
        self.total = 0

    def next(self, val):
        self.window.append(val)          # enqueue at the right end
        self.total += val
        if len(self.window) > self.size:
            self.total -= self.window.popleft()  # dequeue the oldest at the left
        return self.total / len(self.window)
```
