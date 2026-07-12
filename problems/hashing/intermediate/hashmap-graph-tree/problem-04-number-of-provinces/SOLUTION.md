# Number of Provinces — Solution

## Optimal Approach

Count DFS launches over a visited set (or use union-find).

### Reference implementation

```python
class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        seen = set()
        count = 0

        def dfs(u):
            for v in range(n):
                if isConnected[u][v] == 1 and v not in seen:
                    seen.add(v)
                    dfs(v)

        for u in range(n):
            if u not in seen:
                seen.add(u)
                dfs(u)
                count += 1
        return count
```

### Complexity

Time O(n^2), space O(n).

## Key Insights & Edge Cases

Diagonal-only matrix ⇒ n isolated provinces.
