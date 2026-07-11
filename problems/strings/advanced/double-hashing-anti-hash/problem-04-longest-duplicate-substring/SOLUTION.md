# Solution — Longest Duplicate Substring

## Brute Force

Try every length `L` from `n-1` down to `1`. For each `L`, put every length-`L`
substring into a set of *strings*; if any repeats, return it.

- **Time:** `O(n^3)` — `O(n)` lengths, `O(n)` windows per length, `O(n)` to
  build/hash each substring string.
- **Space:** `O(n^2)` for the stored substrings at a given length.

For `n = 3 * 10^4` this is far too slow.

## Optimal Approach (Binary Search on Length + Double Hashing)

### Monotonicity -> binary search

If some substring of length `L` appears twice, then its length-`(L-1)` prefix
also appears (at least) twice. So the predicate

```
P(L) = "there exist two equal substrings of length L"
```

is **monotone**: true for all lengths `<=` the answer and false above it. That
lets us **binary search** the largest `L` with `P(L)` true in `O(log n)`
predicate evaluations.

### Testing P(L) with hashing

For a fixed `L`, we need "do two windows of length `L` share the same content?"
Compute the double hash `(v1, v2)` of every window in `O(1)` using prefix
hashes, and insert each pair into a dictionary `hash_pair -> start_index`. If a
pair is already present, we found a duplicate; return its start index as a
candidate.

```
pref[i+1] = (pref[i] * B + s[i]) mod M
pow[i+1]  = (pow[i]  * B) mod M
sub(l, r) = (pref[r+1] - pref[l] * pow[r-l+1]) mod M
```

Each `P(L)` evaluation is `O(n)`, so the total is `O(n log n)`.

### Why double hashing is critical here

There are up to `~n` windows per level and `O(log n)` levels, so we perform on
the order of `n log n` hash insertions/lookups. With a single `~10^9` modulus,
the birthday-paradox collision probability across so many windows is
uncomfortably high, and a collision here makes us **claim a duplicate that does
not exist** — a wrong answer. Two independent moduli reduce the effective
collision space to `~10^18`, making a false "duplicate found" essentially
impossible. This problem is a canonical motivation for anti-hash: single-hash
submissions are known to be broken by adversarial tests.

### Steps

1. Build prefix-hash and power tables for two `(B, M)` pairs.
2. Binary search `lo = 1`, `hi = n - 1`:
   - `mid = (lo + hi + 1) // 2` (bias up so we converge on the max),
   - `start = has_dup(mid)`; if `start != -1`, record `(start, mid)` and set
     `lo = mid`; else `hi = mid - 1`.
3. Return `s[start : start + best_len]`, or `""` if no duplicate was ever found.

### Reference implementation

```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
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

        def sub(k, l, r):
            mod = MODS[k]
            return (pref[k][r + 1] - pref[k][l] * powr[k][r - l + 1]) % mod

        def has_dup(L):
            seen = {}
            for i in range(0, n - L + 1):
                key = (sub(0, i, i + L - 1), sub(1, i, i + L - 1))
                if key in seen:
                    return i
                seen[key] = i
            return -1

        best_start, best_len = 0, 0
        lo, hi = 1, n - 1
        while lo <= hi:
            mid = (lo + hi + 1) // 2
            start = has_dup(mid)
            if start != -1:
                best_start, best_len = start, mid
                lo = mid + 1
            else:
                hi = mid - 1
        return s[best_start: best_start + best_len]
```

- **Time:** `O(n log n)` — `O(log n)` predicate checks, each `O(n)`.
- **Space:** `O(n)` for hash tables plus `O(n)` for the per-level dictionary.

## Key Insights & Edge Cases

- **Bias the midpoint up** (`(lo + hi + 1)//2` with `lo = mid`, or the
  `lo <= hi` form above) so the search does not spin forever on the boundary.
- **Overlapping occurrences count** — "aaaa" inside "aaaaa" is valid; the sliding
  window naturally allows overlap.
- **No duplicate at all** (e.g. `"abcd"`): `has_dup` fails for every `L`,
  `best_len` stays `0`, and the empty-string slice `s[0:0] == ""` is returned.
- **Return the start index** from `has_dup`, not just a boolean, so the final
  substring can be sliced out without re-scanning.
- A pure single-hash solution risks both false positives (spurious "duplicate")
  here; the anti-hash pair is what makes the reported substring trustworthy.
