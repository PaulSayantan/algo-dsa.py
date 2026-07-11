# Count of Range Sum — Solution

## Brute Force

Enumerate every `(i, j)` pair, compute the range sum (incrementally to avoid an extra
factor), and test the bounds.

```python
def countRangeSum(nums, lower, upper):
    n = len(nums)
    count = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if lower <= s <= upper:
                count += 1
    return count
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

Correct but quadratic — too slow for `n = 10^5`.

## Optimal Approach (Coordinate Compression + Fenwick Tree)

Define prefix sums `P[0] = 0` and `P[k] = nums[0] + ... + nums[k-1]`. Then
`S(i, j) = P[j+1] - P[i]`, and a range ending at position `k = j+1` is valid iff there is an
earlier prefix index `i < k` with

```
lower <= P[k] - P[i] <= upper   <=>   P[k] - upper <= P[i] <= P[k] - lower.
```

So sweep `k` from `0` to `n`, and for each `P[k]` count how many *already-inserted* prefix
sums `P[i]` (`i < k`) fall in the window `[P[k] - upper, P[k] - lower]`, then insert `P[k]`.
That "count values in a range" query is what a Fenwick tree does — after we compress the
prefix sums to a dense index range (they span roughly `±10^14`, far too large to index
directly).

```python
import bisect

class BIT:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
    def update(self, i, delta):     # 1-based
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):             # prefix sum [1..i]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def countRangeSum(nums, lower, upper):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    coords = sorted(set(prefix))          # compress all prefix-sum values
    bit = BIT(len(coords))
    count = 0
    for p in prefix:
        lo = bisect.bisect_left(coords, p - upper)      # first coord >= p-upper
        hi = bisect.bisect_right(coords, p - lower)     # first coord > p-lower
        # inserted values with rank in (lo, hi]  ==  values in [p-upper, p-lower]
        count += bit.query(hi) - bit.query(lo)
        r = bisect.bisect_left(coords, p) + 1           # 1-based rank of p
        bit.update(r, 1)
    return count
```

**Why it is correct.**

- Processing `prefix` left to right guarantees that when we handle `P[k]` the BIT contains
  exactly `P[0..k-1]` — the legal earlier endpoints `i < k`.
- `lo = bisect_left(coords, p - upper)` and `hi = bisect_right(coords, p - lower)` translate
  the value window `[p - upper, p - lower]` into the half-open rank interval `(lo, hi]`, so
  `bit.query(hi) - bit.query(lo)` counts inserted prefix sums in that value window. Each such
  `P[i]` corresponds to exactly one valid range `S(i, k-1)`.
- Compression preserves order, so ranking is faithful, and `p - upper` / `p - lower` need not
  themselves be prefix-sum values — `bisect` still places them correctly in `coords`.

**Step by step** on `nums = [-2, 5, -1]`, `lower = -2`, `upper = 2`:

- `prefix = [0, -2, 3, 2]`, `coords = [-2, 0, 2, 3]`.
- p=0: window `[0-2, 0+2] = [-2, 2]`; BIT empty -> 0. Insert 0.
- p=-2: window `[-4, 0]`; inserted {0}, and 0 is in `[-4, 0]` -> 1. Insert -2.
- p=3: window `[1, 5]`; inserted {0, -2}, none in `[1, 5]` -> 0. Insert 3.
- p=2: window `[0, 4]`; inserted {0, -2, 3}; values 0 and 3 lie in `[0, 4]` -> 2. Insert 2.
- Total `0 + 1 + 0 + 2 = 3`.

- **Time:** `O(n log n)`.
- **Space:** `O(n)` for prefix sums, `coords`, and the BIT.

A merge-sort variant that counts qualifying pairs during the merge is also `O(n log n)` and
avoids compression; the BIT version is the direct illustration of compressing prefix sums.

## Key Insights & Edge Cases

- **Include `P[0] = 0`** among the prefix sums (and in the compressed coordinates). Ranges
  that start at index 0 depend on it; omitting it undercounts (e.g. `[0]` would give 0
  instead of 1).
- **Window mapping with bisect:** use `bisect_left` for the lower bound and `bisect_right`
  for the upper bound so the inclusive value window `[p-upper, p-lower]` becomes the correct
  half-open rank range. Mixing these up causes off-by-one errors at ties.
- **Large prefix sums:** with `n = 10^5` elements up to `2^31`, prefix sums reach ~`2*10^14`.
  A direct value-indexed BIT is impossible; compression makes the index range `O(n)`.
- **Negative numbers** are fine — prefix sums are not monotonic, which is exactly why we need
  a range-count structure rather than two-pointer or sliding window.
- Compress the set of prefix-sum *values only*; the query bounds `p - upper` and `p - lower`
  are located via binary search and do not need to be inserted.
