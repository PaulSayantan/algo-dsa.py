# Delete Operation for Two Strings — Solution

## Brute Force

Enumerate every subsequence of `word1` and check whether it is also a
subsequence of `word2`, tracking the longest common one. If the longest common
subsequence (LCS) has length `L`, the answer is `(m - L) + (n - L)` where
`m = len(word1)`, `n = len(word2)`.

- **Time:** `O(2^m * n)` — exponential in the number of subsequences.
- **Space:** `O(m)` recursion depth.

Hopeless for `m, n` up to 500.

## Optimal Approach (Edit Distance (Levenshtein) with deletions only)

Because only *deletions* are allowed, the characters that remain in both strings
must appear in the **same relative order** in each — that is precisely a common
subsequence. To minimize deletions we keep as many characters as possible, i.e.
the **longest common subsequence**. Everything else is deleted.

If `L = LCS(word1, word2)`, then:

```
answer = (m - L) + (n - L) = m + n - 2 * L
```

### LCS by dynamic programming

Let `dp[i][j]` be the length of the LCS of the first `i` characters of `word1`
and the first `j` characters of `word2`.

```
dp[0][j] = 0        # empty prefix of word1
dp[i][0] = 0        # empty prefix of word2

if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1        # extend the common subsequence
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])   # drop one character, take the best
```

The answer is `m + n - 2 * dp[m][n]`.

### Direct deletion DP (equivalent framing)

You can also define `dp[i][j]` as the *minimum deletions* to make the two
prefixes equal, which mirrors the Levenshtein recurrence with only the delete
transitions kept:

```
dp[i][0] = i        # delete all i chars of word1
dp[0][j] = j        # delete all j chars of word2

if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])   # delete from word1 or word2
```

Both formulations give the same result; the LCS view is the most memorable.

### Why it is correct

A surviving alignment matches characters of `word1` with equal characters of
`word2` in increasing index order — the definition of a common subsequence. Any
character not part of this alignment must be deleted from its own string, and
each deletion is one step. Minimizing total deletions is therefore equivalent to
maximizing the matched (kept) characters, which is the LCS. The DP explores
every prefix pair once with optimal substructure, so it finds the true optimum.

### Reference implementation

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs = dp[m][n]
        return m + n - 2 * lcs
```

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)`, reducible to `O(min(m, n))` with a rolling row since
  each row depends only on the previous one.

## Key Insights & Edge Cases

- **Insert/replace are forbidden**, which collapses the general edit distance
  into the LCS problem — recognizing this is the whole trick.
- **Formula check:** for `"sea"`/`"eat"`, LCS is `"ea"` (length 2), so
  `3 + 3 - 2*2 = 2`. For `"leetcode"`/`"etco"`, LCS is `"etco"` (length 4), so
  `8 + 4 - 2*4 = 4`.
- **Equal strings** -> LCS = full length -> answer 0.
- **No common characters** -> LCS = 0 -> answer `m + n` (delete everything from
  both). Example: `"abc"`, `"xyz"` -> 6.
- One string being empty -> delete the entire other string.
