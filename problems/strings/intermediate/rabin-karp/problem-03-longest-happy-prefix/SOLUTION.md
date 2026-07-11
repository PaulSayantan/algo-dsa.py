# Solution — Longest Happy Prefix

## Brute Force

For each length `L` from `n-1` down to `1`, directly compare the prefix
`s[:L]` with the suffix `s[n-L:]`. Return the first match.

```python
def longestPrefix(s: str) -> str:
    n = len(s)
    for L in range(n - 1, 0, -1):
        if s[:L] == s[n - L:]:
            return s[:L]
    return ""
```

- **Time:** `O(n^2)` — up to `n` candidate lengths, each comparison up to `O(n)`.
  With `n = 10^5` this is far too slow.
- **Space:** `O(n)` for the transient slices.

## Optimal Approach (Rabin–Karp)

Build the prefix hash and the suffix hash **incrementally in the same pass** so
that after processing `L` characters we hold `hash(s[:L])` and `hash(s[n-L:])`,
then compare them in `O(1)`.

The trick is to make both hashes evaluate the same polynomial with the
**leftmost character as the most significant digit**:

- Extend the **prefix** on the right:
  `pref = pref * B + s[i]`
  → after `i+1` chars, `pref = s[0]·B^i + s[1]·B^(i-1) + ... + s[i]`.
- Extend the **suffix** on the left:
  `suf = suf + s[n-1-i] · B^i`
  → after `i+1` chars, `suf = s[n-1-i]·B^i + ... + s[n-1]`.

Both are the polynomial hash of a length-`(i+1)` string ordered left-to-right,
so `pref == suf` means the length-`(i+1)` prefix and suffix are (almost
certainly) equal.

### Why it is correct

Equal strings always hash equally, so every real border produces `pref == suf`.
The only risk is a collision (two different strings hashing the same). Using a
large prime modulus makes collisions negligible; for full determinism you can
verify the candidate with a direct slice comparison, or use **double hashing**
(two independent moduli) so a collision needs both hashes to clash — practically
impossible. Because we track the *largest* matching `L`, we return the longest
happy prefix.

### Step by step

1. Let `n = len(s)`, `B = 31` (or `256`), `M = 1_000_000_007`.
2. Iterate `i` from `0` to `n-2` (length `L = i+1`, staying **proper**):
   - `pref = (pref * B + ord(s[i])) % M`
   - `suf = (suf + ord(s[n-1-i]) * power) % M`
   - `power = (power * B) % M`
   - If `pref == suf`, record `best = i + 1` (a longer valid border).
3. Return `s[:best]` (empty if `best == 0`).

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        B, M = 31, 1_000_000_007
        pref = suf = 0
        power = 1
        best = 0
        for i in range(n - 1):                 # L = i + 1, keeps it proper
            pref = (pref * B + ord(s[i])) % M
            suf = (suf + ord(s[n - 1 - i]) * power) % M
            power = (power * B) % M
            if pref == suf:
                best = i + 1
        return s[:best]
```

- **Time:** `O(n)` — one pass, `O(1)` work per index.
- **Space:** `O(1)` extra (excluding the output slice).

### Relationship to KMP

The longest happy prefix is exactly the value of the last entry of the KMP
failure/prefix function, so KMP solves this in guaranteed `O(n)` with no
collision risk. Rabin–Karp is an equally linear, hashing-based alternative and a
great way to practice prefix-hash comparisons.

## Key Insights & Edge Cases

- **Proper prefix only.** Loop to `n-2` (length `≤ n-1`); never allow `L = n`,
  otherwise you would return the whole string.
- **No border → `""`.** If `best` stays `0` (e.g. `"abcdef"`), return empty.
- **Take the last match, not the first.** Overwriting `best` each time you see a
  match yields the *longest* border, since `L` increases through the loop.
- **Collision safety.** Prefer a large prime modulus; for adversarial inputs use
  double hashing or verify the winning candidate with a slice comparison.
- **Single character** (`n == 1`): the loop body never runs, `best = 0`, answer
  is `""` — correct, since a single-char string has no proper border.
