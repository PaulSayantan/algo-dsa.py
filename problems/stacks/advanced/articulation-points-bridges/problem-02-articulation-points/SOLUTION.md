# Articulation Points — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def articulationPoints(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        disc = [-1] * n
        low = [0] * n
        timer = [0]
        ap = set()

        def dfs(u, parent):
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            children = 0
            for w in graph[u]:
                if w == parent:
                    continue
                if disc[w] == -1:
                    children += 1
                    dfs(w, u)
                    low[u] = min(low[u], low[w])
                    if parent != -1 and low[w] >= disc[u]:
                        ap.add(u)
                else:
                    low[u] = min(low[u], disc[w])
            if parent == -1 and children > 1:
                ap.add(u)

        for v in range(n):
            if disc[v] == -1:
                dfs(v, -1)
        return sorted(ap)
```
