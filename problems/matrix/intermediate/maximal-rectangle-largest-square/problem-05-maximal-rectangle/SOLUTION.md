# Maximal Rectangle — Solution

## Brute Force

Enumerate every rectangle by its top row, bottom row, and column span, then check whether all
its cells are `1`. Even with 2-D prefix sums to make each all-`1` check `O(1)`, there are
`O(rows^2 * cols^2)` rectangles to test.

- **Time:** `O(rows^2 * cols^2)` with prefix sums (worse without).
- **Space:** `O(rows * cols)` for the prefix-sum table.

At `rows, cols <= 200` this is up to `~1.6 * 10^9` checks — too slow.

## Optimal Approach (Histogram per row + monotonic stack)

**The reduction.** Scan the matrix row by row from top to bottom. Maintain an array
`heights[j]` = the number of consecutive `1`s in column `j` ending at the current row:

```
heights[j] = heights[j] + 1   if matrix[i][j] == '1'
heights[j] = 0                if matrix[i][j] == '0'
```

At each row, `heights` describes a histogram whose bars sit on that row as a base. The
largest all-`1` rectangle whose **bottom edge lies on row `i`** is exactly the *largest
rectangle in that histogram* (Problem 3). Every all-`1` rectangle in the matrix has some
bottom row, so taking the max of the per-row histogram answers over all rows gives the global
maximum.

**Why it is correct.** A rectangle of height `h` and width `w` with bottom edge on row `i`
requires `w` consecutive columns each having at least `h` consecutive `1`s ending at row `i`
— i.e. `heights[j] >= h` for those columns. That is precisely a rectangle of area `h * w`
inside the histogram `heights`. The histogram subroutine finds the best such `h * w` for the
current row in `O(cols)`; iterating over rows covers every possible bottom edge, hence every
rectangle.

**The histogram subroutine** uses a monotonic increasing stack (see Problem 3): when a bar
shorter than the stack top arrives, pop the top, its right boundary is the current index and
its left boundary is the new stack top, so its widest rectangle at its own height is
`heights[top] * (i - stack[-1] - 1)`.

**Step by step.**
1. Initialize `heights = [0] * cols` and `best = 0`.
2. For each row: update `heights` per the rule above.
3. Run the histogram routine on `heights`; update `best`.
4. After all rows, return `best`.

```python
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    cols = len(matrix[0])
    heights = [0] * cols
    best = 0
    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0
        best = max(best, largest_in_histogram(heights))
    return best

def largest_in_histogram(heights):
    stack = []          # indices, strictly increasing heights
    best = 0
    n = len(heights)
    for i in range(n + 1):
        h = 0 if i == n else heights[i]
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            left = stack[-1] if stack else -1
            best = max(best, heights[top] * (i - left - 1))
        stack.append(i)
    return best
```

- **Time:** `O(rows * cols)` — each row's histogram is linear in `cols`.
- **Space:** `O(cols)` for `heights` and the stack.

## Key Insights & Edge Cases

- **2-D to 1-D.** The whole technique is: reduce each row to a histogram, then reuse the
  linear-time largest-rectangle-in-histogram subroutine. Master Problem 3 first.
- **Reset on `0`.** A `0` cell zeroes that column's height, correctly cutting the vertical run
  and acting as a boundary inside the histogram.
- **Rectangle vs. square.** Compare Example 1 here (answer 6) with Maximal Square on the same
  grid (answer 4): allowing non-square rectangles strictly can do better, which is why the
  square DP does not solve this problem.
- **Character grid.** Cells are `'0'`/`'1'` characters; compare against `'1'`.
- **Empty / all-zero matrix** returns `0`; the heights stay `0` and the histogram area is `0`.
- **Alternative DP.** A left/right/height DP achieves the same `O(rows * cols)` without an
  explicit stack, but the histogram-per-row framing generalizes better (see Problem 6 for
  counting).
