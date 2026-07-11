# Solution — Trapping Rain Water

## Brute Force

For each position `i`, the water above it is
`min(maxLeft(i), maxRight(i)) - height[i]` (clamped at 0). Compute the two maxima by
scanning both directions for every index.

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

- **Time:** O(n^2) — a full left/right scan per index.
- **Space:** O(1) beyond the input (ignoring the slices).

(A standard O(n) refinement precomputes prefix-max and suffix-max arrays in O(n) time and
O(n) space; the monotonic-stack version below is the amortized-analysis showcase and uses
the same asymptotic time.)

## Optimal Approach (Amortized Analysis with a Monotonic Stack)

Keep a **stack of bar indices whose heights are non-increasing** from bottom to top. Scan
left to right. When the current bar `height[i]` is **taller** than the bar at the stack
top, it can act as a **right wall**: pop the top (the floor of a basin) and, if a bar
remains on the stack, that bar is the **left wall**. Water sits between them at level
`min(leftWall, rightWall)` above the popped floor.

```
stack = []                        # indices, non-increasing heights
total = 0
for i in range(n):
    while stack and height[i] > height[stack.top()]:
        floor = stack.pop()
        if stack is empty:
            break                  # no left wall -> no water
        left = stack.top()
        width = i - left - 1
        bounded_height = min(height[left], height[i]) - height[floor]
        total += width * bounded_height
    stack.push(i)
return total
```

Reference implementation:

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack: list[int] = []        # indices, non-increasing heights
        total = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                floor = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                bounded = min(height[left], h) - height[floor]
                total += width * bounded
            stack.append(i)
        return total
```

### Why it is correct

The stack holds descending "walls" that could bound water to their right. When a taller
bar `i` appears, every stack bar shorter than it can no longer hold back water on its
right, so we settle those basins immediately. For a popped `floor` with left wall `left`
and right wall `i`:

- Water depth above the floor is `min(height[left], height[i]) - height[floor]` — bounded
  by the shorter of the two walls.
- Horizontal width is `i - left - 1`.

We add water **layer by layer** as successive floors are popped, which correctly
accumulates the volume of a wide, stepped basin. If the stack becomes empty while popping,
there is no left wall, so no water is trapped there and we stop.

### Why it is O(n) (the amortized argument)

A single tall bar might pop many basins, hinting at O(n^2). But by the **aggregate
method**, **each index is pushed exactly once and popped at most once** over the entire
scan. Hence the total number of inner-loop iterations across all `i` is ≤ n. Outer loop
O(n) + total pops O(n) ⇒ **O(n) total**, i.e. **O(1) amortized per bar**.

- **Time:** O(n) total.
- **Space:** O(n) for the stack (a non-increasing prefix like `[5,4,3,2,1]` stacks
  everything).

## Key Insights & Edge Cases

- **Water is settled on a pop**, when both walls are known — the same "finalize on pop"
  pattern as Largest Rectangle in Histogram.
- The `if not stack: break` guard handles the case where the popped floor has no bar to
  its left (nothing can hold the water), preventing an index error and a wrong count.
- Equal heights: use strict `>` so equal bars stack without prematurely settling zero-
  depth water; they get resolved when a strictly taller bar arrives.
- Monotonic arrays (all increasing or all decreasing) trap `0` water and are handled
  naturally.
- The two-pointer method (`left`/`right` pointers moving inward, tracking `left_max` and
  `right_max`) is the O(1)-space alternative and is also amortized O(n) because each
  pointer only moves forward — another instance of the "forward-only pointer" amortized
  bound.
