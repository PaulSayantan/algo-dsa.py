# Critical Connections in a Network (Bridges) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def criticalConnections(self, n, connections):
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        disc = [-1] * n
        low = [0] * n
        timer = [0]
        bridges = []

        def dfs(u, parent):
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            for w in graph[u]:
                if w == parent:
                    continue
                if disc[w] == -1:
                    dfs(w, u)
                    low[u] = min(low[u], low[w])
                    if low[w] > disc[u]:
                        bridges.append(sorted([u, w]))
                else:
                    low[u] = min(low[u], disc[w])

        for v in range(n):
            if disc[v] == -1:
                dfs(v, -1)
        return sorted(bridges)
```
