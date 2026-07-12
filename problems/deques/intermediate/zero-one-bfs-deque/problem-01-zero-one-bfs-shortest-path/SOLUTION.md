# Shortest Path with 0/1 Edge Weights — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def shortestPath(self, n, edges, src, dst):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0
        dq = deque([src])
        while dq:
            u = dq.popleft()
            for v, w in adj[u]:
                nd = dist[u] + w
                if nd < dist[v]:
                    dist[v] = nd
                    if w == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
        return dist[dst] if dist[dst] != INF else -1
```

### Complexity

O(V + E) time and space.

## Key Insights & Edge Cases

Node 5 has no incoming edge, so it is unreachable (-1). The path 0->2 (weight 0) then 2->3 (weight 1) reaches node 3 at distance 1, and one more weight-1 edge reaches node 4 at distance 2.
