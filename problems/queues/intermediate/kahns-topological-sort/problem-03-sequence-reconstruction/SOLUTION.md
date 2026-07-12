# Sequence Reconstruction — Solution

## Optimal Approach

Model each `sequences[i]` as a chain of directed edges between consecutive
elements. `nums` is the unique reconstruction exactly when the DAG has a single
topological order equal to `nums`. With Kahn's algorithm, a unique order means
the in-degree-0 queue contains exactly one node at every step; more than one
choice means at least two valid orders exist.

### Reference implementation

```python
class Solution:
    def sequenceReconstruction(self, nums, sequences):
        indeg = {x: 0 for x in nums}
        graph = defaultdict(set)
        for seq in sequences:
            for x in seq:
                if x not in indeg:
                    return False  # value outside 1..n -> impossible
            for a, b in zip(seq, seq[1:]):
                if b not in graph[a]:
                    graph[a].add(b)
                    indeg[b] += 1
        q = deque(x for x in indeg if indeg[x] == 0)
        order = []
        while q:
            if len(q) > 1:
                return False  # more than one node available -> not unique
            u = q.popleft()
            order.append(u)
            for w in graph[u]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    q.append(w)
        return order == nums
```
