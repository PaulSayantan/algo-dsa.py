# Solution — Maximum Points You Can Obtain from Cards

## Brute Force

You take some number `i` of cards from the front and `k - i` from the back, for
`i = 0..k`. Enumerate all `k + 1` splits and, for each, sum the chosen front and back
cards, tracking the maximum.

```python
n = len(cardPoints)
best = 0
for i in range(k + 1):
    front = sum(cardPoints[:i])
    back = sum(cardPoints[n - (k - i):]) if k - i > 0 else 0
    best = max(best, front + back)
return best
```

Recomputing the sums with slicing costs O(k) per split.

- **Time:** O(k²) (or O(k) with prefix sums).
- **Space:** O(1) (O(n) if you materialize prefix sums).

This works, but the sliding-window framing below is cleaner and generalizes the
fixed-window idea to a **complement**.

## Optimal Approach (Sliding Window, Fixed Size — on the Complement)

Key reframing: whatever `k` cards you take from the two ends, the cards you **leave
behind** always form **one contiguous block in the middle** of length `n - k`. Your
score is `total_sum − (sum of the leftover block)`. To maximize the score, you
**minimize** the leftover block's sum. That leftover block has a **fixed size**
`w = n - k`, so finding its minimum sum is exactly a fixed-size sliding-window problem.

1. Let `total = sum(cardPoints)` and `w = n - k`.
2. **Edge case:** if `w == 0`, you take every card → return `total`.
3. Compute `window_sum = sum(cardPoints[0..w-1])`; set `min_sum = window_sum`.
4. Slide a window of width `w` across the array: for `right` from `w` to `n - 1`,
   `window_sum += cardPoints[right] - cardPoints[right - w]` and
   `min_sum = min(min_sum, window_sum)`.
5. Return `total - min_sum`.

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        w = n - k
        total = sum(cardPoints)
        if w == 0:
            return total
        window_sum = sum(cardPoints[:w])
        min_sum = window_sum
        for right in range(w, n):
            window_sum += cardPoints[right] - cardPoints[right - w]
            min_sum = min(min_sum, window_sum)
        return total - min_sum
```

**Why it is correct:** Every legal selection of `k` end-cards leaves exactly one
contiguous middle block of length `w = n - k`, and conversely every contiguous block of
length `w` corresponds to a legal selection (take everything to its left and right).
So the set of achievable scores is `{ total − (sum of any length-w block) }`.
Maximizing the score ⇔ minimizing the block sum. The fixed-size window enumerates every
length-`w` block once and tracks the minimum, so `total − min_sum` is optimal.

**Step by step** on `cardPoints = [1,2,3,4,5,6,1], k = 3`, so `total = 22`, `w = 4`:

1. First window `[1,2,3,4]` → `window_sum = 10`, `min_sum = 10`.
2. `right=4`: `10 + 5 - 1 = 14` (window `[2,3,4,5]`), `min_sum = 10`.
3. `right=5`: `14 + 6 - 2 = 18` (window `[3,4,5,6]`), `min_sum = 10`.
4. `right=6`: `18 + 1 - 3 = 16` (window `[4,5,6,1]`), `min_sum = 10`.

Answer: `22 - 10 = 12`.

## Key Insights & Edge Cases

- **The complement trick** turns "pick from two ends" (which looks like two moving
  pointers) into a single fixed-size window over the middle — much simpler to reason
  about and code.
- **`w == 0` (`k == n`)**: you take all cards; there is no leftover block, so return
  `total` directly. Skipping this check would make the loop and the first
  `sum(cardPoints[:0]) = 0` produce `total - 0 = total` as well, but handling it
  explicitly is clearer and avoids an empty-window edge case.
- **`k == 1`** or small `k`: `w = n - 1`, still one contiguous window — no special
  casing needed.
- **Initialize `min_sum` from the first window**, not `0`; card points are positive so
  `0` would be an incorrect (too-small) lower bound and inflate the score.
- Complexity: **O(n)** time (one pass to total, one pass to slide) and **O(1)** extra
  space.
