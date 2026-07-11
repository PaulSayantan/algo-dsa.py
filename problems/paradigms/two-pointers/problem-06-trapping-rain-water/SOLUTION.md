# Solution - Trapping Rain Water

## Brute Force

For each index, scan left and right to find the tallest walls, then add the
water it holds.

```python
total = 0
for i in range(n):
    left_max = max(height[: i + 1])
    right_max = max(height[i:])
    total += min(left_max, right_max) - height[i]
return total
```

- **Time:** `O(n^2)` — two scans per index.
- **Space:** `O(1)`.

A common `O(n)` improvement precomputes `prefixMax` and `suffixMax` arrays, but
that costs `O(n)` extra space. The two-pointer method matches `O(n)` time with
`O(1)` space.

## Optimal Approach (Two Pointers)

The water over index `i` is `min(maxLeft(i), maxRight(i)) - height[i]`. The
insight: we do not always need the *exact* value of both sides — we only need the
**smaller** of the two, and we can always be sure about the smaller side.

Maintain `left = 0`, `right = n - 1`, and running maxima `left_max`, `right_max`.
At each step compare `height[left]` and `height[right]`:

- If `height[left] < height[right]`, then `left_max` (the max on `[0, left]`) is
  provably `<= right_max` for the current window, because there is a wall at
  `right` at least as tall as `height[left]` off to the right. So the water at
  `left` is bounded by `left_max`. Update `left_max`, add `left_max - height[left]`,
  and do `left += 1`.
- Otherwise the right side is the (weakly) smaller wall, so symmetrically update
  `right_max`, add `right_max - height[right]`, and do `right -= 1`.

### Why it is correct

Water at index `i` is `min(maxLeft(i), maxRight(i)) - height[i]`. The difficulty
is normally that we do not know `maxRight(i)` while scanning left-to-right. The
two-pointer trick sidesteps this:

- Suppose `height[left] < height[right]`. Then there exists a bar at position
  `right >= left` with height `> height[left]`, so the true `maxRight(left)` is at
  least `height[right] > height[left]`. Meanwhile `left_max = maxLeft(left)`
  exactly (we have scanned all of `[0, left]`). Because `left_max <= right side`
  is guaranteed to be the binding constraint, `min(maxLeft, maxRight) = left_max`
  at `left`, and `left_max - height[left]` is the correct trapped amount. We can
  commit it and never need the right side's exact value.
- The symmetric case handles `height[left] >= height[right]`.

Every index is finalized exactly once (whichever side is smaller when the pointer
reaches it), so summing the per-index contributions gives the exact total.

### Step-by-step (height = [3, 0, 2], expected 2)

| left | right | h[left] | h[right] | left_max | right_max | add | total |
|------|-------|---------|----------|----------|-----------|-----|-------|
| 0    | 2     | 3       | 2        | —        | —         | h[left] >= h[right] → work right: right_max=max(0,2)=2, add 2-2=0 | 0 |
| 0    | 1     | 3       | 0        | —        | 2         | h[left] >= h[right] → work right: right_max=max(2,0)=2, add 2-0=2 | 2 |
| 0    | 0     | stop    |          |          |           |     | 2 |

Answer: `2`.

### Reference implementation

```python
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            total += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total += right_max - height[right]
            right -= 1
    return total
```

- **Time:** `O(n)` — each index is processed once as a pointer advances.
- **Space:** `O(1)` — four scalar variables, no prefix/suffix arrays.

## Key Insights & Edge Cases

- **You only need the smaller side.** Whichever of `height[left]`, `height[right]`
  is smaller is the one whose water is fully determined right now; that is why we
  always advance from the smaller side.
- **Update the running max before adding**, so a new tall wall contributes `0`
  (it holds no water itself) rather than a negative amount.
- **Monotonic or empty pockets** (`[1, 2, 3]`, `[5]`) trap `0`: the running max
  always equals the current bar, so each contribution is `0`.
- **Ties** (`height[left] == height[right]`): the `else` branch processes the
  right side; either choice is correct since both walls equal the binding height.
- **Endpoints never trap water**; the loop naturally handles them because their
  running max equals their own height when first visited.
