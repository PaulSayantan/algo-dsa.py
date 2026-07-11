# Damerau-Levenshtein Distance — Solution

## Brute Force

Recurse exactly like plain edit distance, but add a fourth branch: whenever the
last two characters of both prefixes form a swapped pair, also try
`1 + rec(i-2, j-2)`. Take the minimum across insert, delete, replace, and (when
applicable) transpose.

- **Time:** `O(4^(m+n))` in the worst case — one extra branch on top of the
  three-way Levenshtein recursion, with massive recomputation.
- **Space:** `O(m + n)` recursion depth.

Overlapping subproblems again point straight to DP.

## Optimal Approach (Edit Distance (Levenshtein) + transposition)

Take the standard Levenshtein table and extend the recurrence with a
transposition transition. Define:

```
dp[i][j] = OSA Damerau-Levenshtein distance between a[:i] and b[:j]
```

**Base cases** (same as Levenshtein):

```
dp[i][0] = i     # delete all i characters
dp[0][j] = j     # insert all j characters
```

**Transition** for `i, j >= 1`:

```
cost = 0 if a[i-1] == b[j-1] else 1
dp[i][j] = min(
    dp[i-1][j] + 1,        # delete a[i-1]
    dp[i][j-1] + 1,        # insert b[j-1]
    dp[i-1][j-1] + cost,   # replace (or free match)
)

# transposition of adjacent characters
if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
    dp[i][j] = min(dp[i][j], dp[i-2][j-2] + 1)
```

The answer is `dp[m][n]`.

The transposition condition checks that the current last character of `a` equals
the second-to-last of `b`, and vice versa — exactly a swapped adjacent pair. If
so, we can convert `a[:i]` into `b[:j]` by first solving `a[:i-2]` -> `b[:j-2]`
and then paying one operation for the swap.

### OSA vs. "true" Damerau-Levenshtein

This solution implements **Optimal String Alignment (OSA)**, where each
substring is edited at most once. The classic textbook / interview answer.

The *unrestricted* Damerau-Levenshtein distance allows a region to be edited
again after a transposition. The two metrics can differ. For example, with
`a = "ca"`, `b = "abc"`:

- **OSA distance = 3** (a swap then further edits would touch the same region
  twice, which OSA forbids).
- **True Damerau-Levenshtein distance = 2**.

The unrestricted version needs a more involved algorithm that tracks, for each
character, the last row where it appeared (an `O(m * n)` DP over an alphabet with
sentinel rows/columns). For most spell-checkers and interviews, OSA is what is
expected; mention the distinction if asked.

### Why OSA is correct

Every operation affects only the tail of the two prefixes:

- insert/delete/replace behave exactly as in Levenshtein and reference the three
  standard neighbors;
- a transposition of the two trailing characters reduces the problem to
  `a[:i-2]` -> `b[:j-2]` for one unit of cost, and the guard guarantees those two
  characters really are a swapped pair.

Taking the minimum over these mutually exhaustive "last move" choices, filled in
increasing prefix order, yields the optimum by induction. The OSA "edit each
region once" property is exactly what makes the simple `dp[i-2][j-2] + 1` term
valid — we never revisit the swapped positions.

### Reference implementation

```python
class Solution:
    def damerauLevenshtein(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if a[i - 1] == b[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,        # delete
                    dp[i][j - 1] + 1,        # insert
                    dp[i - 1][j - 1] + cost, # replace / match
                )
                if (i > 1 and j > 1
                        and a[i - 1] == b[j - 2]
                        and a[i - 2] == b[j - 1]):
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)
        return dp[m][n]
```

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)`. A rolling-window version needs the last **two** rows
  (because the transposition term reads `dp[i-2][...]`), giving `O(n)`.

## Key Insights & Edge Cases

- **Transposition only fires on adjacent swaps** and requires `i > 1 and j > 1`;
  guarding these indices prevents out-of-range access.
- **Rolling arrays must keep two prior rows**, not one, unlike plain Levenshtein
  — the most common bug when optimizing space here.
- **OSA vs. unrestricted DL:** they diverge on inputs like `"ca"` -> `"abc"`
  (OSA = 3, true DL = 2). Know which one is being asked for.
- **Verification:** `"ca"`/`"ac"` and `"teh"`/`"the"` each cost 1 via one swap;
  `"sitting"`/`"kitten"` has no useful swap and stays at 3 (equal to plain
  Levenshtein).
- **Equal strings** cost 0; when no adjacent swaps apply, the result equals the
  ordinary Levenshtein distance.
