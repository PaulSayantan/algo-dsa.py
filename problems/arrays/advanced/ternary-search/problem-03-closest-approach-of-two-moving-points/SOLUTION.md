# Solution — Closest Approach of Two Moving Points

## Brute Force

Sample time on a dense grid over `[0, T]`, compute the distance at each sample, and
take the minimum.

- **Time:** O(G) for `G` grid points. Reaching `1e-6` accuracy on `T` up to `10^4`
  needs a huge `G`, and the answer is still only approximate.
- **Space:** O(1).

This ignores the smooth, single-valley shape of the distance curve.

## Optimal Approach — two ways

### Why the objective is unimodal

Let `p = a - b` (relative start) and `w = va - vb` (relative velocity). The relative
position at time `t` is `p + w*t`, so the **squared** distance is

```
d(t)^2 = |p + w*t|^2 = |w|^2 * t^2 + 2 (p·w) * t + |p|^2
```

This is a quadratic in `t` with leading coefficient `|w|^2 >= 0`, hence **convex**. A
convex function is unimodal, and `sqrt` is monotonically increasing, so `d(t)` shares
the same (single) minimizer. Ternary search applies.

### Approach A — Ternary Search (the point of this exercise)

Search `[lo, hi] = [0, T]`. Each step:

```
m1 = lo + (hi - lo) / 3
m2 = hi - (hi - lo) / 3
if d2(m1) < d2(m2):  hi = m2      # minimize: drop the side of the larger value
else:                lo = m1
```

Compare on `d(t)^2` (`d2`) to avoid a needless `sqrt` per probe — it has the same
minimizer. Loop ~200 times (or until `hi - lo < eps`), then return `sqrt(d2(mid))`.

- **Time:** O(log_{3/2}(T / eps)) — a fixed ~200 iterations, O(1) each.
- **Space:** O(1).

```python
import math


def closest_approach(a, va, b, vb, T):
    px, py = a[0] - b[0], a[1] - b[1]
    wx, wy = va[0] - vb[0], va[1] - vb[1]

    def d2(t):
        x = px + wx * t
        y = py + wy * t
        return x * x + y * y

    lo, hi = 0.0, float(T)
    for _ in range(200):
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0
        if d2(m1) < d2(m2):
            hi = m2
        else:
            lo = m1
    return math.sqrt(d2((lo + hi) / 2.0))
```

### Approach B — Closed form (sanity check)

The unconstrained minimizer of the quadratic is at

```
t* = -(p·w) / |w|^2        (if |w| == 0, distance is constant = |p|)
```

Clamp `t*` to `[0, T]` and evaluate `d`. This is O(1) and exact. It is a great way to
**verify** the ternary-search answer, and it illustrates that ternary search is the
general tool for when no closed form exists (Problems 4 and 5).

### Why the ternary step is correct

By convexity of `d(t)^2`, if `d2(m1) < d2(m2)` with `m1 < m2`, the function is already
non-decreasing at `m2`, so nothing in `(m2, hi]` can beat `d2(m1)`; dropping `(m2, hi]`
is safe. Symmetrically for the other branch. The minimizer never leaves the window.

## Key Insights & Edge Cases

- **Optimize on `d^2`, report `d`.** Squaring removes the `sqrt` from the hot loop and
  cannot change the location of the minimum, since `sqrt` is increasing.
- **Equal velocities** (`w = 0`): the quadratic degenerates to a constant `|p|`. Ternary
  search still returns `|p|` (every probe is equal), and the closed form handles it via
  the `|w| == 0` guard.
- **Minimum at an endpoint:** if the points are separating for all `t >= 0`, the
  minimum is at `t = 0`; the window collapses to `lo`. If `t* > T`, it collapses to
  `hi`. Both are handled automatically.
- **Fixed iteration count, not exact float equality** — never loop until `m1 == m2`.
- **Relative-motion reduction** (`p = a - b`, `w = va - vb`) turns a two-body problem
  into a one-body distance-from-origin problem and keeps the algebra clean.
