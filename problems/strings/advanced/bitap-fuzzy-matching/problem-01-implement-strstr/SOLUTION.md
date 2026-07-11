# Solution — Implement strStr() (Bitap shift-or)

## Brute Force

Try every start position `s` in `haystack` and compare `haystack[s : s + m]` to `needle` character by
character.

```python
def strStr(haystack, needle):
    m, n = len(needle), len(haystack)
    if m == 0:
        return 0
    for s in range(n - m + 1):
        if haystack[s:s + m] == needle:
            return s
    return -1
```

- **Time:** `O(n · m)` in the worst case (e.g. `haystack = "aaaa…a"`, `needle = "aa…ab"`).
- **Space:** `O(1)` extra (ignoring the slice).

## Optimal Approach — Bitap / shift-or

### The state we track

Let `m = len(needle)`. Keep a single integer register `R` of `m` bits. We maintain the invariant:

> **Bit `j` of `R` is set** after reading text prefix `text[0..i]` **iff** the pattern prefix
> `needle[0..j]` (length `j+1`) equals the text suffix `text[i-j..i]`.

In words, `R` records *every* pattern prefix that currently aligns with a suffix ending at the character we
just consumed. A **full match** ends at position `i` exactly when the top bit `1 << (m-1)` is set.

### Preprocessing: the character-position masks

For each character `c`, `peq[c]` has bit `j` set iff `needle[j] == c`:

```python
peq = {}
for j, ch in enumerate(needle):
    peq[ch] = peq.get(ch, 0) | (1 << j)
```

### The update

For each incoming text character `c`:

```
R = ((R << 1) | 1) & peq[c]
```

- `R << 1` shifts every "matched prefix of length `j+1`" up to "candidate prefix of length `j+2`".
- `| 1` seeds bit 0, i.e. *the length-1 prefix could start here* (a fresh attempt at matching `needle[0]`).
- `& peq[c]` keeps a candidate at position `j` only if `needle[j] == c`, extending the match one character.

### Reference implementation

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m == 0:
            return 0
        peq = {}
        for j, ch in enumerate(needle):
            peq[ch] = peq.get(ch, 0) | (1 << j)
        R = 0
        top = 1 << (m - 1)
        for i, c in enumerate(haystack):
            R = ((R << 1) | 1) & peq.get(c, 0)
            if R & top:
                return i - m + 1   # match ended at i, so it started here
        return -1
```

### Why it is correct

Induction on the update rule preserves the invariant above: a prefix of length `j+1` matches a suffix ending
at `i` iff a prefix of length `j` matched a suffix ending at `i-1` (that is `R`'s bit `j-1` before the shift,
which the `<< 1` moves to bit `j`) **and** `needle[j] == text[i]` (enforced by `& peq[c]`); the `| 1` accounts
for the length-1 base case. When bit `m-1` is set, the whole pattern matched, ending at `i`, i.e. starting at
`i - m + 1`. Returning on the first such `i` gives the first (leftmost) occurrence.

### Complexity

- **Preprocessing:** `O(m + σ)` to build `peq` (`σ` = alphabet size).
- **Search:** each text character costs `O(⌈m / w⌉)` word operations (`w` = machine word width). For
  `m <= w` this is `O(1)` per character, giving `O(n)` overall. In general `O(n · ⌈m / w⌉)`.
- **Space:** `O(σ · ⌈m / w⌉)` for the masks.

## Key Insights & Edge Cases

- **Empty needle → return 0.** Handle it before touching `R` (a 0-bit register has no "top bit").
- **`shift-or` vs `shift-and`.** This write-up uses the *active-bit* (`shift-and`) convention: a set bit means
  "matched". The historically named *shift-or* variant flips the polarity (0 = matched) so the update becomes
  `R = (R << 1) | notpeq[c]`, which avoids the `| 1` step; both are equivalent. Pick one convention and be
  consistent.
- **Unknown characters.** Use `peq.get(c, 0)`; a character not in the pattern has mask `0`, which correctly
  clears all candidate prefixes.
- **Long patterns.** If `m > w`, the register spans multiple words and you carry bits across them, degrading
  to `O(n · ⌈m / w⌉)`. Python's arbitrary-precision integers hide this but it is still true asymptotically.
- **This is the foundation.** Every later problem in this folder reuses the exact same `peq` table and the same
  `((R << 1) | 1) & peq[c]` heartbeat — only the *number* of registers and how they combine changes.
