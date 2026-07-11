# Solution — Shortest Common Supersequence

## Brute Force

Generate candidate supersequences (e.g. try every interleaving of `str1` and `str2`, or
every string over the alphabet in increasing length) and keep the shortest one that contains
both inputs as subsequences. The number of interleavings of two length-`n` strings is
`C(2n, n)`, which explodes well before the constraint limit of 1000.

- **Time:** exponential (`~C(n+m, n)` interleavings to test)
- **Space:** exponential

## Optimal Approach (Wagner–Fischer relative: LCS table + backward reconstruction)

The shortest common supersequence (SCS) is built directly from the alignment produced by
the Longest Common Subsequence (LCS) — the same 2D prefix DP as Wagner–Fischer, just
maximizing matches instead of minimizing edits. Every character of the LCS is written
**once** in the SCS; every non-LCS character of each string is written where it belongs.
Hence

```
len(SCS) = len(str1) + len(str2) − len(LCS(str1, str2))
```

**Step 1 — Fill the LCS table.**

```
dp[i][j] = length of LCS of str1[:i] and str2[:j]

if str1[i-1] == str2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Step 2 — Walk backward from `dp[n][m]` to reconstruct the merged string.** At cell
`(i, j)`:

- If `str1[i-1] == str2[j-1]`: this is a shared character — emit it once, step diagonally to
  `(i-1, j-1)`.
- Else if `dp[i-1][j] >= dp[i][j-1]`: emit `str1[i-1]` (a character unique to `str1` on this
  path), step up to `(i-1, j)`.
- Else: emit `str2[j-1]`, step left to `(i, j-1)`.

When one index hits 0, flush the remaining prefix of the other string. The characters are
emitted in reverse, so reverse the result at the end.

```python
def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    out = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            out.append(str1[i - 1]); i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            out.append(str1[i - 1]); i -= 1
        else:
            out.append(str2[j - 1]); j -= 1
    while i > 0:
        out.append(str1[i - 1]); i -= 1
    while j > 0:
        out.append(str2[j - 1]); j -= 1
    return "".join(reversed(out))
```

- **Time:** `O(n · m)` to fill the table; `O(n + m)` to reconstruct.
- **Space:** `O(n · m)` — the full table is **required** because reconstruction walks it
  backward (this is why the space cannot be compressed here, unlike a pure distance query).

**Why it is correct.** Any common supersequence must contain, in order, every character of
`str1` and every character of `str2`; the only chances to "reuse" a single character for both
are the positions where the two strings agree along a common subsequence. Reusing the
*longest* common subsequence overlaps the maximum possible number of characters, giving the
minimum length `n + m − LCS`. The backward walk realizes exactly such a merge: diagonal steps
overlap a shared LCS character, while up/left steps splice in a character that belongs to only
one string, preserving both strings' internal order.

## Key Insights & Edge Cases

- **SCS length = `n + m − LCS`.** Example 1: `4 + 3 − 2 = 5`. This ties the problem directly
  to the LCS/edit-distance table family.
- **Reconstruction needs the full 2D table.** The `O(min(n,m))` rolling-array trick works for
  the *length* but throws away the information needed to rebuild the string.
- **Tie-break direction is a free choice.** Using `>=` versus `>` when `dp[i-1][j] == dp[i][j-1]`
  changes *which* shortest supersequence you get, not its length — both are accepted.
- **Identical strings** → the string itself (LCS covers everything; no extra characters).
- **Disjoint alphabets** (LCS = 0) → any concatenation `str1 + str2` (or `str2 + str1`) of
  length `n + m` is a valid shortest answer.
- **Off-by-one in indexing.** `dp` is `(n+1) × (m+1)`; string characters are `str1[i-1]` and
  `str2[j-1]` when reading cell `(i, j)`.
