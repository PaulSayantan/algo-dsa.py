# Maximum Flow (Dinic's) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxFlow(self, n, edges, s, t):
        graph = [[] for _ in range(n)]  # each: [to, cap, rev_index]
        def add(u, v, c):
            graph[u].append([v, c, len(graph[v])])
            graph[v].append([u, 0, len(graph[u]) - 1])
        for u, v, c in edges:
            add(u, v, c)
        def bfs():
            level = [-1] * n
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v, cap, _ in graph[u]:
                    if cap > 0 and level[v] == -1:
                        level[v] = level[u] + 1
                        q.append(v)
            return level
        def dfs(u, pushed, level, it):
            if u == t:
                return pushed
            while it[u] < len(graph[u]):
                edge = graph[u][it[u]]
                v, cap, rev = edge
                if cap > 0 and level[v] == level[u] + 1:
                    d = dfs(v, min(pushed, cap), level, it)
                    if d > 0:
                        edge[1] -= d
                        graph[v][rev][1] += d
                        return d
                it[u] += 1
            return 0
        flow = 0
        while True:
            level = bfs()
            if level[t] == -1:
                break
            it = [0] * n
            while True:
                pushed = dfs(s, float('inf'), level, it)
                if pushed == 0:
                    break
                flow += pushed
        return flow
```
