# Solution — Repeated Substring Pattern

## Brute Force

The repeated block, if it exists, must have length `d` where `d` divides `n` and
`d < n`. Try every such divisor and check whether repeating the prefix of length
`d` reconstructs `s`.

```python
def repeatedSubstringPattern(s):
    n = len(s)
    for d in range(1, n // 2 + 1):
        if n % d == 0 and s[:d] * (n // d) == s:
            return True
    return False
```

- **Time:** `O(n · d(n))` where `d(n)` is the number of divisors — roughly
  `O(n·√n)` to `O(n^1.5)` in the worst case because of the string rebuilds.
- **Space:** `O(n)` for the reconstructed candidate.

## Optimal Approach — Boyer–Moore (string search)

### The reduction

Claim: `s` (length `n`) is a repetition of a shorter block **iff** `s` is a
substring of `(s + s)[1 : -1]`.

Intuition: `s + s` contains `s` at index `0` and index `n`. Chopping off the
first and last characters removes exactly those two "trivial" alignments. If `s`
still shows up somewhere at an index `1 <= i <= n - 1`, that means shifting `s`
by `i` leaves it unchanged — i.e. `s` has a period `i` with `i < n`. A string
has a period `p < n` that divides `n` exactly when it is a repetition of a block,
and one can show the smallest such period always divides `n` for a fully
periodic string, so a match here is equivalent to periodicity.

```python
def repeatedSubstringPattern(s):
    if len(s) < 2:
        return False
    doubled = (s + s)[1:-1]
    return boyer_moore_search(doubled, s) != -1
```

`boyer_moore_search(text, pattern)` is the standard right-to-left matcher using
the bad-character and good-suffix tables (see Problem 1). We only need to know
whether a match exists.

### Why it is correct

- **(⇒)** If `s = block * k` with `k >= 2`, let `d = len(block)`. Then `s`
  reappears inside `s + s` starting at index `d` (a valid index in `1..n-1`), so
  it survives the trim and Boyer–Moore finds it.
- **(⇐)** If `s` is found at index `i` (with `1 <= i <= n - 1`) inside
  `(s+s)[1:-1]`, then within `s + s` it sits at index `i` with `1 <= i < n`.
  That equality `((s+s)[i : i+n] == s)` means `s[j] == s[(j + i) mod n]` for all
  `j`, so `i` is a period of `s`. The minimal period then divides `n`, giving a
  block whose repetition equals `s`.

### Step-by-step on Example 1 (`s = "abab"`)

- `doubled = ("abab" + "abab")[1:-1] = "bababa"`.
- Boyer–Moore searches for `"abab"` in `"bababa"` and finds it at index `1`
  (`"bababa"[1:5] == "abab"`). Match exists → return `True`.

For `s = "aba"`: `doubled = ("abaaba")[1:-1] = "baab"`, which does not contain
`"aba"` → return `False`.

### Complexity

- **Preprocess `s`:** `O(n + |Σ|)`.
- **Search over the `2n - 2` length text:** `O(n · m) = O(n^2)` worst case but
  typically sublinear; best case `O(n / m)`.
- **Space:** `O(n)` for `doubled` plus `O(n + |Σ|)` for the tables.

## Key Insights & Edge Cases

- **Single character / empty** (`len(s) < 2`) cannot be a repetition of a
  *shorter* block → `False`. (Guard before slicing to avoid an empty pattern.)
- The `[1:-1]` trim is the whole trick — it deletes exactly the two boundary
  occurrences of `s` so any *remaining* occurrence certifies a real internal
  period.
- This is the same family of reductions as Rotate String (Problem 2): reshape a
  structural question into a single substring search, then let Boyer–Moore do
  the searching fast.
- A pure KMP-failure-function solution also runs in `O(n)`; the point here is
  practicing the "search in a transformed string" pattern with Boyer–Moore.
