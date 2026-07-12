# First N Numbers Using Only Digits 1 and 2 — Solution

## Optimal Approach

This is the generate-binary-numbers pattern over the alphabet `{"1", "2"}`. Seeding the queue with both single-digit strings and always appending `"1"` before `"2"` makes the queue emit values in strictly increasing order: all one-digit values, then two-digit, and so on. Run the loop `n` times and convert each dequeued string to an int.

### Reference implementation

```python
class Solution:
    def firstNumbers(self, n):
        q = deque(["1", "2"])
        out = []
        for _ in range(n):
            s = q.popleft()
            out.append(int(s))
            q.append(s + "1")
            q.append(s + "2")
        return out
```
