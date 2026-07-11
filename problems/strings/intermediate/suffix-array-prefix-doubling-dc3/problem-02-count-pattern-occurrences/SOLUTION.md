# Solution — Count Pattern Occurrences

## Brute Force

For each query `P`, scan `S` and count matches (e.g. `str.count` with overlap
handling, or a sliding window / KMP per query).

- KMP per query: O(n + |P|) per query, so O(q * (n + |P|)) total.
- With `n, q` up to `2 * 10^5`, this is up to ~4 * 10^10 operations — too slow when
  the text is fixed and queries are numerous.
- **Time:** O(sum over queries of (n + |P_i|)). **Space:** O(n).

## Optimal Approach — Suffix Array + Binary Search

**Idea.** Build the suffix array `SA` of `S` once. Every occurrence of `P` in `S`
is a prefix of exactly one suffix `S[i:]`. Since `SA` lists suffixes in sorted
order, **all** suffixes having `P` as a prefix occupy a **contiguous range**
`[lo, hi)` in `SA`. The number of occurrences of `P` is simply `hi - lo`.

**Why the range is contiguous & why binary search works.** Lexicographic order
means that if suffix `a < suffix b` and both start with `P`, then every suffix
between them in sorted order also starts with `P` (they are "sandwiched"). So
finding the block reduces to:
- `lo` = first index in `SA` whose suffix is `>= P` (lower bound), and
- `hi` = first index whose suffix is `>= P + '￿'`, i.e. first suffix that is
  strictly greater than every string starting with `P`.

Both bounds are found by binary search over `SA`. Comparing `P` against a suffix
`S[SA[m]:]` costs O(|P|) (we only ever need the first `|P|` characters), so each
binary search is O(|P| log n).

**Steps.**
1. Build `SA = build_suffix_array(S)` — O(n log n) (or O(n log^2 n)).
2. For each pattern `P`:
   - `lo = lower_bound(P)` — smallest `k` with `S[SA[k]:SA[k]+|P|] >= P`.
   - `hi = lower_bound(P')` where `P'` is `P` with its last char incremented, OR
     just find the first suffix that does **not** start with `P`.
   - answer `= hi - lo` (clamped to `>= 0`).

```python
def count_occurrences(s, queries):
    n = len(s)
    sa = build_suffix_array(s)

    def lower_bound(p):
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            # compare p against the prefix of the mid-th suffix
            if s[sa[mid]:sa[mid] + len(p)] < p:
                lo = mid + 1
            else:
                hi = mid
        return lo

    res = []
    for p in queries:
        left = lower_bound(p)
        # first suffix strictly greater than all strings starting with p
        p_hi = p[:-1] + chr(ord(p[-1]) + 1)
        right = lower_bound(p_hi)
        res.append(right - left)
    return res
```

- Build: O(n log n). Each query: O(|P| log n). Total: O(n log n + sum |P_i| log n).
- **Space:** O(n).

> Note: the slice `s[sa[mid]:sa[mid]+len(p)]` takes O(|P|) to build. To make each
> comparison strictly O(|P|) without extra allocation, compare character-by-character
> or use the LCP array to skip already-matched prefixes (advanced optimization).

## Key Insights & Edge Cases

- **Occurrences = prefix count.** The map "occurrence of `P` at index `i`" ⇔
  "suffix `S[i:]` starts with `P`" is what makes the suffix array applicable.
- **Overlapping matches are counted** automatically — each is a distinct suffix.
- **Pattern longer than `S`** (or than the matched suffix): comparison naturally
  fails, giving count 0 (e.g. `"aaaaa"` in `"aaaa"`).
- **Upper bound trick:** incrementing the last character works for the given ASCII
  alphabet; alternatively define the comparison so a suffix "starts with `P`" and
  binary-search that predicate directly to avoid alphabet assumptions.
- **Empty pattern** (if allowed) matches at every position → `n`; guard for it.
- If you also need the actual positions, they are exactly `SA[lo], ..., SA[hi-1]`.
