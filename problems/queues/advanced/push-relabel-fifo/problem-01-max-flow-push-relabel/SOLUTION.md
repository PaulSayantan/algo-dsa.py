# Maximum Flow (FIFO Push–Relabel) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxFlow(self, n, edges, s, t):
        cap = [[0] * n for _ in range(n)]
        for u, v, c in edges:
            cap[u][v] += c
        flow = [[0] * n for _ in range(n)]
        height = [0] * n
        excess = [0] * n
        height[s] = n
        in_queue = [False] * n
        q = deque()
        for v in range(n):
            if cap[s][v] > 0:
                flow[s][v] = cap[s][v]
                flow[v][s] = -cap[s][v]
                excess[v] = cap[s][v]
                excess[s] -= cap[s][v]
                if v != s and v != t:
                    q.append(v)
                    in_queue[v] = True
        while q:
            u = q.popleft()
            in_queue[u] = False
            while excess[u] > 0:
                pushed = False
                for v in range(n):
                    residual = cap[u][v] - flow[u][v]
                    if residual > 0 and height[u] == height[v] + 1:
                        delta = min(excess[u], residual)
                        flow[u][v] += delta
                        flow[v][u] -= delta
                        excess[u] -= delta
                        excess[v] += delta
                        if v != s and v != t and not in_queue[v]:
                            q.append(v)
                            in_queue[v] = True
                        pushed = True
                        if excess[u] == 0:
                            break
                if not pushed:
                    min_h = float('inf')
                    for v in range(n):
                        if cap[u][v] - flow[u][v] > 0:
                            min_h = min(min_h, height[v])
                    if min_h == float('inf'):
                        break
                    height[u] = min_h + 1
        return excess[t]
```
