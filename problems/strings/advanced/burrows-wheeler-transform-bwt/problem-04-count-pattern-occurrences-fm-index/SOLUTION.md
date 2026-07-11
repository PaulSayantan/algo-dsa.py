# Solution — Count Pattern Occurrences (FM-index)

## Brute Force

Invert the BWT to recover the text, then count each pattern with a substring search.

```python
def count_occurrences(bwt, patterns):
    text = inverse_bwt(bwt)          # from Problem 2, O(n)
    out = []
    for p in patterns:
        cnt, start = 0, text.find(p)
        while start != -1:
            cnt += 1
            start = text.find(p, start + 1)   # count overlapping occurrences
        out.append(cnt)
    return out
```

- **Time:** `O(n)` to invert plus `O(m * (n + |p|))` for `m` patterns — effectively
  `O(n + m*n)`; every query re-scans the whole text.
- **Space:** `O(n)` for the reconstructed text.

This throws away the whole point of the BWT: it decompresses and scans linearly per
query. The FM-index answers each query in time proportional only to the *pattern* length.

## Optimal Approach (FM-index backward search)

The FM-index is `bwt` + two small structures:

- **`C[c]`** — the number of characters in the text strictly smaller than `c`, i.e. the
  first row of the Burrows–Wheeler Matrix whose first column equals `c`.
- **`Occ(c, i)`** (a.k.a. rank) — the number of occurrences of `c` in `bwt[0..i-1]`.

**Backward search** keeps a range `[top, bottom]` of BWM rows whose leading characters
spell the already-processed suffix of the pattern. Scanning the pattern right-to-left,
each new character `c` refines the range by the LF-mapping applied to the endpoints:

```
top_new    = C[c] + Occ(c, top)
bottom_new = C[c] + Occ(c, bottom + 1) - 1
```

If `top_new > bottom_new`, the extended pattern has no match and the count is `0`. After
all characters are consumed, the number of matching rows is `bottom - top + 1`, and each
matching row is a distinct occurrence.

```python
from collections import Counter

def build_fm_index(bwt):
    n = len(bwt)
    counts = Counter(bwt)
    alphabet = sorted(counts)

    # C[c] = number of chars strictly smaller than c.
    C, offset = {}, 0
    for c in alphabet:
        C[c] = offset
        offset += counts[c]

    # Prefix rank table: occ[c] is a list where occ[c][i] = # of c in bwt[0..i-1].
    occ = {c: [0] * (n + 1) for c in alphabet}
    for i, ch in enumerate(bwt):
        for c in alphabet:
            occ[c][i + 1] = occ[c][i] + (1 if ch == c else 0)
    return C, occ, alphabet

def count_occurrences(bwt, patterns):
    n = len(bwt)
    C, occ, alphabet = build_fm_index(bwt)
    alpha_set = set(alphabet)
    results = []
    for p in patterns:
        top, bottom = 0, n - 1
        ok = True
        for c in reversed(p):
            if c not in alpha_set:      # character absent from text
                ok = False
                break
            top = C[c] + occ[c][top]
            bottom = C[c] + occ[c][bottom + 1] - 1
            if top > bottom:            # range collapsed -> no match
                ok = False
                break
        results.append(bottom - top + 1 if ok else 0)
    return results
```

- **Time:** building the prefix-rank table is `O(n * σ)` (or `O(n)` with per-character
  bit-vectors / a wavelet tree). Each query is `O(|p|)` with `O(1)` rank lookups, for
  `O(sum of |p|)` total — **independent of `n`**.
- **Space:** `O(n * σ)` for the dense rank table, reducible to `O(n)` with succinct rank
  structures.

**Why it is correct:** `[top, bottom]` are exactly the rows of the sorted matrix whose
prefixes equal the current pattern suffix (the sorted rows sharing a prefix are
contiguous). The update is the LF-mapping restricted to occurrences of `c`, which maps
that contiguous block to the contiguous block of rows one character longer. When the
whole pattern is consumed, those rows are precisely the suffixes/positions where the
pattern begins, so their count is the number of occurrences.

## Key Insights & Edge Cases

- **Rank is everything.** `Occ(c, i)` at the two endpoints is all backward search needs.
  For big alphabets or memory limits, replace the dense table with a **wavelet tree**
  (`O(log σ)` rank, `O(n log σ)` space) or **sampled bit-vectors**.
- **Half-open indexing.** Use `Occ(c, top)` for the new top and `Occ(c, bottom + 1) - 1`
  for the new bottom; off-by-one here is the most common bug. Test against a brute-force
  counter.
- **Missing characters:** if a pattern contains a symbol not in the text, count is `0` —
  detect it before indexing `C`/`Occ` to avoid a `KeyError`.
- **Overlapping occurrences count separately** (e.g. `"ana"` in `"banana"` at 1 and 3),
  which backward search handles naturally since each start position is its own row.
- **Empty range vs. full match:** initialize `[top, bottom] = [0, n-1]` (all rows); a
  never-narrowed range would (incorrectly) count the empty pattern as `n` — the
  constraints require `|pattern| >= 1`, so this is not exercised, but guard it if you
  relax the constraint.
- **Counting only, no locating.** This problem needs *how many*, not *where*. Reporting
  the actual positions additionally requires the suffix array (see Problem 5).
