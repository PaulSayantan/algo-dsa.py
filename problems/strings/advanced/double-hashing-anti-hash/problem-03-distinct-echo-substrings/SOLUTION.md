# Solution — Distinct Echo Substrings

## Brute Force

Enumerate every even-length substring `text[i..j]`. For each, split it in half
and compare the halves character by character; if equal, insert the substring
*string* into a `set`. Answer is the set size.

- **Time:** `O(n^3)` — `O(n^2)` substrings, each an `O(n)` half-comparison, and
  slicing the substring for the set is also `O(n)`.
- **Space:** `O(n^2)` in the worst case for stored substrings.

With `n = 2000`, `O(n^3) = 8 * 10^9` — too slow, and storing whole substrings
wastes memory.

## Optimal Approach (Double Hashing / Anti-Hash)

Two ideas make it fast:

1. **`O(1)` half comparison.** With prefix hashes, testing whether
   `text[i..i+L-1] == text[i+L..i+2L-1]` is one hash-pair comparison instead of
   `L` character comparisons.
2. **`O(1)` dedup.** Instead of storing the substring itself, store its hash
   pair `(v1, v2)` in a set. Equal echo substrings map to the same pair, so the
   set size is the number of distinct echoes.

### Prefix hash

```
pref[i+1] = (pref[i] * B + text[i]) mod M
pow[i+1]  = (pow[i]  * B) mod M
sub(l, r) = (pref[r+1] - pref[l] * pow[r-l+1]) mod M      # hash of text[l..r]
```

Maintain this for two `(B, M)` pairs.

### Enumeration

For each start `i` and each half-length `L` such that `i + 2L <= n`:

- `left  = sub(i,     i+L-1)`
- `right = sub(i+L,   i+2L-1)`
- if `left == right` on **both** moduli, the window `text[i..i+2L-1]` is an
  echo; add its full-window hash pair `sub(i, i+2L-1)` to the set.

Answer = number of distinct pairs in the set.

### Why double hashing is essential

Two separate collision risks appear here, and both cause a **wrong answer**:

- A single-modulus **false positive** on the half comparison would count a
  window as an echo when its halves differ.
- A single-modulus **collision in the dedup set** would merge two genuinely
  different echoes into one, undercounting.

Two independent `~10^9` moduli drive both probabilities to `~1/10^18`, so the
count is reliable. This is a textbook anti-hash scenario: the failure mode is
incorrectness, not merely time limits.

### Reference implementation

```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        MODS = (1_000_000_007, 998_244_353)
        BASES = (131, 137)

        pref = [[0] * (n + 1) for _ in range(2)]
        powr = [[1] * (n + 1) for _ in range(2)]
        for k in range(2):
            mod, base = MODS[k], BASES[k]
            for i in range(n):
                pref[k][i + 1] = (pref[k][i] * base + ord(text[i])) % mod
                powr[k][i + 1] = (powr[k][i] * base) % mod

        def sub(k, l, r):
            mod = MODS[k]
            return (pref[k][r + 1] - pref[k][l] * powr[k][r - l + 1]) % mod

        seen = set()
        for i in range(n):
            L = 1
            while i + 2 * L <= n:
                left = (sub(0, i, i + L - 1), sub(1, i, i + L - 1))
                right = (sub(0, i + L, i + 2 * L - 1),
                         sub(1, i + L, i + 2 * L - 1))
                if left == right:
                    seen.add((sub(0, i, i + 2 * L - 1),
                              sub(1, i, i + 2 * L - 1)))
                L += 1
        return len(seen)
```

- **Time:** `O(n^2)` — every `(i, L)` pair is `O(1)`.
- **Space:** `O(n)` for hash tables plus `O(#distinct echoes)` for the set.

## Key Insights & Edge Cases

- **Store hash pairs, not substrings**, in the dedup set — that is what turns
  the memory from `O(n^2)` characters into `O(n^2)` small tuples (and lets the
  distinct check stay `O(1)`).
- **Only even lengths** can be echoes; iterating by half-length `L` naturally
  enforces this.
- **Overlapping duplicates** (e.g. `"aaa"` -> `"aa"` twice) collapse to a single
  count because their hash pairs are identical — exactly the desired behavior.
- **`n < 2`** yields no echo; the loops simply never fire and we return `0`.
- If you want a *deterministic* answer for a contest, you can compare halves by
  hash and, only on a hash hit, confirm with a slice equality — but the double
  hash alone is safe for `n <= 2000`.
