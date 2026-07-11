# Reverse Pairs — Solution

## Brute Force

Check every pair `(i, j)` with `i < j` and count those with `nums[i] > 2 * nums[j]`.

- **Time:** O(n²) — ~2.5·10⁹ for n = 5·10⁴, too slow.
- **Space:** O(1).

The classic optimal solutions are **merge sort** (count cross-pairs while merging) and the
**Fenwick Tree** approach below; both are O(n log n).

## Optimal Approach (Binary Indexed Tree / Fenwick Tree)

Sweep left to right. Maintain a frequency BIT over the **values seen so far**. When we reach
index `j`, every value already in the BIT sits at some index `i < j`. We want to count those
with `nums[i] > 2 * nums[j]`. So:

1. **Before inserting `nums[j]`**, query how many inserted values are `> 2 * nums[j]`, and
   add that to the answer.
2. **Then insert `nums[j]`** so it is available for later `j' > j`.

Because values can be as large as `2^31 - 1` and we compare against `2 * nums[j]`, the raw
value range is too big for a direct value-indexed tree — use **coordinate compression**.

**The subtle part: two different lookups.** We insert *values* `nums[k]`, but we query
against *thresholds* `2 * nums[j]`. Compress **both** the values and the doubled values into
one sorted list of coordinates so the BIT index space covers every quantity we ever compare.

**Algorithm.**

1. Build `coords = sorted(set(nums))` and, for querying, use binary search into `coords`.
2. Create a BIT of size `len(coords)`.
3. For `j` from `0` to `n - 1`:
   - We need the count of inserted values `v` with `v > 2 * nums[j]`. Let `k` = number of
     coordinates that are `<= 2 * nums[j]` (via `bisect_right(coords, 2 * nums[j])`). Then
     `answer += inserted_so_far - prefix(k)`, where `prefix(k)` counts inserted values with
     rank `<= k` (i.e. value `<= 2*nums[j]`).
   - Insert `nums[j]`: find its rank `r = bisect_left(coords, nums[j]) + 1`, `add(r, 1)`,
     and increment `inserted_so_far`.

**Why it is correct.** At step `j` the BIT holds exactly `{nums[i] : i < j}`. The count of
those strictly greater than `2 * nums[j]` is `(#inserted) - (#inserted <= 2*nums[j])`, which
the BIT computes as `inserted_so_far - prefix(rank_of_threshold)`. Summing over all `j`
counts every ordered pair `(i, j)` with `i < j` and `nums[i] > 2*nums[j]` exactly once.

**Reference implementation:**

```python
from bisect import bisect_left, bisect_right

class Solution:
    def reversePairs(self, nums):
        coords = sorted(set(nums))       # compress the *values* we insert
        m = len(coords)
        tree = [0] * (m + 1)

        def add(i):
            while i <= m:
                tree[i] += 1
                i += i & (-i)

        def prefix(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        answer = 0
        inserted = 0
        for x in nums:
            # count already-inserted values > 2*x
            k = bisect_right(coords, 2 * x)   # coords with value <= 2*x
            answer += inserted - prefix(k)
            # insert x
            r = bisect_left(coords, x) + 1    # 1-based rank of x
            add(r)
            inserted += 1
        return answer
```

- **Time:** O(n log n) — the sort/compression plus one query and one update per element.
- **Space:** O(n) for the BIT and coordinate list.

## Key Insights & Edge Cases

- **Query the threshold, insert the value.** These are two distinct quantities
  (`2 * nums[j]` vs `nums[i]`). Compress values for insertion; use `bisect_right(coords,
  2*x)` to translate the *threshold* into a rank without needing `2*x` to be an actual value.
- **Strict inequality.** We want `nums[i] > 2*nums[j]`, so use `bisect_right` on `2*x`
  (everything `<= 2x` is excluded) and subtract from the running insert count. This is why
  `[5,4,3,2,1]` excludes `(1,3)`: `4 > 2*2 = 4` is false.
- **Overflow.** In languages with fixed-width integers, `2 * nums[j]` can overflow 32-bit;
  compute the threshold in 64-bit. Python's big ints sidestep this, but the logic still must
  compare against `2*x` precisely.
- **Negatives and large magnitudes** are handled entirely by coordinate compression — the
  BIT only ever indexes ranks.
- **Order of query-then-insert** is essential: querying after inserting `nums[j]` would let
  an element pair with itself or with a later element, corrupting the count.
