# Palindrome Partitioning II — Solution

## Brute Force

Recursively try every cut position: for each prefix `s[0..k]` that is a
palindrome, recurse on the remaining suffix and add one cut. Testing each prefix
for palindrome-ness is `O(n)`, and the branching is exponential.

- **Time:** `O(2^n * n)` in the worst case (e.g. all identical characters).
- **Space:** `O(n)` recursion depth.

## Optimal Approach (Range / Interval DP + linear min-cut DP)

This problem is a great example of **interval DP as a preprocessing step**. It has
two phases.

### Phase 1 — interval DP for the palindrome table

> `isPal[i][j]` = `True` iff `s[i..j]` (inclusive) is a palindrome.

**Recurrence** (compare the two endpoints of the interval):
```
isPal[i][j] = (s[i] == s[j]) and (j - i < 2 or isPal[i+1][j-1])
```
- `j - i < 2` covers length-1 and length-2 intervals, which are palindromes as
  soon as their endpoints match.
- Otherwise the inner interval `[i+1, j-1]` must also be a palindrome.

Because `isPal[i][j]` depends on the shorter interval `isPal[i+1][j-1]`, fill by
iterating `i` from `n-1` down to `0` and `j` from `i` up to `n-1`. This is a
textbook `O(n^2)` interval DP.

### Phase 2 — min-cut DP

> `cut[i]` = minimum cuts needed for the prefix `s[0..i]`.

**Recurrence:**
```
cut[i] = 0                      if isPal[0][i]        (whole prefix is a palindrome)
cut[i] = min over k in [1, i] of  cut[k-1] + 1        if isPal[k][i]
```
The second line says: place the last palindromic piece as `s[k..i]`, having
already optimally cut `s[0..k-1]`, adding one cut.

**Why it is correct.** Any valid partition of `s[0..i]` ends in some palindromic
suffix `s[k..i]`; the prefix before it is itself optimally partitioned. Phase 1
answers "is `s[k..i]` a palindrome?" in `O(1)`, and phase 2 minimizes over all
valid last pieces, covering every partition.

```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True

        cut = [0] * n
        for i in range(n):
            if isPal[0][i]:
                cut[i] = 0
            else:
                best = i                       # worst case: cut before every char
                for k in range(1, i + 1):
                    if isPal[k][i]:
                        best = min(best, cut[k - 1] + 1)
                cut[i] = best
        return cut[n - 1]
```

- **Time:** `O(n^2)` — phase 1 is `O(n^2)`; phase 2 is `O(n^2)` in the worst case.
- **Space:** `O(n^2)` for the `isPal` table (`O(n)` for `cut`).

### Trace for `s = "aab"`

`isPal`: `[0][1]="aa"` True, `[0][0],[1][1],[2][2]` True, `[0][2]="aab"` False,
`[1][2]="ab"` False. Min-cut: `cut[0]=0` ("a"). `cut[1]=0` ("aa" is palindrome).
`cut[2]`: `s[0..2]` not palindrome; try `k=2` (`s[2..2]="b"` palindrome) ->
`cut[1]+1 = 1`. So the answer is `1`.

## Key Insights & Edge Cases

- The **interval DP is the engine that powers an otherwise-linear DP**. Recognizing
  that "is this substring a palindrome?" is itself an `O(n^2)` interval DP is the
  key unlock.
- Initialize `cut[i] = i` (cut before every character) as a safe upper bound so
  the `min` is always well-defined.
- **Already a palindrome** (e.g. `"aabaa"`) returns `0` immediately via the
  `isPal[0][i]` short-circuit.
- **Single character** returns `0`; a string of all identical characters also
  returns `0`.
- An alternative avoids the full `isPal` table by expanding around each of the
  `2n-1` centers while relaxing `cut`, giving `O(n^2)` time with `O(n)` space —
  but the interval-DP table is the clearest to reason about.
