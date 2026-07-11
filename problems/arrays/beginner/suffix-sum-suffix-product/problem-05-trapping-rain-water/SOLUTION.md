# Solution — Trapping Rain Water

## Brute Force

For each bar `i`, scan left to find the tallest bar on the left and scan right to
find the tallest bar on the right. The water above `i` is
`min(leftMax, rightMax) - height[i]` (never negative).

```python
def trap(height):
    n = len(height)
    total = 0
    for i in range(n):
        left_max = max(height[:i + 1])
        right_max = max(height[i:])
        total += min(left_max, right_max) - height[i]
    return total
```

- **Time:** O(n^2) — two scans per bar.
- **Space:** O(1) extra.

## Optimal Approach (Prefix Max + Suffix Max)

The two inner scans recompute the same maxima over and over. Precompute them
once:

- `leftMax[i]` = tallest bar in `height[0..i]` — a **prefix maximum**.
- `rightMax[i]` = tallest bar in `height[i..n-1]` — a **suffix maximum**.

A suffix maximum is just a suffix aggregate where the combining operation is
`max` instead of `+`. Once both arrays exist, the water above bar `i` is
`min(leftMax[i], rightMax[i]) - height[i]`.

Reference implementation:

```python
def trap(height):
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max = [0] * n
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):          # suffix max: build right to left
        right_max[i] = max(right_max[i + 1], height[i])

    total = 0
    for i in range(n):
        total += min(left_max[i], right_max[i]) - height[i]
    return total
```

**Why it is correct:** Water at column `i` can rise no higher than the shorter of
the two tallest walls surrounding it — any higher and it would spill over the
shorter wall. `leftMax[i]` and `rightMax[i]` are exactly those tallest walls
(inclusive of `i`, so `min(leftMax[i], rightMax[i]) >= height[i]` always, keeping
each term non-negative). Subtracting `height[i]` gives the water depth resting on
that column; summing over all columns gives the total.

**Step by step** for `height = [4, 2, 0, 3, 2, 5]`:

```
left_max  = [4, 4, 4, 4, 4, 5]     (prefix max, left to right)
right_max = [5, 5, 5, 5, 5, 5]     (suffix max, right to left)

i : min(left,right) - height
0 : min(4,5) - 4 = 0
1 : min(4,5) - 2 = 2
2 : min(4,5) - 0 = 4
3 : min(4,5) - 3 = 1
4 : min(4,5) - 2 = 2
5 : min(5,5) - 5 = 0

total = 0 + 2 + 4 + 1 + 2 + 0 = 9
```

- **Time:** O(n) — three linear passes.
- **Space:** O(n) for the two auxiliary arrays.

## Key Insights & Edge Cases

- A **suffix maximum** is the same construction as a suffix sum with `+` swapped
  for `max` (and the identity swapped from `0` to `-infinity`, though seeding with
  `height[n-1]` works since heights are non-negative). Recognizing "I need the max
  to the right of every index" is the cue to build a suffix aggregate.
- **O(1) extra space variant:** two pointers moving inward while tracking a
  running `leftMax` and `rightMax` collapse the two arrays into two scalars. The
  side with the smaller running max is safe to process because that side's bound
  is already fixed.
- **No trapping cases:** monotonic arrays (strictly increasing or decreasing),
  arrays of length `<= 2`, and flat arrays trap `0` water; each term is `0`
  because one of the bounding maxima equals `height[i]`.
- Because `leftMax[i]` and `rightMax[i]` both include index `i`, every per-column
  term is guaranteed `>= 0`, so no explicit clamping to `0` is needed.
