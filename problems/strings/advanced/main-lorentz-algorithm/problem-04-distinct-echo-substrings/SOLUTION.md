# Solution — Distinct Echo Substrings (LeetCode 1316)

## Brute Force

For every start `i` and every half length `L`, test whether `s[i:i+L]` equals
`s[i+L:i+2L]`; collect the winning substrings in a set to dedupe by content.

```python
def distinctEchoSubstrings_brute(s: str) -> int:
    n = len(s); seen = set()
    for i in range(n):
        for L in range(1, (n - i) // 2 + 1):
            if s[i:i+L] == s[i+L:i+2*L]:
                seen.add(s[i:i+2*L])
    return len(seen)
```

- **Time:** O(n²) pairs × O(n) comparison and hashing = O(n³); with a precomputed
  rolling hash the comparison drops to O(1) giving O(n²).
- **Space:** O(n²) worst case for the set of distinct substrings.

The O(n²) hashed version passes the original LeetCode limit (`n <= 2000`) but does
not scale to `10⁵`.

## Optimal Approach — Main–Lorentz Algorithm + Rolling Hash

An "echo substring" `a + a` is exactly a **square** `XX`. So the problem is:
*count distinct-by-content squares.*

Two-phase plan:

1. **Enumerate all square occurrences** with Main–Lorentz. This yields O(n log n)
   ranges `(lo, hi, l)`, each meaning "every start in `[lo, hi]` begins a square of
   length `2l`."
2. **Deduplicate by content.** Two squares are the same string iff they have the
   same length and the same characters. Precompute a **polynomial rolling hash** of
   `text`; then each square occurrence maps to the key `(2l, hash(text[start:start+2l]))`.
   Insert every occurrence's key into a hash set; the answer is the set size.

Use a strong modulus (e.g. the Mersenne prime `2⁶¹ − 1`) to make collisions
astronomically unlikely; for guaranteed correctness use a double hash (two moduli).

### Why it is correct

Main–Lorentz enumerates **all** square *occurrences* (validated exhaustively vs.
brute force). Different occurrences of the *same* string collapse because their
`(length, hash)` keys are equal, and different strings almost surely get different
keys. Therefore the set size equals the number of distinct echo substrings. On the
official examples it returns `3` for `"abcabcabc"` and `2` for `"leetcodeleetcode"`.

### Complexity

- **Enumeration:** O(n log n) ranges.
- **Deduplication:** the number of *occurrences* iterated can be Θ(n²) in the worst
  case (e.g. `"aaaa...a"`), because distinct content can still require touching many
  starts. Iterating starts within ranges is therefore O(#occurrences). If you must
  stay strictly sub-quadratic even on such inputs, combine Main–Lorentz with a
  suffix automaton / suffix array; but for the ranged-hash approach:
  - **Time:** O(n log n + #occurrences) ≈ O(n²) worst case, O(n log n) typical.
  - **Space:** O(n) for hashes + O(#distinct) for the set.

For the LeetCode constraints (`n <= 2000`) this is comfortably fast, and it
degrades gracefully far past the original limit on non-degenerate inputs.

### Reference implementation

```python
def z_function(s):
    n = len(s); z = [0]*n; l = r = 0
    for i in range(1, n):
        if i < r: z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
        if i + z[i] > r: l, r = i, i + z[i]
    return z

def _gz(z, i): return z[i] if 0 <= i < len(z) else 0

def square_ranges(S):
    out = []
    def rec(s, shift):
        n = len(s)
        if n < 2: return
        nu = n // 2; nv = n - nu
        u, v = s[:nu], s[nu:]
        rec(u, shift); rec(v, shift + nu)
        z1 = z_function(u[::-1])
        z2 = z_function(v + '#' + u)
        z3 = z_function(u[::-1] + '#' + v[::-1])
        z4 = z_function(v)
        for cntr in range(n):
            if cntr < nu:
                l = nu - cntr
                k1 = _gz(z1, nu - cntr); k2 = _gz(z2, nv + 1 + cntr); left = True
            else:
                l = cntr - nu + 1
                k1 = _gz(z3, nu + 1 + nv - 1 - (cntr - nu)); k2 = _gz(z4, (cntr - nu) + 1); left = False
            if k1 + k2 < l: continue
            lo = max(1, l - k2); hi = min(l, k1)
            if left: hi = min(hi, l - 1)
            if lo > hi: continue
            if left:
                s_lo, s_hi = shift + cntr - hi, shift + cntr - lo
            else:
                s_lo, s_hi = shift + cntr - l - hi + 1, shift + cntr - l - lo + 1
            out.append((s_lo, s_hi, l))
    rec(S, 0)
    return out

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        if n < 2:
            return 0
        B, MOD = 131, (1 << 61) - 1
        pw = [1] * (n + 1); h = [0] * (n + 1)
        for i, ch in enumerate(text):
            h[i+1] = (h[i] * B + ord(ch)) % MOD
            pw[i+1] = (pw[i] * B) % MOD
        def sub(a, b):                      # hash of text[a:b]
            return (h[b] - h[a] * pw[b-a]) % MOD
        seen = set()
        for lo, hi, l in square_ranges(text):
            for start in range(lo, hi + 1):
                seen.add((2 * l, sub(start, start + 2 * l)))
        return len(seen)
```

## Key Insights & Edge Cases

- **Echo substring == square.** Recognizing this reframes 1316 as distinct-square
  counting, which Main–Lorentz handles.
- **Dedup key must include length**, i.e. `(2l, hash)`. Two different lengths can
  share a raw rolling-hash value; pairing with length avoids that class of false
  merges.
- **Hash safety:** prefer `2⁶¹ − 1` (or a double hash) to keep collisions negligible.
- **Degenerate inputs** like `"aaaa...a"` produce many occurrences but few distinct
  strings; the set still collapses them. If even the occurrence iteration must be
  sub-quadratic, switch the dedup phase to a suffix automaton.
- **Short strings** (`n < 2`) trivially return `0`.
