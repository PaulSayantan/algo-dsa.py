# Solution — Minimum Number of Removals to Make Mountain Array

## Reframing the problem

Minimizing removals is the same as **maximizing the number of elements we
keep**, subject to the kept elements forming a mountain. If the largest
mountain subsequence has length `M`, the answer is `n - M`.

A mountain subsequence is: pick a peak index `i`, take a strictly increasing
subsequence that ends at `i`, followed by a strictly decreasing subsequence
that starts at `i`. So for every candidate peak `i`, the best mountain with
peak `i` keeps

```
LIS_left[i] + LDS_right[i] - 1
```

elements (subtract 1 because the peak is counted on both sides), **provided
both sides have length at least 2** so the peak is strictly higher than at
least one neighbor on each side (a real mountain, not a monotone run).

## Brute Force

Compute `LIS_left[i]` and `LDS_right[i]` with the classic `O(n^2)` DP:

- `LIS_left[i]` = longest strictly increasing subsequence ending at `i`
  (`1 + max(LIS_left[j])` over `j < i` with `nums[j] < nums[i]`).
- `LDS_right[i]` = longest strictly decreasing subsequence starting at `i`
  (symmetric, scanning from the right).

Then take `max` over valid peaks. Total `O(n^2)` time, `O(n)` space. This is
already fast enough for `n <= 1000`, but the LIS pieces can be done in
`O(n log n)` with patience + binary search — the intended technique.

## Optimal Approach (patience LIS both directions)

Compute the two per-index arrays with the `O(n log n)` patience method:

1. **`inc[i]`** = length of the longest strictly increasing subsequence
   ending at `i`. Do a left-to-right patience pass; when you place `nums[i]`
   at insertion position `pos` (via `bisect_left`), `inc[i] = pos + 1`.
2. **`dec[i]`** = length of the longest strictly decreasing subsequence
   starting at `i`. This is the LIS ending at `i` when scanning the array
   **from right to left**. Run the same patience pass on the reversed array;
   `dec[i] = pos + 1` for `nums[i]`'s insertion position in that pass.

Then:

```
best = max( inc[i] + dec[i] - 1 )   over all i with inc[i] >= 2 and dec[i] >= 2
answer = n - best
```

The guard `inc[i] >= 2 and dec[i] >= 2` enforces that index `i` is a genuine
interior peak with a strictly smaller element on each side, i.e. it is neither
the first nor last element of the mountain.

### Why it is correct

- Any mountain subsequence decomposes uniquely at its peak into a strictly
  increasing prefix (a candidate for `inc`) and a strictly decreasing suffix
  (a candidate for `dec`), sharing only the peak. Conversely, concatenating a
  best increasing run ending at `i` with a best decreasing run starting at `i`
  yields a valid mountain whenever both runs have length `>= 2`. So maximizing
  `inc[i] + dec[i] - 1` over valid peaks maximizes the kept length.
- The patience computation of `inc[i]`/`dec[i]` is the standard "insertion
  position + 1 = longest run ending here" fact, using `bisect_left` because
  both increase and decrease are **strict**.

### Reference implementation

```python
import bisect

def _lis_ending_lengths(arr):
    """inc[i] = length of longest strictly increasing subseq ending at i."""
    tails = []
    inc = [0] * len(arr)
    for i, x in enumerate(arr):
        pos = bisect.bisect_left(tails, x)   # strict
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
        inc[i] = pos + 1
    return inc

def minimumMountainRemovals(self, nums: List[int]) -> int:
    n = len(nums)
    inc = _lis_ending_lengths(nums)
    # dec[i] = longest strictly DECREASING subseq starting at i
    #        = LIS ending at i over the reversed array
    rev = _lis_ending_lengths(nums[::-1])
    dec = rev[::-1]

    best = 0
    for i in range(n):
        if inc[i] >= 2 and dec[i] >= 2:      # i must be an interior peak
            best = max(best, inc[i] + dec[i] - 1)
    return n - best
```

- **Time:** `O(n log n)` for both patience passes plus an `O(n)` scan.
- **Space:** `O(n)` for `inc`, `dec`, and the two `tails` buffers.

## Key Insights & Edge Cases

- **Convert "minimize removals" to "maximize kept".** This mental flip is the
  crux and recurs across many DP/greedy problems.
- **The `>= 2` guards are mandatory.** Without them a strictly increasing (or
  strictly decreasing) array would report a fake "mountain" with an empty
  side. E.g. `[1, 2, 3]` has no valid peak, so `inc[i] >= 2 and dec[i] >= 2`
  fails for every `i` and the code would keep `best = 0` — but the problem
  guarantees a valid mountain exists, so this degenerate case does not occur
  in valid inputs; the guards still protect the peak semantics.
- **Strictness everywhere:** duplicates cannot sit on the same slope, so use
  `bisect_left` in both directions.
- **Symmetry trick:** longest strictly decreasing subsequence starting at `i`
  equals the longest strictly increasing subsequence ending at `i` in the
  reversed array — reuse the exact same routine.
- Worked check: `[2,1,1,5,6,2,3,1]` → best mountain keeps 5 elements
  (`[1,5,6,3,1]`), so answer `8 - 5 = 3`.
