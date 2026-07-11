# Solution — Count Points in a Rectangle

## Brute Force

Keep a list of inserted points. For each `count`, scan them all and test the
rectangle.

- **Time:** `O(q²)` worst case (each of up to `q` queries scans up to `q`
  points) — `4 × 10^10` for `q = 2×10^5`. Too slow.
- **Space:** `O(q)`.

## Optimal Approach — 2D BIT of frequencies + coordinate compression

Treat the grid as a frequency matrix `f[x][y]` = number of points currently at
`(x, y)`. Then

```
count(x1,y1,x2,y2) = sum of f over [x1..x2] x [y1..y2]
```

which is precisely a **2D BIT range-sum** (Problem 1's machinery), where `add`
is a `+1` point update.

### Coordinate compression

Coordinates go up to `10^9`, so a `10^9 × 10^9` tree is impossible — but at most
`q` distinct x-values and `q` distinct y-values ever appear as *point*
coordinates. Because the whole operation list is available, we can:

1. Gather all x-coordinates from `add` operations into a sorted, de-duplicated
   array `xs`; likewise `ys` for y-coordinates. These are the only positions a
   point can occupy, so they are the only meaningful BIT indices.
2. Map each `add(x, y)` to ranks `(bisect_left(xs, x)+1, bisect_left(ys, y)+1)`.
3. For a `count`, translate the real bounds into **rank prefix boundaries**:
   - right/top edge `x2` → number of `xs` values `<= x2` = `bisect_right(xs, x2)`.
   - `x1 - 1` edge → number of `xs` values `< x1` = `bisect_left(xs, x1)`.
   - Same for y with `ys`.
   These give the four prefix arguments directly, so query bounds need *not* be
   inserted into the compression arrays.

Now the BIT is `(|xs|+1) × (|ys|+1)`, i.e. `O(q²)` memory in the absolute worst
case. If that is too large, replace the *inner* dimension with a **sorted list +
BIT built offline** or a **merge-sort tree / persistent structure**; for
`q <= 2×10^5` with typical distinct counts, the plain 2D BIT (or a BIT of
`dict`s / a BIT-of-sorted-vectors) is standard.

### Rectangle query via inclusion–exclusion

```
def rect(x1, y1, x2, y2):
    a = upper_x(x2); b = lower_x(x1)      # prefix boundaries in x-ranks
    c = upper_y(y2); d = lower_y(y1)      # prefix boundaries in y-ranks
    return P(a, c) - P(b, c) - P(a, d) + P(b, d)
```

where `P(i, j)` is the 2D BIT prefix sum over the first `i` x-ranks and `j`
y-ranks. This is the same `+ - - +` pattern as Problem 1, but the "minus-one"
edges are computed by binary search rather than simple subtraction, because
indices are compressed.

### Worked check (Example 1)

Points `(1,1)`, `(4,4)`, `(2,3)`. `xs = [1,2,4]`, `ys = [1,3,4]`.
- `count 1 1 4 4`: x-range covers ranks of all of `1,2,4`; y-range covers all of
  `1,3,4`; every point qualifies → `3`. ✔
- `count 3 1 4 4`: `x >= 3` keeps only `x = 4`, i.e. the point `(4,4)` → `1`. ✔
- `count 5 5 9 9`: `upper_x(9)=3`, `lower_x(5)=3` so the x-slab is empty → `0`. ✔

- **Time:** compression `O(q log q)`; each op `O(log²q)`. Total `O(q log²q)`.
- **Space:** `O(|xs| · |ys|)` for a dense 2D BIT (use compressed inner
  containers if this is too large).

## Key Insights & Edge Cases

- **Duplicates at one coordinate** must accumulate: use `+1` point-adds, never a
  "set to 1". Example 2 relies on this (`(2,2)` inserted twice → count `2`).
- **Query bounds are not point locations.** Do not insert `x1,x2,y1,y2` into the
  compression arrays; instead binary-search them to prefix boundaries. This
  keeps the tree size at exactly the number of distinct point coordinates.
- **Empty slabs** (e.g. `count 5 5 9 9`) correctly yield `0` because
  `upper == lower` makes the prefix difference vanish.
- **Offline alternative:** if all queries were known and no online constraint
  existed, a sweep-line sorting events by x and using a *1D* BIT over y is even
  simpler (`O(q log q)`); the 2D BIT shines precisely because answers are needed
  online.
