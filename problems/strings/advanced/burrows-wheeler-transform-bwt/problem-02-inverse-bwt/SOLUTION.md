# Solution — Inverse the BWT

## Brute Force

You can rebuild the entire Burrows–Wheeler Matrix column by column. Start with `n` empty
rows. Repeat `n` times: prepend the last column `L` to the front of the current rows,
then sort all rows. After `n` iterations each row is a full cyclic rotation; the row that
ends in `$` (equivalently, starts with `$`) is the original string.

```python
def inverse_bwt(bwt: str) -> str:
    n = len(bwt)
    rows = [""] * n
    for _ in range(n):
        rows = sorted(bwt[i] + rows[i] for i in range(n))
    return next(r for r in rows if r.endswith("$"))
```

- **Time:** `O(n^2 log n)` — `n` rounds, each sorting `n` strings of growing length.
- **Space:** `O(n^2)` — the full matrix is materialized.

Correct but wasteful; it recomputes the whole matrix just to read one row.

## Optimal Approach (LF-mapping walk)

Two structural facts drive the linear-time inverse:

1. **First column `F` = sorted `L`.** Every rotation contributes exactly one character
   to each column, so `F` and `L` contain the same multiset of characters; sorting `L`
   yields `F`.
2. **Rank / order preservation.** Consider all rows whose first character is `c`. Because
   the matrix is sorted, these rows appear consecutively and *in the same relative
   order* as the rows whose last character is `c`. Therefore the **k-th occurrence of `c`
   in `L`** and the **k-th occurrence of `c` in `F`** denote the *same rotation*. This
   gives the **LF-mapping**:

   ```
   LF(i) = (index in F of the same-ranked copy of L[i])
         = C[L[i]] + rank_of_this_occurrence_of_L[i]_in_L
   ```

   where `C[c]` = number of characters in the whole string strictly smaller than `c`
   (the starting offset of block `c` in the first column).

Building `LF` in one linear pass, then walking it, reconstructs the text:

```python
from collections import Counter

def inverse_bwt(bwt: str) -> str:
    n = len(bwt)

    # C[c] = start offset of character c's block in the sorted first column.
    counts = Counter(bwt)
    C, offset = {}, 0
    for c in sorted(counts):
        C[c] = offset
        offset += counts[c]

    # LF[i] = row in F holding the same occurrence of bwt[i] as row i in L.
    seen = {}
    LF = [0] * n
    for i, c in enumerate(bwt):
        LF[i] = C[c] + seen.get(c, 0)   # k-th c in L -> k-th c in F
        seen[c] = seen.get(c, 0) + 1

    # Walk from the row that begins with '$' (row 0 of the sorted matrix).
    # Following LF moves us to the row whose first char is the current last char,
    # i.e. one character earlier in the original text. Collect and reverse.
    out = ["$"]
    row = 0                     # F[0] == '$'
    while bwt[row] != "$":
        out.append(bwt[row])
        row = LF[row]
    return "".join(reversed(out))
```

Walking `LF` from the sentinel row visits the characters of `text` in **reverse** order
(each `LF` step moves one position earlier in the original string), so we collect and
reverse at the end. Equivalently, one can prepend characters as they are discovered.

- **Time:** `O(n + σ)` — one pass to build `C`/`LF` plus one `n`-step walk (`σ` = alphabet
  size for the sort of distinct characters).
- **Space:** `O(n + σ)` — the `LF` array and the counts.

**Why it is correct:** the LF-mapping is a bijection on rows that, applied repeatedly
from the sentinel, traces the unique Hamiltonian cycle through the rotations that spells
out `text`. Rank preservation guarantees each step lands on the correct predecessor
character.

## Key Insights & Edge Cases

- **LF-mapping is the whole game.** `LF(i) = C[L[i]] + Occ(L[i], i)` where `Occ(c, i)` is
  the number of `c`s in `L[0..i]`. Master this and both the inverse and the FM-index
  (Problems 4–5) follow.
- **Direction matters.** Following `LF` gives characters back-to-front; make sure you
  reverse (or prepend) so the output is not mirrored.
- **Row 0 always starts with `$`** because `$` is the smallest character, so it is a
  reliable starting point for the walk.
- **Edge case — single `$`:** input `"$"` returns `"$"`.
- **Edge case — repeated letters** like `"AA$"`: rank preservation still resolves ties
  correctly; the answer is `"AA$"`.
- **Validity assumption:** the problem guarantees the input is a real BWT, so exactly one
  `$` exists and the walk terminates after visiting every row exactly once.
