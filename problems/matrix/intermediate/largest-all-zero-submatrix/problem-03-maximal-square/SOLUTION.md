# Solution — Maximal Square

## Brute Force

For every cell treat it as the top-left corner of a square and expand the side
`k = 1, 2, 3, ...` as long as the whole `k x k` block is all `'1'`s, checking
each new border. Track the largest side seen.

- **Time:** O(m·n·min(m,n)²) in the worst case (each cell tries growing squares,
  each grow re-checks a border). A 2D prefix sum reduces the all-ones test to
  O(1), giving O(m·n·min(m,n)).
- **Space:** O(1) (or O(mn) for the prefix sum).

## Optimal Approach

There are two clean linear solutions. Both are worth knowing.

### A) Per-row heights + histogram (the technique of this folder)

Build `height[j]` = number of consecutive `'1'`s ending at the current row in
column `j` (a `'0'` resets it to 0) — exactly the all-zero-submatrix scan, but
counting `'1'`s. Then, for each row, run a monotonic stack over `height[]`.

The one twist versus the plain rectangle problem: when bar `top` is popped with
available width `w = i - left - 1`, the largest *square* it supports has side
`min(height[top], w)`. Track the maximum side and return `side²`.

```python
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * n
    best_side = 0
    for row in matrix:
        for j in range(n):
            height[j] = height[j] + 1 if row[j] == '1' else 0
        # largest square in this histogram
        stack = []
        for i in range(n + 1):
            h = height[i] if i < n else 0
            while stack and height[stack[-1]] > h:
                top = stack.pop()
                left = stack[-1] if stack else -1
                width = i - left - 1
                side = min(height[top], width)
                best_side = max(best_side, side)
            stack.append(i)
    return best_side * best_side
```

Why it works: any all-`1` square with its bottom edge on row `i`, spanning
columns `[l, r]`, has side `s <= r - l + 1` (width) and `s <= min(height[l..r])`
(vertical room). The histogram scan considers exactly the maximal such
width/height combinations, and capping to `min(height, width)` turns each into
the biggest square it can host.

- **Time:** O(m·n). **Space:** O(n).

### B) Classic DP (often the expected answer)

Let `dp[i][j]` be the side of the largest all-`1` square whose **bottom-right**
corner is `(i, j)`. If `matrix[i][j] == '1'`:

```
dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
```

otherwise `dp[i][j] = 0`. The answer is `max(dp)²`. Intuition: a square of side
`k` ending at `(i, j)` requires squares of side `>= k-1` ending directly above,
to the left, and up-left; the binding constraint is their minimum. This is
O(m·n) time and can be reduced to O(n) space with a rolling row.

## Key Insights & Edge Cases

- **Input is characters** `'0'`/`'1'`, not integers — compare against the
  strings (or convert once).
- **Square vs. rectangle.** The only structural change from the rectangle
  problem is the `min(height, width)` cap. Removing that cap turns solution (A)
  back into "Maximal Rectangle".
- **Return area, not side.** LeetCode asks for `side²`; forgetting to square is
  the most common mistake.
- **No `'1'`s** → `best_side` stays 0 → area 0. **Single `'1'`** → area 1.
- The DP (B) is simplest to code under interview pressure; the histogram (A)
  ties this problem into the broader largest-submatrix technique and generalizes
  to non-square rectangles.
