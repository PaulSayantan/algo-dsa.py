# Solution — Maximum Distance Between Two Convex Polygons

## Brute Force

The farthest pair between two convex polygons is always a **vertex-vertex** pair, so try
every combination:

```python
import math

def max_distance_between_polygons(P, Q):
    return max(math.hypot(a[0]-b[0], a[1]-b[1]) for a in P for b in Q)
```

- **Time:** `O(|P| * |Q|)`.
- **Space:** `O(1)` extra.

Correct, but quadratic — hopeless when both polygons have `~10^5` vertices.

## Optimal Approach — Rotating Calipers on Point Grids

### Set-up

Place a directed supporting line on `P` touching its lowest vertex and a **parallel,
oppositely-directed** supporting line on `Q` touching its highest vertex. The two lines
are *anti-parallel* and squeeze the pair of polygons from opposite sides. As we rotate
this pair of calipers through a full `360°` turn, the contact vertices sweep out all the
**anti-podal vertex pairs** — and the diameter across the two polygons is guaranteed to
be one of them.

### The rotation step

At each step we look at the outgoing hull edge at the `P` caliper (`eP`) and at the `Q`
caliper (`eQ`). To keep the calipers anti-parallel we advance whichever caliper's edge
"turns first". Using the cross product of `eP` with the reversed `Q` edge `-eQ`:

- `cross(eP, -eQ) > 0`  → advance the pointer on `P`,
- `cross(eP, -eQ) < 0`  → advance the pointer on `Q`,
- `= 0` (parallel edges) → advance both and test the extra corner pairs.

Each pointer advances forward only; over one full turn the total number of steps is
`|P| + |Q|`. Record the vertex-vertex distance at every step (and the extra pairs in the
parallel case).

### Reference implementation (verified against brute force)

```python
import math

def dist(a, b):    return math.hypot(a[0]-b[0], a[1]-b[1])

def max_distance_between_polygons(P, Q):
    # assume P, Q are convex hulls given CCW; rebuild if unsure:
    # P = convex_hull(P); Q = convex_hull(Q)
    n, m = len(P), len(Q)
    if n == 1 and m == 1:
        return dist(P[0], Q[0])

    # start at extreme vertices in opposite directions
    i = min(range(n), key=lambda k: (P[k][1], P[k][0]))   # lowest of P
    j = max(range(m), key=lambda k: (Q[k][1], Q[k][0]))   # highest of Q

    best = 0.0
    for _ in range(n + m):
        best = max(best, dist(P[i], Q[j]))
        pi, qj = (i + 1) % n, (j + 1) % m
        eP = (P[pi][0] - P[i][0], P[pi][1] - P[i][1])
        eQ = (Q[qj][0] - Q[j][0], Q[qj][1] - Q[j][1])
        c = eP[0] * (-eQ[1]) - eP[1] * (-eQ[0])           # cross(eP, -eQ)
        if c > 0:
            i = pi
        elif c < 0:
            j = qj
        else:  # parallel supporting edges: check all 4 corner combinations
            best = max(best, dist(P[pi], Q[j]),
                             dist(P[i], Q[qj]),
                             dist(P[pi], Q[qj]))
            i, j = pi, qj
    return best
```

- **Time:** `O(|P| + |Q|)` for the sweep (plus `O(n log n)` if you must build the hulls
  from raw point sets first).
- **Space:** `O(1)` extra beyond the hulls.

### Why it is correct

For two convex bodies the maximum-distance pair admits parallel supporting lines on
opposite sides (each point is the extreme of its polygon in opposite directions). Every
such anti-podal configuration is realized exactly once as the anti-parallel calipers
complete a full turn, and the algorithm evaluates the vertex pair at each such
orientation — so the recorded maximum equals the true one.

## Key Insights & Edge Cases

- **Vertices only:** convexity guarantees the extreme pair is vertex-vertex, so edges and
  interiors are irrelevant for the *maximum*. (Contrast with the *minimum* distance in
  Problem 5, where the closest points can lie in the interior of an edge.)
- **Anti-parallel, not parallel:** the two calipers point in opposite directions — this
  is what distinguishes the two-polygon diameter sweep from the single-polygon one.
- **Parallel-edge ties (`c == 0`)** must test all four corner combinations, otherwise you
  can miss the true farthest pair when both polygons have a pair of parallel edges.
- **Degenerate polygons** (a single point or a segment) still work if you special-case
  `n == 1 and m == 1`; a segment (2 vertices) is handled by the general loop.
- Building the loop for exactly `n + m` steps guarantees a full turn without an explicit
  angle computation.
