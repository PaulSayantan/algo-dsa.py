# Solution — Intersection of Two Sorted Arrays (Galloping)

## Brute Force

Put the smaller array in a hash set and scan the larger one (or vice versa),
collecting matches; then sort.

```python
def intersect_sorted(a, b):
    seen = set(a)
    return sorted(v for v in b if v in seen)
```

- **Time:** `O(m + n)` expected for the set build and scan, plus `O(k log k)` to
  sort the `k` matches. Dominated by the huge array's length `n`.
- **Space:** `O(min(m, n))` for the set.

This works, but touches every element of the giant array and needs extra memory.
The classic two-pointer merge avoids the set yet is still `O(m + n)` — every
element of the big array is visited once. When one array is tiny, that is
wasteful: we should be able to *skip* long stretches of the big array.

## Optimal Approach (Galloping / one-sided binary search)

Let `a` be the smaller array (swap if needed) and `b` the larger. Walk `a` left
to right. Keep a cursor `start` into `b`. For each `x = a[i]`, **gallop** through
`b` starting at `start`: try offsets `1, 2, 4, 8, ...` from `start` until either
`b[start + offset] >= x` or the offset runs past the end of `b`. That brackets
`x` between the previous and current probe; binary-search that bracket for `x`.

Crucially, advance `start` to the position where the search landed, so the next
(larger) element of `a` resumes from there instead of restarting at 0 — the
cursor only ever moves forward.

```python
def intersect_sorted(a, b):
    # Ensure `a` is the smaller array so we gallop through the larger `b`.
    if len(a) > len(b):
        a, b = b, a

    result = []
    n = len(b)
    start = 0                       # cursor into b; never moves backward
    for x in a:
        if start >= n:
            break                   # exhausted b; no more matches possible

        # Gallop: expand the step until b overshoots x or we pass the end.
        offset = 1
        while start + offset < n and b[start + offset] < x:
            offset *= 2

        # Bracket is [start + offset // 2, min(start + offset, n - 1)].
        lo = start + offset // 2
        hi = min(start + offset, n - 1)
        pos = _lower_bound(b, lo, hi, x)   # first index in [lo, hi] with b[idx] >= x

        if pos < n and b[pos] == x:
            result.append(x)
            start = pos + 1         # x consumed; next search starts after it
        else:
            start = pos             # x absent; resume from the overshoot point
    return result


def _lower_bound(b, lo, hi, x):
    """First index in [lo, hi] whose value is >= x (or hi + 1 if none)."""
    hi = hi + 1                     # search half-open [lo, hi+1)
    while lo < hi:
        mid = (lo + hi) // 2
        if b[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

**Why is it correct?** For each `x`, the gallop establishes a bracket that
provably contains the first position in `b` (at or after `start`) whose value is
`>= x`: everything below `start + offset // 2` is `< x` (loop invariant), and
`b[start + offset] >= x` or we hit the end. The lower-bound search finds that
position exactly, and we record a match only when `b[pos] == x`. Because `a` is
increasing, the next value is `>= x`, so resuming the cursor at `pos` (or
`pos + 1` on a match) never skips a possible future match — the cursor is
monotonic and each element of `b` is entered by a gallop at most a logarithmic
number of times overall.

**Why `O(m * log(n / m))`?** Each of the `m` elements of `a` galloples across
some gap `g_i` in `b`, costing `O(log g_i)`. The gaps sum to at most `n`
(`sum g_i <= n`), and `sum log g_i` is maximized when the gaps are equal
(`g_i = n / m`), giving `O(m * log(n / m))` by concavity of `log`. This beats
`O(m log n)` (independent binary searches from scratch) and beats the
`O(m + n)` linear merge whenever `m << n`. This is exactly the "galloping mode"
Timsort switches into when one run keeps winning the merge.

- **Time:** `O(m * log(n / m))` where `m = min(len(a), len(b))`,
  `n = max(len(a), len(b))`.
- **Space:** `O(1)` beyond the output list.

### Step-by-step on `a = [1,4,9]`, `b = [0..10]`

- `x = 1`, `start = 0`: `b[1] = 1 >= 1` -> offset stays 1; bracket `[0, 1]`;
  `lower_bound = 1`, `b[1] = 1 == 1` -> match, `start = 2`.
- `x = 4`, `start = 2`: `b[3] = 3 < 4` -> offset 2; `b[4] = 4 >= 4` -> stop;
  bracket `[3, 4]`; `lower_bound = 4`, `b[4] = 4` -> match, `start = 5`.
- `x = 9`, `start = 5`: `b[6]=6<9` -> 2; `b[7]=7<9` -> 4; `b[9]=9>=9` -> stop;
  bracket `[7, 9]`; `lower_bound = 9`, `b[9] = 9` -> match, `start = 10`.

Result: `[1, 4, 9]`.

## Key Insights & Edge Cases

- **Always gallop through the *larger* array.** Iterating the smaller array
  keeps the outer loop count `m` small; galloping through the larger array is
  where the logarithmic skipping pays off. Swap the roles up front.
- **Persist the cursor across iterations.** Restarting each search at index 0
  would give `O(m log n)`; monotonically advancing `start` is what yields the
  tighter `O(m * log(n / m))` and prevents rescanning skipped regions.
- **Empty input / no overlap:** if either array is empty, or the smallest of one
  exceeds the largest of the other, the cursor logic returns `[]` (Example 3:
  galloping for `10` immediately hits the end of `b`).
- **Value past the end of `b` (`100` in Example 2):** the gallop runs `offset`
  past `n`, the bracket is clamped with `min(..., n - 1)`, `lower_bound` returns
  `n`, and the `pos < n` guard rejects the match.
- **Distinct values assumed.** With duplicates you would additionally advance
  past equal runs to avoid emitting a value twice; here each value is unique so
  `start = pos + 1` after a match suffices.
- **Clamp the bracket high end** with `min(start + offset, n - 1)` — after the
  final doubling `start + offset` can exceed the array; forgetting this reads out
  of bounds.
