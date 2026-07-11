# One Edit Distance — Solution

## Brute Force

Compute the full Levenshtein edit distance between `s` and `t` with the standard
`O(m * n)` DP table, then return `True` if and only if the distance equals `1`.

- **Time:** `O(m * n)` where `m = len(s)`, `n = len(t)`.
- **Space:** `O(m * n)` (or `O(min(m, n))` with a rolling row).

This works, but it is wasteful: we only care whether the distance is exactly 1,
so we can stop the moment we have seen more than one difference.

## Optimal Approach (Edit Distance (Levenshtein), specialized)

The single-edit constraint pins down the length relationship between `s` and
`t`. Let `m = len(s)` and `n = len(t)`.

1. **Length gate.** If `|m - n| > 1`, more than one edit is required, so return
   `False` immediately. Assume WLOG `m <= n` (swap if needed so `s` is the
   shorter one).
2. **Scan to the first mismatch.** Walk both strings in lockstep until the
   characters differ at some index `i`.
   - If we reach the end of the shorter string with no mismatch, the strings
     share a common prefix. They are one edit apart **iff** their lengths differ
     by exactly 1 (a single trailing insert/delete). Equal length here means the
     strings are identical -> `False`.
3. **Resolve the first mismatch at index `i`.**
   - **Equal lengths (`m == n`):** the only allowed edit is a *replace*. The two
     strings must be identical after position `i`, i.e. `s[i+1:] == t[i+1:]`.
   - **Lengths differ by 1 (`n == m + 1`):** the only allowed edit is an
     *insert into `s`* (equivalently a delete from `t`). Skip the extra
     character in the longer string and require the remainders to match, i.e.
     `s[i:] == t[i+1:]`.

Because a valid one-edit transformation can differ in at most one spot, finding
a second mismatch (or the wrong length relationship) proves the answer is
`False`.

### Why it is correct

Each Levenshtein operation changes the strings in a very local way:

- A **replace** keeps lengths equal and alters exactly one position; everything
  before and after that position must match.
- An **insert/delete** makes the lengths differ by one; before the edit point
  the strings match, and after it the shorter string's suffix must equal the
  longer string's suffix shifted by one.

The scan verifies exactly these conditions, and the length gate rejects
anything needing two or more edits.

### Reference implementation

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:                      # ensure s is the shorter (or equal) one
            return self.isOneEditDistance(t, s)
        if n - m > 1:                  # too far apart in length
            return False

        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    # replace: rest must match
                    return s[i + 1:] == t[i + 1:]
                # insert into s / delete from t: skip t[i]
                return s[i:] == t[i + 1:]

        # no mismatch in the shared prefix -> must differ by a trailing char
        return m + 1 == n
```

- **Time:** `O(min(m, n))` — a single linear scan; slicing comparisons are also
  linear.
- **Space:** `O(1)` extra (ignoring the slices, which can be replaced by index
  comparisons for true `O(1)`).

## Key Insights & Edge Cases

- **Identical strings return `False`.** Zero edits is not one edit. This is the
  most commonly missed case.
- **Length difference of 2 or more** is an instant `False`.
- **Empty string cases:** `s = ""`, `t = "a"` -> `True` (one insert). `s = ""`,
  `t = ""` -> `False` (zero edits).
- **Mismatch resolution depends on the length relationship:** equal lengths
  force a replace; a length difference of one forces an insert/delete. Mixing
  these up is the classic bug.
- Making `s` the shorter string first removes the need to handle two symmetric
  cases separately.
