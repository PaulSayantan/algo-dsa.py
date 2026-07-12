# Evaluate Division — Solution

## Optimal Approach

Treat ratios as weighted edges; a path product answers each query.

### Reference implementation

```python
class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for nxt, w in graph[src].items():
                if nxt not in visited:
                    sub = dfs(nxt, dst, visited)
                    if sub != -1.0:
                        return w * sub
            return -1.0

        return [dfs(a, b, set()) for a, b in queries]
```

### Complexity

O(Q * (V+E)).

## Key Insights & Edge Cases

a/c=6.0, b/a=0.5, a/e unknown=-1.0, a/a=1.0, x/x unknown=-1.0 (float tolerance in the grader).
