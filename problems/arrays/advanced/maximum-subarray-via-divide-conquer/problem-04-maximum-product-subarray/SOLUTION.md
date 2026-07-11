# Maximum Product Subarray — Solution

## Brute Force

Try every subarray, multiply out its elements, track the maximum.

```python
def brute(nums):
    best = nums[0]
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            best = max(best, prod)
    return best
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

## Optimal Approach (Divide & Conquer)

Products differ from sums in two ways that break a naive "best crossing value"
merge:

- Multiplying by a **negative** swaps the roles of max and min.
- A **zero** annihilates any subarray that spans it.

To merge two halves in `O(1)`, each recursive call returns a **range summary**:

```
(total, max_prefix, min_prefix, max_suffix, min_suffix, best)
```

- `total`        — product of the whole range,
- `max_prefix` / `min_prefix` — best/worst product of a prefix starting at `lo`,
- `max_suffix` / `min_suffix` — best/worst product of a suffix ending at `hi`,
- `best`         — best product of any subarray fully inside the range.

**Base case** (single element `x`): every field is `x`.

**Merge** of left summary `L` and right summary `R` (left range immediately
precedes right range):

```python
def merge(L, R):
    total = L.total * R.total

    # A prefix of the combined range is either a prefix of L, or all of L times a
    # prefix of R. Track both max and min (sign flips).
    cand_pref = (L.max_prefix, L.min_prefix,
                 L.total * R.max_prefix, L.total * R.min_prefix)
    max_prefix = max(cand_pref)
    min_prefix = min(cand_pref)

    cand_suf = (R.max_suffix, R.min_suffix,
                R.total * L.max_suffix, R.total * L.min_suffix)
    max_suffix = max(cand_suf)
    min_suffix = min(cand_suf)

    # Best crossing product: left suffix * right prefix, all four sign combos.
    cross = (L.max_suffix * R.max_prefix, L.max_suffix * R.min_prefix,
             L.min_suffix * R.max_prefix, L.min_suffix * R.min_prefix)
    best = max(L.best, R.best, max(cross))

    return Summary(total, max_prefix, min_prefix, max_suffix, min_suffix, best)
```

Reference driver:

```python
from collections import namedtuple
Summary = namedtuple("Summary", "total max_prefix min_prefix max_suffix min_suffix best")

def maxProduct(nums):
    def solve(lo, hi):
        if lo == hi:
            x = nums[lo]
            return Summary(x, x, x, x, x, x)
        mid = (lo + hi) // 2
        return merge(solve(lo, mid), solve(mid + 1, hi))
    return solve(0, len(nums) - 1).best
```

**Why it is correct.** By induction each half's summary is correct. Any subarray
of the merged range is (a) inside the left → covered by `L.best`, (b) inside the
right → `R.best`, or (c) crossing → a non-empty suffix of the left times a
non-empty prefix of the right. Because a product's extremes depend on sign, the
crossing optimum must consider all four combinations of {left max/min suffix} ×
{right max/min prefix}; taking the max over those four captures the case where two
negatives multiply into a large positive. The prefix/suffix fields are maintained
analogously so the next level up can keep merging. Zeros are handled with no
special case: a zero factor simply makes the relevant products `0`, and `max`
still picks a better positive subarray elsewhere (or `0` if none exists).

**Step by step on `[-2, 3, -4]`:**

- Summaries for singletons: `-2`, `3`, `-4` (all fields equal to the element).
- Merge `[-2]` and `[3]`: crossing = `-2 * 3 = -6`; `best = max(-2, 3, -6) = 3`;
  `max_suffix = max(3, 3*-2) = 3`, `min_suffix = min(3, -6) = -6`,
  `min_prefix = min(-2, -2*3) = -6`, `total = -6`.
- Merge that with `[-4]`: crossing candidates include `min_suffix(-6) *
  min_prefix(-4) = 24` and `max_suffix(3) * -4 = -12`; `best = max(3, -4, 24) =
  24`. ✓

**Complexity.** `T(n) = 2T(n/2) + O(1)` merge = `O(n)` total by the master theorem
(the merge is constant work, unlike the sum problem's linear crossing scan!).
Space is `O(log n)` recursion depth.

## Key Insights & Edge Cases

- **Track BOTH max and min everywhere.** The minimum (most negative) suffix/prefix
  becomes the maximum after another negative factor. Dropping the min silently
  fails on inputs like `[-2, 3, -4]`.
- **All four crossing sign combinations** must be enumerated:
  `max*max, max*min, min*max, min*min`.
- **Zeros need no special case** here — they zero out spanning products and `max`
  naturally avoids them, e.g. `[-2, 0, -1] → 0`.
- **Prefix/suffix must stay non-empty** (`L.total * R.max_prefix` uses the whole
  left, and `L.max_prefix` uses only the left). The merge candidate lists encode
  exactly the "extend or not" choices.
- **This merge is `O(1)`**, so unlike the sum version, divide & conquer here is
  `O(n)` — matching the DP/Kadane-style two-variable solution asymptotically. The
  summary tuple is precisely what you would store in a segment tree if products
  needed range queries.
