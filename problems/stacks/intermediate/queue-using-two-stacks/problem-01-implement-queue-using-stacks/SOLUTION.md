# Implement Queue using Stacks — Solution

## Optimal Approach

### Reference implementation

```python
class MyQueue:
    def __init__(self):
        self._in = []
        self._out = []

    def push(self, x):
        self._in.append(x)

    def _shift(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def pop(self):
        self._shift()
        return self._out.pop()

    def peek(self):
        self._shift()
        return self._out[-1]

    def empty(self):
        return not self._in and not self._out
```
