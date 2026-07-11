# Solution — Find the Index of the First Occurrence in a String

## Brute Force

For every start index `i` in `haystack` (there are `n - m + 1` of them),
compare the `m` characters of `needle` one by one.

- **Time:** `O((n - m + 1) * m)` = `O(n*m)` in the worst case (e.g.
  `haystack = "aaaa...a"`, `needle = "aaa...ab"`).
- **Space:** `O(1)`.

## Optimal Approach (Double Hashing / Rabin-Karp)

Rabin-Karp turns each length-`m` comparison into an `O(1)` hash comparison by
maintaining a **rolling hash** of the current window.

### Polynomial hash recap

Treat characters as digits in base `B`. For a string `t` of length `m`:

```
H(t) = ( t[0]*B^(m-1) + t[1]*B^(m-2) + ... + t[m-1]*B^0 ) mod M
```

(Any consistent placement of powers works; here the leftmost char carries the
highest power so that "rolling" one step right is clean.)

To slide the window from `s[i..i+m-1]` to `s[i+1..i+m]`:

```
H_new = ( (H_old - s[i]*B^(m-1)) * B + s[i+m] ) mod M
```

Remove the leaving character's contribution, shift everyone up by one power
(multiply by `B`), then add the entering character. Precompute `B^(m-1) mod M`
once.

### Why *double* hashing

A single modulus `M` has collisions: distinct windows can share a hash and
produce a false positive. Adversarial inputs (anti-hash tests) exploit exactly
this. Two independent moduli `M1`, `M2` (each `~10^9`) make a simultaneous
collision have probability `~1/10^18`, so a matching hash pair is a real match
for all practical inputs. If you want a *guaranteed* correct answer, verify with
a direct `haystack[i:i+m] == needle` comparison only when both hash components
match — that verification is `O(m)` but runs rarely.

### Steps

1. `m = len(needle)`, `n = len(haystack)`; if `m > n` return `-1`.
2. Compute `target = (h1(needle), h2(needle))` and the power `B^(m-1) mod M` for
   each modulus.
3. Compute the hash of the first window `haystack[0..m-1]`.
4. For `i` from `0` to `n - m`:
   - if the window hash pair equals `target`, return `i`;
   - otherwise roll the hash to the next window.
5. Return `-1`.

### Reference implementation

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        MODS = (1_000_000_007, 998_244_353)
        BASES = (131, 137)

        def build(mod, base):
            th = 0
            wh = 0
            for c in needle:
                th = (th * base + ord(c)) % mod
            for i in range(m):
                wh = (wh * base + ord(haystack[i])) % mod
            top = pow(base, m - 1, mod)
            return th, wh, top

        (t1, w1, top1), (t2, w2, top2) = (
            build(MODS[0], BASES[0]),
            build(MODS[1], BASES[1]),
        )

        for i in range(n - m + 1):
            if (w1, w2) == (t1, t2):
                # optional exact check: if haystack[i:i+m] == needle:
                return i
            if i + m < n:
                w1 = ((w1 - ord(haystack[i]) * top1) * BASES[0]
                      + ord(haystack[i + m])) % MODS[0]
                w2 = ((w2 - ord(haystack[i]) * top2) * BASES[1]
                      + ord(haystack[i + m])) % MODS[1]
        return -1
```

- **Time:** `O(n + m)` expected (each roll is `O(1)`; optional verification is
  rare).
- **Space:** `O(1)` extra.

## Key Insights & Edge Cases

- **Python `%` is non-negative**, so `(w - ord(c)*top)` staying negative before
  the `% mod` is fine here. In C++/Java add `mod` before taking the modulus to
  avoid negative values.
- **`m > n`** must short-circuit to `-1` before building any window.
- **`m == n`**: the loop runs once (index 0) — correct.
- **Single-character needle** works: the window is one character and no roll is
  needed.
- A **single modulus** would pass most tests but can be defeated by anti-hash
  inputs; two moduli (ideally with a randomized base per run) close that gap.
- If you truly cannot tolerate any error, the optional exact comparison on a
  hash match gives a deterministic answer while keeping the expected runtime
  linear.
