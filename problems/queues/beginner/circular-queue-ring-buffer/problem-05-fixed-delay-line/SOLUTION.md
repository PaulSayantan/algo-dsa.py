# Fixed-Delay Line — Solution

## Optimal Approach

Allocate a fixed array of exactly `delay` slots, pre-seeded with `fill`, plus one
`head` index. The key invariant is that the slot at `head` always holds the value
pushed `delay` steps ago — because the buffer length equals the delay, wrapping
`head` around by one each push naturally revisits each slot every `delay` pushes.

Each `push(x)` reads the value at `head` (the one that has now aged out), writes
`x` into that same slot, and advances `head = (head + 1) % delay`. During the
first `delay` pushes the slots still contain the initial `fill`, so those are what
get returned. No re-summing, shifting, or reallocation occurs, giving O(1) time
per push and O(delay) space overall — the direct ring-buffer expression of a
fixed lag.

### Reference implementation

```python
class DelayLine:
    def __init__(self, delay, fill=0):
        self._buf = [fill] * delay
        self._delay = delay
        self._head = 0

    def push(self, x):
        out = self._buf[self._head]
        self._buf[self._head] = x
        self._head = (self._head + 1) % self._delay
        return out
```
