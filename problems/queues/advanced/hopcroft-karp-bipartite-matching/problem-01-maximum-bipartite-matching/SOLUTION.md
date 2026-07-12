# Maximum Bipartite Matching — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxMatching(self, left, right, edges):
        graph = [[] for _ in range(left)]
        for u, v in edges:
            graph[u].append(v)
        INF = float('inf')
        match_l = [-1] * left
        match_r = [-1] * right
        dist = [0] * left

        def bfs():
            q = deque()
            for u in range(left):
                if match_l[u] == -1:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = INF
            found = False
            while q:
                u = q.popleft()
                for v in graph[u]:
                    w = match_r[v]
                    if w == -1:
                        found = True
                    elif dist[w] == INF:
                        dist[w] = dist[u] + 1
                        q.append(w)
            return found

        def dfs(u):
            for v in graph[u]:
                w = match_r[v]
                if w == -1 or (dist[w] == dist[u] + 1 and dfs(w)):
                    match_l[u] = v
                    match_r[v] = u
                    return True
            dist[u] = INF
            return False

        matching = 0
        while bfs():
            for u in range(left):
                if match_l[u] == -1 and dfs(u):
                    matching += 1
        return matching
```
