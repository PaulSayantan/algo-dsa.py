# Solution — Repeated Substring Pattern

## Brute Force

The period length `L` of the repeating block must divide `n = len(s)` and satisfy
`L < n`. For each such divisor, check whether repeating `s[0:L]` exactly `n // L` times
reproduces `s`.

```python
def repeatedSubstringPattern(s):
    n = len(s)
    for L in range(1, n // 2 + 1):     # candidate block lengths
        if n % L == 0:                 # must tile evenly
            if s[:L] * (n // L) == s:  # build and compare
                return True
    return False
```

- **Time:** `O(n · d(n))` where `d(n)` is the number of divisors of `n`; building/
  comparing each candidate is `O(n)`. Loosely `O(n · sqrt(n))` in the worst case.
- **Space:** `O(n)` to build `s[:L] * (n // L)`.

## Optimal Approach (Naive Pattern Matching)

**The reduction.** Consider `doubled = s + s`. Cutting off the first and last character
gives `mid = (s + s)[1:-1]`, a string of length `2n - 2`. Claim: **`s` is a repeated
substring pattern iff `s` occurs inside `mid`.**

Intuition: `s + s` obviously contains `s` at index `0` and index `n`. Chopping one
character from each end destroys those two "trivial" copies. If any *other* copy of `s`
survives, it starts at some index `1 <= k <= n - 1`, which means shifting `s` by `k`
leaves it unchanged — i.e. `s` has a period `k` that divides `n`, so `s` is a repetition
of its length-`k` prefix. If `s` is *not* periodic, the only copies of `s` in `s + s`
are the two trivial ones, and both are removed, so the search fails.

We run that substring search with naive matching:

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        mid = (s + s)[1:-1]            # length 2n - 2
        n, m = len(mid), len(s)
        for start in range(n - m + 1):
            j = 0
            while j < m and mid[start + j] == s[j]:
                j += 1
            if j == m:
                return True
        return False
```

**Step-by-step** on `s = "abab"` (`n = 4`): `s + s = "abababab"`, `mid = "ababab"`
(length 6). Search for `"abab"` in `"ababab"`: alignment `start = 0` matches
`mid[0:4] = "abab"` -> return `True`. For `s = "aba"`: `s + s = "abaaba"`,
`mid = "baab"`; searching `"aba"` in `"baab"` finds no match -> `False`.

- **Time:** `O(n · m)` worst case where `m = n` and `mid` length is about `2n`, so
  `O(n^2)`; near-linear on typical inputs due to early mismatch exit.
- **Space:** `O(n)` for the `mid` string.

### Direct alternative (also naive matching)

Instead of the reduction, verify a candidate block tiles `s` by comparing
`s[i] == s[i % L]` for all `i` — a naive character-by-character sweep:

```python
def repeatedSubstringPattern(self, s):
    n = len(s)
    for L in range(1, n // 2 + 1):
        if n % L == 0:
            if all(s[i] == s[i % L] for i in range(n)):
                return True
    return False
```

## Key Insights & Edge Cases

- **Why trim exactly one char from each end.** Removing one character kills the copy of
  `s` that starts at index `0` (its last character is gone) and the copy that starts at
  index `n` (its first character is gone), while preserving any genuinely periodic copy.
- **Length 1 strings** like `s = "a"`: `mid = ""`, the search range is empty, return
  `False` — correct, since a single character can't be a repetition of a *shorter*
  substring.
- **Divisibility is essential** in the direct approach: only block lengths dividing `n`
  can tile `s`, so skip non-divisors.
- Replacing the naive search with KMP's failure function gives the well-known `O(n)`
  solution, but the `(s + s)[1:-1]` reduction is identical.
