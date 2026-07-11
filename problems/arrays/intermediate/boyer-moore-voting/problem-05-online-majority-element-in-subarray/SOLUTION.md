# Online Majority Element in Subarray — Solution

## Brute Force

For each query, count occurrences directly over the subarray (a fresh Boyer–Moore or hash-map
pass), then check against `threshold`.

```python
class MajorityChecker:
    def __init__(self, arr):
        self.arr = arr

    def query(self, left, right, threshold):
        # Boyer–Moore over the subarray + verify.
        cand, cnt = None, 0
        for i in range(left, right + 1):
            if cnt == 0:
                cand = self.arr[i]
            cnt += 1 if self.arr[i] == cand else -1
        real = sum(1 for i in range(left, right + 1) if self.arr[i] == cand)
        return cand if real >= threshold else -1
```

- **Time:** O(Q · n) — each of Q queries scans up to n elements.
- **Space:** O(1) beyond the input.

With `n, Q` up to ~2·10^4 / 10^4 this is ~2·10^8 operations in the worst case — too slow. We
need each query to be sublinear.

## Optimal Approach — Boyer–Moore Segment Tree + Indexed Verification

Two ideas combine:

**1. The Boyer–Moore vote is associative, so it merges.** Represent a range by its
`(candidate, count)` vote summary. Two adjacent summaries merge in O(1):

- If both have the **same candidate**, the merged count is the sum.
- Otherwise the larger count "wins": merged candidate is whichever has the bigger count, and
  the merged count is `|count_left − count_right|` (the smaller cancels part of the larger).

A single element `x` is the summary `(x, 1)`. Building a **segment tree** with this merge lets
us fold any range `[left, right]` into one summary in **O(log n)**. Just as with the plain
array, the surviving candidate is the *only* value that could possibly be a strict majority of
that range — but the count field is a net vote, **not** the real frequency, so it must be
verified.

**2. Verify the candidate's real frequency in O(log n).** Precompute, for every distinct
value, the **sorted list of indices** where it occurs. The number of occurrences of value `v`
in `[left, right]` is `bisect_right(idx[v], right) - bisect_left(idx[v], left)`. Compare that
to `threshold`.

```python
from collections import defaultdict
from bisect import bisect_left, bisect_right


class MajorityChecker:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.positions = defaultdict(list)
        for i, v in enumerate(arr):
            self.positions[v].append(i)

        # Segment tree of (candidate, count) Boyer–Moore summaries.
        self.tree = [(-1, 0)] * (2 * self.n)
        for i, v in enumerate(arr):
            self.tree[self.n + i] = (v, 1)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2 * i], self.tree[2 * i + 1])

    @staticmethod
    def _merge(a, b):
        ca, na = a
        cb, nb = b
        if ca == cb:
            return (ca, na + nb)
        if na >= nb:
            return (ca, na - nb)
        return (cb, nb - na)

    def _range_vote(self, left, right):
        # Iterative segment-tree query over [left, right] (inclusive).
        res_l = (-1, 0)
        res_r = (-1, 0)
        lo = left + self.n
        hi = right + self.n + 1
        while lo < hi:
            if lo & 1:
                res_l = self._merge(res_l, self.tree[lo])
                lo += 1
            if hi & 1:
                hi -= 1
                res_r = self._merge(self.tree[hi], res_r)
            lo >>= 1
            hi >>= 1
        return self._merge(res_l, res_r)

    def query(self, left, right, threshold):
        cand, _ = self._range_vote(left, right)
        if cand == -1:
            return -1
        idx = self.positions[cand]
        occ = bisect_right(idx, right) - bisect_left(idx, left)
        return cand if occ >= threshold else -1
```

### Why it is correct

The merge rule is precisely the running Boyer–Moore vote expressed as a fold: same-candidate
segments accumulate; opposing segments cancel pair-for-pair, leaving the majority candidate of
the more-voted side with the surplus. Associativity of this fold is what makes the segment
tree valid — any grouping of the leaves produces the same final `(candidate, count)`. As in
the base algorithm, **if** a strict majority of `[left, right]` exists it must equal the folded
candidate; because the query guarantees `2 * threshold > right - left + 1`, a qualifying value
*is* a strict majority, so it can only be `cand`. The index-list binary search then returns
`cand`'s exact frequency; comparing to `threshold` accepts or rejects it. When no value reaches
`threshold`, the verification fails and we return `-1`.

### Worked trace on `arr = [1, 1, 2, 2, 1, 1]`

- `query(0, 5, 4)`: range vote folds to candidate `1`. `positions[1] = [0, 1, 4, 5]`;
  occurrences in `[0, 5]` = `bisect_right([...],5) - bisect_left([...],0) = 4 - 0 = 4`.
  `4 >= 4` → return `1`. ✓
- `query(0, 3, 3)`: subarray `[1,1,2,2]` folds to some candidate with net count 0-ish; say
  `1`. `positions[1] = [0,1,4,5]`; occurrences in `[0, 3]` = `2 - 0 = 2`. `2 < 3` → `-1`. ✓
  (Even if the fold returned `2`, `positions[2] = [2, 3]` gives `2 < 3`, also `-1`.)
- `query(2, 3, 2)`: subarray `[2, 2]` folds to candidate `2`. `positions[2] = [2, 3]`;
  occurrences in `[2, 3]` = `2 - 0 = 2`. `2 >= 2` → return `2`. ✓

### Complexity

- **Build:** O(n) segment tree + O(n) index lists.
- **Query:** O(log n) to fold the range vote + O(log n) for the binary-search verification =
  **O(log n)** per query.
- **Space:** O(n) for the tree and the index lists.

Total: O(n + Q log n) time — comfortably within limits.

## Key Insights & Edge Cases

- **Associativity is the linchpin.** The Boyer–Moore vote merges like a monoid, which is
  exactly the property a segment tree needs; without it, ranges could not be composed.
- **The tree gives only a *candidate*, never a proven count.** The stored count is a net vote
  after cancellation, so an independent frequency check is mandatory — skipping it produces
  wrong answers for subarrays with no majority.
- **Index-list + binary search** is the standard O(log n) verifier; an alternative is a
  randomized approach (sample a few indices in `[left, right]`, each has > 1/2 chance of being
  the majority) combined with the same index lists — but the deterministic segment tree is
  cleaner to reason about.
- The `2 * threshold > length` guarantee is what makes the answer unique; without it there
  could be several values above `threshold` and a single Boyer–Moore candidate would be
  insufficient.
- Edge cases: length-1 subarrays, subarrays where the candidate exists but falls short of
  `threshold`, and repeated identical queries all resolve correctly.
