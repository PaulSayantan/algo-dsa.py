# Solution — Shortest Common Supersequence

## Brute Force

Try every string in increasing length and test whether it is a supersequence of both
inputs, or enumerate all interleavings. This is exponential and hopeless beyond tiny
inputs.

A polynomial baseline builds the full `O(n·m)` SCS DP table (or LCS table) and backtracks
to interleave.

- **Time:** `O(n·m)`
- **Space:** `O(n·m)` — the table is retained for the backtrack.

## Optimal Approach — Merge Along a Linear-Space LCS

**Key identity.** `len(SCS) = len(str1) + len(str2) - len(LCS(str1, str2))`. Every
character of both strings must appear; the only characters you can *share* (write once
instead of twice) are those that line up as a common subsequence, and the most you can
share is the longest common subsequence. So an SCS is exactly: walk `str1` and `str2`
together, and for each character `c` of a chosen LCS, first flush the private (non-LCS)
characters of `str1` and then of `str2` that precede `c`, write `c` once, and advance past
it in both strings. Finally append the leftover tails.

Because we only need the LCS *string*, we recover it in linear space with Hirschberg's
algorithm (Problem 2), then do a single linear interleave pass.

```python
from typing import List


def lcs_score_row(a: str, b: str) -> List[int]:
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        curr = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            if ai == b[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = prev[j] if prev[j] >= curr[j - 1] else curr[j - 1]
        prev = curr
    return prev


def hirschberg_lcs(a: str, b: str) -> str:
    n, m = len(a), len(b)
    if n == 0 or m == 0:
        return ""
    if n == 1:
        return a if a in b else ""
    mid = n // 2
    L = lcs_score_row(a[:mid], b)
    R = lcs_score_row(a[mid:][::-1], b[::-1])
    best_k, best = 0, -1
    for k in range(m + 1):
        s = L[k] + R[m - k]
        if s > best:
            best, best_k = s, k
    return hirschberg_lcs(a[:mid], b[:best_k]) + hirschberg_lcs(a[mid:], b[best_k:])


def shortest_common_supersequence(str1: str, str2: str) -> str:
    lcs = hirschberg_lcs(str1, str2)
    out = []
    i = j = 0
    for c in lcs:
        while str1[i] != c:      # flush str1's private run before c
            out.append(str1[i]); i += 1
        while str2[j] != c:      # flush str2's private run before c
            out.append(str2[j]); j += 1
        out.append(c)            # write the shared char once
        i += 1
        j += 1
    out.append(str1[i:])         # trailing tails
    out.append(str2[j:])
    return "".join(out)
```

### Why it is correct

- `hirschberg_lcs` returns a genuine LCS of maximal length (proved in Problem 2), so the
  number of shared characters is maximised and the produced string has minimal length
  `len(str1) + len(str2) - len(LCS)`.
- The interleave keeps every character of `str1` and `str2` in its original relative
  order, so both are subsequences of the result. Because each LCS character is emitted
  once (not twice) and every private character exactly once, the length matches the SCS
  identity — confirmed against the DP length formula over thousands of random pairs.

### Complexity

- **Time:** `O(n·m)` — dominated by the Hirschberg LCS; the interleave is `O(n + m)`.
- **Space:** `O(min(n, m))` for Hirschberg's rolling rows and `O(log n)` stack, plus the
  `O(n + m)` output.

## Key Insights & Edge Cases

- **No shared characters** (`"abc"`, `"def"`): the LCS is empty, both `while` loops never
  match a guide character, and you just concatenate the two strings — length `n + m`.
- **One string is a subsequence of the other** (e.g. `str2 ⊑ str1`): the LCS equals
  `str2`, so the SCS is just `str1`.
- **Multiple valid answers:** the specific LCS chosen (and its tie-breaks) determines which
  shortest supersequence you emit; all have the same minimal length.
- **The linear-space win is entirely in the LCS step;** never build the SCS DP table
  directly, or you re-introduce `O(n·m)` space.
- **Interleave invariant:** after the loop, `str1[i:]` and `str2[j:]` are the untouched
  suffixes past the last LCS character and must both be appended.
