# Largest Rectangle in Histogram — Solution

## Brute Force

For each pair of left/right boundaries `(i, j)`, the tallest rectangle spanning them has
height `min(heights[i..j])` and width `j - i + 1`. Track the maximum area.

- All pairs with running min: `O(n^2)`.
- **Time:** `O(n^2)`.
- **Space:** `O(1)` beyond the input.

An alternative brute force fixes each bar as the limiting height and expands left/right while
bars are `>=` it — also `O(n^2)` in the worst case (e.g. all equal heights). Too slow for
`n` up to `10^5`.

## Optimal Approach (Monotonic Stack / Queue)

**Insight:** every candidate rectangle is limited by some bar `h = heights[k]` used as the
height. For that bar, the widest rectangle of height `h` extends:

- left until the **previous bar strictly shorter** than `h`, and
- right until the **next bar strictly shorter** than `h`.

If we know those two boundaries, the area contributed by bar `k` is
`heights[k] * (right - left - 1)`. A single **monotonic increasing stack** of indices finds
both boundaries as we scan.

### How the pass works

Maintain a stack of indices whose heights are non-decreasing from bottom to top. Iterate `i`
over the bars (and one extra sentinel step with height `0` at the end to flush the stack):

1. While the stack is non-empty **and** the current height `heights[i]` is **less than**
   `heights[stack[-1]]`, pop the top index `top`. The popped bar can extend no further right
   than `i` (exclusive) because `i` is shorter. It extends left down to the new stack top
   (exclusive). So:
   - `height = heights[top]`
   - `right boundary = i`
   - `left boundary = stack[-1]` after popping (or `-1` if the stack is now empty)
   - `width = i - left_boundary - 1`
   - update `best = max(best, height * width)`
2. Push `i`.

The sentinel `0` at index `n` guarantees every remaining bar gets popped and measured.

### Why it is correct

When we pop `top`, the current `i` is the *first* bar to its right that is shorter (that is
exactly why we are popping now), and the element beneath `top` on the stack is the *nearest*
bar to its left that is shorter (everything between them was already popped and was taller).
Hence `(left, right)` are precisely the maximal boundaries within which `heights[top]` is the
minimum — the widest rectangle of that height.

### Reference implementation

```python
def largestRectangleArea(self, heights):
    stack = []            # indices, heights non-decreasing bottom -> top
    best = 0
    n = len(heights)
    for i in range(n + 1):
        cur = heights[i] if i < n else 0   # sentinel 0 flushes the stack
        while stack and heights[stack[-1]] > cur:
            top = stack.pop()
            height = heights[top]
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, height * width)
        stack.append(i)
    return best
```

### Complexity

- **Time:** `O(n)`. Each index is pushed once and popped once.
- **Space:** `O(n)` for the stack.

## Key Insights & Edge Cases

- **Height fixed by the shortest bar:** the trick is to let each bar be the *limiting height*
  once, and find how wide a rectangle of that exact height can be.
- **Width from boundaries:** `width = right - left - 1`, where `left` is the index of the
  previous shorter bar (or `-1`) and `right = i` is the current (shorter) bar.
- **Sentinel flush:** appending a virtual bar of height `0` at the end (loop to `n`
  inclusive) forces all remaining stack entries to be measured; otherwise the tallest
  trailing bars would never be popped.
- **Equal heights:** using strict `>` on the pop means equal bars are not popped prematurely;
  the later index carries the run forward, and the sentinel resolves them all at the end with
  the correct combined width.
- **Zero-height bars** partition the histogram; a `0` immediately flushes taller bars to its
  left, which is the desired behavior.
- **Single bar** `[h]`: no pops until the sentinel, then area `h * 1 = h`.
