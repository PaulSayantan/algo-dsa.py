# Reverse Pairs — Solution

## Brute Force

Check every pair `(i, j)` with `i < j`.

```python
def reversePairs(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                count += 1
    return count
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

Too slow for `n = 5 * 10^4` (up to ~2.5 billion pair checks).

## Optimal Approach (Coordinate Compression + Fenwick Tree)

Sweep `i` from left to right, keeping in a BIT all the raw values `nums[0..i-1]` we have
already passed. For the current `nums[i]` we want the number of *earlier* values `nums[k]`
(`k < i`) with `nums[k] > 2 * nums[i]`. Equivalently, count how many inserted values are
**strictly greater than** the threshold `2 * nums[i]`. Summing that over all `i` gives the
answer (each reverse pair `(k, i)` is counted once, when we process `j = i`).

To index a BIT by value we compress. The threshold is `2 * nums[i]`, so the comparison mixes
two magnitude scales. We therefore compress the union of `nums` **and** `2 * nums`, giving a
single coordinate system in which both a stored value and any threshold have a well-defined
rank.

```python
import bisect

class BIT:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
    def update(self, i, delta):      # i is 1-based
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):              # prefix sum of [1..i]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def reversePairs(nums):
    coords = sorted(set(nums) | set(2 * x for x in nums))
    m = len(coords)
    bit = BIT(m)
    count = 0
    for x in nums:
        # number of already-inserted values strictly greater than 2*x:
        # 2*x sits at position p = bisect_right(coords, 2*x); values with
        # rank in (p, m] are strictly greater. Use suffix = total - prefix(p).
        p = bisect.bisect_right(coords, 2 * x)     # count of coords <= 2*x
        count += bit.query(m) - bit.query(p)        # inserted values with rank > p
        r = bisect.bisect_left(coords, x) + 1       # 1-based rank of x
        bit.update(r, 1)
    return count
```

**Why it is correct.**

- We insert values in index order, so when processing `x = nums[i]` the BIT holds exactly
  `nums[0..i-1]` — the valid partners with smaller index.
- `bit.query(m) - bit.query(p)` counts inserted values whose compressed rank is `> p`, where
  `p` is the number of coordinates `<= 2*x`. Any coordinate with rank `> p` has value
  `> 2*x`, so this is exactly the count of stored `nums[k] > 2 * nums[i]`.
- Using `bisect_right(coords, 2*x)` for the threshold guarantees we exclude values equal to
  `2*x` (we need *strictly greater*), and it works even when `2*x` is not itself a stored
  raw value — it still has a valid position in the shared coordinate list.

**Step by step** on `[1, 3, 2, 3, 1]`:

- `coords = sorted(set{1,3,2,3,1} ∪ {2,6,4,6,2}) = [1, 2, 3, 4, 6]`.
- x=1: threshold 2, `p = bisect_right(coords,2)=2`; suffix count = 0 (empty). Insert 1.
- x=3: threshold 6, `p = bisect_right(coords,6)=5`; suffix = 0. Insert 3.
- x=2: threshold 4, `p = bisect_right(coords,4)=4`; stored {1,3}, ranks 1 and 3, none `>4`th
  coord -> 0. Insert 2.
- x=3: threshold 6, `p=5`; suffix = 0. Insert 3.
- x=1: threshold 2, `p=2`; stored {1,3,2,3} have ranks 1,3,2,3; those with rank `>2` are the
  two 3's -> count += 2. Insert 1.
- Total `2`.

- **Time:** `O(n log n)`.
- **Space:** `O(n)` for the coordinate list and BIT.

A merge-sort counting variant is also `O(n log n)` and avoids compression, but the BIT
version is the clean illustration of compressing two value scales together.

## Key Insights & Edge Cases

- **Compress both `nums` and `2*nums`.** If you only compress `nums`, the threshold `2*x`
  may have no rank and the comparison breaks. This is the crux of the problem.
- **Overflow:** `2 * nums[j]` can exceed 32 bits. In Python integers are unbounded, but in
  languages with fixed-width ints, use 64-bit types for the doubled values.
- **Strict inequality:** `bisect_right(coords, 2*x)` excludes coordinates equal to `2*x`, so
  ties never count. `[5, 5, 5]` yields 0 because `5 > 10` is never true.
- **Insert after querying**, not before — otherwise an element could pair with itself or
  with a later element.
- Size the BIT to the number of distinct coordinates `m`, not to the value range.
