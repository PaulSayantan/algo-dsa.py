# Container With Most Water — Solution

## Brute Force

Try every pair of lines `(i, j)` and track the maximum area.

```python
best = 0
for i in range(len(height)):
    for j in range(i + 1, len(height)):
        best = max(best, min(height[i], height[j]) * (j - i))
return best
```

- **Time:** `O(n^2)` — all pairs.
- **Space:** `O(1)`.

For `n = 10^5` this is ~`5 * 10^9` pairs — far too slow. The two-pointer method
brings it to a single pass.

## Optimal Approach (Two Pointers, opposite ends)

Start with the **widest** container: `left = 0`, `right = n - 1`. Track
`best = 0`.

1. While `left < right`:
   - `area = min(height[left], height[right]) * (right - left)`; update
     `best = max(best, area)`.
   - **Move the shorter wall inward:** if `height[left] < height[right]`, do
     `left += 1`; otherwise `right -= 1`. (On a tie, moving either works.)
2. Return `best`.

**Why it is correct.** The area is `min(left_wall, right_wall) * width`. When we
move a pointer inward the width **always decreases by 1**. The only way to
possibly compensate for the lost width is to raise the limiting (shorter) wall,
so moving the shorter side is the only move that could yield a larger area.

Formally, suppose `height[left] <= height[right]`. Any container that keeps
`left` fixed and uses some `j < right` has width `< (right - left)` and height
`<= height[left]` (still capped by the shorter `left` wall), so its area is
strictly less than the current one. Hence no better container uses `left`, and
we may safely discard it. By always discarding the provably-dominated wall, we
examine an `O(n)` sequence of candidates that is guaranteed to contain the
optimum.

```python
def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
```

- **Time:** `O(n)` — the two pointers together take exactly `n - 1` steps.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Move the shorter side, never the taller.** Moving the taller wall can only
  keep the height the same or lower it while also shrinking the width, so it can
  never improve the result.
- **Start as wide as possible** — the initial container has maximum width, and
  every subsequent candidate trades width for a potentially taller minimum wall.
- **Ties** (`height[left] == height[right]`): moving either pointer is safe; the
  discarded wall cannot beat the current area with any narrower width.
- **Zero heights** are allowed; they simply produce zero-area containers and are
  skipped over as the pointers advance.
- Minimum input `n == 2` yields the single container `min(h0, h1) * 1`.
