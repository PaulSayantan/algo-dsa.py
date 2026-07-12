# Course Schedule II (Lexicographically Smallest Order) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        heap = [i for i in range(numCourses) if indeg[i] == 0]
        heapq.heapify(heap)
        order = []
        while heap:
            u = heapq.heappop(heap)
            order.append(u)
            for w in graph[u]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    heapq.heappush(heap, w)
        return order if len(order) == numCourses else []
```
