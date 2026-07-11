# Solution - Container With Most Water

## Brute Force

Try every pair of lines and track the maximum area.

```python
best = 0
for i in range(n):
    for j in range(i + 1, n):
        best = max(best, min(height[i], height[j]) * (j - i))
return best
```

- **Time:** `O(n^2)` — all pairs.
- **Space:** `O(1)`.

Too slow for `n` up to `10^5`.

## Optimal Approach (Two Pointers)

Start with the **widest** container: `left = 0`, `right = n - 1`. Its area is
`min(height[left], height[right]) * (right - left)`. Record it, then decide which
pointer to move:

- **Always move the pointer at the shorter line inward.** If they tie, moving
  either works.

Repeat until `left == right`, keeping the best area seen.

### Why it is correct

The area is `min(h[left], h[right]) * width`. When we move a pointer inward the
`width` strictly decreases by 1. So to ever beat the current area we must
*increase* the limiting height `min(h[left], h[right])`.

Suppose `h[left] < h[right]`. The current pair's height is capped by `h[left]`.
Consider keeping `left` fixed and moving `right` inward to any `right' < right`:
the width shrinks and the height is still at most `h[left]` (the min can't exceed
the shorter wall `h[left]`), so **every** container that pairs `left` with an
index inside `right` has area `<= h[left] * (right - left)`, i.e. no bigger than
what we already recorded. Therefore `left` can never be part of a strictly better
container, and we may discard it by doing `left += 1`. A symmetric argument
handles `h[right] < h[left]`. Thus each move safely eliminates one line without
skipping the optimum.

### Step-by-step (height = [1, 8, 6, 2, 5, 4, 8, 3, 7])

| left | right | h[left] | h[right] | width | area | best | move                |
|------|-------|---------|----------|-------|------|------|---------------------|
| 0    | 8     | 1       | 7        | 8     | 8    | 8    | h[left] smaller → left++  |
| 1    | 8     | 8       | 7        | 7     | 49   | 49   | h[right] smaller → right-- |
| 1    | 7     | 8       | 3        | 6     | 18   | 49   | right--             |
| 1    | 6     | 8       | 8        | 5     | 40   | 49   | tie → right--       |
| 1    | 5     | 8       | 4        | 4     | 16   | 49   | right--             |
| 1    | 4     | 8       | 5        | 3     | 15   | 49   | right--             |
| 1    | 3     | 8       | 2        | 2     | 4    | 49   | right--             |
| 1    | 2     | 8       | 6        | 1     | 6    | 49   | right--             |
| 1    | 1     | —       | —        | stop  |      | 49   |                     |

Answer: `49`.

### Reference implementation

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

- **Time:** `O(n)` — the pointers move a combined `n - 1` steps.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Move the shorter wall.** This is the crux: moving the taller wall can never
  help because the shorter wall still caps the height while the width shrinks.
- **Tie-breaking** (`height[left] == height[right]`): moving either pointer is
  safe; both candidate lines are individually dominated by the recorded area.
- **The greedy start from maximum width** is what lets the argument work — we
  give up width only when forced, and only for a chance at more height.
- **Flat arrays** like `[1, 1]` still work: width `1`, height `1`, area `1`
  (Example 2).
- **Zero heights** contribute area `0` but are handled uniformly by the `min`.
