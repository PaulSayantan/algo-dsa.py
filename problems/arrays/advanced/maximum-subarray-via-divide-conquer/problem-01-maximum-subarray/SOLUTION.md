# Maximum Subarray — Solution

## Brute Force

Try every subarray `nums[i..j]` and track the maximum sum. Using a running inner
sum avoids recomputation.

```python
def maxSubArray_brute(nums):
    best = nums[0]
    for i in range(len(nums)):
        running = 0
        for j in range(i, len(nums)):
            running += nums[j]
            best = max(best, running)
    return best
```

- **Time:** `O(n^2)` — every start `i` with every end `j`.
- **Space:** `O(1)`.

A naive triple loop that re-sums each subarray from scratch is `O(n^3)`; the
running-sum version above trims it to `O(n^2)`.

## Optimal Approach (Divide & Conquer)

This is the CLRS chapter-4 recursion. It runs in `O(n log n)` — asymptotically
slower than Kadane's `O(n)`, but it is the canonical divide-and-conquer training
problem and generalizes to range queries.

**Idea.** Split the range `[lo, hi]` at `mid = (lo + hi) // 2`. Any maximum
subarray of `[lo, hi]` must fall into exactly one of three cases:

1. It lies **entirely in the left half** `[lo, mid]`.
2. It lies **entirely in the right half** `[mid+1, hi]`.
3. It **crosses the midpoint**, i.e. includes both `nums[mid]` and `nums[mid+1]`.

Cases 1 and 2 are solved by recursion. Case 3 is special: a crossing subarray is
some suffix of the left half glued to some prefix of the right half. Because the
two pieces are independent, the best crossing subarray is the *best suffix ending
at `mid`* plus the *best prefix starting at `mid+1`*. Each is found by a single
linear scan outward from the middle.

```python
def maxSubArray(nums):
    def best_crossing(lo, mid, hi):
        left = float("-inf")
        s = 0
        for i in range(mid, lo - 1, -1):   # walk left from mid
            s += nums[i]
            left = max(left, s)
        right = float("-inf")
        s = 0
        for j in range(mid + 1, hi + 1):   # walk right from mid+1
            s += nums[j]
            right = max(right, s)
        return left + right                # both halves are non-empty

    def solve(lo, hi):
        if lo == hi:
            return nums[lo]                 # base case: single element
        mid = (lo + hi) // 2
        return max(solve(lo, mid),
                   solve(mid + 1, hi),
                   best_crossing(lo, mid, hi))

    return solve(0, len(nums) - 1)
```

**Why it is correct.** The three cases are exhaustive: for any subarray `[i, j]`
either `j <= mid` (left), `i >= mid+1` (right), or `i <= mid < j` (crossing).
Recursion handles left and right optimally by induction; `best_crossing`
enumerates every crossing subarray implicitly because choosing the best suffix
and the best prefix independently maximizes their sum (the two ranges never
overlap, so the choices are separable). Taking the max over the three cases
therefore returns the global optimum for `[lo, hi]`. The base case `lo == hi`
returns the single element, which correctly handles all-negative arrays.

**Step by step on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:**

- Split repeatedly until singletons; the right sub-half `[4, -1, 2, 1, -5, 4]`
  is where the winner lives.
- Within it, the crossing/merge steps eventually surface the suffix `4` (from the
  `4, -1` region) joined with the prefix `-1, 2, 1`, producing `[4, -1, 2, 1] = 6`.
- No left-only, right-only, or other crossing candidate exceeds 6, so the answer
  bubbles up as `6`.

**Complexity.** The recurrence is `T(n) = 2T(n/2) + O(n)` (the `O(n)` is the two
crossing scans), which solves to `T(n) = O(n log n)` by the master theorem.
Space is `O(log n)` for the recursion stack.

## Key Insights & Edge Cases

- **The subarray must be non-empty.** Initialize the best with `nums[0]` (or use
  the singleton base case) so an all-negative array like `[-3, -1, -2]` returns
  `-1`, not `0`.
- **Crossing subarray always includes both `nums[mid]` and `nums[mid+1]`.** That
  is why `best_crossing` seeds each scan from those two positions and starts the
  running sum before the max, guaranteeing each half contributes at least one
  element.
- **Use `-inf`, not `0`, as the initial max** inside the crossing scan so negative
  values are handled correctly.
- **Kadane comparison:** if you only need one answer, Kadane's `O(n)` DP is
  strictly better. Reach for divide & conquer to *learn* the paradigm or when you
  later need the segment-tree merge (see problem 5).
- **Single element** (`[1]`) hits the base case immediately and returns that
  element.
