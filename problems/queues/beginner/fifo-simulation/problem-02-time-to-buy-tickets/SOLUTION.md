# Time Needed to Buy Tickets — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def timeRequiredToBuy(self, tickets, k):
        q = deque(range(len(tickets)))
        left = list(tickets)
        time = 0
        while True:
            i = q.popleft()
            left[i] -= 1
            time += 1
            if i == k and left[i] == 0:
                return time
            if left[i] > 0:
                q.append(i)
```
