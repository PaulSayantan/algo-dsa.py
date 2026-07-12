# Strongly Connected Components (Gabow) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def scc(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        preorder = [0] * n
        assigned = [False] * n
        visited = [False] * n
        path = []      # stack S
        boundary = []  # stack B
        counter = [1]
        comps = []

        def dfs(start):
            work = [(start, 0)]
            while work:
                v, pi = work[-1]
                if pi == 0:
                    visited[v] = True
                    preorder[v] = counter[0]
                    counter[0] += 1
                    path.append(v)
                    boundary.append(v)
                advanced = False
                while pi < len(graph[v]):
                    w = graph[v][pi]
                    pi += 1
                    if not visited[w]:
                        work[-1] = (v, pi)
                        work.append((w, 0))
                        advanced = True
                        break
                    elif not assigned[w]:
                        while preorder[boundary[-1]] > preorder[w]:
                            boundary.pop()
                if advanced:
                    continue
                if boundary and boundary[-1] == v:
                    boundary.pop()
                    comp = []
                    while True:
                        w = path.pop()
                        assigned[w] = True
                        comp.append(w)
                        if w == v:
                            break
                    comps.append(sorted(comp))
                work.pop()

        for v in range(n):
            if not visited[v]:
                dfs(v)
        return sorted(comps)
```
