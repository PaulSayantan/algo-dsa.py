# Solution — Trapping Rain Water

## Brute Force

For each bar `i`, scan left to find the tallest bar on the left and scan right to
find the tallest on the right, then add the water it holds.

```python
def trap(height):
    n = len(height)
    total = 0
    for i in range(n):
        left_max = max(height[:i + 1])   # tallest from 0..i
        right_max = max(height[i:])      # tallest from i..n-1
        total += min(left_max, right_max) - height[i]
    return total
```

- **Time:** O(n^2) — each bar rescans both sides.
- **Space:** O(1) extra (ignoring the slices).

## Optimal Approach (Prefix-Max + Suffix-Max)

The water above bar `i` depends on information from **both** directions:

```
water(i) = min(left_max[i], right_max[i]) - height[i]
```

where `left_max[i]` is the tallest bar in `height[0..i]` and `right_max[i]` is the
tallest in `height[i..n-1]`. These are a **prefix maximum** and a **suffix maximum** —
each buildable in one pass. Because `max` is not invertible (you cannot recover it by
subtraction from a total), we must keep **both** arrays rather than deriving one from
a running total, then combine them per index. This is the archetypal
"prefix pass + suffix pass, merge at each index" problem.

### Two-array version (clearest)

```python
def trap(height):
    n = len(height)
    if n == 0:
        return 0
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
```

**Why it is correct.** Water rests at the level of the shorter of the two enclosing
walls. `left_max[i]` and `right_max[i]` (which *include* bar `i`) are exactly those
two walls, so `min(...) - height[i]` is the water depth above bar `i`; it is never
negative because both maxima are at least `height[i]`. Summing over all bars gives
the total.

**Step by step** on `[4, 2, 0, 3, 2, 5]`:

```
index      0  1  2  3  4  5
height     4  2  0  3  2  5
left_max   4  4  4  4  4  5
right_max  5  5  5  5  5  5
min        4  4  4  4  4  5
water      0  2  4  1  2  0     -> total = 9
```

- **Time:** O(n) — three linear passes.
- **Space:** O(n) for the two arrays.

### O(1) space — two-pointer collapse (follow-up)

You do not need the full arrays. Walk two pointers inward while tracking the running
left-max and right-max; process the side whose running max is smaller, because that
side's max is guaranteed to bound the water there.

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    total = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            total += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total += right_max - height[right]
            right -= 1
    return total
```

**Why it is correct.** When `height[left] < height[right]`, the right side has *some*
bar at least as tall as `height[right] > height[left]`, so the true right-max is at
least `left_max`. Hence `min(left_max, true_right_max) = left_max`, and the water at
`left` is determined solely by `left_max`. The symmetric argument holds for the right
side. Each pointer moves inward once, giving O(n) time and O(1) space.

## Key Insights & Edge Cases

- **Prefix-max / suffix-max, not prefix-sum.** The `total - prefix` shortcut (used in
  Find Pivot Index) does not apply because `max` has no inverse. When the combining
  operation is non-invertible you *must* keep both a prefix and a suffix array — this
  is the defining trait of the two-sided precomputation pattern.
- The maxima **include** the current bar. Because of that, `min(left_max[i],
  right_max[i]) >= height[i]`, so the per-bar water is always `>= 0` and no explicit
  clamp is needed in the array version.
- Boundary bars (`i = 0`, `i = n-1`) trap nothing: one side's max equals the bar
  itself, so the contribution is `0`.
- Monotonic arrays like `[1, 2, 3]` or `[3, 2, 1]` trap `0` — there is never a taller
  wall on the downhill side.
- The two-pointer version is the interview-favorite optimal answer: O(n) time, O(1)
  space, and it is directly derived from the prefix-max/suffix-max idea.
