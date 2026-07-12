# First Non-Repeating Word in a Stream — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def firstUniqWords(self, words):
        count = {}
        dq = deque()  # candidate words, oldest at front
        out = []
        for w in words:
            count[w] = count.get(w, 0) + 1
            if count[w] == 1:
                dq.append(w)
            while dq and count[dq[0]] > 1:
                dq.popleft()
            out.append(dq[0] if dq else "")
        return out
```

### Complexity

O(n) time (each word enqueued and dequeued at most once), O(n) space.
