# Queue-Backed Stack with Bottom Query — Solution

## Optimal Approach

Use one queue with the rotate-on-push scheme so the queue's front is the stack
top. Because rotation always pushes the newest element to the front and shifts
older ones back, the **back** of the queue (`q[-1]`) is the oldest element —
the stack bottom. That makes `getBottom` an O(1) read alongside O(1) `top`/`pop`.

- `push` — O(n) (rotation)
- `pop` / `top` / `getBottom` / `empty` — O(1)

### Reference implementation

```python
class BottomStack:
    def __init__(self):
        self._q = deque()

    def push(self, x):
        self._q.append(x)
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self):
        return self._q.popleft()

    def top(self):
        return self._q[0]

    def getBottom(self):
        return self._q[-1]

    def empty(self):
        return not self._q
```

## Edge Cases

- With a single element, `top` and `getBottom` return the same value.
- `getBottom` never mutates the queue, so it does not disturb LIFO order.
- After the last `pop`, `empty` returns `True`.
