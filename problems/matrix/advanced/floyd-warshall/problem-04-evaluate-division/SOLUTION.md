# Solution — Evaluate Division

## Brute Force

For each query `[C, D]`, run a BFS/DFS from `C` through the equation graph, multiplying edge weights along the way until you reach `D` (or exhaust the component).

- `O(Q · (V + E))` time, and it re-explores the graph for every query.
- Correct and, honestly, very common for this problem. But when queries are numerous relative to variables, the ratios are better precomputed once.

## Optimal Approach (Floyd–Warshall — Multiplicative Variant)

Treat variables as graph nodes. Equation `A / B = v` gives a directed edge `A → B` with weight `v` and `B → A` with weight `1/v`. The ratio `C / D` equals the **product** of edge weights along any path from `C` to `D` (the "no contradiction" guarantee means all such paths agree). So we want all-pairs *products* — Floyd–Warshall with `×` in place of `+`.

### Steps

1. Map each distinct variable string to an index `0 .. V - 1`.
2. Build a `V × V` matrix `ratio` initialized to `0.0` (meaning "unknown"), with `ratio[i][i] = 1.0`.
3. For each equation `(A, B, v)`: `ratio[A][B] = v`, `ratio[B][A] = 1.0 / v`.
4. Run the triple loop, `k` outermost, combining with multiplication:
   ```
   for k in range(V):
       for i in range(V):
           for j in range(V):
               if ratio[i][k] != 0 and ratio[k][j] != 0 and ratio[i][j] == 0:
                   ratio[i][j] = ratio[i][k] * ratio[k][j]
   ```
5. For each query `[C, D]`: if either variable is unknown or `ratio[C][D] == 0`, answer `-1.0`; otherwise answer `ratio[C][D]`.

### Why it is correct

`ratio[i][j]` accumulates `var_i / var_j` as a telescoping product: `(a/b)·(b/c) = a/c`. After intermediate vertex `k` is processed, `ratio[i][j]` is defined whenever `i` and `j` are connected using intermediates in `{0, ..., k}`; by `k = V - 1`, every connected pair is filled. Because the problem promises no contradictions, any valid path yields the same product, so it does not matter which one Floyd–Warshall settles on — hence the `ratio[i][j] == 0` guard that just fills unknowns once.

### Reference implementation

```python
def calcEquation(self, equations, values, queries):
    idx = {}
    for a, b in equations:
        idx.setdefault(a, len(idx))
        idx.setdefault(b, len(idx))
    n = len(idx)

    ratio = [[0.0] * n for _ in range(n)]
    for i in range(n):
        ratio[i][i] = 1.0
    for (a, b), v in zip(equations, values):
        i, j = idx[a], idx[b]
        ratio[i][j] = v
        ratio[j][i] = 1.0 / v

    for k in range(n):
        for i in range(n):
            if ratio[i][k] == 0.0:
                continue
            for j in range(n):
                if ratio[k][j] != 0.0 and ratio[i][j] == 0.0:
                    ratio[i][j] = ratio[i][k] * ratio[k][j]

    ans = []
    for c, d in queries:
        if c in idx and d in idx and ratio[idx[c]][idx[d]] != 0.0:
            ans.append(ratio[idx[c]][idx[d]])
        else:
            ans.append(-1.0)
    return ans
```

### Complexity

- Time: `O(V³)` for the matrix + `O(Q)` for lookups → `O(V³ + Q)`. With `V ≤ ~40` variables, this is tiny.
- Space: `O(V²)`.

## Key Insights & Edge Cases

- **Multiplicative semiring.** Same triple loop, but combine with `×` and seed reciprocal edges — the ratio equivalent of shortest paths.
- **Unknown variable in a query** (never appears in any equation) → `-1.0`, even for `x / x`. Only *known* variables get the reflexive `1.0`.
- **Disconnected components:** `a / bc` where `a` and `bc` live in different components stays `0.0` → answer `-1.0`.
- **Using `0.0` as the "unknown" sentinel** is safe because valid values are strictly positive (`0 < values[i] <= 20`).
- **No contradictions** is guaranteed, so we never have to reconcile conflicting products; the first product found for a pair is final.
- Floating-point: products of a handful of values in `(0, 20]` stay well within double precision; LeetCode accepts answers within `1e-5`.
