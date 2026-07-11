# 2D Prefix Sum (Integral Image)

## What it is

A **2D prefix sum** (also called a *summed-area table* or *integral image* in
computer vision) precomputes, for every cell `(i, j)`, the sum of all elements
in the rectangle from the top-left corner `(0, 0)` down to `(i, j)`. Once this
table is built, the sum of **any** axis-aligned submatrix can be answered in
**O(1)** using the inclusion-exclusion principle.

### The core formulas

Using a padded table `P` of size `(R+1) x (C+1)` where row 0 and column 0 are
all zeros (so we never index out of bounds):

**Build** (each cell in O(1)):

```
P[i][j] = matrix[i-1][j-1]
        + P[i-1][j]      # everything above
        + P[i][j-1]      # everything to the left
        - P[i-1][j-1]    # the doubly-counted overlap
```

**Query** the sum of the submatrix with rows `r1..r2` and columns `c1..c2`
(inclusive, 0-indexed in the original matrix):

```
sum = P[r2+1][c2+1]
    - P[r1][c2+1]        # strip above the region
    - P[r2+1][c1]        # strip left of the region
    + P[r1][c1]          # add back the corner subtracted twice
```

## When to reach for it

- You must answer **many** submatrix / subrectangle sum queries on an
  **immutable** grid.
- You need the sum of a fixed-size or variable-size window over a 2D grid.
- You want to turn an "is there a submatrix with property X on its sum" question
  into O(1) sum lookups (often combined with binary search, hashing, or a sorted
  set).
- The values are static after preprocessing. If the matrix is frequently
  updated, prefer a 2D Binary Indexed Tree / Segment Tree instead.

## Complexity

| Phase        | Time            | Space           |
|--------------|-----------------|-----------------|
| Build table  | O(R * C)        | O(R * C)        |
| Each query   | O(1)            | O(1) extra      |

The same recurrence generalizes to any associative + invertible operation
(e.g. **XOR** prefix tables), which is why one of the problems below uses XOR
instead of addition.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Range Sum Query 2D - Immutable](problem-01-range-sum-query-2d-immutable/PROBLEM.md) | Build the table once, answer O(1) region-sum queries | Medium |
| 2 | [Matrix Block Sum](problem-02-matrix-block-sum/PROBLEM.md) | Every cell = sum of a clamped Chebyshev block | Medium |
| 3 | [Max Side Length of a Square with Sum <= Threshold](problem-03-max-side-length-square-sum-threshold/PROBLEM.md) | Prefix sums + search over square side length | Medium |
| 4 | [Kth Largest Value in a Matrix](problem-04-kth-largest-value-xor-coordinate/PROBLEM.md) | 2D prefix table using XOR instead of `+` | Medium |
| 5 | [Number of Submatrices That Sum to Target](problem-05-num-submatrices-sum-target/PROBLEM.md) | Row/column compression + hash map of prefix sums | Hard |
| 6 | [Max Sum of Rectangle No Larger Than K](problem-06-max-sum-rectangle-no-larger-than-k/PROBLEM.md) | Column-pair prefix sums + sorted-set search | Hard |
