# 0-1 Weighted Shortest Path — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def shortestPath(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0
        dq = deque([0])
        while dq:
            u = dq.popleft()
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if w == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
        return dist[n - 1] if dist[n - 1] != INF else -1
```
