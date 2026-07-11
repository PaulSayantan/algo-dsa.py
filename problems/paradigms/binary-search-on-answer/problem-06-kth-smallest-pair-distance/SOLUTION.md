# Solution - Find K-th Smallest Pair Distance

## Brute Force

Compute every pairwise distance, sort them, and index.

```python
dists = sorted(abs(nums[i] - nums[j])
               for i in range(len(nums))
               for j in range(i + 1, len(nums)))
return dists[k - 1]
```

- **Time:** `O(n^2 log n)` — there are `O(n^2)` pairs and we sort them.
- **Space:** `O(n^2)` — storing all distances.

With `n` up to `10^4`, that is `~5 * 10^7` distances; materializing and sorting
them blows both the time and memory budget.

## Optimal Approach (Binary Search on Answer)

Sort `nums`. Binary-search the **distance value** `d` in the range
`[0, nums[-1] - nums[0]]`.

Define `count_le(d)` = the number of pairs with distance `<= d`. This is
**monotonically non-decreasing** in `d`, so `check(d) = (count_le(d) >= k)` flips
`False → True` exactly once. We want the **smallest** `d` with `count_le(d) >= k`
— and, as with the sorted-matrix problem, that smallest `d` is guaranteed to be an
actual pair distance (if it were not, `d - 1` would already reach the count `k`).

Counting pairs with distance `<= d` on the **sorted** array is an `O(n)` sliding
window: for each right index `j`, advance a left index `i` until
`nums[j] - nums[i] <= d`; then all `j - i` pairs `(i..j-1, j)` are within `d`.

```python
def smallestDistancePair(self, nums: List[int], k: int) -> int:
    nums.sort()
    n = len(nums)

    def count_le(d: int) -> int:
        # Number of pairs (i, j), i < j, with nums[j] - nums[i] <= d.
        count = 0
        i = 0
        for j in range(n):
            while nums[j] - nums[i] > d:
                i += 1
            count += j - i        # pairs ending at j with left index in [i, j)
        return count

    lo, hi = 0, nums[-1] - nums[0]
    while lo < hi:
        mid = (lo + hi) // 2
        if count_le(mid) >= k:    # enough pairs within mid → shrink distance
            hi = mid
        else:                     # too few → allow a larger distance
            lo = mid + 1
    return lo
```

### Why it is correct

On the sorted array, for a fixed right endpoint `j` the set of valid left
endpoints `i` (those with `nums[j] - nums[i] <= d`) is a contiguous suffix
`[i, j)`, and its left edge only moves rightward as `j` increases — so the two
pointers sweep in `O(n)` total and `count_le` is exact. Because `count_le` is
non-decreasing in `d`, the "first True" template locates the smallest feasible
`d`. That value is a genuine pair distance (a gap in the distance multiset would
make the predicate turn `True` one step earlier), so it is exactly the `k`-th
smallest distance: fewer than `k` pairs are strictly closer, and at least `k` are
within it.

### Step-by-step (Example 3: nums sorted = [1, 1, 6], k = 3)

Distances sorted: `[0, 5, 5]`; the 3rd is `5`. Range `[0, 5]`.

| lo | hi | mid | count_le(mid) | >= 3 | action |
|----|----|-----|---------------|------|--------|
| 0  | 5  | 2   | 1  (only the (1,1) pair) | no  | lo = 3 |
| 3  | 5  | 4   | 1             | no   | lo = 5 |
| 5  | 5  | —   | —             | stop | ret 5  |

Answer: `5`.

- **Time:** `O(n log n)` for the sort plus `O(n * log(maxDist))` for the search
  (each `count_le` is `O(n)`).
- **Space:** `O(1)` extra beyond the sort.

## Key Insights & Edge Cases

- **Two nested binary searches vs. sliding window:** you *can* count pairs with
  `bisect` per element (`O(n log n)` per predicate), but the two-pointer sweep is
  `O(n)` and cleaner — the sorted order guarantees the left pointer never moves
  backward.
- **Lower bound is `0`, not `1`:** duplicate values produce distance `0`, and `k`
  can legitimately select it (Examples 1 and 2).
- **The answer is always a real distance** — same gap-free argument as the
  sorted-matrix problem — so returning `lo` needs no post-processing.
- **`count_le` must count pairs, not distinct distances**, so duplicate distances
  are handled correctly (`[1,1,1]` with `k = 2` returns `0`).
- **Overflow:** distances stay within `nums` value range (`<= 10^6`), so no
  special handling is needed here; the counting variable can reach `~5 * 10^7`,
  which fits comfortably in a 64-bit integer.
