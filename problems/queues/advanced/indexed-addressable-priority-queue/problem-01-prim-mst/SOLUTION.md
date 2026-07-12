# Minimum Spanning Tree (Prim) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def mstWeight(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))
        in_tree = [False] * n
        heap = [(0, 0)]
        total = 0
        count = 0
        while heap and count < n:
            w, u = heapq.heappop(heap)
            if in_tree[u]:
                continue
            in_tree[u] = True
            total += w
            count += 1
            for ew, v in graph[u]:
                if not in_tree[v]:
                    heapq.heappush(heap, (ew, v))
        return total
```
