# Course Schedule — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        seen = 0
        while q:
            u = q.popleft()
            seen += 1
            for w in graph[u]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    q.append(w)
        return seen == numCourses
```
