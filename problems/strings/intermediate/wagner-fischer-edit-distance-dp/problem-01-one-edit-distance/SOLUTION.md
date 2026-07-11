# Solution — One Edit Distance

## Brute Force

Run the **full Wagner–Fischer edit-distance DP** on `s` and `t`, compute the exact
Levenshtein distance `dp[n][m]`, and return `dp[n][m] == 1`.

```python
def isOneEditDistance(self, s: str, t: str) -> bool:
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m] == 1
```

- **Time:** `O(n · m)`
- **Space:** `O(n · m)` (reducible to `O(min(n, m))`)

This is correct but computes far more than the question asks — we only care whether the
distance is `1`, not its exact value when it is larger.

## Optimal Approach (Wagner–Fischer, banded / bounded)

The Wagner–Fischer recurrence tells us that moving from `dp[i-1][j-1]` costs `0` on a
match and `1` on a substitution, while an insertion or deletion moves the row/column
index by one. For the total distance to be `1`, we are allowed **at most one off-diagonal
step**. That confines every relevant cell to a band of width 1 around the main diagonal —
i.e. `|n - m| <= 1`. So the general `O(n·m)` table collapses to a single left-to-right
scan (this bounded/banded specialization of Wagner–Fischer is exactly Ukkonen's idea for
threshold-`k` distance, here with `k = 1`).

**Algorithm**

1. Let `n = len(s)`, `m = len(t)`. If `|n - m| > 1`, return `False` (need at least two
   insert/delete edits).
2. Ensure `s` is the shorter string (swap if needed) so the two cases below are symmetric.
3. Scan both strings together until the first mismatch at index `i`:
   - **Equal lengths (`n == m`):** the only allowed edit is a substitution. From the
     first mismatch onward, the remaining suffixes `s[i+1:]` and `t[i+1:]` must be
     identical. If there is **no** mismatch at all the strings are equal (distance `0`),
     so return `False`.
   - **Lengths differ by 1 (`m == n + 1`, `s` shorter):** the only allowed edit is
     inserting one character into `s`. At the first mismatch, skip one character of the
     longer string `t` and require `s[i:] == t[i+1:]`.
4. If we reach the end of the shorter string with no mismatch, the strings are one edit
   apart **iff** their lengths differ by exactly 1 (the extra trailing character is the
   single insertion/deletion).

```python
def isOneEditDistance(self, s: str, t: str) -> bool:
    n, m = len(s), len(t)
    if abs(n - m) > 1:
        return False
    if n > m:                       # make s the shorter (or equal) string
        s, t, n, m = t, s, m, n
    for i in range(n):
        if s[i] != t[i]:
            if n == m:
                return s[i + 1:] == t[i + 1:]   # substitute s[i]
            return s[i:] == t[i + 1:]           # insert t[i] into s
    # no mismatch within the shorter string:
    # one edit iff the longer string has exactly one extra trailing char
    return m == n + 1
```

- **Time:** `O(n + m)` — a single linear scan (suffix comparison is also linear).
- **Space:** `O(1)` extra (or `O(n)` if the suffix slices allocate).

**Why it is correct.** Every candidate for distance `1` keeps the alignment on the main
diagonal except for a single off-diagonal move. If lengths are equal, that move must be a
substitution at the first differing position, after which the alignment returns to the
diagonal — so the suffixes must match exactly. If lengths differ by one, the move is a
single insertion/deletion at the first mismatch, after which the shorter suffix must equal
the longer string's suffix shifted by one. Any second mismatch would force a second
off-diagonal move, i.e. distance `>= 2`.

## Key Insights & Edge Cases

- **"Exactly one," not "at most one."** Identical strings (`s == t`) have distance `0`
  and must return `False`. The `m == n + 1` check and the `s[i+1:] == t[i+1:]` (rather
  than `>=`) comparisons enforce this.
- **Length gap short-circuit.** `abs(n - m) > 1` immediately rules out any single edit.
- **Empty strings.** `("", "")` → `False` (distance 0). `("", "a")` → `True` (one
  insertion). Both fall out of the length logic naturally.
- **First mismatch dominates.** After the first differing character the remaining suffixes
  must be perfectly aligned; a naïve character-by-character equality that keeps going will
  double-count and is wrong.
- **Substitution requires a *different* character** — but that is automatic here because
  we only reach the substitution branch at a position where `s[i] != t[i]`.
