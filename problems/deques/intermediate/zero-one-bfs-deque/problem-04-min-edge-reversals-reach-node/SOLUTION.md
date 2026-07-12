# Minimum Edge Reversals to Reach a Node — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minReversals(self, n, edges, src, dst):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append((v, 0))  # follow the arc u->v for free
            adj[v].append((u, 1))  # go against it (reverse the edge) for cost 1
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

Every directed edge becomes two 0-1 weighted arcs: the original direction is free and the reverse costs one reversal. Once weights are in `{0, 1}`, 0-1 BFS finalizes each node's minimum reversal count in O(V + E). If `dst` sits in a component that shares no edge (directed either way) with `src`, it stays at infinity and the answer is `-1`. In example 3, reaching node 2 from node 0 requires reversing both `1->0` and `2->1`, giving a cost of 2.
