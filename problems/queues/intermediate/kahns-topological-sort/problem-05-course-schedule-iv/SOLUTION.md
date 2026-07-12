# Course Schedule IV — Solution

## Optimal Approach

Compute, for every course, the set of all of its ancestors (transitive
prerequisites). Process courses in Kahn's topological order: when a course `u`
is dequeued, every neighbor `v` inherits `u`'s ancestor set plus `u` itself.
Because `u` is emitted only after all of its own prerequisites, its ancestor set
is already complete when it is used. Each query `[u, v]` is then answered by
testing whether `u` is in `v`'s ancestor set.

### Reference implementation

```python
class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indeg[b] += 1
        ancestors = [set() for _ in range(numCourses)]
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        while q:
            u = q.popleft()
            for v in graph[u]:
                ancestors[v] |= ancestors[u]
                ancestors[v].add(u)
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return [u in ancestors[v] for u, v in queries]
```
