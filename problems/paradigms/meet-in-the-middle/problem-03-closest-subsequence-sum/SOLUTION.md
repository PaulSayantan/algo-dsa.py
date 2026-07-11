# Closest Subsequence Sum — Solution

## Brute Force

Enumerate all `2^n` subset sums and track the one nearest to `goal`.

```python
def minAbsDifference(nums, goal):
    n = len(nums)
    best = float("inf")
    for mask in range(1 << n):
        s = sum(nums[i] for i in range(n) if mask & (1 << i))
        best = min(best, abs(s - goal))
    return best
```

- **Time:** `O(2^n * n)` — `n = 40` gives `~4 * 10^13`, far too slow.
- **Space:** `O(1)`.

Because values are as large as `10^7` (and negative), a sum-indexed DP is out;
`n <= 40` is the signal for Meet in the Middle.

## Optimal Approach (Meet in the Middle)

Split `nums` into halves `L` and `R` (about 20 elements each). A full subset
sum is `leftSum + rightSum` where `leftSum` ranges over subsets of `L` and
`rightSum` over subsets of `R`. We want `leftSum + rightSum` as close to `goal`
as possible, so for a fixed `leftSum` the ideal partner is a `rightSum` closest
to `goal - leftSum`.

**Step by step**

1. Enumerate all subset sums of `L` into list `A` (`<= 2^20` values) and of `R`
   into list `B`.
2. Sort `B`.
3. For each `a` in `A`, we need a `b` in `B` minimizing `abs(a + b - goal)`,
   i.e. `b` closest to `t = goal - a`. Binary search `t` in the sorted `B`:
   the best candidate is at the insertion point or the element just before it.
   Update the running minimum with both.

```python
from bisect import bisect_left

def subset_sums(arr):
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]
    return sums

def minAbsDifference(nums, goal):
    mid = len(nums) // 2
    A = subset_sums(nums[:mid])
    B = sorted(subset_sums(nums[mid:]))
    best = float("inf")
    for a in A:
        t = goal - a                 # want b closest to t
        i = bisect_left(B, t)
        if i < len(B):               # candidate >= t
            best = min(best, abs(a + B[i] - goal))
        if i > 0:                    # candidate < t
            best = min(best, abs(a + B[i - 1] - goal))
    return best
```

Why it is correct: the empty subset (`sum = 0`) is present in both `A` and `B`,
so every combined subset — including all-of-`L`-with-none-of-`R`, etc. — is
representable. For each `a`, the value of `b` that minimizes `abs((a + b) - goal)`
is the `b` nearest to `goal - a`; in a sorted array that nearest value is always
one of the two neighbors of the binary-search insertion point. Iterating `a` over
all left sums therefore examines the global optimum.

- **Time:** `O(2^(n/2) * n)` to build the halves, `O(2^(n/2) log 2^(n/2)) =
  O(n * 2^(n/2))` to sort `B`, and `O(2^(n/2) * log 2^(n/2))` for the binary
  searches — overall `O(n * 2^(n/2))`. For `n = 40` that is a few million ops.
- **Space:** `O(2^(n/2))` for the two subset-sum lists.

## Key Insights & Edge Cases

- **Closest, not exact:** hashing (Problem 1/2) answers "does a matching value
  exist?"; here we need the *nearest* value, so the combine step becomes
  **sort + binary search** instead of a hash lookup. Check *both* neighbors of
  the insertion point — the closer one can be on either side.
- **Empty subset must be included** (`goal` far outside the reachable range,
  as in Example 3, is answered by the empty sum 0). Seeding with `[0]` handles
  it in both halves.
- **Early exit:** if `best` ever reaches 0 you can return immediately.
- **Negative numbers** are fine — sorting orders sums correctly regardless of
  sign; nothing here assumes positivity.
- **A two-pointer variant** also works: sort `A` ascending and `B` descending,
  then sweep both — but sort-plus-binary-search is easier to get right and has
  the same asymptotic cost.
