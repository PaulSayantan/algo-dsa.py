# Find the Town Judge — Solution

## Optimal Approach

The unique person with indegree n-1 and outdegree 0.

### Reference implementation

```python
class Solution:
    def findJudge(self, n, trust):
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        for a, b in trust:
            outdeg[a] += 1
            indeg[b] += 1
        for person in range(1, n + 1):
            if indeg[person] == n - 1 and outdeg[person] == 0:
                return person
        return -1
```

### Complexity

Time O(n + trust), space O(n).

## Key Insights & Edge Cases

n=1 with no trust: person 1 trivially satisfies indegree 0 = n-1 and outdegree 0.
