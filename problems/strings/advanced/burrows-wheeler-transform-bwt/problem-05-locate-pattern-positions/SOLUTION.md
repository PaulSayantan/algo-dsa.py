# Solution — Locate Pattern Positions (FM-index + Suffix Array)

## Brute Force

Slide the pattern across the text and record every match.

```python
def locate(text, pattern):
    out, start = [], text.find(pattern)
    while start != -1:
        out.append(start)
        start = text.find(pattern, start + 1)   # allow overlaps
    return out
```

- **Time:** `O(n * |pattern|)` in the worst case (naive scan; `O(n)` with KMP/Z).
- **Space:** `O(1)` beyond the output.

Perfectly fine for a single search on a modest string, but it does **no preprocessing
reuse**: every query re-scans the whole text. When you must answer many pattern queries
against one large text (a genome, a log corpus), amortize the work into an index.

## Optimal Approach (FM-index range + suffix-array lookup)

Locating is counting (Problem 4) plus one translation step. Backward search over the
FM-index yields a contiguous **row range** `[top, bottom]` of the Burrows–Wheeler Matrix
whose row-prefixes equal `pattern`. Row `i` of the sorted matrix is the rotation/suffix
that starts at `SA[i]`, so **every matching start position is `SA[j]` for `j` in
`[top, bottom]`**.

```python
from collections import Counter

def suffix_array(text):
    # O(n log^2 n) prefix doubling shown for clarity; use SA-IS for O(n).
    return sorted(range(len(text)), key=lambda i: text[i:])

def locate(text, pattern):
    n = len(text)
    sa = suffix_array(text)
    bwt = "".join(text[i - 1] for i in sa)     # L[i] = text[SA[i]-1]

    # ---- FM-index: C[] and prefix-rank table Occ ----
    counts = Counter(bwt)
    alphabet = sorted(counts)
    C, offset = {}, 0
    for c in alphabet:
        C[c] = offset
        offset += counts[c]
    occ = {c: [0] * (n + 1) for c in alphabet}
    for i, ch in enumerate(bwt):
        for c in alphabet:
            occ[c][i + 1] = occ[c][i] + (1 if ch == c else 0)

    # ---- backward search -> row range [top, bottom] ----
    alpha_set = set(alphabet)
    top, bottom = 0, n - 1
    for c in reversed(pattern):
        if c not in alpha_set:
            return []
        top = C[c] + occ[c][top]
        bottom = C[c] + occ[c][bottom + 1] - 1
        if top > bottom:
            return []

    # ---- translate rows to text positions via the suffix array ----
    return sorted(sa[top:bottom + 1])
```

- **Time:** suffix-array build dominates the preprocessing — `O(n log n)` (or `O(n)` with
  SA-IS/DC3). A query is `O(|pattern|)` for the search plus `O(k + k log k)` to collect
  and sort the `k` reported positions.
- **Space:** `O(n * σ)` for the dense rank table (reducible to `O(n)` with succinct
  structures) plus `O(n)` for the suffix array.

**Why it is correct:** the sorted matrix places all rotations sharing a prefix
contiguously, and backward search maintains exactly the rows matching the current pattern
suffix. When the whole pattern is consumed, `[top, bottom]` is the set of rows whose
prefix equals `pattern`; each such row `j` corresponds to a distinct text position
`SA[j]` where the pattern starts. Overlapping matches are handled because each start
position is its own suffix/row.

## Key Insights & Edge Cases

- **Locate = count + `SA` lookup.** The whole extra cost over Problem 4 is `SA[j]` for the
  surviving rows. Keep the suffix array around and locating is nearly free.
- **Sampled suffix array (real FM-indexes).** Storing the full `SA` costs `O(n)` words. In
  practice FM-indexes store `SA` only at sampled positions and recover an unsampled
  `SA[j]` by following `LF` until a sampled row is hit, adding an `O(sampling_gap)` factor
  per reported position while cutting `SA` memory dramatically. This is the classic
  space/time trade-off behind read aligners (Bowtie, BWA).
- **Sort the output.** Row order in `[top, bottom]` reflects lexicographic suffix order,
  not text order, so `SA[top..bottom]` must be sorted before returning.
- **Empty result paths:** a character absent from the text, or a collapsed range
  (`top > bottom`), both return `[]`. Handle the missing-character case before touching
  `C`/`Occ`.
- **Overlaps are reported** (e.g. `issi` at 1 and 4 in `mississippi`) — do not dedupe or
  skip past a match by `|pattern|`.
- **Sentinel never appears** as a start position for a non-empty pattern, so index
  `n - 1` is naturally excluded.
