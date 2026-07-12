# Buffet Serving Station — Solution

## Optimal Approach

Model the line as a FIFO `deque` holding each guest's remaining portion count. On each step, hand the front guest one portion: decrement the shared `servings` and the guest's count. If that guest still wants more (`count - 1 > 0`) they rejoin the back of the line; otherwise they leave satisfied. The loop stops as soon as the queue empties (everyone served) or `servings` reaches zero. Whatever is still in the queue at that point is the set of unsatisfied guests, so its length is the answer.

### Reference implementation

```python
class Solution:
    def unservedGuests(self, hunger, servings):
        q = deque(hunger)
        while q and servings > 0:
            remaining = q.popleft() - 1
            servings -= 1
            if remaining > 0:
                q.append(remaining)
        return len(q)
```
