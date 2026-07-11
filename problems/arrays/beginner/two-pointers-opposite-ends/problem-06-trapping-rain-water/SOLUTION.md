# Trapping Rain Water — Solution

## Brute Force

For each index `i`, water trapped there is
`min(maxLeft, maxRight) - height[i]` (clamped at 0), where `maxLeft` /
`maxRight` are the tallest bars to the left/right (inclusive). Compute those
maxima by scanning outward for every index.

```python
total = 0
for i in range(len(height)):
    left_max = max(height[: i + 1])
    right_max = max(height[i:])
    total += min(left_max, right_max) - height[i]
return total
```

- **Time:** `O(n^2)` — a full scan of both sides per index.
- **Space:** `O(1)`.

### Precomputed-arrays improvement

Precompute `maxLeft[]` and `maxRight[]` in two passes, then sum in a third:

- **Time:** `O(n)`.
- **Space:** `O(n)` for the two auxiliary arrays.

The two-pointer method achieves the same `O(n)` time using only `O(1)` space.

## Optimal Approach (Two Pointers, opposite ends)

Maintain `left = 0`, `right = n - 1`, plus running maxima `left_max` and
`right_max` (both start at 0). The insight: the water over a bar depends on
`min(overall left max, overall right max)`, and we can commit to whichever side
currently has the **smaller running max** without knowing the far side exactly.

1. While `left < right`:
   - If `height[left] < height[right]`: the left side is the limiting wall.
     - If `height[left] >= left_max`, update `left_max = height[left]` (this bar
       is a new left boundary, traps nothing itself).
     - Else add `left_max - height[left]` to the total.
     - `left += 1`.
   - Else (`height[right] <= height[left]`): the right side is limiting.
     - If `height[right] >= right_max`, update `right_max = height[right]`.
     - Else add `right_max - height[right]` to the total.
     - `right -= 1`.
2. Return the accumulated total.

**Why it is correct.** Suppose `height[left] < height[right]`. Then there exists
a bar on the right (namely `right`, or something taller found earlier) that is at
least `height[left]`, so the **right boundary for every index `<= left` is
guaranteed to be `>= left_max`**. Hence the true limiting wall for the current
`left` bar is exactly `left_max`, and the water it holds is precisely
`left_max - height[left]`. We can therefore finalize the left bar's contribution
immediately, without knowing the exact right-hand maximum. The symmetric argument
handles the other branch. Because we always process the side with the smaller
running max, the "other side is at least as tall" guarantee always holds.

```python
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total += right_max - height[right]
            right -= 1
    return total
```

- **Time:** `O(n)` — each bar is visited once as a pointer moves inward.
- **Space:** `O(1)` — four scalars, no auxiliary arrays.

## Key Insights & Edge Cases

- **Process the smaller side.** Comparing `height[left]` and `height[right]`
  tells you which running max is *definitely* the binding constraint, letting you
  commit that bar's water immediately. This is the crux that makes `O(1)` space
  possible.
- **Boundary bars trap nothing** — when the current bar is itself a new running
  maximum, it raises the wall rather than holding water.
- **Monotonic maps** (`[1, 2, 3]` or `[3, 2, 1]`) trap `0` water; the "new max"
  branch fires every step.
- **Flat maps** (`[2, 2, 2]`) trap `0` as well.
- **Single bar / two bars** (`n <= 2`) cannot form a basin → `0`.
- Use consistent tie-breaking (here the `else` branch handles
  `height[right] == height[left]`) so no bar is double-counted or skipped.
