# Strange Printer — Solution

## Brute Force

Model the printing process forward: at each state (current partially-printed
string) try every possible print (any character over any contiguous range) and
search for the shortest sequence of turns reaching `s`. The state space of
partial strings is astronomically large.

- **Time:** super-exponential; intractable even for small `n`.
- **Space:** exponential.

## Optimal Approach (Range / Interval DP)

Think **backwards / structurally** about the final string on an interval.

> `dp[i][j]` = minimum turns to print the substring `s[i..j]`.

Consider the leftmost character `s[i]`. In the worst case you spend one turn to
paint `s[i]` and then print the rest: `dp[i][j] = 1 + dp[i+1][j]`. But you can do
better whenever some later position `k` (`i < k <= j`) has `s[k] == s[i]`: the
single stroke that prints `s[i]` can be **extended to also cover position `k`**
in the same turn. That merge saves the separate turn `k` would otherwise need,
which is captured by combining the interior and the tail:

**Recurrence:**
```
dp[i][j] = 1 + dp[i+1][j]                              # base: paint s[i] alone
for k in (i, j]:
    if s[k] == s[i]:
        dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
```
Here `dp[i+1][k-1]` handles the region strictly between the two equal characters,
and `dp[k][j]` handles from `k` onward — and because `s[i]` and `s[k]` are the
same and printed together, we do **not** add an extra turn at the merge.

**Base case:** `dp[i][i] = 1` (one character, one turn); `dp[i][j] = 0` for
`i > j`.

**Why it is correct.** The first character `s[i]` must be printed by some stroke.
Either that stroke covers only `s[i]`'s own run (cost `1 + dp[i+1][j]`), or it is
extended rightward to end at some later equal character `s[k]`; everything
strictly inside `(i, k)` must then be reprinted on top (`dp[i+1][k-1]`), and the
suffix from `k` is solved independently with `s[k]` "free" because it shares the
stroke with `s[i]`. Taking the min over all matching `k` covers all optimal
structures.

**Optional optimization:** first collapse consecutive duplicate characters
(`"aaabbb"` -> `"ab"`); they never change the answer and shrink `n`.

```python
from functools import lru_cache

class Solution:
    def strangePrinter(self, s: str) -> int:
        # collapse runs of equal characters
        squeezed = []
        for c in s:
            if not squeezed or squeezed[-1] != c:
                squeezed.append(c)
        s = "".join(squeezed)
        n = len(s)
        if n == 0:
            return 0

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            best = dp(i + 1, j) + 1
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    best = min(best, dp(i + 1, k - 1) + dp(k, j))
            return best

        return dp(0, n - 1)
```

- **Time:** `O(n^3)` — `O(n^2)` intervals, `O(n)` matching positions each.
- **Space:** `O(n^2)` for the memo table.

### Trace for `s = "aba"`

`dp(0,2)`: base `1 + dp(1,2) = 1 + 2 = 3`. Try `k = 2` (`s[2]='a' == s[0]`):
`dp(1,1) + dp(2,2) = 1 + 1 = 2`. So `dp(0,2) = 2` — the outer `a`s share one
stroke, and the middle `b` is one more. Answer `2`.

## Key Insights & Edge Cases

- The merge rule "**do not pay again when `s[k] == s[i]`**" is the interval-DP
  heart: equal endpoints let two prints collapse into one, exactly like the
  endpoint-matching bonus in Longest Palindromic Subsequence — but here it saves
  a *turn* rather than adding length.
- **Collapsing consecutive duplicates** is a clean preprocessing win and avoids
  off-by-one confusion; it never changes the minimum turns.
- **Single character** returns `1`; a string of one repeated character (e.g.
  `"aaaa"`) collapses to length 1 and returns `1`.
- Closely related to "Remove Boxes"; both reward grouping equal characters across
  an interval, though Remove Boxes needs an extra count dimension.
- Use memoized recursion or fill by increasing interval length — never iterate
  `i, j` in the naive nested order.
