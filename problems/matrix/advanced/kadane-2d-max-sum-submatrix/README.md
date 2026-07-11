# Kadane 2D — Maximum Sum Submatrix

**Kadane 2D** is a technique for finding the rectangular submatrix with the
largest possible sum inside an `n × m` grid that may contain negative numbers.

## The core idea

A brute-force search over all submatrices is `O(n² · m²)` (choose two rows and
two columns) or worse. Kadane 2D reduces this by turning the 2D problem into a
sequence of 1D problems:

1. **Fix a pair of rows** `(top, bottom)` — there are `O(n²)` such pairs.
2. **Compress the columns** between those rows into a single 1D array
   `colSum[c] = sum of matrix[top..bottom][c]`. Maintaining this array
   incrementally as `bottom` moves down costs `O(m)` per pair.
3. **Run 1D Kadane** on `colSum` to find the best contiguous column band.
   The best band, combined with the fixed row pair, defines a rectangle whose
   sum is the maximum for that pair of rows.

Taking the maximum over all row pairs gives the global answer.

```
best = -inf
for top in range(n):
    colSum = [0] * m
    for bottom in range(top, n):
        for c in range(m):
            colSum[c] += matrix[bottom][c]   # incremental column compression
        best = max(best, kadane(colSum))     # 1D subroutine
return best
```

## When to reach for it

Reach for Kadane 2D whenever a problem asks for the **best contiguous
rectangular region** of a matrix under an additive objective and the matrix can
contain negatives. The same "fix two rows, compress columns, solve a 1D
problem" skeleton also solves richer variants by swapping out the 1D
subroutine:

- **Maximum sum** → 1D Kadane.
- **Count of rectangles with a target sum** → 1D prefix-sum hash map.
- **Maximum sum not larger than K** → 1D prefix sums + sorted-set / binary search.

## Complexity

| Quantity | Cost |
|---|---|
| Time | `O(n² · m)` (fix rows `O(n²)`, compress + 1D pass `O(m)`) |
| Space | `O(m)` for the compressed column array |

Tip: put the smaller dimension on the "fixed rows" axis. If the matrix is
`n × m`, doing `O(min(n,m)² · max(n,m))` is optimal.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Maximum Subarray](problem-01-maximum-subarray/PROBLEM.md) | Master 1D Kadane — the subroutine at the heart of Kadane 2D. | Medium |
| 2 | [Maximum Sum Rectangle in a 2D Matrix](problem-02-maximum-sum-rectangle-2d/PROBLEM.md) | The canonical Kadane 2D application: max-sum rectangle. | Medium |
| 3 | [Maximum Sum Rectangle with Coordinates](problem-03-max-sum-rectangle-coordinates/PROBLEM.md) | Same reduction, but also report the rectangle's boundary. | Hard |
| 4 | [Number of Submatrices That Sum to Target](problem-04-num-submatrices-sum-target/PROBLEM.md) | Swap the 1D subroutine for a prefix-sum hash map. | Hard |
| 5 | [Max Sum of Rectangle No Larger Than K](problem-05-max-sum-rectangle-no-larger-than-k/PROBLEM.md) | Swap the 1D subroutine for sorted prefix sums + binary search. | Hard |
