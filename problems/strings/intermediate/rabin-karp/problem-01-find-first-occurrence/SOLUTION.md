# Solution — Find the Index of the First Occurrence in a String

## Brute Force

For every start index `i` in `haystack` (from `0` to `n - m`), compare the
`m`-character slice `haystack[i:i+m]` against `needle`.

```python
def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1
```

- **Time:** `O(n·m)` — up to `n - m + 1` windows, each compared in up to `m`
  character operations. Worst case is patterns like `haystack = "aaaa...a"`,
  `needle = "aaa...b"`.
- **Space:** `O(1)` extra (the slice is `O(m)` but transient).

## Optimal Approach (Rabin–Karp)

Represent each length-`m` window as a base-`B` number modulo a large prime `M`
(a **polynomial hash**). Compute the pattern's hash once, then roll the window
hash across the text in `O(1)` per shift.

### Why it is correct

If two strings are equal, their hashes are equal, so a true occurrence will
*always* produce a hash match. The converse can fail — different strings may
hash to the same value (a **collision**) — so every hash match is only a
*candidate* and must be verified character-by-character. Verification guarantees
we never report a false positive, so the algorithm is exactly correct. With a
large prime `M` (e.g. `1_000_000_007`) and a base like `256` or a random value,
collisions are rare, so verification runs seldom and the expected work stays
linear.

### Step by step

1. Handle the trivial case: if `needle` is empty, return `0`. If
   `m > n`, return `-1`.
2. Precompute `high = B^(m-1) mod M`, the weight of the leading character.
3. Compute `pattern_hash` (hash of `needle`) and `window_hash` (hash of the
   first window `haystack[0:m]`).
4. Slide the window from `i = 0` to `n - m`:
   - If `window_hash == pattern_hash`, verify `haystack[i:i+m] == needle`; if it
     matches, return `i`.
   - Roll to the next window:
     `window_hash = ((window_hash - ord(haystack[i]) * high) * B + ord(haystack[i+m])) mod M`.
5. If no window matches, return `-1`.

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        B, M = 256, 1_000_000_007
        high = pow(B, m - 1, M)

        pattern_hash = 0
        window_hash = 0
        for i in range(m):
            pattern_hash = (pattern_hash * B + ord(needle[i])) % M
            window_hash = (window_hash * B + ord(haystack[i])) % M

        for i in range(n - m + 1):
            if window_hash == pattern_hash and haystack[i:i + m] == needle:
                return i
            if i < n - m:
                window_hash = (
                    (window_hash - ord(haystack[i]) * high) * B
                    + ord(haystack[i + m])
                ) % M
        return -1
```

Python's `%` already returns a non-negative result for a positive modulus, so
the subtraction `window_hash - ord(...) * high` cannot leave us with a bad
negative hash after `% M`.

- **Time:** expected `O(n + m)`. Worst case `O(n·m)` only if hashes collide on
  nearly every window (extremely unlikely with a good prime/base).
- **Space:** `O(1)` extra.

## Key Insights & Edge Cases

- **Empty needle → 0.** Guard this before any hashing.
- **`m > n` → -1.** No window exists.
- **Always verify on a hash hit.** Skipping verification turns the algorithm
  into a Monte-Carlo method that can return a wrong index on a collision.
- **Choose `M` large and prime.** A small modulus produces frequent collisions
  and degrades to `O(n·m)`.
- **Rolling update pitfall:** subtract the *leading* character's contribution
  (weighted by `B^(m-1)`) before multiplying by `B` and adding the new trailing
  character. Getting the weight or the order wrong silently breaks the hash.
- For this problem KMP or Python's built-in `str.find` also work; Rabin–Karp is
  the natural choice when you later generalize to *many* patterns at once.
