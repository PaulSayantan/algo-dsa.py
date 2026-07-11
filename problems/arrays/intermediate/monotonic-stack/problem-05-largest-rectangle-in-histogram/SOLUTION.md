# Largest Rectangle in Histogram — Solution

## Brute Force

Fix a starting bar `i`, extend a range to the right, and track the running
minimum height; the area for range `[i, j]` is `min_height * (j - i + 1)`.

```python
def brute(heights):
    n = len(heights)
    best = 0
    for i in range(n):
        min_h = heights[i]
        for j in range(i, n):
            min_h = min(min_h, heights[j])
            best = max(best, min_h * (j - i + 1))
    return best
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

## Optimal Approach (Monotonic Stack)

The rectangle whose height equals `heights[i]` is as wide as possible when it
extends left and right until it hits a bar **strictly shorter** than
`heights[i]`. If `left[i]` is the index of the nearest strictly shorter bar on
the left and `right[i]` the nearest strictly shorter bar on the right, then the
best rectangle using bar `i` as its limiting height has

```
width = right[i] - left[i] - 1
area  = heights[i] * width
```

An **increasing** monotonic stack of indices computes both boundaries in one
pass. Keep indices whose heights are non-decreasing bottom to top. When a bar
`i` is shorter than the stack top, the top's *right* boundary is `i`, and after
popping it, its *left* boundary is the new stack top. Using a trailing sentinel
of height `0` flushes everything at the end.

```python
def optimal(heights):
    stack = []          # indices, heights increasing bottom -> top
    best = 0
    # Append a sentinel 0-height bar so every real bar gets popped.
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            top = stack.pop()
            height = heights[top]
            # left boundary is the new top (or -1 if stack empty)
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, height * width)
        stack.append(i)
    return best
```

### Why it is correct

When bar `i` triggers a pop of `top`, we have found `top`'s nearest strictly
shorter bar on the **right** (that is `i`, since we pop while
`heights[top] >= h`). The element now on top of the stack is `top`'s nearest
strictly shorter bar on the **left**, because everything between them was already
popped (they were all `>= heights[top]`). So `width = i - left - 1` is exactly the
maximal span where `heights[top]` is the limiting height. Every bar becomes the
limiting height of some maximal rectangle, and we evaluate each such rectangle
exactly once. The sentinel `0` at the end is shorter than any real bar, forcing
all remaining bars to be popped and measured.

### Step-by-step on `[2, 1, 5, 6, 2, 3]` (sentinel 0 appended at index 6)

| i | h | pops (top: height, width -> area)           | best | stack after |
|---|---|---------------------------------------------|------|-------------|
| 0 | 2 | —                                           | 0    | [0]         |
| 1 | 1 | 0: h=2, w=1-(-1)-1=1 -> 2                    | 2    | [1]         |
| 2 | 5 | —                                           | 2    | [1,2]       |
| 3 | 6 | —                                           | 2    | [1,2,3]     |
| 4 | 2 | 3: h=6,w=4-2-1=1->6; 2: h=5,w=4-1-1=2->10   | 10   | [1,4]       |
| 5 | 3 | —                                           | 10   | [1,4,5]     |
| 6 | 0 | 5:h=3,w=6-4-1=1->3; 4:h=2,w=6-1-1=4->8; 1:h=1,w=6-(-1)-1=6->6 | 10 | [6] |

Maximum area is `10`.

- **Time:** `O(n)` — each index is pushed once and popped once.
- **Space:** `O(n)` for the stack.

## Key Insights & Edge Cases

- Storing **indices** (not heights) is essential to recover the width from the
  gap between boundaries.
- The trailing sentinel of height `0` (or a final loop that flushes the stack
  with `i = n`) is what handles bars still on the stack at the end — a common
  bug source if omitted.
- Using `>=` when popping merges equal-height bars naturally; the widths still
  come out correct because a later equal bar recomputes the full width when it
  is itself popped.
- Bars of height `0` split the histogram into independent segments; the algorithm
  handles this automatically.
- This routine is the core subroutine for **Maximal Rectangle** (LeetCode 85),
  applied row by row.
