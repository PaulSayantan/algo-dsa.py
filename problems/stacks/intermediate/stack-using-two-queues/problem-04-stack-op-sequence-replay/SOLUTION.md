# Replay Stack Operations Using a Queue — Solution

## Optimal Approach

Back the stack with a single queue and use the rotate-on-push scheme so the
front of the queue is always the stack top. Then walk the operation list,
dispatching on the tuple's tag: `push` enqueues and rotates, `pop` pops the
front, `top` reads the front, and `empty` reports whether the queue is empty.
Collect the outputs of `pop`/`top`/`empty` in order.

- `push` — O(n) (rotation)
- `pop` / `top` / `empty` — O(1)
- Total — O(n·k) for `k` pushes over `n` ops

### Reference implementation

```python
class Solution:
    def simulateStack(self, ops):
        q = deque()
        out = []
        for op in ops:
            tag = op[0]
            if tag == "push":
                q.append(op[1])
                for _ in range(len(q) - 1):
                    q.append(q.popleft())
            elif tag == "pop":
                out.append(q.popleft())
            elif tag == "top":
                out.append(q[0])
            elif tag == "empty":
                out.append(len(q) == 0)
        return out
```

## Edge Cases

- An `ops` list with only `empty` returns `[True]`.
- No `pop`/`top`/`empty` ops (all pushes) returns an empty list.
- The rotation on push keeps the newest element at the front, so successive
  `pop`s return values in strict LIFO order.
