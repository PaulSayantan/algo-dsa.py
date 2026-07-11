# Gaussian Elimination

**Gaussian Elimination** is the workhorse algorithm for solving systems of linear
equations. It applies *elementary row operations* — swapping two rows, scaling a row,
and adding a multiple of one row to another — to reduce an augmented matrix to
**row-echelon form** (upper triangular) and then **back-substitutes** to recover the
solution. The same machinery answers whether a system has a unique solution, infinitely
many, or none, and it computes matrix rank, determinants, and inverses along the way.

## When to reach for it

- **Solve `A x = b`** over the rationals/reals — the textbook use case.
- **XOR / linear-basis problems over GF(2)** — treat each integer as a bit-vector and run
  Gaussian elimination over the two-element field. This gives you a *linear basis* that
  answers questions like "maximum XOR of a subset", "how many subsets XOR to `k`", and
  "is this value reachable?" in near-linear time. Over GF(2) every arithmetic op is just
  `XOR`, so a whole row is one machine-word (or `int`) operation.
- **Combinatorial systems that reduce to linear algebra mod 2** — Lights Out puzzles,
  "product is a perfect square" (prime-exponent parity vectors), turning-toggling games.

## Core idea (row reduction)

1. For each column (pivot position), find a row at or below the current pivot row whose
   entry in that column is non-zero — the **pivot**. (For numerical stability over the
   reals, pick the row with the largest absolute value: *partial pivoting*.)
2. Swap it into the pivot row, then eliminate that column from every other row by
   subtracting (or XOR-ing, over GF(2)) an appropriate multiple of the pivot row.
3. Advance to the next column. When done you have an upper-triangular / reduced form.
4. **Back-substitute** to read off the solution, or inspect pivots to count rank, detect
   inconsistency (`0 = nonzero`), and identify free variables.

## Complexity

| Setting                     | Time                | Space   |
|-----------------------------|---------------------|---------|
| `n` equations, `n` unknowns | `O(n^3)`            | `O(n^2)`|
| `n x m` system              | `O(n * m * min(n,m))` | `O(n*m)`|
| GF(2) with `W`-bit words     | `O(n * m * W / 64)` (rows as bitsets) | `O(n*m/64)` |
| Building an XOR basis of `n` numbers with `B` bits | `O(n * B)` | `O(B)` |

Over GF(2) the `int`/bitset representation makes each row operation `O(1)`-ish (one XOR),
which is why linear-basis solutions run comfortably on 10^5+ elements.

## Problems

| # | Problem | Technique | Difficulty |
|---|---------|-----------|------------|
| 1 | [Solve a Linear System](problem-01-solve-linear-system/PROBLEM.md) | Classic Gaussian elimination over the reals with back-substitution | Medium |
| 2 | [Maximum XOR of a Subset](problem-02-maximum-xor-subset/PROBLEM.md) | Build a linear basis (Gaussian elimination over GF(2)), greedily maximize | Medium |
| 3 | [Count Subsets with a Given XOR](problem-03-count-subsets-with-xor/PROBLEM.md) | Rank of the GF(2) basis gives `2^(n-r)` reachable subsets | Medium |
| 4 | [Lights Out](problem-04-lights-out/PROBLEM.md) | Model presses as a GF(2) linear system and solve it | Hard |
| 5 | [Square Subsets (product is a perfect square)](problem-05-square-subsets/PROBLEM.md) | Prime-exponent parity vectors + GF(2) rank | Hard |

Solve them in order — each reuses ideas from the previous one, moving from real-number
elimination to the GF(2) toolkit and finally to modeling a combinatorial problem as a
linear system.
