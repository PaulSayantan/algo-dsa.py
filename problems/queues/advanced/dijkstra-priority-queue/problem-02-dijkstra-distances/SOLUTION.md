# Dijkstra Distance Array — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def dijkstra(self, n, edges, src):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(heap, (d + w, v))
        return [x if x != INF else -1 for x in dist]
```
