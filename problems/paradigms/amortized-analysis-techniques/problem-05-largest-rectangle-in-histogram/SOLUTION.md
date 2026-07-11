# Solution — Largest Rectangle in Histogram

## Brute Force

For each bar `i`, treat it as the limiting (shortest) bar and expand left and right
while bars are at least as tall as `heights[i]`; the area is `heights[i] * width`.

```python
def largestRectangleArea(heights):
    n = len(heights)
    best = 0
    for i in range(n):
        left = right = i
        while left - 1 >= 0 and heights[left - 1] >= heights[i]:
            left -= 1
        while right + 1 < n and heights[right + 1] >= heights[i]:
            right += 1
        best = max(best, heights[i] * (right - left + 1))
    return best
```

- **Time:** O(n^2) — each bar may expand across the whole array (e.g. all equal heights).
- **Space:** O(1) beyond the input.

## Optimal Approach (Amortized Analysis with a Monotonic Stack)

Keep a **stack of bar indices whose heights are non-decreasing** from bottom to top. We
scan left to right. The key observation: **the moment a bar is popped, we know both of
its boundaries** — the bar being processed is its first strictly shorter bar on the
right, and the new stack top (after popping) is its nearest shorter bar on the left. So
we can finalize the largest rectangle that has the popped bar as its limiting height.

```
push a sentinel by iterating i from 0..n (treat height[n] = 0 to flush the stack)
stack = []                       # indices, non-decreasing heights
for i in 0..n:
    cur = heights[i] if i < n else 0
    while stack and heights[stack.top()] > cur:
        h = heights[stack.pop()]
        # width spans from just after the new top to i-1
        left = stack.top() if stack not empty else -1
        width = i - left - 1
        best = max(best, h * width)
    stack.push(i)
```

Reference implementation:

```python
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[int] = []          # indices with non-decreasing heights
        best = 0
        n = len(heights)
        for i in range(n + 1):
            cur = heights[i] if i < n else 0    # trailing 0 flushes the stack
            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                best = max(best, h * width)
            stack.append(i)
        return best
```

### Why it is correct

When bar `t = stack.pop()` is removed because `heights[i] < heights[t]`:

- **Right boundary:** bar `i` is the first bar to the right that is *shorter* than
  `heights[t]`, so the rectangle of height `heights[t]` cannot extend past `i-1`.
- **Left boundary:** after popping, the new stack top `left` is the nearest bar to the
  left that is *shorter* than `heights[t]` (everything between was already popped and was
  ≥ `heights[t]`), so the rectangle can extend left only to `left+1`.

Thus `width = i - left - 1` is exactly the maximal span where `heights[t]` is the
limiting height, and `heights[t] * width` is the best rectangle capped by bar `t`. Every
bar becomes the limiting bar for some rectangle, so scanning all pops covers every
candidate. The trailing sentinel height `0` guarantees every remaining bar is popped and
evaluated.

### Why it is O(n) (the amortized argument)

The inner `while` can pop many bars in one outer step, which naively suggests O(n^2). But
by the **aggregate method**, **each index is pushed exactly once and popped exactly
once** across the whole scan. The total number of inner-loop iterations over all `i` is
therefore ≤ n. Outer loop O(n) + total pops O(n) ⇒ **O(n) total**, i.e. **O(1) amortized
per bar**.

- **Time:** O(n) total.
- **Space:** O(n) for the stack (all bars increasing is the worst case).

## Key Insights & Edge Cases

- **Popping is when you finalize an answer**, not pushing. A bar sits on the stack while
  its right boundary is still unknown; the pop supplies that boundary.
- The **sentinel** (iterating one step past the end with height 0, or appending a 0) is
  what forces every leftover bar to be resolved. Forgetting it loses rectangles that run
  to the end of the array, e.g. `[2, 4]`.
- Use `left = -1` when the stack is empty so a bar shorter than everything to its left
  correctly gets `width = i`.
- Zero-height bars naturally partition the histogram and are handled with no special
  case (a `0` pops everything taller before it).
- This structure (nearest-smaller-to-left and nearest-smaller-to-right in one pass) is a
  building block for "Maximal Rectangle" (LeetCode 85), where you run this per row.
