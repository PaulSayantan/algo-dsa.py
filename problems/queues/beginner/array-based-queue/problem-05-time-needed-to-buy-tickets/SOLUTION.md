# Time Needed to Buy Tickets — Solution

## Optimal Approach

Simulate the line directly with an array-backed FIFO queue. Each queue entry is
`[index, remaining]`. We repeatedly dequeue the person at the front (index 0),
spend one second on their purchase (decrement `remaining`, increment the clock),
and — if they still need more tickets — enqueue them at the rear. The instant
person `k` reaches `0` remaining tickets, the elapsed time is the answer.

This mirrors the physical process exactly and runs in O(total tickets) time.

### Reference implementation

```python
class Solution:
    def timeRequiredToBuy(self, tickets, k):
        queue = [[i, tickets[i]] for i in range(len(tickets))]
        time = 0
        while queue:
            idx, remaining = queue.pop(0)
            remaining -= 1
            time += 1
            if idx == k and remaining == 0:
                return time
            if remaining > 0:
                queue.append([idx, remaining])
        return time
```
