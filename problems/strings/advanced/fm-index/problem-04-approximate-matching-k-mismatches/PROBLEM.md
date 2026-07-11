# Approximate Matching (k Mismatches)

**Difficulty:** Hard

Source: Bioinformatics read alignment (BWA / Bowtie use branching backward search
over an FM-Index); classic "approximate string matching with k mismatches"

## Description

You are given a fixed text `T` and a pattern `P` of length `m`. Count the number
of positions where `P` aligns to `T` with **at most `k` mismatches** under the
Hamming distance — that is, the number of start indices `i` (with
`0 <= i <= n - m`) such that `P` and `T[i : i + m]` differ in at most `k`
character positions. Insertions and deletions are **not** allowed (equal-length
alignment only).

This is the core operation of DNA read alignment: map a short read against a
reference genome allowing a handful of sequencing errors. The FM-Index solves it
with a **branching backward search** — at each pattern position you may follow
the matching character (cost 0) or any other character (cost 1), pruning as soon
as the mismatch budget is exceeded or the BWT interval empties.

Return the total number of valid alignment start positions (counting overlapping
alignments separately).

## Constraints

- `1 <= n <= 5 * 10^4`
- `1 <= m <= 50`
- `0 <= k <= 3`
- `T` and `P` are over a small alphabet (e.g. `{a, c, g, t}` or lowercase
  letters).
- Overlapping alignments are counted separately.

## Examples

### Example 1
```
Input:
  T = "acgtacgt", P = "acg", k = 0
Output:
  2
Explanation:
  With 0 mismatches this is exact matching. "acg" occurs at indices 0 and 4.
```

### Example 2
```
Input:
  T = "acgtacgt", P = "aca", k = 1
Output:
  2
Explanation:
  "aca" vs T[0:3]="acg": differs only at the last position (a vs g) -> 1 mismatch, OK.
  "aca" vs T[4:7]="acg": likewise 1 mismatch, OK.
  No other window is within 1 mismatch, so the count is 2.
```

### Example 3
```
Input:
  T = "mississippi", P = "issa", k = 1
Output:
  2
Explanation:
  "issa" vs T[1:5]="issi": differ only at the last char (a vs i) -> 1 mismatch, OK.
  "issa" vs T[4:8]="issi": same, 1 mismatch, OK.
  All other windows differ in 2+ positions, so the count is 2.
```

## Hint

Use the **FM-Index** with **branching backward search**. Recurse over the pattern
from right to left carrying a remaining mismatch budget. At each step try every
alphabet character `c`: the BWT interval update `C[c] + Occ(c, .)` is the same as
exact search, but spend one unit of budget when `c` differs from the current
pattern character. Prune branches whose interval is empty or whose budget is
negative; when the whole pattern is consumed, add the interval width to the total.
