# Max Value in a Queue — Solution

## Optimal Approach

Store each element together with the running maximum of everything at or below it on its own stack. The `in` stack folds the max as elements arrive; when `out` is empty we pour `in` into it, recomputing the running max in the new (reversed) order. The queue-wide maximum is simply the larger of the two stack tops' running maxes, so every operation is amortized O(1) — each element is moved between stacks at most once.

### Reference implementation

```python
class MaxQueue:
    def __init__(self):
        self._in = []   # list of (value, running_max)
        self._out = []  # list of (value, running_max)

    def push_back(self, x):
        m = x if not self._in else max(x, self._in[-1][1])
        self._in.append((x, m))

    def _shift(self):
        if not self._out:
            while self._in:
                v, _ = self._in.pop()
                m = v if not self._out else max(v, self._out[-1][1])
                self._out.append((v, m))

    def pop_front(self):
        if not self._in and not self._out:
            return -1
        self._shift()
        return self._out.pop()[0]

    def max_value(self):
        if not self._in and not self._out:
            return -1
        cands = []
        if self._in:
            cands.append(self._in[-1][1])
        if self._out:
            cands.append(self._out[-1][1])
        return max(cands)
```
