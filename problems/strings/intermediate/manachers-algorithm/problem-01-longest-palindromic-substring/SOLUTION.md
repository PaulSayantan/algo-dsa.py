# Longest Palindromic Substring — Solution

## Brute Force

Enumerate every substring `s[i..j]` and check whether it is a palindrome, keeping
the longest one seen.

- Number of substrings: O(n^2). Each palindrome check is O(n).
- **Time:** O(n^3). **Space:** O(1).

A better O(n^2) baseline is **expand around center**: for each of the `2n - 1`
centers (n single-character centers and n-1 between-character centers), expand
outward while the characters match. This removes the redundant palindrome check.

- **Time:** O(n^2). **Space:** O(1).

Dynamic programming (`dp[i][j] = s[i]==s[j] and dp[i+1][j-1]`) is also O(n^2) time
but O(n^2) space, so expand-around-center is usually preferred among the quadratic
options.

## Optimal Approach (Manacher's Algorithm)

Manacher's Algorithm turns expand-around-center into O(n) by **reusing** the
palindrome information already computed.

### Step 1 — Transform the string

Even-length palindromes have their "center" between two characters, which is
awkward. Fix this by interposing a separator that never appears in `s`:

```
s = "abba"   ->   t = "#a#b#b#a#"
```

Now `t` always has odd length `2n + 1`, and **every** palindrome in `t` is
odd-length and centered on an actual index of `t`. A `#` center corresponds to an
even palindrome in `s`; a letter center corresponds to an odd palindrome in `s`.

### Step 2 — Compute radii with the mirror trick

Maintain `p[i]` = radius (number of characters on each side, in `t`) of the
longest palindrome centered at `i`. Track the palindrome currently reaching
farthest right: its center `c` and right boundary `r = c + p[c]`.

For each `i`:

1. If `i < r`, its mirror is `mir = 2*c - i`. We may copy the mirror's radius, but
   only up to the right boundary: `p[i] = min(r - i, p[mir])`.
2. Attempt to expand further: while `t[i - p[i] - 1] == t[i + p[i] + 1]`,
   increment `p[i]`.
3. If `i + p[i] > r`, update `c = i`, `r = i + p[i]`.

Because `r` only ever moves forward and each expansion step advances it, the total
expansion work over all `i` is O(n).

### Step 3 — Read the answer

`p[i]` in the transformed string equals the **length** of the corresponding
palindrome in the original string. The palindrome in `s` starts at
`(i - p[i]) // 2`. Take the `i` with the maximum `p[i]`.

### Reference implementation

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
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
        best_len = max(p)
        center = p.index(best_len)
        start = (center - best_len) // 2
        return s[start:start + best_len]
```

- **Time:** O(n). **Space:** O(n) for `t` and `p`.

### Why it is correct

The mirror step never claims a palindrome longer than what is provable "for free":
if the mirror palindrome stays strictly inside the current right boundary, symmetry
guarantees the same palindrome at `i`; if it would reach or cross the boundary, we
cap at `r - i` and re-verify by explicit expansion. Thus `p[i]` is always exactly
the true radius, and the maximum radius gives a genuine longest palindrome.

## Key Insights & Edge Cases

- **Separator choice:** any character not in `s` works; the leading and trailing
  `#` remove all boundary special-casing so `i - p[i] - 1` and `i + p[i] + 1` never
  need explicit bounds guards beyond the array ends.
- **Index mapping:** in the transformed string, `p[i]` is simultaneously the radius
  in `t` and the palindrome *length* in `s` — a convenient coincidence of the `#`
  padding. The original start index is `(i - p[i]) // 2`.
- **Single character / all identical:** `"a"` returns `"a"`; `"aaaa"` returns
  `"aaaa"` — the mirror trick handles the long run without quadratic blowup.
- **Empty string:** guard up front and return `""`.
- **Ties:** any maximal palindrome is acceptable; `p.index(best_len)` returns the
  leftmost, which is fine.
