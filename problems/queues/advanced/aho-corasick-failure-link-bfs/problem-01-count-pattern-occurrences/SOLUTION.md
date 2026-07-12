# Count Multi-Pattern Occurrences — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countOccurrences(self, patterns, text):
        goto = [{}]
        fail = [0]
        out = [0]
        for p in patterns:
            node = 0
            for ch in p:
                if ch not in goto[node]:
                    goto.append({})
                    fail.append(0)
                    out.append(0)
                    goto[node][ch] = len(goto) - 1
                node = goto[node][ch]
            out[node] += 1
        q = deque()
        for ch, nxt in goto[0].items():
            fail[nxt] = 0
            q.append(nxt)
        while q:
            u = q.popleft()
            for ch, v in goto[u].items():
                f = fail[u]
                while f and ch not in goto[f]:
                    f = fail[f]
                fail[v] = goto[f][ch] if (f != 0 or ch in goto[0]) and ch in goto[f] else 0
                if fail[v] == v:
                    fail[v] = 0
                out[v] += out[fail[v]]
                q.append(v)
        node = 0
        total = 0
        for ch in text:
            while node and ch not in goto[node]:
                node = fail[node]
            node = goto[node].get(ch, 0)
            total += out[node]
        return total
```
