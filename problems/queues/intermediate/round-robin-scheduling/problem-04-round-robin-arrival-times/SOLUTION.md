# Round-Robin With Arrival Times — Solution

## Optimal Approach

Process arrivals in `(arrival, id)` order with a pointer `ptr` that lazily
enqueues everything that has arrived by the current clock `t`. After each quantum,
enqueue newly-arrived processes **before** requeuing the running process, so
arrivals during the quantum sit ahead of it in the FIFO. If the ready queue drains
while processes remain, jump the clock to the next arrival (the CPU idles).

### Reference implementation

```python
class Solution:
    def completionTimes(self, arrival, burst, quantum):
        n = len(arrival)
        order = sorted(range(n), key=lambda i: (arrival[i], i))
        remaining = list(burst)
        completion = [0] * n
        q = deque()
        ptr = 0
        t = 0

        def enqueue_arrivals(upto):
            nonlocal ptr
            while ptr < n and arrival[order[ptr]] <= upto:
                q.append(order[ptr])
                ptr += 1

        enqueue_arrivals(t)
        if not q and ptr < n:
            t = arrival[order[ptr]]
            enqueue_arrivals(t)

        while q:
            pid = q.popleft()
            run = min(quantum, remaining[pid])
            t += run
            remaining[pid] -= run
            enqueue_arrivals(t)
            if remaining[pid] > 0:
                q.append(pid)
            else:
                completion[pid] = t
            if not q and ptr < n:
                t = arrival[order[ptr]]
                enqueue_arrivals(t)
        return completion
```
