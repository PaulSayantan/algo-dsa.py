# Solution — Longest Duplicate Substring

## Brute Force

Consider every pair of start positions and extend the common run; or, more
simply, put every substring in a set and track the longest one seen twice.

```python
def longestDupSubstring(s: str) -> str:
    n = len(s)
    best = ""
    for i in range(n):
        for j in range(i + 1, n):
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if k > len(best):
                best = s[i:i + k]
    return best
```

- **Time:** `O(n^3)` (pairs of starts × extension), or `O(n^2)` substrings each
  costing `O(n)` to hash if you use a set of slices — still far too slow for
  `n = 3·10^4`.
- **Space:** up to `O(n^2)`.

## Optimal Approach (Binary Search on Length + Rolling Hash)

**Monotonicity.** If some substring of length `L` repeats, its length-`(L-1)`
prefix repeats too. So `feasible(L)` = "a duplicate substring of length `L`
exists" is monotone: `True` for all `L <= ans` and `False` above. Binary search
the largest feasible `L`; the answer is any duplicate window of that length.

**Feasibility check `search(L)` with rolling hash.** Roll a length-`L`
polynomial hash across `s`. Keep a dict mapping `hash -> list of start indices`.
When a new window's hash is already present, **verify** the actual substrings
(collision guard); if they truly match, we found a duplicate of length `L` — return
its start index. Each check is `O(n)` (plus rare verification).

Rolling update (drop leading char, shift, add trailing char):

```
h = ( h·B - val(s[i-L])·B^L + val(s[i]) ) mod M
```

### Why it is correct

Equal substrings share a hash, so a genuine duplicate always produces a hash
collision in the dict — `search(L)` never misses. A *spurious* collision (different
strings, same hash) is filtered out by the character verification, so `search(L)`
never returns a false duplicate. With a correct monotone predicate, binary search
converges to the exact maximum length, and we return a real occurrence of that
length.

### Step by step

1. Map characters to integers `1..26`.
2. `lo, hi = 1, n - 1`; `res = ""`.
3. While `lo <= hi`: `mid = (lo + hi) // 2`; run `search(mid)`.
   - If it returns a start index `idx`, record `res = s[idx:idx+mid]` and search
     longer: `lo = mid + 1`.
   - Else search shorter: `hi = mid - 1`.
4. Return `res`.

```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        M, B = (1 << 61) - 1, 131          # Mersenne prime keeps collisions rare
        nums = [ord(c) - 96 for c in s]     # 'a' -> 1

        def search(L: int) -> int:
            power = pow(B, L, M)
            h = 0
            for i in range(L):
                h = (h * B + nums[i]) % M
            seen = {h: [0]}
            for i in range(L, n):
                h = (h * B - nums[i - L] * power + nums[i]) % M
                start = i - L + 1
                if h in seen:
                    for j in seen[h]:               # verify to kill collisions
                        if s[j:j + L] == s[start:start + L]:
                            return start
                    seen[h].append(start)
                else:
                    seen[h] = [start]
            return -1

        lo, hi, res = 1, n - 1, ""
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = search(mid)
            if idx != -1:
                res = s[idx:idx + mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return res
```

- **Time:** `O(n log n)` — `log n` binary-search steps, each an `O(n)` rolling
  scan. Verification is amortized negligible with a `2^61 - 1` modulus.
- **Space:** `O(n)` for the hash dict.

## Key Insights & Edge Cases

- **Binary search on the length**, not on positions. The monotone predicate is
  the whole trick that turns an `O(n^2)`-ish search into `O(n log n)`.
- **Overlaps are allowed** — `"aaaaa"` returns `"aaaa"` (starts 0 and 1 overlap).
  The dict-of-starts approach handles this naturally; do not require disjoint
  occurrences.
- **No duplicate** (`"abcd"`) → every `search(L)` for `L >= 1` fails, `res`
  stays `""`.
- **Always verify a hash hit.** With `n = 3·10^4` there are many windows; a
  single-modulus collision without verification could return a bogus (or wrong
  length) substring. A Mersenne-prime modulus plus verification (or double
  hashing) is the robust combination.
- **`hi = n - 1`**, not `n`: a length-`n` substring is the whole string and can
  only occur once, so it can never be a duplicate.
- **Any longest duplicate is acceptable** — for `"banana"`, both `"ana"` and
  `"nan"` are valid length-3 answers.
