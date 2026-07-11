# Solution — Last-to-First (LF) Mapping

## Brute Force

Materialize both columns explicitly and, for each row `i`, count how many copies of
`L[i]` precede it, then scan the sorted first column `F` to find that same-ranked copy.

```python
def lf_mapping(bwt: str):
    n = len(bwt)
    F = sorted(bwt)
    LF = [0] * n
    for i in range(n):
        c = bwt[i]
        rank = bwt[:i].count(c)          # k-1 where this is the k-th c in L
        # find the position of the (rank)-th c in F
        seen = -1
        for j in range(n):
            if F[j] == c:
                seen += 1
                if seen == rank:
                    LF[i] = j
                    break
    return LF
```

- **Time:** `O(n^2)` — the inner `count` and the linear scan of `F` are each `O(n)` per
  row.
- **Space:** `O(n)` for `F` and the output.

Correct, but the repeated scanning is unnecessary once you realize `F` is just blocks of
equal characters laid out in sorted order.

## Optimal Approach (C-array + running rank)

The position of the `k`-th occurrence of character `c` in the sorted first column is
completely determined by two quantities:

- `C[c]` — the number of characters strictly smaller than `c` in the entire string. This
  is exactly where `c`'s block **begins** in `F`.
- the **rank** of this occurrence, i.e. how many `c`s appeared in `L` before index `i`.

Hence:

```
LF(i) = C[bwt[i]] + Occ(bwt[i], i)
```

where `Occ(c, i)` = number of `c`s in `bwt[0..i-1]`. Both pieces are computed in a single
linear sweep by maintaining a running tally:

```python
from collections import Counter

def lf_mapping(bwt: str):
    n = len(bwt)

    # C[c] = number of characters strictly smaller than c = start of c's block in F.
    counts = Counter(bwt)
    C, offset = {}, 0
    for c in sorted(counts):
        C[c] = offset
        offset += counts[c]

    # Sweep once, tracking how many of each character we have already seen.
    seen = {}
    LF = [0] * n
    for i, c in enumerate(bwt):
        LF[i] = C[c] + seen.get(c, 0)   # block start + rank-so-far
        seen[c] = seen.get(c, 0) + 1
    return LF
```

- **Time:** `O(n + σ)` — one pass to count, `O(σ log σ)` to order distinct characters,
  one pass to fill `LF`.
- **Space:** `O(n + σ)`.

**Why it is correct:** all rows beginning with `c` occupy the contiguous block
`[C[c], C[c] + counts[c])` of `F`, in the same relative order as the rows ending with `c`
in `L` (sorted-matrix rank preservation). So the `k`-th `c` in `L` maps to slot
`C[c] + (k-1)` of `F`, which is precisely `C[c] + seen_before`.

## Key Insights & Edge Cases

- **`LF` is a bijection / permutation** of the row indices — every row is the image of
  exactly one row. This is why iterating `LF` (Problem 2) visits each row once and
  terminates.
- **`Occ`/rank generalizes.** `Occ(c, i)` used here for the *diagonal* case
  (`c == bwt[i]`) is the same rank function the FM-index needs for *arbitrary* `c`
  (Problems 4–5). Precomputing a full `Occ` table (or a wavelet tree / bit-vectors) makes
  those queries `O(1)`.
- **Edge case — the sentinel:** `$` is the unique smallest char, so `C['$'] = 0` and the
  single `$` in `L` always maps to row `0` in `F`.
- **Edge case — length 1:** `bwt = "$"` gives `LF = [0]`.
- Building `C` over a fixed alphabet (e.g. `ACGT$`) lets you drop the sort and use a
  size-`σ` array, shaving the `O(σ log σ)` term for genomic data.
