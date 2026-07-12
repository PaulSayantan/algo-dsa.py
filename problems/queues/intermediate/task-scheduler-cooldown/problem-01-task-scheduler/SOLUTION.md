# Task Scheduler — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)
        max_freq = max(counts.values())
        num_max = sum(1 for c in counts.values() if c == max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)
```
