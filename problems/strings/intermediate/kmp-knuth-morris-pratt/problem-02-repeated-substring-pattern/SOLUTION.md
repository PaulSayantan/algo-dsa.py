# Solution — Repeated Substring Pattern

## Brute Force

Any repeating block must have length `L` that divides `n`, and `L < n`. Try
every such divisor length, take the prefix of that length, and check whether
repeating it reconstructs `s`.

```python
def repeatedSubstringPattern(s):
    n = len(s)
    for L in range(1, n // 2 + 1):
        if n % L == 0:
            block = s[:L]
            if block * (n // L) == s:
                return True
    return False
```

- **Time:** `O(n * d)` where `d` is the number of divisors; each rebuild+compare
  is `O(n)`, so worst case is roughly `O(n * sqrt(n))` — fine for `n <= 10^4`
  but not linear.
- **Space:** `O(n)` for the rebuilt candidate string.

A slick one-liner also exists: `s` is periodic iff `s` appears in
`(s + s)[1:-1]`. That is elegant but relies on Python's substring search, which
is itself often KMP-like under the hood; below is the explicit KMP argument.

## Optimal Approach — KMP period property

Build the LPS array of the **entire** string `s`. Let `k = lps[n-1]` be the
length of the longest proper prefix of `s` that is also a suffix of `s`.

Define the **candidate period** `p = n - k`. The key theorem:

> `s` is a concatenation of a strictly shorter block **iff** `k > 0` and
> `n % p == 0` (equivalently `n % (n - k) == 0`).

When that holds, `p` is the length of the smallest repeating block and the
block is `s[:p]`.

```python
def build_lps(p):
    m = len(p)
    lps = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and p[i] != p[k]:
            k = lps[k - 1]
        if p[i] == p[k]:
            k += 1
        lps[i] = k
    return lps

def repeatedSubstringPattern(s):
    n = len(s)
    lps = build_lps(s)
    k = lps[n - 1]
    return k > 0 and n % (n - k) == 0
```

### Why it is correct

`lps[n-1] = k` means the length-`k` prefix equals the length-`k` suffix. Shifting
`s` right by `p = n - k` positions lines it up with itself over the overlapping
`k` characters, which forces `s[i] == s[i-p]` for every `i >= p`. That is exactly
the statement "`s` has period `p`." A string with period `p` is a repetition of
its length-`p` prefix **exactly when `p` divides `n`** (otherwise the last block
is truncated and `s` is not a clean repetition). Since `k > 0` guarantees
`p < n`, the block is strictly shorter, giving at least two copies.

Trace `s = "abcabcabcabc"`, `n = 12`: `lps[n-1] = 9`, so `p = 12 - 9 = 3`, and
`12 % 3 == 0` → `True`, block `"abc"`.

Trace `s = "aba"`, `n = 3`: `lps = [0,0,1]`, `k = 1`, `p = 2`, `3 % 2 != 0`
→ `False`.

### Complexity

- **Time:** `O(n)` to build LPS, `O(1)` for the divisibility check → **O(n)**.
- **Space:** `O(n)` for the LPS array.

## Key Insights & Edge Cases

- **`k > 0` guard is required.** For a string with no repetition (e.g. `"abc"`,
  `lps[n-1] = 0`), `p = n`, and `n % n == 0` would wrongly say `True`. Requiring
  `k > 0` (equivalently `p < n`) rejects it.
- **Single character (`n = 1`)** → `lps[0] = 0`, `k = 0` → `False`, correct.
- **Smallest vs. any block.** The theorem gives the *smallest* period. Any valid
  repeating block length is a multiple of `p` that divides `n`, but you only
  need existence, so testing the smallest period suffices.
- This LPS-period trick generalizes: `n - lps[n-1]` is *the* number to remember
  whenever a problem asks about periodicity or "smallest repeating unit".
