# Valid Sudoku — Solution

## Optimal Approach

One pass; three region keys per filled cell into a shared set.

### Reference implementation

```python
class Solution:
    def isValidSudoku(self, board):
        seen = set()
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                keys = ((v, "row", r), (v, "col", c), (v, "box", r // 3, c // 3))
                for key in keys:
                    if key in seen:
                        return False
                    seen.add(key)
        return True
```

### Complexity

Time O(81), space O(81).

## Key Insights & Edge Cases

b2 has two 8s in the top-left box (positions (0,0) and (3,0)) → invalid.
