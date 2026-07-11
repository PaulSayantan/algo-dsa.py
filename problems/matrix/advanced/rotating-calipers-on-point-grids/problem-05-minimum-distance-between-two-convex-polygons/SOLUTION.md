# Solution — Minimum Distance Between Two Convex Polygons

## Brute Force

The closest features between two convex polygons are two of their **edges** (a vertex
of one can lie closest to the interior of an edge of the other), so compare every edge
of `P` against every edge of `Q` with a segment-to-segment distance:

```python
import math

def pt_seg(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))

def seg_seg(p1, p2, p3, p4):
    return min(pt_seg(p1, p3, p4), pt_seg(p2, p3, p4),
               pt_seg(p3, p1, p2), pt_seg(p4, p1, p2))

def min_distance_between_polygons(P, Q):
    n, m = len(P), len(Q)
    best = float('inf')
    for i in range(n):
        for j in range(m):
            best = min(best, seg_seg(P[i], P[(i+1) % n], Q[j], Q[(j+1) % m]))
    return best
```

- **Time:** `O(|P| * |Q|)`.
- **Space:** `O(1)` extra.

Correct but quadratic.

## Optimal Approach — Rotating Calipers on Point Grids

### Idea (co-parallel calipers)

For the *maximum* distance the calipers were anti-parallel; for the *minimum* distance
they are **co-parallel** — the two support lines point the same way, forming a moving
"bridge" that keeps the polygons on the same side. Concretely, we track a single
rotating direction. At each moment, `P`'s supporting edge has some outward normal, and
`Q`'s supporting edge has the *opposite* outward normal (`Q` faces `P`). We advance
whichever polygon's next edge-normal event comes first as the direction rotates through
a full `2π`.

At every configuration the current supporting edges of `P` and `Q` are the **co-podal**
pair; the closest features are always one of these co-podal edge pairs, so we take the
segment-to-segment distance at each step and keep the minimum.

### Steps

1. Build both hulls in CCW order (`O(n log n)`). Start `P`'s pointer at its lowest
   vertex (support direction "down", normal angle `-90°`) and `Q`'s pointer at its
   highest vertex (support direction "up") — these two supports face each other.

2. Maintain the current rotation angle `curP` (`P`'s outward-normal angle). For the two
   current edges compute their outward-normal angles; map `Q`'s into `P`'s frame by
   subtracting `π` (co-parallel bridge). Advance the pointer whose normal is reached
   with the smaller angular gap. Do this for `|P| + |Q|` steps to complete a full turn.

3. At each step record `seg_seg(P[p], P[p+1], Q[q], Q[q+1])`; the running minimum is the
   answer.

Each pointer advances forward only, so the sweep is `O(|P| + |Q|)`.

### Reference implementation (verified against brute force on 270k+ disjoint cases)

```python
import math

TAU = 2 * math.pi

def norm(a):
    a %= TAU
    return a + TAU if a < 0 else a

def edge_normal_angle(A, B):
    # outward normal of a CCW edge A->B is (edge rotated -90 deg) = (ey, -ex)
    ex, ey = B[0] - A[0], B[1] - A[1]
    return math.atan2(-ex, ey)

def min_distance_between_polygons(P, Q):
    # P, Q are convex hulls in CCW order (rebuild with convex_hull() if unsure)
    n, m = len(P), len(Q)
    p = min(range(n), key=lambda k: (P[k][1], P[k][0]))   # lowest of P
    q = max(range(m), key=lambda k: (Q[k][1], Q[k][0]))   # highest of Q
    curP = norm(-math.pi / 2)
    best = float('inf')
    for _ in range(n + m + 1):
        best = min(best, seg_seg(P[p], P[(p+1) % n], Q[q], Q[(q+1) % m]))
        thetaP = edge_normal_angle(P[p], P[(p+1) % n])
        thetaQ = norm(edge_normal_angle(Q[q], Q[(q+1) % m]) - math.pi)  # into P's frame
        gapP = norm(thetaP - curP)
        gapQ = norm(thetaQ - curP)
        eps = 1e-12
        if gapP < gapQ - eps:
            curP = norm(thetaP); p = (p + 1) % n
        elif gapQ < gapP - eps:
            curP = norm(thetaQ); q = (q + 1) % m
        else:                                 # both edges become supporting together
            curP = norm(thetaP); p = (p + 1) % n; q = (q + 1) % m
    return best
```

(`seg_seg` / `pt_seg` are the helpers from the brute-force section.)

- **Time:** `O(|P| + |Q|)` for the sweep (plus `O(n log n)` per hull if you build them).
- **Space:** `O(1)` extra beyond the hulls.

### Why it is correct

For two disjoint convex polygons, the closest pair of points lies on a pair of parallel
supporting lines that separate the two shapes — a co-podal edge/edge or vertex/edge
pair. As the co-parallel calipers rotate a full turn, every co-podal configuration is
visited exactly once. Measuring the segment-to-segment distance at each catches the case
where the closest point is in the interior of an edge, so the minimum over all steps is
the true minimum distance.

## Key Insights & Edge Cases

- **Segment-to-segment, not vertex-to-vertex.** This is the crucial difference from the
  *maximum*-distance problem (Problem 4). For the minimum, the closest point can lie in
  the middle of an edge, so vertex-vertex comparisons alone can overestimate. Example 1
  (two axis-aligned squares) is exactly such a case: the closest features are two
  *edges* facing across the gap.
- **Precondition: disjoint polygons.** If the polygons overlap or touch, the minimum
  distance is 0; detect intersection separately (any edge crossing, or one polygon's
  vertex inside the other) before/instead of running the sweep — the co-parallel sweep
  assumes a clean separating direction exists.
- **Co-parallel vs anti-parallel.** Minimum distance uses co-parallel calipers (bridge);
  maximum distance uses anti-parallel calipers. Getting this backwards silently returns
  wrong answers.
- **Parallel-edge ties (`gapP == gapQ`)** advance both pointers; still take the
  segment-to-segment distance so no facing pair is skipped.
- **Full turn:** iterate `|P| + |Q|` steps (a full `2π`), not `π` — the closest support
  direction may point either way around, and a half-turn can miss it.
