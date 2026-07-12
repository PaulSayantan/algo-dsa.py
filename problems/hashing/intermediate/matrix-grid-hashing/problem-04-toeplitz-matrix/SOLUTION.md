# Toeplitz Matrix — Solution

## Optimal Approach

One dict from r-c to the diagonal's value; mismatch ⇒ not Toeplitz.

### Reference implementation

```python
class Solution:
    def isToeplitzMatrix(self, matrix):
        diag = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                key = r - c
                if key in diag:
                    if diag[key] != matrix[r][c]:
                        return False
                else:
                    diag[key] = matrix[r][c]
        return True
```

### Complexity

Time O(R*C), space O(R+C).

## Key Insights & Edge Cases

[[1,2],[2,2]]: diagonal r-c=0 holds 1 then 2 → not Toeplitz.
