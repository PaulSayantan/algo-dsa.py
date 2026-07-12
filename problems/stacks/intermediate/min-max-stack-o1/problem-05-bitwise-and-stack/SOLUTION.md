# Bitwise-AND Stack — Solution

## Optimal Approach

The bitwise AND of all current elements is prefix-computable: the AND-so-far at
position `i` is `value[i] & and-so-far[i-1]`. Storing it beside each value keeps
the running AND on the top pair, so `andAll()` is an O(1) read and `pop` just
discards the pair — no need to "un-AND" (which is impossible once a bit is
cleared).

### Reference implementation

```python
class AndStack:
    def __init__(self):
        self._stack = []  # (val, and_so_far)

    def push(self, x):
        a = x if not self._stack else x & self._stack[-1][1]
        self._stack.append((x, a))

    def pop(self):
        self._stack.pop()

    def top(self):
        return self._stack[-1][0]

    def andAll(self):
        return self._stack[-1][1]
```
