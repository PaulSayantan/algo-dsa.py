# Solution — Count Distinct Substrings

## Brute Force

Enumerate every substring by materializing the slice and putting it in a set.

```python
def countDistinct(s: str) -> int:
    seen = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            seen.add(s[i:j])   # building the slice is O(j - i)
    return len(seen)
```

- **Time:** `O(n^3)` — there are `O(n^2)` substrings and building/hashing each
  slice costs up to `O(n)`. (Also `O(n^2)` total characters stored.)
- **Space:** `O(n^3)` worst case for all the stored substrings.

This is fine for `n <= 500` but wastes work re-hashing overlapping slices.

## Optimal Approach (Polynomial Prefix Hashing)

Build prefix hashes so the hash of any substring is `O(1)`. Enumerate all
`O(n^2)` `(l, r)` pairs, compute each substring's hash in constant time, and add
it to a set. The set's size is the number of distinct substrings.

Prefix hash and substring hash (same identities as the equality problem):

```
H[0] = 0,  H[i] = (H[i-1]*B + val(s[i-1])) mod M
sub(l, r) = (H[r+1] - H[l]*B^(r-l+1)) mod M      # hash of s[l..r]
```

### Why it is correct

Equal substrings hash to equal values, so identical strings collapse to one set
entry — exactly the dedup we want. The only risk is a **false collision** (two
different substrings sharing a hash), which would *undercount*. Guard against it:

- **Double hashing**: store the pair `(hash1, hash2)`. With two ~`10^9` primes
  the chance any of the `~n^2/2 ≈ 1.25·10^5` substrings collides is astronomically
  small.
- Alternatively, key the set by `(length, hash)` so only equal-length strings can
  ever collide, further shrinking the risk.

### Step by step

1. Pick two `(B, M)` pairs; build `H` and power arrays for each in `O(n)`.
2. For each start `l` from `0` to `n-1`, for each end `r` from `l` to `n-1`:
   add the tuple `(sub1(l,r), sub2(l,r))` to a set.
3. Return the set size.

```python
class Solution:
    def countDistinct(self, s: str) -> int:
        n = len(s)
        MODS = (1_000_000_007, 998_244_353)
        BASES = (131, 137)

        H = [[0] * (n + 1) for _ in MODS]
        PW = [[1] * (n + 1) for _ in MODS]
        for c in range(len(MODS)):
            M, B = MODS[c], BASES[c]
            for i in range(1, n + 1):
                H[c][i] = (H[c][i - 1] * B + (ord(s[i - 1]) - 96)) % M
                PW[c][i] = (PW[c][i - 1] * B) % M

        def sub(c, l, r):
            return (H[c][r + 1] - H[c][l] * PW[c][r - l + 1]) % MODS[c]

        seen = set()
        for l in range(n):
            for r in range(l, n):
                seen.add((sub(0, l, r), sub(1, l, r)))
        return len(seen)
```

- **Time:** `O(n^2)` — `O(n)` preprocessing plus `O(1)` per substring over
  `O(n^2)` substrings.
- **Space:** `O(n^2)` for the set of hashes (but only integers/tuples, not the
  strings themselves).

### Note on the truly optimal bound

A **suffix automaton** or **suffix array + LCP** counts distinct substrings in
`O(n)` / `O(n log n)` and is exact. Hashing is the fastest to *write* and is the
idiomatic choice at these constraints; for `n` up to `10^5+` you would switch to
a suffix structure.

## Key Insights & Edge Cases

- **Set of hashes, not of strings** — this is the whole point: dedup in `O(1)`
  per substring instead of `O(length)`.
- **Undercounting is the failure mode**, not overcounting: a collision merges two
  distinct strings into one entry. Double hashing / `(length, hash)` keys defend
  against it.
- **Character mapping must be nonzero** (`ord(c) - 'a' + 1`) so that leading
  characters contribute and different-length all-same strings don't collide to 0.
- **Single character / all-identical string**: `"aaa"` correctly yields `3`
  because the three distinct lengths give three distinct hashes.
- **Empty string** is excluded (only non-empty substrings are counted).
