# Baseball Game (Deque as a Stack) — Solution

## Optimal Approach

A deque used as a stack models the record exactly: `append` pushes new scores at
the right end, `pop` handles `"C"`, and the two most recent scores are `dq[-1]`
and `dq[-2]` for `"D"` and `"+"`. One left-to-right pass is O(n); the answer is
the sum of what remains.

### Reference implementation

```python
class Solution:
    def calPoints(self, operations):
        dq = deque()
        for op in operations:
            if op == "+":
                dq.append(dq[-1] + dq[-2])   # sum of previous two scores
            elif op == "D":
                dq.append(2 * dq[-1])        # double the previous score
            elif op == "C":
                dq.pop()                      # invalidate the previous score
            else:
                dq.append(int(op))            # record a new integer score
        return sum(dq)
```
