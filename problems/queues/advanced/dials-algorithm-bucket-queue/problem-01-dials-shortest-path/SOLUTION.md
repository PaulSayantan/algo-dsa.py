# Shortest Path with Small Integer Weights — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def shortestPaths(self, n, edges, src):
        graph = [[] for _ in range(n)]
        max_w = 0
        for u, v, w in edges:
            graph[u].append((v, w))
            max_w = max(max_w, w)
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        max_dist = (n - 1) * max(max_w, 1) + 1
        buckets = [[] for _ in range(max_dist + 1)]
        buckets[0].append(src)
        d = 0
        processed = 0
        while d <= max_dist and processed < n:
            while buckets[d]:
                u = buckets[d].pop()
                if dist[u] != d:
                    continue
                processed += 1
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        buckets[nd].append(v)
            d += 1
        return [x if x != INF else -1 for x in dist]
```
