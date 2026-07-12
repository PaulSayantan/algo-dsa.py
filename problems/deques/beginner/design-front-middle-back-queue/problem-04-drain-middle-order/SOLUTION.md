# Drain a Queue From the Middle — Solution

## Optimal Approach

Work on a copy so the input is not mutated. On each iteration compute the
front-middle index `(len - 1) // 2` of the *current* list, `pop` it, and append
the removed value to the output. Stop when the list is empty.

### Reference implementation

```python
class Solution:
    def drainMiddle(self, nums):
        q = list(nums)
        out = []
        while q:
            out.append(q.pop((len(q) - 1) // 2))
        return out
```
