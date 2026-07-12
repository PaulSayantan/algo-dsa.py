# BFS Distances From a Source — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def bfsDistances(self, n, edges, src):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dist = [-1] * n
        dist[src] = 0
        q = deque([src])
        while q:
            u = q.popleft()
            for w in graph[u]:
                if dist[w] == -1:
                    dist[w] = dist[u] + 1
                    q.append(w)
        return dist
```
