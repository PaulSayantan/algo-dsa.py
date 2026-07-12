# Monotonic-Deque DP (General)

Any optimization that maximizes an expression over a bounded window reduces to a monotonic-deque scan. In 'Max Value of Equation', rewriting `yi + yj + |xi - xj|` (with xi < xj) as `(yj + xj) + (yi - xi)` lets a deque track the best `yi - xi` within the window. O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Max Value of Equation](problem-01-max-value-of-equation/PROBLEM.md) | Window-max reformulation | Hard |
