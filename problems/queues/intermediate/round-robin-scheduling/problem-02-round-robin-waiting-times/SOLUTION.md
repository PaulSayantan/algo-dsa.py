# Round-Robin Waiting Times — Solution

## Optimal Approach

Run the round-robin simulation exactly as for completion order, but keep a global
clock `t`. Each time a process's remaining work drops to zero, record `t` as its
completion time. The waiting time is then `completion[i] - burst[i]`.

### Reference implementation

```python
class Solution:
    def waitingTimes(self, burst, quantum):
        q = deque((i, b) for i, b in enumerate(burst))
        t = 0
        completion = [0] * len(burst)
        while q:
            pid, remaining = q.popleft()
            run = min(quantum, remaining)
            t += run
            remaining -= run
            if remaining > 0:
                q.append((pid, remaining))
            else:
                completion[pid] = t
        return [completion[i] - burst[i] for i in range(len(burst))]
```
