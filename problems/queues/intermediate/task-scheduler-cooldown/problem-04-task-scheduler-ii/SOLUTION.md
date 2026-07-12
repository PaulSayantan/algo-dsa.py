# Task Scheduler II — Solution

## Optimal Approach

Because the tasks must run in order, we never reorder them; the only choice is how many idle days to insert. Keep a dictionary mapping each task type to the earliest day it may next run. Walk the tasks left to right, incrementing the day by one for each. If the current type is still cooling down (its next-available day is in the future), jump the day counter forward to that ready-time. After running a task on day `day`, its type becomes available again on `day + space + 1`.

### Reference implementation

```python
class Solution:
    def taskSchedulerII(self, tasks, space):
        next_avail = {}  # task type -> earliest day it may run again
        day = 0
        for t in tasks:
            day += 1
            if t in next_avail and next_avail[t] > day:
                day = next_avail[t]
            next_avail[t] = day + space + 1
        return day
```

### Complexity

O(n) time, O(u) space where u is the number of distinct task types.
