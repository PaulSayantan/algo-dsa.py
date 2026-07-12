# First Unique Character in a String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def firstUniqChar(self, s):
        count = {}
        dq = deque()  # candidate indices, oldest at front
        for i, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            if count[ch] == 1:
                dq.append(i)
            while dq and count[s[dq[0]]] > 1:
                dq.popleft()
        return dq[0] if dq else -1
```

### Complexity

O(n) time, O(1) extra space over the fixed alphabet.
