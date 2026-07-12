# Parallel Courses — Solution

## Optimal Approach

Because each semester can absorb every currently-unblocked course, the minimum
number of semesters equals the number of "levels" produced by peeling
in-degree-0 courses in waves — i.e. the longest chain of prerequisites. Run
Kahn's algorithm but drain the whole queue one level at a time, incrementing a
semester counter per level. If some courses never reach in-degree 0, a cycle
exists and the answer is `-1`.

### Reference implementation

```python
class Solution:
    def minimumSemesters(self, n, relations):
        graph = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        for a, b in relations:
            graph[a].append(b)
            indeg[b] += 1
        q = deque(v for v in range(1, n + 1) if indeg[v] == 0)
        semesters = 0
        studied = 0
        while q:
            semesters += 1
            for _ in range(len(q)):
                u = q.popleft()
                studied += 1
                for w in graph[u]:
                    indeg[w] -= 1
                    if indeg[w] == 0:
                        q.append(w)
        return semesters if studied == n else -1
```
