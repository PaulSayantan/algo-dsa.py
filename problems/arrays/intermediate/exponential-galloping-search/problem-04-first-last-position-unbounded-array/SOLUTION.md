# Solution — First and Last Position in an Unbounded Sorted Array

## Brute Force

Scan from index 0, remember the first index where the value equals `target`,
and keep updating the last such index, stopping once the value exceeds `target`
(or you hit the out-of-bounds sentinel).

```python
def search_range(reader, target):
    first = last = -1
    i = 0
    while reader.get(i) <= target:      # sentinel 2**31 - 1 stops the loop
        if reader.get(i) == target:
            if first == -1:
                first = i
            last = i
        i += 1
    return [first, last]
```

- **Time:** `O(p + c)` where `p` is the first index `>= target` and `c` is the
  count of matches — up to `O(n)`.
- **Space:** `O(1)`.

It never exploits the sort order to skip regions, so it is linear.

## Optimal Approach (Galloping to bound, then two boundary searches)

Finding first and last occurrence is two **boundary** queries on a sorted array:

- `first` = smallest index `i` with `get(i) >= target` — the **lower bound** —
  *provided* the value there actually equals `target`.
- `last`  = (smallest index `i` with `get(i) > target`) minus one — derived from
  the **upper bound**.

Both are monotonic-predicate searches, but they need a right endpoint, and the
length is hidden. **Exponential search supplies that endpoint.**

**Phase 1 — gallop to a `hi` with `get(hi) >= target`.** Double `bound` from 1
while `get(bound) < target`, capped at `2^31 - 1`. The out-of-bounds sentinel is
`> target`, so an array that ends before `target` still terminates the gallop.
Now the answer region is `[0, min(bound, INT_MAX)]`.

**Phase 2 — two boundary binary searches inside `[0, hi]`.**

```python
def search_range(reader, target):
    INT_MAX = 2**31 - 1

    # Phase 1: gallop to an upper endpoint whose value is >= target.
    bound = 1
    while bound <= INT_MAX and reader.get(bound) < target:
        bound *= 2
    hi_bound = min(bound, INT_MAX)

    def lower_bound(x):
        """First index i in [0, hi_bound] with reader.get(i) >= x."""
        lo, hi = 0, hi_bound
        while lo < hi:
            mid = (lo + hi) // 2
            if reader.get(mid) < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(target)
    if reader.get(first) != target:
        return [-1, -1]
    # last occurrence = (first index with value > target) - 1
    last = lower_bound(target + 1) - 1
    return [first, last]
```

**Why is it correct?** `lower_bound(target)` returns the leftmost index whose
value is at least `target`; if that value is exactly `target`, it is the first
occurrence, otherwise `target` is absent. `lower_bound(target + 1)` returns the
leftmost index whose value exceeds `target`; the index just before it is the
last `target`. The gallop guarantees `hi_bound` is a valid right endpoint
(`get(hi_bound) >= target`, or the sentinel), so both bisections stay inside a
region that certainly contains the boundary.

- **Time:** `O(log p)` to gallop (`p` = first index `>= target`) plus two
  `O(log p)` bisections = `O(log p)`, which is `<= O(log n)`.
- **Space:** `O(1)`.

### Step-by-step on `arr = [5,7,7,8,8,8,10], target = 8`

Gallop: `get(1)=7 < 8` -> `bound=2`; `get(2)=7 < 8` -> `bound=4`;
`get(4)=8 >= 8` -> stop. `hi_bound = 4`... but wait — the last `8` is at index 5,
outside `[0,4]`!

That is the subtlety: **the gallop only guarantees the region contains the
*first* occurrence, not the last.** So the lower-bound search must run on
`[0, hi_bound]`, but the upper-bound search needs a right endpoint proven to be
`> target`. Re-gallop (or gallop once for `target + 1`) to get it. The robust
version below galloples for each boundary target separately:

```python
def search_range(reader, target):
    INT_MAX = 2**31 - 1

    def gallop_hi(x):
        """Smallest bound (<= INT_MAX) with reader.get(bound) >= x."""
        b = 1
        while b <= INT_MAX and reader.get(b) < x:
            b *= 2
        return min(b, INT_MAX)

    def lower_bound(x, hi_bound):
        lo, hi = 0, hi_bound
        while lo < hi:
            mid = (lo + hi) // 2
            if reader.get(mid) < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(target, gallop_hi(target))
    if reader.get(first) != target:
        return [-1, -1]
    last = lower_bound(target + 1, gallop_hi(target + 1)) - 1
    return [first, last]
```

Now on `target = 8`: `gallop_hi(8)` gives `bound = 4` (`get(4)=8`), and
`lower_bound(8, 4) = 3` -> `first = 3`. `gallop_hi(9)`: `get(1)=7<9`,
`get(2)=7<9`, `get(4)=8<9`, `get(8)=sentinel>=9` -> `bound = 8`;
`lower_bound(9, 8) = 6` (`get(6)=10>=9`), so `last = 6 - 1 = 5`. Return `[3, 5]`.

## Key Insights & Edge Cases

- **The gallop bounds the *lower* boundary, not the upper one.** Because
  duplicates can extend past the first index that reaches `target`, gallop
  *separately* for `target` and for `target + 1` (or gallop far enough that
  `get(bound) > target` strictly). This is the most common bug in the unbounded
  variant.
- **`lower_bound(target + 1) - 1` gives the last occurrence** without a special
  "search rightmost" routine — reuse the same lower-bound helper.
- **Missing target (`6`):** `lower_bound(6, ...)` lands on the first index `>= 6`
  (index 3, value 7); since `get(3) != 6`, return `[-1, -1]`.
- **All elements equal target (`[2,2]`):** `gallop_hi(2)` -> `bound = 1`
  (`get(1)=2>=2`); `lower_bound(2,1)=0`. `gallop_hi(3)`: `get(1)=2<3`,
  `get(2)=sentinel>=3` -> `bound = 2`; `lower_bound(3, 2) = 2` (`get(2)` sentinel
  `> 2`), so `last = 1`. Return `[0, 1]`.
- **Sentinel dominates comparisons.** `2^31 - 1 > target` and
  `> target + 1` for all valid targets, so out-of-bounds reads always push the
  boundary search left correctly.
- **Cap the gallop** at `INT_MAX`; out-of-bounds returns the sentinel here (not
  0), so the gallop naturally stops, but the cap protects against fixed-width
  overflow when doubling.
