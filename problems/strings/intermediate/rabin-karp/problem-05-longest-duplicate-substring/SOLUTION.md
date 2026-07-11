# Solution — Longest Duplicate Substring

## Brute Force

Try every length `L` from `n-1` down to `1`; for each, collect all length-`L`
substrings in a set and stop when one repeats.

```python
def longestDupSubstring(s: str) -> str:
    n = len(s)
    for L in range(n - 1, 0, -1):
        seen = set()
        for i in range(n - L + 1):
            sub = s[i:i + L]          # O(L) to build and hash
            if sub in seen:
                return sub
            seen.add(sub)
    return ""
```

- **Time:** `O(n^3)` — `O(n)` lengths × `O(n)` windows × `O(n)` to build/hash
  each substring. With `n = 3·10^4` this is hopeless.
- **Space:** `O(n^2)` for the stored substrings at a given length.

Two independent improvements combine to fix this: (1) **binary search** the
length instead of scanning it linearly, and (2) make the per-length test `O(n)`
with a **rolling hash** instead of `O(n·L)`.

## Optimal Approach (Binary Search + Rabin–Karp)

### Monotonicity → binary search

If a substring of length `L` occurs twice, so does any length-`(L-1)` prefix of
it. Thus "a duplicate of length `L` exists" is **monotone** in `L`: true for all
`L ≤ answer` and false above. Binary search the smallest length that is *not*
achievable; the answer is one below it. This replaces the `O(n)` outer loop with
`O(log n)` iterations.

### The `O(n)` feasibility test (Rabin–Karp)

For a fixed `L`, compute the rolling hash of each length-`L` window in `O(1)`
per shift, and keep a dictionary mapping `hash → list of start indices` (or
`hash → one start index`). If a hash repeats, verify the two windows are truly
equal (guarding against collisions); if equal, we found a duplicate of length
`L` and return its start index.

### Why it is correct

- **Completeness:** equal windows always share a hash, so a real duplicate is
  never missed.
- **Soundness:** a hash collision could suggest a false duplicate, so we verify
  candidates by comparing the actual substrings (or use **double hashing** so a
  false positive needs both moduli to collide — effectively impossible). Thus
  `search(L)` returns a start index only for a genuine duplicate.
- Binary search over a monotone predicate returns the exact maximum length, and
  we return the substring found at that length.

### Step by step

1. Encode `s` to integers `nums[i] = ord(s[i]) - ord('a')` over base `B = 26`
   (or larger) and a large prime `M`.
2. `search(L)`: precompute `high = B^(L-1) mod M` (the weight of the leading
   character); hash the first window; roll
   across all `n - L + 1` windows, storing `hash → start`. On a hash hit,
   verify with a slice compare; return the start on success, else `-1`.
3. Binary search `lo = 1`, `hi = n - 1`. While `lo <= hi`, test `mid`; if
   `search(mid) != -1`, record the start and set `lo = mid + 1`, else
   `hi = mid - 1`.
4. Return the recorded best substring (empty if none).

```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - ord("a") for c in s]
        B, M = 26, (1 << 61) - 1

        def search(L: int) -> int:
            if L == 0:
                return 0
            high = pow(B, L - 1, M)   # weight of the leading character
            h = 0
            for i in range(L):
                h = (h * B + nums[i]) % M
            seen = {h: [0]}
            for i in range(1, n - L + 1):
                h = ((h - nums[i - 1] * high) * B + nums[i + L - 1]) % M
                if h in seen:
                    # verify to defeat collisions
                    for j in seen[h]:
                        if s[j:j + L] == s[i:i + L]:
                            return i
                    seen[h].append(i)
                else:
                    seen[h] = [i]
            return -1

        lo, hi = 1, n - 1
        start, length = -1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            pos = search(mid)
            if pos != -1:
                start, length = pos, mid
                lo = mid + 1
            else:
                hi = mid - 1
        return s[start:start + length] if start != -1 else ""
```

- **Time:** `O(n log n)` expected — `O(log n)` binary-search steps, each an
  `O(n)` rolling-hash scan. (Verification is rare with a large prime; with
  double hashing it can be skipped for practical purposes.)
- **Space:** `O(n)` for the hash-to-index map.

## Key Insights & Edge Cases

- **Two orthogonal ideas.** Binary search collapses the length dimension to
  `log n`; the rolling hash collapses the per-length test to `O(n)`. Either
  alone is not enough.
- **No duplicate → `""`.** `search` returns `-1` for every length (e.g.
  `"abcd"`), so `start` stays `-1`.
- **Overlaps are allowed.** `"aaaaa"` → `"aaaa"` at indices 0 and 1;
  `"banana"` → `"ana"` at indices 1 and 3. The window scan naturally permits
  overlapping matches.
- **Verify or double-hash.** A single modulus with no verification is
  Monte-Carlo and can return a wrong (colliding) substring. Verify candidates,
  or hash under two independent moduli.
- **Modulus choice.** `(1<<61)-1` is a Mersenne prime that fits in 64-bit
  arithmetic and gives an extremely low collision rate; `1_000_000_007` also
  works if you verify.
- **Correct rolling order.** Remove the outgoing character `nums[i-1]` scaled by
  `B^(L-1)` *before* multiplying by `B` and adding the incoming `nums[i+L-1]`.
  Using `B^L` here is a classic off-by-one that silently corrupts every rolled
  hash.
