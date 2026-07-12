# Two-Queue Stack (Push-Efficient) — Solution

## Optimal Approach

Keep two queues. `push` is O(1): just enqueue onto the primary queue `q1`. To
`pop` (or `top`), move every element except the last from `q1` into `q2`; the
single element left in `q1` is the stack top. Swap `q1` and `q2` so the moved
elements become the new primary. `top` does the same but re-appends the exposed
element before swapping.

- `push` — O(1)
- `pop` / `top` — O(n)
- `empty` — O(1)

### Reference implementation

```python
class MyStack:
    def __init__(self):
        self._q1 = deque()
        self._q2 = deque()

    def push(self, x):
        self._q1.append(x)

    def pop(self):
        while len(self._q1) > 1:
            self._q2.append(self._q1.popleft())
        top = self._q1.popleft()
        self._q1, self._q2 = self._q2, self._q1
        return top

    def top(self):
        while len(self._q1) > 1:
            self._q2.append(self._q1.popleft())
        top = self._q1.popleft()
        self._q2.append(top)
        self._q1, self._q2 = self._q2, self._q1
        return top

    def empty(self):
        return not self._q1
```

## Edge Cases

- A `top`/`pop` on a single-element stack simply returns that element.
- After a `top`, the element is preserved (re-enqueued), so a following `pop`
  returns the same value.
