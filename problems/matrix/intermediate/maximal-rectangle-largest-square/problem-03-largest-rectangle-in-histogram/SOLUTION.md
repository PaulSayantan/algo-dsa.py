# Largest Rectangle in Histogram — Solution

## Brute Force

For each pair of left/right boundaries `(l, r)`, the rectangle height is
`min(heights[l..r])` and the area is `height * (r - l + 1)`. Take the max over all pairs.

- **Time:** `O(n^2)` if you extend `r` from each `l` and track the running minimum
  (`O(n^3)` if you recompute the min from scratch each time).
- **Space:** `O(1)`.

An alternative `O(n log n)` divide-and-conquer splits at the minimum bar, but the stack
solution below is both faster and simpler to reason about.

## Optimal Approach (Monotonic Increasing Stack)

For each bar `i`, the largest rectangle using bar `i` as its limiting (shortest) height
extends left to the first bar shorter than `heights[i]` and right to the next bar shorter
than `heights[i]`. If we knew, for every bar, its "previous smaller" and "next smaller"
boundaries, the answer would be
`max_i heights[i] * (nextSmaller[i] - prevSmaller[i] - 1)`.

A **monotonic increasing stack** computes these boundaries in one pass. We keep a stack of
bar indices whose heights are strictly increasing. When the current bar `i` is *shorter* than
the bar on top of the stack, that top bar can no longer extend to the right — bar `i` is its
"next smaller". We pop it and resolve its rectangle immediately.

**Why it is correct.** When we pop index `top`:
- The **right boundary** is the current index `i` (first bar to the right that is shorter).
- The **left boundary** is the new stack top after popping (the nearest bar to the left that
  is still shorter than `heights[top]`, since everything between was taller and got popped
  earlier).
- So the width is `i - stack[-1] - 1` (or `i` if the stack is now empty, meaning nothing to
  the left is shorter). Multiplying by `heights[top]` gives the maximal rectangle with `top`
  as its shortest bar. Every bar is pushed and popped exactly once, so every candidate height
  is considered exactly once.

**Sentinel trick.** Append a virtual bar of height `0` at the end (and optionally treat an
empty stack as boundary `-1`) so the stack is guaranteed to fully drain and all pending bars
get resolved.

**Step by step.**
1. Initialize an empty index stack and `best = 0`.
2. Iterate `i` from `0` to `n` (inclusive), using height `0` for the virtual index `n`.
3. While the stack is non-empty and the current height is less than the height at the stack
   top, pop `top`, compute `width = i - stack[-1] - 1` (or `i` if the stack is empty), and
   update `best`.
4. Push `i`.
5. Return `best`.

```python
def largestRectangleArea(heights):
    stack = []          # indices with strictly increasing heights
    best = 0
    n = len(heights)
    for i in range(n + 1):
        h = 0 if i == n else heights[i]
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, heights[top] * width)
        stack.append(i)
    return best
```

- **Time:** `O(n)` — each index is pushed once and popped once.
- **Space:** `O(n)` for the stack.

## Key Insights & Edge Cases

- **The pop is the "aha".** Popping a bar is the moment you have discovered *both* its left
  and right smaller-boundaries, so you can finalize its best rectangle right then.
- **Strict vs. non-strict comparison.** Using `>` (pop when top is strictly taller) with the
  left boundary read as the post-pop stack top handles equal heights correctly — equal bars
  simply extend the width naturally without over/undercounting.
- **Sentinel.** The trailing `0` height forces every remaining bar off the stack; without it
  you must drain the stack in a separate loop.
- **Zero-height bars** act as natural cut points (width contributions become 0), so they need
  no special handling.
- **Single bar / all equal heights** are handled uniformly by the same loop.
- **This subroutine powers Problem 5 (Maximal Rectangle):** run it once per row over the
  column heights.
