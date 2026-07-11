# Hungarian Algorithm

The **Hungarian Algorithm** (a.k.a. the Kuhn–Munkres algorithm) solves the
**assignment problem**: given an `n x n` cost matrix where `cost[i][j]` is the
cost of assigning agent `i` to task `j`, find a one-to-one assignment (a perfect
matching) of agents to tasks that **minimizes the total cost**.

It is the polynomial-time replacement for the exponential "try every
permutation" (`O(n!)`) brute force. The classic dense-matrix implementation runs
in **`O(n^3)` time** and **`O(n^2)` space**.

## When to reach for it

Reach for the Hungarian Algorithm whenever a problem reduces to *"pair up two
equal-sized groups so that the total pairing cost is optimal, each element used
exactly once."* Tell-tale signs:

- You are given (or can build) a **cost/score matrix** between two sets.
- Each element on the left is matched to **exactly one** element on the right,
  and vice-versa (a **bijection / perfect matching**).
- You want the **minimum total cost** (or maximum total score — negate the
  matrix or subtract from a constant to flip the objective).

If `n` is tiny (`n <= ~12`) a bitmask DP (`O(n * 2^n)`) or brute force also
works, but Hungarian is the general `O(n^3)` tool that scales to a few hundred
rows. For non-square inputs, pad the matrix to a square with dummy rows/columns
of zero cost.

### Core ideas

- **Reduction / potentials:** subtracting a constant from an entire row or
  column never changes *which* assignment is optimal, only the reported total.
  The algorithm maintains row potentials `u[i]` and column potentials `v[j]`
  keeping every reduced cost `cost[i][j] - u[i] - v[j] >= 0`.
- **Augmenting paths:** it grows a matching one row at a time, using shortest
  augmenting paths in the graph of tight (zero reduced-cost) edges, adjusting
  potentials when no tight edge is available.

## Problems

| # | Problem | Technique fit | Difficulty |
|---|---------|---------------|------------|
| 1 | [Classic Assignment Problem](problem-01-classic-assignment-problem/PROBLEM.md) | Direct min-cost square assignment — the textbook case | Easy |
| 2 | [Maximum Compatibility Score Sum](problem-02-maximum-compatibility-score-sum/PROBLEM.md) | Build a score matrix, **maximize** by negating → Hungarian | Medium |
| 3 | [Campus Bikes II](problem-03-campus-bikes-ii/PROBLEM.md) | Manhattan-distance cost matrix, minimize total distance | Medium |
| 4 | [Rectangular Job Assignment](problem-04-rectangular-job-assignment/PROBLEM.md) | Unbalanced (non-square) matrix — pad with dummies | Medium |
| 5 | [Minimum XOR Sum of Two Arrays](problem-05-minimum-xor-sum-of-two-arrays/PROBLEM.md) | XOR cost matrix; Hungarian beats bitmask DP as `n` grows | Hard |

Each problem folder contains:

- `PROBLEM.md` — the statement, constraints, and worked examples.
- `solution.py` — an empty template for you to implement.
- `SOLUTION.md` — the answer key: brute force, the optimal Hungarian approach,
  and key insights / edge cases.
