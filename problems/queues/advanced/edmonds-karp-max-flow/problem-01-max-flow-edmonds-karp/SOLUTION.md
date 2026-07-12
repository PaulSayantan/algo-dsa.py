# Maximum Flow (Edmonds–Karp) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxFlow(self, n, edges, s, t):
        cap = [[0] * n for _ in range(n)]
        for u, v, c in edges:
            cap[u][v] += c
        flow = 0
        while True:
            parent = [-1] * n
            parent[s] = s
            q = deque([s])
            while q:
                u = q.popleft()
                for v in range(n):
                    if parent[v] == -1 and cap[u][v] > 0:
                        parent[v] = u
                        q.append(v)
            if parent[t] == -1:
                break
            bottleneck = float('inf')
            v = t
            while v != s:
                u = parent[v]
                bottleneck = min(bottleneck, cap[u][v])
                v = u
            v = t
            while v != s:
                u = parent[v]
                cap[u][v] -= bottleneck
                cap[v][u] += bottleneck
                v = u
            flow += bottleneck
        return flow
```
