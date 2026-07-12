# Strongly Connected Components — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def scc(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        index = [0]
        disc = [-1] * n
        low = [0] * n
        on_stack = [False] * n
        stack = []
        comps = []

        def strongconnect(start):
            work = [(start, 0)]
            while work:
                v, pi = work[-1]
                if pi == 0:
                    disc[v] = low[v] = index[0]
                    index[0] += 1
                    stack.append(v)
                    on_stack[v] = True
                recursed = False
                while pi < len(graph[v]):
                    w = graph[v][pi]
                    if disc[w] == -1:
                        work[-1] = (v, pi + 1)
                        work.append((w, 0))
                        recursed = True
                        break
                    elif on_stack[w]:
                        low[v] = min(low[v], disc[w])
                    pi += 1
                if recursed:
                    continue
                if low[v] == disc[v]:
                    comp = []
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        comp.append(w)
                        if w == v:
                            break
                    comps.append(sorted(comp))
                work.pop()
                if work:
                    parent = work[-1][0]
                    low[parent] = min(low[parent], low[v])

        for v in range(n):
            if disc[v] == -1:
                strongconnect(v)
        return sorted(comps)
```
