# Solution — Shortest Palindrome

## Brute Force

The answer is `reverse(s[k:]) + s` where `k` is the length of the **longest
palindromic prefix**. The naive way to find `k` is to test each prefix.

```python
def shortestPalindrome(s: str) -> str:
    n = len(s)
    for k in range(n, 0, -1):
        if s[:k] == s[:k][::-1]:        # longest palindromic prefix
            return s[k:][::-1] + s
    return s
```

- **Time:** `O(n^2)` — up to `n` prefixes, each palindrome test `O(n)`.
- **Space:** `O(n)` for the reversed slices.

## Optimal Approach (Forward vs. Reverse Rolling Hash)

Why the longest palindromic prefix? To turn `s` into a palindrome by only
prepending, the added block must mirror the tail of `s`. The characters we
*cannot* avoid re-adding are exactly those past the longest prefix that is
already a palindrome. So find the largest `k` such that `s[0..k-1]` is a
palindrome, then answer `reverse(s[k:]) + s`.

Compute `k` in one pass with two rolling hashes over the growing prefix:

- **Forward hash** of `s[0..i]` read left→right:
  `fwd = (fwd·B + val(s[i])) mod M`.
- **Reverse hash** of the same characters read right→left, i.e. hash of
  `s[i], s[i-1], ..., s[0]`:
  `rev = (rev + val(s[i])·B^i) mod M`.

`s[0..i]` is a palindrome iff it reads the same forwards and backwards, i.e. iff
`fwd == rev`. Track the largest `i+1` where they match.

### Why it is correct

`fwd` is the polynomial value of the prefix; `rev` is the polynomial value of the
*reversed* prefix (each new character enters as the new most-significant digit,
weighted by `B^i`). Equality of the two hashes ⇒ (with high probability) the
prefix equals its own reverse ⇒ palindrome. Because a false positive would make
us pick a `k` that is too large and emit a non-palindrome, **verify the candidate
prefix** on a hash match (`s[:i+1] == s[:i+1][::-1]`) or use double hashing. The
longest verified palindromic prefix gives the provably shortest answer.

### Step by step

1. Iterate `i` from `0` to `n-1`, updating `fwd`, `rev`, and `power = B^i`.
2. Whenever `fwd == rev` (verified), record `k = i + 1`.
3. Return `s[k:][::-1] + s`.

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        M, B = (1 << 61) - 1, 131
        fwd = rev = 0
        power = 1
        k = 0
        for i, ch in enumerate(s):
            v = ord(ch) - 96                 # 'a' -> 1, keeps values nonzero
            fwd = (fwd * B + v) % M
            rev = (rev + v * power) % M
            power = (power * B) % M
            if fwd == rev and s[:i + 1] == s[:i + 1][::-1]:
                k = i + 1
        return s[k:][::-1] + s
```

- **Time:** `O(n)` for the scan (each verification only runs on a hash match; on
  typical input `O(n)` overall, and a Mersenne-prime hash makes false matches
  vanishingly rare).
- **Space:** `O(n)` for the output string; `O(1)` extra beyond it.

The textbook alternative is **KMP**: build the failure function of
`s + '#' + reverse(s)`; its last value is exactly `k`. That is `O(n)` and fully
deterministic. The hashing version is shown here because it directly exercises
the forward/reverse polynomial-hash idea.

## Key Insights & Edge Cases

- **Answer = `reverse(s[k:]) + s`** where `k` is the longest palindromic prefix
  length. Prepending fewer characters cannot fix the un-mirrored tail.
- **Empty string** → return `""` (`k = 0`, `s[0:][::-1] + "" == ""`). Handle
  gracefully; the loop simply never runs.
- **Already a palindrome** (`"aba"`) → `k = n`, nothing prepended.
- **Longest, not any, palindromic prefix.** Recording the *largest* matching
  `i+1` is what minimizes the added characters.
- **Reverse-hash weighting:** the new character must enter weighted by `B^i` (the
  current power), not by `B^0`; otherwise `rev` is not the hash of the reversed
  prefix and the palindrome test breaks.
- **Verify or double-hash** — a single small-modulus collision would prepend the
  wrong (too-short) block and return a non-palindrome.
