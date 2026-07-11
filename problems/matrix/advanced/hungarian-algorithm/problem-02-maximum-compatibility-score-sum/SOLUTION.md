# Solution — Maximum Compatibility Score Sum

## Brute Force

There are only `m <= 8` students and mentors, so try **every** pairing: a
permutation assigns student `i` to mentor `perm[i]`. Precompute the `m x m`
score matrix, then sum scores for each permutation and keep the maximum.

```python
from itertools import permutations

def maxCompatibilitySum_brute(students, mentors):
    m, n = len(students), len(students[0])
    score = [[sum(students[i][k] == mentors[j][k] for k in range(n))
              for j in range(m)] for i in range(m)]
    return max(sum(score[i][p[i]] for i in range(m)) for p in permutations(range(m)))
```

- **Time:** `O(m^2 * n)` to build the matrix + `O(m! * m)` to enumerate — with
  `m <= 8` (`8! = 40320`) this passes, but it does not generalize.
- **Space:** `O(m^2)` for the score matrix.

## Optimal Approach — Hungarian Algorithm

This is a **maximum-weight perfect matching** on a complete bipartite graph. The
Hungarian Algorithm minimizes cost, so convert maximization into minimization:

1. Build the score matrix `score[i][j]` = number of positions where student `i`
   and mentor `j` agree (`0 <= score[i][j] <= n`).
2. Form a cost matrix `cost[i][j] = -score[i][j]` (or equivalently
   `n - score[i][j]`, which keeps entries non-negative).
3. Run the `O(m^3)` Hungarian Algorithm to get the minimum total cost `C`.
4. The answer is `-C` (if you negated) or `n * m - C` (if you used `n - score`).

### Why it is correct

Any one-to-one student→mentor assignment corresponds to a permutation matrix.
Negating turns "largest total score" into "smallest total negated score", and
Hungarian returns the exact optimum of the latter, so its negation is the exact
maximum score. The `n - score` variant works because subtracting the constant
`n` from *every* entry shifts every complete assignment's total by the same
`n * m`, leaving the optimal assignment unchanged.

```python
from typing import List

class Solution:
    def maxCompatibilitySum(self, students, mentors) -> int:
        m, n = len(students), len(students[0])
        score = [[sum(students[i][k] == mentors[j][k] for k in range(n))
                  for j in range(m)] for i in range(m)]
        cost = [[n - score[i][j] for j in range(m)] for i in range(m)]  # >= 0
        INF = float("inf")
        u = [0] * (m + 1); v = [0] * (m + 1)
        p = [0] * (m + 1); way = [0] * (m + 1)
        for i in range(1, m + 1):
            p[0] = i; j0 = 0
            minv = [INF] * (m + 1); used = [False] * (m + 1)
            while True:
                used[j0] = True; i0 = p[j0]; delta = INF; j1 = -1
                for j in range(1, m + 1):
                    if not used[j]:
                        cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur; way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]; j1 = j
                for j in range(m + 1):
                    if used[j]:
                        u[p[j]] += delta; v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            while j0:
                j1 = way[j0]; p[j0] = p[j1]; j0 = j1
        min_cost = sum(cost[p[j] - 1][j - 1] for j in range(1, m + 1) if p[j])
        return n * m - min_cost
```

- **Time:** `O(m^2 * n)` to build the matrix + `O(m^3)` for Hungarian.
- **Space:** `O(m^2)` for the matrix, `O(m)` for the potentials/matching arrays.

For the tiny constraints here (`m, n <= 8`) both approaches pass; the point of
the exercise is recognizing the assignment structure and applying Hungarian so
the method scales when `m` grows well beyond what `m!` allows.

## Key Insights & Edge Cases

- **Maximize → minimize:** the standard trick is negation (`cost = -score`) or
  subtracting from a constant (`cost = n - score`). Prefer the constant-subtract
  form if your Hungarian implementation assumes non-negative entries.
- **Square matrix:** here students and mentors are equal in number, so the
  matrix is already square — no padding needed.
- **All-equal rows:** if every pair scores the same (Example 2), every pairing
  ties; Hungarian still returns the correct common total.
- **Score bounds:** each score is between `0` and `n`, so totals fit easily in a
  machine integer.
