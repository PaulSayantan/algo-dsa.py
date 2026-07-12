# Max Stack Backed by a Queue — Solution

## Optimal Approach

Use one queue with the rotate-on-push trick: after enqueuing `x`, rotate the
earlier `len(q)-1` elements to the back so `x` sits at the front. The front is
therefore always the stack top, giving O(1) `pop`/`top`. `peekMax` is a linear
scan over the queue for the largest value.

- `push` — O(n) (rotation)
- `pop` / `top` — O(1)
- `peekMax` — O(n)

### Reference implementation

```python
class MaxStack:
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

    def peekMax(self):
        return max(self._q)
```

## Edge Cases

- Duplicate maxima (e.g. two 5s): removing one occurrence leaves the max
  unchanged, which the linear scan handles naturally.
- `peekMax` does not mutate the stack, so subsequent `top`/`pop` are unaffected.
