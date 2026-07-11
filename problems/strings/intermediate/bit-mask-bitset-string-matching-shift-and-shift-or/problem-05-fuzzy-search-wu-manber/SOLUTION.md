# Solution — Fuzzy Substring Search (Wu-Manber)

## Brute Force

Run the classic approximate-search dynamic program. Let `C[i][j]` be the minimum
edit distance between `pattern[0..j-1]` and *any* substring of `text` ending at
`text[i-1]`. Set `C[i][0] = 0` (a match may start anywhere) and `C[0][j] = j`
(deleting the first `j` pattern chars). Then

```
C[i][j] = min(
    C[i-1][j-1] + (text[i-1] != pattern[j-1]),  # match / substitution
    C[i-1][j]   + 1,                             # delete a text char (insertion into pattern)
    C[i][j-1]   + 1,                             # delete a pattern char
)
```

Report end position `i-1` whenever `C[i][m] <= k`.

```python
def fuzzy_search_ends(text, pattern, k):
    n, m = len(text), len(pattern)
    prev = list(range(m + 1))   # C[0][j] = j
    ends = []
    for i in range(1, n + 1):
        cur = [0] * (m + 1)     # cur[0] = 0
        for j in range(1, m + 1):
            cost = 0 if text[i-1] == pattern[j-1] else 1
            cur[j] = min(prev[j-1] + cost, prev[j] + 1, cur[j-1] + 1)
        if cur[m] <= k:
            ends.append(i - 1)
        prev = cur
    return ends
```

- **Time:** `O(n * m)`.
- **Space:** `O(m)` with the rolling-row optimization.

## Optimal Approach — Wu-Manber bit-parallel recurrence

Wu-Manber packs each DP *row* into `k+1` bitmasks and updates them with shifts and
ORs, replacing the inner `O(m)` loop with `O(k)` word operations. Keep state words
`R[0], ..., R[k]`:

> **Invariant:** after processing `text[0..pos]`, bit `j` of `R[d]` is set iff
> `pattern[0..j]` can be matched to a substring of `text` ending at `pos` using at
> most `d` edits.

### Initialization

`R[d] = (1 << d) - 1` for each `d`. This encodes the `C[0][j] = j` boundary: before
reading any text, a prefix of length up to `d` is reachable using `d` deletions of
pattern characters, so the low `d` bits of `R[d]` start set.

### The four update terms

For each text character `c` (with mask `bc = B[c]`), let `old` be the previous
step's `R` and `new` the values being computed left-to-right by increasing `d`:

```
new[0] = ((old[0] << 1) | 1) & bc

new[d] =  (((old[d] << 1) | 1) & bc)   # (a) match: extend & require pattern[j]==c
        |  old[d-1]                     # (b) deletion of a pattern char (no shift, one edit)
        | ((old[d-1] << 1) | 1)         # (c) substitution: advance regardless of c
        |  (new[d-1] << 1)              # (d) insertion of a text char (uses THIS step)
```

- **(a)** is ordinary Shift-And: keep prefixes whose next char equals `c`.
- **(b) deletion in pattern:** a prefix of length `j+1` at cost `d` is reachable if
  the length-`j+1` prefix was reachable at cost `d-1` at the *same* text position —
  we skip a pattern character. No shift; it reuses `old[d-1]` at the same bit.
  (Wu-Manber's original writes this as `R'[d-1]` combined with `R[d-1]`; the
  `old[d-1] | (new[d-1] << 1)` pairing below captures both deletion and insertion.)
- **(c) substitution:** advance the prefix (shift) and accept `c` no matter what,
  spending one edit — so it draws from `old[d-1]`.
- **(d) insertion in text:** consume a text char without advancing the pattern
  matched so far at this level; it references `new[d-1]` (the value already computed
  this step) shifted up.

A match ends at `pos` exactly when bit `m-1` of `R[k]` (i.e. `new[k]`) is set.

### Reference implementation

```python
from typing import List

def fuzzy_search_ends(text: str, pattern: str, k: int) -> List[int]:
    m = len(pattern)
    if m == 0:
        return list(range(len(text)))
    B = {}
    for j, c in enumerate(pattern):
        B[c] = B.get(c, 0) | (1 << j)
    match_bit = 1 << (m - 1)
    R = [(1 << d) - 1 for d in range(k + 1)]
    ends: List[int] = []
    for pos, c in enumerate(text):
        bc = B.get(c, 0)
        old = R[:]
        new = [0] * (k + 1)
        new[0] = ((old[0] << 1) | 1) & bc
        for d in range(1, k + 1):
            new[d] = ((((old[d] << 1) | 1) & bc)
                      | old[d - 1]
                      | ((old[d - 1] << 1) | 1)
                      | (new[d - 1] << 1))
        R = new
        if R[k] & match_bit:
            ends.append(pos)
    return ends
```

### Worked example — `text = "hello"`, `pattern = "hallo"`, `k = 1`

`m = 5`, `match_bit = 0b10000`, `B = {h:00001, a:00010, l:01100, o:10000}`.
Distance("hello","hallo") = 1 (substitute `e`→`a`). Tracing `R[1]`, only after
consuming the full `"hello"` (index 4) does bit 4 of `R[1]` light up, giving end
position `[4]`. With `k = 0` the substitution term is unavailable, so `R[0]` never
reaches bit 4 and the result is `[]` — matching the stated examples.

### Complexity

- **Time:** `O(n * k * ceil(m/w))`; with `m <= w` this is `O(n * k)` — a factor of
  `m/(k)` faster than the `O(n*m)` DP when `k` is small.
- **Space:** `O(k)` state words plus `O(sigma)` masks.

## Key Insights & Edge Cases

- **Report end positions, not starts:** with insert/delete the matched substring's
  length varies, so a single end position may correspond to several start positions.
  End positions are the automaton's natural, unambiguous output. To recover a start,
  re-run a small local DP anchored at the reported end.
- **`k = 0`** removes terms (b), (c), (d) (they all reference level `-1`), leaving
  plain Shift-And exact matching — end positions of exact occurrences.
- **Initialization is essential:** starting `R[d]` at `0` instead of `(1<<d)-1`
  would miss matches that begin with pattern deletions; the `(1<<d)-1` seed encodes
  the `C[0][j]=j` DP boundary.
- **Update order within a step:** compute `new[d]` for increasing `d` because the
  insertion term (d) depends on `new[d-1]` (this step), while (a)-(c) depend on
  `old[*]` (previous step). Snapshot `old = R[:]` to keep the two apart.
- **Overshoot on `k`:** if `k >= m` essentially every position matches; the
  recurrence still behaves correctly, just with saturated masks.
- **Practical note:** this is the engine of `agrep` and fuzzy finders; for
  `m <= 64` it is extremely fast because each level is a handful of word ops.
