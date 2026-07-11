# Solution — Minimum ASCII Delete Sum for Two Strings

## Brute Force

Try every subset of characters to delete from `s1` and every subset from `s2`, keep the
pairs of subsets whose leftovers are equal, and take the minimum deleted ASCII sum. This is
exponential in both lengths (`2^n · 2^m`) and impossible for lengths up to 1000.

- **Time:** `O(2^n · 2^m)`
- **Space:** exponential

## Optimal Approach (Wagner–Fischer, ASCII-weighted deletions)

This is the delete-only edit-distance DP from Problem 2, except each deletion is charged
`ord(char)` rather than `1`. Let

```
dp[i][j] = minimum ASCII delete sum to make s1[:i] equal to s2[:j]
```

**Recurrence**

```
dp[0][0] = 0
dp[i][0] = dp[i-1][0] + ord(s1[i-1])     # must delete every char of s1's prefix
dp[0][j] = dp[0][j-1] + ord(s2[j-1])     # must delete every char of s2's prefix

if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1]                          # keep the matched pair, cost 0
else:
    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]),        # delete s1[i-1]
                   dp[i][j-1] + ord(s2[j-1]))        # delete s2[j-1]
```

The answer is `dp[n][m]`.

```python
def minimumDeleteSum(self, s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),
                               dp[i][j - 1] + ord(s2[j - 1]))
    return dp[n][m]
```

- **Time:** `O(n · m)`
- **Space:** `O(n · m)`, reducible to `O(min(n, m))` with a rolling row.

**Why it is correct.** Making the strings equal by deletions means keeping a common
subsequence and removing everything else. The total cost is the ASCII sum of *all*
characters minus twice the ASCII sum of the kept common subsequence — so minimizing deleted
ASCII is equivalent to maximizing the ASCII weight of the common subsequence. The DP builds
the optimum over prefixes: a matching pair can be kept for zero cost (`dp[i-1][j-1]`), and
on a mismatch we pay to delete whichever character we skip, taking the cheaper of the two
directions. Base rows/columns encode that emptying a prefix forces deleting every character
in it.

**Equivalent "max-kept" formulation.** Let `total = sum(ord(c) for c in s1) + sum(ord(c)
for c in s2)` and let `W` be the maximum ASCII weight of a common subsequence (a weighted
LCS). Then the answer is `total - 2·W`.

## Key Insights & Edge Cases

- **Greedy is wrong.** Deleting the cheapest characters, or matching greedily, does not
  yield the minimum — a low-ASCII match may block a more valuable one. Only the DP explores
  all alignments.
- **Base cases are cumulative sums, not indices.** Unlike `dp[i][0] = i` in unweighted edit
  distance, here `dp[i][0]` accumulates the ASCII values of `s1[:i]`.
- **Matches are free but not forced.** Even when `s1[i-1] == s2[j-1]`, keeping the pair is
  optimal here (both would otherwise be deleted, and `ord` is positive), so the equal branch
  can safely take the diagonal without a `min`.
- **Identical strings** → cost `0`. **Disjoint alphabets** → delete everything:
  `sum(ord(c) for c in s1) + sum(ord(c) for c in s2)` (e.g. `"a"` vs `"b"` → `97 + 98 = 195`).
- **All costs positive**, so there is never an incentive to delete a shared character you
  could have kept — which is what makes the "keep = free diagonal" step valid.
