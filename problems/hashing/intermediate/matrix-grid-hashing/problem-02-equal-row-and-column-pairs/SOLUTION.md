# Equal Row and Column Pairs — Solution

## Optimal Approach

Count row tuples; sum matches over column tuples (handles duplicate rows).

### Reference implementation

```python
class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        rows = defaultdict(int)
        for r in range(n):
            rows[tuple(grid[r])] += 1
        count = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            count += rows[col]
        return count
```

### Complexity

Time O(n^2), space O(n^2).

## Key Insights & Edge Cases

[[1,1],[1,1]]: 2 identical rows x 2 identical columns = 4 pairs.
