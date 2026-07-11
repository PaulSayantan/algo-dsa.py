# Gauss–Jordan Elimination

**Gauss–Jordan elimination** is a variant of Gaussian elimination that reduces a
matrix all the way to **Reduced Row Echelon Form (RREF)** — a form in which every
pivot equals `1` and is the *only* non-zero entry in its column. Because the
elimination goes both *below* and *above* each pivot, once the algorithm finishes
you can read the answer straight off the matrix with **no back-substitution
required**.

It is the go-to hand/coding technique for three closely related jobs:

- **Solving a linear system `Ax = b`** — augment `[A | b]`, reduce to RREF, read `x`.
- **Inverting a matrix** — augment `[A | I]`, reduce the left block to `I`, and the
  right block becomes `A⁻¹`.
- **Analysing a system** — the RREF exposes the **rank**, the **pivot / free
  columns**, and therefore whether a system has a unique solution, infinitely many,
  or none.

The same machinery works over the rationals/reals, over a **finite field `GF(2)`**
(XOR puzzles such as *Lights Out*), and over **integers mod a prime `p`** (using
modular inverses) — only the "divide by the pivot" step changes.

## When to reach for it

- You need the *actual* solution vector, an inverse, or a rank — not just a yes/no.
- The matrix is small/medium (`n` up to a few hundred, or a few thousand for the
  bit-packed `GF(2)` version).
- You want a single, uniform routine that also detects inconsistent or
  under-determined systems.

## Complexity

| Task | Time | Space |
|------|------|-------|
| Solve `n×n` system (`[A\|b]`) | `O(n³)` | `O(n²)` |
| Invert `n×n` matrix (`[A\|I]`) | `O(n³)` | `O(n²)` |
| `GF(2)` system with bitsets | `O(n³ / w)` (`w` = word size) | `O(n² / w)` |

Gauss–Jordan does roughly **1.5×** the arithmetic of plain Gaussian elimination +
back-substitution (both are `O(n³)`), and you trade that extra work for a cleaner,
branch-free "read-off" at the end and a direct inverse.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Solve a System of Linear Equations](problem-01-solve-linear-system/PROBLEM.md) | Reduce `[A\|b]` to RREF and read the unique solution vector. | Easy |
| 2 | [Invert a Matrix](problem-02-matrix-inverse/PROBLEM.md) | Reduce `[A\|I]` to `[I\|A⁻¹]`; detect singular matrices. | Easy–Medium |
| 3 | [Classify a Linear System](problem-03-classify-linear-system/PROBLEM.md) | Use RREF rank to decide unique / infinite / no solution. | Medium |
| 4 | [Lights Out](problem-04-lights-out/PROBLEM.md) | Solve the light-toggling puzzle as a `GF(2)` linear system. | Medium–Hard |
| 5 | [Linear System Modulo a Prime](problem-05-linear-system-mod-p/PROBLEM.md) | Solve `Ax ≡ b (mod p)` and count solutions via free variables. | Hard |

Each problem folder contains `PROBLEM.md` (statement), `solution.py` (empty
template for you to fill in), and `SOLUTION.md` (answer key & explanation).
