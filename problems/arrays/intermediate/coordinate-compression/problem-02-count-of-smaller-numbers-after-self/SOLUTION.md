# Count of Smaller Numbers After Self — Solution

## Brute Force

For every `i`, scan all `j > i` and count how many `nums[j] < nums[i]`.

```python
def countSmaller(nums):
    n = len(nums)
    counts = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                counts[i] += 1
    return counts
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)` beyond the output.

Correct, but `O(n^2)` is far too slow for `n = 10^5`.

## Optimal Approach (Coordinate Compression + Fenwick Tree)

We want, for each element scanned from the **right**, the count of already-seen values that
are strictly smaller. If values were small we could keep a frequency array `freq[v]` and
answer with a prefix sum `freq[0] + ... + freq[v-1]`. A Fenwick tree maintains such prefix
sums with `O(log n)` point-update and prefix-query. The obstacle is the value range, so we
**compress** the values into ranks `0 .. k-1` first.

```python
class BIT:
    def __init__(self, n):
        self.tree = [0] * (n + 1)          # 1-indexed
    def update(self, i, delta):             # i is 0-based rank
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):                     # sum of ranks in [0, i-1]  (i is 0-based rank)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def countSmaller(nums):
    order = {v: i for i, v in enumerate(sorted(set(nums)))}
    bit = BIT(len(order))
    counts = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        r = order[nums[i]]           # compressed rank in [0, k-1]
        counts[i] = bit.query(r)     # how many seen values have rank < r  (strictly smaller)
        bit.update(r, 1)             # record this value as seen
    return counts
```

**Why it is correct.**

- Processing right-to-left means the BIT contains exactly the elements strictly to the right
  of index `i` when we query for `i`.
- `query(r)` returns the number of seen elements with rank in `[0, r-1]`, i.e. strictly
  smaller than `nums[i]` (equal values share rank `r` and are excluded — giving the required
  *strict* inequality).
- Coordinate compression preserves order, so "rank `< r`" is equivalent to "value
  `< nums[i]`."

**Step by step** on `[5, 2, 6, 1]`:

1. `sorted(set)` = `[1, 2, 5, 6]` -> map `{1:0, 2:1, 5:2, 6:3}`.
2. i=3, value 1 (rank 0): `query(0)=0`; update rank 0.
3. i=2, value 6 (rank 3): `query(3)=1` (only value 1 seen, rank 0 < 3); update rank 3.
4. i=1, value 2 (rank 1): `query(1)=1` (value 1 has rank 0 < 1); update rank 1.
5. i=0, value 5 (rank 2): `query(2)=2` (values 1 and 2 have ranks 0,1 < 2); update rank 2.
6. Result `[2, 1, 1, 0]`.

- **Time:** `O(n log n)` — sort for compression plus `n` BIT operations at `O(log n)` each.
- **Space:** `O(n)` for the map and BIT.

An alternative optimal approach is a modified merge sort that counts inversions during the
merge; it is also `O(n log n)` and needs no compression, but the BIT solution is the
canonical showcase of coordinate compression.

## Key Insights & Edge Cases

- **Strict vs. non-strict:** querying `[0, r-1]` (excluding rank `r`) enforces *strict*
  smaller. In `[-1, -1]`, both share the same rank so neither counts the other -> `[0, 0]`.
- **Negatives** are handled for free: compression maps them to small ranks like any other
  value.
- **Duplicates** collapse to one rank via `set`, which is exactly what we want — an equal
  value must not be counted as smaller.
- **Off-by-one:** be careful with 0-based ranks vs. the 1-indexed BIT. Here `update`
  shifts by `+1` internally and `query(r)` sums the first `r` slots (ranks `0..r-1`).
- The BIT must be sized to the number of *distinct* values (`k`), not `max(nums)`.
