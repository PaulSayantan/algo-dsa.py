# Solution — Locate Substring Occurrences

## Brute Force

Scan `T` for each pattern and record the start indices of every match. With KMP
this is `O(n + m + occ)` per query, but every query re-reads the entire text, so
across `q` queries the total is `O(q * (n + m) + total_occ)`. For a fixed text
and many queries the recurring `O(n)` term dominates.

- Time: `O(q * (n + m)) + O(total_occ)`
- Space: `O(m)` per query

## Optimal Approach (FM-Index: backward search + suffix-array lookup)

Locating is counting plus one more step: turn the matching **rows** into text
**positions**.

### Steps

1. Build the FM-Index exactly as for counting: `S = T + "$"`, suffix array `SA`,
   `BWT`, `C[]`, and rank table `Occ`. Keep `SA` available.
2. Run **backward search** to get the half-open interval `[sp, ep)` of
   suffix-array rows whose suffixes begin with `P`:
   ```
   sp, ep = 0, n
   for c in reversed(P):
       sp = C[c] + Occ(c, sp)
       ep = C[c] + Occ(c, ep)
       if sp >= ep:
           return []
   ```
3. Each row `i` in `[sp, ep)` corresponds to the suffix that starts at `SA[i]`,
   so the occurrence positions are `{ SA[i] : sp <= i < ep }`. Sort them.

```python
def locate(self, pattern):
    sp, ep = self._bw_range(pattern)
    return sorted(self.sa[i] for i in range(sp, ep))
```

Reporting is `O(occ)` after an `O(m)` search (the `sort` adds
`O(occ log occ)`; since the rows in `[sp, ep)` are sorted by suffix, not by
position, a sort is needed if you want positions in ascending order).

### Space-optimized locate (sampled suffix array)

Storing the full `SA` costs `O(n log n)` bits, which defeats the FM-Index's
space advantage. The real technique samples the suffix array: keep `SA[i]` only
for rows whose text position is a multiple of a sample rate `s` (or, commonly,
mark sampled positions with a bitvector). For an unsampled row `i`, repeatedly
apply the **LF-mapping**

```
LF(i) = C[BWT[i]] + Occ(BWT[i], i)
```

which moves to the row of the suffix that is one character to the *left*. After
`t` steps you land on a sampled row with known position `p`; then the original
position is `p + t`. Because you never walk more than `s` steps, each occurrence
costs `O(s)`, giving `O(m + occ * s)` time while storing only `O((n/s) log n)`
bits of samples. This folder's teaching implementation keeps the full `SA` for
clarity.

### Why it is correct

The interval `[sp, ep)` is (by the backward-search invariant) exactly the block
of sorted suffixes beginning with `P`; each such suffix is an occurrence of `P`,
and `SA[i]` is where that suffix — hence that occurrence — starts. The LF-mapping
is correct because the last and first BWT columns list identical characters in
the same relative order, so `LF(i)` is the row whose suffix is `S[SA[i]-1 :]`.

### Complexity

- Build: `O(n)`–`O(n log n)` time, `O(n)` space (teaching) / `n H_k + o(n)` bits
  (compressed).
- `locate(P)`: `O(m + occ)` with a full `SA`; `O(m + occ * s)` with a sampled
  `SA`. Sorting positions adds `O(occ log occ)`.

## Key Insights & Edge Cases

- **Rows vs. positions:** backward search yields rows; you still need `SA` (full
  or sampled) to recover text positions. This is the whole point of the sample.
- **Ordering:** rows in `[sp, ep)` are in *lexicographic-suffix* order, not
  positional order. Sort if the problem wants ascending indices (this one does).
- **Empty result:** if `sp >= ep` at any step, `P` is absent — return `[]`.
- **Overlapping matches** appear as distinct suffix-array rows, so they are all
  reported (e.g. `"aaaa"`, `"aa"` -> `[0, 1, 2]`).
- **Single character queries** are the degenerate case: the interval is the whole
  block of that character, `[C[c], C[next_char])`.
- The sentinel row (the suffix `"$"`) never matches a non-empty pattern, so it is
  naturally excluded.
