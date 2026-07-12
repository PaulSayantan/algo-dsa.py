# First Non-Repeating Character in a Stream — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def firstUniqStream(self, stream):
        count = {}
        dq = deque()  # candidate chars, oldest at front
        out = []
        for ch in stream:
            count[ch] = count.get(ch, 0) + 1
            dq.append(ch)
            while dq and count[dq[0]] > 1:
                dq.popleft()
            out.append(dq[0] if dq else "#")
        return "".join(out)
```

### Complexity

O(n) time, O(1) extra space over the alphabet.
