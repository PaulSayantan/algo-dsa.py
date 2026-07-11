# 2D Sparse Table

A **2D Sparse Table** generalizes the 1D sparse table to a matrix. It answers
**submatrix range queries in O(1)** for *idempotent* operations (min, max, gcd,
bitwise AND, bitwise OR) after an O(n·m·log n·log m) precompute.

## Core idea

For a 1D idempotent operation, a range `[l, r]` can be covered by exactly two
overlapping blocks of length `2^k` where `2^k` is the largest power of two that
fits in the range. Overlap is harmless *because the operation is idempotent*:
`f(x, x) = x`, so counting an element twice does not change the answer.

In 2D we precompute, for every top-left cell `(r, c)`, the answer over every
block whose height is `2^i` and width is `2^j`. A query over rectangle
`[r1, r2] x [c1, c2]` is then covered by **four** overlapping blocks:

```
kr = floor(log2(r2 - r1 + 1))     kc = floor(log2(c2 - c1 + 1))
answer = f( sp[kr][kc][r1        ][c1        ],
            f( sp[kr][kc][r1        ][c2-2^kc+1],
               f( sp[kr][kc][r2-2^kr+1][c1        ],
                  sp[kr][kc][r2-2^kr+1][c2-2^kc+1] ) ) )
```

The four blocks together cover the rectangle exactly, and their overlaps are
absorbed by idempotency.

## When to reach for it

- You have a **static** (never-changing) matrix.
- You need **many** submatrix min / max / gcd / and / or queries.
- You want **O(1)** per query and can afford the precompute memory.

If the operation is *not* idempotent (e.g. sum), use a 2D prefix-sum array
instead — a sparse table gives wrong answers there because overlaps are counted.
If the matrix changes, use a 2D segment tree / 2D BIT instead.

## Complexity

| Phase      | Time                     | Space                    |
|------------|--------------------------|--------------------------|
| Precompute | O(n·m·log n·log m)        | O(n·m·log n·log m)       |
| Query      | O(1)                     | —                        |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Submatrix Minimum Query](problem-01-submatrix-minimum-query/PROBLEM.md) | Answer many min-over-rectangle queries on a fixed grid | Easy |
| 2 | [Submatrix GCD Query](problem-02-submatrix-gcd-query/PROBLEM.md) | Answer many gcd-over-rectangle queries on a fixed grid | Medium |
| 3 | [Maximum in Every k×k Window](problem-03-max-in-all-k-by-k-windows/PROBLEM.md) | Report the max of every fixed-size square window | Medium |
| 4 | [Submatrix Value Spread](problem-04-submatrix-value-spread/PROBLEM.md) | Answer many (max − min) spread queries on rectangles | Medium |
| 5 | [Largest Uniform Square](problem-05-largest-uniform-square/PROBLEM.md) | Largest square whose value spread is ≤ D | Hard |
