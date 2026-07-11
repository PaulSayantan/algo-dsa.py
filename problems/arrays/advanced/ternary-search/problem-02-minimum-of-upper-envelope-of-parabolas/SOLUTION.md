# Solution — Minimum of the Upper Envelope of Parabolas

## Brute Force

Sample `x` on a fine grid over `[lo, hi]` (say `10^6` points), evaluate
`g(x) = max_i f_i(x)` at each, and keep the smallest.

- **Time:** O(G · n) where `G` is the number of grid points. To hit `1e-6` accuracy on
  a range of width up to `2·10^4`, `G` must be enormous (`~10^{10}`), so this is far
  too slow — and still only approximate.
- **Space:** O(1).

The grid wastes work because `g` is convex: once you pass the valley the values only
grow. We should exploit that shape.

## Optimal Approach (Ternary Search on a real interval)

### Why the objective is unimodal

Each `f_i(x) = a_i x^2 + b_i x + c_i` with `a_i > 0` is **convex** (second derivative
`2 a_i > 0`). The **pointwise maximum of convex functions is convex**. Therefore
`g(x) = max_i f_i(x)` is convex on `[lo, hi]`, and a convex function on an interval is
**unimodal**: it decreases to a single minimum, then increases (either piece may be
empty if the min is at an endpoint). That is exactly the shape ternary search needs.

### The search

Maintain `[lo, hi]`. Each iteration place two probes at the thirds:

```
m1 = lo + (hi - lo) / 3
m2 = hi - (hi - lo) / 3
```

Evaluate `g(m1)` and `g(m2)` (each is an `O(n)` pass computing the max). For a
**minimum**:

- If `g(m1) < g(m2)`: the minimum cannot be in `(m2, hi]` (values there are at least
  `g(m2) > g(m1)` by convexity), so `hi = m2`.
- Else (`g(m1) >= g(m2)`): the minimum cannot be in `[lo, m1)`, so `lo = m1`.

Repeat for a fixed number of iterations (e.g. 200) or until `hi - lo < eps`. Each step
multiplies the interval width by `2/3`, so 200 iterations drive the width to
essentially machine precision regardless of the starting range. Return `g((lo+hi)/2)`.

### Why it is correct

By convexity, if `g(m1) < g(m2)` with `m1 < m2`, then `g` is already non-decreasing at
`m2` (it can never come back down after starting to rise), so no point to the right of
`m2` beats `g(m1)`. Discarding `(m2, hi]` cannot remove the true minimizer. The
symmetric argument justifies discarding `[lo, m1)`. Thus the minimizer always stays
inside the shrinking window.

### Reference implementation

```python
from typing import List


def eval_g(parabolas: List[List[float]], x: float) -> float:
    return max(a * x * x + b * x + c for a, b, c in parabolas)


def min_of_upper_envelope(parabolas, lo, hi):
    for _ in range(200):                     # 200 iters -> width * (2/3)^200 ~ 0
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0
        if eval_g(parabolas, m1) < eval_g(parabolas, m2):
            hi = m2
        else:
            lo = m1
    return eval_g(parabolas, (lo + hi) / 2.0)
```

- **Time:** O(n · log_{3/2}((hi-lo)/eps)) — a fixed ~200 iterations, each `O(n)`.
- **Space:** O(1).

An optional constant-factor optimization: reuse one probe/value across iterations
(golden-section search) to cut the number of `g` evaluations roughly in half.

## Key Insights & Edge Cases

- **Convexity ⇒ unimodality** is the license to use ternary search. If you cannot argue
  the objective is unimodal, do **not** apply this method — a multimodal envelope would
  break it.
- **Iteration count, not exact equality.** With floating point, never loop until
  `m1 == m2`; loop a fixed number of times or until `hi - lo < eps`. ~200 iterations of
  the `2/3` shrink is comfortably enough for `1e-9`.
- **Minimum vs. maximum:** for a minimum, discard the third on the side of the *larger*
  probe; for a maximum, discard the side of the *smaller* probe. Getting this backwards
  converges to the wrong endpoint.
- **Minimum at an endpoint** (e.g. Example 1 truncated to `[2, 10]`) is handled
  automatically: the window simply collapses toward `lo` or `hi`.
- **Ties** (`g(m1) == g(m2)`) are safe to break either way; the true minimizer lies in
  `[m1, m2]`, which both branches keep.
