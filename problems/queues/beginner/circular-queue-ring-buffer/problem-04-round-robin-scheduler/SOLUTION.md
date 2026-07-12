# Round-Robin Task Scheduler — Solution

## Optimal Approach

Treat the task array as a circular queue: keep a single `head` index. `next()`
reads `tasks[head]`, then advances `head = (head + 1) % n` so the cursor wraps
from the last task back to the first. `peek()` simply returns `tasks[head]`
without moving the cursor. Both operations are O(1) and use no extra space beyond
the stored task list.

### Reference implementation

```python
class RoundRobin:
    def __init__(self, tasks):
        self._tasks = list(tasks)
        self._n = len(tasks)
        self._head = 0

    def next(self):
        task = self._tasks[self._head]
        self._head = (self._head + 1) % self._n
        return task

    def peek(self):
        return self._tasks[self._head]
```
