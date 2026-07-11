# Maximum Subarray With Indices — Solution

## Brute Force

Enumerate every subarray `nums[i..j]`, keep a running sum, and remember the
`(i, j, sum)` with the greatest sum.

```python
def find_brute(nums):
    best = (0, 0, nums[0])
    for i in range(len(nums)):
        running = 0
        for j in range(i, len(nums)):
            running += nums[j]
            if running > best[2]:
                best = (i, j, running)
    return best
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

## Optimal Approach (Divide & Conquer)

This is CLRS `FIND-MAXIMUM-SUBARRAY`. The structure is identical to problem 1, but
every helper now returns a `(start, end, sum)` triple so we can reconstruct the
boundaries.

**Divide.** Split `[lo, hi]` at `mid = (lo + hi) // 2`.

**Conquer.** Recurse to get the best subarray fully inside `[lo, mid]` and the
best fully inside `[mid+1, hi]`.

**Combine (`max_crossing`).** A crossing subarray must contain both `nums[mid]`
and `nums[mid+1]`. Scan left from `mid`, tracking the running sum and the index
`left_i` where the running sum was largest; that is the best suffix ending at
`mid`. Scan right from `mid+1` the same way to get `right_j`, the best prefix
starting at `mid+1`. The best crossing subarray is `(left_i, right_j,
left_sum + right_sum)`.

```python
def find_maximum_subarray(nums):
    def max_crossing(lo, mid, hi):
        s, left_sum, left_i = 0, float("-inf"), mid
        for i in range(mid, lo - 1, -1):
            s += nums[i]
            if s > left_sum:
                left_sum, left_i = s, i
        s, right_sum, right_j = 0, float("-inf"), mid + 1
        for j in range(mid + 1, hi + 1):
            s += nums[j]
            if s > right_sum:
                right_sum, right_j = s, j
        return (left_i, right_j, left_sum + right_sum)

    def solve(lo, hi):
        if lo == hi:
            return (lo, hi, nums[lo])              # base case
        mid = (lo + hi) // 2
        left = solve(lo, mid)
        right = solve(mid + 1, hi)
        cross = max_crossing(lo, mid, hi)
        # tie-break: left, then cross, then right (use >= carefully)
        best = left
        if cross[2] > best[2]:
            best = cross
        if right[2] > best[2]:
            best = right
        return best

    return solve(0, len(nums) - 1)
```

**Why it is correct.** Same three-case exhaustiveness argument as problem 1: any
subarray is left-only, right-only, or crossing. The two scans in `max_crossing`
find the optimal suffix and prefix independently, and since they occupy disjoint
index ranges their optimum sums add. Because the strict `>` comparisons in
`solve` only replace the current best on a *strict* improvement, the left
candidate is preferred over the crossing on a tie, and the crossing over the
right — giving deterministic indices.

**Step by step on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:**

- The recursion narrows onto the region around index 3–6.
- `max_crossing` around the boundary between `4` (index 3) and `-1` (index 4)
  finds the best suffix `[4]` (`left_i = 3`, sum 4) and best prefix `[-1, 2, 1]`
  (`right_j = 6`, sum 2), giving `(3, 6, 6)`.
- No competing candidate beats sum 6, so `(3, 6, 6)` is returned.

**Complexity.** `T(n) = 2T(n/2) + O(n) = O(n log n)` time, `O(log n)` stack space.

## Key Insights & Edge Cases

- **Track the index at the moment the running sum peaks**, not after the loop —
  the best suffix/prefix may end before you finish scanning.
- **Seed `left_sum`/`right_sum` with `-inf`** and start the scan *at* `mid` /
  `mid+1` so each half is guaranteed non-empty (a crossing subarray cannot be
  empty on either side).
- **Base case returns `(lo, lo, nums[lo])`**, which naturally handles the
  all-negative case `[-5, -2, -3]` → `(1, 1, -2)`.
- **Tie-breaking is a policy, not a correctness requirement.** Any maximum
  subarray is a valid answer; the strict-`>` scheme above just makes the output
  reproducible. If a grader expects a specific tie result, adjust the comparison
  operators.
- **Off-by-one traps:** `range(mid, lo - 1, -1)` includes `lo`; `range(mid + 1,
  hi + 1)` includes `hi`. Getting either bound wrong drops a valid element.
