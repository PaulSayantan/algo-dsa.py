# Task Dispatch Log — Solution

## Optimal Approach

Model the ready queue as a FIFO `deque` of `[task_id, work_left]` pairs. Each time slice, pop the front task, record its id in the log (it was just dispatched), and let it run for `min(quantum, work_left)` units. If the task still has work left it rejoins the back of the queue; otherwise it finishes and drops out. The loop runs until the queue is empty, and the accumulated log is the dispatch order.

### Reference implementation

```python
class Solution:
    def dispatchLog(self, work, quantum):
        q = deque([[i, w] for i, w in enumerate(work)])
        log = []
        while q:
            task_id, work_left = q.popleft()
            log.append(task_id)
            work_left -= min(quantum, work_left)
            if work_left > 0:
                q.append([task_id, work_left])
        return log
```
