# Logger Rate Limiter — Solution

## Optimal Approach

Only store the most recent accepted time per message.

### Reference implementation

```python
class Logger:
    def __init__(self):
        self._last = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self._last and timestamp < self._last[message] + 10:
            return False
        self._last[message] = timestamp
        return True
```

### Complexity

O(1) per call.

## Key Insights & Edge Cases

"foo" at 1 blocks it until 11; at t=11 (>=1+10) it prints again.
