# Build a Queue by Middle Insertion — Solution

## Optimal Approach

Maintain the queue as a list. For each value, insert it at index `len // 2` of
the current list — the same front-middle position `pushMiddle` uses. After
processing all values, the list is the final queue contents, front first.

### Reference implementation

```python
class Solution:
    def buildByMiddle(self, nums):
        q = []
        for v in nums:
            q.insert(len(q) // 2, v)
        return q
```
