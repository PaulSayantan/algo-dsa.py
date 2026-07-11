# Solution — Minimum-Area Bounding Rectangle

## Brute Force

By the enclosing-rectangle theorem the optimal rectangle has a side flush with some
hull edge, so it suffices to try each hull edge as the reference direction. For each
edge, rotate the coordinate frame so that edge is horizontal, project every hull vertex,
and read off the bounding box in that frame:

```python
import math

def minimum_area_rectangle(points):
    h = convex_hull(points)
    n = len(h)
    if n < 3:
        return 0.0
    best = float('inf')
    for i in range(n):
        a, b = h[i], h[(i + 1) % n]
        ex, ey = b[0]-a[0], b[1]-a[1]
        L = math.hypot(ex, ey)
        ux, uy = ex/L, ey/L          # unit vector along the edge
        nx, ny = -uy, ux             # unit normal
        us = [(p[0]-a[0])*ux + (p[1]-a[1])*uy for p in h]
        vs = [(p[0]-a[0])*nx + (p[1]-a[1])*ny for p in h]
        width  = max(us) - min(us)
        height = max(vs) - min(vs)
        best = min(best, width * height)
    return best
```

- **Time:** `O(h^2)` — each of `h` edges re-projects all `h` vertices (plus
  `O(n log n)` for the hull).
- **Space:** `O(n)`.

This is already correct and often fast enough; the rotating-calipers version removes the
inner `O(h)` re-projection.

## Optimal Approach — Rotating Calipers on Point Grids

### Idea

Maintain **four** support pointers around the hull:

- `edge` line flush with the current hull edge (the bottom caliper),
- `top` — vertex farthest in the edge-normal direction,
- `right` — vertex farthest along the edge direction,
- `left` — vertex farthest against the edge direction.

As the reference edge advances one step, each of the other three pointers advances
**monotonically forward** (never backward) because the extreme vertex in a rotating
direction moves monotonically on a convex hull. Thus the four pointers together make one
full loop, and the whole sweep is `O(h)`.

For the current orientation:

```
width  = (projection of right vertex - projection of left vertex) onto edge direction
height = (projection of top vertex)                               onto edge normal
area   = width * height
```

Track the minimum area (you can also track perimeter or the rectangle corners the same
way).

### Sketch

The subtlety is **initialization**: the three moving pointers must start at the true
extreme vertices for the *first* edge. After that, each advance is forward-only — a
pointer moves while the next vertex has a strictly larger projection in its direction.
Because the extreme vertex is a unimodal (monotone-then-monotone) function of the
rotating direction, a naive "advance from wherever you are" without a correct start can
stop at the wrong vertex, so seed the pointers with one full scan on edge 0.

```python
import math

def sub(p, q):  return (p[0]-q[0], p[1]-q[1])
def dot(a, b):  return a[0]*b[0] + a[1]*b[1]

def minimum_area_rectangle(points):
    h = convex_hull(points)          # CCW
    n = len(h)
    if n < 3:
        return 0.0

    def adv(ptr, direction):
        # forward-only: advance while the next vertex projects strictly farther
        while dot(direction, sub(h[(ptr + 1) % n], h[ptr])) > 0:
            ptr = (ptr + 1) % n
        return ptr

    # seed pointers at the true extremes for edge 0
    d0 = sub(h[1], h[0]); perp0 = (-d0[1], d0[0])
    top   = max(range(n), key=lambda k: dot(perp0,             h[k]))
    right = max(range(n), key=lambda k: dot(d0,                h[k]))
    left  = max(range(n), key=lambda k: dot((-d0[0], -d0[1]),  h[k]))

    best = float('inf')
    for i in range(n):
        ni = (i + 1) % n
        d = sub(h[ni], h[i]); perp = (-d[1], d[0])   # edge dir and its left normal
        top   = adv(top,   perp)
        right = adv(right, d)
        left  = adv(left,  (-d[0], -d[1]))
        L = math.hypot(*d)
        width  = (dot(d, sub(h[right], h[i])) - dot(d, sub(h[left], h[i]))) / L
        height = dot(perp, sub(h[top], h[i])) / L
        best = min(best, width * height)
    return best
```

(The seeding scan is `O(h)` once; the `adv` pointers each advance at most `O(h)` total
across the whole loop, so the sweep stays linear. This version is verified against the
`O(h^2)` brute force on thousands of random hulls.)

- **Time:** `O(n log n)` (hull sort) then `O(h)` sweep.
- **Space:** `O(n)`.

### Why it is correct

The minimum-area rectangle theorem (Freeman & Shapira; used by Toussaint) guarantees an
optimal rectangle is flush with a hull edge. Enumerating all edge-flush orientations and
taking the extreme vertices in the three other directions therefore examines a superset
of candidate optima that includes the true minimum. Monotone motion of the extreme
vertices makes the enumeration linear.

## Key Insights & Edge Cases

- **Flush-edge theorem is what makes this finite** — without it the orientation space is
  continuous. Do not forget to try *every* hull edge, not just the longest.
- **Degenerate hull** (`n < 3`, all collinear, single/duplicate points): area is 0.
- **Axis-aligned box is not always optimal** — Example 1 (the diamond) shows the tilted
  rectangle (area 2) beats the axis-aligned box (area 4).
- **Divide projections by edge length** so `width`/`height` are true distances; a common
  bug is forgetting to normalize, which scales area by `|edge|^2`.
- **Same skeleton, different objective:** swap `width * height` for `2*(width+height)` to
  get the minimum-*perimeter* rectangle, still `O(h)`.
- Use strict `>` in every advance test to stay finite on hulls with parallel edges.
