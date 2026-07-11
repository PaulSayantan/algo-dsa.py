# Solution — Distinct Echo Substrings

## Brute Force

Enumerate every even-length substring `text[i:i+2L]`, split it in half, and
compare the halves directly. Deduplicate the winners with a set of *strings*.

```python
def distinctEchoSubstrings(text: str) -> int:
    n = len(text)
    seen = set()
    for i in range(n):
        for L in range(1, (n - i) // 2 + 1):
            left = text[i:i + L]
            right = text[i + L:i + 2 * L]
            if left == right:
                seen.add(left + right)
    return len(seen)
```

- **Time:** `O(n^3)` — `O(n^2)` (start, half-length) pairs, each comparison
  costs `O(L) = O(n)`. With `n = 2000` this is ~8·10^9 char operations: too slow.
- **Space:** `O(n^2)` worst case for the stored substrings (each up to `O(n)`).

## Optimal Approach (Rabin–Karp)

Precompute **prefix hashes** so that the polynomial hash of any substring
`text[l:r]` can be read in `O(1)`. Then for each start `i` and half-length `L`,
compare `hash(text[i:i+L])` with `hash(text[i+L:i+2L])` in `O(1)`. Confirmed
echoes are deduplicated by inserting their hash (ideally a pair of hashes under
two moduli) into a set.

### Prefix-hash formula

Let `h[k]` be the hash of `text[:k]` with `h[k] = h[k-1]·B + text[k-1]`, and let
`pow[k] = B^k mod M`. Then the hash of `text[l:r]` (0-indexed, half-open) is:

```
sub(l, r) = ( h[r] - h[l] * pow[r - l] ) mod M
```

This is the standard "prefix minus scaled prefix" substring-hash identity.

### Why it is correct

`left == right` implies `sub(i, i+L) == sub(i+L, i+2L)`, so we never miss a real
echo. The reverse can fail only on a hash collision. Two defenses keep it exact:

- **Verify** each hash-equal candidate with a direct slice comparison
  (`text[i:i+L] == text[i+L:i+2L]`). Over the whole run the number of true
  echoes is `O(n^2)` and verification adds at most `O(n)` each, which is fine
  for `n ≤ 2000`; false-positive verifications are astronomically rare.
- Or use **double hashing** (two independent `(B, M)` pairs) and treat the pair
  of hashes as the identity — collisions then require a simultaneous clash in
  both, which is effectively impossible.

For distinctness, key the set by the substring's hash (or hash pair, or the
substring itself since `n` is small), so each unique echo is counted once even
if it occurs at several positions (Example 3: `"aa"`).

### Step by step

1. Build `h[0..n]` and `pow[0..n]` for a chosen `(B, M)` (use two pairs for
   safety).
2. For each start `i` from `0` to `n-1`:
   - For each half-length `L` from `1` while `i + 2L <= n`:
     - If `sub(i, i+L) == sub(i+L, i+2L)` (both moduli), the window is an echo.
     - Add its identity (e.g. `(sub_left_mod1, sub_left_mod2, L)`, or the
       substring) to a set.
3. Return the size of the set.

```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        B, M = 131, (1 << 61) - 1          # large prime modulus
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        for k in range(n):
            h[k + 1] = (h[k] * B + ord(text[k])) % M
            p[k + 1] = (p[k] * B) % M

        def sub(l: int, r: int) -> int:    # hash of text[l:r]
            return (h[r] - h[l] * p[r - l]) % M

        seen = set()
        for i in range(n):
            L = 1
            while i + 2 * L <= n:
                left = sub(i, i + L)
                right = sub(i + L, i + 2 * L)
                if left == right:          # candidate echo of half-length L
                    seen.add((left, i + 2 * L - i))  # (hash, total length) key
                L += 1
        return len(seen)
```

Because two equal halves have identical `left` hash, keying by
`(hash_of_left, full_length)` uniquely identifies the echo substring; with a
`(1<<61)-1` modulus, distinct substrings essentially never collide. For a
100%-deterministic solution, verify with a slice compare before inserting.

- **Time:** `O(n^2)` expected — `O(n^2)` `(i, L)` pairs, each handled in `O(1)`
  hash lookups. Verification (if used) adds negligible amortized cost.
- **Space:** `O(n)` for the hash/power arrays plus `O(#echoes)` for the set.

## Key Insights & Edge Cases

- **Only even lengths can echo.** Iterate half-length `L` and require
  `i + 2L <= n`.
- **Distinct, not total.** Store an identity in a set; `"aa"` appearing twice in
  `"aaa"` counts once (Example 3).
- **Prefix hashes turn each half-comparison into `O(1)`**, dropping the naive
  `O(n^3)` to `O(n^2)` — the crux of fitting `n = 2000`.
- **Guard the substring identity.** Keying only by the left-half hash without
  the length could merge different-length echoes; include the length (or the
  full-length hash) in the key.
- **Collision hardening.** Use a large prime (e.g. `(1<<61)-1`) or double
  hashing; optionally verify hash matches with a direct comparison for
  determinism.
