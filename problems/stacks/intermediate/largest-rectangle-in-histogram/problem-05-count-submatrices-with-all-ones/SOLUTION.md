# Count Submatrices With All Ones — Solution

## Optimal Approach

Maintain a running histogram `h[j]` = number of consecutive `1`s ending at column
`j` in the current row (reset to 0 on a `0`). For a fixed bottom row, the count of
all-`1` submatrices with right edge at column `j` is the sum, over every subarray
of columns ending at `j`, of the minimum height in that subarray. A monotonic
(non-decreasing) stack accumulates that "sum of subarray minima ending here"
incrementally: on each new bar pop taller-or-equal runs, fold their column counts
into the current one, and add `height * count`. Summing the running total across
all columns and rows gives the answer in O(rows * cols).

### Reference implementation

```python
class Solution:
    def numSubmat(self, mat):
        if not mat or not mat[0]:
            return 0
        n = len(mat[0])
        h = [0] * n
        res = 0
        for row in mat:
            for j in range(n):
                h[j] = h[j] + 1 if row[j] else 0
            stack = []  # (height, number_of_columns_folded_into_this_run)
            running = 0  # sum of subarray minima over subarrays ending at column j
            for j in range(n):
                cnt = 1
                while stack and stack[-1][0] >= h[j]:
                    ph, pc = stack.pop()
                    running -= ph * pc
                    cnt += pc
                running += h[j] * cnt
                stack.append((h[j], cnt))
                res += running
        return res
```
