# Solution — Largest Rectangle in Histogram

## Brute Force

For every pair of left/right boundaries `(l, r)`, the tallest rectangle you can
draw over that span is `min(heights[l..r]) * (r - l + 1)`. Iterate over all
pairs and track the running minimum.

```python
def brute(heights):
    n, best = len(heights), 0
    for l in range(n):
        h = heights[l]
        for r in range(l, n):
            h = min(h, heights[r])         # running min avoids inner scan
            best = max(best, h * (r - l + 1))
    return best
```

- **Time:** O(n²) — every pair of endpoints.
- **Space:** O(1).

For `n` up to `10^5` this is ~10^10 operations and will time out.

## Optimal Approach (Monotonic Stack)

**Key idea.** For each bar `i`, imagine it as the *limiting* (shortest) bar of a
rectangle. That rectangle extends left until it hits a bar strictly shorter than
`heights[i]`, and right until it hits a bar strictly shorter than `heights[i]`.
If `left[i]` and `right[i]` are those first-strictly-shorter boundaries, then the
best rectangle with bar `i` as the limiter has area
`heights[i] * (right[i] - left[i] - 1)`. The answer is the max over all `i`.

A **monotonic increasing stack** finds those boundaries in one pass.

Maintain a stack of indices whose heights are non-decreasing from bottom to top.
Walk `i` from left to right (append a sentinel bar of height `0` at the end so
the stack fully drains):

1. While the stack is non-empty and `heights[i] < heights[stack top]`:
   - Pop index `top`. The popped bar's height is `heights[top]`.
   - Its right boundary is `i` (first bar to the right that is shorter).
   - Its left boundary is the new stack top after popping (first bar to the left
     that is shorter), or `-1` if the stack is empty.
   - Width = `i - left - 1`. Update `best = max(best, heights[top] * width)`.
2. Push `i`.

Each index is pushed once and popped once, so the loop is O(n).

```python
def largestRectangleArea(heights):
    stack = []          # indices, heights non-decreasing bottom -> top
    best = 0
    for i, h in enumerate(heights + [0]):   # sentinel 0 drains the stack
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, heights[top] * width)
        stack.append(i)
    return best
```

**Why it is correct.** When we pop `top` because a shorter bar `i` appeared,
`i` is provably the nearest strictly-shorter bar to the right of `top` (nothing
between them was shorter, or it would have popped `top` earlier). The element
now under `top` is the nearest bar to the left that is strictly shorter (the
stack stayed non-decreasing, and any equal/taller bars in between were already
popped). So `width = i - left - 1` is exactly the maximal span over which
`heights[top]` is the minimum — the largest rectangle limited by bar `top`.
Every bar gets its turn as the limiter, so no rectangle is missed.

- **Time:** O(n) — each index pushed and popped at most once.
- **Space:** O(n) for the stack.

## Key Insights & Edge Cases

- **The sentinel `0`** appended at the end forces every remaining bar to be
  popped and evaluated; without it, bars in a strictly increasing tail never get
  measured.
- **Strict vs. non-strict comparison.** Using `>` (pop when the top is strictly
  taller than the incoming bar) means equal-height bars are left on the stack.
  That is fine: when the equal bar is eventually popped, its left boundary reaches
  back past the earlier equal bar, so the full width is still captured.
- **All-equal input** like `[3, 3, 3]` → the last bar (or sentinel) pops
  everything and yields `3 * 3 = 9`.
- **Single bar** `[5]` → area `5`. **Zeros** contribute area `0`.
- This exact routine is the inner loop of the 2D "largest all-zero submatrix":
  each row's `height[]` array is fed into `largestRectangleArea`.
