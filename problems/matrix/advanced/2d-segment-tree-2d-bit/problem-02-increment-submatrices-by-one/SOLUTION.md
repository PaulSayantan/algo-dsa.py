# Solution — Increment Submatrices by One

## Brute Force

For each of the `q` queries, loop over the whole rectangle and add 1.

- **Time:** `O(q · n²)` — up to `10^4 · 500² = 2.5 × 10^9`. Too slow.
- **Space:** `O(n²)` for the matrix.

## Optimal Approach

This is the **range-update / point-query** direction, the mirror image of
Problem 1 (point-update / range-query). Two equivalent implementations:

### Approach A — 2D difference array (linear, simplest)

Maintain a difference grid `diff` of size `(n+1) × (n+1)`. Adding 1 to rectangle
`(r1,c1)..(r2,c2)` costs `O(1)` via four corner stamps:

```
diff[r1][c1]     += 1
diff[r2+1][c1]   -= 1
diff[r1][c2+1]   -= 1
diff[r2+1][c2+1] += 1
```

After all queries, run a **2D prefix sum** over `diff` to recover the answer:

```
mat[i][j] = diff[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
```

- **Time:** `O(q + n²)`.
- **Space:** `O(n²)`.

### Approach B — 2D BIT (range-update / point-query)

The four-corner stamp is exactly a 2D difference; a Fenwick tree lets us apply
it *and* read any single cell **online** (without a final full pass), which is
the reusable pattern when queries and reads interleave.

Key identity: if we place the four `±1` stamps into a BIT via point-add, then the
**2D prefix sum up to `(i, j)`** of the BIT equals the number of query
rectangles covering cell `(i, j)` — i.e. `mat[i][j]`.

```
def add(self, r, c, delta):         # point add, 1-indexed internally
    i = r + 1
    while i <= n:
        j = c + 1
        while j <= n:
            bit[i][j] += delta
            j += j & (-j)
        i += i & (-i)

def point_value(self, r, c):        # prefix sum [0..r] x [0..c]
    total, i = 0, r + 1
    while i > 0:
        j = c + 1
        while j > 0:
            total += bit[i][j]
            j -= j & (-j)
        i -= i & (-i)
    return total
```

For each query:

```
add(r1, c1, +1); add(r2+1, c1, -1); add(r1, c2+1, -1); add(r2+1, c2+1, +1)
```

Then `mat[i][j] = point_value(i, j)`.

Note `r2+1` or `c2+1` may equal `n`; with 1-indexing those stamps land at BIT
index `n+1`, so allocate the tree as `(n+2) × (n+2)` (or guard the loop bound).

- **Time:** `O(q · log²n + n² · log²n)`.
- **Space:** `O(n²)`.

### Why range-add ↔ point-read is a prefix sum

A cell `(i, j)` is inside rectangle `(r1,c1)..(r2,c2)` iff `r1 <= i <= r2` and
`c1 <= j <= c2`. The four stamps are the 2D indicator's inclusion–exclusion: the
prefix sum accumulates `+1` when it passes the top-left corner and cancels it
again past the bottom/right edges, so the running prefix at `(i,j)` counts
exactly the rectangles that still "cover" it.

## Key Insights & Edge Cases

- The **four-corner stamp** is the heart of range updates in 2D; memorize the
  `+ - - +` sign pattern.
- **Off-by-one on the far corners:** stamps go at `r2+1` and `c2+1`, which can be
  `n`. Size the difference/BIT arrays to `n+1` (or `n+2` for the 1-indexed BIT).
- For this exact problem, **Approach A wins** — it is `O(q + n²)` with a tiny
  constant. Reach for the BIT (Approach B) only when reads must be answered
  *interleaved* with updates, where the linear final pass is not an option.
- Roles are dual to Problem 1: there, point-update + range-query; here,
  range-update + point-query. Recognizing which mode a problem needs is the
  main skill.
