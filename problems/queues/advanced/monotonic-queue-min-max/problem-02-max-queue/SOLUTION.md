# Queue with max_value — Solution

## Optimal Approach

### Reference implementation

```python
class MaxQueue:
    def __init__(self):
        self._data = deque()
        self._mono = deque()  # decreasing

    def push_back(self, x):
        self._data.append(x)
        while self._mono and self._mono[-1] < x:
            self._mono.pop()
        self._mono.append(x)

    def pop_front(self):
        if not self._data:
            return -1
        val = self._data.popleft()
        if self._mono and self._mono[0] == val:
            self._mono.popleft()
        return val

    def max_value(self):
        return self._mono[0] if self._mono else -1
```
