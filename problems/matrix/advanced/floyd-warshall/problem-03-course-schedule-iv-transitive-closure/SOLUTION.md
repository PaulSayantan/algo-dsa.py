# Solution — Course Schedule IV

## Brute Force

For each query `[u, v]`, run a fresh BFS/DFS from `u` and check whether `v` is reachable.

- `O(Q · (V + E))` time. With `Q` up to `10^4` and the graph re-traversed every query, this repeats a lot of work.
- Space `O(V + E)` for the adjacency list plus the visited set per traversal.

This passes for small graphs but recomputes reachability the queries could share.

## Optimal Approach (Floyd–Warshall — Boolean Transitive Closure)

Reachability "does a path from `u` to `v` exist?" is a fixed relation over the `V` courses. Precompute the whole `V × V` closure once, then each query is `O(1)`.

This is Floyd–Warshall where the semiring changes: replace `min` with logical **OR** and `+` with logical **AND**.

### Steps

1. Create a `V × V` boolean matrix `reach`, all `False`.
2. For each direct prerequisite `[a, b]`, set `reach[a][b] = True`.
3. Run the triple loop, `k` outermost:
   ```
   for k in range(V):
       for i in range(V):
           if reach[i][k]:
               for j in range(V):
                   if reach[k][j]:
                       reach[i][j] = True
   ```
   Read it as: "`i` reaches `j` if `i` reaches `k` **and** `k` reaches `j`."
4. For each query `[u, v]`, append `reach[u][v]`.

### Why it is correct

The min-plus DP invariant carries over to the boolean semiring: after processing intermediate vertex `k`, `reach[i][j]` is `True` iff there is a path from `i` to `j` using only intermediates in `{0, ..., k}`. When `k = V - 1`, `reach` is the full transitive closure. Because prerequisites and reachability both compose associatively ("a before b, b before c ⟹ a before c"), OR/AND accumulation computes exactly the indirect-prerequisite relation. This is the classic **Warshall's algorithm** for transitive closure.

### Reference implementation

```python
def checkIfPrerequisite(self, numCourses, prerequisites, queries):
    n = numCourses
    reach = [[False] * n for _ in range(n)]
    for a, b in prerequisites:
        reach[a][b] = True

    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                row_k = reach[k]
                row_i = reach[i]
                for j in range(n):
                    if row_k[j]:
                        row_i[j] = True

    return [reach[u][v] for u, v in queries]
```

### Complexity

- Time: `O(V³)` for the closure + `O(Q)` for the queries → `O(V³ + Q)`.
- Space: `O(V²)` for the boolean matrix.

## Key Insights & Edge Cases

- **Same triple loop, different operators.** min/plus → shortest paths; OR/AND → reachability; +/× → path counting. Recognizing the pattern lets one algorithm solve many problems.
- **DAG guarantee** means `reach[i][i]` stays `False` (no self-prerequisite), though the algorithm would still be correct with cycles.
- **The `if reach[i][k]` guard** skips whole inner loops when `i` cannot reach `k`, a meaningful speedup on sparse graphs.
- **Alternative:** topological sort + bitset propagation of ancestor sets is `O(V·E/word)` and can be faster, but Floyd–Warshall is the simplest correct approach at `V ≤ 100`.
- **Batch queries:** because the closure is precomputed, `10^4` queries cost only `10^4` lookups.
