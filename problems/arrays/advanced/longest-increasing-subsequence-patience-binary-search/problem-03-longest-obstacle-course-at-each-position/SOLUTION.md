# Solution — Longest Obstacle Course at Each Position

## Brute Force

For each index `i`, run the `O(i)` dynamic program that computes the longest
non-decreasing subsequence ending at `i`: `dp[i] = 1 + max(dp[j])` over all
`j < i` with `obstacles[j] <= obstacles[i]`. Doing this for every `i` gives
the whole answer array.

- **Time:** `O(n^2)`. With `n` up to `10^5` that is `10^10` operations — far
  too slow.
- **Space:** `O(n)`.

## Optimal Approach (patience LIS, non-decreasing variant)

This is the LIS patience algorithm, except we output the *insertion position*
at every step instead of only the final length. Crucially the course is
**non-decreasing** (equal heights are allowed), so we must use an
**upper-bound** search, `bisect_right`, rather than `bisect_left`.

Maintain `tails`, where `tails[L]` is the smallest possible tail of a
non-decreasing subsequence of length `L + 1` among the elements seen so far.
For each height `h = obstacles[i]`:

1. `pos = bisect_right(tails, h)` — the number of existing tails that are
   `<= h`. This equals the length of the longest non-decreasing course we can
   append `h` to, minus... precisely: `pos` is the index where `h` belongs,
   and the resulting course length is `pos + 1`.
2. Record `ans[i] = pos + 1`.
3. If `pos == len(tails)`, append `h` (new longest course / new pile).
   Otherwise set `tails[pos] = h` (shrink the tail of that length).

### Why `bisect_right` (not `bisect_left`)

The course allows equal heights (`>=`). If we used `bisect_left`, an equal
value would land on the leftmost `>= h` slot and be treated as if it could not
follow an equal predecessor, undercounting. `bisect_right` places `h` after
all equal values, so a run like `[2, 2]` correctly yields course lengths
`[1, 2]`. In example 2 the second `2` gives `bisect_right([2], 2) = 1`, so
`ans = 2`. Correct.

### Why it is correct

`tails` stays sorted (non-decreasing) throughout, which is what makes the
binary search valid. `tails[L]` being the minimal achievable tail for length
`L + 1` is the same greedy invariant as ordinary LIS: keeping tails as small
as possible maximizes future extendability and never loses an optimum. The
position where `h` is inserted is, by definition of `tails`, one more than the
length of the best non-decreasing course among earlier elements whose tail is
`<= h`; appending `h` to that course and ending at `i` gives `ans[i]`. Because
we process indices in order, only elements at indices `< i` are in `tails`
when we compute `ans[i]`, so the "ends at `i`, uses only `0..i`" requirement
is respected.

### Reference implementation

```python
import bisect

def longestObstacleCourseAtEachPosition(self, obstacles):
    tails = []
    ans = []
    for h in obstacles:
        pos = bisect.bisect_right(tails, h)   # non-decreasing => upper bound
        ans.append(pos + 1)
        if pos == len(tails):
            tails.append(h)
        else:
            tails[pos] = h
    return ans
```

- **Time:** `O(n log n)` — one binary search per element.
- **Space:** `O(n)` for `tails` and the output array.

## Key Insights & Edge Cases

- **Non-decreasing vs strictly increasing** is the whole trick: swap
  `bisect_left` ↔ `bisect_right`. This is the single most common LIS variant
  bug, so internalize it.
- **Answer is per-index.** Unlike LC 300, we do not want a single number; the
  insertion position at step `i` *is* the answer for `i`, so no extra pass is
  needed.
- **`ans[i] >= 1` always**, since the course can always be just `obstacles[i]`
  itself (`bisect_right` returns `0` for a value smaller than all tails, giving
  `ans = 1`).
- **Large heights (up to `10^7`)** need no special handling; comparisons are
  value-based.
- **Single element** returns `[1]`.
