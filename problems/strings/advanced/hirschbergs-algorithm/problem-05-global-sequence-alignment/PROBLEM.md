# Global Sequence Alignment (Needleman–Wunsch) in Linear Space

**Difficulty:** Hard

**Source:** Needleman–Wunsch (1970) global alignment; linear-space traceback is Hirschberg (1975). This is the original application of Hirschberg's algorithm in computational biology.

## Description

Given two strings `a` and `b` and a scoring scheme

- `match` — score added when two aligned characters are equal (typically positive),
- `mismatch` — score when two aligned characters differ (typically negative),
- `gap` — score for aligning a character against a gap `-` (a negative penalty),

compute an **optimal global alignment**: insert gap characters `-` into `a` and `b` so the
two results have equal length and the total column score is **maximised**. Return the two
aligned strings (and, optionally, the score).

Every character of `a` and `b` must appear (in order) in its aligned string; deleting all
`-` from `a`'s aligned string must give back `a`, and likewise for `b`.

The requirement that makes this Hirschberg's flagship problem: produce the alignment using
only **`O(min(len(a), len(b)))` extra space**. A genome-scale alignment with the naive
`O(n·m)` table would need terabytes; Hirschberg reduces the memory to linear while keeping
the same `O(n·m)` time.

## Constraints

- `0 <= len(a), len(b) <= 10000`
- `a`, `b` consist of uppercase letters (e.g. DNA bases `A`, `C`, `G`, `T`).
- Scores are integers with `match > mismatch` and `gap < 0` (standard setting).
- Extra space (beyond inputs and the two output strings) must be `O(min(n, m))`; the full
  `O(n·m)` DP table may **not** be stored.
- Any alignment achieving the optimal score is accepted.

## Examples

Assume `match = +1`, `mismatch = -1`, `gap = -2` for both examples.

### Example 1
```
Input:  a = "TACG", b = "TCG"
Output: optimal score = 1, e.g.
        TACG
        T-CG
Explanation: T:T match (+1), A:- gap (-2), C:C match (+1), G:G match (+1) = +1.
No alignment scores higher.
```

### Example 2
```
Input:  a = "AGTA", b = "ATA"
Output: optimal score = 1, e.g.
        AGTA
        A-TA
Explanation: A:A (+1), G:- gap (-2), T:T (+1), A:A (+1) = +1. This beats forcing a
mismatch column, which would score lower with these penalties.
```

## Hint

The optimal alignment path is monotone, so it crosses the middle row of `a` at one column.
Locate that column with a forward and a backward linear-space score sweep (each keeps just
one row), split both strings there, and recurse — the general **Hirschberg's Algorithm**,
here maximising an affine-free (linear-gap) alignment score.
