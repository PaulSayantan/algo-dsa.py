# Solution — Maximum Side Length of a Square with Sum <= Threshold

## Brute Force

Try every possible top-left corner and every possible side length, summing each
candidate square from scratch.

```python
best = 0
for i in range(m):
    for j in range(n):
        for L in range(1, min(m - i, n - j) + 1):
            s = sum(mat[r][c]
                    for r in range(i, i + L)
                    for c in range(j, j + L))
            if s <= threshold:
                best = max(best, L)
```

- **Time:** O(m * n * min(m, n)^3) — recomputing each square sum is `O(L^2)`.
  Far too slow for `300 x 300`.
- **Space:** O(1) extra.

## Optimal Approach — 2D Prefix Sum (Integral Image)

Two independent optimizations combine cleanly:

1. **Integral image** makes any square sum O(1).
2. **Monotonicity of the side length** lets us stop early or binary-search:
   because all values are **non-negative**, if a square of side `L` with a given
   top-left corner has sum `> threshold`, growing it never helps, and if a side
   `L` works *somewhere*, then side `L-1` also works somewhere. So the predicate
   "does a square of side `L` with sum `<= threshold` exist?" is monotone in `L`.

### Square-sum query

For a square with top-left corner `(i, j)` and side `L` (so bottom-right is
`(i+L-1, j+L-1)`), using the padded prefix table `P`:

```
sum = P[i+L][j+L] - P[i][j+L] - P[i+L][j] + P[i][j]
```

### Step by step (linear scan variant)

1. Build the padded prefix table `P` of size `(m+1) x (n+1)`.
2. Keep a running answer `L`, starting at 0.
3. For each top-left corner `(i, j)`, while a square of side `L+1` fits in the
   grid and its sum is `<= threshold`, increment `L`. Because `L` only ever
   grows, the total work is bounded.
4. Return `L`.

Alternatively, **binary search** the side length in `[0, min(m, n)]`: for a
candidate side `L`, scan all corners and check whether any square of side `L`
qualifies — O(m * n) per check, O(m * n * log(min(m, n))) overall.

### Why it is correct

The prefix-sum query returns the exact square sum, and monotonicity guarantees
that once we know the largest achievable side we have not skipped any larger
feasible square (a larger square contains a smaller one, and with non-negative
entries a contained square never has a larger sum).

### Reference implementation (growing-window scan, O(m*n))

```python
class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (mat[i - 1][j - 1] + P[i - 1][j]
                           + P[i][j - 1] - P[i - 1][j - 1])

        def square_sum(i, j, L):  # top-left (i, j), side L
            return (P[i + L][j + L] - P[i][j + L]
                    - P[i + L][j] + P[i][j])

        best = 0
        for i in range(m):
            for j in range(n):
                while (best + 1 <= m - i and best + 1 <= n - j
                       and square_sum(i, j, best + 1) <= threshold):
                    best += 1
        return best
```

- **Time:** O(m * n) — `best` increases at most `min(m, n)` times overall and
  each corner does O(1) amortized work. **Space:** O(m * n).

## Key Insights & Edge Cases

- **Non-negativity is essential** for the monotonic-side argument. If negatives
  were allowed, a bigger square could have a smaller sum and this pruning would
  break — you would fall back to checking each side length independently.
- `threshold` may be smaller than every single cell, so the answer can be **0**;
  make sure the code can return 0 rather than assuming at least a 1x1 square.
- Ensure the square stays in bounds: side `L` at corner `(i, j)` requires
  `i + L <= m` and `j + L <= n`.
- The growing-window scan is O(m * n) and slightly faster than the
  O(m * n * log) binary-search variant, but both pass comfortably.
