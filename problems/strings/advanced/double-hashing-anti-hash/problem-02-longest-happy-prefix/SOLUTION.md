# Solution — Longest Happy Prefix

## Brute Force

For each length `L` from `n-1` down to `1`, check whether `s[0:L] == s[n-L:n]`
by comparing characters. Return the first `L` that matches.

- **Time:** `O(n^2)` — up to `n` candidate lengths, each an `O(n)` comparison.
- **Space:** `O(1)` (excluding the returned slice).

For `n` up to `10^5` this is `~10^10` operations in the worst case (e.g.
`"aaaa...a"`), which is too slow.

## Optimal Approach (Double Hashing / Anti-Hash)

Precompute **prefix hashes** so that the hash of any substring is available in
`O(1)`. Then comparing a length-`L` prefix with a length-`L` suffix becomes a
single `O(1)` hash-pair comparison, giving an overall `O(n)` scan.

### Prefix hash setup

Define, for a single modulus `M` and base `B` (indexing `s[0..n-1]`):

```
pref[0] = 0
pref[i+1] = (pref[i] * B + s[i]) mod M
pow[0] = 1
pow[i+1] = (pow[i] * B) mod M
```

Then the hash of `s[l..r]` (inclusive) is:

```
sub(l, r) = ( pref[r+1] - pref[l] * pow[r-l+1] ) mod M
```

Do this for two independent `(B, M)` pairs and combine the results into a
tuple `(v1, v2)`.

### Why two moduli here

The prefix and suffix can **overlap** (e.g. `"ababab"` -> `"abab"`), and there
are up to `n` candidate lengths. A single-modulus collision would return a
prefix that is not actually a suffix — a wrong answer, not just slowness. With
two `~10^9` moduli the false-match probability is `~1/10^18` per comparison, so
the longest matching `L` is genuinely a happy prefix.

### Steps

1. Build `pref1/pow1` (modulus `M1`, base `B1`) and `pref2/pow2` (`M2`, `B2`).
2. For `L` from `n-1` down to `1`:
   - `a = sub(0, L-1)` — the prefix of length `L`;
   - `b = sub(n-L, n-1)` — the suffix of length `L`;
   - if `a == b` on both moduli, return `s[:L]`.
3. Return `""`.

### Reference implementation

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        MODS = (1_000_000_007, 998_244_353)
        BASES = (131, 137)

        pref = [[0] * (n + 1) for _ in range(2)]
        powr = [[1] * (n + 1) for _ in range(2)]
        for k in range(2):
            mod, base = MODS[k], BASES[k]
            for i in range(n):
                pref[k][i + 1] = (pref[k][i] * base + ord(s[i])) % mod
                powr[k][i + 1] = (powr[k][i] * base) % mod

        def sub(k, l, r):  # hash of s[l..r] inclusive
            mod = MODS[k]
            return (pref[k][r + 1] - pref[k][l] * powr[k][r - l + 1]) % mod

        for L in range(n - 1, 0, -1):
            pre = (sub(0, 0, L - 1), sub(1, 0, L - 1))
            suf = (sub(0, n - L, n - 1), sub(1, n - L, n - 1))
            if pre == suf:
                return s[:L]
        return ""
```

- **Time:** `O(n)` to build tables + `O(n)` scan (each step `O(1)`).
- **Space:** `O(n)` for the prefix and power arrays.

## Key Insights & Edge Cases

- **Scan from long to short** so the first match is automatically the *longest*
  happy prefix — no need to track a maximum.
- **Overlap is allowed**: prefix and suffix may share characters in `s`, which
  is exactly why `"ababab"` yields `"abab"` (length 4 for `n = 6`).
- **`n == 1`**: the loop range is empty, so we correctly return `""`.
- **No happy prefix** (e.g. `"abcdef"`): fall through to `""`.
- KMP's failure function solves this in `O(n)` deterministically; hashing is the
  chosen practice technique here, and the anti-hash (two moduli) guard keeps it
  correct against adversarial strings.
- In non-Python languages, add `mod` before the final `%` in `sub` to keep the
  intermediate value non-negative.
