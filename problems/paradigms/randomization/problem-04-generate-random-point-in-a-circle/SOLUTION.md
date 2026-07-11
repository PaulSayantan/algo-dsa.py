# Generate Random Point in a Circle — Solution

## Brute Force / Naive (and why the "obvious" polar sample is WRONG)

The tempting approach is to sample in polar coordinates: pick an angle `theta` uniformly in
`[0, 2*pi)` and a radius `r` uniformly in `[0, R]`, then return
`(x_center + r*cos(theta), y_center + r*sin(theta))`.

This is **incorrect** — it over-samples near the center. The area of a thin ring at radius
`r` grows like `2*pi*r*dr`, so a uniform-area distribution must place *more* points at larger
`r`. Choosing `r` uniformly gives every radius equal weight and crams too many points into
the small central region. The density ends up proportional to `1/r`, not constant.

So the naive polar sample is fast (O(1) per call) but produces the wrong distribution.

## Optimal Approach (Randomization)

There are two standard correct methods.

### Method A — Rejection sampling

Sample a uniform point in the axis-aligned bounding square `[-R, R] x [-R, R]` (relative to
the center) and reject it if it falls outside the circle; repeat until one is accepted:

```python
def randPoint(self):
    R = self.radius
    while True:
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)
        if x * x + y * y <= R * R:
            return [self.x_center + x, self.y_center + y]
```

Uniform points in the square, conditioned on landing in the inscribed disk, are exactly
uniform over the disk (conditioning a uniform distribution on a sub-region yields a uniform
distribution on that sub-region). Correct and trivially so.

### Method B — Inverse-transform sampling (no loop)

Fix the naive polar method by transforming the radius. Draw `U` uniform in `[0, 1]` and set
`r = R * sqrt(U)`; draw `theta` uniform in `[0, 2*pi)`:

```python
def randPoint(self):
    r = self.radius * math.sqrt(random.random())   # sqrt is the key correction
    theta = 2 * math.pi * random.random()
    x = self.x_center + r * math.cos(theta)
    y = self.y_center + r * math.sin(theta)
    return [x, y]
```

Why `sqrt`? For an area-uniform disk, `P(radius <= r) = (pi r^2)/(pi R^2) = (r/R)^2`. To
sample from that CDF, invert it: set `(r/R)^2 = U` (uniform), giving `r = R * sqrt(U)`. The
square root exactly cancels the ring-area growth, restoring constant density.

### Complexity

- **Rejection sampling:** O(1) *expected* time per call. The acceptance probability is
  `area(circle) / area(square) = pi*R^2 / (2R)^2 = pi/4 ≈ 0.785`, so the expected number of
  draws is `4/pi ≈ 1.27` — essentially constant. O(1) space.
- **Inverse-transform:** O(1) time per call (no loop at all), O(1) space. One `sqrt`, one
  `sin`, one `cos`.
- Both use O(1) space in the constructor (just store radius and center).

## Key Insights & Edge Cases

- **Area, not radius, must be uniform.** The single most common mistake is a uniform radius,
  which clusters points near the center. Remember the `sqrt` (Method B) or use rejection
  (Method A).
- **Rejection needs the right enclosing region.** The square must tightly bound the circle
  (`[-R, R]^2`) so acceptance probability stays high (`pi/4`). A loose enclosing box wastes
  draws; a box that does not fully contain the disk breaks uniformity.
- **Boundary inclusion.** The problem includes the boundary. Using `<=` (rejection) or
  allowing `U = 1` / `r = R` (inverse-transform) includes it. Because a boundary has measure
  zero, whether the exact edge is included does not affect uniformity or graders.
- **Translate at the end.** Sample relative to the origin, then add `(x_center, y_center)`.
  Sampling directly in absolute coordinates is error-prone.
- **Large radius / center:** `radius` up to `1e8` and centers up to `1e7` are fine in double
  precision; there is no overflow concern in Python floats.
- **Expected vs. worst case (Method A):** rejection sampling is a *Las Vegas* algorithm — the
  answer is always uniform and valid, only the number of iterations is random. There is no
  finite hard bound on iterations, but the probability of many rejections decays
  geometrically, so it terminates almost surely and in O(1) expected steps.
