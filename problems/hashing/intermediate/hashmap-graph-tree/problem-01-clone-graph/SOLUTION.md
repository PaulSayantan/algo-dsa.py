# Clone Graph — Solution

## Optimal Approach

Clone-map guarantees each node is copied once; summarize deterministically.

### Reference implementation

```python
class Solution:
    def cloneGraphSummary(self, n, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        clones = {}
        for node in range(1, n + 1):
            clones[node] = node
        cloned_edges = set()
        for u in range(1, n + 1):
            for v in adj[u]:
                a, b = clones[u], clones[v]
                cloned_edges.add((min(a, b), max(a, b)))
        return [n, sorted(cloned_edges)]
```

### Complexity

Time O(V+E), space O(V+E).

## Key Insights & Edge Cases

Returning a sorted edge summary avoids comparing object identities.
