# Palindromic Substrings — Solution

## Brute Force

Enumerate all O(n^2) substrings and check each for being a palindrome in O(n).

- **Time:** O(n^3). **Space:** O(1).

The standard quadratic improvement is **expand around center**: for each of the
`2n - 1` centers, expand while characters match and add 1 to the count for every
successful expansion (each expansion reveals one more palindrome centered there).

- **Time:** O(n^2). **Space:** O(1).

## Optimal Approach (Manacher's Algorithm)

The key observation: a palindrome of length `L` centered at some position contains
exactly `ceil(L / 2)` palindromes sharing that same center (peel one character off
each end repeatedly). So if we know the *longest* palindrome radius at every
center, we can count all palindromes without re-expanding.

### Steps

1. **Transform:** build `t = "#" + "#".join(s) + "#"`. Every palindrome in `t` is
   odd-length and centered on an index of `t`.
2. **Run Manacher** to get `p[i]` = palindrome radius at center `i` in `t`. By the
   `#`-padding property, `p[i]` equals the *length* of the corresponding palindrome
   in `s`.
3. **Count:** a center with transformed radius `p[i]` contributes `(p[i] + 1) // 2`
   palindromic substrings in the original string. Sum this over all `i`.

Why `(p[i] + 1) // 2`? In the transformed string a palindrome of radius `p` spans
`p` real characters. The number of nested palindromes sharing that center is
`ceil(p / 2) = (p + 1) // 2`. For a letter center (odd palindromes) radius 5 gives
lengths 1, 3, 5 -> 3 palindromes; for a `#` center (even palindromes) radius 4
gives lengths 2, 4 -> 2 palindromes. The single formula `(p + 1) // 2` covers both.

### Reference implementation

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        c = r = 0
        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < n
                   and t[i - p[i] - 1] == t[i + p[i] + 1]):
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]
        return sum((v + 1) // 2 for v in p)
```

- **Time:** O(n). **Space:** O(n).

### Why it is correct

Manacher gives the exact maximal radius at each center. Because every palindromic
substring has a unique center (a letter for odd length, a gap for even length) that
coincides with exactly one index of `t`, summing the per-center counts
`(p[i] + 1) // 2` counts each palindromic substring exactly once — no double
counting, no omissions.

## Key Insights & Edge Cases

- **Each palindrome counted once:** the center-based decomposition partitions all
  palindromic substrings by their unique center, so the sum is exact.
- **The `(p + 1) // 2` bridge:** it converts a transformed radius into a real count
  and handles odd and even palindromes uniformly.
- **All-identical strings** like `"aaaa"` produce `n * (n + 1) / 2` palindromes
  (10 for n = 4); Manacher still runs in O(n) thanks to the mirror reuse.
- **Single character:** returns 1.
- **Overflow:** in Python integers are unbounded; in fixed-width languages the
  count can reach ~n^2 / 2, so use a 64-bit accumulator for large n.
