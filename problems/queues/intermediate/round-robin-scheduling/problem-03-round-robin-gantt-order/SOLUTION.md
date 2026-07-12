# Round-Robin Gantt Order — Solution

## Optimal Approach

Run the standard round-robin simulation with a FIFO queue of `(id, remaining)`.
The only difference from computing the completion order is *when* we record the
id: dispatch order is recorded the moment a process reaches the front and is put
on the CPU (before running its slice), whereas completion order is recorded only
when a process finishes. Append the id to the output on every dispatch, run
`min(quantum, remaining)`, and requeue the process at the back if work remains.

### Reference implementation

```python
class Solution:
    def ganttOrder(self, burst, quantum):
        q = deque((i, b) for i, b in enumerate(burst))
        order = []
        while q:
            pid, remaining = q.popleft()
            order.append(pid)
            run = min(quantum, remaining)
            remaining -= run
            if remaining > 0:
                q.append((pid, remaining))
        return order
```
